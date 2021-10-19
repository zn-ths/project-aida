# Generated by Django 3.2.8 on 2021-10-19 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BloodPressure',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField(editable=False)),
                ('measured_at', models.DateTimeField(help_text='Enter the date and time the measurement took place')),
                ('systolic', models.PositiveSmallIntegerField()),
                ('diastolic', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name_plural': 'Blood pressure metrics',
            },
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField(editable=False)),
                ('type', models.CharField(choices=[('c', 'Cardio'), ('w', 'Weight'), ('u', 'Undefined')], help_text='Select the type of the exercise', max_length=25)),
                ('name', models.CharField(help_text='The name of the exercise', max_length=255)),
                ('vest_weight', models.FloatField(default=0, help_text='Additional weight with a vest')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HeartRate',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField(editable=False)),
                ('measured_at', models.DateTimeField(help_text='Enter the date and time the measurement took place')),
                ('pulse', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name_plural': 'Pulse metrics',
            },
        ),
        migrations.CreateModel(
            name='Sleep',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField(editable=False)),
                ('slept_at', models.DateTimeField(help_text='Enter the date and time you went to sleep')),
                ('awoke_at', models.DateTimeField(help_text='Enter the date and time you woke up at')),
                ('duration', models.PositiveIntegerField(default=0, help_text='Duration of sleep')),
            ],
            options={
                'verbose_name_plural': 'Sleep metrics',
                'ordering': ['-slept_at'],
            },
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField(editable=False)),
                ('engaged_at', models.DateTimeField(help_text='Enter the date and time that you engaged in the activity')),
                ('type', models.CharField(choices=[('c', 'Cardio Workout'), ('w', 'Weight Workout')], help_text='Select the type of workout', max_length=255)),
            ],
            options={
                'ordering': ('-engaged_at',),
            },
        ),
        migrations.CreateModel(
            name='WeightSet',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField(editable=False)),
                ('reps', models.PositiveSmallIntegerField(default=0, help_text='Enter the amount of repetitions performed in the set')),
                ('weight', models.PositiveSmallIntegerField(default=0, help_text='Enter the weight the set was performed with')),
                ('weight_unit', models.CharField(blank=True, choices=[('g', 'Grams'), ('k', 'Kilograms'), ('l', 'Pounds')], default='k', help_text='Enter the weight unit of the set', max_length=10, null=True)),
                ('exercise', models.ForeignKey(help_text='The exercise the set belongs to', on_delete=django.db.models.deletion.CASCADE, to='aida.exercise')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='exercise',
            name='workout',
            field=models.ForeignKey(help_text='The workout the exercise belongs to', on_delete=django.db.models.deletion.CASCADE, to='aida.workout'),
        ),
        migrations.CreateModel(
            name='CardioSet',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField(editable=False)),
                ('speed', models.PositiveSmallIntegerField(default=0, help_text='Enter the speed the set was performed in (km/h)')),
                ('duration', models.PositiveSmallIntegerField(default=0, help_text='Enter the duration of the set')),
                ('time_unit', models.CharField(blank=True, choices=[('s', 'Seconds'), ('m', 'Minutes'), ('h', 'Hours')], default='m', help_text='Enter the time unit of the set', max_length=10, null=True)),
                ('exercise', models.ForeignKey(help_text='The exercise the set belongs to', on_delete=django.db.models.deletion.CASCADE, to='aida.exercise')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]