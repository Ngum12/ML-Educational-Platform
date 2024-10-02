from flask import Blueprint, request, jsonify
from src.models.quiz_model import Quiz, db

quiz_bp = Blueprint('quiz_bp', __name__)

@quiz_bp.route('/create', methods=['POST'])
def create_quiz():
    data = request.get_json()
    new_quiz = Quiz(title=data['title'], questions=data['questions'], user_id=data['user_id'])
    db.session.add(new_quiz)
    db.session.commit()
    return jsonify({'message': 'Quiz created successfully'}), 201

@quiz_bp.route('/<int:id>', methods=['GET'])
def get_quiz(id):
    quiz = Quiz.query.get_or_404(id)
    return jsonify({
        'title': quiz.title,
        'questions': quiz.questions
    })

@quiz_bp.route('/<int:id>/delete', methods=['DELETE'])
def delete_quiz(id):
    quiz = Quiz.query.get_or_404(id)
    db.session.delete(quiz)
    db.session.commit()
    return jsonify({'message': 'Quiz deleted successfully'}), 204

