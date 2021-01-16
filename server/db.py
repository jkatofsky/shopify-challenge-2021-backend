from flask_mongoengine import MongoEngine

db = MongoEngine()


class Image(db.Document):
    image = db.ImageField(required=True)


def read(id):
    return Image.objects.get_or_404(pk=id)


def delete(id):
    image_obj = Image.objects.get_or_404(pk=id)
    image_obj.image.delete()
    image_obj.delete()


def update(data: dict):
    image_obj = Image.objects.get_or_404(pk=data['id'])
    image = image_obj.image.read()
    
    if data['image'] != image:
        image_obj.image.put(data['image'], content_type='image/jpg')

    image_obj.save()


def create(data: dict):
    image_obj = Image.objects.create()
    image_obj.image.put(data['image'], content_type='image/jpg')

    image_obj.save()
    return image_obj.id
