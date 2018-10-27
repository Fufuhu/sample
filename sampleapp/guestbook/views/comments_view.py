from django.views.generic import View
from django.shortcuts import render, redirect
from django.urls import reverse

from guestbook.models.comments import Comment
from guestbook.models.users import Commentator

class CommentsView(View):
    def get(self, request, comment_id):


        root_comment = Comment.objects.get(comment_id=comment_id)
        thread_comments = Comment.objects.filter(parent=root_comment).order_by('append_at')

        comments = [root_comment]
        for comment in thread_comments:
            comments.append(comment)

        response_params = {
            'root_comment': root_comment,
            'comments': comments,
        }
        
        return render(request, 'comments.html', response_params)

    
    def post(self, request, comment_id):

        user_name = request.POST.get('name')
        if Commentator.objects.filter(name=user_name).exists():
            commentator = Commentator.objects.get(name=user_name)
        else:
            commentator = Commentator(
                name=user_name
            )
            commentator.save()

        title = request.POST.get('title')
        comment = request.POST.get('comment')

        Comment(
            title=title,
            comment=comment,
            commentator=commentator,
            parent=Comment.objects.get(comment_id=comment_id)
        ).save()

        return redirect(to=reverse('guestbook:comments', args=[comment_id]))