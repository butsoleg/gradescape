# Generated by Django 2.2 on 2019-10-11 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('subject', models.CharField(choices=[('Math', 'Math'), ('ELA', 'ELA'), ('Science', 'Science'), ('History', 'History'), ('Other', 'Other')], max_length=30)),
                ('grade_level', models.CharField(choices=[('P', 'Pre-K'), ('K', 'Kinder'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('All', 'All'), ('High School', 'High School')], max_length=20)),
                ('tracking', models.CharField(choices=[('Minutes', 'Minutes'), ('Lessons', 'Lessons'), ('Percentage Complete', 'Percentage Complete')], max_length=20)),
                ('recorded_from', models.CharField(choices=[('Manual', 'Manual'), ('Automatic', 'Automatic')], max_length=20)),
                ('semesterend', models.CharField(max_length=50, null=True)),
                ('username', models.CharField(max_length=50, null=True)),
                ('password', models.CharField(max_length=50, null=True)),
                ('loginurl', models.CharField(max_length=100, null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade_level', models.CharField(choices=[('PK', 'Pre-K'), ('K', 'Kindergarten'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('PA', 'PA'), ('HS', 'HS'), ('9', '9'), ('A1', 'A1'), ('10', '10'), ('A2', 'A2'), ('11', '11'), ('G', 'G'), ('12', '12')], max_length=60)),
                ('standard_number', models.CharField(max_length=5)),
                ('standard_description', models.CharField(max_length=2000)),
                ('strand_code', models.CharField(max_length=10)),
                ('strand', models.CharField(max_length=50, null=True)),
                ('strand_description', models.CharField(max_length=1000, null=True)),
                ('objective_number', models.CharField(max_length=4)),
                ('objective_description', models.CharField(max_length=1000)),
                ('standard_code', models.CharField(max_length=20)),
                ('subject', models.CharField(choices=[('Math', 'Math'), ('ELA', 'ELA'), ('Science', 'Science'), ('History', 'History'), ('Other', 'Other')], max_length=30)),
                ('PDF_link', models.CharField(choices=[('Math', 'Math'), ('ELA', 'ELA'), ('Science', 'Science'), ('History', 'History'), ('Other', 'Other')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('epicenter_id', models.CharField(max_length=10, unique=True)),
                ('last_name', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=120)),
                ('phone_number', models.CharField(max_length=50)),
                ('additional_email', models.EmailField(max_length=120, null=True)),
                ('additional_phone_number', models.CharField(max_length=20, null=True)),
                ('grade', models.CharField(choices=[('P', 'Pre-K'), ('K', 'Kinder'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Gradebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking', models.CharField(max_length=20)),
                ('quarter', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=1)),
                ('week', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18')], max_length=2)),
                ('grade', models.IntegerField()),
                ('semester', models.CharField(choices=[('1', '1'), ('2', '2')], max_length=1)),
                ('curriculum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='curriculum_grade', to='mygrades.Curriculum')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gradebook_student', to='mygrades.Student')),
            ],
            options={
                'unique_together': {('student', 'curriculum', 'week', 'quarter')},
            },
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('curriculum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='curriculum_assignment', to='mygrades.Curriculum')),
                ('standard', models.ManyToManyField(to='mygrades.Standard')),
            ],
            options={
                'unique_together': {('name', 'curriculum')},
            },
        ),
    ]
