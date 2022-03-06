from flask import Flask, render_template, request
Users=[{"name":"User1","E-mail":"User1@yahoo.com","Password":"Pass1"},{"name":"User2","E-mail":"User2@yahoo.com","Password":"Pass2"}]
app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("index.html")


@app.route("/Signup", methods=["POST"])
def sign_up():
    email = request.form['Email']
    username = request.form['Username']
    password = request.form['Password']
    User = {"name":username,"E-mail":email,"Password":password}
    if not user_exists(email=email, username=username, password=password):
        Users.append(User)
        return "<h2>New user has been created</h2><a href=http://127.0.0.1:5000/>Return</a>"
    else:
        return "<h2>This user already exists</h2>"

def Check(User,username):
    return (User["name"]==username)

def user_exists(email, username, password):
    # TODO: check for user if exists, you can use an array as your records.
<<<<<<< HEAD
    # M1:checks array for user
=======
    #user exists checks if there is a user in our array and makes sure it is not repeated
>>>>>>> e3032469b1d2736775a45e7dc477fdf6da1c1f3a
    return True in list(map(lambda user: Check(user, username),Users))

app.run(debug=True)    