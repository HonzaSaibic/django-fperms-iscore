# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-13 15:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='IsCorePerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codename', models.CharField(max_length=100, verbose_name='codename')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='name')),
                ('object_id', models.SmallIntegerField(blank=True, null=True, verbose_name='object pk')),
                ('field_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='field name')),
                ('type', models.CharField(choices=[('generic', 'resource')], default='generic', max_length=10)),
                ('core', models.CharField(max_length=100, verbose_name='core')),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='content type')),
            ],
            options={
                'verbose_name': 'permission',
                'abstract': False,
                'verbose_name_plural': 'permissions',
                'ordering': ('content_type', 'object_id', 'field_name', 'codename'),
            },
        ),
        migrations.AlterUniqueTogether(
            name='iscoreperm',
            unique_together=set([('type', 'codename', 'content_type', 'object_id', 'field_name', 'core')]),
        ),
    ]
