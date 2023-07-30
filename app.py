import streamlit as st
from pathlib import Path
from PIL import Image
from streamlit_extras.mention import mention



# !----- Path Settings -----

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "style" / "main.css"
resume_file = current_dir / "assets" / "Rahul_Resume.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"



# !----- General Settings ---

Page_Title = "Rahul's Resume"
Page_Icon = "📄"
Name = "Rahul Sharma"
Description = """:orange[Ex-Software Engineer Intern at Microsoft] | B.Tech in Computer Science and Artificial Intelligence | Expert at Codeforces | Max 4⭐ at Codechef"""
Email = "lci2020029@iiitl.ac.in"
Social_Media = {
    "LinkedIn": "https://www.linkedin.com/in/rahul-sharma-2bba60203/",
    "GitHub": "https://github.com/The1one1",
    # "Twitter": "https://twitter.com/RahulSharma_1",
    # "Youtube": "https://www.youtube.com/@informationclub8300",
}

Projects = {
    "✅ DressMate": {
        "https://github.com/The1one1/DressMate.git": "Clothing recommendation system that provides accurate and personalized recommendations. It includes a :orange[***virtual try-on feature***] that produces realistic and visually appealing virtual try-ons.",
        ":green[Tech Stack]": "Python, Streamlit, TensorFlow, ResNet50, Pinecone",
        "Repository Link": "https://github.com/The1one1/DressMate.git",
        "Demo Link": "https://www.linkedin.com/feed/update/urn:li:activity:7056917973499867136?utm_source=share&utm_medium=member_android",
    },
    "✅ Movie Recommendation System": {
        "https://github.com/The1one1/Movie_Recommendation_System.git": "It recommends the movies on the basis of movies selected by user.",
        ":green[Tech Stack]": "Python, Streamlit, Pandas, Numpy, Scikit-learn",
        "Respository Link": "https://github.com/The1one1/Movie_Recommendation_System.git",
        "App Link": "https://the1one1-resume-formate-app-xawhlf.streamlit.app/",
    },
}

Experience = {
    " ✅ Microsoft": {
        "https://www.linkedin.com/company/microsoft/": "Software Engineer Intern",
        # add content in decsription in points with :blue[Description] and add new line with and the description is Worked on the development of Data Loss Prevention (DLP) policies. ◦ Created a Dynamic Link Library (DLL) to recommend Sensitive Information Type (SIT)
        ":green[Description]": "Worked on the development of Data Loss Prevention (DLP) policies. Created a :orange[Dynamic Link Library (DLL)] to recommend :orange[Sensitive Information Type (SIT)].",
        ":green[Duration]": "May 2021 - July 2021",
        ":green[Tech Stack]": "C#, XML, Microsoft Azure Cognitive Services, Rest API, XAML",
        ":blue[Certificate]": "https://drive.google.com/file/d/1ebsILg7vuLgaFwvYIRz4neUqIb5a3yW5/view?usp=sharing",
    },
}

st.set_page_config(page_title=Page_Title, page_icon=Page_Icon, layout="centered")




# ! ----CSS file, PDF and Profile Pic -----

with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()


profile_pic = Image.open(profile_pic)




# !-- HEro Section --
col1, col2 = st.columns([1, 1], gap="small")

with col1:
    st.image(profile_pic, width=400)

with col2:
    st.title(Name)
    items = Description.split("|")
    
    for item in items:
        st.write(f"✅ {item}")

    # add direct link to download resume


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

with cols[0]:
    mention(
        label="LinkedIn",
        # icon="LinkedIn",
        url="https://www.linkedin.com/in/rahul-sharma-2bba60203/",
    )

with cols[1]:
    mention(
        label="github",
        icon="github",
        url="https://github.com/The1one1",
    )





# !--- Education Section ---

st.write("#")
st.write("## Education 🎓")
st.write("---")

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




# ! --- Experience Section ---

st.write("#")
st.subheader("Experience 🏢 ")
st.write("---")
for name, detail in Experience.items():
    col1, col2 = st.columns([1, 2])
    link = list(detail.keys())
    description = list(detail.values())
    with col1:
        st.write(f"[{name}]({link[0]})")
    with col2:
        st.write(description[0])
        st.write(f"{link[1]} : {description[1]}")
        st.write(f"{link[2]} : {description[2]}")
        st.write(f"{link[3]} : {description[3]}")
        st.write(f"[{link[4]}]({description[4]})")
        st.write("---")

st.write(
    """
    ✅  Strong hands on experience in Machine Learning and Deep Learning
    """
)




# !--- Projects Section ---

st.write("#")
st.subheader("Projects 📚")
st.write("---")
for name, detail in Projects.items():
    col1, col2 = st.columns([1, 2])
    link = list(detail.keys())
    description = list(detail.values())
    with col1:
        st.write(f"[{name}]({link[0]})")
    with col2:
        st.write(description[0])
        st.write(f"{link[1]} : {description[1]}")
        st.write(f"[{link[2]}]({description[2]})")
        st.write(f"[{link[3]}]({description[3]})")
        
        # add new line with --- and add this only if there is a new project
        if name != "✅ Movie Recommendation System":
            st.write("---")







# !---Skills Section ---
st.write("#")
st.subheader("Technical Skills 💻")
st.write("---")
    # - ✅  :green[Database]: MySQL, MongoDB
st.write(
    """
    - ✅  :green[Programming]: Python (TensorFlow, scikit-learn, pandas, numpy), C++, c#, XML
    - ✅  Machine Learning and Deep Learning
    - ✅  :green[Technologies]: Git, [Github](https://github.com/The1one1), Microsft Azure DecOps, Azure Machine Learning, [Google Cloud](https://drive.google.com/file/d/1tY1qlHoWfRiN3mS7_JDYeozE4g1oqGqh/view?usp=drivesdk/), Jupyter Notebook, Visual Studio, Sublime Text
    - ✅  :green[Frameworks]: Streamlit
    """
)

# !--- Coding Section ---
    # - ✅  [HackerRank]( https://www.hackerearth.com/@rahul9038/)
st.write("#")
st.subheader("Coding Profiles 📝")
st.write("---")
st.write(
    """
    - ✅  [CodeForces Expert Account]( https://codeforces.com/profile/brickiq)
    - ✅  [Codeforces Practice Account:]( https://codeforces.com/profile/Aswathama./)
    - ✅  [LeetCode]( https://leetcode.com/Ra1Sharma/)
    - ✅  [CodeChef]( https://www.codechef.com/users/rahul_00101/)
    """
)
    # - ✅  [GeeksForGeeks]( https://auth.geeksforgeeks.org/user/rahulsharma22459/profile/)