import streamlit as st

st.set_page_config(
    page_title="CGPA Calculator",
    page_icon="🎓"
)

# Set the title of the app
st.title("CT Revision 2021")


# Define the subjects and their corresponding credit hours for each semester

last_4_sem = {
    "Semester 3": {
        "3139. Computer System Hardware Lab":0,
        "3138. Web Technology lab":2.5,
        "3137. Digital Computer Fundamentals Lab":1.5,
        "3136. Database Management System lab":1.5,
        "3135. Programming in C Lab": 1.5,
        "3134. Digital Computer Fundamentals": 3,
        "3133. Database Management Systems": 3,
        "3132. Programming in C": 3,
        "3131. Computer Organisation": 4,
    },
    "Semester 4": {
        "5009. Internship II":3,
        "4139. Application Development Lab":0,
        "4138. Data Structures Lab":1.5,
        "4137. Web Programming Lab":0,
        "4136. Object Oriented Programming Lab": 1.5,
        "4133. Data Structures": 4,
        "4132. Computer Communication and Networks": 3,
        "4131. Object Oriented Programming": 4,
        "4006. Minor Project":2,
        "4001. Community Skills in Indian knowledge system": 0,
    },
    "Semester 5": {
        "6009. Major Project":0,
        "5139. Virtualisation Technology and cloud computing Lab / Ethical Hacking Lab / Fundamentals of Artificial Intelligence and Machine Learning Lab":1.5,
        "5138. System Administration Lab":1.5,
        "5137. Embedded Systems and Real Time Operating System Lab": 1.5,
        "5133. Community Skills in Indian knowledge system": 4,
        "5132. Virtualisation Technology and Cloud Computing / Ethical Hacking / Fundamentals of Artificial Intelligence and Machine Learning": 4,
        "5131. Embedded System and Real time Operating System": 4,
        "5008. Seminar":1,
        "5002. Project Management and Software Engineering": 0,
    },
    "Semester 6": {
        "6139. Program elective course lab (Software Testing Lab / Internet of Things Lab / Server Administration Lab)":1.5,
        "6138. Smart Device Programming Lab":1.5,
        "6137. Computer Network Engineering Lab": 1.5,
        "6132. Open elective course (Introduction to IoT / Fundamentals of Web Technology / Multimedia / Cloud Computing)": 0,
        "6131. Program elective course (Software Testing / Internet of Things / Server Administration)": 4,
        "6009. Major Project":4,
        "6002. Indian Constitution": 2.5,
        "6001. Entrepreneurship and Startup": 4,
    },
}

semesters_regular = {
    "Semester 1": {
        "1009. Sports and Yoga": 1,
        "1008. Introduction to IT systems Lab": 2,
        "1007. Chemistry Lab": 1,
        "1005. Engineering Graphics": 1.5,
        "1004. Chemistry": 3,
        "1003. Physics I": 3,
        "1002. Mathematics I": 5,
        "1001. English": 4,
    },
    "Semester 2": {
        "3009. Internship I": 2,
        "2139. Problem Solving and Programming Lab":0,
        "2131. Problem Solving and Programming": 3,
        "2039. Fundamentals of Eletrical & Electronics Engineering Lab":0,
        "2031. Fundamentals of Electrical & Electronics Engineering": 3,
        "2009. Engineering Workshop Practice": 1.5,
        "2008. Communication Skills in English Lab": 1.5,
        "2006. Physics Lab": 1,
        "2003. Physics II": 3,
        "2002. Mathematics II": 4,
        "2001. Environmental Science":0,
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
