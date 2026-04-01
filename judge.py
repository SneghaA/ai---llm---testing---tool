import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def judge_response(prompt, response, expected):
    judge_prompt = f"""
You are an AI evaluator.

Prompt: {prompt}
Expected Answer: {expected}
Model Response: {response}

Give:
1. Score (0 to 10)
2. Reason

Format:
Score: X
Reason: ...
"""

    result = openai.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": judge_prompt}]
    )

    return result.choices[0].message.content