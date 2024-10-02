from flask import Blueprint, request, jsonify
from src.models.content_model import Content, db

content_bp = Blueprint('content_bp', __name__)

@content_bp.route('/create', methods=['POST'])
def create_content():
    data = request.get_json()
    new_content = Content(title=data['title'], content_type=data['content_type'], url=data['url'], user_id=data['user_id'])
    db.session.add(new_content)
    db.session.commit()
    return jsonify({'message': 'Content created successfully'}), 201

@content_bp.route('/<int:id>', methods=['GET'])
def get_content(id):
    content = Content.query.get_or_404(id)
    return jsonify({
        'title': content.title,
        'content_type': content.content_type,
        'url': content.url
    })

@content_bp.route('/<int:id>/delete', methods=['DELETE'])
def delete_content(id):
    content = Content.query.get_or_404(id)
    db.session.delete(content)
    db.session.commit()
    return jsonify({'message': 'Content deleted successfully'}), 204

