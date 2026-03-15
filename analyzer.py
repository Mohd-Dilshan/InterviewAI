def analyze_answer(answer):

    feedback = []

    if len(answer.split()) < 8:
        feedback.append("Your answer is too short. Try explaining more.")

    if "um" in answer or "uh" in answer:
        feedback.append("Avoid filler words like 'um' or 'uh'.")

    if "I don't know" in answer:
        feedback.append("Try explaining your thought process instead of saying you don't know.")

    if not feedback:
        feedback.append("Good answer! Keep it up.")

    return feedback