# Generated by Django 5.1.1 on 2024-09-24 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=100)),
                ('descriere', models.TextField()),
                ('imagine', models.ImageField(upload_to='produse/')),
            ],
        ),
    ]
