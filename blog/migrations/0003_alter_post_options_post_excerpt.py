# Generated by Django 4.2.2 on 2023-06-07 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_publish_date_post_publish'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-publish',)},
        ),
        migrations.AddField(
            model_name='post',
            name='excerpt',
            field=models.TextField(null=True),
        ),
    ]