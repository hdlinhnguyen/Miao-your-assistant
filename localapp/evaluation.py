### CONTEXT PRECISION EVALUATION:
from ragas.metrics import context_precision
# Define context precision chain
context_precision_chain = EvaluatorChain(metric=context_precision, llm=watsonx_llm, embeddings=watsonx_embeddings)
# Evaluate the context precision of the RAG chain
eval_result = context_precision_chain({
  "question": "How does RAG enable AI applications?",
  "ground_truth": "RAG enables AI applications by integrating external data in generative models.",
  "contexts": [
    "RAG enables AI applications by integrating external data in generative models.",
    "RAG enables AI applications such as semantic search engines, recommendation systems, and context-aware chatbots."
  ]
})

print(f"Context Precision: {eval_result['context_precision']}")

### FAITHFULNESS EVALUATION:
from ragas.metrics import faithfulness
# Query the retriever using the query and extract the document text
query = "How does RAG improve question answering with LLMs?"
retrieved_docs = [loaded_document.page_content for loaded_document in retriever.invoke(query)]
# Define the faithfulness chain
faithfulness_chain = EvaluatorChain(metric=faithfulness, llm=watsonx_llm, embeddings=watsonx_embeddings)
# Evaluate the faithfulness of the RAG chain
eval_result = faithfulness_chain({
  "question": query,
  "answer": chain.invoke(query),
  "contexts": retrieved_docs
})
print(eval_result)
