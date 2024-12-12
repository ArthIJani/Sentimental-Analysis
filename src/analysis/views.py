from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login 
from .forms import SentimentForm
from .utils import analyze_sentiment
from .models import SentimentHistory



@login_required  # Ensure only authenticated users can access this view
def analyze_view(request):
    result = None
    if request.method == 'POST':
        form = SentimentForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['user_input']
            result = analyze_sentiment(user_input)

            # Save the sentiment analysis result linked to the logged-in user
            SentimentHistory.objects.create(user=request.user, user_input=user_input, sentiment=result)

    else:
        form = SentimentForm()

    # Fetch the logged-in user's sentiment history
    history = SentimentHistory.objects.filter(user=request.user).order_by('-timestamp')[:10]

    return render(request, 'analysis/analyze.html', {'form': form, 'result': result, 'history': history})


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Log in the new user automatically
            return redirect('analyze')  # Redirect to the analysis page
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})