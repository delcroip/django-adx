from django.db.models import Model, CharField, UUIDField, DateField, ForeignKey, CASCADE
import uuid


class Gender(Model):
    name = CharField(max_length=1)
    code = CharField(max_length=10, unique=True)
    
    def __str__(self):
        return self.name


class HealthFacility(Model):
    uuid = UUIDField(default=uuid.uuid4, editable=False, unique=True)
    
    def __str__(self):
        return str(self.uuid)


class Insuree(Model):
    dob = DateField()
    gender = ForeignKey(Gender, on_delete=CASCADE)
    code = CharField(max_length=100, unique=True)
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    uuid = UUIDField(default=uuid.uuid4, editable=False, unique=True)
    fsp = ForeignKey(HealthFacility, on_delete=CASCADE, null=True, related_name='insurees')
    validity_from = DateField()
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
