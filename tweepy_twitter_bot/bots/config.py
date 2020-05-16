# import tweepy, logging and os modules to config.py
import tweepy
import logging
import os

# define a variable for calling logging module
logger = logging.getLogger()

# create twitter api function to be reused across all bots
def create_api():
    # input twitter api credentials
    consumer_key = os.getenv("JLKFgAoS1zwP0OfQWWlgHxxWm")
    consumer_secret = os.getenv("PUs78WIfZvt1c8p3s2RuoAw2amBu1K6nIugy9WFI5xHEDVBKfM")
    access_token = os.getenv("1261346688884563968-xRNEoQhTJMJ2GjXHPAfvT5Vs8BTyVJ")
    access_token_secret = os.getenv("9q42pHeji4KyPbYRZuPTiAeXruvavi1lPgPVU0siDooRY")

    # create api request for twitter api
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    # check for connection errors and log if any
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api




