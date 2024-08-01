from django.shortcuts import render

from .forms import RatingForm

def form(request):
    if request.method == 'POST':
        rating_form = RatingForm(request.POST)
    else:
        rating_form = RatingForm()

    return render(request, 'form.html', {'rating_form': rating_form})
