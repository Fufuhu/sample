from django.test import TestCase, Client
from django.urls import reverse

import uuid

from guestbook.models.comments import Comment
from guestbook.models.users import Commentator


class TestCommentsView(TestCase):

    URL_NAME='guestbook:comments'
    STATUS_OK=200
    REDIRECT=302

    def setUP(self):
        Comment.objects.all().delete()
        Commentator.objects.all().delete()

    def tearDown(self):
        Comment.objects.all().delete()
        Commentator.objects.all().delete()

    def test_get_comments_view(self):

        comment_id = uuid.uuid4()

        commentator = Commentator(
            name="test_commentator"
        )

        commentator.save()

        root_comment = Comment(
            comment_id=comment_id,
            title="test",
            comment="test_comment",
            commentator=commentator,
            parent=None
        )

        root_comment.save()

        client = Client()
        response = client.get(reverse(TestCommentsView.URL_NAME, args=[comment_id]))

        self.assertEqual(TestCommentsView.STATUS_OK, response.status_code)
    
    def test_post_comment_view(self):

        comment_id = uuid.uuid4()

        commentator = Commentator(
            name="test_commentator"
        )

        commentator.save()

        root_comment = Comment(
            comment_id=comment_id,
            title="test",
            comment="test_comment",
            commentator=commentator,
            parent=None
        )
        
        root_comment.save()

        request_body = {
            'name': 'test_name',
            'title': 'test_title',
            'comment': 'test_comment',
        }

        client = Client()
        response = client.post(reverse(TestCommentsView.URL_NAME, args=[comment_id]), request_body)

        self.assertEqual(TestCommentsView.REDIRECT, response.status_code) 

        comments = Comment.objects.filter(parent=root_comment)
        self.assertEqual(len(comments), 1)

        self.assertEqual(comments[0].commentator.name, request_body['name'])
        self.assertEqual(comments[0].title, request_body['title'])
        self.assertEqual(comments[0].comment, request_body['comment'])
