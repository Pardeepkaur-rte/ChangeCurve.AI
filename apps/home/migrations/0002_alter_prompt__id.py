# Generated by Django 3.2.6 on 2024-11-12 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prompt',
            name='_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
