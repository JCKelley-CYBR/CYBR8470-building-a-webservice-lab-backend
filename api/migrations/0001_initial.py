# Generated by Django 4.1.3 on 2022-11-14 23:22

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Australian Shepherd', max_length=25)),
                ('size', models.CharField(choices=[('TINY', 'Tiny'), ('SMALL', 'Small'), ('MEDIUM', 'Medium'), ('LARGE', 'Large')], default='Medium', max_length=6)),
                ('friendliness', models.IntegerField(default=5, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('trainability', models.IntegerField(default=5, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('sheddingamount', models.IntegerField(default=5, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('exerciseneeds', models.IntegerField(default=5, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Reese', max_length=25)),
                ('age', models.IntegerField(default=1)),
                ('gender', models.CharField(default='Female', max_length=6)),
                ('color', models.CharField(default='Red Merle', max_length=25)),
                ('favoritefood', models.CharField(default='Twizzlers', max_length=25)),
                ('favoritetoy', models.CharField(default='Frisbee', max_length=25)),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.breed')),
            ],
        ),
    ]
