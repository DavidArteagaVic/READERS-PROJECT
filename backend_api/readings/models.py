from django.db import models
import datetime


# Create your models here.

class books(models.Model):
    title = models.CharField(max_length = 255)
    author = models.CharField(max_length = 255)
    genre = models.CharField (max_length = 100)
    published_year = models.IntegerField()
    isbn = models.CharField (max_length = 13)
    publisher = models.CharField(max_length = 255) 
    pages = models.IntegerField()
    lenguage = models.CharField(max_length = 50)
    description = models.TextField()
    cover_image_url = models.CharField(max_length = 255)
    created_at = models.DateTimeField(default = datetime.datetime.now())
    updated_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)
    status = models.BooleanField(default=True) 
    
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Published Year: {self.published_year}, ISBN: {self.isbn}, Publisher: {self.publisher}, Pages: {self.pages}, Language: {self.language}, Description: {self.description}, Created At: {self.created_at}, Updated At: {self.updated_at}, Deleted At: {self.deleted_at}, Status: {self.status}"
