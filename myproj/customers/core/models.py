from django.db import models

class Profession(models.Model):
    description = models.CharField(max_length=50)

class DataSheet(models.Model):
    description = models.CharField(max_length=50)
    historical_data = models.TextField()

    def __str__(self):
        return self.description

class Customers(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    profession = models.ManyToManyField(Profession)
    data_sheet = models.OneToOneField(DataSheet, on_delete = models.CASCADE )

    def __str__(self):
        return self.name

class Document(models.Model):
    PP = "PP"
    ID =  "ID"
    OT = "OT"

    DOC_TYPE = (
        (PP, "Passport"),
        (ID, "Identity Care"),
        (OT, "Others")
    )

    dtype = models.CharField(max_length=50)
    doc_number = models.CharField(max_length=50)
    customer = models.ForeignKey(Customers, on_delete = models.CASCADE)

    def __str__(self):
        return self.doc_number
