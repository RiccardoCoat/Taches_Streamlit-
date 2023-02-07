import streamlit as st

tasks = ["Task 1", "Task 2", "Task 3", "Task 4", "Task 5", "Task 6", "Task 7", "Task 8", "Task 9"]
progress = [0, 0, 0, 0, 0, 0, 0, 0, 0]

st.title("Task Management App")

selected_task = st.selectbox("Select a task", tasks)
task_index = tasks.index(selected_task)

if st.button("Mark as Complete"):
    progress[task_index] = 100

st.write("Progress: ", progress[task_index], "%")

st.write("Tasks:")
for i in range(len(tasks)):
    st.write("- ", tasks[i], ": ", progress[i], "%")
