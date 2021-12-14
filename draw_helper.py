import json
from PyInquirer import prompt
from examples import custom_style_2


class DrawHelper():
    def __init__(self, input_file):
        with open(input_file) as f:
            teams_json = json.load(f)

        if len(teams_json['unseeded']) != len(teams_json['seeded']):
            raise Exception(
                "Invalid Input: length of the seeded teams doesn't match the length of the seeded teams")

        for team in [*teams_json['unseeded'], *teams_json['seeded']]:
            team['available'] = True

        self.seeded = teams_json['seeded']
        self.unseeded = teams_json['unseeded']
        self.pairs = []

    def teams_can_play_each_other(self, team_1, team_2):
        return team_1['country'] != team_2['country'] and team_1['group'] != team_2['group']

    def get_opposition_options(self, team, is_recursive=True):
        available_opposition_teams = []
        excluded_teams = []

        # find potential opposition teams for remaining unseeded teams
        # and if there is only one potential option, exclude it from
        # the list of the current team's potential opposition.
        if is_recursive:
            for u in self.unseeded:
                if u['available']:
                    potential_oppositions = self.get_opposition_options(
                        u, is_recursive=False)
                    if len(potential_oppositions) == 1:
                        excluded_teams.append(*potential_oppositions)

        for s in self.seeded:
            if s['available']:
                if self.teams_can_play_each_other(s, team) and s['team'] not in excluded_teams:
                    available_opposition_teams.append(s['team'])

        return available_opposition_teams

    def make_a_pair(self):
        team_choices = []
        for u in self.unseeded:
            team_choices.append(
                {
                    'name': u['team'],
                    'disabled': '❌' if u['available'] == False else None
                }
            )

        select_first_team_prompt = {
            'type': 'list',
            'name': 'selected_team',
            'message': 'Select an unseeded team:',
            'choices': team_choices
        }

        selections = prompt([select_first_team_prompt], style=custom_style_2)
        selected_team_name = selections.get('selected_team')
        selected_team = None

        for u in self.unseeded:
            if u['team'] == selected_team_name:
                u['available'] = False
                selected_team = u
                break

        opposition_options = self.get_opposition_options(selected_team)

        select_opposition_prompt = {
            'type': 'list',
            'name': 'selected_team',
            'message': 'Select the opposition:',
            'choices': opposition_options
        }
        selections = prompt([select_opposition_prompt], style=custom_style_2)
        opposition_team_name = selections.get('selected_team')
        for s in self.seeded:
            if s['team'] == opposition_team_name:
                s['available'] = False
                break

        self.pairs.append(selected_team_name + ' - ' + opposition_team_name)

    def start(self):
        teams_left = len(self.seeded)

        while teams_left > 0:
            self.make_a_pair()
            teams_left -= 1
        return
