# Generated by Django 4.0.4 on 2022-05-07 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tecblicapp', '0031_delete_gst_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='send_email',
            field=models.CharField(choices=[('only_generate', 'Only Generate'), ('generate_and_send', 'Generate And Send Mail')], default='only_generate', max_length=20),
        ),
    ]
