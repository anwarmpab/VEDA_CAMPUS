import re
from datetime import datetime

# --- Normalization helpers ---
def normalize_branch(text):
    corrections = {
        "csc": "CSE", "cs": "CSE", "bca": "CSE", "it": "CSE",
        "ece": "ECE", "eee": "EEE", "mech": "MECH", "civil": "CIVIL"
    }
    text = text.lower()
    for key, value in corrections.items():
        if key in text:
            return value
    return None

def normalize_day(text):
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    for day in days:
        if day in text.lower():
            return day.capitalize()
    return None

def normalize_year(text):
    text = text.lower()
    if "first" in text or "1st" in text or "1 " in text:
        return "1"
    elif "second" in text or "2nd" in text or "2 " in text:
        return "2"
    elif "third" in text or "3rd" in text or "3 " in text:
        return "3"
    elif "fourth" in text or "4th" in text or "4 " in text:
        return "4"
    return None

def extract_topic(text):
    # Capture known subject topics more flexibly
    keywords = [
        "digital signal processing", "microprocessors", "signals and systems",
        "data structures", "wireless communication", "basic electronics",
        "engineering mathematics"
    ]
    for word in keywords:
        if word in text.lower():
            return word.title()
    return None

def detect_intent(text):
    text = text.lower()
    if any(x in text for x in ["syllabus", "subjects"]):
        return "syllabus"
    elif any(x in text for x in ["faculty", "teacher", "professor", "teaches", "who teaches"]):
        return "faculty"
    elif "timetable" in text or "time table" in text:
        return "timetable"
    elif any(x in text for x in ["library", "books"]):
        return "library"
    elif any(x in text for x in ["hello", "hi", "hey"]):
        return "greeting"
    return None

def parse_query(query):
    return {
        "intent": detect_intent(query),
        "year": normalize_year(query),
        "branch": normalize_branch(query),
        "topic": extract_topic(query),
        "day": normalize_day(query)
    }