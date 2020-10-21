from django.urls import path
from . import views

app_name = "election"

urlpatterns = [
    path('', views.display_polling_unit_results, name="polling_units"),
    path('total_results/', views.display_poll_units_total, name="total_results"),
    path('add_polls_result', views.add_polling_unit_result, name="add_polls_result"),
]