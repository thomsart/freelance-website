import os
import json

from const import UNDESIRED_WORDS


def load_feedbacks():
    """  """

    path = os.path.join("static", "medias", "blog", "feedbacks.json")
    json_file = open(path)

    copy = {}
    js = json_file.read()
    data = json.loads(js)
    copy.update(data)

    return copy


def add_feedback(new_version: dict) -> bool:
    """  """

    path = os.path.join("static", "medias", "blog", "feedbacks.json")

    try:
        with open(path, "w", encoding="utf-8") as new:
            json.dump(new_version, new)

        return True

    except:
        return False


def is_valid_form(email, job, link):
    """
    This functionn allows to filtre all shity emails.
    """

    if email==None or job==None:
        return False

    if link!="None":
        if "https//" not in link:
            return False

    if len(job) < 50:
        return False

    for word in UNDESIRED_WORDS:
        if word in email:
            return False

    return True