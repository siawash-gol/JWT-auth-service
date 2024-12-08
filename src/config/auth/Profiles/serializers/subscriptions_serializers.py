from rest_framework import serializers
from config.apps.ClientHub.models import UserPlan, Subscription, PlanFeatures


class PlanDetailSerializer(serializers.ModelSerializer):
    plan_name = serializers.CharField(source='plan.plan')
    duration = serializers.CharField(source='plan.duration_period')
    price = serializers.DecimalField(source='plan.price', max_digits=10, decimal_places=1)
    date_created = serializers.DateTimeField()
    expires_in = serializers.DateTimeField(source='subscriptions.first.expires_in')
    active = serializers.BooleanField(source='subscriptions.first.active')
    get_features = serializers.CharField()
    get_progres = serializers.DecimalField(max_digits=10, decimal_places=2, source='subscriptions.first.get_progres')

    class Meta:
        model = UserPlan
        fields = ['plan_name', 'duration',
                  'price', 'date_created',
                  'expires_in', 'active',
                  'get_features', 'get_progres']


class DeleteUserPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPlan
        fields = ['id', 'user', 'plan']
