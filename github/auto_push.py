import os
import datetime

os.chdir("C:/Users/monik/Documents/VEDA_CAMPUS")  # Replace with your repo path
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

os.system("git add .")
os.system(f'git commit -m "Auto update: {timestamp}"')
os.system("git push origin main")
