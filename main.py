import streamlit as st
import json
from prompt import recommend, llm
st.title("Student Recommendation System")

#get strengths, weaknesses and recommendations
strengths = json.load(open("./data/interim/strengths.json"))
weaknesses = json.load(open("./data/interim/weaknesses.json"))
recommend = recommend.format(strengths = strengths, weaknesses = weaknesses)
result = llm.invoke(recommend)

def show_visualizations():
    st.header("Recent Quiz Analysis")
    col1, col2 = st.columns(2)
    image1 = "./visualizations\Questions Analysis.png"
    image2 = "./visualizations\Score Analysis.png"
    # Display images in the columns
    with col1:
        st.image(image1, use_container_width=True)

    with col2:
        st.image(image2, use_container_width=True)
    
def show_details(strengths, weaknesses):
    # Display strengths
    strengths = strengths['strengths']
    st.header("Strengths")
    st.markdown(f"{strengths['description']}")
    st.write("**Strong Topics:**")
    for topic in strengths['topics']:
        st.markdown(f"- {topic}")

    # Display weaknesses
    st.header("Weaknesses")
    weaknesses = weaknesses['weaknesses']
    st.markdown(f"{weaknesses['description']}")
    st.write("**Weak Topics:**")
    for topic in weaknesses['topics']:
        st.markdown(f"- {topic}")

def show_impovements():
    #display improvements
    st.header("Suggested Improvements")
    st.write(result.content)

show_visualizations()
show_details(strengths, weaknesses)
show_impovements()