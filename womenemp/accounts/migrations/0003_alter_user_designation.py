# Generated by Django 4.1.7 on 2023-02-24 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_phone_alter_user_designation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='designation',
            field=models.CharField(choices=[('W', 'Women')], default='W', max_length=1),
        ),
    ]
