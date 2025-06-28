import re
from difflib import get_close_matches

# Known Subjects for matching
KNOWN_SUBJECTS = [
    "Digital Signal Processing", "Microprocessors", "Signals and Systems",
    "Data Structures", "Engineering Mathematics", "Basic Electronics",
    "Wireless Communication", "Python Programming", "Operating Systems"
]

SUBJECT_KEYWORDS = [s.lower() for s in KNOWN_SUBJECTS]

# Days for timetable understanding
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

def extract_day(query):
    for day in DAYS:
        if day in query.lower():
            return day.capitalize()
    return None

def extract_topic(query):
    query_lower = query.lower()
    # Exact match first
    for sub in SUBJECT_KEYWORDS:
        if sub in query_lower:
            return sub.title()
    # Fuzzy match (e.g. "microprocessor" -> "Microprocessors")
    match = get_close_matches(query_lower, SUBJECT_KEYWORDS, n=1, cutoff=0.7)
    if match:
        return match[0].title()
    return None

def extract_intent(query):
    query_lower = query.lower()

    # Exit
    if any(exit_word in query_lower for exit_word in ["exit", "quit", "shutdown", "bye", "stop now"]):
        return {"intent": "exit", "year": None, "branch": None, "topic": None, "day": None}

    # Greeting
    if any(greet in query_lower for greet in ["hi", "hello", "hey", "namaste", "yo"]):
        return {"intent": "greeting", "year": None, "branch": None, "topic": None, "day": None}

    # Year
    year = None
    if re.search(r"\b(1st|first|1)\b", query_lower):
        year = "1"
    elif re.search(r"\b(2nd|second|2)\b", query_lower):
        year = "2"
    elif re.search(r"\b(3rd|third|3)\b", query_lower):
        year = "3"
    elif re.search(r"\b(4th|fourth|4)\b", query_lower):
        year = "4"

    # Branch
    branch = None
    for b in ["ece", "cse", "eee", "mech", "civil", "bca", "it"]:
        if b in query_lower:
            branch = b.upper()

    # Day
    day = extract_day(query)

    # Topic/Subject
    topic = extract_topic(query)

    # Intent Detection
    if "syllabus" in query_lower:
        return {"intent": "syllabus", "year": year, "branch": branch, "topic": topic, "day": None}

    if any(x in query_lower for x in ["faculty", "teacher", "professor", "teaches", "who teaches", "who is teaching"]):
        return {"intent": "faculty", "year": year, "branch": branch, "topic": topic, "day": None}

    if "timetable" in query_lower or "schedule" in query_lower or "classes on" in query_lower:
        return {"intent": "timetable", "year": year, "branch": branch, "topic": None, "day": day}

    if "library" in query_lower or "book" in query_lower or "reference" in query_lower:
        return {"intent": "library", "year": year, "branch": branch, "topic": topic, "day": None}

    if "materials" in query_lower or "notes" in query_lower or "pdf" in query_lower or "slides" in query_lower:
        return {"intent": "materials", "year": year, "branch": branch, "topic": topic, "day": None}

    # Fallback to faculty if only topic is matched
    if topic:
        return {"intent": "faculty", "year": year, "branch": branch, "topic": topic, "day": None}

    return {"intent": None, "year": year, "branch": branch, "topic": topic, "day": day}
