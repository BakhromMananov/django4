# Generated by Django 4.2.7 on 2024-08-18 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0005_siteuser_alter_school_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='siteuser',
            old_name='user_name',
            new_name='username',
        ),
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
