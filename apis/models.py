from django.db import models

class AddressManager(models.Manager):
    def get_by_natural_key(self, street1, street2, city, state, zipcode, latitude, longitude):
        return self.get(street1=street1, street2=street2, city=city, state=state, zipcode=zipcode, latitude=latitude, longitude=longitude)

class Address(models.Model):
    street1 = models.CharField(max_length=80)
    street2 = models.CharField(max_length=80, blank=True)
    city = models.CharField(max_length=80)
    state = models.CharField(max_length=80)
    zipcode = models.CharField(max_length=80)
    latitude  = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    def __unicode__(self):
        return u"%s (%s)" % (self.street1,self.zipcode)

    def natural_key(self):
        return (self.street1, self.street2, self.city, self.state, self.zipcode, self.latitude, self.longitude)


    class Meta:
        unique_together = (('street1', 'street2', 'city', 'state', 'zipcode', 'latitude', 'longitude'),)
        

class Startup(models.Model):
    INDUSTRY_CHOICES = (
    ('Tech', 'Technology'),
    ('Med', 'Medical'),
    ('Consumer', 'Consumer Goods'),
    ('Energy', 'Energy'),
    ('Other', 'Other'),
)
    SIZE_CHOICES = (
        ('1', '1-4'),
        ('5', '5-9'),
        ('10', '10+'),
)

    name = models.CharField(max_length=200)
    founded = models.DateField('date started')
    url = models.URLField(verify_exists=True, blank=True)
    jobs_url = models.URLField(blank=True)
    industry = models.CharField(max_length=20, choices=INDUSTRY_CHOICES)
    description = models.TextField(blank=True)
    employee_count = models.CharField(max_length=6, choices=SIZE_CHOICES)
    linkedin = models.URLField(blank=True)
    twitter = models.CharField(max_length=18,blank=True) 
    hiring = models.BooleanField(blank=True)
    admin_email = models.EmailField(blank=True)
    hq = models.ForeignKey(Address)

    def __unicode__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.ForeignKey(Address)
    when = models.DateTimeField()
    url = models.URLField(blank=True)
    
    def __unicode__(self):
        return self.name

class Resource(models.Model):
    RESOURCE_TYPE_CHOICES = (
    ('Investor', 'Investor'),
    ('Incubator', 'Incubator/Accelerator'),
    ('CoworkSpace', 'Co-working space'),
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.ForeignKey(Address)
    url = models.URLField()
