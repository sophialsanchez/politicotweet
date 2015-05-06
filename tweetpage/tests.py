from django.test import TestCase
from tweetpage.models import Result

class ResultTests(TestCase):

	def test_title(self):
		"""The result title should match a string of that title."""
		test_result = Result.objects.create(title="Ace", img_src="ace.jpg",
		description="You're a superstar, ace!", slug="ace")
		self.assertEqual(Result.objects.get(title="Ace").title, "Ace")
	
	def test_img_src(self):
		"""The result image source should match a string of that image source."""
		test_result = Result.objects.create(title="Ace", img_src="ace.jpg",
		description="You're a superstar, ace!", slug="ace")
		self.assertEqual(Result.objects.get(title="Ace").img_src, "ace.jpg")

	def test_description(self):
		"""The result description should match a string of that description."""
		test_result = Result.objects.create(title="Ace", img_src="ace.jpg",
		description="You're a superstar, ace!", slug="ace")
		self.assertEqual(Result.objects.get(title="Ace").description, "You're a superstar, ace!")
	
	def test_slug(self):
		"""The result slug should match a string of that slug."""
		test_result = Result.objects.create(title="Ace", img_src="ace.jpg",
		description="You're a superstar, ace!", slug="ace")
		self.assertEqual(Result.objects.get(title="Ace").slug, "ace")
