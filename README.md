# Course Clash Checker

A web app for students to pick courses from a semester timetable, see which ones clash, and generate every clash-free combination of a chosen size. Built with Python and Streamlit.

**Live app:** https://course-clash-checker.streamlit.app/
## Features

- Pick any courses from the list and see every clashing pair
- Choose how many courses you want (k) and get all clash-free combinations of that size
- Sections of the same course (e.g. CN-A and CN-B) are never combined
- Weekly timetable grid (Mon to Fri, 30-minute rows) for any combination

## How it works

**Data model.** A course is a name, a group, and a list of meetings. Each meeting is a day plus start and end time in minutes from midnight (9:30 AM = 570). A course with a lecture and a tutorial simply has more than one meeting.

```json
{"name": "DVD", "group": "DVD", "meetings": [
  {"day": "Mon", "start": 660, "end": 750},
  {"day": "Tue", "start": 840, "end": 900}
]}
```

**Clash detection.** Two meetings clash if they are on the same day and overlap:

```
a.start < b.end and b.start < a.end
```

The comparison is strict, so a class ending at 12:30 and another starting at 12:30 do not clash. Two courses clash if any meeting of one clashes with any meeting of the other.

**Clash-free combinations (backtracking).** The app builds a combination one course at a time. A course is added only if it clashes with none already chosen and is not another section of a chosen course. When the combination reaches size k it is saved. The last choice is then removed and the next option is tried. A clashing branch is abandoned as soon as the clash appears, so the app does not test every possible subset.

## Project structure

- `app.py` : Streamlit interface
- `clash.py` : clash checks and the backtracking search
- `grid.py` : builds the weekly timetable table
- `courses.json` : course data
- `requirements.txt` : dependencies

## Run locally

```
pip install -r requirements.txt
python -m streamlit run app.py
```

## Data note

Course data was taken from the IIIT Delhi Monsoon 2026 timetable (B.Tech 3rd and 4th year grid) and may contain errors. Check against the official timetable before relying on it.

## Limitations

- Only a subset of the grid is covered, and room allocations are ignored
- Selecting many courses with a large k can produce a very large number of combinations
