# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-05 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[(b'yesNoQuestion', '<span class="black-text">Yes/No</span><br><small class="teal-text">The participant must respond with Yes or No.</small>'), (b'MultiChoices', '<span class="black-text">Multiple choices with one Answer</span><br><small class="teal-text">The participant is conducted to pick one in response options list.</small>'), (b'MultiChoiceWithAnswer', '<span class="black-text">Multiple choices with multiple answers</span><br><small class="teal-text">The participant is conducted to pick (one or more responses) in response options list.</small>'), (b'TextField', '<span class="black-text">Comment Area</span><br><small class="teal-text">Use the comment box to collect written comments from respondents.</small>'), (b'RatingField', '<span class="black-text">Rating scale</span><br><small class="teal-text">The respondents will rate the level of satisfaction.</small>')], default=b'yesNoQuestion', max_length=200, verbose_name='Type of answer'),
        ),
    ]