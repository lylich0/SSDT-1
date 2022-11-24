import uuid
from datetime import datetime

from flask import jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
from SSDT.data import json_extract
from SSDT.schemas import RecordSchema

records = []
blp = Blueprint("record", __name__, description="Operations on record")


@blp.route("/record/<string:uid>")
class Record(MethodView):
    def get(self, uid: str):
        existing_id = json_extract(records, "user_id")
        records_by_user = []
        try:
            if uid in existing_id:
                for i in range(len(records)):
                    if records[i]["user_id"] == uid:
                        records_by_user.append(records[i])
                return records_by_user
        except (KeyError, IndexError) as e:
            return jsonify(message="Record not found"), 404


@blp.route('/record/<string:uid>/<string:cid>')
class Record(MethodView):
    def get(self, uid: str, cid: str):
        existing_user_id = json_extract(records, "user_id")
        records_by_user = []
        try:
            if uid in existing_user_id:
                for i in range(len(records)):
                    if records[i]["user_id"] == uid:
                        if records[i]["category_id"] == cid:
                            records_by_user.append(records[i])
            if len(records_by_user) > 0:
                return records_by_user
        except (KeyError, IndexError) as e:
            return jsonify(message="Record not found"), 404

    def delete(self, uid: str, cid: str):
        global deleted_record
        try:
            if uid in json_extract(records, "user_id"):
                for i in range(len(records)):
                    if records[i]["user_id"] == uid:
                        if records[i]["category_id"] == cid:
                            deleted_record = records[i]
                            del records[i]
                            return jsonify(message="Record deleted successfully", deleted_record=deleted_record), 200
        except (KeyError, IndexError) as e:
            return jsonify(message="Record not found"), 404


@blp.route('/record')
class RecordList(MethodView):
    @blp.arguments(RecordSchema)
    def post(self, record_data):
        record_id = uuid.uuid4().hex[:7]
        new_record = {"id": record_id, "date": datetime.now(), **record_data}
        records.append(new_record)
        return records


