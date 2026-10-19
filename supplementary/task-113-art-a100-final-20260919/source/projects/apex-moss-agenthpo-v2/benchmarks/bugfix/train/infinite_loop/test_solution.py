import signal
import pytest
from solution import sum_until


class TimeoutError(Exception):
    pass


def _timeout_handler(signum, frame):
    raise TimeoutError("Function took too long — possible infinite loop")


def run_with_timeout(func, args=(), timeout=2):
    old = signal.signal(signal.SIGALRM, _timeout_handler)
    signal.alarm(timeout)
    try:
        result = func(*args)
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old)
    return result


def test_sum_until_5():
    assert run_with_timeout(sum_until, (5,)) == 15


def test_sum_until_1():
    assert run_with_timeout(sum_until, (1,)) == 1


def test_sum_until_10():
    assert run_with_timeout(sum_until, (10,)) == 55
