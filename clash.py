def meetings_clash(m1, m2):
    if m1["day"] != m2["day"]:
        return False
    return m1["start"] < m2["end"] and m2["start"] < m1["end"]

def courses_clash(c1, c2):
    for m1 in c1["meetings"]:
        for m2 in c2["meetings"]:
            if meetings_clash(m1, m2):
                return True
    return False # return True can fire early, as soon as one clash is found. return False must wait until every pair has been checked.

def fits(course, chosen):
    for c in chosen:
        if course["group"] == c["group"]:
            return False
        if courses_clash(course, c):
            return False
    return True

def find_combos(courses, k):
    results = []

    def backtrack(start, chosen):
        if len(chosen) == k:
            results.append([c["name"] for c in chosen])
            return
        for i in range(start, len(courses)):
            if fits(courses[i], chosen):
                chosen.append(courses[i])
                backtrack(i + 1, chosen)
                chosen.pop()

    backtrack(0, [])
    return results