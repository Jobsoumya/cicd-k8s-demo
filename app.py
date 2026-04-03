from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>CI/CD Demo App</title>
    <style>
        body {
            font-family: Arial;
            text-align: center;
            margin-top: 100px;
            background: #f4f4f4;
        }
        input, button {
            padding: 10px;
            font-size: 16px;
        }
        .box {
            background: white;
            padding: 30px;
            border-radius: 10px;
            display: inline-block;
            box-shadow: 0 0 10px rgba(0,0,0,0.2);
        }
    </style>
</head>
<body>

<div class="box">
<h2>🚀 CI/CD Pipeline Demo</h2>
<p>Your Kubernetes deployment is running!</p>

<form method="POST">
    <input type="text" name="username" placeholder="Enter your name" required>
    <button type="submit">Submit</button>
</form>

{% if name %}
<h3>Hello {{name}} 👋</h3>
<p>Your CI/CD pipeline deployment is working successfully!</p>
{% endif %}

</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    name = None
    if request.method == "POST":
        name = request.form.get("username")
    return render_template_string(HTML_PAGE, name=name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
