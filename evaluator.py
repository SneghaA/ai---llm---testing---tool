from metrics import calculate_similarity

def evaluate_response(response, expected_answer):
    score = 0   # ✅ ADD THIS

    similarity = calculate_similarity(response, expected_answer)
    score += similarity

    hallucination_flag = False

    if expected_answer.lower() not in response.lower():
        hallucination_flag = True

    return score, hallucination_flag