# Generated by Django 2.2.16 on 2020-09-11 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200911_0626'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]