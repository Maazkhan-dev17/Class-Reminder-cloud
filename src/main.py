timetable = [
    {"teacher": "Inam Sir", "subject": "Design and Analysis of Algorithm", "room": "06", "start": "09:00", "end": "09:50"},
    {"teacher": "Fazal Rabi Sir", "subject": "Data Base", "room": "06", "start": "09:50", "end": "10:40"},
    {"teacher": "Suliman Khelji Sir", "subject": "Parallel and Distributed Computing", "room": "06", "start": "10:40", "end": "11:30"},
]

for c in timetable:
    print(c["teacher"], "- class of", c["subject"], "start at", c["start"], "in room", c["room"])