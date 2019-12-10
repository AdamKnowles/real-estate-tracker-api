from django.db import models
from datetime import date



class Property(models.Model):
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    year_built = models.IntegerField()
    price = models.IntegerField()
    square_feet = models.IntegerField()
    bedroom_count = models.IntegerField()
    bathroom_count = models.IntegerField()
    has_basement = models.BooleanField()
    date_listed = models.DateField()

    class Meta:
        verbose_name = ("property")
        verbose_name_plural = ("properties")

    def days_listed(self):

        current_property = Property.objects.get(pk=self.pk)

        today = str(date.today())

        current_date = today.split("-")

        current_year = int(current_date[0])
        current_month = int(current_date[1])
        current_day = int(current_date[2])

        list_date = str(current_property.date_listed)
        new_list_date = list_date.split("-")

        listed_year = int(new_list_date[0])
        listed_month = int(new_list_date[1])
        listed_day = int(new_list_date[2])

        todays_date = date(listed_year, listed_month, listed_day)
        date_in_database = date(current_year, current_month, current_day)
        
        total_days = date_in_database - todays_date
        
        return total_days.days

    def price_per_square_foot(self):

        price = Property.objects.get(pk=self.pk)

        price_per_square_foot = price.price / price.square_feet

        return price_per_square_foot












