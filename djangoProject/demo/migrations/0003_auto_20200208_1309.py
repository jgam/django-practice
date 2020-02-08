# Generated by Django 3.0.3 on 2020-02-08 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20200208_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='covers/'),
        ),
        migrations.AddField(
            model_name='car',
            name='description',
            field=models.TextField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
        migrations.AddField(
            model_name='car',
            name='published',
            field=models.DateField(null=True),
        ),
    ]
