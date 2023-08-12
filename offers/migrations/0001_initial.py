# Generated by Django 4.2.4 on 2023-08-12 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_cake', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('pricing', models.DecimalField(decimal_places=2, max_digits=15)),
                ('image', models.ImageField(blank=True, null=True, upload_to='offers/')),
            ],
        ),
    ]
