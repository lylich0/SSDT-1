import uuid

from flask import jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
from SSDT.data import json_extract
from SSDT.schemas import CategorySchema

categories = []
blp = Blueprint("category", __name__, description="Operations on category")


@blp.route('/category/<string:cid>')
class Category(MethodView):
    def get(self, cid: str):
        try:
            if cid in json_extract(categories, "id"):
                for i in range(len(categories)):
                    if categories[i]["id"] == cid:
                        return categories[i]
        except KeyError:
            return jsonify(message="Category not found"), 404

    def delete(self, cid: str):
        global deleted_category
        try:
            if cid in json_extract(categories, "id"):
                for i in range(len(categories)):
                    if categories[i]["id"] == cid:
                        deleted_category = categories[i]
                        del categories[i]
            return jsonify(message="Category deleted successfully", deleted_category=deleted_category), 200
        except (KeyError, IndexError) as e:
            return jsonify(message="Category not found"), 404


@blp.route('/category')
class CategoryList(MethodView):
    def get(self):
        return jsonify(categories=json_extract(categories, "name")), 200

    @blp.arguments(CategorySchema)
    def post(self, category_data):
        category_id = uuid.uuid4().hex[:7]
        new_category = {"id": category_id, **category_data}
        categories.append(new_category)
        return categories
