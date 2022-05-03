exercises = []

class Exercise:

    def __init__(self, name, challenge, whiteboard, link, topics, completed):
        self.name = name
        self.challenge = challenge
        self.whiteboard = whiteboard
        self.link = link
        self.topics = topics
        self.completed = completed

    def __repr__(self):

        return f'<Exercise name={self.name} challenge={self.challenge}>'

    

for line in open('hb_exercises.txt'):

    #split
    parsed = line.rstrip().split(', ')

    #unpack
    name, challenge, whiteboard, link, topics, availability = parsed

    #adjust if necessary
    challenge_diff = challenge[10:]

    if 'none' in whiteboard.lower():
        whiteboard_diff = None
    else:
        whiteboard_diff = whiteboard[11:]

    topics_list = topics.lower().split(' and ')

    exercises.append(Exercise(name=name,
                              challenge=challenge_diff,
                              whiteboard=whiteboard_diff,
                              link=link,
                              topics=topics_list,
                              completed=availability))

def print_exercises():
    """shows all exercises"""

    for exercise in exercises:
        print(f'{exercise}, link: {exercise.link}')

def print_unfinished_exercises():
    """shows all exercises that haven't been done yet
    when you finish an exercise, write date and name in hb_exercises.txt"""

    for exercise in exercises:
        if exercise.completed == 'Available':
            print(f'{exercise}, link: {exercise.link}')

def print_exercises_difficulty(target):
    """Select difficulty from Easier, Medium, or Harder, case insensitive"""

    for exercise in exercises:
        if exercise.challenge.lower() == target.lower():
            print(f'{exercise}, link: {exercise.link}')

def print_exercises_whiteboarding():
    """shows all exercises with a whiteboarding difficulty"""
    
    for exercise in exercises:
        if exercise.whiteboard:
            print(f'{exercise}, link: {exercise.link}')