import mongoengine


mongoengine.connect(
    'ies_db',
    host='192.168.160.212',
    port=27017,
    password='iespass'
)

'''
{'date': '2019-12-08 12:38:18',
  'exercises': [{'weight': 38.12, 'repetitions': 3}],
  'machine': 'Cable triceps bar',
  'heartbeat': 164,
  'user': 'Diogo',
  'type': 'triceps'}
'''


class ExercisesModel(mongoengine.EmbeddedDocument):
    weight = mongoengine.FloatField()
    repetitions = mongoengine.IntField()


class WorkModel(mongoengine.Document):
    _id = mongoengine.ObjectIdField()
    user = mongoengine.StringField()
    type = mongoengine.StringField()
    machine = mongoengine.StringField()
    date = mongoengine.DateTimeField()
    heartbeat = mongoengine.IntField()
    exercises = mongoengine.ListField(mongoengine.EmbeddedDocumentField(ExercisesModel))


'''
{'name': 'Diogo', 'start': '2019-07-01', 'email': 'diogo.andrade@ua.pt', 'birth_date': '1999-04-07', 'weight': 61}
'''


class UserModel(mongoengine.Document):
    _id = mongoengine.ObjectIdField()
    name = mongoengine.StringField()
    email = mongoengine.EmailField()
    birth_date = mongoengine.DateTimeField()
    start = mongoengine.DateTimeField()
    weight = mongoengine.FloatField()


'''
{'name': 'José', 'email': 'jose@gym.pt', 'password': '1234'}
'''

'''
class PersonalModel(mongoengine.Document):
    _id = mongoengine.StringField()
    name = mongoengine.StringField()
    email = mongoengine.EmailField()
    password = mongoengine.StringField()
'''
'''
class DynamicPageModel(DynamicDocument):
    title = StringField(max_length=150, required=True)
'''
