import cgi, os

os.remove('current_user.txt')

print("Content-type:text/html")

print("""
<html><text>Successfully logged out. Exit out of your web browser</text></html>
""")