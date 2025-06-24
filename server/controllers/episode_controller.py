from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from ..models.episode import Episode
from ..models.appearance import Appearance
from ..models.guest import Guest
from ..app import db

episode_bp = Blueprint('episode_bp', __name__)

# GET /episodes
@episode_bp.route('/', methods=['GET'])
def get_episodes():
    return jsonify([
        {'id': e.id, 'date': e.date, 'number': e.number}
        for e in Episode.query.all()
    ])

# GET /episodes/<id>
@episode_bp.route('/<int:id>', methods=['GET'])
def get_episode(id):
    ep = Episode.query.get_or_404(id)
    return jsonify({
        'id': ep.id,
        'date': ep.date,
        'number': ep.number,
        'appearances': [
            {'guest': app.guest.name, 'rating': app.rating}
            for app in ep.appearances
        ]
    })

# DELETE /episodes/<id>
@episode_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    ep = Episode.query.get_or_404(id)
    db.session.delete(ep)
    db.session.commit()
    return jsonify(message="Episode deleted"), 200