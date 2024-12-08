from config.auth.Profiles.serializers.subscriptions_serializers import PlanDetailSerializer, DeleteUserPlanSerializer
from config.apps.ClientHub.models import Plan, PlanFeatures, UserPlan
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics


class ActivePlanDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_plan = request.user.user_plan
        serializer = PlanDetailSerializer(user_plan)
        return Response(serializer.data)


class DeleteUserPlanView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DeleteUserPlanSerializer
    queryset = UserPlan.objects.all()
