from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)
df = pd.read_excel("data.xlsx")

# 受験番号の列を文字列に変換（ここがポイント！）
df["受験番号"] = df["受験番号"].astype(str)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        exam_number = request.form["exam_number"]
        match = df[df["受験番号"] == exam_number]
        if not match.empty:
            result = {
                "氏名": match.iloc[0]["氏名"],
                "受験区分": match.iloc[0]["受験区分"],
                "クラス": match.iloc[0]["クラス"],
                "出席番号": match.iloc[0]["出席番号"],
                "座席番号": match.iloc[0]["座席番号"]
            }
    return render_template("index.html", result=result)
