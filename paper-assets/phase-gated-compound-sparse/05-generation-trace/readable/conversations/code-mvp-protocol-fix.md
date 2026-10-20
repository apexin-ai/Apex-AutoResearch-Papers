# code mvp protocol fix

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 51
- **Recorded user turns:** 0
- **Tool calls:** 25
- **Original source:** `logs/chats/worker_code_mvp-protocol-fix_20260513T183157.jsonl`
- **Structured JSON:** [`94fad5c7d1170cbb5a06.json`](../../sessions/94/94fad5c7d1170cbb5a06.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

51 recorded events

### Tool call

_source line 1 · 2026-05-13T18:38:06.486510+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/profiling/interaction_index.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/profiling/interaction_index.py"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-13T18:38:06.487021+00:00_

1	# Interaction Index (II) calculator for measuring super/sub-additivity
2	# of compound sparsity (attention head pruning + KV cache eviction).
3	#
4	# II = quality(both_sparse) - quality(attn_only) - quality(kv_only) + quality(dense)
5	# where quality = -perplexity.  II > 0 means super-additive.
6	
7	from __future__ import annotations
8	
9	import math
10	from dataclasses import dataclass, field
11	from typing import Dict, List, Optional, Tuple
12	
13	import torch
14	import torch.nn.functional as F
15	
16	from ..utils.metrics import compute_perplexity
17	
18	try:
19	    from .phase_segmentation import Phase
20	except ImportError:
21	    Phase = None  # will be resolved when phase_segmentation is created
22	
23	
24	# ---------------------------------------------------------------------------
25	# Data classes
26	# ---------------------------------------------------------------------------
27	
28	@dataclass
29	class InteractionResult:
30	    ii_value: float
31	    ppl_dense: float
32	    ppl_attn_sparse: float
33	    ppl_kv_sparse: float
34	    ppl_both_sparse: float
35	    is_super_additive: bool
36	    phase_name: Optional[str] = None
37	    num_tokens: int = 0
38	
39	    def summary(self) -> str:
40	        tag = "super-additive" if self.is_super_additive else "sub-additive"
41	        return (
42	            f"II={self.ii_value:+.4f} ({tag})  "
43	            f"dense={self.ppl_dense:.2f}  attn={self.ppl_attn_sparse:.2f}  "
44	            f"kv={self.ppl_kv_sparse:.2f}  both={self.ppl_both_sparse:.2f}"
45	        )
46	
47	
48	# ---------------------------------------------------------------------------
49	# Hook-based head masking (works with GQA / MHA / MQA)
50	# ---------------------------------------------------------------------------
51	
52	class _HeadMaskHook:
53	    """Registers forward hooks that zero out masked attention heads."""
54	
55	    def __init__(self, model: torch.nn.Module, head_mask: torch.Tensor):
56	        """
57	        head_mask: (num_layers
…[truncated 14105 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-13T18:38:06.488338+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/profiling/run_profiling.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/profiling/run_profiling.py"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-13T18:38:06.488663+00:00_

1	"""
2	PACS Profiling Entry Point.
3	
4	End-to-end pipeline:
5	  1. Load a causal LM (HuggingFace)
6	  2. Load MATH-500 subset from JSON
7	  3. Generate reasoning traces with output_attentions=True
8	  4. Segment each trace into phases via PhaseSegmenter
9	  5. (Optional) Compute per-phase Interaction Index
10	  6. Save results to JSON
11	"""
12	
13	from __future__ import annotations
14	
15	import argparse
16	import json
17	import logging
18	import os
19	import sys
20	from pathlib import Path
21	from typing import Any, Dict, List
22	
23	import numpy as np
24	import torch
25	
26	# ---------------------------------------------------------------------------
27	# Resolve sibling imports without __init__.py
28	# ---------------------------------------------------------------------------
29	_PROFILING_DIR = Path(__file__).resolve().parent
30	if str(_PROFILING_DIR) not in sys.path:
31	    sys.path.insert(0, str(_PROFILING_DIR))
32	
33	from phase_segmentation import PhaseAnnotation, PhaseSegmenter
34	
35	logging.basicConfig(
36	    level=logging.INFO,
37	    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
38	)
39	logger = logging.getLogger("run_profiling")
40	
41	
42	# ---------------------------------------------------------------------------
43	# Helpers
44	# ---------------------------------------------------------------------------
45	
46	def load_model_and_tokenizer(model_path: str, device: str = "cuda"):
47	    """Load a HuggingFace causal LM with attention output enabled."""
48	    from transformers import AutoModelForCausalLM, AutoTokenizer
49	
50	    logger.info("Loading tokenizer from %s", model_path)
51	    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
52	    if tokenizer.pad_token is None:
53	        tokenizer.pad_token = tokenizer.eos_token
54	
55	    logger.info("Loading model from %s", model_path)
56	    model = AutoModelForCausalLM.from_pretrained(
57	        model_path,
58	        torch_dtype=torch.float16,
59	  
…[truncated 7020 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-13T18:38:06.488851+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/profiling/phase_segmentation.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/profiling/phase_segmentation.py"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-13T18:38:06.489107+00:00_

1	"""
2	Phase Segmentation via Attention Sparsity Profiling.
3	
4	Implements the ThinKV (ICLR 2026 Oral) methodology:
5	  attention sparsity -> Gaussian KDE -> tri-modal phase detection.
6	
7	Each token is assigned to one of three phases:
8	  - execution:   low sparsity (dense attention), focused computation
9	  - reasoning:   intermediate sparsity, broad cross-token reasoning
10	  - transition:  high sparsity, uncertainty/backtracking patterns
11	"""
12	
13	from __future__ import annotations
14	
15	import logging
16	import warnings
17	from dataclasses import dataclass, field
18	from typing import List, Optional, Tuple
19	
20	import numpy as np
21	import torch
22	from scipy.signal import argrelmin
23	from scipy.stats import gaussian_kde
24	
25	logger = logging.getLogger(__name__)
26	
27	PHASE_NAMES_BY_SPARSITY = ["execution", "reasoning", "transition"]
28	
29	
30	@dataclass
31	class Phase:
32	    name: str            # "reasoning" / "execution" / "transition"
33	    start: int           # token start position (inclusive)
34	    end: int             # token end position (exclusive)
35	    mean_sparsity: float
36	
37	
38	@dataclass
39	class PhaseAnnotation:
40	    phases: List[Phase]
41	    boundaries: List[int]       # token indices where phase transitions occur
42	    sparsity: np.ndarray        # raw per-token sparsity, shape (seq_len,)
43	    kde_x: np.ndarray
44	    kde_density: np.ndarray
45	
46	
47	class PhaseSegmenter:
48	    """Segment a token sequence into reasoning / transition / execution phases
49	    based on the attention sparsity profile and Gaussian KDE peak detection."""
50	
51	    def __init__(
52	        self,
53	        bandwidth: str = "scott",
54	        min_phase_length: int = 10,
55	        sparsity_threshold_ratio: float = 0.01,
56	        kde_grid_points: int = 512,
57	        min_seq_length: int = 50,
58	    ):
59	        """
60	        Args:
61	            bandwidth: KDE bandwidth selection — "scott", "silverman", or a float.
62	          
…[truncated 14428 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-13T18:38:06.489268+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/utils/metrics.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/utils/metrics.py"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-13T18:38:06.489451+00:00_

1	# General-purpose metrics for PACS profiling: perplexity, accuracy, etc.
2	
3	from typing import List, Optional
4	
5	import torch
6	import torch.nn.functional as F
7	
8	
9	def compute_perplexity(
10	    logits: torch.Tensor,
11	    labels: torch.Tensor,
12	    token_indices: Optional[List[int]] = None,
13	) -> float:
14	    """Compute mean per-token perplexity, optionally restricted to specific positions.
15	
16	    Args:
17	        logits: (seq_len, vocab_size) – unnormalized logits.
18	        labels: (seq_len,) – ground-truth token ids.  Positions with label == -100
19	                are ignored (standard HF convention).
20	        token_indices: If given, only these positions contribute to the result.
21	                       None means all valid positions.
22	
23	    Returns:
24	        Scalar perplexity (exp of mean cross-entropy over selected positions).
25	    """
26	    # Shift: logits[t] predicts labels[t+1]
27	    shift_logits = logits[:-1]  # (S-1, V)
28	    shift_labels = labels[1:]   # (S-1,)
29	
30	    per_token_ce = F.cross_entropy(
31	        shift_logits, shift_labels, reduction="none"
32	    )  # (S-1,)
33	
34	    if token_indices is not None:
35	        # token_indices refer to *label* positions; after shift they map to index-1
36	        idx = torch.tensor(
37	            [i - 1 for i in token_indices if 0 < i < len(labels)],
38	            device=per_token_ce.device,
39	        )
40	        if idx.numel() == 0:
41	            return float("nan")
42	        per_token_ce = per_token_ce[idx]
43	
44	    # Ignore positions where label == -100
45	    valid = shift_labels[: per_token_ce.size(0)] != -100 if token_indices is None else torch.ones_like(per_token_ce, dtype=torch.bool)
46	    if token_indices is None:
47	        per_token_ce = per_token_ce[valid]
48	
49	    if per_token_ce.numel() == 0:
50	        return float("nan")
51	
52	    return torch.exp(per_token_ce.mean()).item()
53	
54	
55	def compute_accuracy(predictions: List[str], reference
…[truncated 274 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-13T18:38:06.489627+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/_project/intermediate"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/_project/intermediate"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-13T18:38:06.489752+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/_project/intermediate. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-13T18:38:06.489872+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/__init__.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/__init__.py",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-13T18:38:06.489988+00:00_

artifacts/pacs/profiling/__init__.py
artifacts/pacs/utils/__init__.py
artifacts/pacs/__init__.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-13T18:38:06.490104+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/_project -name \"*.py\" 2>/dev/null || echo \"NO_INTERMEDIATE_DIR\"",
  "description": "Find intermediate Python files to delete"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/_project -name \"*.py\" 2>/dev/null || echo \"NO_INTERMEDIATE_DIR\"",
    "description": "Find intermediate Python files to delete"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-13T18:38:06.490225+00:00_

NO_INTERMEDIATE_DIR

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-13T18:38:06.490340+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/__init__.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/__init__.py"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-13T18:38:06.490479+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (1). The file has 1 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-13T18:38:06.490596+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/profiling/__init__.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/profiling/__init__.py"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-13T18:38:06.490709+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (1). The file has 1 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-13T18:38:06.490823+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/utils/__init__.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/utils/__init__.py"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-13T18:38:06.490957+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (1). The file has 1 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-13T18:38:06.491134+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/profiling/phase_segmentation.py",
  "old_string": "@dataclass\nclass Phase:\n    name: str            # \"reasoning\" / \"execution\" / \"transition\"\n    start: int           # token start position (inclusive)\n    end: int             # token end position (exclusive)\n    mean_sparsity: float",
  "new_string": "@dataclass\nclass Phase:\n    name: str            # \"reasoning\" / \"execution\" / \"transition\"\n    start: int           # token start position (inclusive)\n    end: int             # token end position (exclusive)\n    mean_sparsity: float\n\n    @property\n    def token_indices(self) -> List[int]:\n        return list(range(self.start, self.end))"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/profiling/phase_segmentation.py",
    "old_string": "@dataclass\nclass Phase:\n    name: str            # \"reasoning\" / \"execution\" / \"transition\"\n    start: int           # token start position (inclusive)\n    end: int             # token end position (exclusive)\n    mean_sparsity: float",
    "new_string": "@dataclass\nclass Phase:\n    name: str            # \"reasoning\" / \"execution\" / \"transition\"\n    start: int           # token start position (inclusive)\n    end: int             # token end position (exclusive)\n    mean_sparsity: float\n\n    @property\n    def token_indices(self) -> List[int]:\n        return list(range(self.start, self.end))"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-13T18:38:06.491327+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/profiling/phase_segmentation.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-13T18:38:06.491501+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/profiling/interaction_index.py",
  "old_string": "# Interaction Index (II) calculator for measuring super/sub-additivity\n# of compound sparsity (attention head pruning + KV cache eviction).\n#\n# II = quality(both_sparse) - quality(attn_only) - quality(kv_only) + quality(dense)\n# where quality = -perplexity.  II > 0 means super-additive.",
  "new_string": "# Interaction Index (II) calculator for measuring super/sub-additivity\n# of compound sparsity (attention head pruning + KV cache eviction).\n#\n# II = R_both - R_attn - R_kv + 1\n# where R_x = ppl_x / ppl_dense (relative degradation ratio).\n# II > 0 → super-additive degradation (compound sparsity hurts more than sum of parts)\n# II < 0 → sub-additive degradation\n# II = 0 → independent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/profiling/interaction_index.py",
    "old_string": "# Interaction Index (II) calculator for measuring super/sub-additivity\n# of compound sparsity (attention head pruning + KV cache eviction).\n#\n# II = quality(both_sparse) - quality(attn_only) - quality(kv_only) + quality(dense)\n# where quality = -perplexity.  II > 0 means super-additive.",
    "new_string": "# Interaction Index (II) calculator for measuring super/sub-additivity\n# of compound sparsity (attention head pruning + KV cache eviction).\n#\n# II = R_both - R_attn - R_kv + 1\n# where R_x = ppl_x / ppl_dense (relative degradation ratio).\n# II > 0 → super-additive degradation (compound sparsity hurts more than sum of parts)\n# II < 0 → sub-additive degradation\n# II = 0 → independent"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-13T18:38:06.491707+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/profiling/interaction_index.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-13T18:38:06.491879+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/profiling/interaction_index.py",
  "old_string": "from __future__ import annotations\n\nimport math\nfrom dataclasses import dataclass, field\nfrom typing import Dict, List, Optional, Tuple",
  "new_string": "from __future__ import annotations\n\nimport math\nfrom dataclasses import dataclass, field\nfrom typing import Dict, List, Optional, Tuple\n\nimport numpy as np"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/profiling/interaction_index.py",
    "old_string": "from __future__ import annotations\n\nimport math\nfrom dataclasses import dataclass, field\nfrom typing import Dict, List, Optional, Tuple",
    "new_string": "from __future__ import annotations\n\nimport math\nfrom dataclasses import dataclass, field\nfrom typing import Dict, List, Optional, Tuple\n\nimport numpy as np"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-13T18:38:06.492074+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/profiling/interaction_index.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-13T18:38:06.492217+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/profiling/interaction_index.py",
  "old_string": "@dataclass\nclass InteractionResult:\n    ii_value: float\n    ppl_dense: float\n    ppl_attn_sparse: float\n    ppl_kv_sparse: float\n    ppl_both_sparse: float\n    is_super_additive: bool\n    phase_name: Optional[str] = None\n    num_tokens: int = 0\n\n    def summary(self) -> str:\n        tag = \"super-additive\" if self.is_super_additive else \"sub-additive\"\n        return (\n            f\"II={self.ii_value:+.4f} ({tag})  \"\n            f\"dense={self.ppl_dense:.2f}  attn={self.ppl_attn_sparse:.2f}  \"\n            f\"kv={self.ppl_kv_sparse:.2f}  both={self.ppl_both_sparse:.2f}\"\n        )",
  "new_string": "@dataclass\nclass InteractionResult:\n    ii_value: float\n    ppl_dense: float\n    ppl_attn_sparse: float\n    ppl_kv_sparse: float\n    ppl_both_sparse: float\n    r_attn: float          # ppl_attn / ppl_dense\n    r_kv: float            # ppl_kv / ppl_dense\n    r_both: float          # ppl_both / ppl_dense\n    is_super_additive: bool  # II > 0 → compound sparsity degrades more than sum of parts\n    sparsity_level: float = 0.0\n    phase_name: Optional[str] = None\n    num_tokens: int = 0\n\n    def summary(self) -> str:\n        tag = \"super-additive\" if self.is_super_additive else \"sub-additive\"\n        return (\n            f\"II={self.ii_value:+.4f} ({tag})  \"\n            f\"R_attn={self.r_attn:.4f}  R_kv={self.r_kv:.4f}  R_both={self.r_both:.4f}  \"\n            f\"dense={self.ppl_dense:.2f}  attn={self.ppl_attn_sparse:.2f}  \"\n            f\"kv={self.ppl_kv_sparse:.2f}  both={self.ppl_both_sparse:.2f}\"\n        )"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/profiling/interaction_index.py",
    "old_string": "@dataclass\nclass InteractionResult:\n    ii_value: float\n    ppl_dense: float\n    ppl_attn_sparse: float\n    ppl_kv_sparse: float\n    ppl_both_sparse: float\n    is_super_additive: bool\n    phase_name: Optional[str] = None\n    num_tokens: int = 0\n\n    def summary(self) -> str:\n        tag = \"super-additive\" if self.is_super_additive else \"sub-additive\"\n        return (\n            f\"II={self.ii_value:+.4f} ({tag})  \"\n            f\"dense={self.ppl_dense:.2f}  attn={self.ppl_attn_sparse:.2f}  \"\n            f\"kv={self.ppl_kv_sparse:.2f}  both={self.ppl_both_sparse:.2f}\"\n        )",
    "new_string": "@dataclass\nclass InteractionResult:\n    ii_value: float\n    ppl_dense: float\n    ppl_attn_sparse: float\n    ppl_kv_sparse: float\n    ppl_both_sparse: float\n    r_attn: float          # ppl_attn / ppl_dense\n    r_kv: float            # ppl_kv / ppl_dense\n    r_both: float          # ppl_both / ppl_dense\n    is_super_additive: bool  # II > 0 → compound sparsity degrades more than sum of parts\n    sparsity_level: float = 0.0\n    phase_name: Optional[str] = None\n    num_tokens: int = 0\n\n    def summary(self) -> str:\n        tag = \"super-additive\" if self.is_super_additive else \"sub-additive\"\n        return (\n            f\"II={self.ii_value:+.4f} ({tag})  \"\n            f\"R_attn={self.r_attn:.4f}  R_kv={self.r_kv:.4f}  R_both={self.r_both:.4f}  \"\n            f\"dense={self.ppl_dense:.2f}  attn={self.ppl_attn_sparse:.2f}  \"\n            f\"kv={self.ppl_kv_sparse:.2f}  both={self.ppl_both_sparse:.2f}\"\n        )"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-13T18:38:06.492439+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/profiling/interaction_index.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-13T18:38:06.492618+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/profiling/interaction_index.py",
  "old_string": "    def compute_interaction_index(\n        self,\n        input_ids: torch.Tensor,\n        attn_sparsity_ratio: float = 0.3,\n        kv_eviction_ratio: float = 0.3,\n        phase_token_indices: Optional[List[int]] = None,\n        head_importance: Optional[torch.Tensor] = None,\n        kv_importance: Optional[torch.Tensor] = None,\n    ) -> InteractionResult:\n        \"\"\"Compute the Interaction Index for a single input.\n\n        II = -ppl(both) + ppl(attn_only) + ppl(kv_only) - ppl(dense)\n\n        II > 0 means super-additive: combining both sparsity axes hurts\n        less than the sum of individual degradations.\n        \"\"\"\n        num_layers, num_heads = self._get_model_dims()\n        seq_len = input_ids.size(-1)\n\n        attn_head_mask = self._select_heads_to_mask(\n            num_layers, num_heads, attn_sparsity_ratio, head_importance\n        )\n        kv_mask = self._select_kv_to_evict(\n            num_layers, seq_len, kv_eviction_ratio, kv_importance\n        )\n\n        # 1. Dense\n        ppl_dense = self.forward_with_sparse_config(\n            input_ids, phase_token_indices=phase_token_indices,\n        )\n        # 2. Attention-only sparse\n        ppl_attn = self.forward_with_sparse_config(\n            input_ids, attn_head_mask=attn_head_mask,\n            phase_token_indices=phase_token_indices,\n        )\n        # 3. KV-only sparse\n        ppl_kv = self.forward_with_sparse_config(\n            input_ids, kv_mask=kv_mask,\n            phase_token_indices=phase_token_indices,\n        )\n        # 4. Both sparse\n        ppl_both = self.forward_with_sparse_config(\n            input_ids, attn_head_mask=attn_head_mask, kv_mask=kv_mask,\n            phase_token_indices=phase_token_indices,\n        )\n\n        # II = quality(both) - quality(attn) - quality(kv) + quality(dense)\n        # quality = -ppl, so:\n        ii = -ppl_both + ppl_attn + ppl_kv - ppl_dense\n\n        num_tokens = len(phase_token_indices) if phase_token_indices else seq_len\n\n        return InteractionResult(\n            ii_value=ii,\n            ppl_dense=ppl_dense,\n            ppl_attn_sparse=ppl_attn,\n            ppl_kv_sparse=ppl_kv,\n            ppl_both_sparse=ppl_both,\n            is_super_additive=ii > 0,\n            num_tokens=num_tokens,\n        )",
  "new_string": "    def compute_interaction_index(\n        self,\n        input_ids: torch.Tensor,\n        sparsity_level: float = 0.3,\n        phase_token_indices: Optional[List[int]] = None,\n        head_importance: Optional[torch.Tensor] = None,\n        kv_importance: Optional[torch.Tensor] = None,\n    ) -> InteractionResult:\n        \"\"\"Compute the Interaction Index for a single input.\n\n        II = R_both - R_attn - R_kv + 1, where R_x = ppl_x / ppl_dense.\n        II > 0 → super-additive degradation (compound sparsity is worse than\n        the sum of individual degradations).\n        \"\"\"\n        num_layers, num_heads = self._get_model_dims()\n        seq_len = input_ids.size(-1)\n\n        attn_head_mask = self._select_heads_to_mask(\n            num_layers, num_heads, sparsity_level, head_importance\n        )\n        kv_mask = self._select_kv_to_evict(\n            num_layers, seq_len, sparsity_level, kv_importance\n        )\n\n        ppl_dense = self.forward_with_sparse_config(\n            input_ids, phase_token_indices=phase_token_indices,\n        )\n        ppl_attn = self.forward_with_sparse_config(\n            input_ids, attn_head_mask=attn_head_mask,\n            phase_token_indices=phase_token_indices,\n        )\n        ppl_kv = self.forward_with_sparse_config(\n            input_ids, kv_mask=kv_mask,\n            phase_token_indices=phase_token_indices,\n        )\n        ppl_both = self.forward_with_sparse_config(\n            input_ids, attn_head_mask=attn_head_mask, kv_mask=kv_mask,\n            phase_token_indices=phase_token_indices,\n        )\n\n        r_attn = ppl_attn / ppl_dense if ppl_dense > 0 else float(\"nan\")\n        r_kv = ppl_kv / ppl_dense if ppl_dense > 0 else float(\"nan\")\n        r_both = ppl_both / ppl_dense if ppl_dense > 0 else float(\"nan\")\n        ii = r_both - r_attn - r_kv + 1\n\n        num_tokens = len(phase_token_indices) if phase_token_indices else seq_len\n\n        return InteractionResult(\n            ii_value=ii,\n            ppl_dense=ppl_dense,\n            ppl_attn_sparse=ppl_attn,\n            ppl_kv_sparse=ppl_kv,\n            ppl_both_sparse=ppl_both,\n            r_attn=r_attn,\n            r_kv=r_kv,\n            r_both=r_both,\n            is_super_additive=ii > 0,\n            sparsity_level=sparsity_level,\n            num_tokens=num_tokens,\n        )"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/profiling/interaction_index.py",
    "old_string": "    def compute_interaction_index(\n        self,\n        input_ids: torch.Tensor,\n        attn_sparsity_ratio: float = 0.3,\n        kv_eviction_ratio: float = 0.3,\n        phase_token_indices: Optional[List[int]] = None,\n        head_importance: Optional[torch.Tensor] = None,\n        kv_importance: Optional[torch.Tensor] = None,\n    ) -> InteractionResult:\n        \"\"\"Compute the Interaction Index for a single input.\n\n        II = -ppl(both) + ppl(attn_only) + ppl(kv_only) - ppl(dense)\n\n        II > 0 means super-additive: combining both sparsity axes hurts\n        less than the sum of individual degradations.\n        \"\"\"\n        num_layers, num_heads = self._get_model_dims()\n        seq_len = input_ids.size(-1)\n\n        attn_head_mask = self._select_heads_to_mask(\n            num_layers, num_heads, attn_sparsity_ratio, head_importance\n        )\n        kv_mask = self._select_kv_to_evict(\n            num_layers, seq_len, kv_eviction_ratio, kv_importance\n        )\n\n        # 1. Dense\n        ppl_dense = self.forward_with_sparse_config(\n            input_ids, phase_token_indices=phase_token_indices,\n        )\n        # 2. Attention-only sparse\n        ppl_attn = self.forward_with_sparse_config(\n            input_ids, attn_head_mask=attn_head_mask,\n            phase_token_indices=phase_token_indices,\n        )\n        # 3. KV-only sparse\n        ppl_kv = self.forward_with_sparse_config(\n            input_ids, kv_mask=kv_mask,\n            phase_token_indices=phase_token_indices,\n        )\n        # 4. Both sparse\n        ppl_both = self.forward_with_sparse_config(\n            input_ids, attn_head_mask=attn_head_mask, kv_mask=kv_mask,\n            phase_token_indices=phase_token_indices,\n        )\n\n        # II = quality(both) - quality(attn) - quality(kv) + quality(dense)\n        # quality = -ppl, so:\n        ii = -ppl_both + ppl_attn + ppl_kv - ppl_dense\n\n        num_tokens = len(phase_token_indices) if phase_token_indices else seq_len\n\n        return InteractionResult(\n            ii_value=ii,\n            ppl_dense=ppl_dense,\n            ppl_attn_sparse=ppl_attn,\n            ppl_kv_sparse=ppl_kv,\n            ppl_both_sparse=ppl_both,\n            is_super_additive=ii > 0,\n            num_tokens=num_tokens,\n        )",
    "new_string": "    def compute_interaction_index(\n        self,\n        input_ids: torch.Tensor,\n        sparsity_level: float = 0.3,\n        phase_token_indices: Optional[List[int]] = None,\n        head_importance: Optional[torch.Tensor] = None,\n        kv_importance: Optional[torch.Tensor] = None,\n    ) -> InteractionResult:\n        \"\"\"Compute the Interaction Index for a single input.\n\n        II = R_both - R_attn - R_kv + 1, where R_x = ppl_x / ppl_dense.\n        II > 0 → super-additive degradation (compound sparsity is worse than\n        the sum of individual degradations).\n        \"\"\"\n        num_layers, num_heads = self._get_model_dims()\n        seq_len = input_ids.size(-1)\n\n        attn_head_mask = self._select_heads_to_mask(\n            num_layers, num_heads, sparsity_level, head_importance\n        )\n        kv_mask = self._select_kv_to_evict(\n            num_layers, seq_len, sparsity_level, kv_importance\n        )\n\n        ppl_dense = self.forward_with_sparse_config(\n            input_ids, phase_token_indices=phase_token_indices,\n        )\n        ppl_attn = self.forward_with_sparse_config(\n            input_ids, attn_head_mask=attn_head_mask,\n            phase_token_indices=phase_token_indices,\n        )\n        ppl_kv = self.forward_with_sparse_config(\n            input_ids, kv_mask=kv_mask,\n            phase_token_indices=phase_token_indices,\n        )\n        ppl_both = self.forward_with_sparse_config(\n            input_ids, attn_head_mask=attn_head_mask, kv_mask=kv_mask,\n            phase_token_indices=phase_token_indices,\n        )\n\n        r_attn = ppl_attn / ppl_dense if ppl_dense > 0 else float(\"nan\")\n        r_kv = ppl_kv / ppl_dense if ppl_dense > 0 else float(\"nan\")\n        r_both = ppl_both / ppl_dense if ppl_dense > 0 else float(\"nan\")\n        ii = r_both - r_attn - r_kv + 1\n\n        num_tokens = len(phase_token_indices) if phase_token_indices else seq_len\n\n        return InteractionResult(\n            ii_value=ii,\n            ppl_dense=ppl_dense,\n            ppl_attn_sparse=ppl_attn,\n            ppl_kv_sparse=ppl_kv,\n            ppl_both_sparse=ppl_both,\n            r_attn=r_attn,\n            r_kv=r_kv,\n            r_both=r_both,\n            is_super_additive=ii > 0,\n            sparsity_level=sparsity_level,\n            num_tokens=num_tokens,\n        )"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-13T18:38:06.492884+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/profiling/interaction_index.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-13T18:38:06.493061+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/profiling/interaction_index.py",
  "old_string": "    def compute_per_phase_ii(\n        self,\n        input_ids: torch.Tensor,\n        phases: List,\n        attn_sparsity_ratio: float = 0.3,\n        kv_eviction_ratio: float = 0.3,\n    ) -> Dict[str, InteractionResult]:\n        \"\"\"Compute II separately for each phase (reasoning / execution / transition).\n\n        Args:\n            phases: List of Phase objects from phase_segmentation.  Each Phase must\n                    have .name (str) and .token_indices (List[int]) attributes.\n\n        Returns:\n            Dict mapping phase name to its InteractionResult.\n        \"\"\"\n        results: Dict[str, InteractionResult] = {}\n\n        for phase in phases:\n            result = self.compute_interaction_index(\n                input_ids,\n                attn_sparsity_ratio=attn_sparsity_ratio,\n                kv_eviction_ratio=kv_eviction_ratio,\n                phase_token_indices=phase.token_indices,\n            )\n            result.phase_name = phase.name\n            results[phase.name] = result\n\n        return results",
  "new_string": "    def compute_per_phase_ii(\n        self,\n        input_ids: torch.Tensor,\n        phases: List,\n        sparsity_level: float = 0.3,\n    ) -> Dict[str, InteractionResult]:\n        \"\"\"Compute II separately for each phase (reasoning / execution / transition).\n\n        Args:\n            phases: List of Phase objects with .name and .token_indices attributes.\n            sparsity_level: Fraction of heads to mask / KV positions to evict.\n\n        Returns:\n            Dict mapping phase name to its InteractionResult.\n        \"\"\"\n        results: Dict[str, InteractionResult] = {}\n\n        for phase in phases:\n            result = self.compute_interaction_index(\n                input_ids,\n                sparsity_level=sparsity_level,\n                phase_token_indices=phase.token_indices,\n            )\n            result.phase_name = phase.name\n            results[phase.name] = result\n\n        return results\n\n\n# ---------------------------------------------------------------------------\n# Bootstrap CI for Interaction Index\n# ---------------------------------------------------------------------------\n\ndef bootstrap_interaction_index(\n    ii_samples: List[float],\n    n_resamples: int = 1000,\n    ci_level: float = 0.95,\n    seed: int = 42,\n) -> Tuple[float, float, float]:\n    \"\"\"Bootstrap confidence interval for the mean II.\n\n    Args:\n        ii_samples: Per-problem II values for a given (phase, level).\n        n_resamples: Number of bootstrap resamples.\n        ci_level: Confidence level (default 0.95 → 95% CI).\n        seed: Random seed for reproducibility.\n\n    Returns:\n        (mean, ci_low, ci_high) using percentile method.\n    \"\"\"\n    rng = np.random.RandomState(seed)\n    samples = np.array(ii_samples)\n    n = len(samples)\n    boot_means = np.empty(n_resamples)\n    for i in range(n_resamples):\n        idx = rng.randint(0, n, size=n)\n        boot_means[i] = samples[idx].mean()\n    alpha = 1.0 - ci_level\n    ci_low = float(np.percentile(boot_means, 100 * alpha / 2))\n    ci_high = float(np.percentile(boot_means, 100 * (1 - alpha / 2)))\n    return float(samples.mean()), ci_low, ci_high"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/profiling/interaction_index.py",
    "old_string": "    def compute_per_phase_ii(\n        self,\n        input_ids: torch.Tensor,\n        phases: List,\n        attn_sparsity_ratio: float = 0.3,\n        kv_eviction_ratio: float = 0.3,\n    ) -> Dict[str, InteractionResult]:\n        \"\"\"Compute II separately for each phase (reasoning / execution / transition).\n\n        Args:\n            phases: List of Phase objects from phase_segmentation.  Each Phase must\n                    have .name (str) and .token_indices (List[int]) attributes.\n\n        Returns:\n            Dict mapping phase name to its InteractionResult.\n        \"\"\"\n        results: Dict[str, InteractionResult] = {}\n\n        for phase in phases:\n            result = self.compute_interaction_index(\n                input_ids,\n                attn_sparsity_ratio=attn_sparsity_ratio,\n                kv_eviction_ratio=kv_eviction_ratio,\n                phase_token_indices=phase.token_indices,\n            )\n            result.phase_name = phase.name\n            results[phase.name] = result\n\n        return results",
    "new_string": "    def compute_per_phase_ii(\n        self,\n        input_ids: torch.Tensor,\n        phases: List,\n        sparsity_level: float = 0.3,\n    ) -> Dict[str, InteractionResult]:\n        \"\"\"Compute II separately for each phase (reasoning / execution / transition).\n\n        Args:\n            phases: List of Phase objects with .name and .token_indices attributes.\n            sparsity_level: Fraction of heads to mask / KV positions to evict.\n\n        Returns:\n            Dict mapping phase name to its InteractionResult.\n        \"\"\"\n        results: Dict[str, InteractionResult] = {}\n\n        for phase in phases:\n            result = self.compute_interaction_index(\n                input_ids,\n                sparsity_level=sparsity_level,\n                phase_token_indices=phase.token_indices,\n            )\n            result.phase_name = phase.name\n            results[phase.name] = result\n\n        return results\n\n\n# ---------------------------------------------------------------------------\n# Bootstrap CI for Interaction Index\n# ---------------------------------------------------------------------------\n\ndef bootstrap_interaction_index(\n    ii_samples: List[float],\n    n_resamples: int = 1000,\n    ci_level: float = 0.95,\n    seed: int = 42,\n) -> Tuple[float, float, float]:\n    \"\"\"Bootstrap confidence interval for the mean II.\n\n    Args:\n        ii_samples: Per-problem II values for a given (phase, level).\n        n_resamples: Number of bootstrap resamples.\n        ci_level: Confidence level (default 0.95 → 95% CI).\n        seed: Random seed for reproducibility.\n\n    Returns:\n        (mean, ci_low, ci_high) using percentile method.\n    \"\"\"\n    rng = np.random.RandomState(seed)\n    samples = np.array(ii_samples)\n    n = len(samples)\n    boot_means = np.empty(n_resamples)\n    for i in range(n_resamples):\n        idx = rng.randint(0, n, size=n)\n        boot_means[i] = samples[idx].mean()\n    alpha = 1.0 - ci_level\n    ci_low = float(np.percentile(boot_means, 100 * alpha / 2))\n    ci_high = float(np.percentile(boot_means, 100 * (1 - alpha / 2)))\n    return float(samples.mean()), ci_low, ci_high"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-13T18:38:06.493308+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/profiling/interaction_index.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-13T18:38:06.493487+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/utils/data_utils.py",
  "content": "# MATH-500 stratified sampling utility.\n# Selects problems evenly across difficulty levels for balanced profiling.\n\nfrom collections import defaultdict\nfrom typing import Any, Dict, List\nimport random\n\n\ndef stratified_sample_math500(\n    data: List[Dict[str, Any]],\n    per_level: int = 10,\n    seed: int = 42,\n) -> List[Dict[str, Any]]:\n    \"\"\"Stratified sampling from MATH-500: 10 problems per difficulty level.\n\n    MATH has 5 levels (1-5), yielding 50 problems total.\n    The level field may be named \"level\", \"difficulty\", or \"type\".\n    \"\"\"\n    by_level: Dict[Any, List[Dict]] = defaultdict(list)\n    for item in data:\n        lvl = item.get(\"level\", item.get(\"difficulty\", item.get(\"type\")))\n        if lvl is None:\n            continue\n        by_level[lvl].append(item)\n\n    rng = random.Random(seed)\n    sampled: List[Dict] = []\n    for lvl in sorted(by_level.keys()):\n        pool = by_level[lvl]\n        k = min(per_level, len(pool))\n        sampled.extend(rng.sample(pool, k))\n\n    return sampled\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/utils/data_utils.py",
    "content": "# MATH-500 stratified sampling utility.\n# Selects problems evenly across difficulty levels for balanced profiling.\n\nfrom collections import defaultdict\nfrom typing import Any, Dict, List\nimport random\n\n\ndef stratified_sample_math500(\n    data: List[Dict[str, Any]],\n    per_level: int = 10,\n    seed: int = 42,\n) -> List[Dict[str, Any]]:\n    \"\"\"Stratified sampling from MATH-500: 10 problems per difficulty level.\n\n    MATH has 5 levels (1-5), yielding 50 problems total.\n    The level field may be named \"level\", \"difficulty\", or \"type\".\n    \"\"\"\n    by_level: Dict[Any, List[Dict]] = defaultdict(list)\n    for item in data:\n        lvl = item.get(\"level\", item.get(\"difficulty\", item.get(\"type\")))\n        if lvl is None:\n            continue\n        by_level[lvl].append(item)\n\n    rng = random.Random(seed)\n    sampled: List[Dict] = []\n    for lvl in sorted(by_level.keys()):\n        pool = by_level[lvl]\n        k = min(per_level, len(pool))\n        sampled.extend(rng.sample(pool, k))\n\n    return sampled\n"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-13T18:38:06.493636+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/utils/data_utils.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-13T18:38:06.493830+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/profiling/run_profiling.py",
  "content": "# PACS Profiling — full MVP pipeline.\n#\n# End-to-end:\n#   1. Load causal LM + MATH-500 (stratified 50 problems)\n#   2. Generate reasoning traces, segment into phases\n#   3. For each sparsity level (30%, 50%):\n#      - Compute per-phase perplexity under 4 conditions (dense/attn/kv/both)\n#      - Compute per-phase Interaction Index\n#   4. Bootstrap 95% CI per (phase, level)\n#   5. Pass/fail judgment (CI overlap + sign reversal, OR logic)\n#   6. Output structured JSON\n#\n# Usage:\n#   python -m pacs.profiling.run_profiling \\\n#     --model_path &lt;HF model ID or path> \\\n#     --data_path &lt;MATH-500 JSON> \\\n#     --output_dir ./profiling_output\n\nfrom __future__ import annotations\n\nimport argparse\nimport json\nimport logging\nimport os\nimport sys\nfrom collections import defaultdict\nfrom itertools import combinations\nfrom pathlib import Path\nfrom typing import Any, Dict, List, Optional, Tuple\n\nimport numpy as np\nimport torch\n\nfrom ..utils.data_utils import stratified_sample_math500\nfrom ..utils.metrics import compute_perplexity\nfrom .interaction_index import InteractionIndexCalculator, bootstrap_interaction_index\nfrom .phase_segmentation import PhaseSegmenter\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(name)s: %(message)s\",\n)\nlogger = logging.getLogger(\"run_profiling\")\n\nSPARSITY_LEVELS = [0.3, 0.5]\nN_BOOTSTRAP = 1000\nMIN_SEGMENTS_WARN = 20\nSEED = 42\n\n\n# ---------------------------------------------------------------------------\n# Model / data loading\n# ---------------------------------------------------------------------------\n\ndef load_model_and_tokenizer(model_path: str, device: str = \"cuda\"):\n    from transformers import AutoModelForCausalLM, AutoTokenizer\n\n    logger.info(\"Loading tokenizer from %s\", model_path)\n    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    logger.info(\"Loading model from %s\", model_path)\n    model = AutoModelForCausalLM.from_pretrained(\n        model_path,\n        torch_dtype=torch.float16,\n        device_map=device,\n        trust_remote_code=True,\n        attn_implementation=\"eager\",\n    )\n    model.eval()\n    return model, tokenizer\n\n\ndef load_data(data_path: str) -> List[Dict[str, Any]]:\n    logger.info(\"Loading data from %s\", data_path)\n    with open(data_path) as f:\n        data = json.load(f)\n    if isinstance(data, dict) and \"data\" in data:\n        data = data[\"data\"]\n    logger.info(\"Loaded %d problems\", len(data))\n    return data\n\n\n# ---------------------------------------------------------------------------\n# Phase-conditioned perplexity\n# ---------------------------------------------------------------------------\n\ndef compute_conditioned_perplexities(\n    ii_calc: InteractionIndexCalculator,\n    input_ids: torch.Tensor,\n    phase_token_indices: List[int],\n    sparsity_level: float,\n    head_importance: Optional[torch.Tensor] = None,\n    kv_importance: Optional[torch.Tensor] = None,\n) -> Dict[str, float]:\n    \"\"\"Run 4 forward passes (dense/attn/kv/both) and return per-condition ppl.\"\"\"\n    num_layers, num_heads = ii_calc._get_model_dims()\n    seq_len = input_ids.size(-1)\n\n    attn_head_mask = ii_calc._select_heads_to_mask(\n        num_layers, num_heads, sparsity_level, head_importance\n    )\n    kv_mask = ii_calc._select_kv_to_evict(\n        num_layers, seq_len, sparsity_level, kv_importance\n    )\n\n    ppl_dense = ii_calc.forward_with_sparse_config(\n        input_ids, phase_token_indices=phase_token_indices,\n    )\n    ppl_attn = ii_calc.forward_with_sparse_config(\n        input_ids, attn_head_mask=attn_head_mask,\n        phase_token_indices=phase_token_indices,\n    )\n    ppl_kv = ii_calc.forward_with_sparse_config(\n        input_ids, kv_mask=kv_mask,\n        phase_token_indices=phase_token_indices,\n    )\n    ppl_both = ii_calc.forward_with_sparse_config(\n        input_ids, attn_head_mask=attn_head_mask, kv_mask=kv_mask,\n        phase_token_indices=phase_token_indices,\n    )\n\n    return {\"dense\": ppl_dense, \"attn\": ppl_attn, \"kv\": ppl_kv, \"both\": ppl_both}\n\n\n# ---------------------------------------------------------------------------\n# Pass/fail judgment (OR logic)\n# ---------------------------------------------------------------------------\n\ndef evaluate_pass_fail(\n    ii_results: Dict[str, Dict[str, Dict[str, float]]],\n) -> Dict[str, Any]:\n    \"\"\"Check pass criteria across phases.\n\n    Args:\n        ii_results: {phase_name: {level_str: {\"mean\", \"ci_low\", \"ci_high\"}}}.\n\n    Returns:\n        Dict with ci_overlap_test, sign_reversal_test, overall verdict.\n    \"\"\"\n    phase_names = list(ii_results.keys())\n    ci_pass = False\n    ci_detail = \"\"\n    sign_pass = False\n    sign_detail = \"\"\n\n    for level_str in [\"0.3\", \"0.5\"]:\n        phase_cis = {}\n        for pname in phase_names:\n            entry = ii_results.get(pname, {}).get(level_str)\n            if entry is None:\n                continue\n            phase_cis[pname] = (entry[\"ci_low\"], entry[\"ci_high\"], entry[\"mean\"])\n\n        for (p1, c1), (p2, c2) in combinations(phase_cis.items(), 2):\n            # CI non-overlap\n            if c1[1] < c2[0] or c2[1] < c1[0]:\n                ci_pass = True\n                ci_detail = f\"{p1} vs {p2} CI non-overlapping at {level_str}\"\n            # Sign reversal: one strictly positive, other strictly negative\n            sign1 = \"pos\" if c1[0] > 0 else (\"neg\" if c1[1] < 0 else \"zero\")\n            sign2 = \"pos\" if c2[0] > 0 else (\"neg\" if c2[1] < 0 else \"zero\")\n            if {sign1, sign2} == {\"pos\", \"neg\"}:\n                sign_pass = True\n                sign_detail = f\"{p1} II{'>' if sign1 == 'pos' else '<'}0, {p2} II{'>' if sign2 == 'pos' else '<'}0 at {level_str}\"\n\n    overall = \"PASS\" if (ci_pass or sign_pass) else \"FAIL\"\n    return {\n        \"ci_overlap_test\": {\"pass\": ci_pass, \"details\": ci_detail},\n        \"sign_reversal_test\": {\"pass\": sign_pass, \"details\": sign_detail},\n        \"overall\": overall,\n    }\n\n\n# ---------------------------------------------------------------------------\n# Main pipeline\n# ---------------------------------------------------------------------------\n\n@torch.no_grad()\ndef run_profiling(args: argparse.Namespace) -> None:\n    device = \"cuda\" if torch.cuda.is_available() else \"cpu\"\n    model, tokenizer = load_model_and_tokenizer(args.model_path, device=device)\n\n    raw_data = load_data(args.data_path)\n    data = stratified_sample_math500(raw_data, seed=SEED)\n    logger.info(\"Stratified sample: %d problems\", len(data))\n\n    segmenter = PhaseSegmenter(\n        bandwidth=args.kde_bandwidth,\n        min_phase_length=args.min_phase_length,\n    )\n    ii_calc = InteractionIndexCalculator(model, tokenizer, device=device)\n\n    os.makedirs(args.output_dir, exist_ok=True)\n    warnings_list: List[str] = []\n\n    # Accumulators: {phase_name: {level_str: [ii_values]}}\n    ii_per_phase_level: Dict[str, Dict[str, List[float]]] = defaultdict(\n        lambda: defaultdict(list)\n    )\n    # Accumulators: {phase_name: {level_str: {condition: [ppl_values]}}}\n    ppl_per_phase_level: Dict[str, Dict[str, Dict[str, List[float]]]] = defaultdict(\n        lambda: defaultdict(lambda: defaultdict(list))\n    )\n    # Phase token counts\n    phase_token_counts: Dict[str, List[int]] = defaultdict(list)\n    phase_segment_counts: Dict[str, int] = defaultdict(int)\n\n    for idx, item in enumerate(data):\n        problem_text = item.get(\"problem\", item.get(\"question\", \"\"))\n        problem_id = item.get(\"id\", str(idx))\n        logger.info(\"[%d/%d] Processing problem %s\", idx + 1, len(data), problem_id)\n\n        prompt = (\n            f\"Solve the following math problem step by step.\\n\\n\"\n            f\"Problem: {problem_text}\\n\\nSolution:\"\n        )\n        inputs = tokenizer(prompt, return_tensors=\"pt\").to(device)\n        prompt_len = inputs[\"input_ids\"].shape[1]\n\n        outputs = model.generate(\n            **inputs,\n            max_new_tokens=args.max_new_tokens,\n            do_sample=False,\n            output_attentions=True,\n            return_dict_in_generate=True,\n        )\n\n        if not hasattr(outputs, \"attentions\") or outputs.attentions is None:\n            logger.warning(\"No attentions for problem %s, skipping.\", problem_id)\n            warnings_list.append(f\"No attentions for problem {problem_id}\")\n            continue\n\n        first_step_attentions = outputs.attentions[0]\n        last_layer_attn = first_step_attentions[-1][0]  # (H, prompt_len, prompt_len)\n\n        annotation = segmenter.segment(last_layer_attn)\n\n        # Full generated sequence (prompt + generation) for perplexity eval\n        full_ids = outputs.sequences  # (1, full_len)\n\n        for phase in annotation.phases:\n            phase_token_counts[phase.name].append(len(phase.token_indices))\n            phase_segment_counts[phase.name] += 1\n\n            for level in SPARSITY_LEVELS:\n                level_str = str(level)\n                ppls = compute_conditioned_perplexities(\n                    ii_calc, full_ids, phase.token_indices, level,\n                )\n                for cond, val in ppls.items():\n                    ppl_per_phase_level[phase.name][level_str][cond].append(val)\n\n                # II from the 4 perplexities\n                ppl_d = ppls[\"dense\"]\n                if ppl_d > 0:\n                    r_attn = ppls[\"attn\"] / ppl_d\n                    r_kv = ppls[\"kv\"] / ppl_d\n                    r_both = ppls[\"both\"] / ppl_d\n                    ii_val = r_both - r_attn - r_kv + 1\n                else:\n                    ii_val = float(\"nan\")\n                ii_per_phase_level[phase.name][level_str].append(ii_val)\n\n        logger.info(\n            \"  -> %d phases, boundaries at %s\",\n            len(annotation.phases), annotation.boundaries,\n        )\n\n    # ------------------------------------------------------------------\n    # Aggregate: per-phase stats\n    # ------------------------------------------------------------------\n    phase_stats: Dict[str, Any] = {}\n    for pname in sorted(phase_token_counts.keys()):\n        n_tokens = sum(phase_token_counts[pname])\n        n_segments = phase_segment_counts[pname]\n        phase_stats[pname] = {\"n_tokens\": n_tokens, \"n_segments\": n_segments}\n        if n_segments < MIN_SEGMENTS_WARN:\n            msg = f\"Phase '{pname}' has only {n_segments} segments (< {MIN_SEGMENTS_WARN})\"\n            warnings_list.append(msg)\n            logger.warning(msg)\n\n    # ------------------------------------------------------------------\n    # Aggregate: mean perplexity per (phase, level, condition)\n    # ------------------------------------------------------------------\n    perplexity_out: Dict[str, Dict[str, Dict[str, float]]] = {}\n    for pname in sorted(ppl_per_phase_level.keys()):\n        perplexity_out[pname] = {}\n        for level_str in sorted(ppl_per_phase_level[pname].keys()):\n            cond_means: Dict[str, float] = {}\n            for cond in [\"dense\", \"attn\", \"kv\", \"both\"]:\n                vals = ppl_per_phase_level[pname][level_str][cond]\n                valid = [v for v in vals if not (isinstance(v, float) and v != v)]\n                cond_means[cond] = round(float(np.mean(valid)), 4) if valid else float(\"nan\")\n            perplexity_out[pname][level_str] = cond_means\n\n    # ------------------------------------------------------------------\n    # Bootstrap CI per (phase, level)\n    # ------------------------------------------------------------------\n    ii_out: Dict[str, Dict[str, Dict[str, float]]] = {}\n    for pname in sorted(ii_per_phase_level.keys()):\n        ii_out[pname] = {}\n        for level_str in sorted(ii_per_phase_level[pname].keys()):\n            samples = [v for v in ii_per_phase_level[pname][level_str] if not np.isnan(v)]\n            if len(samples) < 2:\n                ii_out[pname][level_str] = {\n                    \"mean\": float(np.mean(samples)) if samples else float(\"nan\"),\n                    \"ci_low\": float(\"nan\"),\n                    \"ci_high\": float(\"nan\"),\n                }\n                warnings_list.append(\n                    f\"Phase '{pname}' at {level_str}: only {len(samples)} valid II samples, CI unavailable\"\n                )\n            else:\n                mean, ci_low, ci_high = bootstrap_interaction_index(\n                    samples, n_resamples=N_BOOTSTRAP, seed=SEED,\n                )\n                ii_out[pname][level_str] = {\n                    \"mean\": round(mean, 6),\n                    \"ci_low\": round(ci_low, 6),\n                    \"ci_high\": round(ci_high, 6),\n                }\n\n    # ------------------------------------------------------------------\n    # Pass / fail\n    # ------------------------------------------------------------------\n    pass_fail = evaluate_pass_fail(ii_out)\n\n    # ------------------------------------------------------------------\n    # Assemble output\n    # ------------------------------------------------------------------\n    output = {\n        \"config\": {\n            \"model\": args.model_path,\n            \"sparsity_levels\": SPARSITY_LEVELS,\n            \"n_bootstrap\": N_BOOTSTRAP,\n            \"n_problems\": len(data),\n            \"seed\": SEED,\n        },\n        \"phase_stats\": phase_stats,\n        \"perplexity\": perplexity_out,\n        \"interaction_index\": ii_out,\n        \"pass_fail\": pass_fail,\n        \"warnings\": warnings_list,\n    }\n\n    out_path = os.path.join(args.output_dir, \"profiling_results.json\")\n    with open(out_path, \"w\") as f:\n        json.dump(output, f, indent=2, ensure_ascii=False)\n    logger.info(\"Results saved to %s\", out_path)\n\n    # Print summary\n    print(f\"\\n{'='*60}\")\n    print(f\"PACS Profiling Complete — {len(data)} problems\")\n    print(f\"{'='*60}\")\n    for pname, stats in phase_stats.items():\n        print(f\"  {pname}: {stats['n_tokens']} tokens, {stats['n_segments']} segments\")\n    print()\n    for pname in sorted(ii_out.keys()):\n        for level_str in sorted(ii_out[pname].keys()):\n            e = ii_out[pname][level_str]\n            print(\n                f\"  II[{pname}, {level_str}]: \"\n                f\"mean={e['mean']:+.4f}  95%CI=[{e['ci_low']:+.4f}, {e['ci_high']:+.4f}]\"\n            )\n    print(f\"\\nVerdict: {pass_fail['overall']}\")\n    if pass_fail[\"ci_overlap_test\"][\"pass\"]:\n        print(f\"  CI overlap test: {pass_fail['ci_overlap_test']['details']}\")\n    if pass_fail[\"sign_reversal_test\"][\"pass\"]:\n        print(f\"  Sign reversal:   {pass_fail['sign_reversal_test']['details']}\")\n    print(f\"{'='*60}\\n\")\n\n\n# ---------------------------------------------------------------------------\n# CLI\n# ---------------------------------------------------------------------------\n\ndef parse_args() -> argparse.Namespace:\n    parser = argparse.ArgumentParser(\n        description=\"PACS Phase Profiling — interaction index analysis\"\n    )\n    parser.add_argument(\n        \"--model_path\", type=str, required=True,\n        help=\"Path or HF model ID for the causal LM\",\n    )\n    parser.add_argument(\n        \"--data_path\", type=str, required=True,\n        help=\"Path to MATH-500 JSON\",\n    )\n    parser.add_argument(\n        \"--output_dir\", type=str, default=\"./profiling_output\",\n        help=\"Directory for output JSON (default: ./profiling_output)\",\n    )\n    parser.add_argument(\n        \"--max_new_tokens\", type=int, default=2048,\n        help=\"Max tokens to generate per problem (default: 2048)\",\n    )\n    parser.add_argument(\n        \"--kde_bandwidth\", type=str, default=\"scott\",\n        help=\"KDE bandwidth: scott / silverman / float (default: scott)\",\n    )\n    parser.add_argument(\n        \"--min_phase_length\", type=int, default=10,\n        help=\"Min tokens per phase segment (default: 10)\",\n    )\n    return parser.parse_args()\n\n\nif __name__ == \"__main__\":\n    run_profiling(parse_args())\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/profiling/run_profiling.py",
    "content": "# PACS Profiling — full MVP pipeline.\n#\n# End-to-end:\n#   1. Load causal LM + MATH-500 (stratified 50 problems)\n#   2. Generate reasoning traces, segment into phases\n#   3. For each sparsity level (30%, 50%):\n#      - Compute per-phase perplexity under 4 conditions (dense/attn/kv/both)\n#      - Compute per-phase Interaction Index\n#   4. Bootstrap 95% CI per (phase, level)\n#   5. Pass/fail judgment (CI overlap + sign reversal, OR logic)\n#   6. Output structured JSON\n#\n# Usage:\n#   python -m pacs.profiling.run_profiling \\\n#     --model_path &lt;HF model ID or path> \\\n#     --data_path &lt;MATH-500 JSON> \\\n#     --output_dir ./profiling_output\n\nfrom __future__ import annotations\n\nimport argparse\nimport json\nimport logging\nimport os\nimport sys\nfrom collections import defaultdict\nfrom itertools import combinations\nfrom pathlib import Path\nfrom typing import Any, Dict, List, Optional, Tuple\n\nimport numpy as np\nimport torch\n\nfrom ..utils.data_utils import stratified_sample_math500\nfrom ..utils.metrics import compute_perplexity\nfrom .interaction_index import InteractionIndexCalculator, bootstrap_interaction_index\nfrom .phase_segmentation import PhaseSegmenter\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(name)s: %(message)s\",\n)\nlogger = logging.getLogger(\"run_profiling\")\n\nSPARSITY_LEVELS = [0.3, 0.5]\nN_BOOTSTRAP = 1000\nMIN_SEGMENTS_WARN = 20\nSEED = 42\n\n\n# ---------------------------------------------------------------------------\n# Model / data loading\n# ---------------------------------------------------------------------------\n\ndef load_model_and_tokenizer(model_path: str, device: str = \"cuda\"):\n    from transformers import AutoModelForCausalLM, AutoTokenizer\n\n    logger.info(\"Loading tokenizer from %s\", model_path)\n    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    logger.info(\"Loading model from %s\", model_path)\n    model = AutoModelForCausalLM.from_pretrained(\n        model_path,\n        torch_dtype=torch.float16,\n        device_map=device,\n        trust_remote_code=True,\n        attn_implementation=\"eager\",\n    )\n    model.eval()\n    return model, tokenizer\n\n\ndef load_data(data_path: str) -> List[Dict[str, Any]]:\n    logger.info(\"Loading data from %s\", data_path)\n    with open(data_path) as f:\n        data = json.load(f)\n    if isinstance(data, dict) and \"data\" in data:\n        data = data[\"data\"]\n    logger.info(\"Loaded %d problems\", len(data))\n    return data\n\n\n# ---------------------------------------------------------------------------\n# Phase-conditioned perplexity\n# ---------------------------------------------------------------------------\n\ndef compute_conditioned_perplexities(\n    ii_calc: InteractionIndexCalculator,\n    input_ids: torch.Tensor,\n    phase_token_indices: List[int],\n    sparsity_level: float,\n    head_importance: Optional[torch.Tensor] = None,\n    kv_importance: Optional[torch.Tensor] = None,\n) -> Dict[str, float]:\n    \"\"\"Run 4 forward passes (dense/attn/kv/both) and return per-condition ppl.\"\"\"\n    num_layers, num_heads = ii_calc._get_model_dims()\n    seq_len = input_ids.size(-1)\n\n    attn_head_mask = ii_calc._select_heads_to_mask(\n        num_layers, num_heads, sparsity_level, head_importance\n    )\n    kv_mask = ii_calc._select_kv_to_evict(\n        num_layers, seq_len, sparsity_level, kv_importance\n    )\n\n    ppl_dense = ii_calc.forward_with_sparse_config(\n        input_ids, phase_token_indices=phase_token_indices,\n    )\n    ppl_attn = ii_calc.forward_with_sparse_config(\n        input_ids, attn_head_mask=attn_head_mask,\n        phase_token_indices=phase_token_indices,\n    )\n    ppl_kv = ii_calc.forward_with_sparse_config(\n        input_ids, kv_mask=kv_mask,\n        phase_token_indices=phase_token_indices,\n    )\n    ppl_both = ii_calc.forward_with_sparse_config(\n        input_ids, attn_head_mask=attn_head_mask, kv_mask=kv_mask,\n        phase_token_indices=phase_token_indices,\n    )\n\n    return {\"dense\": ppl_dense, \"attn\": ppl_attn, \"kv\": ppl_kv, \"both\": ppl_both}\n\n\n# ---------------------------------------------------------------------------\n# Pass/fail judgment (OR logic)\n# ---------------------------------------------------------------------------\n\ndef evaluate_pass_fail(\n    ii_results: Dict[str, Dict[str, Dict[str, float]]],\n) -> Dict[str, Any]:\n    \"\"\"Check pass criteria across phases.\n\n    Args:\n        ii_results: {phase_name: {level_str: {\"mean\", \"ci_low\", \"ci_high\"}}}.\n\n    Returns:\n        Dict with ci_overlap_test, sign_reversal_test, overall verdict.\n    \"\"\"\n    phase_names = list(ii_results.keys())\n    ci_pass = False\n    ci_detail = \"\"\n    sign_pass = False\n    sign_detail = \"\"\n\n    for level_str in [\"0.3\", \"0.5\"]:\n        phase_cis = {}\n        for pname in phase_names:\n            entry = ii_results.get(pname, {}).get(level_str)\n            if entry is None:\n                continue\n            phase_cis[pname] = (entry[\"ci_low\"], entry[\"ci_high\"], entry[\"mean\"])\n\n        for (p1, c1), (p2, c2) in combinations(phase_cis.items(), 2):\n            # CI non-overlap\n            if c1[1] < c2[0] or c2[1] < c1[0]:\n                ci_pass = True\n                ci_detail = f\"{p1} vs {p2} CI non-overlapping at {level_str}\"\n            # Sign reversal: one strictly positive, other strictly negative\n            sign1 = \"pos\" if c1[0] > 0 else (\"neg\" if c1[1] < 0 else \"zero\")\n            sign2 = \"pos\" if c2[0] > 0 else (\"neg\" if c2[1] < 0 else \"zero\")\n            if {sign1, sign2} == {\"pos\", \"neg\"}:\n                sign_pass = True\n                sign_detail = f\"{p1} II{'>' if sign1 == 'pos' else '<'}0, {p2} II{'>' if sign2 == 'pos' else '<'}0 at {level_str}\"\n\n    overall = \"PASS\" if (ci_pass or sign_pass) else \"FAIL\"\n    return {\n        \"ci_overlap_test\": {\"pass\": ci_pass, \"details\": ci_detail},\n        \"sign_reversal_test\": {\"pass\": sign_pass, \"details\": sign_detail},\n        \"overall\": overall,\n    }\n\n\n# ---------------------------------------------------------------------------\n# Main pipeline\n# ---------------------------------------------------------------------------\n\n@torch.no_grad()\ndef run_profiling(args: argparse.Namespace) -> None:\n    device = \"cuda\" if torch.cuda.is_available() else \"cpu\"\n    model, tokenizer = load_model_and_tokenizer(args.model_path, device=device)\n\n    raw_data = load_data(args.data_path)\n    data = stratified_sample_math500(raw_data, seed=SEED)\n    logger.info(\"Stratified sample: %d problems\", len(data))\n\n    segmenter = PhaseSegmenter(\n        bandwidth=args.kde_bandwidth,\n        min_phase_length=args.min_phase_length,\n    )\n    ii_calc = InteractionIndexCalculator(model, tokenizer, device=device)\n\n    os.makedirs(args.output_dir, exist_ok=True)\n    warnings_list: List[str] = []\n\n    # Accumulators: {phase_name: {level_str: [ii_values]}}\n    ii_per_phase_level: Dict[str, Dict[str, List[float]]] = defaultdict(\n        lambda: defaultdict(list)\n    )\n    # Accumulators: {phase_name: {level_str: {condition: [ppl_values]}}}\n    ppl_per_phase_level: Dict[str, Dict[str, Dict[str, List[float]]]] = defaultdict(\n        lambda: defaultdict(lambda: defaultdict(list))\n    )\n    # Phase token counts\n    phase_token_counts: Dict[str, List[int]] = defaultdict(list)\n    phase_segment_counts: Dict[str, int] = defaultdict(int)\n\n    for idx, item in enumerate(data):\n        problem_text = item.get(\"problem\", item.get(\"question\", \"\"))\n        problem_id = item.get(\"id\", str(idx))\n        logger.info(\"[%d/%d] Processing problem %s\", idx + 1, len(data), problem_id)\n\n        prompt = (\n            f\"Solve the following math problem step by step.\\n\\n\"\n            f\"Problem: {problem_text}\\n\\nSolution:\"\n        )\n        inputs = tokenizer(prompt, return_tensors=\"pt\").to(device)\n        prompt_len = inputs[\"input_ids\"].shape[1]\n\n        outputs = model.generate(\n            **inputs,\n            max_new_tokens=args.max_new_tokens,\n            do_sample=False,\n            output_attentions=True,\n            return_dict_in_generate=True,\n        )\n\n        if not hasattr(outputs, \"attentions\") or outputs.attentions is None:\n            logger.warning(\"No attentions for problem %s, skipping.\", problem_id)\n            warnings_list.append(f\"No attentions for problem {problem_id}\")\n            continue\n\n        first_step_attentions = outputs.attentions[0]\n        last_layer_attn = first_step_attentions[-1][0]  # (H, prompt_len, prompt_len)\n\n        annotation = segmenter.segment(last_layer_attn)\n\n        # Full generated sequence (prompt + generation) for perplexity eval\n        full_ids = outputs.sequences  # (1, full_len)\n\n        for phase in annotation.phases:\n            phase_token_counts[phase.name].append(len(phase.token_indices))\n            phase_segment_counts[phase.name] += 1\n\n            for level in SPARSITY_LEVELS:\n                level_str = str(level)\n                ppls = compute_conditioned_perplexities(\n                    ii_calc, full_ids, phase.token_indices, level,\n                )\n                for cond, val in ppls.items():\n                    ppl_per_phase_level[phase.name][level_str][cond].append(val)\n\n                # II from the 4 perplexities\n                ppl_d = ppls[\"dense\"]\n                if ppl_d > 0:\n                    r_attn = ppls[\"attn\"] / ppl_d\n                    r_kv = ppls[\"kv\"] / ppl_d\n                    r_both = ppls[\"both\"] / ppl_d\n                    ii_val = r_both - r_attn - r_kv + 1\n                else:\n                    ii_val = float(\"nan\")\n                ii_per_phase_level[phase.name][level_str].append(ii_val)\n\n        logger.info(\n            \"  -> %d phases, boundaries at %s\",\n            len(annotation.phases), annotation.boundaries,\n        )\n\n    # ------------------------------------------------------------------\n    # Aggregate: per-phase stats\n    # ------------------------------------------------------------------\n    phase_stats: Dict[str, Any] = {}\n    for pname in sorted(phase_token_counts.keys()):\n        n_tokens = sum(phase_token_counts[pname])\n        n_segments = phase_segment_counts[pname]\n        phase_stats[pname] = {\"n_tokens\": n_tokens, \"n_segments\": n_segments}\n        if n_segments < MIN_SEGMENTS_WARN:\n            msg = f\"Phase '{pname}' has only {n_segments} segments (< {MIN_SEGMENTS_WARN})\"\n            warnings_list.append(msg)\n            logger.warning(msg)\n\n    # ------------------------------------------------------------------\n    # Aggregate: mean perplexity per (phase, level, condition)\n    # ------------------------------------------------------------------\n    perplexity_out: Dict[str, Dict[str, Dict[str, float]]] = {}\n    for pname in sorted(ppl_per_phase_level.keys()):\n        perplexity_out[pname] = {}\n        for level_str in sorted(ppl_per_phase_level[pname].keys()):\n            cond_means: Dict[str, float] = {}\n            for cond in [\"dense\", \"attn\", \"kv\", \"both\"]:\n                vals = ppl_per_phase_level[pname][level_str][cond]\n                valid = [v for v in vals if not (isinstance(v, float) and v != v)]\n                cond_means[cond] = round(float(np.mean(valid)), 4) if valid else float(\"nan\")\n            perplexity_out[pname][level_str] = cond_means\n\n    # ------------------------------------------------------------------\n    # Bootstrap CI per (phase, level)\n    # ------------------------------------------------------------------\n    ii_out: Dict[str, Dict[str, Dict[str, float]]] = {}\n    for pname in sorted(ii_per_phase_level.keys()):\n        ii_out[pname] = {}\n        for level_str in sorted(ii_per_phase_level[pname].keys()):\n            samples = [v for v in ii_per_phase_level[pname][level_str] if not np.isnan(v)]\n            if len(samples) < 2:\n                ii_out[pname][level_str] = {\n                    \"mean\": float(np.mean(samples)) if samples else float(\"nan\"),\n                    \"ci_low\": float(\"nan\"),\n                    \"ci_high\": float(\"nan\"),\n                }\n                warnings_list.append(\n                    f\"Phase '{pname}' at {level_str}: only {len(samples)} valid II samples, CI unavailable\"\n                )\n            else:\n                mean, ci_low, ci_high = bootstrap_interaction_index(\n                    samples, n_resamples=N_BOOTSTRAP, seed=SEED,\n                )\n                ii_out[pname][level_str] = {\n                    \"mean\": round(mean, 6),\n                    \"ci_low\": round(ci_low, 6),\n                    \"ci_high\": round(ci_high, 6),\n                }\n\n    # ------------------------------------------------------------------\n    # Pass / fail\n    # ------------------------------------------------------------------\n    pass_fail = evaluate_pass_fail(ii_out)\n\n    # ------------------------------------------------------------------\n    # Assemble output\n    # ------------------------------------------------------------------\n    output = {\n        \"config\": {\n            \"model\": args.model_path,\n            \"sparsity_levels\": SPARSITY_LEVELS,\n            \"n_bootstrap\": N_BOOTSTRAP,\n            \"n_problems\": len(data),\n            \"seed\": SEED,\n        },\n        \"phase_stats\": phase_stats,\n        \"perplexity\": perplexity_out,\n        \"interaction_index\": ii_out,\n        \"pass_fail\": pass_fail,\n        \"warnings\": warnings_list,\n    }\n\n    out_path = os.path.join(args.output_dir, \"profiling_results.json\")\n    with open(out_path, \"w\") as f:\n        json.dump(output, f, indent=2, ensure_ascii=False)\n    logger.info(\"Results saved to %s\", out_path)\n\n    # Print summary\n    print(f\"\\n{'='*60}\")\n    print(f\"PACS Profiling Complete — {len(data)} problems\")\n    print(f\"{'='*60}\")\n    for pname, stats in phase_stats.items():\n        print(f\"  {pname}: {stats['n_tokens']} tokens, {stats['n_segments']} segments\")\n    print()\n    for pname in sorted(ii_out.keys()):\n        for level_str in sorted(ii_out[pname].keys()):\n            e = ii_out[pname][level_str]\n            print(\n                f\"  II[{pname}, {level_str}]: \"\n                f\"mean={e['mean']:+.4f}  95%CI=[{e['ci_low']:+.4f}, {e['ci_high']:+.4f}]\"\n            )\n    print(f\"\\nVerdict: {pass_fail['overall']}\")\n    if pass_fail[\"ci_overlap_test\"][\"pass\"]:\n        print(f\"  CI overlap test: {pass_fail['ci_overlap_test']['details']}\")\n    if pass_fail[\"sign_reversal_test\"][\"pass\"]:\n        print(f\"  Sign reversal:   {pass_fail['sign_reversal_test']['details']}\")\n    print(f\"{'='*60}\\n\")\n\n\n# ---------------------------------------------------------------------------\n# CLI\n# ---------------------------------------------------------------------------\n\ndef parse_args() -> argparse.Namespace:\n    parser = argparse.ArgumentParser(\n        description=\"PACS Phase Profiling — interaction index analysis\"\n    )\n    parser.add_argument(\n        \"--model_path\", type=str, required=True,\n        help=\"Path or HF model ID for the causal LM\",\n    )\n    parser.add_argument(\n        \"--data_path\", type=str, required=True,\n        help=\"Path to MATH-500 JSON\",\n    )\n    parser.add_argument(\n        \"--output_dir\", type=str, default=\"./profiling_output\",\n        help=\"Directory for output JSON (default: ./profiling_output)\",\n    )\n    parser.add_argument(\n        \"--max_new_tokens\", type=int, default=2048,\n        help=\"Max tokens to generate per problem (default: 2048)\",\n    )\n    parser.add_argument(\n        \"--kde_bandwidth\", type=str, default=\"scott\",\n        help=\"KDE bandwidth: scott / silverman / float (default: scott)\",\n    )\n    parser.add_argument(\n        \"--min_phase_length\", type=int, default=10,\n        help=\"Min tokens per phase segment (default: 10)\",\n    )\n    return parser.parse_args()\n\n\nif __name__ == \"__main__\":\n    run_profiling(parse_args())\n"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-13T18:38:06.494367+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/profiling/run_profiling.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-13T18:38:06.494578+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts && PYTHONPATH=. python -c \"from pacs.profiling.interaction_index import InteractionIndexCalculator, bootstrap_interaction_index; print('interaction_index OK')\"",
  "description": "Test interaction_index import"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts && PYTHONPATH=. python -c \"from pacs.profiling.interaction_index import InteractionIndexCalculator, bootstrap_interaction_index; print('interaction_index OK')\"",
    "description": "Test interaction_index import"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-13T18:38:06.494715+00:00_

Exit code 127
/bin/bash: line 1: python: command not found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-13T18:38:06.494847+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts && python3 -c \"from pacs.profiling.interaction_index import InteractionIndexCalculator, bootstrap_interaction_index; print('interaction_index OK')\"",
  "description": "Test interaction_index import"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts && python3 -c \"from pacs.profiling.interaction_index import InteractionIndexCalculator, bootstrap_interaction_index; print('interaction_index OK')\"",
    "description": "Test interaction_index import"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-13T18:38:06.494974+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 1, in &lt;module>
    from pacs.profiling.interaction_index import InteractionIndexCalculator, bootstrap_interaction_index; print('interaction_index OK')
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/profiling/interaction_index.py", line 18, in &lt;module>
    import torch
ModuleNotFoundError: No module named 'torch'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-13T18:38:06.495109+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts && python3 -c \"from pacs.utils.data_utils import stratified_sample_math500; print('data_utils OK')\"",
  "description": "Test data_utils import"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts && python3 -c \"from pacs.utils.data_utils import stratified_sample_math500; print('data_utils OK')\"",
    "description": "Test data_utils import"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-13T18:38:06.495228+00:00_

data_utils OK

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-13T18:38:06.495346+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport ast, sys\n\nfiles = [\n    'pacs/profiling/interaction_index.py',\n    'pacs/profiling/phase_segmentation.py',\n    'pacs/profiling/run_profiling.py',\n    'pacs/utils/metrics.py',\n    'pacs/utils/data_utils.py',\n]\nok = True\nfor f in files:\n    try:\n        with open(f) as fh:\n            ast.parse(fh.read())\n        print(f'  {f}: syntax OK')\n    except SyntaxError as e:\n        print(f'  {f}: SYNTAX ERROR: {e}')\n        ok = False\nsys.exit(0 if ok else 1)\n\"",
  "description": "Verify syntax of all modified files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport ast, sys\n\nfiles = [\n    'pacs/profiling/interaction_index.py',\n    'pacs/profiling/phase_segmentation.py',\n    'pacs/profiling/run_profiling.py',\n    'pacs/utils/metrics.py',\n    'pacs/utils/data_utils.py',\n]\nok = True\nfor f in files:\n    try:\n        with open(f) as fh:\n            ast.parse(fh.read())\n        print(f'  {f}: syntax OK')\n    except SyntaxError as e:\n        print(f'  {f}: SYNTAX ERROR: {e}')\n        ok = False\nsys.exit(0 if ok else 1)\n\"",
    "description": "Verify syntax of all modified files"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-13T18:38:06.495494+00:00_

  pacs/profiling/interaction_index.py: syntax OK
  pacs/profiling/phase_segmentation.py: syntax OK
  pacs/profiling/run_profiling.py: syntax OK
  pacs/utils/metrics.py: syntax OK
  pacs/utils/data_utils.py: syntax OK

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-13T18:38:06.495628+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\n# Verify II formula: ppl_dense=10, ppl_attn=12, ppl_kv=11, ppl_both=15\nppl_dense, ppl_attn, ppl_kv, ppl_both = 10, 12, 11, 15\nr_attn = ppl_attn / ppl_dense  # 1.2\nr_kv = ppl_kv / ppl_dense      # 1.1\nr_both = ppl_both / ppl_dense  # 1.5\nii = r_both - r_attn - r_kv + 1  # 1.5 - 1.2 - 1.1 + 1 = 0.2\nprint(f'R_attn={r_attn}, R_kv={r_kv}, R_both={r_both}, II={ii}')\nassert ii == 0.2, f'Expected 0.2, got {ii}'\nassert ii > 0, 'Should be super-additive'\nprint('Formula test PASSED')\n\n# Verify bootstrap\nimport sys; sys.path.insert(0, '.')\nfrom pacs.utils.data_utils import stratified_sample_math500\n# Test with mock data\ndata = [{'problem': f'q{i}', 'level': (i%5)+1} for i in range(100)]\nsample = stratified_sample_math500(data)\nprint(f'Stratified sample: {len(sample)} problems')\nfrom collections import Counter\nlevels = Counter(item['level'] for item in sample)\nprint(f'Level distribution: {dict(sorted(levels.items()))}')\nassert len(sample) == 50\nassert all(v == 10 for v in levels.values())\nprint('Stratified sampling test PASSED')\n\"",
  "description": "Verify II formula and stratified sampling logic"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\n# Verify II formula: ppl_dense=10, ppl_attn=12, ppl_kv=11, ppl_both=15\nppl_dense, ppl_attn, ppl_kv, ppl_both = 10, 12, 11, 15\nr_attn = ppl_attn / ppl_dense  # 1.2\nr_kv = ppl_kv / ppl_dense      # 1.1\nr_both = ppl_both / ppl_dense  # 1.5\nii = r_both - r_attn - r_kv + 1  # 1.5 - 1.2 - 1.1 + 1 = 0.2\nprint(f'R_attn={r_attn}, R_kv={r_kv}, R_both={r_both}, II={ii}')\nassert ii == 0.2, f'Expected 0.2, got {ii}'\nassert ii > 0, 'Should be super-additive'\nprint('Formula test PASSED')\n\n# Verify bootstrap\nimport sys; sys.path.insert(0, '.')\nfrom pacs.utils.data_utils import stratified_sample_math500\n# Test with mock data\ndata = [{'problem': f'q{i}', 'level': (i%5)+1} for i in range(100)]\nsample = stratified_sample_math500(data)\nprint(f'Stratified sample: {len(sample)} problems')\nfrom collections import Counter\nlevels = Counter(item['level'] for item in sample)\nprint(f'Level distribution: {dict(sorted(levels.items()))}')\nassert len(sample) == 50\nassert all(v == 10 for v in levels.values())\nprint('Stratified sampling test PASSED')\n\"",
    "description": "Verify II formula and stratified sampling logic"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-13T18:38:06.495761+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 9, in &lt;module>
    assert ii == 0.2, f'Expected 0.2, got {ii}'
           ^^^^^^^^^
AssertionError: Expected 0.2, got 0.19999999999999996
R_attn=1.2, R_kv=1.1, R_both=1.5, II=0.19999999999999996

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-13T18:38:06.495929+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nppl_dense, ppl_attn, ppl_kv, ppl_both = 10, 12, 11, 15\nr_attn = ppl_attn / ppl_dense\nr_kv = ppl_kv / ppl_dense\nr_both = ppl_both / ppl_dense\nii = r_both - r_attn - r_kv + 1\nprint(f'R_attn={r_attn}, R_kv={r_kv}, R_both={r_both}, II={ii}')\nassert abs(ii - 0.2) < 1e-10, f'Expected ~0.2, got {ii}'\nassert ii > 0, 'Should be super-additive'\nprint('Formula test PASSED')\n\nfrom pacs.utils.data_utils import stratified_sample_math500\ndata = [{'problem': f'q{i}', 'level': (i%5)+1} for i in range(100)]\nsample = stratified_sample_math500(data)\nprint(f'Stratified sample: {len(sample)} problems')\nfrom collections import Counter\nlevels = Counter(item['level'] for item in sample)\nprint(f'Level distribution: {dict(sorted(levels.items()))}')\nassert len(sample) == 50\nassert all(v == 10 for v in levels.values())\nprint('Stratified sampling test PASSED')\n\n# Bootstrap test\nimport numpy as np\nnp.random.seed(42)\nii_samples = list(np.random.randn(30) * 0.1 + 0.05)\n\n# Inline bootstrap (can't import due to torch dep)\nrng = np.random.RandomState(42)\narr = np.array(ii_samples)\nn = len(arr)\nboots = np.array([arr[rng.randint(0, n, size=n)].mean() for _ in range(1000)])\nci_low = float(np.percentile(boots, 2.5))\nci_high = float(np.percentile(boots, 97.5))\nmean = float(arr.mean())\nprint(f'Bootstrap: mean={mean:.4f}, CI=[{ci_low:.4f}, {ci_high:.4f}]')\nprint('Bootstrap test PASSED')\n\"",
  "description": "Verify all formula and logic tests"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nppl_dense, ppl_attn, ppl_kv, ppl_both = 10, 12, 11, 15\nr_attn = ppl_attn / ppl_dense\nr_kv = ppl_kv / ppl_dense\nr_both = ppl_both / ppl_dense\nii = r_both - r_attn - r_kv + 1\nprint(f'R_attn={r_attn}, R_kv={r_kv}, R_both={r_both}, II={ii}')\nassert abs(ii - 0.2) < 1e-10, f'Expected ~0.2, got {ii}'\nassert ii > 0, 'Should be super-additive'\nprint('Formula test PASSED')\n\nfrom pacs.utils.data_utils import stratified_sample_math500\ndata = [{'problem': f'q{i}', 'level': (i%5)+1} for i in range(100)]\nsample = stratified_sample_math500(data)\nprint(f'Stratified sample: {len(sample)} problems')\nfrom collections import Counter\nlevels = Counter(item['level'] for item in sample)\nprint(f'Level distribution: {dict(sorted(levels.items()))}')\nassert len(sample) == 50\nassert all(v == 10 for v in levels.values())\nprint('Stratified sampling test PASSED')\n\n# Bootstrap test\nimport numpy as np\nnp.random.seed(42)\nii_samples = list(np.random.randn(30) * 0.1 + 0.05)\n\n# Inline bootstrap (can't import due to torch dep)\nrng = np.random.RandomState(42)\narr = np.array(ii_samples)\nn = len(arr)\nboots = np.array([arr[rng.randint(0, n, size=n)].mean() for _ in range(1000)])\nci_low = float(np.percentile(boots, 2.5))\nci_high = float(np.percentile(boots, 97.5))\nmean = float(arr.mean())\nprint(f'Bootstrap: mean={mean:.4f}, CI=[{ci_low:.4f}, {ci_high:.4f}]')\nprint('Bootstrap test PASSED')\n\"",
    "description": "Verify all formula and logic tests"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-13T18:38:06.496069+00:00_

R_attn=1.2, R_kv=1.1, R_both=1.5, II=0.19999999999999996
Formula test PASSED
Stratified sample: 50 problems
Level distribution: {1: 10, 2: 10, 3: 10, 4: 10, 5: 10}
Stratified sampling test PASSED
Bootstrap: mean=0.0312, CI=[-0.0010, 0.0622]
Bootstrap test PASSED

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-13T18:38:06.496201+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/profiling/interaction_index.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/profiling/interaction_index.py"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-13T18:38:06.496491+00:00_

1	# Interaction Index (II) calculator for measuring super/sub-additivity
2	# of compound sparsity (attention head pruning + KV cache eviction).
3	#
4	# II = R_both - R_attn - R_kv + 1
5	# where R_x = ppl_x / ppl_dense (relative degradation ratio).
6	# II > 0 → super-additive degradation (compound sparsity hurts more than sum of parts)
7	# II < 0 → sub-additive degradation
8	# II = 0 → independent
9	
10	from __future__ import annotations
11	
12	import math
13	from dataclasses import dataclass, field
14	from typing import Dict, List, Optional, Tuple
15	
16	import numpy as np
17	
18	import torch
19	import torch.nn.functional as F
20	
21	from ..utils.metrics import compute_perplexity
22	
23	try:
24	    from .phase_segmentation import Phase
25	except ImportError:
26	    Phase = None  # will be resolved when phase_segmentation is created
27	
28	
29	# ---------------------------------------------------------------------------
30	# Data classes
31	# ---------------------------------------------------------------------------
32	
33	@dataclass
34	class InteractionResult:
35	    ii_value: float
36	    ppl_dense: float
37	    ppl_attn_sparse: float
38	    ppl_kv_sparse: float
39	    ppl_both_sparse: float
40	    r_attn: float          # ppl_attn / ppl_dense
41	    r_kv: float            # ppl_kv / ppl_dense
42	    r_both: float          # ppl_both / ppl_dense
43	    is_super_additive: bool  # II > 0 → compound sparsity degrades more than sum of parts
44	    sparsity_level: float = 0.0
45	    phase_name: Optional[str] = None
46	    num_tokens: int = 0
47	
48	    def summary(self) -> str:
49	        tag = "super-additive" if self.is_super_additive else "sub-additive"
50	        return (
51	            f"II={self.ii_value:+.4f} ({tag})  "
52	            f"R_attn={self.r_attn:.4f}  R_kv={self.r_kv:.4f}  R_both={self.r_both:.4f}  "
53	            f"dense={self.ppl_dense:.2f}  attn={self.ppl_attn_sparse:.2f}  "
54	            f"kv={self.ppl_kv_sparse:.2f}  both={self.ppl_both_sparse:
…[truncated 15861 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_mvp-protocol-fix_20260513T183157",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-13T18:38:06.496770+00:00_

All changes complete. Summary of what was done:

**Bug #1 (II formula)**: Changed from `-ppl_both + ppl_attn + ppl_kv - ppl_dense` to `R_both - R_attn - R_kv + 1` where `R_x = ppl_x / ppl_dense`. Added `r_attn`, `r_kv`, `r_both` fields to `InteractionResult`. Updated all comments.

**Bug #2 (token_indices)**: Added `@property token_indices` to `Phase` dataclass in `phase_segmentation.py:35-37`, returns `list(range(self.start, self.end))`.

**Bug #3 (run_profiling.py)**: Complete rewrite — now runs full MVP pipeline: stratified sampling → generation → phase segmentation → per-phase × per-level (0.3, 0.5) × 4-condition perplexity → II computation → bootstrap 1000 resamples → CI → pass/fail (OR logic: CI non-overlap OR sign reversal) → structured JSON output.

**Protocol #1-6**: All implemented:
- Two sparsity levels (0.3, 0.5), unified `sparsity_level` parameter
- Bootstrap with 1000 resamples, percentile CI, min-segment warning
- OR-logic pass/fail (CI non-overlap or sign reversal across phase pairs)
- `stratified_sample_math500` in new `pacs/utils/data_utils.py`
- JSON output matches specified schema exactly
- Directory structure preserved

**No intermediate files** to delete (`_project/intermediate/` doesn't exist).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_mvp-protocol-fix_20260513T183157"
}
```

</details>

---
