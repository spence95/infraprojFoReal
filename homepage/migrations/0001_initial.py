# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('UID', models.CharField(unique=True, max_length=256)),
                ('organizationalTag', models.CharField(max_length=256)),
                ('manufacturerPartNumber', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=256, blank=True)),
                ('maintenanceNotes', models.CharField(max_length=256, blank=True)),
                ('dateImplemented', models.DateField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('UID', models.CharField(unique=True, max_length=256)),
                ('name', models.CharField(max_length=256)),
                ('address', models.CharField(max_length=256)),
                ('phone', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('UID', models.CharField(unique=True, max_length=256)),
                ('name', models.CharField(max_length=256)),
                ('address', models.CharField(max_length=256)),
                ('phone', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='asset',
            name='currentAssignedLocation',
            field=models.ForeignKey(to='homepage.Location'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='asset',
            name='manufacturer',
            field=models.ForeignKey(to='homepage.Manufacturer'),
            preserve_default=True,
        ),
    ]
