from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


Bedfordshire = 'Bedfordshire'
Berkshire = 'Berkshire'
Bristol = 'Bristol'
Buckinghamshire = 'Buckinghamshire'
Cambridgeshire = 'Cambridgeshire'
Cheshire = 'Cheshire'
City_of_London = 'City_of_London'
Cornwall = 'Cornwall'
County_Durham = 'County_Durham'
Cumbria = 'Cumbria'
Derbyshire = 'Derbyshire'
Devon = 'Devon'
Dorset = 'Dorset'
East_Riding_of_Yorkshire = 'East_Riding_of_Yorkshire'
East_Sussex = 'East_Sussex'
Essex = 'Essex'
Gloucestershire = 'Gloucestershire'
Greater_London = 'Greater_London'
Greater_Manchester = 'Greater_Manchester'
Hampshire = 'Hampshire'
Herefordshire = 'Herefordshire'
Hertfordshire = 'Hertfordshire'
Isle_of_Wight = 'Isle_of_Wight'
Kent = 'Kent'
Lancashire = 'Lancashire'
Leicestershire = 'Leicestershire'
Lincolnshire = 'Lincolnshire'
Merseyside = 'Merseyside'
Norfolk_East = 'Norfolk_East'
North_Yorkshire = 'North_Yorkshire'
Northamptonshire = 'Northamptonshire'
Northumberland = 'Northumberland'
Nottinghamshire = 'Nottinghamshire'
Oxfordshire = 'Oxfordshire'
Rutland = 'Rutland'
Shropshire = 'Shropshire'
Somerset = 'Somerset'
South_Yorkshire = 'South_Yorkshire'
Staffordshire = 'Staffordshire'
Suffolk_East = 'Suffolk_East'
Surrey = 'Surrey'
Tyne_Wear = 'Tyne_Wear'
Warwickshire = 'Warwickshire'
West_Midlands = 'West_Midlands'
West_Sussex = 'West_Sussex'
West_Yorkshire = 'West_Yorkshire'
Wiltshire  = 'Wiltshire '
Worcestershire = 'Worcestershire'

COUNTIES = [
    (Bedfordshire, 'Bedfordshire'),
    (Berkshire, 'Berkshire'),
    (Bristol, 'Bristol'),
    (Buckinghamshire, 'Buckinghamshire'),
    (Cambridgeshire, 'Cambridgeshire')
]



class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    contact information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(
        max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(
        max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True)
    default_county = models.CharField(
        max_length=80, null=True, blank=True,
        choices=COUNTIES)
    default_postcode = models.CharField(
        max_length=20, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
        # Existing users: just save the profile
        instance.userprofile.save()