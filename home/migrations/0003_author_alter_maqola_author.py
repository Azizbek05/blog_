# Generated by Django 5.0.3 on 2024-04-15 07:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_maqola_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=133)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='maqola',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.author'),
        ),
    ]
