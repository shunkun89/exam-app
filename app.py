from flask import Flask, request, jsonify, render_template
import pandas as pd

app = Flask(__name__)
df = pd.read_excel("data.xlsx")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    exam_number = request.json.get("exam_number")
    result = df[df['受験番号'] == int(exam_number)]

    if not result.empty:
        record = result.iloc[0]
        return jsonify({
            "氏名": record["氏名"],
            "受験区分": record["受験区分"],
            "クラス": record["クラス"],
            "出席番号": record["出席番号"],
            "座席番号": record["座席番号"]
        })
    else:
        return jsonify({"error": "受験番号が見つかりませんでした。"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)