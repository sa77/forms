# Generated by Django 3.0.6 on 2020-05-07 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255)),
                ('location', models.CharField(blank=True, choices=[('North America', 'North America'), ('Asia', 'Asia'), ('South America', 'South America'), ('Africa', 'Africa'), ('Australia', 'Australia')], default='', max_length=255)),
                ('address_line_one', models.CharField(blank=True, default='', max_length=255)),
                ('address_line_two', models.CharField(blank=True, default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255)),
                ('age', models.PositiveSmallIntegerField(null=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='', max_length=255)),
                ('business', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Business')),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255)),
                ('relation', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(blank=True, default='', max_length=255)),
                ('profile_verified', models.BooleanField(default=False)),
                ('phone_verified', models.BooleanField(default=False)),
                ('reviewed_at', models.DateField()),
                ('profile', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review', to='core.Profile')),
            ],
        ),
    ]
