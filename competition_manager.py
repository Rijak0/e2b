```python
import random
from utils import load_data

class CompetitionManager:
    def __init__(self):
        self.competition_info = load_data("competition_info")
        self.group_info = load_data("group_info")
        self.activity_list = load_data("activity_list")
        self.scores = {member: 0 for member in self.group_info['members']}

    def assign_points(self, activity):
        if activity in self.competition_info['point_activities']:
            points = random.randint(self.competition_info['min_points'], self.competition_info['max_points'])
            winner = random.choice(self.group_info['members'])
            self.scores[winner] += points
            print(f"{winner} won {points} points in {activity}!")

    def get_winner(self):
        winner = max(self.scores, key=self.scores.get)
        print(f"The winner of the competition is {winner} with {self.scores[winner]} points!")

    def manage_competition(self):
        for activity in self.activity_list:
            self.assign_points(activity)
        self.get_winner()

if __name__ == "__main__":
    competition_manager = CompetitionManager()
    competition_manager.manage_competition()
```