 stats = df[["marks", "age", "attendance"]].describe().T

stats = stats.rename(columns={
    "count": "Count",
    "mean": "Mean",
    "std": "Std Dev",
    "min": "Minimum",
    "25%": "25%",
    "50%": "Median",
    "75%": "75%",
    "max": "Maximum"
})

st.dataframe(stats.round(2), use_container_width=True)
s1, s2, s3 = st.columns(3)
s1.metric("Highest Marks", f"{df['marks'].max():.0f}")
s2.metric("Lowest Marks", f"{df['marks'].min():.0f}")
s3.metric("Highest Attendance", f"{df['attendance'].max():.0f}%")

# -----------------------------
# 4. Top performing students
# -----------------------------
st.header("4. Top Performing Students")

top_n = st.slider("Number of top students", 3, min(20, len(df)), 10)

top_students = df.sort_values(
    by=["marks", "attendance"],
    ascending=[False, False]
).head(top_n)

st.dataframe(
    top_students[
        ["roll_number", "name", "gender", "department",
         "marks", "grade", "attendance"]
    ],
    use_container_width=True
)

# -----------------------------
# 5. Charts
# -----------------------------
st.header("5. Data Visualizations")

tab1, tab2, tab3, tab4 = st.tabs([
    "Marks Distribution",
    "Department Performance",
    "Grade Distribution",
    "Marks vs Attendance"
])

with tab1:
    fig, ax = plt.subplots()
    ax.hist(df["marks"].dropna(), bins=10)
    ax.set_title("Distribution of Student Marks")
    ax.set_xlabel("Marks")
    ax.set_ylabel("Number of Students")
    st.pyplot(fig)
    plt.close(fig)

with tab2:
    dept_avg = df.groupby("department")["marks"].mean().sort_values(ascending=False)

    fig, ax = plt.subplots()
    dept_avg.plot(kind="bar", ax=ax)
    ax.set_title("Average Marks by Department")
    ax.set_xlabel("Department")
    ax.set_ylabel("Average Marks")
    plt.xticks(rotation=0)
    st.pyplot(fig)
    plt.close(fig)

with tab3:
    grade_counts = df["grade"].value_counts()

    fig, ax = plt.subplots()
    grade_counts.plot(kind="bar", ax=ax)
    ax.set_title("Grade Distribution")
    ax.set_xlabel("Grade")
    ax.set_ylabel("Number of Students")
    plt.xticks(rotation=0)
    st.pyplot(fig)
    plt.close(fig)

with tab4:
    fig, ax = plt.subplots()
    ax.scatter(df["attendance"], df["marks"], alpha=0.7)
    ax.set_title("Marks vs Attendance")
    ax.set_xlabel("Attendance (%)")
    ax.set_ylabel("Marks")
    st.pyplot(fig)
    plt.close(fig)

# -----------------------------
# 6. Concise summary
# -----------------------------
st.header("6. Summary of Findings")

avg_marks = df["marks"].mean()
avg_attendance = df["attendance"].mean()
highest_mark = df.loc[df["marks"].idxmax()]
lowest_mark = df.loc[df["marks"].idxmin()]
best_department = (
    df.groupby("department")["marks"]
    .mean()
    .idxmax()
)

high_attendance_count = int((df["attendance"] >= 75).sum())
low_attendance_count = int((df["attendance"] < 75).sum())

st.markdown(f"""
### 📌 Key Findings

- **Total students:** {len(df)}
- **Average marks:** {avg_marks:.2f}
- **Average attendance:** {avg_attendance:.2f}%
- **Highest marks:** {highest_mark['marks']:.0f} — **{highest_mark['name']}**
- **Lowest marks:** {lowest_mark['marks']:.0f} — **{lowest_mark['name']}**
- **Best-performing department by average marks:** **{best_department}**
- **Students with attendance ≥ 75%:** {high_attendance_count}
- **Students with attendance < 75%:** {low_attendance_count}

Overall, the dashboard provides a quick view of student academic performance,
attendance, grade distribution, department performance, and the relationship
between attendance and marks.
""")

st.success("Analysis completed successfully. 🎓")
