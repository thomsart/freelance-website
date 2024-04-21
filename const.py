"""
All constants of the application.
"""

URLS = {
    'home': '/',
    'contact': '/contact',
    'blog': '/blog',
    'comment': '/comment',
    'mentions_legales': '/mentions_legales',
    'static': '/<filename>',
}

UNDESIRED_WORDS = [
    "SEO", "Seo", "seo", "Hi", "hi","Are", "are", "You", "you", "We", "we", "To", "to", 
    "Hola", "Wilkomenn",
    "Ո", "ղ", "ջ", "ն", "з", "д", "й",
    "https://", "http://",
]