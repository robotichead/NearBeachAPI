from NearBeach.models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

"""
Rules
~~~~~
1. Each view set will need to have permissions checked
2. Can only list those objects that user has access to
"""
class CustomerViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = customer.objects.filter(
            is_deleted="FALSE",
        )
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)

class OrganisationViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = organisation.objects.filter(
            is_deleted="FALSE",
        )
        serializer = OrganisationSerializer(queryset, many=True)
        return Response(serializer.data)


class ProjectViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = project.objects.filter(
            is_deleted="FALSE",
            project_id__in=object_assignment.objects.filter(
                is_deleted="FALSE",
                project_id__isnull=False,
                group_id__in=user_group.objects.filter(
                    is_deleted="FALSE",
                    username=request.user,
                    group_id__isnull=False,
                ).values('group_id')
            ).values('project_id')
        )
        serializer = ProjectSerializer(queryset, many=True)
        return Response(serializer.data)

class QuoteViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = quote.objects.filter(
            is_deleted="FALSE",
            quote_id__in=object_assignment.objects.filter(
                is_deleted="FALSE",
                quote_id__isnull=False,
                group_id__in=user_group.objects.filter(
                    is_deleted="FALSE",
                    username=request.user,
                    group_id__isnull=False,
                ).values('group_id')
            ).values('quote_id')
        )
        serializer = QuoteSerializer(queryset, many=True)
        return Response(serializer.data)

class RequestForChangeViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = request_for_change.objects.filter(
            is_deleted="FALSE",
            rfc_id__in=object_assignment.objects.filter(
                is_deleted="FALSE",
                request_for_change_id__isnull=False,
                group_id__in=user_group.objects.filter(
                    is_deleted="FALSE",
                    username=request.user,
                    group_id__isnull=False,
                ).values('group_id')
            ).values('request_for_change_id')
        )
        serializer = RequestForChangeSerializer(queryset, many=True)
        return Response(serializer.data)


class RequirementViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = requirement.objects.filter(
            is_deleted="FALSE",
            requirement_id__in=object_assignment.objects.filter(
                is_deleted="FALSE",
                requirement_id__isnull=False,
                group_id__in=user_group.objects.filter(
                    is_deleted="FALSE",
                    username=request.user,
                    group_id__isnull=False,
                ).values('group_id')
            ).values('requirement_id')
        )
        serializer = RequirementSerializer(queryset, many=True)
        return Response(serializer.data)


class RequirementItemViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = requirement_item.objects.filter(
            is_deleted="FALSE",
            requirement_id__in=object_assignment.objects.filter(
                is_deleted="FALSE",
                requirement_id__isnull=False,
                group_id__in=user_group.objects.filter(
                    is_deleted="FALSE",
                    username=request.user,
                    group_id__isnull=False,
                ).values('group_id')
            ).values('requirement_id')
        )
        serializer = RequirementItemSerializer(queryset, many=True)
        return Response(serializer.data)


class TaskViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = task.objects.filter(
            is_deleted="FALSE",
            task_id__in=object_assignment.objects.filter(
                is_deleted="FALSE",
                task_id__isnull=False,
                group_id__in=user_group.objects.filter(
                    is_deleted="FALSE",
                    username=request.user,
                    group_id__isnull=False,
                ).values('group_id')
            ).values('task_id')
        )
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)


class UserViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)