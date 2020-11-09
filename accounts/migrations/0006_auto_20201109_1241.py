# Generated by Django 3.1.3 on 2020-11-09 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20201109_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='date_closed',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='date_last_update',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='category',
            field=models.CharField(choices=[('1', 'איטום'), ('2', 'אינסטלציה'), ('3', 'אקוסטיקה'), ('4', 'ביטחון'), ('5', 'בטיחות - אש'), ('6', 'בטיחות - אתר'), ('7', 'בינוי'), ('8', 'חשמל'), ('9', 'מיזוג אוויר'), ('10', 'נגישות'), ('11', 'ניקיון'), ('12', 'תאורה'), ('13', 'תקשורת')], default='1', max_length=2),
        ),
    ]