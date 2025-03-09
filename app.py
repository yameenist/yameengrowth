#streamlit
import streamlit as st
import random
import time

# Function to provide encouraging feedback based on user progress
def growth_mindset_feedback(progress):
    if progress == "Not Started":
        return "Great! You are about to embark on a journey of growth. Start by setting your first goal!"
    elif progress == "In Progress":
        return "Awesome! Keep going, you're making progress. Remember, challenges are opportunities to learn."
    elif progress == "Completed":
        return "Fantastic! You've achieved your goal. Reflect on what you've learned and think about your next challenge."
    else:
        return "Hmm, something went wrong. Try again!"

# Function to generate a random motivational quote
def random_motivation():
    quotes = [
        "Believe you can and you're halfway there.",
        "Success is the sum of small efforts, repeated day in and day out.",
        "The only way to do great work is to love what you do.",
        "Your limitation—it’s only your imagination.",
        "Push yourself, because no one else is going to do it for you.",
        "Great things never come from comfort zones.",
        "Dream it. Wish it. Do it."
    ]
    return random.choice(quotes)

# Function to show celebration when goal is completed
def celebrate_win():
    st.balloons()  # Streamlit built-in function to show balloons
    st.markdown(
        """
        <div style="text-align:center; font-size: 30px; font-weight: bold; color: #28a745;">
            Congratulations! 🎉 You've completed your goal!
        </div>
        """, unsafe_allow_html=True)
    st.markdown(
        """
        <div style="text-align:center; font-size: 20px; font-style: italic; color: #6c757d;">
            You are one step closer to your dreams. Keep going, the sky's the limit!
        </div>
        """, unsafe_allow_html=True)

# Function to set up the growth mindset challenge
def growth_mindset_challenge():
    # Custom Styling for background, fonts, etc.
    st.markdown(
        """
        <style>
        .main {
            background-color: #f7f7f7;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        }
        .quote {
            font-size: 24px;
            font-style: italic;
            color: #2e6da4;
            text-align: center;
            padding: 1rem 0;
        }
        .title {
            text-align: center;
            color: #d9534f;
            font-size: 40px;
            font-weight: bold;
            letter-spacing: 2px;
        }
        .goal-input {
            margin-top: 1rem;
            padding: 1rem;
            border-radius: 10px;
            background-color: #e9ecef;
            border: 1px solid #ddd;
            width: 100%;
        }
        .progress-select {
            margin-top: 1rem;
            padding: 0.8rem;
            border-radius: 10px;
            background-color: #f0f0f0;
        }
        .feedback {
            font-size: 18px;
            font-weight: bold;
            color: #3c763d;
            background-color: #dff0d8;
            border: 1px solid #d0e9c6;
            padding: 1rem;
            border-radius: 10px;
            margin-top: 1rem;
        }
        .add-goal {
            font-size: 16px;
            margin-top: 2rem;
            text-align: center;
        }
        </style>
        """, unsafe_allow_html=True
    )
    
    # Display a motivational quote at the top
    st.markdown('<div class="quote">"The journey of a thousand miles begins with one step."</div>', unsafe_allow_html=True)

    st.markdown('<div class="title">Growth Mindset Challenge</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="main">', unsafe_allow_html=True)
    
    # Ask user to input their challenge goal
    goal = st.text_input("What is your challenge goal?", key="goal", placeholder="E.g., Learn Python")

    if goal:
        st.write(f"Your challenge goal: **{goal}**")

        # Choose progress status
        progress = st.selectbox(
            "What's your current progress?",
            ["Not Started", "In Progress", "Completed"],
            key="progress",
            help="Select the progress stage of your goal",
            format_func=lambda x: f"{x}",
        )

        # Provide feedback based on progress
        feedback = growth_mindset_feedback(progress)
        st.markdown(f'<div class="feedback">{feedback}</div>', unsafe_allow_html=True)

        # Celebrate when the user completes their goal
        if progress == "Completed":
            celebrate_win()

            # Show additional motivation
            time.sleep(2)  # Slight delay before showing the motivation
            motivation = random_motivation()
            st.markdown(f'<div style="text-align:center; font-size: 22px; color: #007bff; font-weight: bold;">{motivation}</div>', unsafe_allow_html=True)

        # Give an option to add more goals
        add_more_goals = st.checkbox("Add another goal", key="add_more")
        if add_more_goals:
            st.text_input("New Goal", key="new_goal", placeholder="What will be your next goal?")
        
    else:
        st.write("Please enter your challenge goal!")

    st.markdown('</div>', unsafe_allow_html=True)


# Main app
if __name__ == "__main__":
    growth_mindset_challenge()
