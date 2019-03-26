from .viewsets import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register('customer', CustomerViewSet, base_name='customer')
router.register('organisation', OrganisationViewSet, base_name='organisation')
router.register('project', ProjectViewSet, base_name='project')
router.register('quote', QuoteViewSet, base_name='quote')
router.register('request_for_change', RequestForChangeViewSet, base_name='request_for_change')
router.register('requirement', RequirementViewSet, base_name='requirement')
router.register('requirement_item', RequirementItemViewSet, base_name='requirement_item')
router.register('task', TaskViewSet, base_name='task')
router.register('user', UserViewSet, base_name='user')
