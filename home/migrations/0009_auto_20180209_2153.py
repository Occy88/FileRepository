# Generated by Django 2.0.1 on 2018-02-09 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20180209_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(null=True, upload_to='documents'),
        ),
    ]
