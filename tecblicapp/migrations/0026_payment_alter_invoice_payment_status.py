# Generated by Django 4.0.4 on 2022-05-06 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tecblicapp', '0025_alter_invoice_payment_status_delete_paymentdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ps', models.CharField(blank=True, choices=[('PENDING', 'PENDING'), ('PAID', 'PAID')], max_length=10, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='invoice',
            name='payment_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tecblicapp.payment'),
        ),
    ]
