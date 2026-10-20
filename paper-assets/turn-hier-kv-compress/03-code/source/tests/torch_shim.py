"""Minimal torch-compatible tensor API backed by numpy, for CPU-only testing
without a real torch installation."""

import numpy as np


class Tensor:
    """Thin wrapper around ndarray that provides the torch Tensor subset used by turnkv."""

    def __init__(self, data, dtype=None):
        if isinstance(data, Tensor):
            self._data = data._data.copy()
        elif isinstance(data, np.ndarray):
            self._data = data if dtype is None else data.astype(dtype)
        else:
            self._data = np.array(data, dtype=dtype or np.float32)

    # --- properties --------------------------------------------------------
    @property
    def shape(self):
        return self._data.shape

    @property
    def dtype(self):
        return self._data.dtype

    @property
    def device(self):
        return "cpu"

    # --- creation helpers --------------------------------------------------
    def clone(self):
        return Tensor(self._data.copy())

    # --- indexing ----------------------------------------------------------
    def __getitem__(self, key):
        result = self._data[key]
        if isinstance(result, np.ndarray):
            return Tensor(result)
        return result  # scalar

    def __setitem__(self, key, value):
        if isinstance(value, Tensor):
            self._data[key] = value._data
        else:
            self._data[key] = value

    # --- arithmetic --------------------------------------------------------
    def __mul__(self, other):
        if isinstance(other, Tensor):
            return Tensor(self._data * other._data)
        return Tensor(self._data * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __add__(self, other):
        if isinstance(other, Tensor):
            return Tensor(self._data + other._data)
        return Tensor(self._data + other)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Tensor):
            return Tensor(self._data - other._data)
        return Tensor(self._data - other)

    def __truediv__(self, other):
        if isinstance(other, Tensor):
            return Tensor(self._data / other._data)
        return Tensor(self._data / other)

    def __pow__(self, other):
        return Tensor(self._data ** other)

    # --- reductions --------------------------------------------------------
    def mean(self, dim=None, keepdim=False):
        result = self._data.mean(axis=dim, keepdims=keepdim)
        return Tensor(result)

    def std(self, dim=None, keepdim=False):
        # torch default: ddof=1 for .std()
        result = self._data.std(axis=dim, ddof=1, keepdims=keepdim)
        return Tensor(result)

    def sum(self, dim=None, keepdim=False):
        result = self._data.sum(axis=dim, keepdims=keepdim)
        return Tensor(result)

    def min(self):
        return Tensor(np.array(self._data.min()))

    def max(self):
        return Tensor(np.array(self._data.max()))

    def item(self):
        return self._data.item()

    def clamp(self, min=None, max=None):
        return Tensor(np.clip(self._data, min, max))

    # --- shape ops ---------------------------------------------------------
    def unsqueeze(self, dim):
        return Tensor(np.expand_dims(self._data, axis=dim))

    def expand(self, *sizes):
        return Tensor(np.broadcast_to(self._data, sizes).copy())

    def argsort(self, dim=-1):
        return Tensor(np.argsort(self._data, axis=dim))

    def __repr__(self):
        return f"Tensor({self._data})"

    def __eq__(self, other):
        if isinstance(other, Tensor):
            return Tensor(self._data == other._data)
        return Tensor(self._data == other)


# ---------------------------------------------------------------------------
# Module-level functions matching torch.*
# ---------------------------------------------------------------------------

def tensor(data, dtype=None):
    return Tensor(data, dtype=dtype or np.float32)


def zeros(*size, dtype=None, device=None):
    return Tensor(np.zeros(size, dtype=dtype or np.float32))


def ones(*size, dtype=None, device=None):
    return Tensor(np.ones(size, dtype=dtype or np.float32))


def rand(*size):
    return Tensor(np.random.rand(*size).astype(np.float32))


def linspace(start, end, steps):
    return Tensor(np.linspace(start, end, steps, dtype=np.float32))


def allclose(a, b, atol=1e-5, rtol=1e-5):
    return np.allclose(a._data, b._data, atol=atol, rtol=rtol)


def equal(a, b):
    return np.array_equal(a._data, b._data)
