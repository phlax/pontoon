
import pytest

from pontoon.base.models import Group


@pytest.fixture
def group0():
    return Group.objects.create(name="group0")
