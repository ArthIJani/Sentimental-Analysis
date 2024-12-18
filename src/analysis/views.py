from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login 
from .forms import SentimentForm,FileUploadForm
from .utils import analyze_sentiment, summarize_text
from .models import SentimentHistory
import csv
from io import TextIOWrapper



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


@login_required
def batch_analysis_view(request):
    result = []
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Process uploaded CSV
            csv_file = TextIOWrapper(request.FILES['file'].file, encoding='utf-8')
            reader = csv.reader(csv_file)
            next(reader)  # Skip header row if necessary

            for row in reader:
                text = row[0]  # Assuming the first column contains the text
                sentiment = analyze_sentiment(text)
                result.append({'text': text, 'sentiment': sentiment})
                # Optionally save to the database
                SentimentHistory.objects.create(user=request.user, user_input=text, sentiment=sentiment)
    else:
        form = FileUploadForm()

    return render(request, 'analysis/batch_analysis.html', {'form': form, 'result': result})


@login_required
def summarize_view(request):
    result = None
    if request.method == 'POST':
        form = SentimentForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['user_input']
            result = summarize_text(user_input)
    else:
        form = SentimentForm()

    return render(request, 'analysis/summarize.html', {'form': form, 'result': result})