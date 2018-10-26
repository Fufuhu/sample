from django.test import TestCase, Client
from django.urls import reverse

from guestbook.models.comments import Comment
from guestbook.models.users import Commentator

class TestThreadsView(TestCase):

    URL_NAME='guestbook:threads'
    STATUS_OK=200
    REDIRECT=302

    def setUp(self):
        Comment.objects.all().delete()
        Commentator.objects.all().delete()

    def tearDown(self):
        Comment.objects.all().delete()
        Commentator.objects.all().delete()

    def test_get_thread_view(self):

        client = Client()
        response = client.get(reverse(TestThreadsView.URL_NAME))

        self.assertEqual(TestThreadsView.STATUS_OK, response.status_code)

    def test_post_thread_view(self):

        request_body = {
            'name': 'test_name',
            'title': 'test_title',
            'comment': 'test_comment',
        }

        client = Client()
        response = client.post(reverse(TestThreadsView.URL_NAME), request_body)

        self.assertEqual(TestThreadsView.REDIRECT, response.status_code)

        self.assertEqual(1, len(Comment.objects.all()))
        self.assertEqual(1, len(Commentator.objects.all()))

        self.assertEqual(request_body.get('name'), Commentator.objects.all()[0].name)

        comments = Comment.objects.all()
        self.assertEqual(request_body.get('title'), comments[0].title)
        self.assertEqual(request_body.get('comment'), comments[0].comment)

    def test_post_multiple_thread_view(self):

        request_bodies = [
            {
                'name': 'test_name1',
                'title': 'test_title1',
                'comment': 'test_comment1',
            },
            {
                'name': 'test_name2',
                'title': 'test_title2',
                'comment': 'test_comment2',
            }
        ]

        client = Client()
        for request_body in request_bodies:
            response = client.post(reverse(TestThreadsView.URL_NAME), request_body)
            self.assertEqual(TestThreadsView.REDIRECT, response.status_code)
        
        self.assertEqual(len(request_bodies), len(Comment.objects.all()))
        self.assertEqual(len(request_bodies), len(Commentator.objects.all()))

            