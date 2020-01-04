from django.db import models
from django.utils import timezone
import datetime
from datetime import datetime
from django.contrib.auth.models import User
import pytz


# Create your models here.
class Contract(models.Model):
    contract_title = models.TextField(max_length=250)
    contract_details = models.TextField()
    contract_price = models.IntegerField()
    contract_date = models.DateTimeField(auto_now_add=True)
    contract_deadline = models.DateTimeField()
    contract_creator = models.ForeignKey(User, on_delete=models.CASCADE)
    contract_image1 = models.ImageField(upload_to='contract_image' , blank=True)
    contract_image2 = models.ImageField(upload_to='contract_image' , blank=True)
    contract_doc = models.FileField(upload_to='documents', blank=True)
    contract_paymentVerification = models.ImageField(upload_to='payment' , blank=True)
    approved_contract = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = "entries"

    @property
    def compdate(self):
        return pytz.utc.localize(datetime.today()) > self.contract_deadline



class Comment(models.Model):
    contract = models.ForeignKey('entries.Contract', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text



