# Generated by Django 2.1 on 2018-11-16 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('duplicate', '0007_auto_20181116_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='employee',
            field=models.ManyToManyField(blank=True, null=True, to='duplicate.Employee'),
        ),
    ]
