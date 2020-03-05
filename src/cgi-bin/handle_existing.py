import cgi, os, string, sys
normal_sys = sys.path
sys.path.append(os.path.abspath(os.pardir) + "\\src\\")
import FitnessClasses as fc
from back_end.database import database

sys.path = normal_sys

form = cgi.FieldStorage()

username = form.getvalue("username")
password = form.getvalue("password")

print("Content-type:text/html")

continue_string = """
<div>
<form action="/cgi-bin/{}" method="post">
    <input type="submit" value="Continue"></input>
</form>
</div>
"""

db = database("CYBERFITNESS", "1")

print("<html><body><center>")
with open('current_user.txt', 'w') as fd:
    fd.write(username + '\n' + password)
if db.db_query(username, password) == -1:
    print("<text>No user by those credentials</text>")
    print(continue_string.format("existing_user.py"))
    # Continue button sends user to "index.html"
else:
    print(f"<text>Welcome back {username}</text>!")
    print(continue_string.format("gym_welcome.py"))
    # Continue button sends user to "Gym interface"

print("</center></body></html>")