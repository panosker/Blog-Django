# Generated by Django 4.2.2 on 2023-06-14 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogboard', '0006_alter_post_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]