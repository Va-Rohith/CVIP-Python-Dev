from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

appointments = []

@app.route('/appointments', methods=['GET', 'POST'])
def handle_appointments():
    if request.method == 'GET':
        return jsonify(appointments)
    elif request.method == 'POST':
        data = request.get_json()
        required_fields = ['patient_name', 'phone_number', 'date', 'time']
        
        if all(field in data for field in required_fields):
            appointments.append(data)
            return jsonify({'message': 'Appointment created successfully.'}), 201
        else:
            return jsonify({'error': 'Invalid data. Make sure to include patient_name, phone_number, date, and time.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
