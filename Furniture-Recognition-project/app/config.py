import os
class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    UPLOAD_FOLDER = "image-file"
    CSRF_ENABLED = True
    DEBUG = False
    
    # Enter your API Key and Custom Classifier ID below
    API_KEY = "18pWdvmGn6s94t7iBYT9C54x3ztNo47dKij7TjsRBpyW"
    CLASSIFIER_ID = ""
