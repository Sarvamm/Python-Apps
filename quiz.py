import streamlit as st
import random

# Set page configuration
st.set_page_config(
    page_title="Quiz App",
    page_icon="❓",
    layout="centered"
)

# Initialize session state variables if they don't exist
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'quiz_complete' not in st.session_state:
    st.session_state.quiz_complete = False
if 'questions' not in st.session_state:
    # Sample quiz questions - you can replace these with your own
    st.session_state.questions = [
        {
            "question": "What is the capital of France?",
            "options": ["London", "Berlin", "Paris", "Madrid"],
            "correct": 2  # Paris (index 2)
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Venus", "Mars", "Jupiter", "Saturn"],
            "correct": 1  # Mars (index 1)
        },
        {
            "question": "What is 2 + 2?",
            "options": ["3", "4", "5", "6"],
            "correct": 1  # 4 (index 1)
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"],
            "correct": 1  # Shakespeare (index 1)
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
            "correct": 3  # Pacific (index 3)
        }
    ]

# Function to handle answer submission
def check_answer(selected_index):
    correct_index = st.session_state.questions[st.session_state.current_question]["correct"]
    if selected_index == correct_index:
        st.session_state.score += 1
    
    # Move to next question or end quiz
    if st.session_state.current_question < len(st.session_state.questions) - 1:
        st.session_state.current_question += 1
    else:
        st.session_state.quiz_complete = True

# Function to restart quiz
def restart_quiz():
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.quiz_complete = False
    # Shuffle questions for variety
    random.shuffle(st.session_state.questions)

# App header
st.title("📚 Quiz App")
st.markdown("---")

# Display quiz or results based on state
if not st.session_state.quiz_complete:
    # Display progress
    progress = (st.session_state.current_question) / len(st.session_state.questions)
    st.progress(progress)
    st.write(f"Question {st.session_state.current_question + 1} of {len(st.session_state.questions)}")
    
    # Display current question
    current_q = st.session_state.questions[st.session_state.current_question]
    st.subheader(current_q["question"])
    
    # Display options as buttons
    for i, option in enumerate(current_q["options"]):
        if st.button(option, key=f"option_{i}"):
            check_answer(i)
            st.rerun()
else:
    # Quiz complete - show results
    st.subheader("Quiz Complete! 🎉")
    
    # Calculate percentage
    percentage = (st.session_state.score / len(st.session_state.questions)) * 100
    
    # Display score with appropriate emoji
    if percentage >= 80:
        st.success(f"Your score: {st.session_state.score}/{len(st.session_state.questions)} ({percentage:.1f}%) 🌟")
    elif percentage >= 60:
        st.info(f"Your score: {st.session_state.score}/{len(st.session_state.questions)} ({percentage:.1f}%) 👍")
    else:
        st.warning(f"Your score: {st.session_state.score}/{len(st.session_state.questions)} ({percentage:.1f}%) 📚")
    
    # Add some encouragement
    if percentage == 100:
        st.balloons()
        st.write("Perfect score! Impressive! 🏆")
    elif percentage >= 80:
        st.write("Great job! You really know your stuff! 👏")
    elif percentage >= 60:
        st.write("Good effort! Keep learning! 📖")
    else:
        st.write("Keep practicing! You'll improve with time. 💪")
    
    # Option to restart
    if st.button("Restart Quiz"):
        restart_quiz()
        st.rerun()

# Add a sidebar with instructions
with st.sidebar:
    st.header("Instructions")
    st.write("1. Read each question carefully")
    st.write("2. Click on the option you think is correct")
    st.write("3. See your final score at the end")
    st.write("4. Try to beat your previous score!")
    
    # Add a customization section
    st.header("Customization")
    if st.button("Shuffle Questions"):
        random.shuffle(st.session_state.questions)
        st.rerun()