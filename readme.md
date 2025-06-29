# 🤖 VEDA CAMPUS — Your Intelligent College Buddy

> Built by [M P Anwar Baba](https://github.com/anwarmpab) | Powered by Python + NLU + Voice AI

VEDA (Voice-Enabled Digital Assistant) is a **smart campus assistant** built to revolutionize student access to academic information. With voice commands or text inputs, VEDA instantly provides:

🎓 Syllabus info  
👨‍🏫 Faculty details  
📆 Timetables  
📚 Library/book queries *(coming soon)*  
🧠 And more smart NLU-powered answers

---

## 🧩 Features

- 🎙️ **Voice & Text Interface**  
  Seamless interaction with VEDA via mic or keyboard.

- 🧠 **NLU-Powered Understanding**  
  Smart natural language engine to detect intent (like asking for *"Who teaches microprocessors?"* or *"CSE timetable on Monday"*).

- 📚 **Modular Knowledge Base**  
  - `syllabus.csv`: Curriculum info by year and branch  
  - `faculty.json`: Faculty subject assignments  
  - `timetable.json`: Smart weekday schedules

- 🧾 **Logging System**  
  Auto-logs every user query and VEDA’s response with timestamp.

## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/anwarmpab/VEDA_CAMPUS.git
cd VEDA_CAMPUS

# Create virtual environment
python -m venv .venv
.\.venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Run VEDA (voice mode)
python modules/voice_veda.py

# Or run in terminal mode
python main.py
🔍 Example Commands
You Say / Type	VEDA Responds With
"3rd year ECE syllabus"	List of subjects + unit count
"Who teaches Microprocessors?"	Faculty name, email, room number
"CSE timetable on Monday"	Lecture schedule
"Hello" / "Hi VEDA"	Friendly greeting
"Exit" / "Shutdown"	Ends session gracefully

🔍 Example Commands
You Say / Type	VEDA Responds With
"3rd year ECE syllabus"	List of subjects + unit count
"Who teaches Microprocessors?"	Faculty name, email, room number
"CSE timetable on Monday"	Lecture schedule
"Hello" / "Hi VEDA"	Friendly greeting
"Exit" / "Shutdown"	Ends session gracefully


🛠 File Structure
VEDA_CAMPUS/
│
├── main.py                  # Text interface
├── modules/
│   ├── voice_veda.py        # Voice assistant engine
│   ├── veda_core.py         # Master brain (intent -> response)
│   ├── nlu_engine.py        # Natural language understanding
│   ├── faculty_ai.py        # Faculty resolver
│   ├── syllabus_ai.py       # Syllabus resolver
│   ├── timetable_ai.py      # Timetable resolver
│   ├── logger.py            # Interaction logging
│
├── data/
│   ├── syllabus.csv         # Syllabus info
│   ├── faculty.json         # Faculty info
│   ├── timetable.json       # Time table info
│
└── README.md            

💡 Vision
VEDA is not just a project — it’s a proof-of-concept for AI in campus life. Future upgrades will include:
📱 Android app version (via Kivy or Flutter)
🔍 Book finder via library API integration
🧠 AI chatbot with GPT-style understanding
📊 Analytics dashboard (auto logs, usage trends, queries per student)

🧠 Built With
Python 3.x
SpeechRecognition
Pyttsx3 (TTS)
Pandas, JSON
Custom NLU logic (no LLM used)

🙌 Author
M P Anwar Baba
Third-year ECE student | Passionate Innovator | Building like Tony Stark
🔗 GitHub

