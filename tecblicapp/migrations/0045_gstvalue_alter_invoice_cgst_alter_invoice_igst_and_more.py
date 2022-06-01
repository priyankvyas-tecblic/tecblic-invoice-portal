# Generated by Django 4.0.4 on 2022-05-25 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tecblicapp', '0044_invoice_igst'),
    ]

    operations = [
        migrations.CreateModel(
            name='gstValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cgst', models.CharField(blank=True, max_length=20, null=True)),
                ('sgst', models.CharField(blank=True, max_length=20, null=True)),
                ('igst', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='invoice',
            name='cgst',
            field=models.CharField(blank=True, default=0, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='igst',
            field=models.CharField(blank=True, default=0, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='sgst',
            field=models.CharField(blank=True, default=0, max_length=20, null=True),
        ),
    ]
