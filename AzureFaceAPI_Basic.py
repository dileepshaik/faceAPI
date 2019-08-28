import requests
from PIL import Image
import os
import FaceAPIConfig as cnfg

image_path = os.path.join('C:/Py/FaceAPIAzure/CapFrame.jpg')
image_data = open(image_path, "rb")

subscription_key, face_api_url = cnfg.config();

headers = {'Content-Type': 'application/octet-stream',
           'Ocp-Apim-Subscription-Key': subscription_key}

params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'true',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion'
}

response = requests.post(face_api_url, params=params, headers=headers, data=image_data)
response.raise_for_status()
faces = response.json()
print(faces)

