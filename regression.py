
def compare_models(score_v1, score_v2):
    improvement = score_v2 - score_v1

    status_v1 = "PASS" if score_v1 >= 2 else "FAIL"
    status_v2 = "PASS" if score_v2 >= 2 else "FAIL"

    return {
        "Score_V1": score_v1,
        "Score_V2": score_v2,
        "Improvement": improvement,
        "Status_V1": status_v1,
        "Status_V2": status_v2
    }