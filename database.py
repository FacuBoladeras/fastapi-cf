from peewee import *
from datetime import datetime
from datetime import *
import hashlib

database = MySQLDatabase(
                        "fastapi_project",
                        user="root",
                        password="Soler839",
                        host="localhost",
                        port=3306)

class User(Model):
    username = CharField(max_length=50, unique=True)
    password= CharField(max_length=50)
    created_at= DateTimeField(default= datetime.now)

    
    def __str__(self) -> str:
        return self.username
    
    class Meta:        
        database= database
        table_name = "users"
        
    @classmethod
    def create_password(cls, password):
        h = hashlib.md5()
        h.update(password.encode("utf-8"))
        return h.hexdigest()
    
class Movie(Model):
    
    tittle = CharField(max_length=50)
    created_at = DateTimeField(default= datetime.now)
    
    def __str__(self) -> str:
        return self.tittle
    
    class Meta:        
        database= database
        table_name = "movies"
    
class UserReview(Model):
    user = ForeignKeyField(User, backref='reviews')
    movie = ForeignKeyField(Movie)
    review = TextField()
    score = IntegerField()
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = database
        table_name = 'user_reviews'

    def __str__(self):
        return f'{self.user.username} - #{self.movie.title}'