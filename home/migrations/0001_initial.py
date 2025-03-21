# Generated by Django 5.1.6 on 2025-02-16 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('foto', models.URLField()),
                ('precio', models.FloatField()),
                ('stock', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
