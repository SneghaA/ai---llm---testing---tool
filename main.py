import json
import pandas as pd
import os
from openai import OpenAI
from dotenv import load_dotenv
from evaluator import evaluate_response
from regression import compare_models

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_ai_response(prompt, model_name):
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content



with open("test_cases.json", "r") as file:
    test_cases = json.load(file)

results = []
model_v1 = "gpt-4o-mini"
model_v2 = "gpt-4o-mini"  # simulate new version

for test in test_cases:
    print("Running:", test["id"])

    response_v1 = get_ai_response(test["prompt"], model_v1)
    score_v1, hallucination_v1 = evaluate_response(response_v1, test["expected_answer"])

    response_v2 = get_ai_response(test["prompt"], model_v2)
    score_v2, hallucination_v2 = evaluate_response(response_v2, test["expected_answer"])

    comparison_result = compare_models(score_v1, score_v2)

    results.append({
        "Test ID": test["id"],
        **comparison_result
    })

df = pd.DataFrame(results)
df.to_csv("test_report.csv", index=False)

print("Testing complete. Report saved as test_report.csv")

total_tests = len(results)
improvements = sum(1 for r in results if r["Improvement"] > 0)
degradations = sum(1 for r in results if r["Improvement"] < 0)

print("\n===== REGRESSION SUMMARY =====")
print("Total Tests:", total_tests)
print("Improved Cases:", improvements)
print("Degraded Cases:", degradations)

drift_percentage = (degradations / total_tests) * 100
print("Performance Drift %:", round(drift_percentage, 2))