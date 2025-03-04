from flask import Blueprint, jsonify

bp = Blueprint("courses", __name__)

@bp.route("/courses", methods=["GET"])
def get_courses():
    return jsonify({"message": "Lista de cursos"})
