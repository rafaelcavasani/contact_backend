# Generated by Django 3.0.8 on 2020-07-30 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='nome', max_length=100)),
                ('age', models.IntegerField(blank=True, db_column='idade', null=True)),
            ],
            options={
                'db_table': 'contato',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(db_column='numero', max_length=16)),
                ('contact', models.ForeignKey(db_column='idcontato', on_delete=django.db.models.deletion.CASCADE, to='contact.Contact')),
            ],
            options={
                'db_table': 'telefone',
                'managed': True,
            },
        ),
    ]
