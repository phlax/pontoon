
import pytest

from django.db import DataError

from pontoon.base.models import UserRoleLogAction


@pytest.mark.django_db
def test_user_role_log_action_defaults(user0, user1, group0):
    log_action = UserRoleLogAction.objects.create(
        group=group0, performed_by=user0, performed_on=user1)
    assert log_action.created_at
    assert log_action.group == group0
    assert log_action.performed_by == user0
    assert log_action.performed_on == user1
    assert log_action.action_type == ''


@pytest.mark.django_db
def test_user_role_log_action_action_type(user0, user1, group0):
    # action_type should not be longer than 6 chars
    UserRoleLogAction.objects.create(
        group=group0,
        performed_by=user0,
        performed_on=user1,
        action_type='x' * 6)
    with pytest.raises(DataError):
        UserRoleLogAction.objects.create(
            group=group0,
            performed_by=user0,
            performed_on=user1,
            action_type='x' * 7)
