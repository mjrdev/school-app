# Generated by Django 4.1.4 on 2022-12-31 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapi', '0004_alter_registration_course_alter_registration_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='shift',
            field=models.CharField(choices=[('noturno', 'noturno'), ('matutino', 'matutino'), ('vespertino', 'vespertino'), ('integral', 'integral'), ('EAD', 'EAD')], max_length=15),
        ),
    ]
