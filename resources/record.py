from sqlite3 import IntegrityError
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from database import RecordModel, db, UserModel, CategoryModel
from schemas import RecordSchema

records = []
blp = Blueprint("record", __name__, description="Operations on record")


@blp.route('/record')
class RecordList(MethodView):
    @blp.arguments(RecordSchema)
    @blp.response(200, RecordSchema)
    def post(self, record_data):
        if UserModel.query.filter_by(id=record_data.get("user_id")).first() is not None \
                and \
                CategoryModel.query.filter_by(id=record_data.get("category_id")).first() is not None:
            record = RecordModel(**record_data)
            try:
                db.session.add(record)
                db.session.commit()
            except IntegrityError:
                abort(404, message="Not found") # TODO test error message
            return record


@blp.route("/record/<string:uid>")
class Record(MethodView):
    @blp.response(200, RecordSchema(many=True))
    def get(self, uid: str):
        record = RecordModel.query.filter_by(user_id=uid).all()
        return record

    @blp.response(200, RecordSchema)
    def delete(self, uid: str):
        record = RecordModel.query.get_or_404(uid)
        db.session.delete(record)
        db.session.commit()
        return record


@blp.route('/record/<string:uid>/<string:cid>')
class Record(MethodView):
    @blp.response(200, RecordSchema(many=True))
    def get(self, uid: str, cid: str):
        record = RecordModel.query.filter_by(user_id=uid, category_id=cid).all()
        return record