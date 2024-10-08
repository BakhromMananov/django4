# Generated by Django 4.2.7 on 2024-08-17 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0004_school_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('user_name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('password_repeat', models.CharField(max_length=250)),
            ],
        ),
        migrations.AlterModelOptions(
            name='school',
            options={'ordering': ('id',), 'verbose_name': 'School', 'verbose_name_plural': 'Schools'},
        ),
    ]
