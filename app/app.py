import streamlit as st
from core.graph import compiled_graph





st.set_page_config(page_title="Agentic AI LinkedIn Post Generator", page_icon="⚡", layout="wide")

st.title("⚡ LinkedIn Post Generator")
st.markdown("LinkedIn-ready posts with an agentic workflow.")


# Sidebar inputs
industry = st.sidebar.text_input("Topic to Generate Post", "Renewable Energy")
run_button = st.sidebar.button("Generate")

#graph_png = compiled_graph.get_graph().draw_mermaid_png()
#st.sidebar.image(graph_png, caption="Workflow Graph", use_column_width=True)

if run_button:
    with st.spinner("Running agent workflow..."):
        state = {"industry": industry}
        result = compiled_graph.invoke(state)

        st.subheader("✅ Final LinkedIn Post")
        st.markdown(result["generator"])

        with st.expander("📝 Summarized News"):
            st.markdown(result["summarize"])

        with st.expander("📊 Raw Trending News Data"):
            st.json(result["trending_news"])

        if "review_feedback" in result:
            with st.expander("🔍 Reviewer Feedback"):
                st.write(result["review_feedback"])