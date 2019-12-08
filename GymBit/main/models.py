from mongoengine import *

connect(
    'ies_db',
    '''host='172.17.0.1',
    port=27017'''
)

'''
{'date': '2019-12-08 12:38:18',
  'exercises': [{'weight': 38.12, 'repetitions': 3}],
  'machine': 'Cable triceps bar',
  'user': 'Diogo',
  'type': 'triceps'}
'''


class ExercisesModel(EmbeddedDocument):
    weight = FloatField()
    repetitions = IntField()


class WorkModel(Document):
    user = StringField()
    type = StringField()
    machine = StringField()
    date = DateTimeField()
    exercises = ListField(EmbeddedDocumentField(ExercisesModel))


'''
{'name': 'Diogo', 'start': '2019-07-01', 'email': 'diogo.andrade@ua.pt', 'birth_date': '1999-04-07', 'weight': 61}
'''


class UserModel(Document):
    name = StringField()
    email = EmailField()
    birth_date = DateTimeField()
    start = DateTimeField()
    weight = FloatField()


'''
class DynamicPageModel(DynamicDocument):
    title = StringField(max_length=150, required=True)
'''
