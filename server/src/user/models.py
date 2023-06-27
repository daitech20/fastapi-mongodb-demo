from umongo import Document, fields
from server.database import get_database, get_umongo_instance

ame = get_database()
ame_instance = get_umongo_instance()



@ame_instance.register
class Users(Document):
    username = fields.StrField(unique=True)
    email = fields.EmailField(unique=True)
    password = fields.StrField()
    fullname = fields.StrField(default="John")

    class Meta:
        collection = ame.users