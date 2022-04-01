from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def email_validator(self,email):
        try:
            validate_email()
        except ValidationError:
            raise ValueError('Please provide a valid email address')

    def create_user(self,first_name,last_name,email,password,**extra_fields):
        if not username:
            # underscroe was used for django translation package to easily translate the log message
            raise valueError(_('Please submit a username'))
        
        if not first_name:
            raise valueError(_('Please submit a first name'))

        if not last_name:
            raise valueError(_('Please submit a last name'))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise valueError(_('Base user account: an email address is required'))
            
        user = self.model(
            username=username, first_name=first_name, last_name=last_name, email=email, **extra_fields
        )

        user.set_password(password)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        user.save(using=self._db) 
        return user


    def create_superuser(self,first_name,last_name,email,password,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superusers must have isStaff=True'))

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superusers must have is_superuser=True'))

        if not password:
            raise valueError(_('Superuser must have a password'))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise valueError(_('Admin account: an email address is required'))

        user = self.create_user(first_name, last_name, email, password, **extra_fields)
        user.save(using=self._db) 
        return user