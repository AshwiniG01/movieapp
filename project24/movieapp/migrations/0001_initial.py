# Generated by Django 3.0.2 on 2020-09-04 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('hero_name', models.CharField(max_length=50)),
                ('heroin_name', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=50)),
            ],
        ),
    ]