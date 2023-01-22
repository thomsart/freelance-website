"""
All path and files we need for the web-site.
"""

import os

css_root = os.path.join("static", "css")
css = [f for f in os.listdir(css_root) if os.path.isfile(os.path.join(css_root, f))]

js_root = os.path.join("static", "js")
js = [f for f in os.listdir(js_root) if os.path.isfile(os.path.join(js_root, f))]

font_serif_root = os.path.join("static", "medias", "font", "serif")
font_serif = [f for f in os.listdir(font_serif_root) if os.path.isfile(os.path.join(font_serif_root, f))]

font_noserif_root = os.path.join("static", "medias", "font", "no_serif")
font_noserif = [f for f in os.listdir(font_noserif_root) if os.path.isfile(os.path.join(font_noserif_root, f))]

icon_root = os.path.join("static", "medias", "icon")
icon = [f for f in os.listdir(icon_root) if os.path.isfile(os.path.join(icon_root, f))]

photo_root = os.path.join("static", "medias", "photo")
photo = [f for f in os.listdir(photo_root) if os.path.isfile(os.path.join(photo_root, f))]