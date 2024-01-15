from django.db import models
from django.utils.timezone import now


# Create your models here.
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30)
    description = models.CharField(max_length=500)

    def __str__(self):
        return "Name: " + self.name + "," + \
            "Description: " + self.description

class CarModel(models.Model):
    make = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=30)
    id = models.IntegerField(primary_key=True)

    SEDAN = "Sedan"
    SUV = "SUV"
    WAGON = "Wagon"
    CAR_CHOICES = [
        (SEDAN, "Sedan"),
        (SUV, "SUV"),
        (WAGON, "Wagon"),
    ]
    model_type = models.CharField(
        null=False, max_length=5, choices=CAR_CHOICES, default=SEDAN)
    
    year = models.DateField(default=now)

    def __str__(self):
        return "Name: " + self.name + ", " \
                "Type: " + self.model_type + ", " + \
                "Year: " + str(self.year.year)

# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
