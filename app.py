from pathlib import Path
import streamlit as st
from PIL import Image


# !----- Path Settings -----

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "style" / "main.css"
resume_file = current_dir / "assets" / "Rahul_Resume.pdf"
profile_pic = current_dir / "assets" / "profile-pic.jpeg"


# !----- General Settings ---

Page_Title = "Rahul's Resume"
Page_Icon = "📄"
Name = "Rahul Sharma"
Description = """Upcommig Software Engineer Intern at Microsoft"""
Email = "lci2020029@iiitl.ac.in"
Social_Media = {
    "LinkedIn": "https://www.linkedin.com/in/rahul-sharma-2bba60203/",
    "GitHub": "https://github.com/The1one1",
    # "Twitter": "https://twitter.com/RahulSharma_1",
    # "Youtube": "https://www.youtube.com/@informationclub8300",
}

Projects = {
    "✅ Movie Recommendation System": {
        "https://github.com/The1one1/Movie_Recommendation_System.git": "It recommends the movies on the basis of movies selected by user.",
        ":blue[Tech Stack]": "Python, Streamlit, Pandas, Numpy, Scikit-learn"
    },
    "✅ Excel File reader": {
        "https://github.com/The1one1/Excel-file-reader.git": "It reads the excel file and gives the output in the form of a table.",
        ":blue[Tech Stack]": "Python, Streamlit, Pandas, Numpy,"
    }
}


st.set_page_config(page_title=Page_Title,
                   page_icon=Page_Icon, layout="centered")



# ! ----CSS file, PDF and Profile Pic -----

with open(css_file) as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()


profile_pic = Image.open(profile_pic)


# !-- HEro Section --
col1, col2 = st.columns([1, 1], gap="small")

with col1:
    st.image(profile_pic, width=200)

with col2:
    st.title(Name)
    st.write(Description)
    st.download_button(
        label="Download Resume",
        data=PDFbyte,
        file_name="Rahul_Resume.pdf",
        mime="application/pdf",
    )
    st.write("Email: ", Email)



# ! --- Social Media Section ---

st.write("#")
cols = st.columns([1, 1])

for index, (name, link) in enumerate(Social_Media.items()):
    cols[index].write(f"[{name}]({link})")



# !--- Education Section ---

st.write("#")
st.write("## Education 🎓")
st.write('---')

col1, col2 = st.columns([4, 1])

with col1:
    st.write(
        """
        - ✅ [Indian Institute of Information Technology](https://iiitl.ac.in/), Lucknow
        - B.Tech in Computer Science and Artificial Intelligence
        """
    )
with col2:
    st.write(
        """
        - 2020  --------
        - CGPA: 8.02
        """
    )


col1, col2 = st.columns([4, 1])

with col1:
    st.write(
        """
        - ✅ :blue[Orange County School], Rajsamand, Rajasthan
        - $12^{th} Percentage: 86.7%$
        """
    )



# !--- Projects Section ---

st.write("#")
st.subheader("Projects 📚")
st.write('---')
for name, detail in Projects.items():
    col1, col2 = st.columns([1, 2])
    link = list(detail.keys())
    description = list(detail.values())
    with col1:
        st.write(f"[{name}]({link[0]})")
    with col2:
        st.write(description[0])
        st.write(f"{link[1]} : {description[1]}")



# ! --- Experience Section ---

st.write("#")
st.subheader("Experience 🏢 ")
st.write('---')
st.write(
    """
    - ✅  Upcoming Software Engineer Intern at Microsoft
    - ✅  Strong hands on experience in Machine Learning and Deep Learning
    """
)


# !---Skills Section ---
st.write("#")
st.subheader("Hard Skills 💻")
st.write('---')
st.write(
    """
    - ✅  Programming: Python (scikit-learn, pandas, numpy), C++, SQL
    - ✅  Machine Learning and Deep Learning
    - ✅  Database: MySQL, MongoDB
    - ✅  Technologies: Git, [Github](https://github.com/The1one1), [Google Cloud](https://drive.google.com/file/d/1tY1qlHoWfRiN3mS7_JDYeozE4g1oqGqh/view?usp=drivesdk/), Jupyter Notebook, Vs Code, Sublime Text
    - ✅  Frameworks: Streamlit
    """
)

# !--- Coding Section ---
st.write("#")
st.subheader("Coding Profiles 📝")
st.write('---')
st.write(
    """
    - ✅  [CodeForces]( https://codeforces.com/profile/Aswathama./)
    - ✅  [LeetCode]( https://leetcode.com/Ra1Sharma/)
    - ✅  [CodeChef]( https://www.codechef.com/users/rahul_00101/)
    - ✅  [HackerRank]( https://www.hackerearth.com/@rahul9038/)
    - ✅  [GeeksForGeeks]( https://auth.geeksforgeeks.org/user/rahulsharma22459/profile/)
    """
)