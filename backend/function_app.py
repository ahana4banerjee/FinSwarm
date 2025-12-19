from agents.goal_planner.agent import run as goal_planner
from agents.curriculum_builder.agent import run as curriculum_builder
from agents.tutor.agent import run as tutor
from agents.safety.agent import run as safety
from agents.knowledge.agent import run as knowledge_agent
from agents.proactive.agent import run as proactive_agent
from agents.memory import update_memory




import azure.functions as func
import logging
import json

# Initialize the Function App
app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

# ---------------------------------------------------------
# 1. GOAL SETTING ENDPOINT
# Route: /api/goal
# Description: Takes user goal text, returns a dummy roadmap
# ---------------------------------------------------------
@app.route(route="goal", auth_level=func.AuthLevel.ANONYMOUS)
def goal_endpoint(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Goal Planner endpoint triggered.')

    try:
        req_body = req.get_json()
        user_goal = req_body.get('goal')
        duration = req_body.get('duration')
    except ValueError:
        return func.HttpResponse("Invalid JSON", status_code=400)

    if not user_goal:
        return func.HttpResponse("Please provide a goal.", status_code=400)

    # STUB RESPONSE (We will replace this with the Agent in Phase 2)
    roadmap = goal_planner(user_goal, duration)
    curriculum = curriculum_builder(roadmap)

    response_data = {
        "roadmap": roadmap,
        "learning_state": curriculum
    }


    return func.HttpResponse(
        json.dumps(response_data),
        mimetype="application/json",
        status_code=200
    )

# ---------------------------------------------------------
# 2. CHAT ENDPOINT
# Route: /api/chat
# Description: Takes user message, returns a dummy tutor response
# ---------------------------------------------------------
@app.route(route="chat", auth_level=func.AuthLevel.ANONYMOUS)
def chat_endpoint(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Chat endpoint triggered.')

    try:
        req_body = req.get_json()
        message = req_body.get('message')
    except ValueError:
        return func.HttpResponse("Invalid JSON", status_code=400)

    if not message:
        return func.HttpResponse("Please provide a message.", status_code=400)

    # STUB RESPONSE (We will replace this with the Tutor Agent later)
    knowledge = knowledge_agent(message)

    primary = knowledge
    memory = update_memory(primary["concept"])
    ask_count = memory["ask_count"].get(primary["concept"], 1)


    tutor_response = tutor(primary["explanation"], primary["confidence"])

    safe_text = safety(tutor_response["content"])
    proactive = proactive_agent(primary["concept"], ask_count)

    


    response_data = {
        "answer": safe_text,
        "source": primary["source"],
        "related_concepts": primary["related"],
        "memory": {
            "last_concept": memory["last_concept"],
            "times_asked": ask_count
        },
        "trace": {
            "knowledge": primary.get("meta"),
            "tutor": tutor_response.get("meta"),
            "proactive": proactive.get("meta") if proactive else None
        }

    }



    return func.HttpResponse(
        json.dumps(response_data),
        mimetype="application/json",
        status_code=200
    )