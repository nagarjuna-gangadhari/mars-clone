# Generated by Django 4.1.3 on 2022-12-01 10:06

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
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('code', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_id', models.IntegerField(blank=True, null=True)),
                ('country_code', models.CharField(blank=True, max_length=20, null=True)),
                ('country_name', models.CharField(blank=True, max_length=128, null=True)),
                ('state_name', models.CharField(blank=True, max_length=128, null=True)),
                ('city_name', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(max_length=512)),
                ('board', models.CharField(blank=True, choices=[('APSB', 'APSB'), ('TNSB', 'TNSB'), ('DSERT', 'DSERT'), ('NCERT', 'NCERT'), ('MHSB', 'MHSB'), ('WBSED', 'WBSED'), ('SCERT', 'SCERT'), ('OPEPA', 'OPEPA'), ('UPMSP ', 'UPMSP '), ('JACB', 'JACB'), ('eVidyaloka ', 'eVidyaloka '), ('BSEB', 'BSEB'), ('UBSE', 'UBSE'), ('GSEB', 'GSEB'), ('JKBOSE', 'JKBOSE'), ('CBSE', 'CBSE')], max_length=128, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('is_current', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
