# Generated by Django 3.1.3 on 2020-11-12 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20201112_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractor',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]