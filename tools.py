import os
import json

from const import UNDESIRED_WORDS


def return_file_path(file_name: str) -> str:
    """
    This function returned the complete path since the folder 'statics'
    of a given file, if its not found it returned an error message.
    """

    for each_path in os.walk('statics'):
        if file_name in each_path[2]:
            return os.path.join(each_path[0], file_name)


def load_feedbacks():
    """  """

    json_file = open(return_file_path("feedbacks.json"))
    copy = {}
    js = json_file.read()
    data = json.loads(js)
    copy.update(data)

    return copy


def add_feedback(new_version: dict) -> bool:
    """  """

    try:
        with open(return_file_path("feedbacks.json"), "w", encoding="utf-8") as new:
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