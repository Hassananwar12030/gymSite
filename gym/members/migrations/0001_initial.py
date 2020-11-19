# Generated by Django 3.1 on 2020-11-19 09:49

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='exercise',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('exercise_name', models.CharField(default='', max_length=124)),
            ],
        ),
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male', max_length=124)),
                ('type_person', models.CharField(choices=[('Memeber', 'Member'), ('Trainer', 'Trainer')], default='Member', max_length=124)),
                ('fullname', models.CharField(default='', max_length=124)),
                ('description', models.TextField(default='', null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='service_type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('service_name', models.CharField(default='', max_length=124)),
            ],
        ),
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_online', models.BooleanField(default=False, null=True)),
                ('is_oneToOne', models.BooleanField(default=False, null=True)),
                ('startdate', models.DateTimeField(auto_now_add=True)),
                ('days', models.CharField(choices=[('Weekdays', 'Regular Weekdays'), ('Alternate Days', 'Alternate Days on Weekdays'), ('Weekends', 'Weekends')], default='Weekdays', max_length=124, null=True)),
                ('timings', models.CharField(choices=[('8am', '8am'), ('5pm', '5pm'), ('8pm', '8pm')], default='5pm', max_length=124, null=True)),
                ('duration', models.IntegerField(default=0, null=True)),
                ('class_link', models.URLField(null=True)),
                ('charges', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1)])),
                ('excercise_field', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='members.exercise')),
                ('service_provider_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.person')),
                ('type_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.service_type')),
            ],
        ),
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('time_of_booking', models.DateTimeField(auto_now_add=True)),
                ('person_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.person')),
                ('service_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.service')),
            ],
        ),
    ]
