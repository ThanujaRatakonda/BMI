from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h2>BMI Calculator</h2>
    <form action="/bmi" method="get">
        Height (m): <input type="text" name="height"><br><br>
        Weight (kg): <input type="text" name="weight"><br><br>
        <input type="submit" value="Calculate BMI">
    </form>
    '''

@app.route('/bmi')
def bmi():
    try:
        height = float(request.args.get('height'))
        weight = float(request.args.get('weight'))
        bmi_value = weight / (height ** 2)

        if bmi_value < 18.5:
            category = "Underweight"
        elif bmi_value < 25:
            category = "Normal"
        elif bmi_value < 30:
            category = "Overweight"
        else:
            category = "Obese"

        return f"<h3>Your BMI is {bmi_value:.2f}, which is considered <b>{category}</b>.</h3>"

    except:
        return "<h3 style='color:red;'>Invalid input. Please enter valid numbers.</h3>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

