# Generated by Django 4.0.4 on 2022-05-11 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tecblicapp', '0038_alter_invoice_invoice_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoice_no',
            field=models.CharField(max_length=500, primary_key=True, serialize=False),
        ),
    ]
