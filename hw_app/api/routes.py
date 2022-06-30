from crypt import methods
from email import message
from flask import Blueprint, request, jsonify
from hw_app.helpers import token_required
from hw_app.models import db, User, Car, car_schema, cars_schema
api = Blueprint('api', __name__, url_prefix = '/api')

@api.route('/cars', methods = ['POST'])
@token_required
def create_car(current_user_token):
    make = request.json['make']
    model = request.json['model']
    series = request.json['series']
    description = request.json['description']
    price = request.json['price']
    condition = request.json['condition']
    max_speed = request.json['max_speed']
    horsepower = request.json['horsepower']
    user_token = current_user_token.token

    car = Car(make, model, series, description, price, condition, max_speed, horsepower, user_token= user_token)

    db.session.add(car)
    db.session.commit()

    response = car_schema.dump(car)

    return jsonify(response)

@api.route('/cars', methods = ['GET'])
@token_required
def get_cars(current_user_token):
    owner = current_user_token.token
    cars = Car.query.filter_by(user_token = owner).all()
    response = cars_schema.dump(cars)
    return jsonify(response)

@api.route('/cars/<id>', methods = ['GET'])
@token_required
def get_car(current_user_token):
    owner = current_user_token.token
    if owner == current_user_token.token:
        car = Car.query.get(id)
        response = cars_schema.dump(car)
        return jsonify(response)
    else:
        return jsonify({'message': "Valid Token Required"}), 401


@api.route('/cars/<id>', methods = ['POST', 'PUT'])
@token_required
def update_car(current_user_token, id):
    car = Car.query.get(id)

    car.make = request.json['make']
    car.model = request.json['model']
    car.series = request.json['series']
    car.description = request.json['description']
    car.price = request.json['price']
    car.condition = request.json['condition']
    car.max_speed = request.json['max_speed']
    car.horsepower = request.json['horsepower']
    car.user_token = current_user_token.token

    db.session.commit()
    response = car_schema.dump(car)
    return jsonify(response)

@api.route('/cars/<id>', methods=['DELETE'])
@token_required
def delete_car(current_user_token, id):
    car = Car.query.get(id)
    db.session.delete(car)
    db.session.commit()
    response = car_schema.dump(car)
    return jsonify(response)