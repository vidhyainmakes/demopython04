# Generated by Django 4.1.6 on 2023-05-04 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_userbankaccount_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbankaccount',
            name='account_type',
            field=models.ForeignKey(blank=True, default='1000000008', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='accounts.bankaccounttype'),
        ),
    ]