# main.py — VEDA-CAMPUS Entry Point
# Author: M P Anwar Baba

from modules.veda_core import ask_veda
from modules.logger import log_interaction

def intro():
    print("\n====================================")
    print("     Welcome to VEDA CAMPUS AI      ")
    print("   Your Intelligent College Buddy   ")
    print("====================================")
    print("Ask me about syllabus, faculty, timetable, library, or materials.")
    print("Type 'exit' or 'quit' to end the session.\n")

if __name__ == "__main__":
    intro()

    while True:
        try:
            user_input = input("You > ").strip()
            if user_input.lower() in ["exit", "quit", "shutdown"]:
                print("VEDA > Logging off. Study well, rise high! 🚀")
                break

            response = ask_veda(user_input)
            log_interaction("TEXT", user_input, response)

            print("VEDA >", response)
        except KeyboardInterrupt:
            print("\nVEDA > Session interrupted. Goodbye Anwar! ✋")
            break
        except Exception as e:
            print(f"VEDA > ⚠️ Something went wrong: {str(e)}")

