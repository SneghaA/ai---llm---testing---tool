# AI LLM Evaluation Tool

This project is a Python-based testing framework designed to evaluate responses from Large Language Models (LLMs).

The system automatically runs prompt test cases against AI models and analyzes responses using automated scoring and hallucination detection rules.

---

## Features

• Prompt evaluation system  
• Response scoring engine  
• Hallucination detection  
• Toxicity detection  
• Model regression comparison  
• Performance drift monitoring  
• Automated CSV test reports  

---

## Project Structure

main.py → Runs test suite  
evaluator.py → Response evaluation logic  
regression.py → Model comparison  
metrics.py → Performance metrics  
test_cases.json → Prompt test dataset  
test_report.csv → Generated test results  

---

## Example Test Results

Total Tests: 6  
Improved Cases: 0  
Degraded Cases: 0  
Performance Drift: 0%

---

## Technologies Used

Python  
OpenAI API  
Pandas  
JSON test datasets  

---

## Purpose

This tool demonstrates how QA engineers can test AI systems, detect hallucinations, and monitor model performance across versions.