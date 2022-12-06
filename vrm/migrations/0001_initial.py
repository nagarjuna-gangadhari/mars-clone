# Generated by Django 4.1.3 on 2022-12-01 10:06

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utils', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Center',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('state', models.CharField(blank=True, max_length=128, null=True)),
                ('district', models.CharField(blank=True, max_length=128, null=True)),
                ('village', models.CharField(blank=True, max_length=128, null=True)),
                ('language', models.CharField(blank=True, choices=[('Bengali', 'Bengali'), ('Gujarathi', 'Gujarathi'), ('Hindi', 'Hindi'), ('Kannada', 'Kannada'), ('Malayalam', 'Malayalam'), ('Marathi', 'Marathi'), ('Oriya', 'Oriya'), ('Punjabi', 'Punjabi'), ('Tamil', 'Tamil'), ('Telugu', 'Telugu'), ('Urdu', 'Urdu')], max_length=128, null=True)),
                ('board', models.CharField(blank=True, choices=[('APSB', 'APSB'), ('TNSB', 'TNSB'), ('DSERT', 'DSERT'), ('NCERT', 'NCERT'), ('MHSB', 'MHSB'), ('WBSED', 'WBSED'), ('SCERT', 'SCERT'), ('OPEPA', 'OPEPA'), ('UPMSP ', 'UPMSP '), ('JACB', 'JACB'), ('eVidyaloka ', 'eVidyaloka '), ('BSEB', 'BSEB'), ('UBSE', 'UBSE'), ('GSEB', 'GSEB'), ('JKBOSE', 'JKBOSE'), ('CBSE', 'CBSE')], max_length=128, null=True)),
                ('working_days', models.TextField(blank=True, null=True)),
                ('working_slots', models.TextField(blank=True, null=True)),
                ('photo', models.FileField(blank=True, null=True, upload_to='static/uploads/images/center')),
                ('description', models.TextField(blank=True, max_length=2048, null=True)),
                ('class_location', models.CharField(blank=True, max_length=256, null=True)),
                ('grades', models.CharField(blank=True, max_length=128, null=True)),
                ('students_count', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('Planned', 'Planned'), ('Active', 'Active'), ('Inactive', 'Inactive'), ('Closed', 'Closed'), ('Provisional', 'Provisional')], default='Planned', max_length=256)),
                ('launch_date', models.DateTimeField(auto_now=True, null=True)),
                ('skype_id', models.CharField(blank=True, max_length=256, null=True)),
                ('location_map', models.CharField(blank=True, max_length=1024, null=True)),
                ('program_type', models.IntegerField(blank=True, choices=[(1, 'Digital Classroom'), (2, 'Digital School'), (3, 'Sampoorna')], default=1, null=True)),
                ('is_test', models.BooleanField(default=False)),
                ('admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='center_admin', to=settings.AUTH_USER_MODEL)),
                ('assistant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='center_assistant', to=settings.AUTH_USER_MODEL)),
                ('delivery_coordinator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='center_delivery_coordinator', to=settings.AUTH_USER_MODEL)),
                ('field_coordinator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='center_field_coordinator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('block', models.CharField(blank=True, max_length=256, null=True)),
                ('cluster', models.CharField(blank=True, max_length=256, null=True)),
                ('village', models.CharField(blank=True, max_length=256, null=True)),
                ('region', models.IntegerField(choices=[(1, 'Rural'), (2, 'Urban')], default=1)),
                ('pincode', models.IntegerField(blank=True, null=True)),
                ('contact_details', models.CharField(blank=True, max_length=512, null=True)),
                ('location_map', models.CharField(blank=True, max_length=1024, null=True)),
                ('languages', models.CharField(blank=True, max_length=100, null=True)),
                ('started_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('beo_name', models.CharField(blank=True, max_length=256, null=True)),
                ('school_number', models.CharField(blank=True, max_length=128, null=True)),
                ('school_code', models.BigIntegerField(db_index=True, default=0)),
                ('photo', models.FileField(blank=True, null=True, upload_to='static/uploads/images/center')),
                ('min_grade', models.IntegerField(default=10, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)])),
                ('total_children', models.IntegerField(blank=True, null=True)),
                ('management_type', models.IntegerField(choices=[(1, 'State'), (2, 'Central'), (3, 'Private')], default=1)),
                ('school_type', models.IntegerField(choices=[(1, 'Co-Educational'), (2, 'Boys Only'), (3, 'Girls Only')], default=1)),
                ('total_teachers', models.IntegerField(blank=True, null=True)),
                ('teachers_male', models.IntegerField(blank=True, null=True)),
                ('teachers_female', models.IntegerField(blank=True, null=True)),
                ('principal', models.CharField(blank=True, max_length=128, null=True)),
                ('building_status', models.IntegerField(choices=[(1, 'Unknown'), (2, 'Poor'), (3, 'Good')], default=1)),
                ('furniture', models.IntegerField(choices=[(1, 'Have None'), (2, 'Require More'), (3, 'Poor'), (4, 'Good')], default=1)),
                ('library', models.BooleanField(default=False)),
                ('extra_rooms', models.IntegerField(default=0)),
                ('electricity', models.BooleanField(default=False)),
                ('internet', models.BooleanField(default=False)),
                ('playground', models.BooleanField(default=False)),
                ('books_in_library', models.IntegerField(default=0)),
                ('computers_available', models.IntegerField(default=0)),
                ('academic_year', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='utils.ay')),
                ('refer_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateTimeField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=1024, null=True)),
                ('ay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utils.ay')),
                ('center', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vrm.center')),
            ],
        ),
        migrations.AddField(
            model_name='center',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='vrm.school'),
        ),
    ]
