from .views.subscription_views import ActivePlanDetailView, DeleteUserPlanView
from django.urls import path

urlpatterns = [
    path('subscriptions/plan-detail', ActivePlanDetailView.as_view(), name='plan_detail'),
    path('subscriptions/plan-cancel/<int:pk>', DeleteUserPlanView.as_view(), name='cancel_plan'),

]
