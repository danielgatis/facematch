import io

import face_recognition
import numpy as np
from PIL import Image, ImageDraw

RED = (255, 0, 0)
GREEN = (0, 255, 0)
SIZE = 500
HALF_SIZE = 250

class EncodingError(Exception):
    pass


def get_concat_h_blank(im1, im2, color=(0, 0, 0)):
    dst = Image.new("RGB", (im1.width + im2.width, max(im1.height, im2.height)), color)
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst


def features(data):
    img = Image.open(io.BytesIO(data))
    img = img.convert("RGB")

    w, h = img.size
    img = img.resize((SIZE, int(SIZE * (h / w))), Image.ANTIALIAS)

    img_np = np.array(img)
    face_encodings = face_recognition.face_encodings(img_np)

    if len(face_encodings) != 1:
        raise EncodingError("The image must contain only one face")

    face_locations = face_recognition.face_locations(
        img_np, number_of_times_to_upsample=0, model="cnn"
    )

    face_images = []
    for (top, right, bottom, left) in face_locations:
        face_image = Image.fromarray(img_np[top:bottom, left:right])

        w, h = face_image.size
        face_image = face_image.resize((HALF_SIZE, int(HALF_SIZE * (h / w))), Image.ANTIALIAS)

        face_images.append(face_image)

    return (face_encodings[0], face_locations[0], face_images[0])


def match(data1, data2, threshold=0.6):
    try:
        face_encoding1, face_location1, face_img1 = features(data1)
    except EncodingError as err:
        raise EncodingError("The first image must contain only one face")

    try:
        face_encoding2, face_location2, face_img2 = features(data2)
    except EncodingError as err:
        raise EncodingError("The second image must contain only one face")

    distance = face_recognition.face_distance([face_encoding1], face_encoding2)[0]

    result = distance <= threshold
    color = GREEN if result else RED

    out = get_concat_h_blank(face_img1, face_img2)
    draw = ImageDraw.Draw(out)

    tw, th = draw.textsize(str(distance))
    ow, oh = out.size

    draw.text((ow - tw, oh - th), str(distance), color)

    bio = io.BytesIO()
    out.save(bio, "PNG")

    return (result, distance, bio.getbuffer())
