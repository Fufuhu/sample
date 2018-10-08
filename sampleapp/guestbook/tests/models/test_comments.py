from django.test import TestCase
from guestbook.models.comments import Comment
from guestbook.models.users import Commentator

class TestComment(TestCase):
    def test_commentator(self):

        commentator = Commentator(
            name="hoge"
        )
        commentator.save()

        comment = Comment(
            title="test",
            comment="test comment",
            commentator=commentator
        )
        comment.save()

        # Commentatorが期待したものが帰ってくることを確認
        commentator = Comment.objects.get(comment_id=comment.comment_id).commentator

        self.assertEqual(commentator.name, "hoge")

        comments = Comment.objects.filter(commentator=commentator)
        self.assertEqual(len(comments), 1)
        self.assertEqual(comment.title, "test")
        self.assertEqual(comment.comment, "test comment")