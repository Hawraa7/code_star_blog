from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Event, Post  # Ensure Post is imported
from .forms import CommentForm

class PostList(generic.ListView):
   model = Event
   template_name = "index.html"
   paginate_by = 12


def event_detail(request, event_id):
   event = get_object_or_404(Event, id=event_id)
   return render(request, "event_detail.html", {"event": event})

def post_detail(request, slug):
   queryset = Post.objects.filter(status=1)  # Ensure correct indentation
   post = get_object_or_404(queryset, slug=slug)
   comments = post.comments.all().order_by("-created_on")
   comment_count = post.comments.filter(approved=True).count()
   if request.method == "POST":
      comment_form = CommentForm(data=request.POST)
      if comment_form.is_valid():
         comment = comment_form.save(commit=False)
         comment.author = request.user
         comment.post = post
         comment.save()
         messages.add_message(
         request, messages.SUCCESS,
         'Comment submitted and awaiting approval'
    )

   comment_form = CommentForm()

   return render(
      request,
      "blog/post_detail.html",
      {
         "post": post,
         "comments": comments,
         "comment_count": comment_count,
         "comment_form": comment_form,
    },
    )