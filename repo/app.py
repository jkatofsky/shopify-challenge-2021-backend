from flask import Flask, request, send_file
from flask_cors import CORS
import base64
import io

app = Flask(__name__)
cors = CORS(app)

import db

db.db.init_app(app)


def base64_convert(base64_image):
    try:
        io.BytesIO(base64.decodebytes(bytes(base64_image, encoding="ascii")))
    except:
        return None


@app.route('/images', methods=['GET', 'DELETE', 'PUT', 'POST'])
def images():

    data = request.json.copy()

    if request.method in ['GET', 'DELETE', 'PUT'] and not data['id']:
        return "ERROR: image ID required", 400
    if request.method in ['PUT', 'POST'] and not data['image']:
        return "ERROR: base64 image required", 400

    if request.method == 'GET':
        image_obj = db.read(data['id'])
        return send_file(image_obj.image, mimetype="image/jpg"), 200

    elif request.method == 'DELETE':
        db.delete(data['id'])
        return {'id': str(data['id'])}, 200

    else:
        image = base64_convert(data['image'])
        if not image:
            return "ERROR: invalid image", 400
        data['image'] = image

        if request.method == 'PUT':
            db.update(data)
            return {'id': str(data['id'])}, 200

        elif request.method == 'POST':
            id = db.create(data)
            return {'id': str(id)}, 200


if __name__ == "__main__":
    app.run(debug=True)
