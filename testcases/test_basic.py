import pytest

from testcases.conftest import launch


@pytest.mark.usefixtures("launch")
class TestBase:
    pass
