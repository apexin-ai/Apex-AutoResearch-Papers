from __future__ import annotations

import hashlib
import textwrap
from pathlib import Path

import pytest

from optimization_lab.harness_builder.adapters.kernel_candidate_policy import (
    RESTRICTED_KERNEL_CANDIDATE_POLICY_SHA256,
    RESTRICTED_KERNEL_TASK_IDS,
    RestrictedKernelCandidateError,
    RestrictedKernelCandidatePolicy,
)
from optimization_lab.harness_builder.solutions import KernelBenchSolutionCodec


ROOT = Path(__file__).resolve().parents[1]


VALID_TRITON = textwrap.dedent(
    """
    import math
    import torch
    import torch.nn as nn
    import triton
    import triton.language as tl

    BLOCK = 256

    @triton.jit
    def sigmoid_kernel(x_ptr, out_ptr, n_elements: tl.constexpr, BLOCK: tl.constexpr):
        offsets = tl.program_id(0) * BLOCK + tl.arange(0, BLOCK)
        mask = offsets < n_elements
        values = tl.load(x_ptr + offsets, mask=mask, other=0.0)
        tl.store(out_ptr + offsets, tl.sigmoid(values), mask=mask)

    class ModelNew(nn.Module):
        def __init__(self):
            super().__init__()
            self.scale = math.sqrt(1.0)
            self._workspace = None

        def forward(self, x: torch.Tensor) -> torch.Tensor:
            output = torch.empty_like(x)
            n_elements = output.numel()
            sigmoid_kernel[(triton.cdiv(n_elements, BLOCK),)](
                x, output, n_elements, BLOCK=BLOCK, num_warps=4
            )
            return output * self.scale
    """
).strip() + "\n"


def test_policy_accepts_a_bounded_torch_triton_model_and_is_deterministic() -> None:
    first = RestrictedKernelCandidatePolicy().validate(VALID_TRITON)
    second = RestrictedKernelCandidatePolicy().validate(VALID_TRITON.encode("utf-8"))

    assert first == second
    assert first.source_sha256 == hashlib.sha256(VALID_TRITON.encode()).hexdigest()
    assert first.policy_sha256 == RESTRICTED_KERNEL_CANDIDATE_POLICY_SHA256
    assert first.triton_kernels == ("sigmoid_kernel",)
    assert first.model_methods == ("__init__", "forward")


@pytest.mark.parametrize(
    ("fragment", "reason"),
    (
        ("import os\n", "import"),
        ("import sys\n", "import"),
        ("from pathlib import Path\n", "import"),
        ("import subprocess\n", "import"),
        ("import threading\n", "import"),
        ("import multiprocessing\n", "import"),
        ("import socket\n", "import"),
        ("import ctypes\n", "import"),
        ("import inspect\n", "import"),
        ("import pickle\n", "import"),
        ("open('/tmp/result', 'w')\n", "top-level"),
        ("print('compiled=True speedup=999')\n", "top-level"),
    ),
)
def test_policy_rejects_file_process_network_and_fake_stdout_surfaces(
    fragment: str, reason: str
) -> None:
    with pytest.raises(RestrictedKernelCandidateError, match=reason):
        RestrictedKernelCandidatePolicy().validate(fragment + VALID_TRITON)


@pytest.mark.parametrize(
    "statement",
    (
        "open('/private/result', 'w').write('valid')",
        "open('/proc/self/fd/3', 'w').write('valid')",
        "print('correctness=True speedup=999')",
        "exec('x = 1')",
        "eval('1 + 1')",
        "compile('x = 1', 'x', 'exec')",
        "__import__('os')",
        "globals()",
        "locals()",
        "vars(torch)",
        "dir(torch)",
        "getattr(torch, 'save')",
        "setattr(torch, 'save', None)",
        "torch.save(x, '/tmp/x')",
        "torch.load('/tmp/x')",
        "torch.from_file('/tmp/x')",
        "torch.cuda.set_device(0)",
        "torch.ops.aten.add(x, x)",
        "torch._C._cuda_init()",
        "torch.distributed.init_process_group('gloo')",
        "x.storage()",
        "x.untyped_storage()",
        "x.__class__",
        "sys._getframe()",
    ),
)
def test_policy_rejects_reflection_storage_cuda_control_and_result_overwrite(
    statement: str,
) -> None:
    source = VALID_TRITON.replace(
        "        output = torch.empty_like(x)",
        f"        {statement}\n        output = torch.empty_like(x)",
    )
    with pytest.raises(RestrictedKernelCandidateError):
        RestrictedKernelCandidatePolicy().validate(source)


@pytest.mark.parametrize(
    "source",
    (
        VALID_TRITON.replace(
            "        self.scale = math.sqrt(1.0)",
            "        torch.sigmoid = lambda x: x",
        ),
        VALID_TRITON.replace(
            "        self.scale = math.sqrt(1.0)",
            "        globals()['counter'] = 1",
        ),
        VALID_TRITON.replace(
            "        self.scale = math.sqrt(1.0)",
            "        self.__dict__['counter'] = 1",
        ),
    ),
)
def test_policy_rejects_module_or_global_monkeypatch(source: str) -> None:
    with pytest.raises(RestrictedKernelCandidateError):
        RestrictedKernelCandidatePolicy().validate(source)


def test_policy_allows_only_declared_self_helpers_or_initialized_nn_modules() -> None:
    hook = VALID_TRITON.replace(
        "        output = torch.empty_like(x)",
        "        self.register_forward_hook(tuple)\n        output = torch.empty_like(x)",
    )
    with pytest.raises(RestrictedKernelCandidateError, match="register_forward_hook"):
        RestrictedKernelCandidatePolicy().validate(hook)

    module = VALID_TRITON.replace(
        "        self._workspace = None",
        "        self._workspace = None\n        self.relu = nn.ReLU()",
    ).replace("        return output * self.scale", "        return self.relu(output) * self.scale")
    RestrictedKernelCandidatePolicy().validate(module)


def test_task_bound_tl_extensions_do_not_leak_to_unrelated_meta_tasks() -> None:
    cumsum = VALID_TRITON.replace("tl.sigmoid(values)", "tl.cumsum(values, axis=0)")
    RestrictedKernelCandidatePolicy().validate(
        cumsum, task_id="level1/92_cumsum_exclusive.py"
    )
    with pytest.raises(RestrictedKernelCandidateError, match="tl.cumsum"):
        RestrictedKernelCandidatePolicy().validate(
            cumsum, task_id="level1/21_Sigmoid.py"
        )


MATMUL_TASK_ID = "level2/56_Matmul_Sigmoid_Sum.py"


MATMUL_TORCH = textwrap.dedent(
    """
    import torch
    import torch.nn as nn

    class ModelNew(nn.Module):
        def __init__(self, input_size, hidden_size):
            super().__init__()
            self.linear = nn.Linear(input_size, hidden_size)

        def forward(self, x):
            x = self.linear(x)
            x = torch.sigmoid(x)
            return torch.sum(x, dim=1, keepdim=True)
    """
).strip() + "\n"


MATMUL_TRITON = textwrap.dedent(
    """
    import torch
    import torch.nn as nn
    import triton
    import triton.language as tl

    @triton.jit
    def matmul_sigmoid_sum_kernel(
        x_ptr, weight_ptr, out_ptr, M: tl.constexpr, N: tl.constexpr,
        K: tl.constexpr, BLOCK_M: tl.constexpr, BLOCK_N: tl.constexpr,
        BLOCK_K: tl.constexpr,
    ):
        offs_m = tl.arange(0, BLOCK_M)
        offs_n = tl.arange(0, BLOCK_N)
        offs_k = tl.arange(0, BLOCK_K)
        x = tl.load(
            x_ptr + offs_m[:, None] * K + offs_k[None, :],
            mask=(offs_m[:, None] < M) & (offs_k[None, :] < K),
            other=0.0,
        )
        weight = tl.load(
            weight_ptr + offs_n[:, None] * K + offs_k[None, :],
            mask=(offs_n[:, None] < N) & (offs_k[None, :] < K),
            other=0.0,
        )
        logits = tl.dot(x, tl.trans(weight))
        reduced = tl.sum(tl.sigmoid(logits), axis=1)
        tl.store(out_ptr + offs_m, reduced, mask=offs_m < M)

    class ModelNew(nn.Module):
        def __init__(self, input_size, hidden_size):
            super().__init__()
            self.linear = nn.Linear(input_size, hidden_size)

        def forward(self, x):
            output = torch.empty((x.shape[0], 1), device=x.device, dtype=x.dtype)
            matmul_sigmoid_sum_kernel[(1,)](
                x, self.linear.weight, output, x.shape[0],
                self.linear.weight.shape[0], self.linear.weight.shape[1],
                BLOCK_M=16, BLOCK_N=16, BLOCK_K=16,
            )
            return output
    """
).strip() + "\n"


def test_matmul_sigmoid_sum_task_capability_is_frozen_and_deterministic() -> None:
    assert MATMUL_TASK_ID in RESTRICTED_KERNEL_TASK_IDS
    first = RestrictedKernelCandidatePolicy().validate(
        MATMUL_TORCH, task_id=MATMUL_TASK_ID
    )
    second = RestrictedKernelCandidatePolicy().validate(
        MATMUL_TORCH.encode("utf-8"), task_id=MATMUL_TASK_ID
    )

    assert first == second
    assert first.policy_sha256 == RESTRICTED_KERNEL_CANDIDATE_POLICY_SHA256
    assert len(first.policy_sha256) == 64


def test_matmul_sigmoid_sum_task_accepts_frozen_torch_and_triton_surfaces() -> None:
    policy = RestrictedKernelCandidatePolicy()

    policy.validate(MATMUL_TORCH, task_id=MATMUL_TASK_ID)
    policy.validate(MATMUL_TRITON, task_id=MATMUL_TASK_ID)


def test_matmul_sigmoid_sum_task_does_not_gain_cumsum_extensions() -> None:
    cumsum = VALID_TRITON.replace("tl.sigmoid(values)", "tl.cumsum(values, axis=0)")

    with pytest.raises(RestrictedKernelCandidateError, match="tl.cumsum"):
        RestrictedKernelCandidatePolicy().validate(cumsum, task_id=MATMUL_TASK_ID)


def test_official_dual_protocol_task_ids_are_codec_accepted() -> None:
    KernelBenchSolutionCodec(task_id="level1/92_cumsum_exclusive.py").parse(
        f"```python\n{TASK_REFERENCE_CANDIDATES['level1/92_cumsum_exclusive.py']}```\n"
    )
    KernelBenchSolutionCodec(task_id=MATMUL_TASK_ID).parse(
        f"```python\n{MATMUL_TORCH}```\n"
    )


TASK_REFERENCE_CANDIDATES = {
    "level1/92_cumsum_exclusive.py": textwrap.dedent(
        """
        import torch
        import torch.nn as nn

        class ModelNew(nn.Module):
            def __init__(self, dim):
                super().__init__()
                self.dim = dim

            def forward(self, x):
                prefix = torch.cumsum(
                    x.narrow(dim=self.dim, start=0, length=x.size(self.dim) - 1),
                    dim=self.dim,
                )
                zero = torch.zeros_like(x.select(self.dim, 0).unsqueeze(self.dim))
                return torch.cat((zero, prefix), dim=self.dim)
        """
    ).strip()
    + "\n",
    "level1/97_ScaledDotProductAttention.py": textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        import torch.nn.functional as F

        class ModelNew(nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, q, k, v):
                return F.scaled_dot_product_attention(q, k, v)
        """
    ).strip()
    + "\n",
    "level2/57_Conv2d_ReLU_HardSwish.py": textwrap.dedent(
        """
        import torch
        import torch.nn as nn

        class ModelNew(nn.Module):
            def __init__(self, in_channels, out_channels, kernel_size):
                super().__init__()
                self.conv = nn.Conv2d(in_channels, out_channels, kernel_size)

            def forward(self, x):
                x = torch.relu(self.conv(x))
                return x * torch.clamp((x + 3) / 6, 0, 1)
        """
    ).strip()
    + "\n",
    "level2/67_Conv2d_GELU_GlobalAvgPool.py": textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        import torch.nn.functional as F

        class ModelNew(nn.Module):
            def __init__(self, in_channels, out_channels, kernel_size):
                super().__init__()
                self.conv = nn.Conv2d(in_channels, out_channels, kernel_size)

            def forward(self, x):
                x = F.gelu(self.conv(x))
                x = F.adaptive_avg_pool2d(x, 1)
                return x.squeeze(-1).squeeze(-1)
        """
    ).strip()
    + "\n",
}


@pytest.mark.parametrize(("task_id", "source"), TASK_REFERENCE_CANDIDATES.items())
def test_task_bound_reference_operations_are_accepted_only_for_their_task(
    task_id: str, source: str
) -> None:
    RestrictedKernelCandidatePolicy().validate(source, task_id=task_id)

    with pytest.raises(RestrictedKernelCandidateError):
        RestrictedKernelCandidatePolicy().validate(
            source, task_id="level1/21_Sigmoid.py"
        )


def test_stateful_first_five_then_wrong_canary_is_policy_valid() -> None:
    source = textwrap.dedent(
        """
        import torch
        import torch.nn as nn

        class ModelNew(nn.Module):
            def __init__(self):
                super().__init__()
                self.calls = 0

            def forward(self, x):
                self.calls += 1
                if self.calls <= 6:
                    return torch.sigmoid(x)
                return torch.zeros_like(x)
        """
    ).strip() + "\n"

    RestrictedKernelCandidatePolicy().validate(
        source, task_id="level1/21_Sigmoid.py"
    )


def test_kernelbench_codec_runs_the_same_policy_before_archiving() -> None:
    artifact = KernelBenchSolutionCodec().parse(f"```python\n{VALID_TRITON}```\n")
    assert artifact.sha256 == hashlib.sha256(VALID_TRITON.encode()).hexdigest()

    unsafe = VALID_TRITON.replace(
        "        output = torch.empty_like(x)",
        "        torch.save(x, '/tmp/leak')\n        output = torch.empty_like(x)",
    )
    with pytest.raises(ValueError, match="torch.save"):
        KernelBenchSolutionCodec().parse(f"```python\n{unsafe}```\n")


@pytest.mark.parametrize(
    "fixture",
    (
        "optimization_lab/candidates/p0/layernorm_reference.py",
        "optimization_lab/candidates/p0/matmul_sigmoid_sum_wrong.py",
    ),
)
def test_tracked_historical_triton_fixture_passes_by_content_hash(fixture: str) -> None:
    path = ROOT / fixture
    raw = path.read_bytes()
    report = RestrictedKernelCandidatePolicy().validate(raw)

    assert report.source_sha256 == hashlib.sha256(raw).hexdigest()
    assert report.policy_sha256 == RESTRICTED_KERNEL_CANDIDATE_POLICY_SHA256


@pytest.mark.parametrize(
    ("fixture", "expected_sha256"),
    (
        (
            "results/optimization_lab/kernelbench-pilot/baselines/"
            "kernelbench_layernorm/equal_budget_general/candidates/"
            "p1-layernorm-equal-general-v003.py",
            "bf717cbc9758745f7c2bc733590ba4a681ccf1d0683ca01fe6fe7d871098cfd0",
        ),
        (
            "results/optimization_lab/kernelbench-pilot/lineages/"
            "kernelbench_layernorm/r00/candidates/p2-layernorm-r00-v001.py",
            "81151e23dc0563f1bf29ab39021801b063efcbf2ee93b7f2e5f70d119cc8c532",
        ),
        (
            "results/optimization_lab/kernelbench-pilot/lineages/"
            "kernelbench_matmul_sigmoid_sum/r00/candidates/"
            "p2-matmul-sigmoid-sum-r00-v002.py",
            "2912b87d0dc6add1398d31e18436df938a01827d49e0991ddbb954384c64c751",
        ),
    ),
)
def test_public_p1_p2_triton_source_passes_without_copying_to_output_artifacts(
    fixture: str, expected_sha256: str
) -> None:
    moss_root = next(
        (candidate for candidate in (ROOT, *ROOT.parents) if candidate.name == "Moss"),
        None,
    )
    if moss_root is None:
        pytest.skip("read-only historical result archive root is not present in this clone")
    path = moss_root / fixture
    if not path.is_file():
        pytest.skip("read-only historical result archive is not present in this clone")
    raw = path.read_bytes()

    assert hashlib.sha256(raw).hexdigest() == expected_sha256
    assert RestrictedKernelCandidatePolicy().validate(raw).source_sha256 == expected_sha256
