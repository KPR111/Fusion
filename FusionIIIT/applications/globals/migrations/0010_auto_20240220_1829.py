# Generated by Django 3.1.5 on 2024-02-20 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globals', '0009_auto_20240219_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='user_status',
            field=models.CharField(choices=[('NEW', 'NEW'), ('PRESENT', 'PRESENT')], default='PRESENT', max_length=50),
        ),
    ]
