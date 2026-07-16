# pyrefly: ignore [missing-import]
from django.urls import path

from .views import (
    HealthCheckView,
    AnalyzeSentimentView,
    BatchAnalyzeView,
    ModelInfoView
)

urlpatterns = [

    path(
        "health/",
        HealthCheckView.as_view()
    ),

    path(
        "analyze/",
        AnalyzeSentimentView.as_view()
    ),

    path(
        "analyze/batch/",
        BatchAnalyzeView.as_view()
    ),

    path(
        "model-info/",
        ModelInfoView.as_view()
    ),

]