# Generated by Django 4.0.4 on 2022-06-16 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0008_subjectstatus_enrollment_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
