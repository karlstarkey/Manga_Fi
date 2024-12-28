import tweepy
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Twitter API credentials from environment variables
API_KEY = os.getenv("TWITTER_API_KEY")
API_SECRET = os.getenv("TWITTER_API_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# Authenticate with Twitter API
def authenticate_twitter_api():
    """
    Authenticates and returns a Tweepy API client.
    """
    try:
        auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth, wait_on_rate_limit=True)
        print("Twitter API authenticated successfully!")
        return api
    except Exception as e:
        print(f"Error during Twitter API authentication: {e}")
        raise

# Example usage: Fetch user tweets
def fetch_mentions(api):
    """
    Fetches the latest mentions of the bot.

    Args:
        api (tweepy.API): Authenticated Twitter API client.

    Returns:
        list: List of tweets mentioning the bot.
    """
    try:
        mentions = api.mentions_timeline(count=10)
        return mentions
    except Exception as e:
        print(f"Error fetching mentions: {e}")
        return []
