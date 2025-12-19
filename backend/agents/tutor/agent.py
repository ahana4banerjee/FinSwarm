from agents.metadata import meta

PROMPT_TEMPLATE = """
You are a financial tutor for beginners.
Explain the concept in simple language.
Use one analogy.
Do NOT give advice.

Concept:
{concept}

Explanation:
"""


def run(explanation, confidence=1.0):
    if confidence < 0.6:
        prefix = "Let’s go step by step, starting from basics."
    else:
        prefix = "Here’s a clear explanation."

    return {
        "role": "assistant",
        "content": f"{prefix}\n\n{explanation}\n\nKey takeaway: learn first, decide later.",
        "meta": meta("tutor", "v1.1")

    }