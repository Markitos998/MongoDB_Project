from django.utils import timezone
from mongoengine import Document, fields

class ToDoItem(Document):
    text = fields.StringField(max_length=100)
    due_date = fields.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.text}: due {self.due_date}"