# import uuid
from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from django.urls import reverse
from datetime import date

# Create your models here.
class Quote(models.Model):
    type_choices = (
    ('Casa', "Casa"),
    ('Escritório', 'Escritório'),
    ('Apartamento', 'Apartamento')
    )
    num_choices = (('1','1'),('2','2'),('3','3'),('4','4'),('5','5'))
    kitchen_choices = (('Microondas', 'Microondas'),
                        ('Frigorífico', 'Frigorífico'),
                        ('Forno', "Forno"))
    bedroom_choices = (('a', 'Limpeza do chão'),
                        ('b', 'Organização dos Armários'),
                        ('c', 'Troca de Roupa de Cama'))

    living_choices = (('a', 'Tirar pó dos armários'),
                        ('b', 'Limpeza interna dos armários'),
                        ('c', "Limpeza de pia e box" ))

    weekdays = (('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'))
    period = (('morning', 'morning'), ('afternoon', 'afternoon'))

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed.")


    response_id = models.AutoField(primary_key=True)
    # response_id = models.UUIDField(default=uuid.uuid4, editable=False)
    observations = models.CharField(max_length=200, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    client_name = models.CharField(max_length=200, blank=False, null=False)
    client_email = models.EmailField(max_length=200)
    mobile = models.CharField(validators=[phone_regex], max_length=15, blank=False)
    location_type = models.CharField(choices=type_choices, max_length=20)
    area_m2 = models.IntegerField(default=1, validators=[MaxValueValidator(999), MinValueValidator(0)])
    qty_bedroom = models.CharField(choices=num_choices, max_length=2)
    qty_living = models.CharField(choices=num_choices, max_length=2)
    qty_bathroom = models.CharField(choices=num_choices, max_length=2)
    window = models.BooleanField()
    qty_window = models.CharField(choices=num_choices, max_length=2)
    kitchen = models.BooleanField()
    kitchen_addon =models.CharField(blank=False, null=True, choices=kitchen_choices, max_length=50, default=None)
    bedroom_addon =models.CharField(blank=False, null=True, choices=bedroom_choices, max_length=50, default=None)
    living_addon = models.CharField(blank=False, null=True, choices=living_choices, max_length=100, default=None)
    last_clean = models.BooleanField(default=True)
    pets = models.BooleanField()
    best_day = models.CharField(choices=weekdays, max_length=50)
    best_time =models.CharField(choices=period, max_length=50)
    address = models.CharField(blank=True, null=True, max_length=200)

    #calculated fields


    def __str__(self):
        return str(self.pk) + " - " + self.client_name

    def get_absolute_url(self):
        return reverse('quote', kwargs={'pk': self.pk })

    @property
    def DaysSince(self):
        today = date.today()
        days_since = (today - self.timestamp.date()).days
