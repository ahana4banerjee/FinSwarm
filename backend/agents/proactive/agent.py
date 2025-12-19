def run(concept, ask_count=1):
    if not concept:
        return None

    concept = concept.lower().strip()

    insights = {
        "inflation": {
            "type": "concept_link",
            "message": "Inflation reduces purchasing power over time.",
            "suggestion": "You should understand interest rates next.",
            "source": "RBI Handbook"
        },
        "risk": {
            "type": "misconception",
            "message": "Risk does not always mean loss.",
            "suggestion": "Learn diversification to manage risk.",
            "source": "SEBI Guide"
        }
    }

    # reinforcement insight
    if ask_count > 1:
        return {
            "type": "reinforcement",
            "message": f"You’ve asked about {concept} multiple times.",
            "suggestion": "Revisit the basics slowly before moving ahead.",
            "source": "FinSwarm Logic"
        }

    return insights.get(concept)

