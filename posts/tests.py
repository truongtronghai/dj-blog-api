from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
# Create your tests here.
class BlogTests(TestCase):
    # Create mock database and mock data for test
    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(username='testuser1',password='abc123')
        testuser1.save()

        testpost = Post.objects.create(author=testuser1,title="Blog title",body="body content")
        testpost.save() # this test post has id =1 in mock database

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'

        self.assertEqual(author,'testuser1')
        self.assertEqual(title,'Blog title')
        self.assertEqual(body,'body content')
