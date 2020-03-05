# Leave a class
import cgi, os, string, sys
normal_sys = sys.path
sys.path.append(os.path.abspath(os.pardir) + "\\src\\")
import FitnessClasses as fc
from back_end.database import database

sys.path = normal_sys

username = None
password = None
with open('current_user.txt', 'r') as fd:
    username, password = fd.read().split('\n')

db = database("CYBERFITNESS", "1")

form = cgi.FieldStorage()

class_name = form.getvalue("choice")
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
    ret = db.db_delete(username, password, class_name)
    if ret == -1:
        print("<text>Unable to remove class</text>")
    else:
        print("<text>Class Removed Successfully</text>")
        print(continue_string.format("gym_welcome.py"))
print("</body></html>")