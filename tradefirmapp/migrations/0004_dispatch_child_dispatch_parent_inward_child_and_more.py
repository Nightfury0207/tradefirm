# Generated by Django 5.0.3 on 2024-03-31 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradefirmapp', '0003_remove_order_client_order_client_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dispatch_Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dispatch_id', models.CharField(max_length=25)),
                ('dispatc_date', models.DateField()),
                ('item_id', models.CharField(max_length=25)),
                ('quantity', models.IntegerField(default=1)),
                ('remark', models.TextField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Dispatch_Parent',
            fields=[
                ('dispatch_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('order_id', models.CharField(max_length=25)),
                ('remark', models.TextField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Inward_Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inward_id', models.CharField(max_length=25)),
                ('item_id', models.CharField(max_length=25)),
                ('quantity', models.IntegerField(default=1)),
                ('remark', models.TextField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Inward_Parent',
            fields=[
                ('inward_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('inward_date', models.DateField()),
                ('remark', models.TextField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Order_Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=25)),
                ('item_id', models.CharField(max_length=25)),
                ('quantity', models.IntegerField(default=1)),
                ('remark', models.TextField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Order_Parent',
            fields=[
                ('order_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateField()),
                ('client_id', models.CharField(max_length=25)),
                ('ordered_via', models.CharField(max_length=50)),
                ('remark', models.TextField(blank=True, max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='unit',
            new_name='item_unit',
        ),
        migrations.RemoveField(
            model_name='client',
            name='gstn',
        ),
        migrations.RemoveField(
            model_name='client',
            name='name',
        ),
        migrations.RemoveField(
            model_name='item',
            name='name',
        ),
        migrations.RemoveField(
            model_name='item',
            name='opening_balance',
        ),
        migrations.AddField(
            model_name='client',
            name='client_gstn',
            field=models.CharField(default='xxxx', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='client_name',
            field=models.CharField(default='xxxx', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='remark',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='item',
            name='item_gst_percent',
            field=models.DecimalField(decimal_places=2, default='12', max_digits=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='item_hsn',
            field=models.CharField(default='xxxx', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='item_name',
            field=models.CharField(default='xxxxx', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='item_opening_balance',
            field=models.DecimalField(decimal_places=3, default=23, max_digits=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.TextField(max_length=254),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(max_length=13),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
