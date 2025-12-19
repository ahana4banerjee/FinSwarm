def run(goal, duration):
    goal = goal.lower()

    roadmap = []

    # Foundations are always first
    roadmap.append({
        "phase": 1,
        "title": "Foundations",
        "concepts": [
            "Money basics",
            "Income vs expenses",
            "Saving vs investing"
        ]
    })

    # Conditional middle phase
    PRODUCT_KEYWORDS = [
        "mutual fund", "mutual funds",
        "fd", "fixed deposit",
        "insurance", "stocks", "invest", "inflation"
    ]

    needs_risk = any(k in goal for k in PRODUCT_KEYWORDS)

    if needs_risk:

        roadmap.append({
            "phase": 2,
            "title": "Risk & Inflation",
            "concepts": [
                "Inflation",
                "Risk vs return",
                "Time value of money"
            ]
        })

    # Products phase
    roadmap.append({
        "phase": 3,
        "title": "Financial Products",
        "concepts": [
            "Fixed deposits",
            "Mutual funds",
            "Insurance basics"
        ]
    })

    return {
        "goal": goal,
        "duration": duration,
        "roadmap": roadmap
    }
