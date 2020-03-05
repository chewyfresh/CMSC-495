# Run a class
import cgi, os, string, sys
normal_sys = sys.path
sys.path.append(os.path.abspath(os.pardir) + "\\src\\")
from back_end.database import database

sys.path = normal_sys

username = None
password = None
with open('current_user.txt', 'r') as fd:
    username, password = fd.read().split('\n')

db = database("CYBERFITNESS", "1")

form = cgi.FieldStorage()

weight = form.getvalue("weight", "0")
cals = form.getvalue("cals", "0")
classes_taken = form.getvalue("classes_taken", "0")

continue_string = """
<div>
<form action="/cgi-bin/{}" method="post">
    <input type="submit" value="Continue"></input>
</form>
</div>
"""
print("Content-type:text/html\n")
print("<html><body>")
user_data = db.db_query(username, password)
if user_data == -1:
    print("<text>Invalid credentials</text>")
    print(continue_string.format("gym_welcome.py"))
else:
    try:
        if int(weight) > 0:
            db.db_goal(username, password, "Weight", weight)
    except:
        pass
    try:
        if int(cals) > 0:
            db.db_goal(username, password, "Total Calorie Loss", cals)
    except:
        pass
    try:
        if int(classes_taken) > 0:
            db.db_goal(username, password, "Total Classes Taken", classes_taken)
    except:
        pass
    print(continue_string.format("gym_welcome.py"))
print("</body></html>")