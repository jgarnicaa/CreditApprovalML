from flask import Flask, render_template, request
from getCreditApprove import get_approval
from waitress import serve

app=Flask(__name__)

@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])

def get_status():
    data = [
        int(request.form.get('code_gender', 0)),
        int(request.form.get('flag_own_car', 0)),
        int(request.form.get('flag_own_realty', 0)),
        int(request.form.get('cnt_children', 0)),
        int(request.form.get('AMT_INCOME_TOTAL', 0)),
        int(request.form.get('name_income_type', 0)),
        int(request.form.get('name_education_type', 0)),
        int(request.form.get('name_family_status', 0)),
        int(request.form.get('name_housing_type', 0)),
        int(request.form.get('days_birth', 0)),
        int(request.form.get('days_employed', 0)),
        int(request.form.get('flag_mobil', 0)),
        int(request.form.get('flag_work_phone', 0)),
        int(request.form.get('flag_phone', 0)),
        int(request.form.get('flag_email', 0)),
        int(request.form.get('occupation_type', 0)),
        int(request.form.get('cnt_fam_members', 0))
    ]

    status_data=(get_approval(data))

    return render_template('result.html', status=status_data)


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)