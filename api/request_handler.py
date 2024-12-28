def parse_request(tweet):
    """
    Parses the user's tweet to extract relevant input for the bot.

    Args:
        tweet (tweepy.models.Status): A tweet mentioning the bot.

    Returns:
        dict: Parsed data such as user ID, username, and input text.
    """
    try:
        user_id = tweet.user.id
        username = tweet.user.screen_name
        text = tweet.text.replace("@YourBotHandle", "").strip()  # Remove bot mention
        return {"user_id": user_id, "username": username, "text": text}
    except Exception as e:
        print(f"Error parsing request: {e}")
        return {}
