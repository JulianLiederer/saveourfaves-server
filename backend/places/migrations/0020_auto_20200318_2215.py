# Generated by Django 3.0.4 on 2020-03-18 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0019_neighborhood_bounds'),
    ]

    operations = [
        migrations.RenameField(
            model_name='area',
            old_name='name',
            new_name='key',
        ),
        migrations.AddField(
            model_name='area',
            name='display_name',
            field=models.TextField(default='moop'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='neighborhood',
            name='area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='places.Area'),
        ),
    ]
