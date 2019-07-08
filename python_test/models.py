from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)

    street_name = models.CharField(max_length=255, blank=True)
    suburb = models.CharField(max_length=255, blank=True)
    postcode = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)

    contact_name = models.CharField(max_length=255, blank=True)

    @property
    def address(self):
        return ', '.join(filter(lambda elem: bool(elem), (
            self.street_name,
            self.suburb,
            self.postcode,
            self.state,
        )))
