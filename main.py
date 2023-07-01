```python
from activity_planner import generateActivities
from accommodation_finder import findAccommodation
from transportation_planner import planTransportation
from food_planner import planFood
from competition_manager import manageCompetition
from html_generator import generateHTML
from config import group_info, activity_list, accommodation_info, transportation_info, food_preferences, competition_info, physical_limitations, schedule_info

def main():
    # Generate activities based on group's interests
    activities = generateActivities(group_info, activity_list)

    # Find accommodation based on group's preferences
    accommodation = findAccommodation(group_info, accommodation_info)

    # Plan transportation based on group's preferences
    transportation = planTransportation(group_info, transportation_info)

    # Plan food based on group's preferences
    food = planFood(group_info, food_preferences)

    # Manage competition and scoring system
    competition = manageCompetition(group_info, competition_info)

    # Generate HTML file for visualization
    generateHTML(activities, accommodation, transportation, food, competition)

if __name__ == "__main__":
    main()
```