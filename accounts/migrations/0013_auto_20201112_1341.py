# Generated by Django 3.1.3 on 2020-11-12 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_contractor_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractor',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contractor',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contractor',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
