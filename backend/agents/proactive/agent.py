from agents.metadata import meta

def run(concept, ask_count=1):
    if ask_count > 2:
        return {
            "type": "reinforcement",
            "message": f"You asked about {concept} multiple times.",
            "suggestion": "Consider reviewing this concept slowly.",
            "source": "FinSwarm Logic",
            "meta": meta("proactive", "v1.0")

        }

    insights = {
        "inflation": {
            "type": "concept_link",
            "message": "Inflation affects purchasing power over time.",
            "suggestion": "Next, learn interest rates.",
            "source": "RBI Handbook"
        },
        "risk": {
            "type": "misconception",
            "message": "Risk does not always mean loss.",
            "suggestion": "Learn diversification.",
            "source": "SEBI Guide"
        }
    }

    return insights.get(concept)
