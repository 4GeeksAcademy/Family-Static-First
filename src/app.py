"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
from random import randint
# from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints


@app.route('/')
def sitemap():
    return generate_sitemap(app)





@app.route("/member/<int:member_id>", methods=['GET'])
def retrieve_one_member(member_id):
    member = jackson_family.get_member(member_id)

    if member:
        return jsonify(member), 200
    else:
        return jsonify({"message": "Member not found"}), 404


@app.route("/member", methods=['POST'])
def handle_member_post():
    data = request.json
    new_member = {
        "id": data.get("id", randint(0, 99999999)),
        "first_name": data.get("first_name", ""),
        "last_name": "Jackson",
        "age": data.get("age", 0),
        "lucky_numbers": data.get("lucky_numbers", []),
    }

    jackson_family.add_member(new_member)

    return jsonify({"message": "Member added successfully"}), 200


@app.route("/member/<int:member_id>", methods=['DELETE'])
def delete_member(member_id):

    deleted_member = jackson_family.delete_member(member_id)

    if deleted_member is not None:
        return jsonify({"done": True}), 200
    else:
        return jsonify({"message": "Member not found"}), 400



@app.route('/members', methods=['GET', 'POST'])
def handle_members():
     if request.method == 'GET':
        members = jackson_family.get_all_members()
        
        return jsonify(members), 200
     elif request.method == 'POST':
        data = request.json
        new_member = {
            "id": data.get("id", randint(0, 99999999)),  
            "first_name": data.get("first_name", ""),
            "last_name": "Jackson",
            "age": data.get("age", 0),
            "lucky_numbers": data.get("lucky_numbers", []),
        }
        jackson_family.add_member(new_member)
        return jsonify({"message": "Member added successfully"}), 200



if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)









# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
