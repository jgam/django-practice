# Generated by Django 3.0.3 on 2020-02-09 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0005_wheels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wheels',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wheels', to='demo.Car'),
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surnawme', models.CharField(max_length=30)),
                ('cars', models.ManyToManyField(to='demo.Car')),
            ],
        ),
    ]