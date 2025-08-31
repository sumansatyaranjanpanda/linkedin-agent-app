
import json

from core.clients import llm,tavily
from core.schema import State,_strip_think



def trending_news_finder(state: State):
    query = f"find the top hot and trending news on {state['industry']}"
    results = tavily.run(query)
    return {"trending_news": results or []}

def summerize1(state: State):
    data = state.get("trending_news", [])
    if not data:
        return {"summarize": "No results found. Broaden the query or change industry."}
    prompt = (
        "You are given items with 'url', 'content', and 'score'. "
        "Do browse urls. Use browse data and the provided 'content'. "
        "Aggregate key facts by theme and produce a structured brief:\n"
        "HEADINGS -> Subheadings -> 2-4 bullets each. Be concise, non-repetitive.\n\n"
        f"DATA:\n{data}"
    )
    res = llm.invoke(prompt)
    cleaned = _strip_think(res.content)
    return {"summarize": cleaned}


def generate(state: State):
    prompt = (
        "You are a professional LinkedIn content creator.\n"
        "Your task: turn the provided industry summary into a polished LinkedIn post.\n\n"
        "Requirements:\n"
        "- Start with a catchy HOOK (1–2 lines) that grabs attention.\n"
        "- Use 2–4 short paragraphs with clear insights from the summary.\n"
        "- Add emojis where they naturally enhance readability (not excessive).\n"
        "- Include 3–5 relevant hashtags at the end (#RenewableEnergy, #EV, etc.).\n"
        "- Keep it professional, engaging, and easy to skim.\n"
        "-  length: ~500 words.\n\n"
        f"SUMMARY:\n{state['summarize']}\n\n"
        "Return only the final LinkedIn post text."
    )
    msg = llm.invoke(prompt)
    return {"generator": _strip_think(msg.content)}




def check_summary(state: State):
    prompt = (
        "You are an expert reviewer.\n"
        "Evaluate the summary for: relevance to topic, recency alignment, "
        "user engagement, professional tone.\n"
        "Return STRICT JSON exactly like:\n"
        '{"result":"1" or "0", "feedback":"<actionable feedback>"}\n\n'
        f"TOPIC: {state['industry']}\n"
        f"SUMMARY:\n{state['summarize']}\n"
    )
    res = llm.invoke(prompt)
    text = _strip_think(res.content).strip()

    # Robust JSON parse
    result = {"result":"0","feedback":"Could not parse reviewer response."}
    try:
        result = json.loads(text)
    except Exception:
        # light fallback: try to find digits
        if "result" in text and "1" in text:
            result["result"] = "1"
        if "feedback" in text:
            # naive slice; you can improve later
            result["feedback"] = text

    review_result = "pass" if result.get("result") == "1" else "fail"


    return {
        "review_result": review_result,
        "review_feedback": result.get("feedback","")
    }



def improve_summary(state: State):

    res = llm.invoke(
        f"Improve this summary for engagement and clarity, "
        f"... based on this feedback:\n{state['review_feedback']}\n\nOriginal:\n{state['summarize']}"
    )
    return {"summarize": _strip_think(res.content)}

def route_on_review(state: State) -> str:
    return state.get("review_result",'fail')