# Generated by Django 4.1.5 on 2023-01-11 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tecblicapp', '0063_alter_invoice_payment_method_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='cost_per_unit1',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='cost_per_unit2',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='cost_per_unit3',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='description1',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='description2',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='description3',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='quantity1',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='quantity2',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='quantity3',
        ),
    ]