# Generated by Django 4.0.4 on 2022-05-11 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tecblicapp', '0039_alter_invoice_invoice_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoice_no',
            field=models.CharField(default=500, max_length=500, primary_key=True, serialize=False),
        ),
    ]
