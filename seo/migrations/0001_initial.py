# Generated by Django 3.2.8 on 2021-10-12 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LatestNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='images/%Y/%m/%d')),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]
