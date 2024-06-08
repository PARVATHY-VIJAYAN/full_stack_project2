# Generated by Django 3.2.8 on 2021-12-22 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendorPortal', '0004_alter_vendor_customers_delivering'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='Maximum_Deliveries',
        ),
        migrations.AddField(
            model_name='vendor',
            name='Total_Customers',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='Customers_Delivering',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]