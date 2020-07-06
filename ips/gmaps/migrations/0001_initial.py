# Generated by Django 2.2.13 on 2020-07-01 18:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_comisaria', models.CharField(max_length=200)),
                ('lat', models.CharField(max_length=50)),
                ('lng', models.CharField(max_length=50)),
                ('nombredd', models.CharField(max_length=50)),
                ('nombrepp', models.CharField(max_length=50)),
                ('nombredi', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
