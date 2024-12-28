def build_response(parsed_data):
    """
    Builds a response message based on the parsed user input.

    Args:
        parsed_data (dict): Parsed input data.

    Returns:
        str: Response message.
    """
    username = parsed_data.get("username", "User")
    return f"Hi @{username}, your custom manga PFP is being generated! Stay tuned!"

def send_response(api, tweet_id, response_message):
    """
    Sends a response to a specific tweet.

    Args:
        api (tweepy.API): Authenticated Twitter API client.
        tweet_id (int): ID of the tweet to respond to.
        response_message (str): The response message to send.

    Returns:
        None
    """
    try:
        api.update_status(status=response_message, in_reply_to_status_id=tweet_id)
        print(f"Response sent to tweet ID {tweet_id}: {response_message}")
    except Exception as e:
        print(f"Error sending response: {e}")
