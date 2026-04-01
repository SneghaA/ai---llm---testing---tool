# 🤖 AI LLM Evaluation Tool

## 🚀 Overview
A Python-based framework to evaluate, compare, and monitor responses from Large Language Models (LLMs).  
This tool automates prompt testing, scoring, hallucination detection, and model performance analysis.

---

## 🧠 Version 1 – Basic LLM Evaluation Tool

- Prompt testing using JSON dataset  
- Single model response evaluation  
- Rule-based scoring (keyword match, response length)  
- Basic hallucination detection  
- Toxicity detection  
- Automated CSV report generation  

---

## 🚀 Version 2 – Advanced LLM Evaluation Framework

- Multi-model comparison (Model V1 vs Model V2)  
- Semantic similarity scoring using embeddings  
- LLM-as-a-Judge for qualitative evaluation  
- Hybrid scoring (rule-based + semantic + judge)  
- Regression testing (improved / degraded / tie cases)  
- Performance drift monitoring (%)  
- Detailed CSV reporting with comparison metrics  

---

## 🏗️ Project Structure

main.py → Runs test suite  
evaluator.py → Response evaluation logic  
metrics.py → Semantic similarity scoring  
regression.py → Model comparison  
evaluators/judge.py → LLM-based judging  
test_cases.json → Prompt dataset  
test_report.csv → Generated results  

