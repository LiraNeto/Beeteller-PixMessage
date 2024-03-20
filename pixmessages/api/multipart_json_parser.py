from rest_framework.renderers import JSONRenderer


class MultiPartJsonParser(JSONRenderer):

    media_type = 'multipart/json'
