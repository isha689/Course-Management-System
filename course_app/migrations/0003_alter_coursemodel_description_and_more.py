# Generated by Django 4.1.7 on 2023-03-25 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0002_coursemodel_hours_alter_coursemodel_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemodel',
            name='description',
            field=models.TextField(blank=True, default='This is the descritpion of the Course', null=True),
        ),
        migrations.AlterField(
            model_name='coursemodel',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
