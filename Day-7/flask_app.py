from flask import Flask, request, render_template, redirect, url_for


notepad_content = "initial notepad is defined"

app = Flask(__name__)

@app.route("/", methods=["GET", "post"])
def index():
    global notepad_content
    return render_template("index.html",content=notepad_content)

@app.route("/updatefortoday", methods=['GET','POST'])
def updatefortoday():
    global notepad_content
    if request.method == 'POST':
        new_content = request.form.get("content", "")
        notepad_content = new_content
        return redirect(url_for("index"))
    return render_template("update.html", content=notepad_content)


@app.route("/share", methods=['GET'])
def share():
    return render_template("share.html", content=notepad_content)


@app.route("/clearnotepadtxt", methods=['GET'])
def clear():
    global notepad_content
    notepad_content = ""
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)