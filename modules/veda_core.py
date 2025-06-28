from modules.nlu_engine import extract_intent
from modules.syllabus_query import get_syllabus
from modules.faculty_search import find_faculty
# from modules.library_ai import search_books  # Optional
# from modules.timetable_ai import get_timetable  # Optional

def ask_veda(query):
    intent_data = extract_intent(query)
    print("[DEBUG]", intent_data)

    intent = intent_data['intent']

    # Greet back!
    if intent == "greeting":
        return "Hi there! I'm VEDA – your intelligent campus assistant. Ask me about syllabus, faculty, timetable, or library."

    # Exit is handled in main/voice module

    # Syllabus logic
    if intent == "syllabus":
        return get_syllabus(query)

    # Faculty logic
    if intent == "faculty":
        return find_faculty(query)

    # You can add more intent checks like timetable or library later
    elif intent == "library":
        from modules.library_ai import search_books
        return search_books(query)

    # 📌 If no intent is detected, check if query contains subject keywords (fallback)
    subject_guess = try_infer_subject(query)
    if subject_guess:
        return find_faculty(subject_guess)

    return "🤔 I'm still learning. Try asking about syllabus, faculty, timetable, or library topics."

def try_infer_subject(query):
    # Simple fallback that reroutes queries like "microprocessor" or "dsp"
    from modules.nlu_engine import SUBJECT_KEYWORDS
    q = query.lower()
    for s in SUBJECT_KEYWORDS:
        if s in q:
            return f"who teaches {s}"  # Fake query to re-trigger intent in find_faculty
    return None
