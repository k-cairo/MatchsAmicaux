from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostAnnounceForm, CommentForm
from .models import Announce, Comment


def index(request):
    announces = Announce.objects.all()
    return render(request, "Website/index.html", context={"announces": announces})


def new_announce(request):
    last_name = request.user.last_name
    first_name = request.user.first_name
    print(f"{last_name} {first_name}")
    if request.method == "POST":
        form = PostAnnounceForm(request.POST)
        if form.is_valid():
            author = f"{request.user.last_name} {request.user.first_name}"
            author_club = request.user.club
            author_category = request.user.category
            author_practice_level = request.user.practice_level
            hour = form.cleaned_data["hour"]
            date = form.cleaned_data["date"]
            location = form.cleaned_data["location"]
            desired_level = form.cleaned_data["desired_level"]
            announce = Announce(author=author, author_club=author_club, author_category=author_category,
                                author_practice_level=author_practice_level, hour=hour, date=date, location=location,
                                desired_level=desired_level)
            announce.save()
            return redirect('Website-index')
    else:
        form = PostAnnounceForm()
    return render(request, "Website/new_announce.html", context={"form": form})


def announce_detail(request, identifier):
    target_announce = get_object_or_404(Announce, id=identifier)

    comments = target_announce.comments.filter(is_active=True)

    new_comment = None

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.announce = target_announce
            new_comment.email = request.user.email
            new_comment.author = f"{request.user.last_name} {request.user.first_name}"
            new_comment.save()
            return redirect('Website-announce', identifier)
    else:
        comment_form = CommentForm()

    return render(request, 'Website/announce_detail.html', context={'target_announce': target_announce,
                                                             "comments": comments,
                                                             "new_comment": new_comment,
                                                             "comment_form": comment_form})


def delete_announce(request, identifier):
    target_announce = Announce.objects.filter(id=identifier).get()
    target_announce.delete()
    return redirect('Website-index')


def delete_comment(request, identifier):
    target_comment = Comment.objects.filter(id=identifier).get()
    target_comment.delete()
    return redirect('Website-index')
