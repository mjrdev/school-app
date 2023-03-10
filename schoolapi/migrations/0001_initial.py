# Generated by Django 4.1.4 on 2022-12-30 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('email', models.EmailField(max_length=254)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('password', models.CharField(default='12345678', max_length=35)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('email', models.EmailField(max_length=254)),
                ('cpf', models.CharField(max_length=11)),
                ('password', models.CharField(default='12345678', max_length=35)),
                ('about', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=7)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registration_student', to='schoolapi.student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registration_teacher', to='schoolapi.student')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift', models.CharField(choices=[('noturno', 'noturno'), ('matutino', 'matutino'), ('vespertino', 'vespertino'), ('integral', 'integral')], max_length=15)),
                ('title', models.CharField(max_length=90)),
                ('description', models.TextField()),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_op', to='schoolapi.teacher')),
            ],
        ),
    ]
