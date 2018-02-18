# Generated by Django 2.0.1 on 2018-02-17 20:13

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modifier', models.IntegerField(default=1)),
                ('name', models.CharField(default='', max_length=50)),
                ('docfile', models.FileField(null=True, upload_to='documents')),
                ('creator', models.IntegerField(default=1)),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
                ('filehash', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=500)),
                ('document', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.Document')),
                ('hasRead', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modifier', models.IntegerField(default=1)),
                ('name', models.CharField(max_length=100)),
                ('creator', models.IntegerField(default=1)),
                ('isLeader', models.ManyToManyField(related_name='isLeader', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(related_name='members', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GroupComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=500)),
                ('group', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.Group')),
                ('hasRead', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=100)),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.Group'),
        ),
    ]
