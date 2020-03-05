import cgi

form = cgi.FieldStorage()
choice_dict = {"join":"join_class.py", "set":"set_goals.py","display":"display_classes.py","run":"run_class.py","remove":"remove_class.py", "end":"end_session.py"}
print("Content-type:text/html")

username = None
password = None
with open('current_user.txt', 'r') as fd:
    username, password = fd.read().split('\n')
choice = choice_dict.get(form.getvalue("choice"))


    
continue_string = """
<div>
<form action="/cgi-bin/{}" method="post">
    <center><input type="submit" value="Continue"></input></center>
</form>
</div>
"""

print("<html><body>")
print(continue_string.format(choice))
print("</body></html>")