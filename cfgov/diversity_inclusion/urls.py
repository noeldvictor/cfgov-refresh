from django.urls import re_path
from django.views.generic import TemplateView

from diversity_inclusion.views import GetAssessmentForm


urlpatterns = [
    re_path(
        r"^voluntary-assessment-onboarding-form/$(?i)",
        GetAssessmentForm.as_view(),
        name="voluntary_assessment_form",
    ),
    re_path(
        r"^voluntary-assessment-onboarding-form/form-submitted/$(?i)",
        TemplateView.as_view(
            template_name="diversity_inclusion/form-submitted.html"
        ),
        name="form_submitted",
    ),
    re_path(
        r"^voluntary-assessment-onboarding-form/privacy-act-statement/$(?i)",
        TemplateView.as_view(
            template_name="diversity_inclusion/privacy.html"
        ),
        name="privacy",
    ),
]
