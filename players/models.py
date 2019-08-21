from django.db import models
from django.utils import timezone

class Club(models.Model):
    name = models.CharField(max_length=20)
    coach_name = models.CharField(max_length=30)
    coach_contact = models.CharField(max_length=15)
    team_manager = models.CharField(max_length=30)
    team_manager_contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class High_school(models.Model):
    name = models.CharField(max_length=225)
    location = models.CharField(max_length=100)
    patron = models.CharField(max_length=100)
    patron_contact = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name

class Role(models.Model):
    role = models.CharField(max_length=10)
    
    def __str__(self):
        return self.role


class Position(models.Model):
    name = models.CharField(max_length=20)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Player(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=15)
    kin = models.CharField(max_length=30)
    kin_contact = models.CharField(max_length=15)
    passport = models.CharField(max_length=150, null=True)
    allergy = models.CharField(max_length=200, null=True)
    injury_history = models.CharField(max_length=225, null=True)
    skills = models.CharField(max_length=225, null=True)
    about_player = models.CharField(max_length=225, null=True)
    tertiary_institution = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=200, null=True)
    address_contact = models.CharField(max_length=15, null=True)
    id_number = models.CharField(max_length= 9, null=True)
    image =models.ImageField(upload_to='static/img', null=True, blank=True, default='default-user.png')


    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    school = models.ForeignKey(High_school, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    last_modified = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "{}  {}".format(self.first_name[:25], self.last_name[:25])
    def age(self):
        return timezone.now().year - self.date_of_birth.year