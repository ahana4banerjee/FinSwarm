from datetime import datetime

def meta(agent_name, version):
    return {
        "agent": agent_name,
        "version": version,
        "timestamp": datetime.utcnow().isoformat()
    }
