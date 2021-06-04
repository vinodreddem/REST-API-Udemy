from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for User Profiles    """
    def create_user(self, email, name, password=None):
        """Create a new User profile """
        if not email:
            raise ValueError('User Must have an email Address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name) #Create the user, which interns calls the BaseManager method
        user.set_password(password) #Set the Password for user, wich is kind of encryption
        user.save()
        return user
    
    def create_superuser(self, email, name, password):
        """ Create the Super User and Note there should be password it shoul not be NOne in this case"""
        user = self.create_user(email, name, password)
       
        user.is_superuser = True #From Permission MIXIN
        user.is_staff = True #From Permission MixIn classs
        user.save(using = self._db)
        
        return user
    

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Database Model for User """
    email = models.EmailField(max_length=250, unique = True)
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserProfileManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    def get_full_name(self):
        """ get the full name of the user
        """
        return self.name
    
    def __str__(self):
        """ return the string representation of the user """
        return self.email
    