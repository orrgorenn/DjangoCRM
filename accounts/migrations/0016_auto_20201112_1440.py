# Generated by Django 3.1.3 on 2020-11-12 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20201112_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractor',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
