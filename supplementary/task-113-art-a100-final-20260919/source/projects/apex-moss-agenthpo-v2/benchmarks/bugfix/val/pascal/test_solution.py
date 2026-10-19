import json
from pathlib import Path

import pytest

import solution

pytestmark = pytest.mark.timeout(3)

CASES = json.loads((Path(__file__).parent / "cases.json").read_text())


@pytest.mark.parametrize("case", CASES)
def test_case(case):
    args, expected = case
    result = getattr(solution, "pascal")(*args)
    if isinstance(result, tuple):
        result = list(result)
    assert result == expected
