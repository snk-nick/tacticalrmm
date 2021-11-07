# Generated by Django 3.2.6 on 2021-10-22 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_auto_20211010_0249'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='can_list_alerttemplates',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='role',
            name='can_manage_alerttemplates',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='role',
            name='can_run_urlactions',
            field=models.BooleanField(default=False),
        ),
    ]