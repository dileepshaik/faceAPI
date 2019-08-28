import requests
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib import patches
from io import BytesIO
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

#Display the image

image_orig = open(image_path, "rb").read()
image = Image.open(BytesIO(image_orig))

plt.figure(figsize=(12, 12))
ax = plt.imshow(image, alpha=1)
for face in faces:
    fr = face["faceRectangle"]
    fa = face["faceAttributes"]
    origin = (fr["left"], fr["top"])
    p = patches.Rectangle(
        origin, fr["width"], fr["height"], fill=False, linewidth=2, color='b')
    plt.text(origin[0], origin[1], "%s, %d , %s" % (fa["gender"], fa["age"], fa["glasses"]),
             fontsize=20, color='w', weight="bold", va="bottom")
    ax.axes.add_patch(p)

_ = plt.axis("off")
plt.show()
