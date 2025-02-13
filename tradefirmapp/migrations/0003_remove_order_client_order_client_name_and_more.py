# Generated by Django 5.0.3 on 2024-03-31 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradefirmapp', '0002_remove_client_gst_client_gstn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='client',
        ),
        migrations.AddField(
            model_name='order',
            name='client_name',
            field=models.CharField(default='test', max_length=100, verbose_name='Client Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='item_name',
            field=models.CharField(default='test', max_length=100, verbose_name='Item Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='ordered_via',
            field=models.CharField(default='test', max_length=100, verbose_name='Ordered Via'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(verbose_name='Order Date'),
        ),
    ]
