import streamlit as st
import random
import datetime
import pandas as pd
import os


# ---------------------- Sidebar Navigation ----------------------
st.sidebar.title("🌱 Growth Mindset App")
st.sidebar.markdown("---")

page = st.sidebar.radio("Navigate to:", [
    "Home", "Motivational Videos", "Daily Challenge", "Journal & Reflection", "Progress Tracker"
])

# ---------------------- Home Page ----------------------
if page == "Home":
    st.title("🚀 Welcome to Your Growth Journey!")
    st.image("image.jpg", width=200, use_container_width=False)
    
    st.markdown("## 🌟 Daily Motivation")
    quotes = [
        "The only limit to our realization of tomorrow is our doubts of today.",
        "Success is not final, failure is not fatal: it is the courage to continue that counts.",
        "Your only limit is your mind.",
        "Difficulties strengthen the mind, as labor does the body.",
        "Growth and comfort do not coexist."
    ]
    st.success(random.choice(quotes))

# ---------------------- Motivational Video Recommender ----------------------
elif page == "Motivational Videos":
    st.title("🎥 Motivational Videos")
    st.write("Select a topic to get a recommended motivational video!")

    topics = {
        "Overcoming Failure": "https://www.youtube.com/watch?v=hzBCI13rJmA",
        "Self-Confidence Boost": "https://youtu.be/l_NYrWqUR40?si=F-88W13dytEUQnH6",
        "Power of Positive Thinking": "https://youtu.be/PFuRKDD4kH4?si=6dup3kaN_szFfADP",
        "Developing a Growth Mindset": "https://www.youtube.com/watch?v=KUWn_TJTrnU"
    }

    choice = st.selectbox("Choose a topic:", list(topics.keys()))

    if st.button("Get Video"):
        st.video(topics[choice])
        st.success("Enjoy the video and stay motivated! 🚀")

# ---------------------- Daily Growth Challenge ----------------------
elif page == "Daily Challenge":
    st.title("🎯 Daily Growth Challenge")
    
    challenges = [
        "Write down three things you are grateful for.",
        "Try a new skill for 10 minutes today.",
        "Reflect on a recent failure and list what you learned.",
        "Give yourself a positive affirmation and repeat it 5 times.",
        "Do something outside your comfort zone today."
    ]
    
    challenge = challenges[datetime.date.today().day % len(challenges)]
    st.info(f"**Your Challenge:** {challenge}")
    
    if st.button("Mark as Completed"):
        st.success("Great job! Keep growing! 🌱")

# ---------------------- Journal & Reflection ----------------------
elif page == "Journal & Reflection":
    st.title("📖 Personal Growth Journal")
    user_journal = st.text_area("Write about today's mindset experience:")

    if st.button("Save Entry"):
        if user_journal.strip():
            if not os.path.exists("journal_entries.csv"):
                df = pd.DataFrame(columns=["Date", "Entry"])
                df.to_csv("journal_entries.csv", index=False)
            
            df = pd.read_csv("journal_entries.csv")
            new_entry = pd.DataFrame({"Date": [datetime.date.today()], "Entry": [user_journal]})
            df = pd.concat([df, new_entry], ignore_index=True)
            df.to_csv("journal_entries.csv", index=False)
            st.success("Your reflection has been saved! 💡")
        else:
            st.warning("Please enter some text before saving!")

# ---------------------- Progress Tracker ----------------------
elif page == "Progress Tracker":
    st.title("🔥 Streak Tracker")
    
    if os.path.exists("journal_entries.csv"):
        df = pd.read_csv("journal_entries.csv")
        df["Date"] = pd.to_datetime(df["Date"])
        df = df.sort_values(by="Date")
        
        streak = 0
        max_streak = 0
        prev_date = None
        
        for date in df["Date"]:
            if prev_date is None or (date - prev_date).days == 1:
                streak += 1
            else:
                streak = 1
            max_streak = max(max_streak, streak)
            prev_date = date
        
        st.write(f"### 🔥 Current Streak: {streak} days")
        st.write(f"### 🏆 Longest Streak: {max_streak} days")
    else:
        st.warning("No journal entries found! Start writing to track progress.")


# ---------------------- Footer ----------------------
st.sidebar.markdown("---")  
st.sidebar.write("Made with ❤️ using Streamlit")
