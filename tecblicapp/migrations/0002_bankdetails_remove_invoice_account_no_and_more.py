# Generated by Django 4.0.4 on 2022-04-29 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tecblicapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(blank=True, max_length=40, null=True)),
                ('account_no', models.CharField(blank=True, max_length=30, null=True)),
                ('ifsc_code', models.CharField(blank=True, max_length=20, null=True)),
                ('bank_branch', models.CharField(blank=True, max_length=40, null=True)),
                ('swift_code', models.CharField(blank=True, max_length=15, null=True)),
                ('cin', models.CharField(blank=True, max_length=20, null=True)),
                ('supplier_pan', models.CharField(blank=True, max_length=20, null=True)),
                ('supplier_gstin', models.CharField(blank=True, max_length=30, null=True)),
                ('arn', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='account_no',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='arn',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='bank_branch',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='bank_name',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='cin',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='ifsc_code',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='supplier_gstin',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='supplier_pan',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='swift_code',
        ),
        migrations.CreateModel(
            name='bank_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_information', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tecblicapp.bankdetails')),
            ],
        ),
    ]
