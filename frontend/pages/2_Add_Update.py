import streamlit as st
from utils import add_student, get_students

tab1, tab2 = st.tabs(["➕ Add Student", "✏️ Update Student"])

with tab1:
    st.subheader("➕ Add Student")
    # Read Data from User
    name = st.text_input("Name")
    tenth = st.number_input("10th %", 0.0, 100.0)
    twelfth = st.number_input("12th %", 0.0, 100.0)
    cgpa = st.number_input("BE CGPA", 0.0, 10.0)
    
    skills = st.text_input("Skills")
    domain = st.text_input("Domain")
    
    projects = st.number_input("Projects", 0)
    hackathons = st.number_input("Hackathons", 0)
    papers = st.number_input("Papers", 0)
    
    placed = st.checkbox(label = "Select", value ="Placed")
    # https://docs.streamlit.io/develop/api-reference/widgets
    company = st.text_input("Company")
    salary = st.number_input("Salary", 0.0)
    
    company_type = st.selectbox(
        "Company Type",
        ["Product", "Service", "Support"]
    )
    
    if st.button("Add Student"):
        data = {
            "name": name,
            "tenth": tenth,
            "twelfth": twelfth,
            "be_cgpa": cgpa,
            "skills": skills,
            "domain": domain,
            "projects": projects,
            "hackathons": hackathons,
            "papers": papers,
            "placed": placed,
            "company": company,
            "salary": salary,
            "company_type": company_type
        }
    
        res = add_student(data)
    
        if res.status_code == 200:
            st.success("Student added ✅")
            st.json(res.json())
        else:
            st.error(res.text)

with tab2:
    st.subheader("✏️ Update Student")

    # Load students for dropdown
    res = get_students()
    
    if res.status_code == 200:
        students = res.json()
    
        if students:
            student_map = {f"{s['id']} - {s['name']}": s for s in students}
    
            selected = st.selectbox("Select Student", list(student_map.keys()))
            data = student_map[selected]
    
            student_id = data["id"]
    
            # Pre-filled form
            name = st.text_input("Name", value=data.get("name", ""))
            tenth = st.number_input("10th %", 0.0, 100.0, value=float(data.get("tenth", 0)))
            twelfth = st.number_input("12th %", 0.0, 100.0, value=float(data.get("twelfth", 0)))
            cgpa = st.number_input("BE CGPA", 0.0, 10.0, value=float(data.get("be_cgpa", 0)))
    
            skills = st.text_input("Skills", value=data.get("skills", ""))
            domain = st.text_input("Domain", value=data.get("domain", ""))
    
            projects = st.number_input("Projects", 0, value=int(data.get("projects", 0)))
            hackathons = st.number_input("Hackathons", 0, value=int(data.get("hackathons", 0)))
            papers = st.number_input("Papers", 0, value=int(data.get("papers", 0)))
    
            placed = st.checkbox("Placed", value=data.get("placed", False))
    
            company = st.text_input("Company", value=data.get("company", ""))
            salary = st.number_input("Salary", 0.0, value=float(data.get("salary", 0)))
    
            company_type = st.selectbox(
                "Company Type",
                ["Product", "Service", "Support"],
                index=["Product", "Service", "Support"].index(data.get("company_type", "Product"))
            )
    
            if st.button("Update Student"):
    
                update_data = {
                    "name": name,
                    "tenth": tenth,
                    "twelfth": twelfth,
                    "be_cgpa": cgpa,
                    "skills": skills,
                    "domain": domain,
                    "projects": projects,
                    "hackathons": hackathons,
                    "papers": papers,
                    "placed": placed,
                    "company": company if company else None,
                    "salary": salary if placed else None,
                    "company_type": company_type if placed else None
                }
    
                res = update_student(student_id, update_data)
    
                if res.status_code == 200:
                    st.success("Student updated ✅")
                    st.json(res.json())
                else:
                    st.error(res.text)
    
        else:
            st.warning("No students found")
    
    else:
        st.error("Failed to fetch students")
