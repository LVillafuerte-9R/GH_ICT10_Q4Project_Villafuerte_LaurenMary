from pyscript import display, document
import numpy as np
import matplotlib.pyplot as plt

class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):
        return f"Hi! I am {self.name} from {self.section}. My favorite subject is {self.favorite_subject}."

classmates_list = [
    Classmate("Kim", "Ruby", "PE"),
    Classmate("Rose", "Ruby", "Science"),
    Classmate("Nilza", "Sapphire", "Filipino"),
    Classmate("Bea", "Topaz", "English"),
    Classmate("Hikari", "Emerald", "Social Studies")
]

def add_new_classmate(e):
    name = document.getElementById("name-input").value
    section = document.getElementById("section-input").value
    subject = document.getElementById("subject-input").value
    
    if name and section and subject:
        new_student = Classmate(name, section, subject)
        classmates_list.append(new_student)
        
        document.getElementById("output").innerHTML = ""
        display(f"{name} added!", target="output")

def show_all_classmates(e):
    output_div = document.getElementById("output")
    output_div.innerHTML = ""
    
    for student in classmates_list:
        display(student.introduce(), target='output', append=True)

# ATTENDANCE
days = np.array(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
absences = np.array([0, 0, 0, 0, 0])

def update_tracker(e):
    day_index = int(document.getElementById("day-select").value)
    count = document.getElementById("absence-input").value
    
    if count == "":
        count = 0
    
    absences[day_index] = int(count)
    display_graph()

def display_graph():
    document.getElementById("graph-output").innerHTML = ""
    
    plt.clf()
    plt.figure(figsize=(6, 4))
    plt.plot(days, absences, marker='o')
    plt.title('Weekly Absences')
    plt.xlabel('Day')
    plt.ylabel('Absences')
    plt.grid(True)
    
    display(plt, target="graph-output")
