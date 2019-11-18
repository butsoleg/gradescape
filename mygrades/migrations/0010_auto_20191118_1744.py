# Generated by Django 2.2 on 2019-11-18 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mygrades', '0009_auto_20191115_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curriculum',
            name='grade_level',
            field=models.CharField(choices=[('PK', 'Pre-K'), ('K', 'K'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('All', 'All'), ('High School', 'High School')], max_length=20),
        ),
        migrations.AlterField(
            model_name='standard',
            name='grade_level',
            field=models.CharField(choices=[('PK', 'Pre-K'), ('K', 'K'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('High School', 'High School')], max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.CharField(choices=[('PK', 'Pre-K'), ('K', 'K'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('High School', 'High School')], max_length=20),
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quarter', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=1)),
                ('week', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18')], max_length=2)),
                ('semester', models.CharField(choices=[('1', '1'), ('2', '2')], max_length=1)),
                ('complete', models.BooleanField(default=False)),
                ('curriculum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='curriculum_attendance', to='mygrades.Curriculum')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendance_student', to='mygrades.Student')),
            ],
        ),
    ]
