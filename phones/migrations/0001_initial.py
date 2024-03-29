# Generated by Django 3.2.9 on 2021-12-14 11:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('release_date', models.DateField(default=django.utils.timezone.now)),
                ('lte_exists', models.BooleanField(null=True)),
                ('slug', models.SlugField(null=True)),
            ],
        ),
    ]
