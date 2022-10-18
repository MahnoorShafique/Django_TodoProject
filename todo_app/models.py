import uuid

from django.db import models

# Create your models here.
class STATUS_CHOICES(models.TextChoices):
    PN='PN','pending'
    BL='BL','block'
    DN='DN','done'
class Todo(models.Model):
#     STATUS_CHOICES=(
#         ('pn', 'pending'),
#     ('bl', 'block'),
#    ('dn', 'done')    )
    task_name=models.CharField(max_length=50)
    task_id= models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    created_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    updated_date = models.DateField(auto_now=True)
    status=models.CharField(default='PN',choices=STATUS_CHOICES.choices,max_length=2)
    description = models.TextField()

    def __str__(self):
        return self.task_name