# Generated by Django 3.1.3 on 2020-11-08 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('digikala', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DigiKalaProducts',
            new_name='DigiKalaProduct',
        ),
        migrations.CreateModel(
            name='ChangeLogProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_price', models.BigIntegerField()),
                ('new_price', models.BigIntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digikala.digikalaproduct')),
            ],
        ),
    ]
