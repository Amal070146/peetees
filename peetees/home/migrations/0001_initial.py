# Generated by Django 3.2.3 on 2021-12-31 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_name', models.CharField(max_length=50)),
                ('mrp', models.IntegerField()),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('our_price', models.IntegerField()),
            ],
        ),
    ]
