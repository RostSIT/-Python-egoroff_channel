class SoccerPlayer:

    def __init__(self, name, surname, goals=0, assists=0):

        self.name = name
        self.surname = surname
        self.goals = goals
        self.assists = assists
        
    def score(self, count=1):
        self.goals += count

    def make_assist(self, count=1):
        self.assists += count

    def statistics(self):
        print(f'{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}')

