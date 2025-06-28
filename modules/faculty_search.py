import json
import os

# Absolute path to data/faculty.json
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "faculty.json")

def find_faculty(query):
    try:
        if not os.path.exists(DATA_PATH):
            return "📂 Faculty database not found."

        with open(DATA_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)

        query_lower = query.lower()
        matches = []

        for faculty in data:
            name = faculty.get("name", "").lower()
            subject = faculty.get("subject", "").lower()
            department = faculty.get("department", "").lower()

            # Normalize subject matching (handle plural/singular)
            subject_keywords = [
                subject,
                subject.rstrip('s'),
                subject.rstrip('es'),
                subject.replace(" and ", " & "),
                subject.replace(" ", "")
            ]

            if any(sub in query_lower for sub in subject_keywords) or \
               name in query_lower or department in query_lower:
                info = (
                    f"👨‍🏫 {faculty.get('name')} ({faculty.get('department')})\n"
                    f"  • Subject: {faculty.get('subject')}\n"
                    f"  • Email: {faculty.get('email')}\n"
                    f"  • Room: {faculty.get('room')}"
                )
                matches.append(info)

        if matches:
            return "\n\n".join(matches)
        else:
            return "🔍 No matching faculty found. Try using subject or department name."

    except Exception as e:
        return f"❌ Error in faculty search: {str(e)}"
