# Generated by Django 5.0.3 on 2024-04-24 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_maqola_author_alter_maqola_tag_delete_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='maqola',
            name='image',
            field=models.ImageField(default=-1, upload_to=''),
            preserve_default=False,
        ),
    ]