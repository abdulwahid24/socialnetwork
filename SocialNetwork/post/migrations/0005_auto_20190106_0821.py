# Generated by Django 2.0.8 on 2019-01-06 08:21

from django.db import migrations
import django_hstore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20190106_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post',
            field=django_hstore.fields.DictionaryField(),
        ),
    ]