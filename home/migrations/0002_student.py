# Generated by Django 4.0.6 on 2022-09-07 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=150, null=True)),
                ('username', models.CharField(max_length=150, null=True)),
                ('password1', models.CharField(max_length=150, null=True)),
                ('password2', models.CharField(max_length=150, null=True)),
            ],
        ),
    ]
