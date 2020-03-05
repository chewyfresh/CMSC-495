# Run a class
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
    fitness_class = fc.class_list.get(class_name)
    print("<text>Class Name: {}</text>\n".format(fitness_class.class_name))
    print("<text>Calorie Loss: {}</text>\n".format(fitness_class.calorie_per_minute * fitness_class.length))
    print("<text>Time: {}</text>\n".format(fitness_class.length))
    print("<text>Intensity: {}</text>\n".format(fitness_class.intensity))
    print(continue_string.format("gym_welcome.py"))
    db.db_delete(username, password, class_name)
print("</body></html>")