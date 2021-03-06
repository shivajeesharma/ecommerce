# Generated by Django 2.2.17 on 2020-11-12 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0047_codeassignmentnudgeemailtemplates'),
    ]

    operations = [
        migrations.AddField(
            model_name='offerassignmentemailsentrecord',
            name='code',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='offerassignmentemailsentrecord',
            name='receiver_id',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='offerassignmentemailsentrecord',
            name='sender_category',
            field=models.CharField(choices=[('automatic', 'Automatic'), ('manual', 'Manual')], max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='offerassignmentemailsentrecord',
            name='sender_id',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='offerassignmentemailsentrecord',
            name='user_email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='offerassignmentemailsentrecord',
            name='email_type',
            field=models.CharField(choices=[('assign', 'Assign'), ('remind', 'Remind'), ('revoke', 'Revoke'), ('Day3', 'Day 3'), ('Day10', 'Day 10'), ('Day19', 'Day 19')], max_length=32),
        ),
        migrations.AlterField(
            model_name='offerassignmentemailsentrecord',
            name='template_content_type',
            field=models.ForeignKey(limit_choices_to=models.Q(models.Q(('app_label', 'offer'), ('model', 'offerassignmentemailtemplates')), models.Q(('app_label', 'offer'), ('model', 'codeassignmentnudgeemailtemplates')), _connector='OR'), null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
    ]
