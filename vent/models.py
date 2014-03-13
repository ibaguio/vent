from django.db import models
from django.contrib.auth.models import (
   AbstractBaseUser, BaseUserManager
)
from django.utils import timezone
class UserManager(BaseUserManager):
   def create_user(self, username, email, password=None):
      if not username:
         raise ValueError('Users must have a username')

      user = self.model(
         username=username,
         email=self.normalize_email(email),
      )

      user.set_password(password)
      user.save(using=self._db)
      return user

   def create_superuser(self, username, email, password):
      user = self.create_user(username,
         password=password,
         email=email
      )
      user.is_admin = True
      user.save(using=self._db)
      return user

class User(AbstractBaseUser):
   username = models.CharField(max_length=16, unique=True)
   email = models.EmailField(
     verbose_name='email address',
     max_length=255,
     unique=True,
   )
   first_name = models.CharField(max_length=30, blank=True)
   last_name = models.CharField(max_length=30, blank=True)
   contact = models.CharField(max_length=30, blank=True)
   age = models.IntegerField(max_length=100, blank=True, null=True)
   gender = models.CharField(max_length=6,choices=(("M","Male"),("F","Female")))

   joined = models.DateTimeField(default=timezone.now)
   is_active = models.BooleanField(default=True)
   is_admin = models.BooleanField(default=False)
   org = models.ManyToManyField('Organization')

   objects = UserManager()

   USERNAME_FIELD = 'username'
   REQUIRED_FIELDS = ['email']

   def get_full_name(self):
      full_name = '%s %s' % (self.first_name, self.last_name)
      return full_name.strip()

   def get_short_name(self):
      return self.first_name

   # On Python 3: def __str__(self):
   def __unicode__(self):
      return self.username

   def has_perm(self, perm, obj=None):
      "Does the user have a specific permission?"
       # Simplest possible answer: Yes, always
      return True

   def has_module_perms(self, app_label):
      "Does the user have permissions to view the app `app_label`?"
      # Simplest possible answer: Yes, always
      return True

   @property
   def is_staff(self):
      "Is the user a member of staff?"
      # Simplest possible answer: All admins are staff
      return self.is_admin

class Organization(models.Model):
   choices = (("Org","Student Org"),("Council","Council"),("Frat","Fraternity"),("Soro","Sorority"),("Other","Other"))

   name = models.CharField(max_length=30, blank=True)
   
   #contact info
   members = models.IntegerField()
   point_person = models.CharField(max_length=40, blank=True)
   point_person_number = models.CharField(max_length=15, blank=True)
   website = models.CharField(max_length=40, blank=True)
   twitter = models.CharField(max_length=16, blank=True)
   facebook = models.CharField(max_length=30, blank=True)
   category = models.CharField(max_length=12, choices=choices)
   college = models.CharField(max_length=32)
   history = models.CharField(max_length=300)

   location = models.CharField(max_length=100, blank=True)
   joined = models.DateTimeField(default=timezone.now)

   admin = models.ManyToManyField('User')

   def __unicode__(self):
      return self.name

class Events(models.Model):
   name = models.CharField(max_length=32)
   start_time = models.DateTimeField() 
   stop_time = models.DateTimeField()
   description = models.CharField(max_length=64)
   location = models.CharField(max_length=32)
   main_org = models.ForeignKey('Organization',related_name='main_org')
   partner_orgs = models.ManyToManyField('Organization',related_name='partner_orgs')

