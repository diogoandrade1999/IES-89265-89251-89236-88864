import mongoengine


'''
mongoengine.connect(
    db='ies_db',
    username='ies_user',
    password='iespass',
    host='192.168.160.212'
)
'''
mongoengine.connect(
    db='ies_db',
    host='localhost'
)


class ExercisesModel(mongoengine.EmbeddedDocument):
    weight = mongoengine.FloatField()
    repetitions = mongoengine.IntField()


class WorkModel(mongoengine.Document):
    _id = mongoengine.ObjectIdField()
    user_id = mongoengine.IntField()
    type_exercise = mongoengine.StringField()
    machine = mongoengine.StringField()
    date = mongoengine.DateTimeField()
    heartbeat = mongoengine.IntField()
    exercises = mongoengine.ListField(mongoengine.EmbeddedDocumentField(ExercisesModel))


class UserModel(mongoengine.Document):
    _id = mongoengine.ObjectIdField()
    user_id = mongoengine.IntField()
    name = mongoengine.StringField()
    email = mongoengine.EmailField()
    birth_date = mongoengine.DateTimeField()
    start = mongoengine.DateTimeField()
    weight = mongoengine.FloatField()
    height = mongoengine.FloatField()
    personal_trainer = mongoengine.StringField()
    medical_condicions = mongoengine.StringField()


class BitModel(mongoengine.Document):
    _id = mongoengine.ObjectIdField()
    user_id = mongoengine.IntField()
    bits = mongoengine.ListField(mongoengine.StringField())
