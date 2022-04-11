# Generated by Django 4.0.3 on 2022-04-11 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getservice', '0002_alter_quote_mobile_alter_quote_qty_bathroom_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='qty_bathroom',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=2),
        ),
        migrations.AlterField(
            model_name='quote',
            name='qty_bedroom',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=2),
        ),
        migrations.AlterField(
            model_name='quote',
            name='qty_living',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=2),
        ),
        migrations.AlterField(
            model_name='quote',
            name='qty_window',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=2),
        ),
    ]
