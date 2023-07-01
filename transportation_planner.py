```python
import json
from utils import load_data, save_data
from constants import TRANSPORTATION_SCHEMA

def validate_transportation_info(transportation_info):
    for key in TRANSPORTATION_SCHEMA:
        if key not in transportation_info:
            return False
    return True

def plan_transportation():
    group_info = load_data("group_info.json")
    transportation_info = group_info.get("transportation_info", {})

    if not validate_transportation_info(transportation_info):
        print("Invalid transportation info")
        return

    preferred_transport = transportation_info.get("preferred_transport")
    rejected_transport = transportation_info.get("rejected_transport")
    luggage_info = transportation_info.get("luggage_info")

    transportation_plan = {
        "preferred_transport": preferred_transport,
        "rejected_transport": rejected_transport,
        "luggage_info": luggage_info,
        "vehicles_available": 3
    }

    save_data("transportation_plan.json", transportation_plan)

if __name__ == "__main__":
    plan_transportation()
```