from flask import Flask, request, render_template
from model import Model
from helper import sorted_cities, datatype_conversion
app = Flask(__name__)

# HTML Form model prediction
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        form_input = dict(request.form)
        print(form_input)
        model_inputs = datatype_conversion(form_input)
        prediction = Model().predict(model_inputs)
        print(prediction)
        return render_template('index.html', prediction=prediction, cities=sorted_cities())

    return render_template('index.html', cities=sorted_cities())


if __name__ == '__main__':
    app.run(debug=True)
