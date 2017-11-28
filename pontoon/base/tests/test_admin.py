"""
Tests related to all admin code
"""

from mock import MagicMock
from nose.tools import assert_equal

from pontoon.base.admin import UserAdmin
from pontoon.base.models import UserRoleLogAction
from pontoon.base.tests import (
    TestCase,
    UserFactory,
    GroupFactory,
)


class UserAdminUserRoleLogTests(TestCase):
    """
    Check if admin form saves logs of changes on users groups they are
    assigned to.
    """
    def setUp(self):
        self.admin_form = UserAdmin()
        self.user = UserFactory.create()
        request = MagicMock()
        request.user = self.user
        self.request = request

    def get_form_mock(self, groups):
        form_mock = MagicMock()
        return form_mock

    def test_no_change_during_save(self):
        pass
    def test_add_user_to_groups(self):
        # Check idempotency
        request = MagicMock()
        first_group, second_group, third_group = GroupFactory.create_batch(3)
        form_mock = self.get_form_mock([first_group])

        self.admin_form.save_model(
            self.request,
            self.user,
            form_mock,
            True
        )
        assert_equal(self.user.groups.all(), list([first_group]))
        assert_equal(list(UserRoleLogAction.objects.all()), [])
        assert False

    def test_remove_user_from_groups(self):
        assert False

    def test_remove_users_from_all_groups(self):
        assert False
