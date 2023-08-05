import streamlit as st

# Set the title of the app
st.title("CT Revision 2015")

# Define the subjects and their corresponding credit hours for each semester

last_4_sem = {
    "Semester 3": {
        "3139. DataBase Management System Lab":3,
        "3138. Digital Computer Principles Lab":3,
        "3137. Object Oriented Programming through C++ Lab":3,
        "3134. Object Oriented Programming through C++": 5,
        "3133. Digital Computer Principles": 4,
        "3132. DataBase Management System": 4,
        "3131. Computer Architecture": 4,
        "3001. Environmental Science & Disaster Management": 3,
    },
    "Semester 4": {
        "4139. System Administration Lab": 3,
        "4138. Data Structures Lab":3,
        "4137. Computer System Hardware Lab":3,
        "4136. Application Development using Java":5,
        "4134. Operating Systems": 4,
        "4133. Data Structures": 5,
        "4132. Data Communication": 4,
        "4131. Computer System Hardware": 4,
    },
    "Semester 5": {
        "5139. Web Programming Lab":4,
        "5138. Microprocessor Lab":4,
        "5137. Computer Network Engineering Lab":3,
        "5134. Cloud Computing": 4,
        "5133. Web Programming": 4,
        "5132. Project Management and Software Engineering": 4,
        "5131. Microprocessor and Interfacing": 4,
        "5009. Industrial Training/Industrial Visit/Collaborative work":2,
    },
    "Semester 6": {
        "6139. Microcontroller Lab": 3,
        "6138. Smart Device Programming Lab": 3,
        "6136. Software Testing": 5,
        "6133. Smart Device Programming": 4,
        "6132. Microcontrollers": 5,
        "6131. Computer Networks": 4,
        "6009. Project & Seminar":10,
    },
}

semesters_regular = {
    "Semester 1": {
        "1009. Health & Physical Education": 2,
        "1008. Computing Fundamentals": 4,
        "1004. Chemistry I": 3,
        "1003. Physics I": 3,
        "1002. Mathematics I": 6,
        "1001. English I": 3,
    },
    "Semester 2": {
        "2139. Programming in C Lab":2,
        "2131. Programming in C": 4,
        "2009. Life Skill": 2,
        "2008. Workshop Practice": 3,
        "2007. Engineering Science Lab II":3,
        "2005. Engineering Graphics": 5,
        "2004. Chemistry II": 3,
        "2003. Physics II":3,
        "2002. Mathematics II": 6,
        "2001. English II": 3,
    },
    "Semester 3": last_4_sem["Semester 3"],
    "Semester 4": last_4_sem["Semester 4"],
    "Semester 5": last_4_sem["Semester 5"],
    "Semester 6": last_4_sem["Semester 6"],
}

semesters_lateral = {
    "Semester 3": last_4_sem["Semester 3"],
    "Semester 4": last_4_sem["Semester 4"],
    "Semester 5": last_4_sem["Semester 5"],
    "Semester 6": last_4_sem["Semester 6"],
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
    st.header(semester)
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
        semester_cgpa_button = st.button("Calculate SGPA", key=semester_cgpa_button_key)

    with col1:
        cumulative_cgpa_button_key = f"cumulative_cgpa_button_{semester}"
        cumulative_cgpa_button = st.button("Calculate CGPA", key=cumulative_cgpa_button_key)

    if semester_cgpa_button:
        semester_credit_points = 0
        semester_credits = sum(subject_data[1] for subject_data in subjects.items())

        for grade, subject_data in zip(semester_grades, subjects.items()):
            credit_hours = subject_data[1]
            semester_credit_points += get_credit_points(grade) * credit_hours

        semester_cgpa = semester_credit_points / semester_credits
        st.subheader(f"{semester} SGPA: {semester_cgpa:.2f}")

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
        st.subheader(f"CGPA till {selected_semester}: {cumulative_cgpa:.2f}")


# Display the CGPAs to the user
# st.subheader("CGPA")
# if semester_cgpas:
#     st.write("Semester CGPAs:")
#     for semester, cgpa in zip(semesters.keys(), semester_cgpas):
#         st.write(f"{semester}: {cgpa}")
    
#     st.write("Cumulative CGPAs:")
#     for semester, cgpa in zip(semesters.keys(), cumulative_cgpas):
#         st.write(f"{semester}: {cgpa}")
# else:
#     st.write("No grades selected yet.")
