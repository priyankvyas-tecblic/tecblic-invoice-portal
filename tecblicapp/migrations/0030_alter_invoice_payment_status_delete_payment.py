# Generated by Django 4.0.4 on 2022-05-06 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tecblicapp', '0029_alter_payment_ps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='payment_status',
            field=models.CharField(choices=[('PENDING', 'PENDING'), ('PAID', 'PAID')], default='PENDING', max_length=100),
        ),
        migrations.DeleteModel(
            name='payment',
        ),
    ]
