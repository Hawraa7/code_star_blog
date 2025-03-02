from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Event, Post  # Ensure Post is imported

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

   return render(
      request,
      "blog/post_detail.html",
      {
         "post": post,
         "coder": "Matt Rudge"
      },
    )