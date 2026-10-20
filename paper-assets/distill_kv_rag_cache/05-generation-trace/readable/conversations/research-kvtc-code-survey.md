# research kvtc code survey

**distill kv rag cache** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 0
- **Tool calls:** 23
- **Original source:** `logs/chats/worker_research_kvtc-code-survey_20260514T042154.jsonl`
- **Structured JSON:** [`64ecf5e173bf83bf0b98.json`](../../sessions/64/64ecf5e173bf83bf0b98.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

47 recorded events

### Tool call

_source line 1 · 2026-05-14T04:28:51.272480+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /tmp/kvtc-survey && git clone https://github.com/OnlyTerp/kvtc.git /tmp/kvtc-survey/kvtc 2>&1",
  "timeout": "60000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /tmp/kvtc-survey && git clone https://github.com/OnlyTerp/kvtc.git /tmp/kvtc-survey/kvtc 2>&1",
    "timeout": "60000"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T04:28:51.272835+00:00_

Cloning into '/tmp/kvtc-survey/kvtc'...

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T04:28:51.273078+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /tmp/kvtc-survey/kvtc -type f | head -100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "Bash",
  "tool_args": {
    "command": "find /tmp/kvtc-survey/kvtc -type f | head -100"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T04:28:51.273251+00:00_

/tmp/kvtc-survey/kvtc/wsl_proof.sh
/tmp/kvtc-survey/kvtc/src/vllm_triton.py
/tmp/kvtc-survey/kvtc/src/vllm_backend.py
/tmp/kvtc-survey/kvtc/src/triton_kernels.py
/tmp/kvtc-survey/kvtc/src/test_real_model.py
/tmp/kvtc-survey/kvtc/src/test_kvtc.py
/tmp/kvtc-survey/kvtc/src/quantize.py
/tmp/kvtc-survey/kvtc/src/pipeline_fast.py
/tmp/kvtc-survey/kvtc/src/pipeline.py
/tmp/kvtc-survey/kvtc/src/pca.py
/tmp/kvtc-survey/kvtc/src/gpu_ops.py
/tmp/kvtc-survey/kvtc/src/fused_ops.py
/tmp/kvtc-survey/kvtc/src/entropy.py
/tmp/kvtc-survey/kvtc/src/common.py
/tmp/kvtc-survey/kvtc/src/calibrate_vllm.py
/tmp/kvtc-survey/kvtc/src/calibrate.py
/tmp/kvtc-survey/kvtc/src/cache.py
/tmp/kvtc-survey/kvtc/src/benchmark_gpu.py
/tmp/kvtc-survey/kvtc/src/ans_entropy.py
/tmp/kvtc-survey/kvtc/src/adaptive_budget.py
/tmp/kvtc-survey/kvtc/src/__init__.py
/tmp/kvtc-survey/kvtc/setup.py
/tmp/kvtc-survey/kvtc/run_on_5090.bat
/tmp/kvtc-survey/kvtc/run_5090_benchmark.bat
/tmp/kvtc-survey/kvtc/proof.py
/tmp/kvtc-survey/kvtc/notebooks/kvtc_demo.ipynb
/tmp/kvtc-survey/kvtc/notebooks/demo.ipynb
/tmp/kvtc-survey/kvtc/deploy/run.sh
/tmp/kvtc-survey/kvtc/deploy/Dockerfile
/tmp/kvtc-survey/kvtc/cuda/test_kvtc_kernels.cu
/tmp/kvtc-survey/kvtc/cuda/patch_setrows.py
/tmp/kvtc-survey/kvtc/cuda/patch_kvtc_real_compression.py
/tmp/kvtc-survey/kvtc/cuda/patch_fa_remap.py
/tmp/kvtc-survey/kvtc/cuda/patch_fa_dispatch.py
/tmp/kvtc-survey/kvtc/cuda/kvtc_kernels.cu
/tmp/kvtc-survey/kvtc/cuda/kvtc.h
/tmp/kvtc-survey/kvtc/cuda/integrate_llamacpp.py
/tmp/kvtc-survey/kvtc/cuda/CMakeLists.txt
/tmp/kvtc-survey/kvtc/benchmarks/results_v4.json
/tmp/kvtc-survey/kvtc/benchmarks/results_v3.json
/tmp/kvtc-survey/kvtc/benchmarks/results_v2.json
/tmp/kvtc-survey/kvtc/benchmarks/results_v1.json
/tmp/kvtc-survey/kvtc/benchmarks/benchmark_v4.py
/tmp/kvtc-survey/kvtc/benchmarks/benchmark_v3.py
/tmp/kvtc-survey/kvtc/benchmarks/benchmark_v2.py
/tmp/kvtc-survey/kvtc/benchmarks/benchmark_v1.py
/tmp/kvtc-survey/kvtc/benchmarks/benchmark_perplexity
…[truncated 2389 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T04:28:51.273426+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /tmp/kvtc-survey/kvtc/README.md 2>/dev/null || echo \"NO README\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /tmp/kvtc-survey/kvtc/README.md 2>/dev/null || echo \"NO README\""
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T04:28:51.273772+00:00_

&lt;div align="center">

&lt;picture>
  &lt;source media="(prefers-color-scheme: dark)" srcset="assets/banner.svg">
  &lt;source media="(prefers-color-scheme: light)" srcset="assets/banner.svg">
  &lt;img alt="KVTC — KV-Cache Tensor Compression" src="assets/banner.svg" width="100%">
&lt;/picture>

&lt;br>

**The first open-source implementation of NVIDIA's KVTC ([arXiv 2511.01815](https://arxiv.org/abs/2511.01815), ICLR 2026)**

Compress LLM KV caches **6-9x** with negligible quality loss. Run **2M+ token context** on a single RTX 5090.

&lt;br>

[![Tests](https://github.com/OnlyTerp/kvtc/actions/workflows/test.yml/badge.svg)](https://github.com/OnlyTerp/kvtc/actions/workflows/test.yml)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OnlyTerp/kvtc/blob/master/notebooks/kvtc_demo.ipynb)
[![arXiv](https://img.shields.io/badge/arXiv-2511.01815-b31b1b.svg)](https://arxiv.org/abs/2511.01815)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.10%2B-ee4c2c.svg)](https://pytorch.org/)
[![CUDA](https://img.shields.io/badge/CUDA-12.x-76b900.svg)](https://developer.nvidia.com/cuda-toolkit)

[Quick Start](#-quick-start) · [How It Works](#-how-it-works) · [Benchmarks](#-benchmarks) · [Landscape](#-the-kv-cache-compression-landscape-april-2026) · [Roadmap](#-roadmap) · [Contributing](#-contributing)

&lt;/div>

---

## Why KV Cache Compression Matters

Every token an LLM generates stores key-value pairs across every attention layer. This **KV cache** grows linearly with context length and is now the dominant memory bottleneck in LLM inference — often exceeding the model weights themselves.

```
Model            Context    KV Cache (FP16)    GPU Required
Llama-3.1-8B     128K       16.7 GB            > 1x A100 80GB
Qwen3.5-27B      128K       ~48 GB       
…[truncated 26713 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T04:28:51.274036+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/kvtc-survey/kvtc/src/quantize.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/kvtc-survey/kvtc/src/quantize.py"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T04:28:51.274217+00:00_

1	"""Quantization utilities for KVTC."""
2	
3	from __future__ import annotations
4	
5	from typing import List
6	
7	import torch
8	
9	from .common import QuantizationParams
10	
11	
12	def _component_groups(eigenvalues: torch.Tensor, group_size: int) -> List[torch.Tensor]:
13	    return [eigenvalues[i : i + group_size] for i in range(0, eigenvalues.numel(), group_size)]
14	
15	
16	def dp_bit_allocation(
17	    eigenvalues: torch.Tensor,
18	    bit_budget: int,
19	    max_bits: int = 16,
20	    group_size: int = 1,
21	) -> torch.Tensor:
22	    """Allocate per-component bit widths with dynamic programming."""
23	
24	    values = eigenvalues.detach().to(torch.float64).flatten()
25	    groups = _component_groups(values, group_size)
26	    max_budget = max(int(bit_budget), 0)
27	    num_groups = len(groups)
28	    inf = float("inf")
29	    dp = [[inf] * (max_budget + 1) for _ in range(num_groups + 1)]
30	    back = [[0] * (max_budget + 1) for _ in range(num_groups + 1)]
31	    dp[0][0] = 0.0
32	    for idx, group in enumerate(groups, start=1):
33	        variance = float(group.sum().item())
34	        width = group.numel()
35	        for used in range(max_budget + 1):
36	            if dp[idx - 1][used] == inf:
37	                continue
38	            for bits in range(0, max_bits + 1):
39	                cost = used + bits * width
40	                if cost > max_budget:
41	                    continue
42	                error = variance if bits == 0 else variance / (4 ** bits)
43	                candidate = dp[idx - 1][used] + error
44	                if candidate < dp[idx][cost]:
45	                    dp[idx][cost] = candidate
46	                    back[idx][cost] = bits
47	    best_budget = min(range(max_budget + 1), key=lambda budget: dp[num_groups][budget])
48	    widths = torch.zeros(values.numel(), dtype=torch.int64)
49	    remaining = best_budget
50	    for idx in range(num_groups, 0, -1):
51	        bits = back[idx][remaining]
52	        group = groups[idx - 
…[truncated 2015 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T04:28:51.274366+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/kvtc-survey/kvtc/src/pca.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/kvtc-survey/kvtc/src/pca.py"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T04:28:51.274590+00:00_

1	"""PCA and RoPE utilities for KVTC."""
2	
3	from __future__ import annotations
4	
5	from collections import defaultdict
6	from dataclasses import dataclass, field
7	from typing import Dict, List, Optional, Tuple
8	
9	import torch
10	import math
11	
12	from .common import CalibrationData, CalibrationKey, PCAEntry
13	from .quantize import dp_bit_allocation
14	
15	
16	def pca_transform(centered: torch.Tensor, eigenvectors: torch.Tensor) -> torch.Tensor:
17	    """Project centered data into PCA space.
18	    
19	    Args:
20	        centered: [num_rows, dim] centered data (mean already subtracted)
21	        eigenvectors: [dim, dim] or [k, dim] PCA basis (rows are eigenvectors)
22	    
23	    Returns:
24	        [num_rows, k] PCA coefficients
25	    """
26	    # eigenvectors from SVD: Vh has shape [k, dim], each row is an eigenvector
27	    # projection = centered @ Vh.T
28	    return centered @ eigenvectors.T
29	
30	
31	def pca_inverse(pca_values: torch.Tensor, eigenvectors: torch.Tensor) -> torch.Tensor:
32	    """Reconstruct from PCA space back to original space.
33	    
34	    Args:
35	        pca_values: [num_rows, k] PCA coefficients
36	        eigenvectors: [k, dim] PCA basis
37	    
38	    Returns:
39	        [num_rows, dim] reconstructed data (without mean)
40	    """
41	    return pca_values @ eigenvectors
42	
43	
44	def _rotary_embedding(positions: torch.Tensor, dim: int, theta: float = 10000.0) -> torch.Tensor:
45	    """Compute rotary position embeddings (cos, sin).
46	    
47	    Args:
48	        positions: [seq_len] position indices
49	        dim: head dimension
50	        theta: RoPE base frequency
51	    
52	    Returns:
53	        (cos, sin) each of shape [seq_len, dim//2]
54	    """
55	    half_dim = dim // 2
56	    freqs = 1.0 / (theta ** (torch.arange(0, half_dim, dtype=torch.float32, device=positions.device) / half_dim))
57	    # [seq_len, half_dim]
58	    angles = positions.float().unsqueeze(1) * freqs.unsqueeze(0)
59	    return torch.cos(angle
…[truncated 9394 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T04:28:51.274749+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/kvtc-survey/kvtc/src/common.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/kvtc-survey/kvtc/src/common.py"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T04:28:51.274917+00:00_

1	"""Shared data structures for KVTC."""
2	
3	from __future__ import annotations
4	
5	from dataclasses import dataclass, field
6	from typing import Dict, List, Tuple
7	
8	import torch
9	
10	
11	CalibrationKey = Tuple[int, int, str]
12	
13	
14	@dataclass
15	class PCAEntry:
16	    """PCA statistics for one layer, head-group, and tensor kind."""
17	
18	    eigenvectors: torch.Tensor
19	    eigenvalues: torch.Tensor
20	    mean: torch.Tensor
21	    head_indices: List[int]
22	    kind: str
23	    bit_budget: int
24	    pca_mins: torch.Tensor | None = None
25	    pca_maxs: torch.Tensor | None = None
26	    bit_widths: torch.Tensor | None = None
27	    scales: torch.Tensor | None = None
28	    zero_points: torch.Tensor | None = None
29	
30	
31	@dataclass
32	class CalibrationData:
33	    """Serialized calibration artifact consumed by the compressor."""
34	
35	    entries: Dict[CalibrationKey, PCAEntry]
36	    head_group_size: int
37	    rope_theta: float = 10000.0
38	    sink_tokens: int = 4
39	    window_tokens: int = 128
40	
41	
42	@dataclass
43	class QuantizationParams:
44	    """Uniform quantization parameters per PCA component."""
45	
46	    bit_widths: torch.Tensor
47	    scales: torch.Tensor
48	    zero_points: torch.Tensor
49	    mins: torch.Tensor
50	
51	
52	@dataclass
53	class CompressedSection:
54	    """Compressed payload for one layer/group/kind middle region."""
55	
56	    layer_idx: int
57	    group_idx: int
58	    kind: str
59	    compressed_bytes: bytes
60	    packed_size: int
61	    lengths: List[int]
62	    num_rows: int
63	    group_heads: int
64	    bit_widths: List[int]
65	    scales: List[float]
66	    zero_points: List[float]
67	    mins: List[float]
68	
69	
70	@dataclass
71	class CompressionMetadata:
72	    """Metadata required for reconstruction."""
73	
74	    positions_middle: List[int]
75	    original_shape: Tuple[int, int, int, int]
76	    sink_len: int
77	    middle_len: int
78	    window_len: int
79	    compression_ratio: float
80	
81	
82	@dat
…[truncated 315 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T04:28:51.275078+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/kvtc-survey/kvtc/src/entropy.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/kvtc-survey/kvtc/src/entropy.py"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T04:28:51.275240+00:00_

1	"""Entropy coding for KVTC — DEFLATE (zlib) based compression/decompression."""
2	
3	from __future__ import annotations
4	
5	from typing import List, Tuple
6	
7	import zlib
8	
9	import torch
10	
11	
12	def compress(packed_bytes: bytes, level: int = 6) -> Tuple[bytes, float]:
13	    """Compress packed bytes using zlib DEFLATE.
14	    
15	    Returns:
16	        (compressed_bytes, compression_ratio)
17	    """
18	    if not packed_bytes:
19	        return b"", 1.0
20	    
21	    compressed = zlib.compress(packed_bytes, level)
22	    ratio = len(packed_bytes) / max(len(compressed), 1)
23	    return compressed, ratio
24	
25	
26	def decompress(compressed_bytes: bytes, original_size: int) -> bytes:
27	    """Decompress zlib-compressed bytes.
28	    
29	    Args:
30	        compressed_bytes: The zlib-compressed data
31	        original_size: Expected size of decompressed data (for validation)
32	    
33	    Returns:
34	        Decompressed bytes
35	    """
36	    if not compressed_bytes:
37	        return b""
38	    
39	    decompressed = zlib.decompress(compressed_bytes)
40	    if len(decompressed) != original_size:
41	        raise ValueError(
42	            f"Decompressed size {len(decompressed)} != expected {original_size}"
43	        )
44	    return decompressed
45	
46	
47	def pack_bits(
48	    indices_list: List[torch.Tensor],
49	    bit_widths: List[int],
50	) -> bytes:
51	    """Pack a list of quantized index tensors into a byte stream.
52	    
53	    Each tensor in indices_list corresponds to one PCA component.
54	    Components are packed sequentially: all rows of comp 0, then comp 1, etc.
55	    
56	    Args:
57	        indices_list: List of [num_rows] int64 tensors, one per component
58	        bit_widths: Bit width for each component
59	    
60	    Returns:
61	        Packed byte stream
62	    """
63	    accumulator = 0
64	    bits_in_acc = 0
65	    output = bytearray()
66	    
67	    for comp_idx, (indices, width) in enumerate(zip(indices_list, bit_widths))
…[truncated 2054 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T04:28:51.275389+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/kvtc-survey/kvtc/src/pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/kvtc-survey/kvtc/src/pipeline.py"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T04:28:51.275562+00:00_

1	"""Full KVTC compression pipeline."""
2	
3	from __future__ import annotations
4	
5	from typing import Dict, List
6	
7	import torch
8	
9	from .common import CalibrationData, CompressedKVCache, CompressedSection, CompressionMetadata
10	from .entropy import compress as entropy_compress
11	from .entropy import decompress as entropy_decompress
12	from .entropy import pack_bits, unpack_bits
13	from .pca import apply_rope, apply_rope_inverse, pca_inverse, pca_transform
14	from .quantize import compute_quant_params, dp_bit_allocation, uniform_dequantize, uniform_quantize
15	
16	
17	class KVTCCompressor:
18	    """Compress and decompress KV caches with KVTC."""
19	
20	    def __init__(self, calibration_data: CalibrationData) -> None:
21	        self.calibration_data = calibration_data
22	
23	    def compress(self, kv_cache: Dict[str, torch.Tensor], positions: torch.Tensor) -> CompressedKVCache:
24	        """Run the full KVTC pipeline."""
25	
26	        keys = kv_cache["keys"]
27	        values = kv_cache["values"]
28	        if keys.shape != values.shape:
29	            raise ValueError("Keys and values must have the same shape.")
30	        if keys.dim() != 4:
31	            raise ValueError("Expected KV tensors with shape [layers, tokens, heads, dim].")
32	        layers, tokens, heads, dim = keys.shape
33	        sink_len = min(self.calibration_data.sink_tokens, tokens)
34	        residual = max(tokens - sink_len, 0)
35	        window_len = min(self.calibration_data.window_tokens, residual)
36	        middle_len = max(tokens - sink_len - window_len, 0)
37	        middle_positions = positions[sink_len : sink_len + middle_len]
38	        sinks = {
39	            "keys": keys[:, :sink_len].clone(),
40	            "values": values[:, :sink_len].clone(),
41	        }
42	        window = {
43	            "keys": keys[:, tokens - window_len :].clone() if window_len else keys[:, 0:0].clone(),
44	            "values": values[:, tokens - window_len :].clone() if window_len else 
…[truncated 6880 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T04:28:51.275716+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/kvtc-survey/kvtc/src/pipeline_fast.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/kvtc-survey/kvtc/src/pipeline_fast.py"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T04:28:51.275942+00:00_

1	"""GPU-accelerated KVTC compression pipeline."""
2	
3	from __future__ import annotations
4	
5	import time
6	from typing import Dict, List, Optional
7	
8	import torch
9	
10	from .common import CalibrationData, CompressedKVCache, CompressedSection, CompressionMetadata
11	from .entropy import compress as entropy_compress
12	from .entropy import decompress as entropy_decompress
13	from .entropy import unpack_bits
14	from .gpu_ops import (
15	    batch_dequantize,
16	    batch_quantize,
17	    fast_pack_bits,
18	    fast_unpack_dequantize,
19	    greedy_bit_allocation,
20	    vectorized_quant_params,
21	)
22	from .pca import apply_rope, apply_rope_inverse, pca_inverse, pca_transform
23	
24	
25	class KVTCCompressorFast:
26	    """GPU-accelerated KVTC compressor. Drop-in replacement for KVTCCompressor."""
27	
28	    def __init__(self, calibration_data: CalibrationData, device: str = "cpu") -> None:
29	        self.calibration_data = calibration_data
30	        self.device = device
31	        self._timing: Dict[str, float] = {}
32	
33	    @property
34	    def timing(self) -> Dict[str, float]:
35	        return self._timing
36	
37	    def compress(self, kv_cache: Dict[str, torch.Tensor], positions: torch.Tensor) -> CompressedKVCache:
38	        """Run the full KVTC pipeline with GPU acceleration."""
39	        self._timing = {}
40	        t_total = time.perf_counter()
41	
42	        keys = kv_cache["keys"]
43	        values = kv_cache["values"]
44	        if keys.shape != values.shape:
45	            raise ValueError("Keys and values must have the same shape.")
46	        if keys.dim() != 4:
47	            raise ValueError("Expected KV tensors with shape [layers, tokens, heads, dim].")
48	
49	        layers, tokens, heads, dim = keys.shape
50	        sink_len = min(self.calibration_data.sink_tokens, tokens)
51	        residual = max(tokens - sink_len, 0)
52	        window_len = min(self.calibration_data.window_tokens, residual)
53	        middle_len = max(tokens - sink_len
…[truncated 9094 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T04:28:51.276106+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/kvtc-survey/kvtc/src/adaptive_budget.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/kvtc-survey/kvtc/src/adaptive_budget.py"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T04:28:51.276292+00:00_

1	"""Per-layer, per-kind adaptive bit budget allocation for KVTC.
2	
3	Instead of uniform bits across all layers, allocate more bits to
4	high-entropy layers and fewer to low-entropy ones. The total bit
5	budget is preserved — bits are redistributed, not added.
6	
7	Key insight: different layers have wildly different compressibility.
8	Layer 27 keys might compress at 0.5 bits while layer 25 values need 5 bits.
9	Giving them the same budget wastes bits on easy layers and starves hard ones.
10	"""
11	
12	from __future__ import annotations
13	
14	import numpy as np
15	import torch
16	from typing import Dict, List, Tuple
17	
18	from common import CalibrationData, PCAEntry
19	
20	
21	def compute_layer_difficulty(calibration: CalibrationData) -> Tuple[np.ndarray, np.ndarray]:
22	    """Compute per-layer compression difficulty from calibration eigenvalues.
23	    
24	    Difficulty is based on the "flatness" of the eigenvalue spectrum.
25	    A flat spectrum (all eigenvalues similar) = high entropy = hard to compress.
26	    A steep spectrum (few dominant eigenvalues) = low entropy = easy to compress.
27	    
28	    Returns:
29	        (key_difficulty, val_difficulty) arrays of shape [num_layers]
30	        Normalized so mean = 1.0. Values > 1 are harder than average.
31	    """
32	    # Collect eigenvalue spectra per layer
33	    key_entropies = []
34	    val_entropies = []
35	    
36	    # Find number of layers
37	    max_layer = max(k[0] for k in calibration.entries.keys()) + 1
38	    
39	    for layer_idx in range(max_layer):
40	        for kind, collector in [("keys", key_entropies), ("values", val_entropies)]:
41	            # Find entries for this layer+kind
42	            entries = [(k, v) for k, v in calibration.entries.items() 
43	                      if k[0] == layer_idx and k[2] == kind]
44	            
45	            if not entries:
46	                collector.append(1.0)
47	                continue
48	            
49	            # Average eigenvalue entropy
…[truncated 6680 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T04:28:51.276446+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/kvtc-survey/kvtc/setup.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/kvtc-survey/kvtc/setup.py"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T04:28:51.276573+00:00_

1	from setuptools import find_packages, setup
2	
3	
4	setup(
5	    name="kvtc",
6	    version="0.1.0",
7	    description="First open-source implementation of KV Cache Transform Coding (KVTC).",
8	    packages=find_packages(),
9	    py_modules=[],
10	    install_requires=["torch", "numpy", "transformers"],
11	    extras_require={"dev": ["pytest"]},
12	    python_requires=">=3.10",
13	)
14	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T04:28:51.276716+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/kvtc-survey/kvtc/src/gpu_ops.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/kvtc-survey/kvtc/src/gpu_ops.py"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T04:28:51.276956+00:00_

1	"""GPU-optimized KVTC operations — vectorized PyTorch, no Python loops."""
2	
3	from __future__ import annotations
4	
5	import torch
6	
7	from common import QuantizationParams
8	
9	
10	def greedy_bit_allocation(
11	    eigenvalues: torch.Tensor,
12	    bit_budget: int,
13	    max_bits: int = 16,
14	) -> torch.Tensor:
15	    """Vectorized greedy bit allocation via precomputed gain sorting.
16	    
17	    Minimizes sum(λᵢ / 4^bᵢ) subject to sum(bᵢ) ≤ B.
18	    
19	    gain(i, b) = λᵢ × 3 / 4^b = marginal MSE reduction from assigning
20	    the b-th bit to component i. We precompute ALL gains, sort them,
21	    and greedily take the top B. Each entry (i, b) is only valid if
22	    all entries (i, 1), (i, 2), ..., (i, b-1) are also taken.
23	    Since gains are monotonically decreasing in b for each i, the
24	    sorted order naturally respects this constraint.
25	    """
26	    d = eigenvalues.numel()
27	    ev = eigenvalues.detach().to(torch.float64).flatten()
28	    budget = max(int(bit_budget), 0)
29	    
30	    if budget == 0 or d == 0:
31	        return torch.zeros(d, dtype=torch.int64)
32	    
33	    # gains_matrix[i, b-1] = λᵢ × 3 / 4^b (gain of b-th bit on component i)
34	    bit_levels = torch.arange(1, max_bits + 1, dtype=torch.float64, device=ev.device)  # [max_bits]
35	    gains_matrix = ev.unsqueeze(1) * 3.0 / (4.0 ** bit_levels.unsqueeze(0))  # [d, max_bits]
36	    
37	    flat_gains = gains_matrix.flatten()  # [d * max_bits]
38	    total_slots = flat_gains.numel()
39	    
40	    if budget >= total_slots:
41	        return torch.full((d,), max_bits, dtype=torch.int64)
42	    
43	    # Take the top `budget` gains
44	    _, top_indices = torch.topk(flat_gains, min(budget, total_slots))
45	    
46	    # Each index maps to (component, bit_level):
47	    # index = component * max_bits + (bit_level - 1)
48	    # For each component, the NUMBER of its entries in top-B = its bit allocation
49	    # This works because gains are monotonically decreasing in bit_lev
…[truncated 8761 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T04:28:51.277157+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/kvtc-survey/kvtc/src/ans_entropy.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/kvtc-survey/kvtc/src/ans_entropy.py"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T04:28:51.277368+00:00_

1	"""ANS (Asymmetric Numeral Systems) entropy coding for KVTC.
2	
3	Replaces zlib/LZMA with tANS (tabled ANS) for 10-20% better compression
4	on quantized KV cache data. Falls back to zlib if ANS isn't available.
5	
6	ANS is what NVIDIA's nvCOMP uses internally. This is a pure-Python
7	implementation for correctness verification before porting to CUDA.
8	"""
9	
10	from __future__ import annotations
11	
12	import struct
13	import zlib
14	import lzma
15	from collections import Counter
16	from typing import Tuple
17	
18	import torch
19	
20	
21	# --- rANS (range ANS) implementation ---
22	# rANS is simpler than tANS and gives identical compression ratios.
23	# Perfect for a reference implementation.
24	
25	RANS_PRECISION = 16  # bits of precision for probability table
26	RANS_LOWER = 1 << 23  # renormalization threshold
27	RANS_UPPER = 1 << 31
28	
29	
30	def _build_freq_table(data: bytes, precision: int = RANS_PRECISION) -> Tuple[list, list, int]:
31	    """Build frequency table for rANS from byte data.
32	    
33	    Returns:
34	        (cumulative_freq, freq, total) where total = 1 << precision
35	    """
36	    total = 1 << precision
37	    counts = Counter(data)
38	    n = len(data)
39	    
40	    if n == 0:
41	        return [0] * 257, [0] * 256, total
42	    
43	    # Assign frequencies proportional to counts, minimum 1 for present symbols
44	    freq = [0] * 256
45	    present = [s for s in range(256) if counts[s] > 0]
46	    
47	    if not present:
48	        return [0] * 257, [0] * 256, total
49	    
50	    # Reserve 1 slot per present symbol, distribute rest proportionally
51	    remaining = total - len(present)
52	    for s in present:
53	        freq[s] = 1 + int(counts[s] / n * remaining)
54	    
55	    # Adjust to sum exactly to total
56	    current_sum = sum(freq)
57	    diff = total - current_sum
58	    # Add/subtract from the most frequent symbol
59	    most_freq = max(present, key=lambda s: freq[s])
60	    freq[most_freq] += diff
61	    
62	    # Build
…[truncated 5633 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T04:28:51.277568+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/kvtc-survey/kvtc/src/fused_ops.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/kvtc-survey/kvtc/src/fused_ops.py"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T04:28:51.277753+00:00_

1	"""Fused GPU operations for KVTC — single-kernel PCA + Quantize + Pack.
2	
3	Combines three separate GPU calls into one fused operation per head group,
4	eliminating intermediate tensor allocations and kernel launch overhead.
5	"""
6	
7	from __future__ import annotations
8	
9	import torch
10	from typing import Tuple
11	
12	from common import PCAEntry, QuantizationParams
13	
14	
15	def fused_pca_quantize(
16	    data: torch.Tensor,
17	    eigenvectors: torch.Tensor,
18	    mean: torch.Tensor,
19	    bit_widths: torch.Tensor,
20	    device: str = "cuda",
21	) -> Tuple[torch.Tensor, QuantizationParams]:
22	    """Fused PCA transform + quantization in a single GPU pass.
23	    
24	    Instead of:
25	        1. centered = data - mean              (GPU kernel 1)
26	        2. pca_values = centered @ Vh.T        (GPU kernel 2, big matmul)
27	        3. compute quant params                (GPU kernel 3)
28	        4. indices = quantize(pca_values)      (GPU kernel 4)
29	    
30	    We do:
31	        1. pca_quantized = fused_kernel(data, mean, Vh, bit_widths)  (1 kernel)
32	    
33	    The key insight: we don't need to materialize the full float32 PCA values
34	    if we're just going to quantize them immediately. We can compute PCA and
35	    quantize in the same memory pass.
36	    
37	    Args:
38	        data: [num_rows, dim] float32 KV cache vectors
39	        eigenvectors: [dim, dim] PCA basis (Vh from SVD)
40	        mean: [dim] PCA mean
41	        bit_widths: [dim] bits per component
42	    
43	    Returns:
44	        (indices, quant_params) where indices is [num_rows, dim] int64
45	    """
46	    data = data.to(device=device, dtype=torch.float32)
47	    ev = eigenvectors.to(device=device, dtype=torch.float32)
48	    mn = mean.to(device=device, dtype=torch.float32)
49	    bw = bit_widths.to(device=device, dtype=torch.float32)
50	    
51	    # Fused step 1+2: center and project in one matmul
52	    # pca_values = (data - mean) @ Vh.T
53	    pca_values = (data - mn) 
…[truncated 4893 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T04:28:51.277919+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/kvtc-survey/kvtc/src/calibrate.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/kvtc-survey/kvtc/src/calibrate.py"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T04:28:51.278073+00:00_

1	"""Calibration utilities for KVTC."""
2	
3	from __future__ import annotations
4	
5	from dataclasses import dataclass, field
6	from pathlib import Path
7	from typing import Sequence
8	
9	import torch
10	
11	from .common import CalibrationData
12	from .pca import PCACalibrator
13	
14	
15	@dataclass
16	class KVTCCalibrator:
17	    """Collect model KV samples and compute calibration artifacts."""
18	
19	    head_group_size: int = 1
20	    rope_theta: float = 10000.0
21	    samples_collected: int = 0
22	    _pca: PCACalibrator = field(init=False)
23	
24	    def __post_init__(self) -> None:
25	        self._pca = PCACalibrator(head_group_size=self.head_group_size, rope_theta=self.rope_theta)
26	
27	    def collect_samples(
28	        self,
29	        model,
30	        tokenizer,
31	        texts: Sequence[str],
32	        max_samples: int = 100,
33	    ) -> None:
34	        """Collect KV cache samples from a causal LM."""
35	
36	        device = next(model.parameters()).device
37	        for text in texts[:max_samples]:
38	            encoded = tokenizer(text, return_tensors="pt")
39	            encoded = {key: value.to(device) for key, value in encoded.items()}
40	            with torch.no_grad():
41	                outputs = model(**encoded, use_cache=True)
42	            positions = torch.arange(encoded["input_ids"].shape[1], device=device)
43	            past = outputs.past_key_values
44	            # Handle DynamicCache (.layers), legacy DynamicCache (.key_cache), and tuple formats
45	            if hasattr(past, 'layers'):
46	                # Newest transformers DynamicCache with .layers[i].keys/.values
47	                for layer_idx, layer in enumerate(past.layers):
48	                    self._pca.collect(layer_idx, "keys", layer.keys[0].transpose(0, 1).detach().cpu(), positions.cpu())
49	                    self._pca.collect(layer_idx, "values", layer.values[0].transpose(0, 1).detach().cpu())
50	            elif hasattr(past, 'key_cache'):
51	               
…[truncated 1402 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T04:28:51.278221+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/kvtc-survey/kvtc/benchmarks/results_v4.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/kvtc-survey/kvtc/benchmarks/results_v4.json"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T04:28:51.278542+00:00_

1	{
2	  "model": "Qwen/Qwen2.5-7B-Instruct",
3	  "ts": "2026-03-31T18:28:25",
4	  "results": [
5	    {
6	      "name": "K2V4-baseline",
7	      "key_bits": 2,
8	      "value_bits": 4,
9	      "avg_bits": 3.0,
10	      "compression_ratio": 5.948289847207098,
11	      "cosine_keys": 0.9968018770217896,
12	      "cosine_values": 0.9971820116043091,
13	      "nmse_keys": 0.007411877783159962,
14	      "nmse_values": 0.00570027717940544,
15	      "max_error": 8.437519454956055,
16	      "compress_ms": 286.76022000727244,
17	      "decompress_ms": 5536.219559999881,
18	      "optimizations": "baseline",
19	      "layer_cosine_keys": [
20	        0.9994092226028443,
21	        0.9907387137413025,
22	        0.9666800737380982,
23	        0.9872852206230164,
24	        0.9198486685752869,
25	        0.9284656405448913,
26	        0.935473370552063,
27	        0.9324450135231018,
28	        0.911102032661438,
29	        0.9281075239181519,
30	        0.9276631355285645,
31	        0.9173038482666016,
32	        0.9278949499130249,
33	        0.9669374227523804,
34	        0.9241477608680725,
35	        0.9339734315872192,
36	        0.9323524117469788,
37	        0.9228281140327453,
38	        0.9213339447975158,
39	        0.965771222114563,
40	        0.9166692495346069,
41	        0.9276591420173645,
42	        0.9298889875411988,
43	        0.9274226903915406,
44	        0.928615415096283,
45	        0.9278865337371827,
46	        0.9278494238853454,
47	        0.9998392224311828
48	      ],
49	      "layer_cosine_values": [
50	        0.9978531241416931,
51	        0.9979618906974792,
52	        0.9978267788887024,
53	        0.9974461197853088,
54	        0.9980403780937195,
55	        0.9978867173194885,
56	        0.9978332281112671,
57	        0.9970708370208741,
58	        0.997931182384491,
59	        0.9972416043281556,
60	        0.9978246927261353,
61	        0.9979458212852478,
62	        0.9977609276771545,
63	        0.9975575804710388,
64	        0.99784622
…[truncated 31944 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T04:28:51.278726+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/kvtc-survey/kvtc/src/cache.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/kvtc-survey/kvtc/src/cache.py"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T04:28:51.278891+00:00_

1	"""Cache integration for KVTC."""
2	
3	from __future__ import annotations
4	
5	from typing import Dict, Optional
6	
7	import torch
8	
9	from .common import CompressedKVCache
10	from .pipeline import KVTCCompressor
11	
12	try:
13	    from transformers.cache_utils import DynamicCache
14	except Exception:  # pragma: no cover
15	    class DynamicCache:  # type: ignore[override]
16	        """Minimal fallback cache base class."""
17	
18	        pass
19	
20	
21	class KVTCCache(DynamicCache):
22	    """Dynamic cache wrapper with transparent KVTC compression."""
23	
24	    def __init__(self, compressor: KVTCCompressor, compression_ratio_target: float = 5.0) -> None:
25	        super().__init__()
26	        self.compressor = compressor
27	        self.compression_ratio_target = compression_ratio_target
28	        self.live_cache: Dict[int, Dict[str, torch.Tensor]] = {}
29	        self.compressed_cache: Dict[int, CompressedKVCache] = {}
30	
31	    def update(self, layer_idx: int, keys: torch.Tensor, values: torch.Tensor) -> None:
32	        """Store a live layer cache."""
33	
34	        self.live_cache[layer_idx] = {"keys": keys, "values": values}
35	        self.compressed_cache.pop(layer_idx, None)
36	
37	    def evict_to_compressed(self, layer_idx: int, positions: torch.Tensor) -> CompressedKVCache:
38	        """Compress a live layer cache."""
39	
40	        layer = self.live_cache.pop(layer_idx)
41	        kv_cache = {"keys": layer["keys"].unsqueeze(0), "values": layer["values"].unsqueeze(0)}
42	        compressed = self.compressor.compress(kv_cache, positions)
43	        self.compressed_cache[layer_idx] = compressed
44	        return compressed
45	
46	    def restore_layer(self, layer_idx: int) -> Dict[str, torch.Tensor]:
47	        """Restore a compressed layer back into live form."""
48	
49	        if layer_idx in self.live_cache:
50	            return self.live_cache[layer_idx]
51	        compressed = self.compressed_cache.pop(layer_idx)
52	        restored = self.
…[truncated 574 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T04:28:51.279040+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/kvtc-survey/kvtc/cuda/kvtc.h"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/kvtc-survey/kvtc/cuda/kvtc.h"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T04:28:51.279223+00:00_

1	/*
2	 * KVTC — KV-Cache Tensor Compression CUDA Kernels
3	 * 
4	 * Header for the CUDA encode/decode kernels that implement:
5	 * 1. PCA transform (matmul with pre-computed eigenvectors)
6	 * 2. Adaptive quantization (per-component bit widths)
7	 * 3. Bit packing into compressed byte stream
8	 * 
9	 * These kernels are designed to be called from llama.cpp's KV cache
10	 * write/read paths, replacing the FP16 KV storage with compressed
11	 * KVTC format.
12	 * 
13	 * Copyright (c) 2026 Terp AI Labs / @OnlyTerp
14	 * License: MIT
15	 */
16	
17	#ifndef KVTC_H
18	#define KVTC_H
19	
20	#include &lt;cuda_fp16.h>
21	#include &lt;stdint.h>
22	
23	#ifdef __cplusplus
24	extern "C" {
25	#endif
26	
27	/* ─── Calibration data (per layer, per head group, per kind) ──────── */
28	
29	typedef struct {
30	    float *eigenvectors;     /* [dim, dim] PCA basis (row-major) */
31	    float *eigenvalues;      /* [dim] eigenvalue magnitudes */
32	    float *mean;             /* [dim] PCA mean vector */
33	    int    dim;              /* head dimension (e.g. 128) */
34	    int    bit_budget;       /* total bits for this group */
35	    float  rope_theta;       /* RoPE base frequency */
36	} kvtc_calibration_t;
37	
38	/* ─── Compressed block metadata ──────────────────────────────────── */
39	
40	typedef struct {
41	    uint8_t *data;           /* compressed byte stream */
42	    int      data_bytes;     /* size of compressed data */
43	    int      num_rows;       /* number of KV vectors compressed */
44	    int      dim;            /* head dimension */
45	    float   *scales;         /* [dim] quantization scales */
46	    float   *zero_points;    /* [dim] quantization zero points */
47	    int8_t  *bit_widths;     /* [dim] bits per component (0-16) */
48	} kvtc_compressed_t;
49	
50	/* ─── Context (holds all calibration data for one model) ─────────── */
51	
52	typedef struct {
53	    kvtc_calibration_t *entries;  /* array of calibration entries */
54	    int                 n_entries;
55	    i
…[truncated 7111 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-14T04:28:51.279380+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/kvtc-survey/kvtc/IMPLEMENTATION_NOTES.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/kvtc-survey/kvtc/IMPLEMENTATION_NOTES.md"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-14T04:28:51.279533+00:00_

1	# Implementation Notes
2	
3	## Algorithm: Three-Stage Transform Coding
4	
5	KVTC (arxiv 2511.01815) compresses KV caches using a pipeline inspired by classical media codecs (JPEG, H.264). The three stages are applied only to the "middle" tokens — attention sinks and the sliding window are preserved exactly.
6	
7	### Stage 1: PCA Feature Decorrelation
8	
9	**Why PCA?** Raw KV cache vectors have correlated dimensions — particularly within attention head groups. PCA decorrelates these dimensions and orders them by variance, enabling Stage 2 to allocate bits efficiently.
10	
11	**RoPE handling (critical for keys):** Rotary Position Embeddings rotate key vectors based on their position in the sequence. This rotation obscures the low-rank structure that PCA needs. We **undo RoPE before PCA** and **reapply it after decompression**. Values don't use RoPE, so no special handling is needed.
12	
13	The RoPE inverse is exact: for a rotation by angle θ, the inverse is a rotation by -θ. We verified this with roundtrip tests (error < 1e-5).
14	
15	**Calibration:** PCA eigenvectors are computed once from a small calibration dataset (~10 texts through the model). The eigenvectors and eigenvalues are stored per `(layer, head_group, key_or_value)`. For a 7B model with 32 layers and 8 KV heads, this produces 32 × 8 × 2 = 512 PCA entries. Storage overhead is small relative to model size.
16	
17	**SVD vs eigendecomposition:** We use `torch.linalg.svd` on the centered data matrix rather than eigendecomposition of the covariance matrix. SVD is numerically more stable and directly gives us the eigenvectors (right singular vectors) and eigenvalues (squared singular values / (n-1)).
18	
19	### Stage 2: Adaptive Quantization via Dynamic Programming
20	
21	**The DP objective:** Given eigenvalues λ₁ ≥ λ₂ ≥ ... ≥ λ_d (from PCA) and a total bit budget B, find bit widths b₁, ..., b_d that minimize total reconstruction error:
22	
23	```
24	minimize  Σᵢ λᵢ / 4^bᵢ     (quantization error per compone
…[truncated 3616 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-14T04:28:51.279698+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T04:28:51.279828+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-14T04:28:51.279991+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-14T04:28:51.280107+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-14T04:28:51.280279+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/kvtc_survey.md",
  "content": "# KVTC 代码库深度调研报告\n\n> 仓库: https://github.com/OnlyTerp/kvtc  \n> 论文: arXiv 2511.01815 (ICLR 2026)  \n> 调研日期: 2026-05-14  \n> 目的: 为 CompressLink RABA 修改方案提供代码级依据\n\n---\n\n## 1. 仓库概览\n\n### 1.1 项目结构\n\n```\nkvtc/\n├── src/\n│   ├── common.py              # 核心数据结构 (CalibrationData, CompressedKVCache, PCAEntry 等)\n│   ├── pca.py                 # PCA transform, RoPE undo/reapply, PCACalibrator\n│   ├── quantize.py            # DP bit allocation (精确版), uniform quantize/dequantize\n│   ├── gpu_ops.py             # greedy bit allocation (近似版), batch quantize/dequantize\n│   ├── entropy.py             # zlib DEFLATE + bit packing/unpacking\n│   ├── ans_entropy.py         # rANS entropy coding (triple-mode picker: zlib/LZMA/rANS)\n│   ├── adaptive_budget.py     # 基于 eigenvalue entropy 的 per-layer adaptive bit budget\n│   ├── fused_ops.py           # Fused PCA+Quantize 单 pass kernel\n│   ├── pipeline.py            # 参考 pipeline (CPU, ~160 行)\n│   ├── pipeline_fast.py       # GPU 加速 pipeline (~233 行)\n│   ├── triton_kernels.py      # Triton GPU kernels (bit packing)\n│   ├── cache.py               # HuggingFace DynamicCache 包装\n│   ├── calibrate.py           # PCA calibration (从模型+数据集)\n│   ├── calibrate_vllm.py      # vLLM 专用 calibration\n│   ├── vllm_backend.py        # vLLM attention backend\n│   ├── vllm_triton.py         # Fused Triton decode attention kernel\n│   ├── test_kvtc.py           # 38 个单元测试\n│   └── test_real_model.py     # TinyLlama 集成测试\n├── cuda/\n│   ├── kvtc.h                 # CUDA kernel C API header\n│   ├── kvtc_kernels.cu        # CUDA kernel 实现\n│   └── CMakeLists.txt\n├── benchmarks/\n│   ├── benchmark_v1-v4.py     # 各版本 benchmark\n│   ├── results_v1-v4.json     # 结果数据\n│   └── benchmark_perplexity.py\n└── setup.py\n```\n\n### 1.2 依赖\n\n- **核心**: `torch`, `numpy`, `transformers`\n- **开发**: `pytest`\n- **可选**: `triton` (GPU bit packing), CUDA toolkit (原生 kernels)\n- Python 3.10+, PyTorch 2.10+\n\n### 1.3 支持模型\n\n代码通过 HuggingFace `transformers` 加载模型，理论上支持所有 causal LM。已验证:\n- Qwen2.5-7B-Instruct (主要 benchmark 模型, 28 layers, 4 KV heads, dim=128)\n- Llama-3.1-8B-Instruct\n- TinyLlama (测试用)\n- Mistral-7B-Instruct\n\nPCA calibration 按 `(layer, head_group, kind)` 存储，天然适配不同模型架构。\n\n---\n\n## 2. 数据流概览\n\n```\n原始 KV cache [layers, tokens, heads, dim] FP16\n  │\n  ├── 前 4 tokens → sink buffer (FP16 保留)\n  ├── 后 128 tokens → window buffer (FP16 保留)\n  └── 中间 tokens → 压缩流水线:\n        │\n        ▼\n      RoPE Undo (仅 keys, 用 -sin 反转旋转)\n        │\n        ▼\n      PCA Transform: centered = x - mean; coeffs = centered @ Vh.T\n        │\n        ▼\n      DP Bit Allocation: eigenvalues + budget → per-component bit widths [0-16]\n        │\n        ▼\n      Uniform Quantize: per-component affine 量化\n        │\n        ▼\n      Bit Packing → Entropy Coding (zlib/LZMA/rANS triple picker)\n        │\n        ▼\n      CompressedKVCache (bytes + metadata)\n```\n\n---\n\n## 3. PCA Pipeline 详解\n\n### 3.1 文件位置\n\n- `src/pca.py`: PCA transform/inverse, RoPE 操作, `PCACalibrator` 类\n- `src/calibrate.py`: `KVTCCalibrator` 高层封装\n\n### 3.2 PCA 训练数据\n\n**离线 one-time calibration**, 流程:\n1. 选取 ~10 个文本样本\n2. 前向传播获取 `past_key_values`\n3. 对 keys 先做 RoPE inverse (消除位置旋转)\n4. 按 `(layer, head_group, kind)` 分组拼接\n5. 对每组做 SVD: `U, S, Vh = torch.linalg.svd(centered, full_matrices=False)`\n6. `eigenvalues = S² / (n-1)`, `eigenvectors = Vh`\n\n关键代码 (`pca.py:222-296`):\n```python\ndef compute(self, bit_budget_ratio: float = 0.25) -> CalibrationData:\n    data = torch.cat(sample_list, dim=0)  # [total_rows, dim]\n    mean = data.mean(dim=0)\n    centered = data - mean\n    _, singular_values, vh = torch.linalg.svd(centered, full_matrices=False)\n    eigenvalues = singular_values.square() / max(centered.shape[0] - 1, 1)\n    # ...\n    bit_widths = dp_bit_allocation(eigenvalues, bit_budget=total_bits, max_bits=16)\n```\n\n### 3.3 PCA 维度策略\n\n- **每层每头独立 PCA** (默认 `head_group_size=1`)，最大化 per-head decorrelation\n- 保留全部 dim 个 PCA component，但通过 DP bit allocation 将低方差 component 的 bits 设为 0（等效剪枝）\n- 不做显式维度裁剪——裁剪由 DP 自动发现\n\n### 3.4 RoPE 处理\n\n- Keys: 压缩前 `apply_rope_inverse` (rotation by -θ)，解压后 `apply_rope` (rotation by θ)\n- Values: 不使用 RoPE，无需处理\n- 逆变换精确 (误差 < 1e-5，旋转矩阵的逆就是转置)\n\n---\n\n## 4. DP Bit Allocation Solver 详解\n\n### 4.1 文件位置与行号\n\n**精确 DP 版本**: `src/quantize.py:16-56` (41 行)  \n**贪心近似版本**: `src/gpu_ops.py:10-57` (48 行)\n\n### 4.2 精确 DP 版本 (`quantize.py:16-56`)\n\n#### 输入\n- `eigenvalues: Tensor[d]` — PCA eigenvalues (方差), 从 calibration 获取\n- `bit_budget: int` — 总 bit 预算 (e.g., `dim * 16 * bit_budget_ratio`)\n- `max_bits: int = 16` — 每 component 最大 bit 宽度\n- `group_size: int = 1` — component 分组大小\n\n#### 输出\n- `widths: Tensor[d]` — per-component bit 分配, 每个值 ∈ [0, 16]\n\n#### Error Function (核心)\n\n```python\nerror = variance if bits == 0 else variance / (4 ** bits)\n```\n\n即: `E(i, b) = λ_i / 4^b`\n\n- `λ_i` 是第 i 个 PCA component 的 eigenvalue (方差)\n- `4^b` 是 b bits 量化带来的 MSE 降低因子 (每 bit 减半量化步长, MSE 减为 1/4)\n- `bits == 0` 时 error 就是 variance 本身 (完全丢弃该 component)\n\n#### DP 状态转移\n\n```\ndp[i][b] = min total MSE using components 0..i-1 with total budget b\n```\n\n转移:\n```\ndp[i][cost] = min over w in {0..16}:  dp[i-1][used] + λ_group / 4^w\n              where cost = used + w * group_width\n```\n\n回溯得到每个 component 的 bit 分配。\n\n#### 复杂度\n\n`O(d × B × max_bits)` = O(128 × 512 × 16) ≈ 1M ops per entry. 足够快。\n\n#### 完整代码\n\n```python\ndef dp_bit_allocation(eigenvalues, bit_budget, max_bits=16, group_size=1):\n    values = eigenvalues.detach().to(torch.float64).flatten()\n    groups = _component_groups(values, group_size)\n    max_budget = max(int(bit_budget), 0)\n    num_groups = len(groups)\n    inf = float(\"inf\")\n    dp = [[inf] * (max_budget + 1) for _ in range(num_groups + 1)]\n    back = [[0] * (max_budget + 1) for _ in range(num_groups + 1)]\n    dp[0][0] = 0.0\n    for idx, group in enumerate(groups, start=1):\n        variance = float(group.sum().item())\n        width = group.numel()\n        for used in range(max_budget + 1):\n            if dp[idx - 1][used] == inf:\n                continue\n            for bits in range(0, max_bits + 1):\n                cost = used + bits * width\n                if cost > max_budget:\n                    continue\n                error = variance if bits == 0 else variance / (4 ** bits)\n                candidate = dp[idx - 1][used] + error\n                if candidate < dp[idx][cost]:\n                    dp[idx][cost] = candidate\n                    back[idx][cost] = bits\n    best_budget = min(range(max_budget + 1), key=lambda b: dp[num_groups][b])\n    # backtrack ...\n    return widths\n```\n\n### 4.3 贪心近似版本 (`gpu_ops.py:10-57`)\n\n生产管线 `pipeline_fast.py` 使用此版本。原理:\n\n```\ngain(i, b) = λ_i × 3 / 4^b\n```\n\n预计算所有 `(component, bit_level)` 的 marginal gain, flatten + topk 取 top-B 个, bincount 得 per-component bits。\n\n复杂度 `O(B log(d × max_bits))`, 远快于精确 DP。\n\n由于 gain 在 bit_level 上单调递减, 贪心解等价于最优解（标准可分离凸优化问题）。\n\n### 4.4 调用链\n\n1. **Calibration 时**: `pca.py:PCACalibrator.compute()` → `quantize.py:dp_bit_allocation()` → 存入 `PCAEntry.bit_widths`\n2. **参考 pipeline**: `pipeline.py:compress()` → `quantize.py:dp_bit_allocation()` (每次压缩重新计算)\n3. **GPU pipeline**: `pipeline_fast.py:compress()` → `gpu_ops.py:greedy_bit_allocation()` (用 calibration 的 bit_budget)\n\n---\n\n## 5. RABA 修改方案\n\n### 5.1 RABA 核心思想\n\n将 error function 从:\n```\nE(i, b) = λ_i / 4^b\n```\n修改为:\n```\nE(i, b, t) = (1 - p_r(t)) × λ_i / 4^b\n```\n\n其中 `p_r(t)` 是 token t 被 RAG cache 恢复的概率。对于高概率被恢复的 token，其量化误差在最终重建时会被精确值覆盖，因此可以分配更少的 bits。\n\n### 5.2 需要修改的文件和函数\n\n#### 修改 1: `src/quantize.py` — `dp_bit_allocation()`\n\n**当前签名** (line 16):\n```python\ndef dp_bit_allocation(eigenvalues, bit_budget, max_bits=16, group_size=1):\n```\n\n**RABA 签名**:\n```python\ndef dp_bit_allocation(eigenvalues, bit_budget, max_bits=16, group_size=1, \n                      restoration_weights=None):\n```\n\n**修改位置** (line 42):\n```python\n# 当前:\nerror = variance if bits == 0 else variance / (4 ** bits)\n\n# RABA:\nif restoration_weights is not None:\n    # weighted_variance = sum of (1 - p_r(t)) * lambda_i for tokens in group\n    # 但注意: DP 是 per-component 的, p_r(t) 是 per-token 的\n    # 这里需要将 per-token weights 聚合为 per-component weight\n    weight = restoration_weights[idx - 1]  # 预计算的 weighted variance\n    error = weight if bits == 0 else weight / (4 ** bits)\nelse:\n    error = variance if bits == 0 else variance / (4 ** bits)\n```\n\n**关键设计问题**: DP 是 per-PCA-component 的, 但 `p_r(t)` 是 per-token 的。需要决定聚合方式:\n\n- **方案 A (per-token DP)**: 将 DP 扩展为 per-token × per-component, 复杂度 O(T × d × B × 16), 对长序列不可行\n- **方案 B (aggregate then DP)**: 将 weighted variance 预计算为 `weighted_λ_i = Σ_t (1 - p_r(t)) × pca_coeffs[t, i]²`, 替换 eigenvalue 输入 DP. 复杂度不变. **推荐方案**\n- **方案 C (per-token bit allocation)**: 对每个 token 独立运行 DP (根据其 p_r), 复杂度 O(T × d × B × 16), 但 bit widths 变为 per-token, bit packing 变复杂\n\n**推荐方案 B 的实现**:\n\n```python\ndef compute_restoration_weighted_eigenvalues(\n    pca_coeffs: torch.Tensor,      # [num_tokens, dim]\n    restoration_probs: torch.Tensor, # [num_tokens]\n) -> torch.Tensor:\n    \"\"\"计算 RABA weighted eigenvalues.\n    \n    weighted_λ_i = mean_t[(1 - p_r(t)) × pca_coeffs[t, i]²]\n    \"\"\"\n    weights = (1 - restoration_probs).unsqueeze(1)  # [T, 1]\n    weighted_var = (weights * pca_coeffs ** 2).mean(dim=0)  # [dim]\n    return weighted_var\n```\n\n然后将 `weighted_eigenvalues` 传入 `dp_bit_allocation` 替代原始 `eigenvalues`。\n\n#### 修改 2: `src/gpu_ops.py` — `greedy_bit_allocation()`\n\n**当前签名** (line 10):\n```python\ndef greedy_bit_allocation(eigenvalues, bit_budget, max_bits=16):\n```\n\n**RABA 修改**: 与精确 DP 类似, 传入 weighted eigenvalues 即可, gain 计算自动适配:\n```python\ngains_matrix = ev.unsqueeze(1) * 3.0 / (4.0 ** bit_levels.unsqueeze(0))\n```\n这里 `ev` 替换为 `weighted_ev` 即可。无需改内部逻辑。\n\n#### 修改 3: `src/pipeline.py` 和 `src/pipeline_fast.py` — `compress()`\n\n需要在 compress 方法中:\n1. 新增 `restoration_probs` 参数 (per-token 概率向量)\n2. 压缩前计算 `pca_coeffs`\n3. 调用 `compute_restoration_weighted_eigenvalues` 得到 weighted eigenvalues\n4. 将 weighted eigenvalues 传入 bit allocation\n\n**`pipeline.py` 修改** (line 23):\n```python\ndef compress(self, kv_cache, positions, restoration_probs=None):\n```\n\n在 line 68 附近, PCA transform 之后:\n```python\npca_values = pca_transform(centered, entry.eigenvectors.to(rows.device))\n\n# RABA: 如果提供了 restoration_probs, 用 weighted eigenvalues\nif restoration_probs is not None:\n    # restoration_probs shape: [middle_len]\n    # rows shape: [middle_len * group_heads, dim]\n    # 需要 expand p_r 到 group_heads\n    pr_expanded = restoration_probs.repeat_interleave(group_heads)\n    weighted_ev = compute_restoration_weighted_eigenvalues(pca_values, pr_expanded)\n    bit_widths = dp_bit_allocation(weighted_ev, entry.bit_budget, group_size=1)\nelse:\n    bit_widths = dp_bit_allocation(entry.eigenvalues.to(rows.device), entry.bit_budget, group_size=1)\n```\n\n**`pipeline_fast.py` 修改** (line 37): 同理, 但用 `greedy_bit_allocation`。\n\n#### 修改 4: `src/calibrate.py` — 可选\n\nCalibration 阶段不需要 RABA (p_r 在推理时才知道)。但可以在 calibration 时额外存储 PCA coefficient 统计, 以加速运行时的 weighted eigenvalue 计算。\n\n### 5.3 额外传入参数\n\n- `restoration_probs: torch.Tensor` — shape `[middle_len]`, 值域 [0, 1]\n  - p_r(t) = 0: token t 不会被恢复, 正常压缩\n  - p_r(t) = 1: token t 必定被恢复, 可分配 0 bits (极端情况)\n  - p_r(t) ∈ (0, 1): 按概率加权降低该 token 的 error 权重\n\n### 5.4 修改复杂度评估\n\n| 文件 | 函数 | 改动行数 | 难度 |\n|------|------|---------|------|\n| `quantize.py` | `dp_bit_allocation` | ~10 行 (新增 weighted_ev 路径) | 低 |\n| `gpu_ops.py` | `greedy_bit_allocation` | ~5 行 (传入 weighted_ev) | 低 |\n| `pipeline.py` | `compress` | ~15 行 (参数 + weighted_ev 计算) | 低 |\n| `pipeline_fast.py` | `compress` | ~15 行 (同上) | 低 |\n| 新增 | `compute_restoration_weighted_eigenvalues` | ~10 行 | 低 |\n| `common.py` | 数据结构 | 0 行 (不需要改) | — |\n| `entropy.py` | — | 0 行 | — |\n\n**总改动: ~55 行代码**, 主要集中在 bit allocation 调用处。不影响量化/编码/解码逻辑。\n\n### 5.5 代码 Diff 草稿\n\n```diff\n--- a/src/quantize.py\n+++ b/src/quantize.py\n@@ -1,5 +1,6 @@\n \"\"\"Quantization utilities for KVTC.\"\"\"\n \n+from __future__ import annotations\n from typing import List\n import torch\n from .common import QuantizationParams\n@@ -12,6 +13,20 @@\n     return [eigenvalues[i : i + group_size] for i in range(0, eigenvalues.numel(), group_size)]\n \n \n+def compute_restoration_weighted_eigenvalues(\n+    pca_coeffs: torch.Tensor,\n+    restoration_probs: torch.Tensor,\n+) -> torch.Tensor:\n+    \"\"\"Compute RABA weighted eigenvalues.\n+    \n+    weighted_lambda_i = mean_t[(1 - p_r(t)) * pca_coeffs[t, i]^2]\n+    \"\"\"\n+    weights = (1 - restoration_probs).unsqueeze(1)  # [T, 1]\n+    weighted_var = (weights * pca_coeffs ** 2).mean(dim=0)  # [dim]\n+    return weighted_var\n+\n+\n def dp_bit_allocation(\n     eigenvalues: torch.Tensor,\n     bit_budget: int,\n```\n\n```diff\n--- a/src/pipeline_fast.py\n+++ b/src/pipeline_fast.py\n@@ -37,7 +37,7 @@\n-    def compress(self, kv_cache, positions):\n+    def compress(self, kv_cache, positions, restoration_probs=None):\n         # ... (unchanged until after PCA transform) ...\n \n                         pca_values = pca_transform(centered, ev)\n \n+                        # RABA: use weighted eigenvalues if restoration probs provided\n+                        if restoration_probs is not None:\n+                            pr = restoration_probs.to(pca_values.device)\n+                            pr_expanded = pr.repeat_interleave(group_heads)\n+                            weighted_ev = compute_restoration_weighted_eigenvalues(\n+                                pca_values, pr_expanded\n+                            )\n+                            bit_widths = greedy_bit_allocation(weighted_ev, entry.bit_budget)\n+                        else:\n-                        bit_widths = greedy_bit_allocation(\n-                            entry.eigenvalues.to(rows.device), entry.bit_budget,\n-                        )\n+                            bit_widths = greedy_bit_allocation(\n+                                entry.eigenvalues.to(rows.device), entry.bit_budget,\n+                            )\n```\n\n### 5.6 不影响的模块\n\n- **PCA transform/inverse**: 不受影响, 仍用相同 eigenvectors\n- **Quantization**: 不受影响, 仍用 uniform affine quantization\n- **Entropy coding**: 不受影响, 仍对量化后的 bytes 做压缩\n- **RoPE**: 不受影响\n- **Token protection** (sink/window): 不受影响\n- **Decompression**: 不受影响, metadata 中已存储 bit_widths\n\n---\n\n## 6. 压缩比评估\n\n### 6.1 Benchmark 数据 (RTX 5090, Qwen2.5-7B)\n\n| Config | K bits | V bits | 压缩比 | K Cosine | V Cosine | 质量 |\n|--------|--------|--------|:------:|:--------:|:--------:|------|\n| K1V2-FULL | 1 | 2 | **12.8x** | 0.9925 | 0.9120 | 低 |\n| K1V3-FULL | 1 | 3 | **8.9x** | 0.9925 | 0.9874 | 可用 |\n| K1V4-FULL | 1 | 4 | **7.1x** | 0.9925 | 0.9974 | 优 |\n| K2V3-FULL | 2 | 3 | **7.2x** | 0.9970 | 0.9874 | 可用 |\n| K2V4-FULL | 2 | 4 | **5.9x** | 0.9970 | 0.9974 | 优 |\n| K3V4-FULL | 3 | 4 | **5.0x** | 0.9993 | 0.9974 | 优 |\n\n### 6.2 8x 压缩比可达性评估\n\n**K1V3 配置达到 8.9x**, cosine similarity 0.987-0.993, 质量为 \"Good\"。\n\n**RABA 对 8x 目标的影响**:\n- RABA 会让部分 token 分配更少 bits (高 p_r tokens) → 平均 bits 降低 → 压缩比提升\n- 但总 bit budget 不变, 只是重分配: 高 p_r tokens 少分, 低 p_r tokens 多分\n- 净效应: 如果大量 tokens 有高 p_r, 可以用更少的 bit budget 达到相同重建质量 → **提升有效压缩比**\n- 在 K2V4 基础上 + RABA (假设 50% tokens 有 p_r > 0.5), 有效压缩比可达 7-9x 同时保持更高质量\n\n**结论**: 8x 在 KVTC 可达范围内。K1V3 直接达到 8.9x, K2V4 + RABA 可在保持更高质量的同时逼近 8x。\n\n### 6.3 Benchmark 脚本\n\n```bash\n# 完整 benchmark\npython benchmarks/benchmark_v4.py --model Qwen/Qwen2.5-7B-Instruct --device cuda\n\n# 指定配置\npython benchmarks/benchmark_v3.py --model meta-llama/Llama-3.1-8B-Instruct --device cuda\n\n# 单元测试 (无需 GPU)\npytest src/test_kvtc.py -v\n```\n\n---\n\n## 7. Entropy Coding 流程\n\n### 7.1 编码方法\n\n三种编码器, triple-mode picker 选最小:\n\n| 编码器 | 文件 | 说明 |\n|--------|------|------|\n| **zlib (DEFLATE)** | `entropy.py` | 默认, 压缩 level 6-9 |\n| **LZMA2** | `ans_entropy.py:compress_best()` | Python `lzma` module |\n| **rANS** | `ans_entropy.py:rans_encode()` | 纯 Python 实现, 16-bit precision |\n\nTriple picker (`ans_entropy.py:184-230`):\n```python\ndef compress_best(packed_bytes, level=6):\n    candidates = []\n    candidates.append((b\"Z\" + zlib.compress(packed_bytes, 9), \"zlib\"))\n    candidates.append((b\"L\" + lzma.compress(packed_bytes, preset=6), \"lzma\"))\n    candidates.append((b\"A\" + rans_encode(packed_bytes), \"rans\"))\n    best = min(candidates, key=lambda x: len(x[0]))\n    return best[0], ratio\n```\n\n1-byte tag 前缀标识编码器: `Z`=zlib, `L`=LZMA, `A`=rANS.\n\n### 7.2 编解码 API\n\n**编码**:\n```python\nfrom src.entropy import pack_bits, compress\nfrom src.ans_entropy import compress_best\n\n# Step 1: 将量化 indices 打包为 bytes\npacked = pack_bits(indices_list, bit_widths)\n\n# Step 2a: zlib 压缩\ncompressed, ratio = compress(packed, level=6)\n\n# Step 2b: 或用 triple picker\ncompressed, ratio = compress_best(packed, level=6)\n```\n\n**解码**:\n```python\nfrom src.entropy import decompress, unpack_bits\nfrom src.ans_entropy import decompress_best\n\n# Step 1: 解压\npacked = decompress(compressed, original_size)\n# 或 triple picker\npacked = decompress_best(compressed, original_size)\n\n# Step 2: 解包\nindices_list = unpack_bits(packed, bit_widths, lengths)\n```\n\n### 7.3 Bit Packing\n\n`entropy.py:47-83`: 按 component 顺序逐个打包 (comp 0 所有 rows, 然后 comp 1, ...), 变宽 bit stream, 无对齐要求。\n\nGPU 加速版在 `gpu_ops.py:fast_pack_bits()` 和 `triton_kernels.py:gpu_pack_variable_width()`。\n\n---\n\n## 8. Adaptive Budget (per-layer)\n\n### 8.1 原理\n\n`adaptive_budget.py`: 不同 layer 的 PCA eigenvalue spectrum \"平坦度\"不同:\n- 平坦 (high Shannon entropy) → 难压缩 → 分配更多 bits\n- 陡峭 (low entropy) → 易压缩 → 分配更少 bits\n\n总预算守恒, 只做重分配。\n\n### 8.2 API\n\n```python\nfrom src.adaptive_budget import apply_adaptive_budgets\n\nkey_diff, val_diff = apply_adaptive_budgets(\n    calibration, key_bits_avg=2, value_bits_avg=4, strength=1.0\n)\n```\n\n`strength=0` 为均匀分配, `strength=1` 为完全自适应。\n\n---\n\n## 9. 集成风险和注意事项\n\n### 9.1 RABA 集成风险\n\n| 风险 | 说明 | 缓解 |\n|------|------|------|\n| **DP 粒度不匹配** | DP 是 per-component, p_r 是 per-token | 用方案 B: 预聚合 weighted eigenvalues |\n| **p_r 精度要求** | p_r 误估可能导致分配不当 | 加 clamp(0.01, 0.99) 防极端值 |\n| **与 adaptive budget 交互** | RABA 和 adaptive budget 都改 bit allocation | 两者正交: adaptive 改 per-layer budget, RABA 改 per-component allocation |\n| **解压不需要 p_r** | metadata 中已存 bit_widths | 正确, 解压路径零改动 |\n| **Calibration 兼容** | RABA 修改运行时 bit allocation, 不改 calibration | 完全兼容, 无需重新 calibrate |\n\n### 9.2 性能影响\n\n- 压缩时增加 `weighted_eigenvalue` 计算: 一次矩阵乘 `O(T × d)`, 可忽略\n- Bit allocation (贪心版) 运行时间不变\n- 解压路径零开销\n\n### 9.3 代码质量观察\n\n- 代码组织清晰, pipeline → pca → quantize → entropy 模块化良好\n- 两个 pipeline (参考 + GPU) 保持接口一致, 修改一个的经验可直接复用\n- 38 个测试覆盖所有核心功能, 添加 RABA 后应增加对应测试\n- `group_size=1` 默认设置意味着 per-head PCA, 对 RABA 的 per-token weight 聚合较友好\n\n### 9.4 推荐实施顺序\n\n1. 在 `quantize.py` 新增 `compute_restoration_weighted_eigenvalues()` 函数\n2. 修改 `pipeline.py` (参考版) 的 `compress()` 方法, 添加 RABA 支持\n3. 编写单元测试: weighted eigenvalues 计算正确性, RABA bit allocation 向后兼容 (p_r=0 时等价原版)\n4. 验证: p_r=0 应产生与原版完全相同的 bit allocation\n5. 修改 `pipeline_fast.py` (GPU 版)\n6. 端到端测试: 带 RABA 的压缩-解压 roundtrip\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/kvtc_survey.md",
    "content": "# KVTC 代码库深度调研报告\n\n> 仓库: https://github.com/OnlyTerp/kvtc  \n> 论文: arXiv 2511.01815 (ICLR 2026)  \n> 调研日期: 2026-05-14  \n> 目的: 为 CompressLink RABA 修改方案提供代码级依据\n\n---\n\n## 1. 仓库概览\n\n### 1.1 项目结构\n\n```\nkvtc/\n├── src/\n│   ├── common.py              # 核心数据结构 (CalibrationData, CompressedKVCache, PCAEntry 等)\n│   ├── pca.py                 # PCA transform, RoPE undo/reapply, PCACalibrator\n│   ├── quantize.py            # DP bit allocation (精确版), uniform quantize/dequantize\n│   ├── gpu_ops.py             # greedy bit allocation (近似版), batch quantize/dequantize\n│   ├── entropy.py             # zlib DEFLATE + bit packing/unpacking\n│   ├── ans_entropy.py         # rANS entropy coding (triple-mode picker: zlib/LZMA/rANS)\n│   ├── adaptive_budget.py     # 基于 eigenvalue entropy 的 per-layer adaptive bit budget\n│   ├── fused_ops.py           # Fused PCA+Quantize 单 pass kernel\n│   ├── pipeline.py            # 参考 pipeline (CPU, ~160 行)\n│   ├── pipeline_fast.py       # GPU 加速 pipeline (~233 行)\n│   ├── triton_kernels.py      # Triton GPU kernels (bit packing)\n│   ├── cache.py               # HuggingFace DynamicCache 包装\n│   ├── calibrate.py           # PCA calibration (从模型+数据集)\n│   ├── calibrate_vllm.py      # vLLM 专用 calibration\n│   ├── vllm_backend.py        # vLLM attention backend\n│   ├── vllm_triton.py         # Fused Triton decode attention kernel\n│   ├── test_kvtc.py           # 38 个单元测试\n│   └── test_real_model.py     # TinyLlama 集成测试\n├── cuda/\n│   ├── kvtc.h                 # CUDA kernel C API header\n│   ├── kvtc_kernels.cu        # CUDA kernel 实现\n│   └── CMakeLists.txt\n├── benchmarks/\n│   ├── benchmark_v1-v4.py     # 各版本 benchmark\n│   ├── results_v1-v4.json     # 结果数据\n│   └── benchmark_perplexity.py\n└── setup.py\n```\n\n### 1.2 依赖\n\n- **核心**: `torch`, `numpy`, `transformers`\n- **开发**: `pytest`\n- **可选**: `triton` (GPU bit packing), CUDA toolkit (原生 kernels)\n- Python 3.10+, PyTorch 2.10+\n\n### 1.3 支持模型\n\n代码通过 HuggingFace `transformers` 加载模型，理论上支持所有 causal LM。已验证:\n- Qwen2.5-7B-Instruct (主要 benchmark 模型, 28 layers, 4 KV heads, dim=128)\n- Llama-3.1-8B-Instruct\n- TinyLlama (测试用)\n- Mistral-7B-Instruct\n\nPCA calibration 按 `(layer, head_group, kind)` 存储，天然适配不同模型架构。\n\n---\n\n## 2. 数据流概览\n\n```\n原始 KV cache [layers, tokens, heads, dim] FP16\n  │\n  ├── 前 4 tokens → sink buffer (FP16 保留)\n  ├── 后 128 tokens → window buffer (FP16 保留)\n  └── 中间 tokens → 压缩流水线:\n        │\n        ▼\n      RoPE Undo (仅 keys, 用 -sin 反转旋转)\n        │\n        ▼\n      PCA Transform: centered = x - mean; coeffs = centered @ Vh.T\n        │\n        ▼\n      DP Bit Allocation: eigenvalues + budget → per-component bit widths [0-16]\n        │\n        ▼\n      Uniform Quantize: per-component affine 量化\n        │\n        ▼\n      Bit Packing → Entropy Coding (zlib/LZMA/rANS triple picker)\n        │\n        ▼\n      CompressedKVCache (bytes + metadata)\n```\n\n---\n\n## 3. PCA Pipeline 详解\n\n### 3.1 文件位置\n\n- `src/pca.py`: PCA transform/inverse, RoPE 操作, `PCACalibrator` 类\n- `src/calibrate.py`: `KVTCCalibrator` 高层封装\n\n### 3.2 PCA 训练数据\n\n**离线 one-time calibration**, 流程:\n1. 选取 ~10 个文本样本\n2. 前向传播获取 `past_key_values`\n3. 对 keys 先做 RoPE inverse (消除位置旋转)\n4. 按 `(layer, head_group, kind)` 分组拼接\n5. 对每组做 SVD: `U, S, Vh = torch.linalg.svd(centered, full_matrices=False)`\n6. `eigenvalues = S² / (n-1)`, `eigenvectors = Vh`\n\n关键代码 (`pca.py:222-296`):\n```python\ndef compute(self, bit_budget_ratio: float = 0.25) -> CalibrationData:\n    data = torch.cat(sample_list, dim=0)  # [total_rows, dim]\n    mean = data.mean(dim=0)\n    centered = data - mean\n    _, singular_values, vh = torch.linalg.svd(centered, full_matrices=False)\n    eigenvalues = singular_values.square() / max(centered.shape[0] - 1, 1)\n    # ...\n    bit_widths = dp_bit_allocation(eigenvalues, bit_budget=total_bits, max_bits=16)\n```\n\n### 3.3 PCA 维度策略\n\n- **每层每头独立 PCA** (默认 `head_group_size=1`)，最大化 per-head decorrelation\n- 保留全部 dim 个 PCA component，但通过 DP bit allocation 将低方差 component 的 bits 设为 0（等效剪枝）\n- 不做显式维度裁剪——裁剪由 DP 自动发现\n\n### 3.4 RoPE 处理\n\n- Keys: 压缩前 `apply_rope_inverse` (rotation by -θ)，解压后 `apply_rope` (rotation by θ)\n- Values: 不使用 RoPE，无需处理\n- 逆变换精确 (误差 < 1e-5，旋转矩阵的逆就是转置)\n\n---\n\n## 4. DP Bit Allocation Solver 详解\n\n### 4.1 文件位置与行号\n\n**精确 DP 版本**: `src/quantize.py:16-56` (41 行)  \n**贪心近似版本**: `src/gpu_ops.py:10-57` (48 行)\n\n### 4.2 精确 DP 版本 (`quantize.py:16-56`)\n\n#### 输入\n- `eigenvalues: Tensor[d]` — PCA eigenvalues (方差), 从 calibration 获取\n- `bit_budget: int` — 总 bit 预算 (e.g., `dim * 16 * bit_budget_ratio`)\n- `max_bits: int = 16` — 每 component 最大 bit 宽度\n- `group_size: int = 1` — component 分组大小\n\n#### 输出\n- `widths: Tensor[d]` — per-component bit 分配, 每个值 ∈ [0, 16]\n\n#### Error Function (核心)\n\n```python\nerror = variance if bits == 0 else variance / (4 ** bits)\n```\n\n即: `E(i, b) = λ_i / 4^b`\n\n- `λ_i` 是第 i 个 PCA component 的 eigenvalue (方差)\n- `4^b` 是 b bits 量化带来的 MSE 降低因子 (每 bit 减半量化步长, MSE 减为 1/4)\n- `bits == 0` 时 error 就是 variance 本身 (完全丢弃该 component)\n\n#### DP 状态转移\n\n```\ndp[i][b] = min total MSE using components 0..i-1 with total budget b\n```\n\n转移:\n```\ndp[i][cost] = min over w in {0..16}:  dp[i-1][used] + λ_group / 4^w\n              where cost = used + w * group_width\n```\n\n回溯得到每个 component 的 bit 分配。\n\n#### 复杂度\n\n`O(d × B × max_bits)` = O(128 × 512 × 16) ≈ 1M ops per entry. 足够快。\n\n#### 完整代码\n\n```python\ndef dp_bit_allocation(eigenvalues, bit_budget, max_bits=16, group_size=1):\n    values = eigenvalues.detach().to(torch.float64).flatten()\n    groups = _component_groups(values, group_size)\n    max_budget = max(int(bit_budget), 0)\n    num_groups = len(groups)\n    inf = float(\"inf\")\n    dp = [[inf] * (max_budget + 1) for _ in range(num_groups + 1)]\n    back = [[0] * (max_budget + 1) for _ in range(num_groups + 1)]\n    dp[0][0] = 0.0\n    for idx, group in enumerate(groups, start=1):\n        variance = float(group.sum().item())\n        width = group.numel()\n        for used in range(max_budget + 1):\n            if dp[idx - 1][used] == inf:\n                continue\n            for bits in range(0, max_bits + 1):\n                cost = used + bits * width\n                if cost > max_budget:\n                    continue\n                error = variance if bits == 0 else variance / (4 ** bits)\n                candidate = dp[idx - 1][used] + error\n                if candidate < dp[idx][cost]:\n                    dp[idx][cost] = candidate\n                    back[idx][cost] = bits\n    best_budget = min(range(max_budget + 1), key=lambda b: dp[num_groups][b])\n    # backtrack ...\n    return widths\n```\n\n### 4.3 贪心近似版本 (`gpu_ops.py:10-57`)\n\n生产管线 `pipeline_fast.py` 使用此版本。原理:\n\n```\ngain(i, b) = λ_i × 3 / 4^b\n```\n\n预计算所有 `(component, bit_level)` 的 marginal gain, flatten + topk 取 top-B 个, bincount 得 per-component bits。\n\n复杂度 `O(B log(d × max_bits))`, 远快于精确 DP。\n\n由于 gain 在 bit_level 上单调递减, 贪心解等价于最优解（标准可分离凸优化问题）。\n\n### 4.4 调用链\n\n1. **Calibration 时**: `pca.py:PCACalibrator.compute()` → `quantize.py:dp_bit_allocation()` → 存入 `PCAEntry.bit_widths`\n2. **参考 pipeline**: `pipeline.py:compress()` → `quantize.py:dp_bit_allocation()` (每次压缩重新计算)\n3. **GPU pipeline**: `pipeline_fast.py:compress()` → `gpu_ops.py:greedy_bit_allocation()` (用 calibration 的 bit_budget)\n\n---\n\n## 5. RABA 修改方案\n\n### 5.1 RABA 核心思想\n\n将 error function 从:\n```\nE(i, b) = λ_i / 4^b\n```\n修改为:\n```\nE(i, b, t) = (1 - p_r(t)) × λ_i / 4^b\n```\n\n其中 `p_r(t)` 是 token t 被 RAG cache 恢复的概率。对于高概率被恢复的 token，其量化误差在最终重建时会被精确值覆盖，因此可以分配更少的 bits。\n\n### 5.2 需要修改的文件和函数\n\n#### 修改 1: `src/quantize.py` — `dp_bit_allocation()`\n\n**当前签名** (line 16):\n```python\ndef dp_bit_allocation(eigenvalues, bit_budget, max_bits=16, group_size=1):\n```\n\n**RABA 签名**:\n```python\ndef dp_bit_allocation(eigenvalues, bit_budget, max_bits=16, group_size=1, \n                      restoration_weights=None):\n```\n\n**修改位置** (line 42):\n```python\n# 当前:\nerror = variance if bits == 0 else variance / (4 ** bits)\n\n# RABA:\nif restoration_weights is not None:\n    # weighted_variance = sum of (1 - p_r(t)) * lambda_i for tokens in group\n    # 但注意: DP 是 per-component 的, p_r(t) 是 per-token 的\n    # 这里需要将 per-token weights 聚合为 per-component weight\n    weight = restoration_weights[idx - 1]  # 预计算的 weighted variance\n    error = weight if bits == 0 else weight / (4 ** bits)\nelse:\n    error = variance if bits == 0 else variance / (4 ** bits)\n```\n\n**关键设计问题**: DP 是 per-PCA-component 的, 但 `p_r(t)` 是 per-token 的。需要决定聚合方式:\n\n- **方案 A (per-token DP)**: 将 DP 扩展为 per-token × per-component, 复杂度 O(T × d × B × 16), 对长序列不可行\n- **方案 B (aggregate then DP)**: 将 weighted variance 预计算为 `weighted_λ_i = Σ_t (1 - p_r(t)) × pca_coeffs[t, i]²`, 替换 eigenvalue 输入 DP. 复杂度不变. **推荐方案**\n- **方案 C (per-token bit allocation)**: 对每个 token 独立运行 DP (根据其 p_r), 复杂度 O(T × d × B × 16), 但 bit widths 变为 per-token, bit packing 变复杂\n\n**推荐方案 B 的实现**:\n\n```python\ndef compute_restoration_weighted_eigenvalues(\n    pca_coeffs: torch.Tensor,      # [num_tokens, dim]\n    restoration_probs: torch.Tensor, # [num_tokens]\n) -> torch.Tensor:\n    \"\"\"计算 RABA weighted eigenvalues.\n    \n    weighted_λ_i = mean_t[(1 - p_r(t)) × pca_coeffs[t, i]²]\n    \"\"\"\n    weights = (1 - restoration_probs).unsqueeze(1)  # [T, 1]\n    weighted_var = (weights * pca_coeffs ** 2).mean(dim=0)  # [dim]\n    return weighted_var\n```\n\n然后将 `weighted_eigenvalues` 传入 `dp_bit_allocation` 替代原始 `eigenvalues`。\n\n#### 修改 2: `src/gpu_ops.py` — `greedy_bit_allocation()`\n\n**当前签名** (line 10):\n```python\ndef greedy_bit_allocation(eigenvalues, bit_budget, max_bits=16):\n```\n\n**RABA 修改**: 与精确 DP 类似, 传入 weighted eigenvalues 即可, gain 计算自动适配:\n```python\ngains_matrix = ev.unsqueeze(1) * 3.0 / (4.0 ** bit_levels.unsqueeze(0))\n```\n这里 `ev` 替换为 `weighted_ev` 即可。无需改内部逻辑。\n\n#### 修改 3: `src/pipeline.py` 和 `src/pipeline_fast.py` — `compress()`\n\n需要在 compress 方法中:\n1. 新增 `restoration_probs` 参数 (per-token 概率向量)\n2. 压缩前计算 `pca_coeffs`\n3. 调用 `compute_restoration_weighted_eigenvalues` 得到 weighted eigenvalues\n4. 将 weighted eigenvalues 传入 bit allocation\n\n**`pipeline.py` 修改** (line 23):\n```python\ndef compress(self, kv_cache, positions, restoration_probs=None):\n```\n\n在 line 68 附近, PCA transform 之后:\n```python\npca_values = pca_transform(centered, entry.eigenvectors.to(rows.device))\n\n# RABA: 如果提供了 restoration_probs, 用 weighted eigenvalues\nif restoration_probs is not None:\n    # restoration_probs shape: [middle_len]\n    # rows shape: [middle_len * group_heads, dim]\n    # 需要 expand p_r 到 group_heads\n    pr_expanded = restoration_probs.repeat_interleave(group_heads)\n    weighted_ev = compute_restoration_weighted_eigenvalues(pca_values, pr_expanded)\n    bit_widths = dp_bit_allocation(weighted_ev, entry.bit_budget, group_size=1)\nelse:\n    bit_widths = dp_bit_allocation(entry.eigenvalues.to(rows.device), entry.bit_budget, group_size=1)\n```\n\n**`pipeline_fast.py` 修改** (line 37): 同理, 但用 `greedy_bit_allocation`。\n\n#### 修改 4: `src/calibrate.py` — 可选\n\nCalibration 阶段不需要 RABA (p_r 在推理时才知道)。但可以在 calibration 时额外存储 PCA coefficient 统计, 以加速运行时的 weighted eigenvalue 计算。\n\n### 5.3 额外传入参数\n\n- `restoration_probs: torch.Tensor` — shape `[middle_len]`, 值域 [0, 1]\n  - p_r(t) = 0: token t 不会被恢复, 正常压缩\n  - p_r(t) = 1: token t 必定被恢复, 可分配 0 bits (极端情况)\n  - p_r(t) ∈ (0, 1): 按概率加权降低该 token 的 error 权重\n\n### 5.4 修改复杂度评估\n\n| 文件 | 函数 | 改动行数 | 难度 |\n|------|------|---------|------|\n| `quantize.py` | `dp_bit_allocation` | ~10 行 (新增 weighted_ev 路径) | 低 |\n| `gpu_ops.py` | `greedy_bit_allocation` | ~5 行 (传入 weighted_ev) | 低 |\n| `pipeline.py` | `compress` | ~15 行 (参数 + weighted_ev 计算) | 低 |\n| `pipeline_fast.py` | `compress` | ~15 行 (同上) | 低 |\n| 新增 | `compute_restoration_weighted_eigenvalues` | ~10 行 | 低 |\n| `common.py` | 数据结构 | 0 行 (不需要改) | — |\n| `entropy.py` | — | 0 行 | — |\n\n**总改动: ~55 行代码**, 主要集中在 bit allocation 调用处。不影响量化/编码/解码逻辑。\n\n### 5.5 代码 Diff 草稿\n\n```diff\n--- a/src/quantize.py\n+++ b/src/quantize.py\n@@ -1,5 +1,6 @@\n \"\"\"Quantization utilities for KVTC.\"\"\"\n \n+from __future__ import annotations\n from typing import List\n import torch\n from .common import QuantizationParams\n@@ -12,6 +13,20 @@\n     return [eigenvalues[i : i + group_size] for i in range(0, eigenvalues.numel(), group_size)]\n \n \n+def compute_restoration_weighted_eigenvalues(\n+    pca_coeffs: torch.Tensor,\n+    restoration_probs: torch.Tensor,\n+) -> torch.Tensor:\n+    \"\"\"Compute RABA weighted eigenvalues.\n+    \n+    weighted_lambda_i = mean_t[(1 - p_r(t)) * pca_coeffs[t, i]^2]\n+    \"\"\"\n+    weights = (1 - restoration_probs).unsqueeze(1)  # [T, 1]\n+    weighted_var = (weights * pca_coeffs ** 2).mean(dim=0)  # [dim]\n+    return weighted_var\n+\n+\n def dp_bit_allocation(\n     eigenvalues: torch.Tensor,\n     bit_budget: int,\n```\n\n```diff\n--- a/src/pipeline_fast.py\n+++ b/src/pipeline_fast.py\n@@ -37,7 +37,7 @@\n-    def compress(self, kv_cache, positions):\n+    def compress(self, kv_cache, positions, restoration_probs=None):\n         # ... (unchanged until after PCA transform) ...\n \n                         pca_values = pca_transform(centered, ev)\n \n+                        # RABA: use weighted eigenvalues if restoration probs provided\n+                        if restoration_probs is not None:\n+                            pr = restoration_probs.to(pca_values.device)\n+                            pr_expanded = pr.repeat_interleave(group_heads)\n+                            weighted_ev = compute_restoration_weighted_eigenvalues(\n+                                pca_values, pr_expanded\n+                            )\n+                            bit_widths = greedy_bit_allocation(weighted_ev, entry.bit_budget)\n+                        else:\n-                        bit_widths = greedy_bit_allocation(\n-                            entry.eigenvalues.to(rows.device), entry.bit_budget,\n-                        )\n+                            bit_widths = greedy_bit_allocation(\n+                                entry.eigenvalues.to(rows.device), entry.bit_budget,\n+                            )\n```\n\n### 5.6 不影响的模块\n\n- **PCA transform/inverse**: 不受影响, 仍用相同 eigenvectors\n- **Quantization**: 不受影响, 仍用 uniform affine quantization\n- **Entropy coding**: 不受影响, 仍对量化后的 bytes 做压缩\n- **RoPE**: 不受影响\n- **Token protection** (sink/window): 不受影响\n- **Decompression**: 不受影响, metadata 中已存储 bit_widths\n\n---\n\n## 6. 压缩比评估\n\n### 6.1 Benchmark 数据 (RTX 5090, Qwen2.5-7B)\n\n| Config | K bits | V bits | 压缩比 | K Cosine | V Cosine | 质量 |\n|--------|--------|--------|:------:|:--------:|:--------:|------|\n| K1V2-FULL | 1 | 2 | **12.8x** | 0.9925 | 0.9120 | 低 |\n| K1V3-FULL | 1 | 3 | **8.9x** | 0.9925 | 0.9874 | 可用 |\n| K1V4-FULL | 1 | 4 | **7.1x** | 0.9925 | 0.9974 | 优 |\n| K2V3-FULL | 2 | 3 | **7.2x** | 0.9970 | 0.9874 | 可用 |\n| K2V4-FULL | 2 | 4 | **5.9x** | 0.9970 | 0.9974 | 优 |\n| K3V4-FULL | 3 | 4 | **5.0x** | 0.9993 | 0.9974 | 优 |\n\n### 6.2 8x 压缩比可达性评估\n\n**K1V3 配置达到 8.9x**, cosine similarity 0.987-0.993, 质量为 \"Good\"。\n\n**RABA 对 8x 目标的影响**:\n- RABA 会让部分 token 分配更少 bits (高 p_r tokens) → 平均 bits 降低 → 压缩比提升\n- 但总 bit budget 不变, 只是重分配: 高 p_r tokens 少分, 低 p_r tokens 多分\n- 净效应: 如果大量 tokens 有高 p_r, 可以用更少的 bit budget 达到相同重建质量 → **提升有效压缩比**\n- 在 K2V4 基础上 + RABA (假设 50% tokens 有 p_r > 0.5), 有效压缩比可达 7-9x 同时保持更高质量\n\n**结论**: 8x 在 KVTC 可达范围内。K1V3 直接达到 8.9x, K2V4 + RABA 可在保持更高质量的同时逼近 8x。\n\n### 6.3 Benchmark 脚本\n\n```bash\n# 完整 benchmark\npython benchmarks/benchmark_v4.py --model Qwen/Qwen2.5-7B-Instruct --device cuda\n\n# 指定配置\npython benchmarks/benchmark_v3.py --model meta-llama/Llama-3.1-8B-Instruct --device cuda\n\n# 单元测试 (无需 GPU)\npytest src/test_kvtc.py -v\n```\n\n---\n\n## 7. Entropy Coding 流程\n\n### 7.1 编码方法\n\n三种编码器, triple-mode picker 选最小:\n\n| 编码器 | 文件 | 说明 |\n|--------|------|------|\n| **zlib (DEFLATE)** | `entropy.py` | 默认, 压缩 level 6-9 |\n| **LZMA2** | `ans_entropy.py:compress_best()` | Python `lzma` module |\n| **rANS** | `ans_entropy.py:rans_encode()` | 纯 Python 实现, 16-bit precision |\n\nTriple picker (`ans_entropy.py:184-230`):\n```python\ndef compress_best(packed_bytes, level=6):\n    candidates = []\n    candidates.append((b\"Z\" + zlib.compress(packed_bytes, 9), \"zlib\"))\n    candidates.append((b\"L\" + lzma.compress(packed_bytes, preset=6), \"lzma\"))\n    candidates.append((b\"A\" + rans_encode(packed_bytes), \"rans\"))\n    best = min(candidates, key=lambda x: len(x[0]))\n    return best[0], ratio\n```\n\n1-byte tag 前缀标识编码器: `Z`=zlib, `L`=LZMA, `A`=rANS.\n\n### 7.2 编解码 API\n\n**编码**:\n```python\nfrom src.entropy import pack_bits, compress\nfrom src.ans_entropy import compress_best\n\n# Step 1: 将量化 indices 打包为 bytes\npacked = pack_bits(indices_list, bit_widths)\n\n# Step 2a: zlib 压缩\ncompressed, ratio = compress(packed, level=6)\n\n# Step 2b: 或用 triple picker\ncompressed, ratio = compress_best(packed, level=6)\n```\n\n**解码**:\n```python\nfrom src.entropy import decompress, unpack_bits\nfrom src.ans_entropy import decompress_best\n\n# Step 1: 解压\npacked = decompress(compressed, original_size)\n# 或 triple picker\npacked = decompress_best(compressed, original_size)\n\n# Step 2: 解包\nindices_list = unpack_bits(packed, bit_widths, lengths)\n```\n\n### 7.3 Bit Packing\n\n`entropy.py:47-83`: 按 component 顺序逐个打包 (comp 0 所有 rows, 然后 comp 1, ...), 变宽 bit stream, 无对齐要求。\n\nGPU 加速版在 `gpu_ops.py:fast_pack_bits()` 和 `triton_kernels.py:gpu_pack_variable_width()`。\n\n---\n\n## 8. Adaptive Budget (per-layer)\n\n### 8.1 原理\n\n`adaptive_budget.py`: 不同 layer 的 PCA eigenvalue spectrum \"平坦度\"不同:\n- 平坦 (high Shannon entropy) → 难压缩 → 分配更多 bits\n- 陡峭 (low entropy) → 易压缩 → 分配更少 bits\n\n总预算守恒, 只做重分配。\n\n### 8.2 API\n\n```python\nfrom src.adaptive_budget import apply_adaptive_budgets\n\nkey_diff, val_diff = apply_adaptive_budgets(\n    calibration, key_bits_avg=2, value_bits_avg=4, strength=1.0\n)\n```\n\n`strength=0` 为均匀分配, `strength=1` 为完全自适应。\n\n---\n\n## 9. 集成风险和注意事项\n\n### 9.1 RABA 集成风险\n\n| 风险 | 说明 | 缓解 |\n|------|------|------|\n| **DP 粒度不匹配** | DP 是 per-component, p_r 是 per-token | 用方案 B: 预聚合 weighted eigenvalues |\n| **p_r 精度要求** | p_r 误估可能导致分配不当 | 加 clamp(0.01, 0.99) 防极端值 |\n| **与 adaptive budget 交互** | RABA 和 adaptive budget 都改 bit allocation | 两者正交: adaptive 改 per-layer budget, RABA 改 per-component allocation |\n| **解压不需要 p_r** | metadata 中已存 bit_widths | 正确, 解压路径零改动 |\n| **Calibration 兼容** | RABA 修改运行时 bit allocation, 不改 calibration | 完全兼容, 无需重新 calibrate |\n\n### 9.2 性能影响\n\n- 压缩时增加 `weighted_eigenvalue` 计算: 一次矩阵乘 `O(T × d)`, 可忽略\n- Bit allocation (贪心版) 运行时间不变\n- 解压路径零开销\n\n### 9.3 代码质量观察\n\n- 代码组织清晰, pipeline → pca → quantize → entropy 模块化良好\n- 两个 pipeline (参考 + GPU) 保持接口一致, 修改一个的经验可直接复用\n- 38 个测试覆盖所有核心功能, 添加 RABA 后应增加对应测试\n- `group_size=1` 默认设置意味着 per-head PCA, 对 RABA 的 per-token weight 聚合较友好\n\n### 9.4 推荐实施顺序\n\n1. 在 `quantize.py` 新增 `compute_restoration_weighted_eigenvalues()` 函数\n2. 修改 `pipeline.py` (参考版) 的 `compress()` 方法, 添加 RABA 支持\n3. 编写单元测试: weighted eigenvalues 计算正确性, RABA bit allocation 向后兼容 (p_r=0 时等价原版)\n4. 验证: p_r=0 应产生与原版完全相同的 bit allocation\n5. 修改 `pipeline_fast.py` (GPU 版)\n6. 端到端测试: 带 RABA 的压缩-解压 roundtrip\n"
  }
}
````

</details>

---

### Tool result

_source line 44 · 2026-05-14T04:28:51.280959+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/kvtc_survey.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-14T04:28:51.281130+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "KVTC 代码库深度调研报告",
  "type": "report",
  "description": "OnlyTerp/kvtc 代码库全面调研: 架构分析、DP solver 详解 (quantize.py:16-56)、error function 确认 (variance/4^bits)、RABA 修改方案 (含代码 diff, ~55 行改动)、压缩比评估 (8x 可达)、entropy coding 流程、集成风险分析",
  "project": "distill_kv_rag_cache",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/kvtc_survey.md",
  "tags": "['kvtc', 'survey', 'raba', 'dp-solver', 'kv-cache-compression']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "KVTC 代码库深度调研报告",
    "type": "report",
    "description": "OnlyTerp/kvtc 代码库全面调研: 架构分析、DP solver 详解 (quantize.py:16-56)、error function 确认 (variance/4^bits)、RABA 修改方案 (含代码 diff, ~55 行改动)、压缩比评估 (8x 可达)、entropy coding 流程、集成风险分析",
    "project": "distill_kv_rag_cache",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/kvtc_survey.md",
    "tags": "['kvtc', 'survey', 'raba', 'dp-solver', 'kv-cache-compression']"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-14T04:28:51.281300+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_43a9d0\", \"name\": \"KVTC 代码库深度调研报告\", \"type\": \"report\", \"description\": \"OnlyTerp/kvtc 代码库全面调研: 架构分析、DP solver 详解 (quantize.py:16-56)、error function 确认 (variance/4^bits)、RABA 修改方案 (含代码 diff, ~55 行改动)、压缩比评估 (8x 可达)、entropy coding 流程、集成风险分析\", \"path\": \"projects/distill_kv_rag_cache/artifacts/_project/report/kvtc_survey.md\", \"url\": null, \"project\": \"distill_kv_rag_cache\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T04:28:38.748513+00:00\", \"tags\": [\"kvtc\", \"survey\", \"raba\", \"dp-solver\", \"kv-cache-compression\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_kvtc-code-survey_20260514T042154",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-14T04:28:51.281498+00:00_

调研完成。核心发现:

**DP Solver**: `src/quantize.py:16-56`, error function 确认为 `λ_i / 4^b`。生产用贪心版在 `src/gpu_ops.py:10-57`。两者数学等价。

**RABA 修改方案**: ~55 行代码, 集中在 bit allocation 调用处。推荐方案 B——预聚合 weighted eigenvalues `weighted_λ_i = mean_t[(1 - p_r(t)) × pca_coeffs[t,i]²]`, 然后传入现有 DP/greedy allocator。不改量化、编码、解压路径。

**压缩比**: K1V3 配置直接达 8.9x (cosine ~0.987)。K2V4 + RABA 可在保持更高质量同时逼近 8x。

**关键低风险点**: 解压路径零改动 (bit_widths 已存 metadata), calibration 完全兼容, 与 adaptive budget 正交。

报告已注册为 artifact `art_20260514_43a9d0`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_kvtc-code-survey_20260514T042154"
}
```

</details>

---
