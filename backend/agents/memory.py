SESSION_MEMORY = {
    "last_concept": None,
    "ask_count": {}
}

def update_memory(concept):
    SESSION_MEMORY["last_concept"] = concept
    SESSION_MEMORY["ask_count"][concept] = SESSION_MEMORY["ask_count"].get(concept, 0) + 1
    return SESSION_MEMORY
