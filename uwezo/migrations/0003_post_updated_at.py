# Generated by Django 4.2.16 on 2024-10-05 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uwezo', '0002_incidentreport'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
