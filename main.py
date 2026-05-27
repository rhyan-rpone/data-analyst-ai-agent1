from tools.data_loader import load_dataset
from graphs.workflow import graph


dataset = load_dataset("datasets/01_Netflix_2016_2025.csv")


result = graph.invoke({

    "question": "Analise esse dataset",

    "dataset_info": dataset
})


print("\n=== RESUMO ===\n")
print(result["final_response"])

print("\n=== ANÁLISE ===\n")
print(result["analysis_result"])