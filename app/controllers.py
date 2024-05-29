from flask import Blueprint, request, jsonify
from .sentiment_analysis import SentimentIntensityAnalyzer

sentiment_bp = Blueprint('sentiment_bp', __name__)

@sentiment_bp.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    text = data['text']
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(text)
    return jsonify(scores)
