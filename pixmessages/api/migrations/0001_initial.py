# Generated by Django 5.0.3 on 2024-03-20 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interaction',
            fields=[
                ('id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('ispb', models.CharField(max_length=8)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_used', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('cpfCnpj', models.CharField(max_length=14)),
                ('ispb', models.CharField(max_length=8)),
                ('agencia', models.CharField(max_length=10)),
                ('contaTransacional', models.CharField(max_length=20)),
                ('tipoConta', models.CharField(max_length=4)),
            ],
        ),
    ]
