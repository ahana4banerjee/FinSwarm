import os
from agents.metadata import meta


BASE_PATH = os.path.join(os.getcwd(), "data", "docs")

INTENTS = {
    "definition": ["what is", "define", "explain"],
    "comparison": ["difference", "vs", "better"],
    "risk_check": ["safe", "risk", "danger"]
}

def detect_intent(query):
    q = query.lower()
    for intent, keywords in INTENTS.items():
        for k in keywords:
            if k in q:
                return intent
    return "general"



def parse_file(filename):
    with open(os.path.join(BASE_PATH, filename), "r") as f:
        lines = f.readlines()

    explanation = lines[0].strip()
    source = [l for l in lines if l.lower().startswith("source")][0].split(":", 1)[1].strip()
    related = [l for l in lines if l.lower().startswith("related")][0].split(":", 1)[1].strip().split(",")

    return explanation, source, [r.strip() for r in related]

def score_document(query, concept, text):
    score = 0
    if concept in query:
        score += 2
    score += text.lower().count(concept)
    return score


def run(query):
    query = query.lower()
    intent = detect_intent(query)
    confidence = 0.4

    candidates = []

    for file in os.listdir(BASE_PATH):
        concept = file.replace(".txt", "").replace("_", " ")
        explanation, source, related = parse_file(file)

        score = score_document(query, concept, explanation.lower())

        if score > 0:
            candidates.append({
                "concept": concept,
                "explanation": explanation,
                "source": source,
                "related": related,
                "score": score
            })

    if candidates:
        best = sorted(candidates, key=lambda x: x["score"], reverse=True)[0]

        return {
            "status": "found",
            "concept": best["concept"],
            "explanation": best["explanation"],
            "source": best["source"],
            "related": best["related"],
            "intent": intent,
            "confidence": 0.9,
            "meta": meta("knowledge", "v1.2")

        }

    


    return {
        "status": "not_found",
        "concept": "unknown",
        "explanation": "This topic is not yet covered.",
        "source": "N/A",
        "related": [],
        "intent": intent,
        "confidence": confidence,
        "meta": meta("knowledge", "v1.2")



    }
