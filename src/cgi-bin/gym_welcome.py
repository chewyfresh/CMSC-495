import cgi

form = cgi.FieldStorage()

print("Content-type:text/html")
print("<html><body>")

# Set
# Check
# Remove

print("""
 <form action="/cgi-bin/handle_gym_choice.py" method="post">
            <select name="choice">
                <OPTION Value="join" selected>Join Class</OPTION>
                <OPTION Value="set">Set Goals</OPTION>
                <OPTION Value="display">Display Classes</OPTION>
                <OPTION Value="run">Run Class</OPTION>
                <OPTION Value="remove">Remove Class</OPTION>
                <OPTION Value="end">Exit</OPTION>
            </select>
        <input type="submit" value="Submit"></input>
        </form>""")
print("</body></html>")