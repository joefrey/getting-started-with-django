from django.db import models
from django.db.models.signals import post_save
# get_user_model is a function
from django.contrib.auth.models import AbstractUser

# instead of using built user from django we should create our custom User class to avoid headache along the way.
# User = get_user_model()

# Create custom User model
class User(AbstractUser):
  # pass means nothing to add
  # pass 
  is_organizer = models.BooleanField(default=True)
  is_agent = models.BooleanField(default=False)

  # but it we want to add new field like phone number
  # cellphone_number = models.CharField(max_length=100)

class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.user.username

class Lead(models.Model):

  # SOURCE_CHOICES = (
  #   ('YT', 'YouTube'),
  #   ('Google', 'Google'),
  #   ('Newsletter', 'Newsletter'),
  # )

  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  age = models.IntegerField(default=0)
  organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
  # Many leads for one agent -- Many to one
  # Every lead associated with one agent
  agent = models.ForeignKey("Agent",  null=True, blank=True, on_delete=models.SET_NULL)

  def __str__(self):
    return f"{self.first_name} {self.last_name}"
  
  # agent = models.ForeignKey("Agent", on_delete=models.SET_NULL, null=True)
  # CASCADE once agent deleted the lead also deleted
  # SET_NULL
  # 

  # phoned = models.BooleanField(default=False) 
  # source = models.CharField(choices=SOURCE_CHOICES, max_length=100)

  # profile_picture = models.ImageField(blank=True, null=True)
  # special_files = models.FileField(blank=True, null=True)

class Agent(models.Model):
  # instead of using ForeignKey for user use OneToOneField because if 
  # we use ForeignKey creates many agents for one user
  # user = models.ForeignKey(User, on_delete=models.CASCADE)
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
  # -- noneed to add first_name and last_name fields coz it's already in the AbstractUser Model
  # first_name = models.CharField(max_length=20)
  # last_name = models.CharField(max_length=20)

  # if we put lead here as foreign key so every agent has one lead. so this wrong because if we have thousands of leads we would not have enough agent.
  # lead = models.ForeignKey('Lead', on_delete=models.CASCADE)

  # age = models.IntegerField(default=0)

  # special method on model
  def __str__(self):
    return self.user.email
  
# Signals
def post_user_created_signal(sender, instance, created, **kwargs):
  print(instance, created)
  if created:
    UserProfile.objects.create(user=instance)

post_save.connect(post_user_created_signal, sender=User)