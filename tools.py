import os
import json



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