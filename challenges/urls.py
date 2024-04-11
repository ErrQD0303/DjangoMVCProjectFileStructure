from django.urls import path, re_path, register_converter, include

# from . mean from the samefolder
from . import views, converters

register_converter(converters.TwoDigitMonthConverter, 'mm')

extra_patterns = [
    re_path(
        r"(?P<folder_name>.*)?/?page-(?P<page_num>\d*)/", views.other_views),]

# path method
# the first argument is the path of the view
urlpatterns = [
    # Placeholder for all the months in the year
    path("", views.index),
    path("<mm:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge"),
    path("credit", include(extra_patterns))
]
