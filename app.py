from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        /bmi
            Height (m): <input type="text" name="height"><br>
            Weight (kg): <input type="text" name="weight"><br>
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
        return f"Your BMI is {bmi_value:.2f}, which is considered '{category}'."
    except:
        return "Invalid input. Please enter valid numbers."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
