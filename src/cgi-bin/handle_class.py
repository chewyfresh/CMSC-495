# Join a class
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

class_name = form.getvalue("class_name")
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
    with open('f.txt', 'w') as f:
        f.write(username)
        f.write('\n' + password)
    print("<text>Invalid credentials</text>")
    print(continue_string.format("gym_welcome.py"))
else:
    fitness_class = fc.class_list.get(class_name)
    ret = db.db_insert(username, password, class_name, (fitness_class.class_name, fitness_class.calorie_per_minute, fitness_class.length, fitness_class.intensity))
    if ret == -1:
        print("<text>Unable to join class</text>")
    else:
        print("<text>Class Joined Successfully</text>")
        print(continue_string.format("gym_welcome.py"))
print("</body></html>")