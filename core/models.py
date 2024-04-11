from django.db import models

# Create your models here.
class UserModel(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 255)
    age = models.IntegerField()
    dob = models.DateField()

    @classmethod
    def createUser(cls, name, email, age, dob):
        user = cls(name = name, email = email, age = age, dob = dob)
        user.save()

    @classmethod
    def getAllUsers(cls):
        return cls.objects.all()
    
    @classmethod
    def getAllUsersById(cls, id):
        try:
            return cls.objects.get(id = id)
        except cls.DoesNotExist:
            return None
        
    @classmethod
    def updateUser(cls, user_id, new_name, new_email, new_age, new_dob):
        user = cls.objects.get(pk = user_id)

        user.name = new_name
        user.age = new_age
        user.email = new_email
        user.dob = new_dob
        user.save()

    @classmethod
    def deleteUser(cls, user_id):
        user = cls.objects.get(id = user_id)
        user.delete()

    def __str__(self):
        return self.name