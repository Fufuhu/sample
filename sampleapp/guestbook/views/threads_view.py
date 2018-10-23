from django.views.generic import View
from django.shortcuts import render, redirect
from django.urls import reverse


from guestbook.models.comments import Comment
from guestbook.models.users import Commentator

class ThreadsView(View):
    def get(self, request):

        response_params = {
            'comments': Comment.objects.filter(parent=None),
        }
        return render(request, 'threads.html', response_params)

    
    def post(self, request):

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
            parent=None
        ).save()

        return redirect(to=reverse('guestbook:threads'))