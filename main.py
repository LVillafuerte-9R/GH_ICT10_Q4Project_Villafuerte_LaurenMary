from pyscript import display, document
import numpy as np
import matplotlib.pyplot as plt

# CLASSMATE SYSTEM

class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):
        return f"{self.name} | Section: {self.section} | Favorite Subject: {self.favorite_subject}"


classmates_list = [
    Classmate("Kim", "Ruby", "PE"),
    Classmate("Rose", "Ruby", "Science"),
    Classmate("Nilza", "Sapphire", "Filipino"),
    Classmate("Bea", "Topaz", "English"),
    Classmate("Hikari", "Emerald", "Social Studies")
]


def add_new_classmate(event):
    name = document.getElementById("name-input").value
    section = document.getElementById("section-input").value
    subject = document.getElementById("subject-input").value

    if name and section and subject:
        new_student = Classmate(name, section, subject)

        classmates_list.append(new_student)

        document.getElementById("output").innerHTML = ""

        display(f"{name} added successfully!",
                target="output")


def show_all_classmates(event):
    output_div = document.getElementById("output")

    output_div.innerHTML = ""

    for student in classmates_list:
        display(student.introduce(),
                target="output",
                append=True)

# ATTENDANCE TRACKER

days = np.array([
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
])

absences = np.array([0, 0, 0, 0, 0])


def update_tracker(event):

    day_index = int(
        document.getElementById("day-select").value
    )

    count = document.getElementById(
        "absence-input"
    ).value

    if count == "":
        count = 0

    absences[day_index] = int(count)

    display_graph()


def display_graph():

    graph_div = document.getElementById(
        "graph-output"
    )

    graph_div.innerHTML = ""

    fig, ax = plt.subplots(figsize=(6, 4))

    ax.plot(days, absences, marker="o")

    ax.set_title("Weekly Absences")

    ax.set_xlabel("Days")

    ax.set_ylabel("Absences")

    ax.grid(True)

    display(fig, target="graph-output")`
