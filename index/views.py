from django.http import HttpResponse
from django.shortcuts import (
    render, get_object_or_404, redirect, reverse
)
from django.views.generic import TemplateView
from django.views import generic
from .models import Review
from .forms import ReviewForm
from django.contrib import messages
from django.db.models import Avg
from django.views.generic import TemplateView
# star ratings instead of numbers

# Create your views here.


def display_index(request):

    return render(
        request,
        "index/index.html", {
        }
    )


class ReviewList(generic.ListView):
    queryset = Review.objects.all()
    template_name = "index.html"

    def get_queryset(self):
        # Annotate each takeaway with its average rating
        return Review.objects.filter(status=1).annotate(
            average_rating=Avg('reviews__rating')
        ).order_by('Review_name')


def takeaway_detail(request, slug):
    queryset = Review.objects.filter(status=1)
    takeaway = get_object_or_404(queryset, slug=slug)
    reviews = takeaway.reviews.all().order_by("-created_on")
    reviews_count = takeaway.reviews.filter(approved=True).count()
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg']

    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.poster = request.user
            review.review_title = review_form.cleaned_data.get('review_title')
            review.review_content = review_form.cleaned_data.get(
                'review_content'
            )
            review.rating = review_form.cleaned_data.get('rating')
            review.takeaway_name = takeaway
            review.save()
            messages.add_message(
                request, messages.SUCCESS, 'Review has been submitted'
            )

            return redirect('index', slug=slug)
    else:
        review_form = ReviewForm()

    return render(
        request,
        "index.html",
        {
            "takeaway": takeaway,
            "reviews": reviews,
            "reviews_count": reviews_count,
            "review_form": review_form,
            "average_rating": average_rating,
        },
    )


def review_edit(request, slug, review_id):
    if request.method == "POST":
        queryset = Review.objects.filter(status=1)
        takeaway = get_object_or_404(queryset, slug=slug)
        review = get_object_or_404(Review, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.poster = request.user
            review.review_title = review_form.cleaned_data.get(
                'review_title'
            )
            review.review_content = review_form.cleaned_data.get(
                'review_content'
            )
            review.rating = review_form.cleaned_data.get('rating')
            review.takeaway_name = takeaway
            review.save()
            messages.add_message(
                request, messages.SUCCESS, 'Review edited successfully'
            )
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating Review!'
            )
    return HttpResponseRedirect(reverse('index', args=[slug]))


def review_delete(request, slug, review_id):
    queryset = Review.objects.filter(status=1)
    takeaway = get_object_or_404(queryset, slug=slug)
    review = get_object_or_404(Review, pk=review_id)

    if review.poster == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own reviews!'
        )

    return HttpResponseRedirect(reverse('index', args=[slug]))
