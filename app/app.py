import streamlit as st
import pandas as pd
import plotly.express as px

from utils import calculate_linkedin_followers, calculate_medium_followers

st.set_page_config(page_title="FollowDash", page_icon="📊", layout="wide")

# Dictionary of follower counts
followers_data = {"LinkedIn": "0",
                  "Medium": "0",
                  "Substack": "100",
                  "X": "100"}

show_metrics = False

st.title("Followers Dashboard 👥")
st.divider()


if st.button("Fetch Latest Metrics ⚡", use_container_width=True):
    with st.spinner("Fetching Followers..."):
        try:
            linkedin_followers = calculate_linkedin_followers()
            medium_followers = calculate_medium_followers()
            followers_data["LinkedIn"] = linkedin_followers
            followers_data["Medium"] = medium_followers
            st.success("Success! Here’s the updated metrics")
            show_metrics = True
        except Exception:
            st.error("Failed to fetch followers. Please Retry ➰")

if show_metrics:

    # Convert follower counts to numbers
    for platform, count in followers_data.items():
        if "K" in count:
            followers_data[platform] = float(count.replace("K", "")) * 1000
        else:
            followers_data[platform] = float(count)

    # Convert the dictionary to a DataFrame
    followers_df = pd.DataFrame(
        list(followers_data.items()), columns=["Platform", "Followers"]
    )

    # Total followers KPI with emoji
    total_followers = followers_df["Followers"].sum()
    st.markdown(
        f"### 🎯 Total Followers: {int(total_followers)} 📊",
        unsafe_allow_html=True)
    st.divider()
    # st.metric(label="✨ Total Followers", value=int(total_followers))

    st.write("### 📝 DataFrame")
    st.dataframe(followers_df)
    st.divider()

    st.write("### 📈 Distribution By Platform")
    col1, col2 = st.columns(2)

    # Bar chart in the first column
    with col1:
        # st.write("#### 📊 Distribution By Platform (Bar Chart)")
        bar_chart = px.bar(
            followers_df,
            x="Platform",
            y="Followers",
            color="Platform",
            labels={"Followers": "Number of Followers"},
            title="Bar Chart",
        )
        st.plotly_chart(bar_chart, use_container_width=True)

    # Pie chart in the second column
    with col2:
        # st.write("#### 🥧 Followers Distribution (Pie Chart)")
        pie_chart = px.pie(
            followers_df,
            values="Followers",
            names="Platform",
            hole=0.3,
            title="Pie Chart",
        )
        st.plotly_chart(pie_chart, use_container_width=True)
