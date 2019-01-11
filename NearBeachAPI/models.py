from django.db import models
from django.contrib.auth.models import User
import uuid

IS_DELETED_CHOICE = (
    ('TRUE', 'TRUE'),
    ('FALSE', 'FALSE'),
)

# Create your models here.
class api_allowed_host(models.Model):
    api_allowed_host_id=models.AutoField(primary_key=True)
    api_uuid=models.ForeignKey(
        'api_uuid',
        on_delete=models.CASCADE,
    )
    allowed_host=models.CharField(
        blank=False,
        null=False,
        max_length=255,
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    change_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='%(class)s_change_user',
    )
    is_deleted = models.CharField(
        max_length=5,
        choices=IS_DELETED_CHOICE,
        default='FALSE',
    )

    class Meta:
        db_table = "api_allowed_host"


class api_uuid(models.Model):
    api_uuid_id=models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True,
    )
    api_description=models.CharField(
        max_length=255,
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    change_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='%(class)s_change_user',
    )
    is_deleted = models.CharField(
        max_length=5,
        choices=IS_DELETED_CHOICE,
        default='FALSE',
    )

    class Meta:
        db_table = "api_uuid"