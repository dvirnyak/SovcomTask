# Generated by Django 4.2.7 on 2023-11-10 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_rename_coordinate_x_office_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='grade',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
