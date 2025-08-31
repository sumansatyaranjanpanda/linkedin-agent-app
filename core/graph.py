from langgraph.graph import StateGraph, START, END


from core.schema import State
from core.node import trending_news_finder,summerize1,generate,improve_summary,check_summary,route_on_review

graph = StateGraph(State)
graph.add_node("trending_news_finder", trending_news_finder)
graph.add_node("summerize1", summerize1)
graph.add_node("generate", generate)
graph.add_node("improve_summary", improve_summary)
graph.add_node("check_summary", check_summary)


graph.add_edge(START, "trending_news_finder")
graph.add_edge("trending_news_finder", "summerize1")
graph.add_edge("summerize1",'check_summary')
graph.add_conditional_edges('check_summary',route_on_review,{'pass':'generate','fail':'improve_summary'})
graph.add_edge("improve_summary", "generate")
graph.add_edge("generate", END)

# Compile the graph
compiled_graph = graph.compile()