from flask import Blueprint, request, jsonify
from core.tweet.services import TweetService
from core.common.utils import ObjectMapperUtil
from datetime import datetime

# Define a new Blueprint for tweets
tweet_blueprint = Blueprint("tweet_blueprint", __name__)
# Create an instance of the TweetService
tweet_service = TweetService()  

# Define a route for posting a new tweet
@tweet_blueprint.route("", methods=["POST"])
def post_tweet():
    # Get the tweet content from the request body
    tweet_content = request.json.get("tweet")

    if tweet_content:
        # For now, the user_id is hardcoded as 1
        user_id = 1
        # The published_at time is set to the current time
        published_at = datetime.now()

        # Create a new tweet using the TweetService
        new_tweet = tweet_service.create_tweet(user_id=user_id, tweet=tweet_content, published_at=published_at)
        # Return the new tweet with a 201 status code
        return jsonify(new_tweet), 201
    else:
        # If no tweet content was provided, return an error with a 400 status code
        return jsonify({"error": "Tweet content not found"}), 400
    
# Define a route for getting all tweets
@tweet_blueprint.route("", methods=["GET"])
def get_all_tweets():
    # Get all tweets using the TweetService
    all_tweets = tweet_service.get_all()

    if all_tweets:
        # If there are tweets, return them with a 200 status code
        return jsonify(ObjectMapperUtil.map(all_tweets)), 200
    else:
        # If there are no tweets, return an error with a 404 status code
        return jsonify({"error": "No tweets found"}), 404 