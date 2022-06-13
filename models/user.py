from mongoengine import EmailField, StringField, BooleanField, DateTimeField, Document, EmbeddedDocument, EmbeddedDocumentField, ListField, ReferenceField, IntField, FloatField

class MongoUser(User):
    email = EmailField(required=True)
    username = StringField(required=True)
    password = StringField(required=True)
    is_active = BooleanField(default=True)
    first_name = StringField(default=None)
    last_name = StringField(default=None)



