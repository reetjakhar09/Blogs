# Generated by Django 2.2.16 on 2020-09-18 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_auto_20200918_0512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='post',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
    ]
