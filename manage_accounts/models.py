from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractUser
# Create your models here.
from django.utils.translation import gettext_lazy as _



class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    use_in_migrations = True
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    
    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)
    
    


class MyUser(AbstractUser):
    username=None
    email=models.EmailField(_('email address'),unique=True,max_length=120)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    profile=models.ImageField(uploaded_to="app/profile/img",blank=True,null=True)
    
    objects=UserManager()
    
    REQUIRED_FIELDS=[]
    USERNAME_FIELD='email'

    def __str__(self) -> str:
        return self.email
    
    
    
    