import os
import random

import requests
from logzero import logger


def lambda_handler(event: dict, context) -> dict:
    response_url = event["headers"]["Nightbot-Response-Url"]
    user_info = header_to_dict(event["headers"]["Nightbot-User"])
    channel_info = header_to_dict(event["headers"]["Nightbot-Channel"])
    filter_list = set(os.environ.get("FILTERED", "").split(","))

    if user_info["providerId"] in filter_list:
        logger.info(f"""User {user_info["displayName"]} (ID: {user_info["providerId"]}) was filtered""")
        return None

    negative_text = [
        "Try whaling next time, I heard that helps PepeLaugh",
        "Don't laugh, this could happen to anybody! DontBully",
        "Better luck next time KannaBlob",
        "A critical failure! PeepoRunCry",
        "How humiliating FeelsBadMan",
    ]

    positive_text = [
        "FeelsOkayMan",
        "RainbowDaijoubu",
        "COGGERS",
        "EHEHE",
        "oddonePog",
        "POGGERS",
        "peepoClap",
        "PepoCheer",
        "PagChomp",
        "FeelsGoodMan",
        "FeelsAmazingMan",
        "VisLaud"
    ]

    neutral_text = [
        "OhISee",
        "PepoG"
    ]

    min_value = 1
    max_value = 20
    roll_value = random.randint(min_value, max_value)
    return_string = [f"""{user_info["displayName"]} rolled a {roll_value}."""]

    if roll_value == max_value:
        return_string.append(positive_text[random.randrange(len(positive_text))])
    elif roll_value == min_value:
        return_string.append(negative_text[random.randrange(len(negative_text))])
    else:
        return_string.append(neutral_text[random.randrange(len(neutral_text))])

    request_body = {
        "message": " ".join(return_string)
    }

    a = requests.post(response_url, None, request_body)


def header_to_dict(header: str) -> dict:
    output = {}
    header_split = header.split("&")
    for frag in header_split:
        pair = frag.split("=")
        output[pair[0]] = pair[1]

    return output
