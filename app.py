import json
import streamlit as st
from clash import courses_clash, find_combos
from grid import build_grid

st.title("Course Clash Checker")

with open("courses.json") as f:
    all_courses = json.load(f)

names = [c["name"] for c in all_courses]
picked = st.multiselect("Pick courses", names)
chosen = [c for c in all_courses if c["name"] in picked]

st.subheader("Clashes")
found = False
for i in range(len(chosen)):
    for j in range(i + 1, len(chosen)):
        if courses_clash(chosen[i], chosen[j]):
            st.write(chosen[i]["name"] + " clashes with " + chosen[j]["name"])
            found = True
if not found:
    st.success("No clashes")

st.subheader("Clash-free combinations")
k = st.number_input("How many courses to take?", min_value=1, max_value=max(len(chosen), 1), value=1)
combos = find_combos(chosen, k)
if len(combos) == 0:
    st.warning("No clash-free combination exists")
else:
    st.write(str(len(combos)) + " combinations")
    labels = [", ".join(combo) for combo in combos]
    pick = st.selectbox("View timetable for", labels)
    names_in = pick.split(", ")
    show = [c for c in all_courses if c["name"] in names_in]
    st.dataframe(build_grid(show))