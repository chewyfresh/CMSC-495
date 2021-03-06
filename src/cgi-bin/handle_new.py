import cgi, os, string, sys
normal_sys = sys.path
sys.path.append(os.path.abspath(os.pardir) + "\\src\\")

from back_end.database import database
sys.path = normal_sys
db = database("CYBERFITNESS", "1")

form = cgi.FieldStorage()
special_char_string = '!@#$%^&*()'
numbers_string = '1234567890'
lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase

def check_password(password):
    capital_letters = 0
    lower_letters = 0
    special_characters = 0
    numbers = 0
    for char in password:
        if char in lower_case:
            lower_letters += 1
        elif char in upper_case:
            capital_letters += 1
        elif char in special_char_string:
            special_characters += 1
        elif char in numbers_string:
            numbers += 1
        else:
            print("<text>Unrecognized character</text>")
            return False
    return False if not all([capital_letters, lower_letters, special_characters, numbers]) else True

username = form.getvalue("username")
password = form.getvalue("password")

user_exists = db.check_if_user_in_db(username)
valid_password = check_password(password)

continue_string = """
<div>
<form action="/cgi-bin/{}" method="post">
        <input type="hidden" name="username" value={}/>
        <input type="hidden" name="password" value={}/>
        <input type="submit" value="Continue"></input>
</form>
</div>
"""

print("Content-type:text/html")
print("<html><body>")

if user_exists:
    # Serve up "User already exists error"
    print("<text>User already exists</text>")
    print(continue_string.format('new_user.py', '', ''))
else:
    if valid_password:
        with open('current_user.txt', 'w') as fd:
            fd.write(username + '\n' + password)
        print("<text>User successfully created.</text>")
        db.add_user(username, password)
        print(continue_string.format('gym_welcome.py', username, password))
        # Continue button sends user to "Gym interface"
    else:
        print("<text>Invalid password, try again</text>")
        print(continue_string.format('new_user.py', '', ''))
        # Continue button sends user to new_user.py
print("</body></html>")