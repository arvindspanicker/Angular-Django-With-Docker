# Generated by Django 2.1.7 on 2019-03-14 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]