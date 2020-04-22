# Generated by Django 3.0.4 on 2020-03-24 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=7)),
                ('receipt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receipts.Receipt')),
            ],
        ),
    ]