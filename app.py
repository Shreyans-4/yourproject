from flask import Flask, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "yoursecretkey"   # Change this for production


# ---------------------------------------------------
# Dummy swap data (you can replace this with a database later)
# ---------------------------------------------------

swaps = [
    {
        "id": 1,
        "teacher_name": "Alice",
        "teaching_skill": "Graphic Design",
        "learning_skill": "Basic Python",
        "avatar_url": "https://randomuser.me/api/portraits/women/1.jpg"
    },
    {
        "id": 2,
        "teacher_name": "Marcus",
        "teaching_skill": "Music Theory",
        "learning_skill": "Video Editing",
        "avatar_url": "https://randomuser.me/api/portraits/men/12.jpg"
    },
    {
        "id": 3,
        "teacher_name": "Sara",
        "teaching_skill": "Spanish",
        "learning_skill": "Photography",
        "avatar_url": "https://randomuser.me/api/portraits/women/20.jpg"
    }
]
# ---------------------------------------------------


# ---------------------------------------------------
# HOME ROUTE
# ---------------------------------------------------
@app.route("/")
def home():
    user_name = session.get("user_name")  # Shows “Welcome, ____”
    return render_template("index.html", swaps=swaps, user_name=user_name)


# ---------------------------------------------------
# SIMPLE LOGIN (temporary)
# ---------------------------------------------------
@app.route("/login")
def login():
    session["user_name"] = "StudentUser"  # mock login
    return redirect(url_for("home"))


# ---------------------------------------------------
# SIMPLIFIED LOGOUT
# ---------------------------------------------------
@app.route("/logout")
def logout():
    session.pop("user_name", None)
    return redirect(url_for("home"))


# ---------------------------------------------------
# JOIN A SWAP ROUTE (mock)
# ---------------------------------------------------
@app.route("/join/<int:swap_id>")
def join_swap(swap_id):
    print(f"User joined swap: {swap_id}")  # For testing
    return redirect(url_for("home"))


# ---------------------------------------------------
# RUN THE SERVER
# ---------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
