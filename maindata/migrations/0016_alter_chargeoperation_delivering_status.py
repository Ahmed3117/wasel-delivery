# Generated by Django 4.2.4 on 2024-02-03 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maindata', '0015_remove_chargeoperation_delivering_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chargeoperation',
            name='delivering_status',
            field=models.CharField(blank=True, choices=[('1', 'انتظار'), ('2', 'خروج'), ('3', 'تم'), ('4', 'مرتجع')], default='1', max_length=10, null=True, verbose_name=' موقف التوصيل'),
        ),
    ]
