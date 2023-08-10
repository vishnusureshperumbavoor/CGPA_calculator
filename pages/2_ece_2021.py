import streamlit as st

# Set the title of the app
st.title("CT Revision 2015")

# Define the subjects and their corresponding credit hours for each semester

last_4_sem = {
    "Semester 3": {
        "3039. Mechanical Engineering Lab": 1.5,
        "3038. Electrical Workshop Practice": 1.5,
        "3037. Electrical Measurements Lab": 1.5,
        "3036. DC Machines Lab": 1.5,
        "3035. Mechanical Engineering": 0,
        "3034. Electrical & Electronics Measuring Instruments": 4,
        "3033. Fundamentals of Electric Circuits": 4,
        "3032. DC Machines & Traction Motors": 3,
        "3031. Analog & Digital Circuits": 3,
    },
    "Semester 4": {
        "5009. Internship II": 3,
        "4039. Professional Practice Lab": 0,
        "4038. Domestic Appliances Repair & Maintenance Workshop": 1.5,
        "4037. Induction Machines Lab": 1.5,
        "4036. Electronics Lab": 1.5,
        "4033. Induction Machines": 4,
        "4032. Electrical Installation Design & Estimation": 4,
        "4031. Power Electronics Devices and Circuits": 4,
        "4009. Minor Project": 2,
        "4001. Community Skills in Indian knowledge system": 0,
    },
    "Semester 5": {
        "6009. Major Project": 0,
        "5039. Solar Energy Technology Lab":1.5,
        "5038. Industrial Electrical Engineering Lab":1.5,
        "5037. Synchronous Machines Lab":1.5,
        "5033. Renewable Energy Power Plant":4,
        "5032. Electricity Generation, Transmission & Distribution": 4,
        "5031. Synchronous Machines & FHP Motors": 4,
        "5008. Seminar": 1,
        "5001. Industrial Management and Safety": 0,
    },
    "Semester 6": {
        "6039. Applied Electrical Testing Lab / Modelling and simulation Lab / Advanced Solar Photovoltaic Lab": 1.5,
        "6038. Industrial Automation Lab": 1.5,
        "6037. Electrical Computer Aided Drafting Lab": 1.5,
        "6032. Solar Power Technologies / Energy Conservation & Management	/ Electrification of Residential Buildings / Electric Vehicles & Traction": 4,
        "6031. Energy Conservation & Audit (EE) / Electric Vehicle Technology / Microcontroller & PLC": 5,
        "6009. Major Project": 4,
        "6002. Indian Constitution": 0,
        "6001. Entrepreneurship and Startup":4,
    },
}

semesters_regular = {
    "Semester 1": {
        "1009. Sports and Yoga": 1,
        "1008. Introduction to IT systems Lab	": 2,
        "1007. Applied Chemistry Lab": 1,
        "1005. Engineering Graphics": 1.5,
        "1004. Applied Chemistry": 3,
        "1003. Applied Physics I": 3,
        "1002. Mathematics I": 5,
        "1001. Communication Skills in English": 4,
    },
    "Semester 2": {
        "3009. Internship I": 2,
        "2039. Fundamentals of Eletrical & Electronics Engineering Lab": 0,
        "2038. Engineering Graphics using CAD software": 0,
        "2032. Elementary Concepts of Electrical Systems": 3,
        "2031. Fundamentals of Electrical & Electronics Engineering": 3,
        "2009. Engineering Workshop Practice": 1.5,
        "2008. Communication Skills in English Lab	": 1.5,
        "2006. Applied Physics Lab": 1,
        "2003. Applied Physics II": 3,
        "2002. Mathematics II": 4,
        "2001. Environmental Science": 0,
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
        st.subheader(f"SGPA {semester}: {semester_cgpa:.2f}")

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

st.markdown("---")
st.write("GitHub Repository: https://github.com/vishnusureshperumbavoor/CGPA_calculator")
st.write("Developed by: VSP (Vishnu Suresh Perumbavoor)")
st.write("GMail: vishnusureshperumbavoor@gmail.com")
st.write("GitHub: [vishnusureshperumbavoor](https://github.com/vishnusureshperumbavoor)")
st.write("Twitter: [vspeeeeee](http://www.twitter.com/vspeeeeee)")
st.write("LinkedIn: [vishnu-suresh-perumbavoor](https://www.linkedin.com/in/vishnu-suresh-perumbavoor/)")
st.write("Website: [vishnusureshperumbavoor.com](https://vishnusureshperumbavoor.github.io/V-S-P/)")
st.write("YouTube: [Vishnu Suresh Perumbavoor](https://www.youtube.com/@vishnusureshperumbavoor/)")
st.write("Instagram: [vishnusureshperumbavoor](https://www.instagram.com/vishnusureshperumbavoor/)")