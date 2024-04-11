from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
# from django.template.loader import render_to_string

# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Learn Django for at least 20 minutes every day!",
    "may": "Learn Django for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Learn Django for at least 20 minutes every day!",
    "august": "Learn Django for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Learn Django for at least 20 minutes every day!",
    "november": "Learn Django for at least 20 minutes every day!",
    "december": None,
}


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html",
                  {"months": months})


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse(
        "month-challenge", args=[redirect_month])  # challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "month_name": month,
            "text": challenge_text
        })
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")


def other_views(request, folder_name, page_num):
    return HttpResponse(f"<div>folder name: {folder_name}</div><div>page number: {page_num}</div>")
