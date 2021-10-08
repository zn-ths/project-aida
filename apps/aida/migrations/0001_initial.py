# Generated by Django 3.2.8 on 2021-10-08 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=25, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('vest_weight', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sets', to='aida.exercise')),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('trained', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CardioSet',
            fields=[
                ('set_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aida.set')),
                ('speed', models.PositiveSmallIntegerField(default=0)),
                ('duration', models.PositiveSmallIntegerField(default=0)),
            ],
            bases=('aida.set',),
        ),
        migrations.CreateModel(
            name='WeightSet',
            fields=[
                ('set_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aida.set')),
                ('weight', models.PositiveSmallIntegerField(default=0)),
                ('reps', models.PositiveSmallIntegerField(default=0)),
            ],
            bases=('aida.set',),
        ),
        migrations.AddField(
            model_name='exercise',
            name='training',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aida.workout'),
        ),
    ]
