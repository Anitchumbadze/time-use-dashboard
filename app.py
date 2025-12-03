import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Time Use Dashboard", layout="wide")

st.title("Time Use Dashboard")

df = pd.read_csv("Time-Use-in-OECD-Countries-OECD - Time Use (OECD).csv")

countries = ["China", "USA"]

categories = [
    "Paid work",
    "Education",
    "Care for household members",
    "Housework",
    "Shopping",
    "Other unpaid work & volunteering",
    "Sleep",
    "Eating and drinking",
    "Personal care",
    "Sports",
    "Attending events",
    "Seeing friends",
    "TV and Radio",
    "Other leisure activities"
]

subset = df[(df["Country"].isin(countries)) & (df["Category"].isin(categories))]

pivot = subset.pivot_table(
    index="Category",
    columns="Country",
    values="Time (minutes)"
)

st.header("China vs USA: Time Use Across Daily Activities")
st.bar_chart(pivot)

st.set_page_config(page_title="Time Use Dashboard", layout="wide")
st.title("Time Use Dashboard")

df = pd.read_csv("Time-Use-in-OECD-Countries-OECD - Time Use (OECD).csv")

countries = ["China", "USA"]

subset = df[df["Country"].isin(countries)]

pivot = subset.pivot_table(
    index="Category",
    columns="Country",
    values="Time (minutes)",
    aggfunc="mean"
)
st.subheader("Minutes per day by activity (China vs USA)")
st.dataframe(pivot)


st.subheader("Top 3 Time-Consuming Activities")

china_top3 = pivot["China"].sort_values(ascending=False).head(3)
usa_top3 = pivot["USA"].sort_values(ascending=False).head(3)

col1, col2 = st.columns(2)

with col1:
    st.write("### China — Top 3 Activities")
    fig_china = px.bar(
        china_top3,
        x=china_top3.values,
        y=china_top3.index,
        orientation="h",
        labels={"x": "Minutes per day", "y": "Activity"},
        color=china_top3.values,
        color_continuous_scale="Blues"
    )
    st.plotly_chart(fig_china, use_container_width=True)

with col2:
    st.write("### USA — Top 3 Activities")
    fig_usa = px.bar(
        usa_top3,
        x=usa_top3.values,
        y=usa_top3.index,
        orientation="h",
        labels={"x": "Minutes per day", "y": "Activity"},
        color=usa_top3.values,
        color_continuous_scale="Reds"
    )
    st.plotly_chart(fig_usa, use_container_width=True)

st.subheader("Lifestyle Balance: Productive vs Well-being vs Leisure")

group_map = {
    "Paid work": "Productive",
    "Education": "Productive",
    "Care for household members": "Well-being",
    "Housework": "Productive",
    "Shopping": "Productive",
    "Other unpaid work & volunteering": "Productive",
    "Sleep": "Well-being",
    "Eating and drinking": "Well-being",
    "Personal care": "Well-being",
    "Sports": "Leisure",
    "Attending events": "Leisure",
    "Seeing friends": "Leisure",
    "TV and Radio": "Leisure",
    "Other leisure activities": "Leisure",
}

grouped = pivot.copy()
grouped["Group"] = grouped.index.to_series().map(group_map)

china_group = grouped.groupby("Group")["China"].sum().reindex(
    ["Productive", "Well-being", "Leisure"]
)
usa_group = grouped.groupby("Group")["USA"].sum().reindex(
    ["Productive", "Well-being", "Leisure"]
)

col1, col2 = st.columns(2)

with col1:
    st.write("### China — Lifestyle Balance")
    fig1 = px.pie(
        values=china_group.values,
        names=china_group.index,
        hole=0.5,
        color=china_group.index,
        color_discrete_map={
            "Productive": "#1f77b4",
            "Well-being": "#2ca02c",
            "Leisure": "#d62728",
        },
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.write("### USA — Lifestyle Balance")
    fig2 = px.pie(
        values=usa_group.values,
        names=usa_group.index,
        hole=0.5,
        color=usa_group.index,
        color_discrete_map={
            "Productive": "#1f77b4",
            "Well-being": "#2ca02c",
            "Leisure": "#d62728",
        },
    )
    st.plotly_chart(fig2, use_container_width=True)

st.subheader("Which Country Spends More Time on Each Activity?")

winner_df = pivot.copy()
winner_df["Winner"] = winner_df.apply(
    lambda row: "China" if row["China"] > row["USA"] else "USA",
    axis=1,
)

fig = px.bar(
    winner_df,
    x=winner_df.index,
    y=winner_df[["China", "USA"]].max(axis=1),
    color="Winner",
    color_discrete_map={"China": "#d62728", "USA": "#1f77b4"},
    labels={"x": "Activity", "y": "Minutes per day"},
)

fig.update_layout(xaxis_tickangle=45)
st.plotly_chart(fig, use_container_width=True)








df_leisure = pd.read_csv("time-women-and-men-spend-on-leisure/time-women-and-men-spend-on-leisure.csv")


df_2020 = df_leisure[df_leisure["Year"] == 2020]


gender_df = df_2020[df_2020["Entity"].isin(["China", "United States"])].copy()


gender_df["Women"] = gender_df[
    "Minutes spent on leisure - women (OECD Gender data (2020))"
]
gender_df["Men"] = gender_df[
    "Minutes spent on leisure - men (OECD Gender data (2020))"
]


gender_df["Total leisure (avg)"] = (gender_df["Women"] + gender_df["Men"]) / 2
gender_df["Gap (men - women)"] = gender_df["Men"] - gender_df["Women"]
gender_df["Women share %"] = (
    gender_df["Women"] / (gender_df["Women"] + gender_df["Men"]) * 100
)


min_val = min(gender_df["Men"].min(), gender_df["Women"].min()) - 10
max_val = max(gender_df["Men"].max(), gender_df["Women"].max()) + 10

st.subheader("Men vs Women: Leisure Time (China vs USA)")

fig_leisure = px.scatter(
    gender_df,
    x="Men",
    y="Women",
    size="Total leisure (avg)",          
    color="Entity",                      
    text="Entity",                      
    hover_name="Entity",
    hover_data={
        "Men": True,
        "Women": True,
        "Gap (men - women)": True,
        "Women share %": ":.1f",
        "Total leisure (avg)": False,
    },
    labels={
        "Men": "Men's leisure (minutes per day)",
        "Women": "Women's leisure (minutes per day)",
    },
)

fig_leisure.add_shape(
    type="line",
    x0=min_val, y0=min_val,
    x1=max_val, y1=max_val,
    line=dict(color="lightgray", dash="dash"),
)


fig_leisure.update_traces(textposition="top center")
fig_leisure.update_layout(
    xaxis=dict(range=[min_val, max_val]),
    yaxis=dict(range=[min_val, max_val]),
)

st.plotly_chart(fig_leisure, use_container_width=True)


st.subheader("Top 5 Countries: Men's vs Women's Leisure Time (Bubble Chart)")


df2 = df_leisure.rename(columns={
    "Minutes spent on leisure - women (OECD Gender data (2020))": "Women",
    "Minutes spent on leisure - men (OECD Gender data (2020))": "Men"
})


df2 = df2[(df2["Men"] > 0) & (df2["Women"] > 0)]


top5 = df2.sort_values("Men", ascending=False).head(5)

fig_top5 = px.scatter(
    top5,
    x="Men",
    y="Women",
    size="Men", 
    color="Entity",
    hover_name="Entity",
    text="Entity",
    title="Top 5 Countries with Highest Men's Leisure Time",
    size_max=50,
)


fig_top5.update_traces(textposition="top center")


fig_top5.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    font_color="white"
)

st.plotly_chart(fig_top5, use_container_width=True)

