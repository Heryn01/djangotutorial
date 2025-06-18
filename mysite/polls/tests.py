from django.test import TestCase

# Create your tests here.
import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
        
    def test_was_published_recently_with_past_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is over a week old.
        """
        time = timezone.now() - datetime.timedelta(days=8)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)
        
    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is under a week old.
        """
        time = timezone.now() - datetime.timedelta(days=6.999)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)
        
    def test_was_published_recently_with_current_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is the same as now.
        """
        time = timezone.now()
        current_question = Question(pub_date=time)
        self.assertIs(current_question.was_published_recently(), True)        