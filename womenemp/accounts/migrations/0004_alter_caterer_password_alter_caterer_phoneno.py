# Generated by Django 4.1.3 on 2023-02-24 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_caterer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caterer',
            name='password',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='caterer',
            name='phoneno',
            field=models.CharField(max_length=10),
        ),
    ]
