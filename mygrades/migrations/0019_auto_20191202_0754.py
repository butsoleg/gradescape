# Generated by Django 2.2 on 2019-12-02 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mygrades', '0018_auto_20191126_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='goog_calendar',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='phone',
            field=models.CharField(max_length=75, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='principal_email',
            field=models.CharField(max_length=75, null=True),
        ),
        migrations.AlterField(
            model_name='curriculum',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='exemptassignment',
            name='assignments',
            field=models.ManyToManyField(blank=True, to='mygrades.Assignment'),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=1500)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_student', to='mygrades.Student')),
            ],
        ),
    ]
