# Generated by Django 4.1.4 on 2022-12-28 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapi', '0004_remove_course_workload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(default='12345678', max_length=35),
        ),
    ]