# Generated by Django 2.0.8 on 2019-01-06 08:21

from django.db import migrations
import django_hstore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20190105_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='data',
            field=django_hstore.fields.DictionaryField(null=True),
        ),
    ]
