# Generated by Django 4.2.23 on 2025-06-20 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_rename_update_on_about_updated_on_alter_about_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollaborateRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('read', models.BooleanField(default=False)),
            ],
        ),
    ]
