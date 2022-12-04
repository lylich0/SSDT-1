from sqlite3 import IntegrityError
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from database import CategoryModel, db
from schemas import CategorySchema

categories = []
blp = Blueprint("category", __name__, description="Operations on category")


@blp.route('/category')
class CategoryList(MethodView):
    @blp.response(200, CategorySchema(many=True))
    def get(self):
        return CategoryModel.query.all()

    @blp.arguments(CategorySchema)
    @blp.response(200, CategorySchema)
    def post(self, category_data):
        category = CategoryModel(**category_data)
        try:
            db.session.add(category)
            db.session.commit()
        except IntegrityError:
            abort(404, message="Category already exists")  # TODO test error message
        return category


@blp.route('/category/<string:cid>')
class Category(MethodView):
    @blp.response(200, CategorySchema)
    def get(self, cid: str):
        category = CategoryModel.query.get_or_404(cid)
        return category

    @blp.response(200, CategorySchema)
    def delete(self, cid: str):
        category = CategoryModel.query.get_or_404(cid)
        db.session.delete(category)
        db.session.commit()
        return category
