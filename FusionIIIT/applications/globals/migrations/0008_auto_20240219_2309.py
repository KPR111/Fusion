# Generated by Django 3.1.5 on 2024-02-19 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globals', '0007_auto_20240218_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='user_status',
            field=models.CharField(choices=[('NEW', 'NEW'), ('PRESENT', 'PRESENT')], default='PRESENT', max_length=50),
        ),
    ]
