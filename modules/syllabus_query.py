import csv
import os

# Point to project root: VEDA_CAMPUS/
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "syllabus.csv")

def get_syllabus(query):
    try:
        if not os.path.exists(DATA_PATH):
            return "📂 Syllabus data file not found."

        year = None
        branch = None

        # Detect year and branch from query
        query_lower = query.lower()
        if "first" in query_lower or "1st" in query_lower or "1" in query_lower:
            year = "1"
        elif "second" in query_lower or "2nd" in query_lower or "2" in query_lower:
            year = "2"
        elif "third" in query_lower or "3rd" in query_lower or "3" in query_lower:
            year = "3"
        elif "fourth" in query_lower or "4th" in query_lower or "4" in query_lower:
            year = "4"

        for b in ["ece", "cse", "mech", "civil", "eee"]:
            if b in query_lower:
                branch = b.upper()

        if not year or not branch:
            return "❓ Please specify the year and branch (e.g., '3rd year ECE syllabus')."

        results = []
        with open(DATA_PATH, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Year'].strip() == year and row['Branch'].strip().upper() == branch:
                    results.append(f"📘 {row['Subject'].strip()} – {row['Units'].strip()} units")

        if results:
            return "\n".join(results)
        else:
            return f"⚠️ No syllabus found for {year} year {branch}."

    except Exception as e:
        return f"❌ Error processing syllabus: {str(e)}"
