from flask import request, jsonify
from models import Customer

@app.route('/customers', methods=['POST'])
def create_customer():
    data = request.get_json()
    name = data['name']
    email = data['email']
    phone_number = data['phone_number']

    customer = Customer(name, email, phone_number)
    db.session.add(customer)
    db.session.commit()

    return jsonify({'message': 'Customer created successfully'})

from flask import request, jsonify
from models import Customer

@app.route('/customers/<int:customer_id>', methods=['GET'])
def read_customer(customer_id):
    customer = Customer.query.get(customer_id)
    if customer is None:
        return jsonify({'message': 'Customer not found'}), 404

    return jsonify({'customer': customer})

from flask import request, jsonify
from models import Customer

@app.route('/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    customer = Customer.query.get(customer_id)
    if customer is None:
        return jsonify({'message': 'Customer not found'}), 404

    data = request.get_json()
    customer.name = data['name']
    customer.email = data['email']
    customer.phone_number = data['phone_number']

    db.session.commit()

    return jsonify({'message': 'Customer updated successfully'})

from flask import request, jsonify
from models import Customer

@app.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    customer = Customer.query.get(customer_id)
    if customer is None:
        return jsonify({'message': 'Customer not found'}), 404

    db.session.delete(customer)
    db.session.commit()

    return jsonify({'message': 'Customer deleted successfully'})

