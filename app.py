import streamlit as st
from questions import questions
from evaluator import evaluate_answer
st.title("🤖 AI Interview Simulator")
st.write("AI-powered interview evaluation system")
role = st.selectbox(
    "Choose Interview Topic",
    list(questions.keys())
)
st.subheader(f"{role} Interview")
total_score = 0
total_questions = len(questions[role])
for idx, q in enumerate(questions[role]):
    st.write(f"### Q{idx+1}: {q['question']}")
    answer = st.text_area(
        f"Your Answer for Q{idx+1}",
        key=idx
    )
    if answer:
        score = evaluate_answer(
            answer,
            q["expected_answer"]
        )
        total_score += score
        st.write(f"Similarity Score: {score:.2f}%")
        if score >= 75:
            st.success("Excellent Answer ✅")
        elif score >= 50:
            st.warning("Good Attempt 👍")
        else:
            st.error("Needs Improvement 🚀")
        st.write("Expected Concept:")
        st.info(q["expected_answer"])
if st.button("Submit Interview"):
    final_score = total_score / total_questions
    st.subheader("📊 Final Performance")
    st.write(f"Final Score: {final_score:.2f}%")
    if final_score >= 80:
        st.success("Outstanding Performance 🎉")
    elif final_score >= 60:
        st.warning("Good Performance 👍")
    else:
        st.error("Keep Practicing 🚀")
    
