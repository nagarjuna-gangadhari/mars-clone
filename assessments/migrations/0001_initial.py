# Generated by Django 4.2.7 on 2023-12-04 07:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taxonomy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open', models.TextField(blank=True, null=True)),
                ('yes_or_no', models.BooleanField(blank=True, null=True)),
                ('matching', models.IntegerField(blank=True, choices=[('1', '{1:5, 2:6, 3:7, 4:8}'), ('2', '{1:5, 2:6, 3:8, 4:7}'), ('3', '{1:5, 2:7, 3:6, 4:8}'), ('4', '{1:5, 2:7, 3:8, 4:6}'), ('5', '{1:5, 2:8, 3:7, 4:5}'), ('6', '{1:5, 2:8, 3:5, 4:7}'), ('7', '{1:6, 2:7, 3:8, 4:5}'), ('8', '{1:6, 2:7, 3:5, 4:8}'), ('9', '{1:6, 2:8, 3:5, 4:7}'), ('10', '{1:6, 2:8, 3:7, 4:5}'), ('11', '{1:7, 2:8, 3:5, 4:6}'), ('12', '{1:7, 2:8, 3:6, 4:5}'), ('13', '{1:7, 2:6, 3:7, 4:5}'), ('14', '{1:7, 2:6, 3:5, 4:7}'), ('15', '{1:7, 2:5, 3:6, 4:8}'), ('16', '{1:7, 2:5, 3:8, 4:6}'), ('17', '{1:8, 2:7, 3:5, 4:6}'), ('18', '{1:8, 2:7, 3:6, 4:5}'), ('19', '{1:8, 2:6, 3:7, 4:5}'), ('20', '{1:8, 2:6, 3:5, 4:7}'), ('21', '{1:8, 2:8, 3:6, 4:7}'), ('22', '{1:8, 2:8, 3:7, 4:6}')], null=True)),
                ('fill_in_the_blank', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FillInTheBlank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('question', models.TextField(blank=True, null=True)),
                ('rubic_code', models.IntegerField(blank=True, null=True)),
                ('question_image', models.ImageField(storage='/static/question/images/', upload_to='')),
                ('marks', models.PositiveIntegerField()),
                ('answer', models.JSONField(blank=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='taxonomy.course')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('sub_topic', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='taxonomy.subtopic')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='taxonomy.topic')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Matching',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('question', models.TextField(blank=True, null=True)),
                ('rubic_code', models.IntegerField(blank=True, null=True)),
                ('question_image', models.ImageField(storage='/static/question/images/', upload_to='')),
                ('marks', models.PositiveIntegerField()),
                ('option1', models.CharField(blank=True, max_length=512, null=True)),
                ('option2', models.CharField(blank=True, max_length=512, null=True)),
                ('option3', models.CharField(blank=True, max_length=512, null=True)),
                ('option4', models.CharField(blank=True, max_length=512, null=True)),
                ('option5', models.CharField(blank=True, max_length=512, null=True)),
                ('option6', models.CharField(blank=True, max_length=512, null=True)),
                ('option7', models.CharField(blank=True, max_length=512, null=True)),
                ('option8', models.CharField(blank=True, max_length=512, null=True)),
                ('answer', models.TextField(blank=True, choices=[('1', '{1:5, 2:6, 3:7, 4:8}'), ('2', '{1:5, 2:6, 3:8, 4:7}'), ('3', '{1:5, 2:7, 3:6, 4:8}'), ('4', '{1:5, 2:7, 3:8, 4:6}'), ('5', '{1:5, 2:8, 3:7, 4:5}'), ('6', '{1:5, 2:8, 3:5, 4:7}'), ('7', '{1:6, 2:7, 3:8, 4:5}'), ('8', '{1:6, 2:7, 3:5, 4:8}'), ('9', '{1:6, 2:8, 3:5, 4:7}'), ('10', '{1:6, 2:8, 3:7, 4:5}'), ('11', '{1:7, 2:8, 3:5, 4:6}'), ('12', '{1:7, 2:8, 3:6, 4:5}'), ('13', '{1:7, 2:6, 3:7, 4:5}'), ('14', '{1:7, 2:6, 3:5, 4:7}'), ('15', '{1:7, 2:5, 3:6, 4:8}'), ('16', '{1:7, 2:5, 3:8, 4:6}'), ('17', '{1:8, 2:7, 3:5, 4:6}'), ('18', '{1:8, 2:7, 3:6, 4:5}'), ('19', '{1:8, 2:6, 3:7, 4:5}'), ('20', '{1:8, 2:6, 3:5, 4:7}'), ('21', '{1:8, 2:8, 3:6, 4:7}'), ('22', '{1:8, 2:8, 3:7, 4:6}')], max_length=5, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='taxonomy.course')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('sub_topic', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='taxonomy.subtopic')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='taxonomy.topic')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OpenQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('question', models.TextField(blank=True, null=True)),
                ('rubic_code', models.IntegerField(blank=True, null=True)),
                ('question_image', models.ImageField(storage='/static/question/images/', upload_to='')),
                ('marks', models.PositiveIntegerField()),
                ('answer', models.TextField(blank=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='taxonomy.course')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('sub_topic', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='taxonomy.subtopic')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='taxonomy.topic')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='YesOrNo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('question', models.TextField(blank=True, null=True)),
                ('rubic_code', models.IntegerField(blank=True, null=True)),
                ('question_image', models.ImageField(storage='/static/question/images/', upload_to='')),
                ('marks', models.PositiveIntegerField()),
                ('answer', models.BooleanField(blank=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='taxonomy.course')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('sub_topic', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='taxonomy.subtopic')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='taxonomy.topic')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuestionSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('type', models.IntegerField(blank=True, choices=[(1, 'Open'), (2, 'Yes Or No'), (3, 'Multiple'), (4, 'Fib')], null=True)),
                ('answer', models.ManyToManyField(to='assessments.answer')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('fill_in_the_blank_question', models.ManyToManyField(to='assessments.fillintheblank')),
                ('matching_question', models.ManyToManyField(to='assessments.matching')),
                ('open_question', models.ManyToManyField(to='assessments.openquestion')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
                ('yes_or_no_question', models.ManyToManyField(to='assessments.yesorno')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MultipleChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('question', models.TextField(blank=True, null=True)),
                ('rubic_code', models.IntegerField(blank=True, null=True)),
                ('question_image', models.ImageField(storage='/static/question/images/', upload_to='')),
                ('marks', models.PositiveIntegerField()),
                ('option1', models.CharField(blank=True, max_length=512, null=True)),
                ('option2', models.CharField(blank=True, max_length=512, null=True)),
                ('option3', models.CharField(blank=True, max_length=512, null=True)),
                ('option4', models.CharField(blank=True, max_length=512, null=True)),
                ('answer', models.IntegerField(blank=True, choices=[(1, 'Option1'), (2, 'Option2'), (3, 'Option3'), (4, 'Option4')], null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='taxonomy.course')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('sub_topic', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='taxonomy.subtopic')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='taxonomy.topic')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('description', models.TextField(verbose_name='Description')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField(auto_now=True)),
                ('completed', models.BooleanField()),
                ('score', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Score')),
                ('type', models.IntegerField(choices=[(1, 'Online'), (2, 'Offline')], default=1)),
                ('approved', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('question_set', models.ManyToManyField(to='assessments.questionset')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
