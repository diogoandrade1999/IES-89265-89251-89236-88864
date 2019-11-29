from mongoengine import *

connect(
    'teste_db',
    host='172.17.0.1',
    port=27017
)


class ChoiceModel(EmbeddedDocument):
    choice_text = StringField(max_length=200)
    votes = IntField(default=0)


class PollModel(Document):
    question = StringField(max_length=200)
    pub_date = DateTimeField(help_text='date published')
    choices = ListField(EmbeddedDocumentField(ChoiceModel))


class DynamicPageModel(DynamicDocument):
    title = StringField(max_length=150, required=True)
