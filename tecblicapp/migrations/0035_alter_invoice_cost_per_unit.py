# Generated by Django 4.0.4 on 2022-05-07 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tecblicapp', '0034_alter_invoice_cost_per_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='cost_per_unit',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
    ]
