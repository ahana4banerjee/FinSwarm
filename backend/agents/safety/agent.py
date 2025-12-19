FORBIDDEN_KEYWORDS = [
    "should i invest",
    "best investment",
    "buy",
    "sell",
    "returns",
    "profit",
    "which is better"
]

def run(text):
    lower = text.lower()

    for phrase in FORBIDDEN_KEYWORDS:
        if phrase in lower:
            return (
                "I can’t give investment advice. "
                "However, I can explain the underlying concepts so you can decide confidently."
            )

    return text
