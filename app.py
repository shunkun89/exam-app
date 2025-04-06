from flask import Flask, request, render_template
import pandas as pd
import os
app = Flask(__name__)
df = pd.read_excel("data.xlsx")

# 受験番号を文字列として扱う（重要）
df["受験番号"] = df["受験番号"].astype(str)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        exam_number = request.form.get("exam_number")
        match = df[df["受験番号"] == exam_number]
        if not match.empty:
            result = match.iloc[0].to_dict()
        else:
            result = {}
    return render_template("index.html", result=result)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
