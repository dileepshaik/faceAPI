
subscription_key = "ENTER YOUR KEY HERE" #DSFace API
face_api_url = 'https://eastus2.api.cognitive.microsoft.com/face/v1.0/detect'


def config():
    print("Call Config")
    return subscription_key, face_api_url
