from flask import Flask, request, render_template
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

# Prometheus metrics endpoint: /metrics
metrics = PrometheusMetrics(app)

metrics.info('app_info', 'Flask Calculator App Info', version='1.0.0')

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = ''
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operation = request.form['operation']

            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                result = num1 / num2
            else:
                result = 'Invalid operation'
        except Exception as e:
            result = f'Error: {e}'

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
