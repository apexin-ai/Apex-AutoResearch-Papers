import pytest
import solution

pytestmark = pytest.mark.timeout(20)


def test_solution_imports_and_entry_point_is_callable():
    assert callable(solution.task_func)
