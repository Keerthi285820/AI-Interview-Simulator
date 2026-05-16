import streamlit as st 
from questions import questions
st.title("🤖 AI Interview Simulator")
st.write("Practice interviews and get instant feedback!")
role = st.selectbox(
    "Choose Interview Topic",
    list(questions.keys())
)
st.subheader(f"Interview Questions for {role}")
score = 0
total_questions = len(questions[role])
for idx, q in enumerate(questions[role]):
    st.write(f"### Q{idx + 1}: {q['question']}")
    answer = st.text_area(
        f"Your Answer for Q{idx+1}",
        key=idx
    )
    if answer:
        matched_keywords = 0
        for keyword in q["keywords"]:
            if keyword.lower() in answer.lower():
                matched_keywords += 1
        question_score = (
            matched_keywords / len(q["keywords"]))*100
        st.write(f"Score: {question_score:.0f}%")
        if question_score >= 70:
            st.success("Excellent Answer ✅")
            score += 1
        elif question_score >= 40:
            st.warning("Good attempt 👍 Add more important concepts.") 
        else:
            st.error("Needs Improvement🚀")    
        st.write("Important Concepts:") 
        st.write(",".join(q["keywords"]))      
if st.button("Submit Interview"):
    st.subheader("📊 Final Performance") 
    final_score = (
        score / total_questions) * 100
    st.write(f"Final Score: {final_score:.0f}%")
    if final_score >= 80:
        st.success("Outstanding Performance🎉")  
    elif final_score >=60:
        st.warning("Good Job! Keep Practicing👍")
    else:
        st.error("Don't Worry! Practice Makes Perfect🚀")
    