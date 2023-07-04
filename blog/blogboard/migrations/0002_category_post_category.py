# Generated by Django 4.2.2 on 2023-06-09 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='No Category', max_length=255),
        ),
    ]
