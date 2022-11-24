import uuid

from flask_smorest import Blueprint
from flask import jsonify, request
from flask.views import MethodView
from SSDT.data import json_extract
from SSDT.schemas import UserSchema

users = []
blp = Blueprint("user", __name__, description="Operations on user")


@blp.route("/user/<string:uid>")
class User(MethodView):
    def get(self, uid: str):
        try:
            if uid in json_extract(users, "id"):
                for i in range(len(users)):
                    if users[i]["id"] == uid:
                        return users[i]
        except (KeyError, IndexError) as e:
            return jsonify(message="User not found"), 404

    def delete(self, uid: str):
        global deleted_user
        try:
            if uid in json_extract(users, "id"):
                for i in range(len(users)):
                    if users[i]["id"] == uid:
                        deleted_user = users[i]
                        del users[i]
            return jsonify(message="User deleted successfully", deleted_user=deleted_user), 200
        except (KeyError, IndexError) as e:
            return jsonify(message="User not found"), 404


@blp.route("/user")
class UserList(MethodView):
    def get(self):
        return jsonify(users=json_extract(users, "name")), 200

    @blp.arguments(UserSchema)
    def post(self, user_data):
        user_id = uuid.uuid4().hex[:7]
        new_user = {"id": user_id, **user_data}
        users.append(new_user)
        return users


