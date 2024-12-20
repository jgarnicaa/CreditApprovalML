from flask import Flask, render_template, request
from getCreditApprove import get_approval
from waitress import serve

app=Flask(__name__)

@app.route('/')
@app.route('/index', methods=['POST'])

def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])

def get_status():
    data = [
        int(request.args.get('code_gender', 0)),
        int(request.args.get('flag_own_car', 0)),
        int(request.args.get('flag_own_realty', 0)),
        int(request.args.get('cnt_children', 0)),
        int(request.args.get('AMT_INCOME_TOTAL', 0)),
        int(request.args.get('name_income_type', 0)),
        int(request.args.get('name_education_type', 0)),
        int(request.args.get('name_family_status', 0)),
        int(request.args.get('name_housing_type', 0)),
        int(request.args.get('days_birth', 0)),
        int(request.args.get('days_employed', 0)),
        int(request.args.get('flag_mobil', 0)),
        int(request.args.get('flag_work_phone', 0)),
        int(request.args.get('flag_phone', 0)),
        int(request.args.get('flag_email', 0)),
        int(request.args.get('occupation_type', 0)),
        int(request.args.get('cnt_fam_members', 0))
    ]

    status_data=(get_approval(data))

    return render_template('result.html', status="status_data")


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)