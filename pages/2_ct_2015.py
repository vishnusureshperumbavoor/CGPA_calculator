import streamlit as st

# Set the title of the app
st.title("CT Revision 2015")

# Define the subjects and their corresponding credit hours for each semester
semesters_regular = {
    "Semester 1": {
        "1. English for Communication I": 3,
        "2. Engineering Mathematics I": 6,
        "3. Engineering Physics I": 3,
        "4. Engineering Chemistry I": 3,
        "5. Health & Physical Education": 2,
        "6. Computing Fundamentals": 4,
    },
    "Semester 2": {
        "1. English for Communication II": 3,
        "2. Engineering Mathematics II": 6,
        "3. Engineering Physics II":3,
        "4. Engineering Chemistry II": 3,
        "5. Programming in C": 4,
        "6. Engineering Graphics": 5,
        "7. Workshop Practice": 3,
        "8. Engineering Science Lab II":3,
        "9. Programming in C Lab":2,
        "10. Life Skill": 2,
    },
    "Semester 3": {
        "1. Digital Computer Principles": 4,
        "2. Object Oriented Programming through C++": 5,
        "3. Computer Architecture": 4,
        "4. Database Management System": 4,
        "5. Environmental Science & Disaster Management": 3,
        "6. Digital Computer Principles Lab":3,
        "7. Object Oriented Programming Lab":3,
        "8. Database Management System Lab":3,
    },
    "Semester 4": {
        "1. Data Communication": 4,
        "2. Operating Systems": 4,
        "3. Data Structures": 5,
        "4. Computer System Hardware": 4,
        "5. System Administration Lab": 3,
        "6. Data Structures Lab":3,
        "7. Computer System Hardware Lab":3,
        "8. Application Development using Java":5,
    },
    "Semester 5": {
        "1. Project Management & Software Engineering": 4,
        "2. Web Programming": 4,
        "3. Microprocessor and Interfacing": 4,
        "4. Information Security / Ethical Hacking / Cloud Computing": 4,
        "5. Web Programming Lab":4,
        "6. Microprocessor Lab":4,
        "7. Industrial Training/Industrial Visit/Collaborative work":2,
        "8. Computer Network Engineering Lab":3,
    },
    "Semester 6": {
        "1. Microcontrollers": 5,
        "2. Computer Networks": 4,
        "3. Smart Device Programming": 4,
        "4. Mobile Communication / Network Infrastructure Mangagement / Software Testing": 5,
        "5. Microcontroller Lab": 3,
        "6. Smart Device Programming Lab": 3,
        "7. Project & Seminar":10,
    },
}

semesters_lateral = {
    "Semester 3": {
        "1. Digital Computer Principles": 4,
        "2. Object Oriented Programming through C++": 3,
        "3. Computer Architecture": 3,
        "4. Database Management System": 3,
        "5. Environmental Science & Disaster Management": 1.5,
        "6. Digital Computer Principles Lab":1.5,
        "7. Object Oriented Programming Lab":1.5,
        "8. Database Management System Lab":2.5,
    },
    "Semester 4": {
        "1. Data Communication": 4,
        "2. Operating Systems": 3,
        "3. Data Structures": 4,
        "4. Computer System Hardware": 0,
        "5. System Administration Lab": 1.5,
        "6. Data Structures Lab":0,
        "7. Computer System Hardware Lab":1.5,
        "8. Application Development using Java":0,
    },
    "Semester 5": {
        "1. Project Management & Software Engineering": 0,
        "2. Web Programming": 4,
        "3. Microprocessor and Interfacing": 4,
        "4. Information Security / Ethical Hacking / Cloud Computing": 4,
        "5. Web Programming Lab": 1.5,
        "6. Microprocessor Lab":1.5,
        "7. Industrial Training/Industrial Visit/Collaborative work":1.5,
        "8. Computer Network Engineering Lab":1,
    },
    "Semester 6": {
        "1. Microcontrollers": 4,
        "2. Computer Networks": 4,
        "3. Smart Device Programming": 4,
        "4. Mobile Communication / Network Infrastructure Mangagement / Software Testing": 0,
        "5. Microcontroller Lab": 2.5,
        "6. Smart Device Programming Lab": 1.5,
        "7. Project & Seminar":1.5,
    },
}

# Get the student category from the user
student_category = st.selectbox("Select student category:", ("Regular Intake", "Lateral Entry"))

# Determine the semesters and subjects based on the student category
if student_category == "Regular Intake":
    semesters = semesters_regular
else:
    semesters = semesters_lateral

# Create empty lists to store course names and grades
course_names = []
grades = []

# Create empty lists to store CGPAs
semester_cgpas = []
cumulative_cgpas = []

def get_credit_points(grade):
    if grade == "S":
        return 10
    elif grade == "A":
        return 9
    elif grade == "B":
        return 8
    elif grade == "C":
        return 7
    elif grade == "D":
        return 6
    elif grade == "E":
        return 5
    else:
        return 0


for semester, subjects in semesters.items():
    st.subheader(semester)
    semester_grades = []
    for i, subject_data in enumerate(subjects.items(), start=1):
        subject, credit_hours = subject_data[0], subject_data[1]
        key = f"{semester}-{subject}-{i}"
        course_names.append(subject)
        grades.append(st.selectbox(f"{subject} (Credits: {credit_hours})", ("S", "A", "B", "C", "D", "E", "F"), key=key))
        semester_grades.append(grades[-1])

    col1, col2 = st.columns(2)

    with col2:
        semester_cgpa_button_key = f"semester_cgpa_button_{semester}"
        semester_cgpa_button = st.button("Calculate Semester CGPA", key=semester_cgpa_button_key)

    with col1:
        cumulative_cgpa_button_key = f"cumulative_cgpa_button_{semester}"
        cumulative_cgpa_button = st.button("Calculate CGPA till Semester", key=cumulative_cgpa_button_key)

    if semester_cgpa_button:
        semester_credit_points = 0
        semester_credits = sum(subject_data[1] for subject_data in subjects.items())

        for grade, subject_data in zip(semester_grades, subjects.items()):
            credit_hours = subject_data[1]
            semester_credit_points += get_credit_points(grade) * credit_hours

        semester_cgpa = semester_credit_points / semester_credits
        st.write(f"{semester} CGPA: {semester_cgpa:.2f}")

    if cumulative_cgpa_button:
        cumulative_credit_points = 0
        cumulative_credits = 0
        selected_semester = semester

        for sem, subjects in semesters.items():
            for subject, credit_hours in subjects.items():
                if sem <= selected_semester:
                    cumulative_credits += credit_hours
                    index = course_names.index(subject)
                    grade = grades[index]
                    cumulative_credit_points += get_credit_points(grade) * credit_hours

        cumulative_cgpa = cumulative_credit_points / cumulative_credits
        st.write(f"CGPA till {selected_semester}: {cumulative_cgpa:.2f}")





# Display the CGPAs to the user
st.subheader("CGPA")
if semester_cgpas:
    st.write("Semester CGPAs:")
    for semester, cgpa in zip(semesters.keys(), semester_cgpas):
        st.write(f"{semester}: {cgpa}")
    
    st.write("Cumulative CGPAs:")
    for semester, cgpa in zip(semesters.keys(), cumulative_cgpas):
        st.write(f"{semester}: {cgpa}")
else:
    st.write("No grades selected yet.")
