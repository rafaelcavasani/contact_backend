from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100, db_column='nome')
    age = models.IntegerField(db_column='idade', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'contato'


class Phone(models.Model):
    contact = models.ForeignKey(Contact,
                                on_delete=models.CASCADE,
                                db_column='idcontato')
    number = models.CharField(max_length=16, db_column='numero')

    class Meta:
        managed = True
        db_table = 'telefone'
