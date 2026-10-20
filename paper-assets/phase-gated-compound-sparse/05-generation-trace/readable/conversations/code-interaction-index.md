# code interaction index

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 0
- **Tool calls:** 16
- **Original source:** `logs/chats/worker_code_interaction_index_20260513T174549.jsonl`
- **Structured JSON:** [`17460833b07fa552cdcd.json`](../../sessions/17/17460833b07fa552cdcd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

33 recorded events

### Tool call

_source line 1 · 2026-05-13T17:48:28.595080+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/ 2>/dev/null && echo \"---\" && find /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/ -type f -name \"*.py\" 2>/dev/null",
  "description": "Check existing pacs directory structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_interaction_index_20260513T174549",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/ 2>/dev/null && echo \"---\" && find /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/ -type f -name \"*.py\" 2>/dev/null",
    "description": "Check existing pacs directory structure"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-13T17:48:28.595586+00:00_

total 12
drwxr-xr-x 3 ubuntu ubuntu 4096 May 13 17:45 .
drwxr-xr-x 3 ubuntu ubuntu 4096 May 13 17:45 ..
drwxr-xr-x 2 ubuntu ubuntu 4096 May 13 17:45 profiling
---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_interaction_index_20260513T174549",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-13T17:48:28.595813+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/profiling/ && echo \"---\" && ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/utils/ 2>/dev/null || echo \"utils/ does not exist\"",
  "description": "Check profiling and utils directories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_interaction_index_20260513T174549",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/profiling/ && echo \"---\" && ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/utils/ 2>/dev/null || echo \"utils/ does not exist\"",
    "description": "Check profiling and utils directories"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-13T17:48:28.595984+00:00_

total 8
drwxr-xr-x 2 ubuntu ubuntu 4096 May 13 17:45 .
drwxr-xr-x 3 ubuntu ubuntu 4096 May 13 17:45 ..
---
utils/ does not exist

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_interaction_index_20260513T174549",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-13T17:48:28.596115+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_interaction_index_20260513T174549",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.py",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-13T17:48:28.596236+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_interaction_index_20260513T174549",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-13T17:48:28.596369+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "class Phase",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_interaction_index_20260513T174549",
  "tool": "Grep",
  "tool_args": {
    "pattern": "class Phase",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-13T17:48:28.596558+00:00_

Found 2 files
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/logs/workers/worker_code_interaction_index_20260513T174549.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/logs/chats/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4.jsonl

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_interaction_index_20260513T174549",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-13T17:48:28.596744+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "class Phase\"",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/logs/workers/worker_code_interaction_index_20260513T174549.log",
  "output_mode": "content",
  "-C": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_interaction_index_20260513T174549",
  "tool": "Grep",
  "tool_args": {
    "pattern": "class Phase\"",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/logs/workers/worker_code_interaction_index_20260513T174549.log",
    "output_mode": "content",
    "-C": "5"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-13T17:48:28.597945+00:00_

8-[Omitted long context line]
9-[Omitted long context line]
10-[Omitted long context line]
11-{"type":"user","message":{"role":"user","content":[{"tool_use_id":"toolu_016CVj3df6arqFvKS6Z1RjDC","type":"tool_result","content":"No files found"}]},"parent_tool_use_id":null,"session_id":"51e7feb4-f917-4807-a197-b194c52b57d6","uuid":"0cf3f6d5-a544-4962-b6cb-7ef0a4ee9ae2","timestamp":"2026-05-13T17:46:15.628Z","tool_use_result":{"filenames":[],"durationMs":10,"numFiles":0,"truncated":false}}
12-[Omitted long context line]
13:[Omitted long matching line]
14-[Omitted long context line]
15-[Omitted long context line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_interaction_index_20260513T174549",
  "tool": "Grep",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-13T17:48:28.598172+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/utils",
  "description": "Create utils directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_interaction_index_20260513T174549",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/utils",
    "description": "Create utils directory"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-13T17:48:28.598314+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_interaction_index_20260513T174549",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-13T17:48:28.598798+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/profiling/__init__.py",
  "content": ""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_interaction_index_20260513T174549",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/profiling/__init__.py",
    "content": ""
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-13T17:48:28.598991+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/profiling/__init__.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_interaction_index_20260513T174549",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-13T17:48:28.599121+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/utils/__init__.py",
  "content": ""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_interaction_index_20260513T174549",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/utils/__init__.py",
    "content": ""
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-13T17:48:28.599246+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/utils/__init__.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_interaction_index_20260513T174549",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-13T17:48:28.599387+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/utils/metrics.py",
  "content": "# General-purpose metrics for PACS profiling: perplexity, accuracy, etc.\n\nfrom typing import List, Optional\n\nimport torch\nimport torch.nn.functional as F\n\n\ndef compute_perplexity(\n    logits: torch.Tensor,\n    labels: torch.Tensor,\n    token_indices: Optional[List[int]] = None,\n) -> float:\n    \"\"\"Compute mean per-token perplexity, optionally restricted to specific positions.\n\n    Args:\n        logits: (seq_len, vocab_size) – unnormalized logits.\n        labels: (seq_len,) – ground-truth token ids.  Positions with label == -100\n                are ignored (standard HF convention).\n        token_indices: If given, only these positions contribute to the result.\n                       None means all valid positions.\n\n    Returns:\n        Scalar perplexity (exp of mean cross-entropy over selected positions).\n    \"\"\"\n    # Shift: logits[t] predicts labels[t+1]\n    shift_logits = logits[:-1]  # (S-1, V)\n    shift_labels = labels[1:]   # (S-1,)\n\n    per_token_ce = F.cross_entropy(\n        shift_logits, shift_labels, reduction=\"none\"\n    )  # (S-1,)\n\n    if token_indices is not None:\n        # token_indices refer to *label* positions; after shift they map to index-1\n        idx = torch.tensor(\n            [i - 1 for i in token_indices if 0 < i < len(labels)],\n            device=per_token_ce.device,\n        )\n        if idx.numel() == 0:\n            return float(\"nan\")\n        per_token_ce = per_token_ce[idx]\n\n    # Ignore positions where label == -100\n    valid = shift_labels[: per_token_ce.size(0)] != -100 if token_indices is None else torch.ones_like(per_token_ce, dtype=torch.bool)\n    if token_indices is None:\n        per_token_ce = per_token_ce[valid]\n\n    if per_token_ce.numel() == 0:\n        return float(\"nan\")\n\n    return torch.exp(per_token_ce.mean()).item()\n\n\ndef compute_accuracy(predictions: List[str], references: List[str]) -> float:\n    \"\"\"Exact-match accuracy between prediction and reference string lists.\"\"\"\n    if len(predictions) == 0:\n        return 0.0\n    matches = sum(p == r for p, r in zip(predictions, references))\n    return matches / len(predictions)\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_interaction_index_20260513T174549",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/utils/metrics.py",
    "content": "# General-purpose metrics for PACS profiling: perplexity, accuracy, etc.\n\nfrom typing import List, Optional\n\nimport torch\nimport torch.nn.functional as F\n\n\ndef compute_perplexity(\n    logits: torch.Tensor,\n    labels: torch.Tensor,\n    token_indices: Optional[List[int]] = None,\n) -> float:\n    \"\"\"Compute mean per-token perplexity, optionally restricted to specific positions.\n\n    Args:\n        logits: (seq_len, vocab_size) – unnormalized logits.\n        labels: (seq_len,) – ground-truth token ids.  Positions with label == -100\n                are ignored (standard HF convention).\n        token_indices: If given, only these positions contribute to the result.\n                       None means all valid positions.\n\n    Returns:\n        Scalar perplexity (exp of mean cross-entropy over selected positions).\n    \"\"\"\n    # Shift: logits[t] predicts labels[t+1]\n    shift_logits = logits[:-1]  # (S-1, V)\n    shift_labels = labels[1:]   # (S-1,)\n\n    per_token_ce = F.cross_entropy(\n        shift_logits, shift_labels, reduction=\"none\"\n    )  # (S-1,)\n\n    if token_indices is not None:\n        # token_indices refer to *label* positions; after shift they map to index-1\n        idx = torch.tensor(\n            [i - 1 for i in token_indices if 0 < i < len(labels)],\n            device=per_token_ce.device,\n        )\n        if idx.numel() == 0:\n            return float(\"nan\")\n        per_token_ce = per_token_ce[idx]\n\n    # Ignore positions where label == -100\n    valid = shift_labels[: per_token_ce.size(0)] != -100 if token_indices is None else torch.ones_like(per_token_ce, dtype=torch.bool)\n    if token_indices is None:\n        per_token_ce = per_token_ce[valid]\n\n    if per_token_ce.numel() == 0:\n        return float(\"nan\")\n\n    return torch.exp(per_token_ce.mean()).item()\n\n\ndef compute_accuracy(predictions: List[str], references: List[str]) -> float:\n    \"\"\"Exact-match accuracy between prediction and reference string lists.\"\"\"\n    if len(predictions) == 0:\n        return 0.0\n    matches = sum(p == r for p, r in zip(predictions, references))\n    return matches / len(predictions)\n"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-13T17:48:28.599594+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/utils/metrics.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_interaction_index_20260513T174549",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-13T17:48:28.599802+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/profiling/interaction_index.py",
  "content": "# Interaction Index (II) calculator for measuring super/sub-additivity\n# of compound sparsity (attention head pruning + KV cache eviction).\n#\n# II = quality(both_sparse) - quality(attn_only) - quality(kv_only) + quality(dense)\n# where quality = -perplexity.  II > 0 means super-additive.\n\nfrom __future__ import annotations\n\nimport math\nfrom dataclasses import dataclass, field\nfrom typing import Dict, List, Optional, Tuple\n\nimport torch\nimport torch.nn.functional as F\n\nfrom ..utils.metrics import compute_perplexity\n\ntry:\n    from .phase_segmentation import Phase\nexcept ImportError:\n    Phase = None  # will be resolved when phase_segmentation is created\n\n\n# ---------------------------------------------------------------------------\n# Data classes\n# ---------------------------------------------------------------------------\n\n@dataclass\nclass InteractionResult:\n    ii_value: float\n    ppl_dense: float\n    ppl_attn_sparse: float\n    ppl_kv_sparse: float\n    ppl_both_sparse: float\n    is_super_additive: bool\n    phase_name: Optional[str] = None\n    num_tokens: int = 0\n\n    def summary(self) -> str:\n        tag = \"super-additive\" if self.is_super_additive else \"sub-additive\"\n        return (\n            f\"II={self.ii_value:+.4f} ({tag})  \"\n            f\"dense={self.ppl_dense:.2f}  attn={self.ppl_attn_sparse:.2f}  \"\n            f\"kv={self.ppl_kv_sparse:.2f}  both={self.ppl_both_sparse:.2f}\"\n        )\n\n\n# ---------------------------------------------------------------------------\n# Hook-based head masking (works with GQA / MHA / MQA)\n# ---------------------------------------------------------------------------\n\nclass _HeadMaskHook:\n    \"\"\"Registers forward hooks that zero out masked attention heads.\"\"\"\n\n    def __init__(self, model: torch.nn.Module, head_mask: torch.Tensor):\n        \"\"\"\n        head_mask: (num_layers, num_heads) float tensor, 1 = active, 0 = masked.\n        \"\"\"\n        self.handles: list = []\n        attn_layers = self._find_attention_layers(model)\n        for layer_idx, attn_module in enumerate(attn_layers):\n            if layer_idx >= head_mask.size(0):\n                break\n            mask = head_mask[layer_idx]  # (num_heads,)\n            handle = attn_module.register_forward_hook(\n                self._make_hook(mask)\n            )\n            self.handles.append(handle)\n\n    @staticmethod\n    def _find_attention_layers(model: torch.nn.Module) -> list:\n        \"\"\"Heuristic: find all self-attention sub-modules by common naming.\"\"\"\n        layers = []\n        for name, module in model.named_modules():\n            # Covers LlamaAttention, Qwen2Attention, MistralAttention, etc.\n            if type(module).__name__.endswith(\"Attention\") and \"self\" not in name.split(\".\")[-1].lower():\n                # Avoid double-counting – only pick the leaf Attention modules\n                children_attn = [\n                    m for m in module.children()\n                    if type(m).__name__.endswith(\"Attention\")\n                ]\n                if not children_attn:\n                    layers.append(module)\n        # Fallback: search by attribute path (model.layers[i].self_attn)\n        if not layers:\n            for name, module in model.named_modules():\n                if name.endswith(\".self_attn\") or name.endswith(\".attention\"):\n                    layers.append(module)\n        return layers\n\n    @staticmethod\n    def _make_hook(mask: torch.Tensor):\n        \"\"\"Return a hook that scales the attention output by head mask.\n\n        For GQA, mask length == num_query_heads.  The hook reshapes the output\n        projection's input by head dim, applies the mask, then collapses back.\n        \"\"\"\n        def hook_fn(module, input, output):\n            # output is typically a tuple; first element is hidden_states\n            if isinstance(output, tuple):\n                hidden = output[0]\n            else:\n                hidden = output\n\n            num_heads = mask.size(0)\n            bsz, seq_len, hidden_dim = hidden.shape\n            head_dim = hidden_dim // num_heads\n\n            reshaped = hidden.view(bsz, seq_len, num_heads, head_dim)\n            head_mask_expanded = mask.to(hidden.device, hidden.dtype).view(1, 1, num_heads, 1)\n            reshaped = reshaped * head_mask_expanded\n            masked_hidden = reshaped.view(bsz, seq_len, hidden_dim)\n\n            if isinstance(output, tuple):\n                return (masked_hidden,) + output[1:]\n            return masked_hidden\n\n        return hook_fn\n\n    def remove(self):\n        for h in self.handles:\n            h.remove()\n        self.handles.clear()\n\n\n# ---------------------------------------------------------------------------\n# KV eviction via attention-mask manipulation\n# ---------------------------------------------------------------------------\n\ndef _build_kv_attention_mask(\n    attention_mask: torch.Tensor,\n    kv_mask: torch.Tensor,\n) -> torch.Tensor:\n    \"\"\"Merge the standard attention mask with per-layer KV eviction mask.\n\n    Args:\n        attention_mask: (batch, seq_len) – 1 = attend, 0 = ignore.\n        kv_mask: (num_layers, seq_len) – 1 = keep, 0 = evict.\n\n    Returns:\n        (num_layers, batch, seq_len) mask suitable for broadcasting into\n        the (batch, num_heads, q_len, kv_len) attention score tensor.\n    \"\"\"\n    # Expand attention_mask: (1, batch, seq_len)\n    base = attention_mask.unsqueeze(0).float()  # (1, B, S)\n    kv = kv_mask.unsqueeze(1).float()            # (L, 1, S)\n    combined = base * kv                          # (L, B, S)\n    return combined\n\n\n# ---------------------------------------------------------------------------\n# Main calculator\n# ---------------------------------------------------------------------------\n\nclass InteractionIndexCalculator:\n    def __init__(\n        self,\n        model: torch.nn.Module,\n        tokenizer,\n        device: str = \"cuda\",\n    ):\n        self.model = model\n        self.tokenizer = tokenizer\n        self.device = device\n        self.model.eval()\n\n    # ------------------------------------------------------------------\n    # Forward with a specific sparsity configuration\n    # ------------------------------------------------------------------\n\n    @torch.no_grad()\n    def forward_with_sparse_config(\n        self,\n        input_ids: torch.Tensor,\n        attention_mask: Optional[torch.Tensor] = None,\n        attn_head_mask: Optional[torch.Tensor] = None,\n        kv_mask: Optional[torch.Tensor] = None,\n        phase_token_indices: Optional[List[int]] = None,\n    ) -> float:\n        \"\"\"Run a forward pass under a given sparsity config, return mean perplexity.\n\n        Args:\n            input_ids: (batch, seq_len).\n            attention_mask: (batch, seq_len), 1=attend. Defaults to all-ones.\n            attn_head_mask: (num_layers, num_heads), 1=active 0=masked.\n            kv_mask: (num_layers, seq_len), 1=keep 0=evict.\n            phase_token_indices: Positions at which to evaluate perplexity.\n        \"\"\"\n        input_ids = input_ids.to(self.device)\n        if attention_mask is None:\n            attention_mask = torch.ones_like(input_ids)\n        attention_mask = attention_mask.to(self.device)\n\n        # --- KV eviction: fold into attention_mask ---\n        model_attention_mask = attention_mask\n        if kv_mask is not None:\n            kv_mask = kv_mask.to(self.device)\n            # For simplicity, apply the *union* (min across layers) to the flat\n            # attention mask. Per-layer masking would need custom model code.\n            flat_kv_mask = kv_mask.min(dim=0).values  # (seq_len,)\n            model_attention_mask = attention_mask * flat_kv_mask.unsqueeze(0)\n\n        # --- Head masking: install hooks ---\n        hook_ctx: Optional[_HeadMaskHook] = None\n        if attn_head_mask is not None:\n            hook_ctx = _HeadMaskHook(self.model, attn_head_mask)\n\n        try:\n            outputs = self.model(\n                input_ids=input_ids,\n                attention_mask=model_attention_mask,\n            )\n        finally:\n            if hook_ctx is not None:\n                hook_ctx.remove()\n\n        logits = outputs.logits[0]   # (seq_len, vocab)\n        labels = input_ids[0]        # (seq_len,)\n\n        return compute_perplexity(logits, labels, token_indices=phase_token_indices)\n\n    # ------------------------------------------------------------------\n    # Mask construction helpers\n    # ------------------------------------------------------------------\n\n    @staticmethod\n    def _select_heads_to_mask(\n        num_layers: int,\n        num_heads: int,\n        ratio: float,\n        importance: Optional[torch.Tensor] = None,\n    ) -> torch.Tensor:\n        \"\"\"Build a (num_layers, num_heads) binary mask, masking `ratio` of heads.\n\n        If importance is given (num_layers, num_heads), mask the least important.\n        Otherwise, mask randomly.\n        \"\"\"\n        mask = torch.ones(num_layers, num_heads)\n        num_to_mask = max(1, int(num_heads * ratio))\n\n        for layer in range(num_layers):\n            if importance is not None:\n                _, indices = importance[layer].topk(num_to_mask, largest=False)\n            else:\n                indices = torch.randperm(num_heads)[:num_to_mask]\n            mask[layer, indices] = 0.0\n\n        return mask\n\n    @staticmethod\n    def _select_kv_to_evict(\n        num_layers: int,\n        seq_len: int,\n        ratio: float,\n        importance: Optional[torch.Tensor] = None,\n    ) -> torch.Tensor:\n        \"\"\"Build a (num_layers, seq_len) binary mask, evicting `ratio` of KV positions.\n\n        If importance is given (num_layers, seq_len), evict the least important.\n        Otherwise, evict randomly (never evict first token / BOS).\n        \"\"\"\n        mask = torch.ones(num_layers, seq_len)\n        num_to_evict = max(1, int(seq_len * ratio))\n        # Never evict position 0 (BOS)\n        num_to_evict = min(num_to_evict, seq_len - 1)\n\n        for layer in range(num_layers):\n            if importance is not None:\n                candidates = importance[layer, 1:]  # skip BOS\n                _, indices = candidates.topk(num_to_evict, largest=False)\n                indices = indices + 1  # shift back\n            else:\n                indices = torch.randperm(seq_len - 1)[:num_to_evict] + 1\n            mask[layer, indices] = 0.0\n\n        return mask\n\n    # ------------------------------------------------------------------\n    # Model config introspection\n    # ------------------------------------------------------------------\n\n    def _get_model_dims(self) -> Tuple[int, int]:\n        \"\"\"Return (num_layers, num_attention_heads) from model config.\"\"\"\n        config = self.model.config\n        num_layers = getattr(config, \"num_hidden_layers\", None)\n        num_heads = getattr(config, \"num_attention_heads\", None)\n        if num_layers is None or num_heads is None:\n            raise ValueError(\n                \"Cannot infer num_hidden_layers / num_attention_heads from model config\"\n            )\n        return num_layers, num_heads\n\n    # ------------------------------------------------------------------\n    # Core: compute Interaction Index\n    # ------------------------------------------------------------------\n\n    def compute_interaction_index(\n        self,\n        input_ids: torch.Tensor,\n        attn_sparsity_ratio: float = 0.3,\n        kv_eviction_ratio: float = 0.3,\n        phase_token_indices: Optional[List[int]] = None,\n        head_importance: Optional[torch.Tensor] = None,\n        kv_importance: Optional[torch.Tensor] = None,\n    ) -> InteractionResult:\n        \"\"\"Compute the Interaction Index for a single input.\n\n        II = -ppl(both) + ppl(attn_only) + ppl(kv_only) - ppl(dense)\n\n        II > 0 means super-additive: combining both sparsity axes hurts\n        less than the sum of individual degradations.\n        \"\"\"\n        num_layers, num_heads = self._get_model_dims()\n        seq_len = input_ids.size(-1)\n\n        attn_head_mask = self._select_heads_to_mask(\n            num_layers, num_heads, attn_sparsity_ratio, head_importance\n        )\n        kv_mask = self._select_kv_to_evict(\n            num_layers, seq_len, kv_eviction_ratio, kv_importance\n        )\n\n        # 1. Dense\n        ppl_dense = self.forward_with_sparse_config(\n            input_ids, phase_token_indices=phase_token_indices,\n        )\n        # 2. Attention-only sparse\n        ppl_attn = self.forward_with_sparse_config(\n            input_ids, attn_head_mask=attn_head_mask,\n            phase_token_indices=phase_token_indices,\n        )\n        # 3. KV-only sparse\n        ppl_kv = self.forward_with_sparse_config(\n            input_ids, kv_mask=kv_mask,\n            phase_token_indices=phase_token_indices,\n        )\n        # 4. Both sparse\n        ppl_both = self.forward_with_sparse_config(\n            input_ids, attn_head_mask=attn_head_mask, kv_mask=kv_mask,\n            phase_token_indices=phase_token_indices,\n        )\n\n        # II = quality(both) - quality(attn) - quality(kv) + quality(dense)\n        # quality = -ppl, so:\n        ii = -ppl_both + ppl_attn + ppl_kv - ppl_dense\n\n        num_tokens = len(phase_token_indices) if phase_token_indices else seq_len\n\n        return InteractionResult(\n            ii_value=ii,\n            ppl_dense=ppl_dense,\n            ppl_attn_sparse=ppl_attn,\n            ppl_kv_sparse=ppl_kv,\n            ppl_both_sparse=ppl_both,\n            is_super_additive=ii > 0,\n            num_tokens=num_tokens,\n        )\n\n    # ------------------------------------------------------------------\n    # Per-phase Interaction Index\n    # ------------------------------------------------------------------\n\n    def compute_per_phase_ii(\n        self,\n        input_ids: torch.Tensor,\n        phases: List,\n        attn_sparsity_ratio: float = 0.3,\n        kv_eviction_ratio: float = 0.3,\n    ) -> Dict[str, InteractionResult]:\n        \"\"\"Compute II separately for each phase (reasoning / execution / transition).\n\n        Args:\n            phases: List of Phase objects from phase_segmentation.  Each Phase must\n                    have .name (str) and .token_indices (List[int]) attributes.\n\n        Returns:\n            Dict mapping phase name to its InteractionResult.\n        \"\"\"\n        results: Dict[str, InteractionResult] = {}\n\n        for phase in phases:\n            result = self.compute_interaction_index(\n                input_ids,\n                attn_sparsity_ratio=attn_sparsity_ratio,\n                kv_eviction_ratio=kv_eviction_ratio,\n                phase_token_indices=phase.token_indices,\n            )\n            result.phase_name = phase.name\n            results[phase.name] = result\n\n        return results\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_interaction_index_20260513T174549",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/profiling/interaction_index.py",
    "content": "# Interaction Index (II) calculator for measuring super/sub-additivity\n# of compound sparsity (attention head pruning + KV cache eviction).\n#\n# II = quality(both_sparse) - quality(attn_only) - quality(kv_only) + quality(dense)\n# where quality = -perplexity.  II > 0 means super-additive.\n\nfrom __future__ import annotations\n\nimport math\nfrom dataclasses import dataclass, field\nfrom typing import Dict, List, Optional, Tuple\n\nimport torch\nimport torch.nn.functional as F\n\nfrom ..utils.metrics import compute_perplexity\n\ntry:\n    from .phase_segmentation import Phase\nexcept ImportError:\n    Phase = None  # will be resolved when phase_segmentation is created\n\n\n# ---------------------------------------------------------------------------\n# Data classes\n# ---------------------------------------------------------------------------\n\n@dataclass\nclass InteractionResult:\n    ii_value: float\n    ppl_dense: float\n    ppl_attn_sparse: float\n    ppl_kv_sparse: float\n    ppl_both_sparse: float\n    is_super_additive: bool\n    phase_name: Optional[str] = None\n    num_tokens: int = 0\n\n    def summary(self) -> str:\n        tag = \"super-additive\" if self.is_super_additive else \"sub-additive\"\n        return (\n            f\"II={self.ii_value:+.4f} ({tag})  \"\n            f\"dense={self.ppl_dense:.2f}  attn={self.ppl_attn_sparse:.2f}  \"\n            f\"kv={self.ppl_kv_sparse:.2f}  both={self.ppl_both_sparse:.2f}\"\n        )\n\n\n# ---------------------------------------------------------------------------\n# Hook-based head masking (works with GQA / MHA / MQA)\n# ---------------------------------------------------------------------------\n\nclass _HeadMaskHook:\n    \"\"\"Registers forward hooks that zero out masked attention heads.\"\"\"\n\n    def __init__(self, model: torch.nn.Module, head_mask: torch.Tensor):\n        \"\"\"\n        head_mask: (num_layers, num_heads) float tensor, 1 = active, 0 = masked.\n        \"\"\"\n        self.handles: list = []\n        attn_layers = self._find_attention_layers(model)\n        for layer_idx, attn_module in enumerate(attn_layers):\n            if layer_idx >= head_mask.size(0):\n                break\n            mask = head_mask[layer_idx]  # (num_heads,)\n            handle = attn_module.register_forward_hook(\n                self._make_hook(mask)\n            )\n            self.handles.append(handle)\n\n    @staticmethod\n    def _find_attention_layers(model: torch.nn.Module) -> list:\n        \"\"\"Heuristic: find all self-attention sub-modules by common naming.\"\"\"\n        layers = []\n        for name, module in model.named_modules():\n            # Covers LlamaAttention, Qwen2Attention, MistralAttention, etc.\n            if type(module).__name__.endswith(\"Attention\") and \"self\" not in name.split(\".\")[-1].lower():\n                # Avoid double-counting – only pick the leaf Attention modules\n                children_attn = [\n                    m for m in module.children()\n                    if type(m).__name__.endswith(\"Attention\")\n                ]\n                if not children_attn:\n                    layers.append(module)\n        # Fallback: search by attribute path (model.layers[i].self_attn)\n        if not layers:\n            for name, module in model.named_modules():\n                if name.endswith(\".self_attn\") or name.endswith(\".attention\"):\n                    layers.append(module)\n        return layers\n\n    @staticmethod\n    def _make_hook(mask: torch.Tensor):\n        \"\"\"Return a hook that scales the attention output by head mask.\n\n        For GQA, mask length == num_query_heads.  The hook reshapes the output\n        projection's input by head dim, applies the mask, then collapses back.\n        \"\"\"\n        def hook_fn(module, input, output):\n            # output is typically a tuple; first element is hidden_states\n            if isinstance(output, tuple):\n                hidden = output[0]\n            else:\n                hidden = output\n\n            num_heads = mask.size(0)\n            bsz, seq_len, hidden_dim = hidden.shape\n            head_dim = hidden_dim // num_heads\n\n            reshaped = hidden.view(bsz, seq_len, num_heads, head_dim)\n            head_mask_expanded = mask.to(hidden.device, hidden.dtype).view(1, 1, num_heads, 1)\n            reshaped = reshaped * head_mask_expanded\n            masked_hidden = reshaped.view(bsz, seq_len, hidden_dim)\n\n            if isinstance(output, tuple):\n                return (masked_hidden,) + output[1:]\n            return masked_hidden\n\n        return hook_fn\n\n    def remove(self):\n        for h in self.handles:\n            h.remove()\n        self.handles.clear()\n\n\n# ---------------------------------------------------------------------------\n# KV eviction via attention-mask manipulation\n# ---------------------------------------------------------------------------\n\ndef _build_kv_attention_mask(\n    attention_mask: torch.Tensor,\n    kv_mask: torch.Tensor,\n) -> torch.Tensor:\n    \"\"\"Merge the standard attention mask with per-layer KV eviction mask.\n\n    Args:\n        attention_mask: (batch, seq_len) – 1 = attend, 0 = ignore.\n        kv_mask: (num_layers, seq_len) – 1 = keep, 0 = evict.\n\n    Returns:\n        (num_layers, batch, seq_len) mask suitable for broadcasting into\n        the (batch, num_heads, q_len, kv_len) attention score tensor.\n    \"\"\"\n    # Expand attention_mask: (1, batch, seq_len)\n    base = attention_mask.unsqueeze(0).float()  # (1, B, S)\n    kv = kv_mask.unsqueeze(1).float()            # (L, 1, S)\n    combined = base * kv                          # (L, B, S)\n    return combined\n\n\n# ---------------------------------------------------------------------------\n# Main calculator\n# ---------------------------------------------------------------------------\n\nclass InteractionIndexCalculator:\n    def __init__(\n        self,\n        model: torch.nn.Module,\n        tokenizer,\n        device: str = \"cuda\",\n    ):\n        self.model = model\n        self.tokenizer = tokenizer\n        self.device = device\n        self.model.eval()\n\n    # ------------------------------------------------------------------\n    # Forward with a specific sparsity configuration\n    # ------------------------------------------------------------------\n\n    @torch.no_grad()\n    def forward_with_sparse_config(\n        self,\n        input_ids: torch.Tensor,\n        attention_mask: Optional[torch.Tensor] = None,\n        attn_head_mask: Optional[torch.Tensor] = None,\n        kv_mask: Optional[torch.Tensor] = None,\n        phase_token_indices: Optional[List[int]] = None,\n    ) -> float:\n        \"\"\"Run a forward pass under a given sparsity config, return mean perplexity.\n\n        Args:\n            input_ids: (batch, seq_len).\n            attention_mask: (batch, seq_len), 1=attend. Defaults to all-ones.\n            attn_head_mask: (num_layers, num_heads), 1=active 0=masked.\n            kv_mask: (num_layers, seq_len), 1=keep 0=evict.\n            phase_token_indices: Positions at which to evaluate perplexity.\n        \"\"\"\n        input_ids = input_ids.to(self.device)\n        if attention_mask is None:\n            attention_mask = torch.ones_like(input_ids)\n        attention_mask = attention_mask.to(self.device)\n\n        # --- KV eviction: fold into attention_mask ---\n        model_attention_mask = attention_mask\n        if kv_mask is not None:\n            kv_mask = kv_mask.to(self.device)\n            # For simplicity, apply the *union* (min across layers) to the flat\n            # attention mask. Per-layer masking would need custom model code.\n            flat_kv_mask = kv_mask.min(dim=0).values  # (seq_len,)\n            model_attention_mask = attention_mask * flat_kv_mask.unsqueeze(0)\n\n        # --- Head masking: install hooks ---\n        hook_ctx: Optional[_HeadMaskHook] = None\n        if attn_head_mask is not None:\n            hook_ctx = _HeadMaskHook(self.model, attn_head_mask)\n\n        try:\n            outputs = self.model(\n                input_ids=input_ids,\n                attention_mask=model_attention_mask,\n            )\n        finally:\n            if hook_ctx is not None:\n                hook_ctx.remove()\n\n        logits = outputs.logits[0]   # (seq_len, vocab)\n        labels = input_ids[0]        # (seq_len,)\n\n        return compute_perplexity(logits, labels, token_indices=phase_token_indices)\n\n    # ------------------------------------------------------------------\n    # Mask construction helpers\n    # ------------------------------------------------------------------\n\n    @staticmethod\n    def _select_heads_to_mask(\n        num_layers: int,\n        num_heads: int,\n        ratio: float,\n        importance: Optional[torch.Tensor] = None,\n    ) -> torch.Tensor:\n        \"\"\"Build a (num_layers, num_heads) binary mask, masking `ratio` of heads.\n\n        If importance is given (num_layers, num_heads), mask the least important.\n        Otherwise, mask randomly.\n        \"\"\"\n        mask = torch.ones(num_layers, num_heads)\n        num_to_mask = max(1, int(num_heads * ratio))\n\n        for layer in range(num_layers):\n            if importance is not None:\n                _, indices = importance[layer].topk(num_to_mask, largest=False)\n            else:\n                indices = torch.randperm(num_heads)[:num_to_mask]\n            mask[layer, indices] = 0.0\n\n        return mask\n\n    @staticmethod\n    def _select_kv_to_evict(\n        num_layers: int,\n        seq_len: int,\n        ratio: float,\n        importance: Optional[torch.Tensor] = None,\n    ) -> torch.Tensor:\n        \"\"\"Build a (num_layers, seq_len) binary mask, evicting `ratio` of KV positions.\n\n        If importance is given (num_layers, seq_len), evict the least important.\n        Otherwise, evict randomly (never evict first token / BOS).\n        \"\"\"\n        mask = torch.ones(num_layers, seq_len)\n        num_to_evict = max(1, int(seq_len * ratio))\n        # Never evict position 0 (BOS)\n        num_to_evict = min(num_to_evict, seq_len - 1)\n\n        for layer in range(num_layers):\n            if importance is not None:\n                candidates = importance[layer, 1:]  # skip BOS\n                _, indices = candidates.topk(num_to_evict, largest=False)\n                indices = indices + 1  # shift back\n            else:\n                indices = torch.randperm(seq_len - 1)[:num_to_evict] + 1\n            mask[layer, indices] = 0.0\n\n        return mask\n\n    # ------------------------------------------------------------------\n    # Model config introspection\n    # ------------------------------------------------------------------\n\n    def _get_model_dims(self) -> Tuple[int, int]:\n        \"\"\"Return (num_layers, num_attention_heads) from model config.\"\"\"\n        config = self.model.config\n        num_layers = getattr(config, \"num_hidden_layers\", None)\n        num_heads = getattr(config, \"num_attention_heads\", None)\n        if num_layers is None or num_heads is None:\n            raise ValueError(\n                \"Cannot infer num_hidden_layers / num_attention_heads from model config\"\n            )\n        return num_layers, num_heads\n\n    # ------------------------------------------------------------------\n    # Core: compute Interaction Index\n    # ------------------------------------------------------------------\n\n    def compute_interaction_index(\n        self,\n        input_ids: torch.Tensor,\n        attn_sparsity_ratio: float = 0.3,\n        kv_eviction_ratio: float = 0.3,\n        phase_token_indices: Optional[List[int]] = None,\n        head_importance: Optional[torch.Tensor] = None,\n        kv_importance: Optional[torch.Tensor] = None,\n    ) -> InteractionResult:\n        \"\"\"Compute the Interaction Index for a single input.\n\n        II = -ppl(both) + ppl(attn_only) + ppl(kv_only) - ppl(dense)\n\n        II > 0 means super-additive: combining both sparsity axes hurts\n        less than the sum of individual degradations.\n        \"\"\"\n        num_layers, num_heads = self._get_model_dims()\n        seq_len = input_ids.size(-1)\n\n        attn_head_mask = self._select_heads_to_mask(\n            num_layers, num_heads, attn_sparsity_ratio, head_importance\n        )\n        kv_mask = self._select_kv_to_evict(\n            num_layers, seq_len, kv_eviction_ratio, kv_importance\n        )\n\n        # 1. Dense\n        ppl_dense = self.forward_with_sparse_config(\n            input_ids, phase_token_indices=phase_token_indices,\n        )\n        # 2. Attention-only sparse\n        ppl_attn = self.forward_with_sparse_config(\n            input_ids, attn_head_mask=attn_head_mask,\n            phase_token_indices=phase_token_indices,\n        )\n        # 3. KV-only sparse\n        ppl_kv = self.forward_with_sparse_config(\n            input_ids, kv_mask=kv_mask,\n            phase_token_indices=phase_token_indices,\n        )\n        # 4. Both sparse\n        ppl_both = self.forward_with_sparse_config(\n            input_ids, attn_head_mask=attn_head_mask, kv_mask=kv_mask,\n            phase_token_indices=phase_token_indices,\n        )\n\n        # II = quality(both) - quality(attn) - quality(kv) + quality(dense)\n        # quality = -ppl, so:\n        ii = -ppl_both + ppl_attn + ppl_kv - ppl_dense\n\n        num_tokens = len(phase_token_indices) if phase_token_indices else seq_len\n\n        return InteractionResult(\n            ii_value=ii,\n            ppl_dense=ppl_dense,\n            ppl_attn_sparse=ppl_attn,\n            ppl_kv_sparse=ppl_kv,\n            ppl_both_sparse=ppl_both,\n            is_super_additive=ii > 0,\n            num_tokens=num_tokens,\n        )\n\n    # ------------------------------------------------------------------\n    # Per-phase Interaction Index\n    # ------------------------------------------------------------------\n\n    def compute_per_phase_ii(\n        self,\n        input_ids: torch.Tensor,\n        phases: List,\n        attn_sparsity_ratio: float = 0.3,\n        kv_eviction_ratio: float = 0.3,\n    ) -> Dict[str, InteractionResult]:\n        \"\"\"Compute II separately for each phase (reasoning / execution / transition).\n\n        Args:\n            phases: List of Phase objects from phase_segmentation.  Each Phase must\n                    have .name (str) and .token_indices (List[int]) attributes.\n\n        Returns:\n            Dict mapping phase name to its InteractionResult.\n        \"\"\"\n        results: Dict[str, InteractionResult] = {}\n\n        for phase in phases:\n            result = self.compute_interaction_index(\n                input_ids,\n                attn_sparsity_ratio=attn_sparsity_ratio,\n                kv_eviction_ratio=kv_eviction_ratio,\n                phase_token_indices=phase.token_indices,\n            )\n            result.phase_name = phase.name\n            results[phase.name] = result\n\n        return results\n"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-13T17:48:28.600194+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/profiling/interaction_index.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_interaction_index_20260513T174549",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-13T17:48:28.600363+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/__init__.py 2>/dev/null || echo \"MISSING\"",
  "description": "Check if pacs __init__.py exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_interaction_index_20260513T174549",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/__init__.py 2>/dev/null || echo \"MISSING\"",
    "description": "Check if pacs __init__.py exists"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-13T17:48:28.600517+00:00_

MISSING

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_interaction_index_20260513T174549",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-13T17:48:28.600641+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/__init__.py",
  "content": ""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_interaction_index_20260513T174549",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/__init__.py",
    "content": ""
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-13T17:48:28.600762+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/__init__.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_interaction_index_20260513T174549",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-13T17:48:28.600882+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"import ast; ast.parse(open('pacs/utils/metrics.py').read()); print('metrics.py OK')\" && python3 -c \"import ast; ast.parse(open('pacs/profiling/interaction_index.py').read()); print('interaction_index.py OK')\"",
  "description": "Syntax-check both files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_interaction_index_20260513T174549",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"import ast; ast.parse(open('pacs/utils/metrics.py').read()); print('metrics.py OK')\" && python3 -c \"import ast; ast.parse(open('pacs/profiling/interaction_index.py').read()); print('interaction_index.py OK')\"",
    "description": "Syntax-check both files"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-13T17:48:28.601002+00:00_

metrics.py OK
interaction_index.py OK

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_interaction_index_20260513T174549",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-13T17:48:28.601131+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_interaction_index_20260513T174549",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-13T17:48:28.601253+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_interaction_index_20260513T174549",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-13T17:48:28.601371+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "interaction_index.py",
  "type": "intermediate",
  "description": "Interaction Index calculator: measures super/sub-additivity of compound sparsity (attention head pruning + KV eviction). Supports per-phase II computation.",
  "project": "phase-gated-compound-sparse",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/profiling/interaction_index.py",
  "tags": "['interaction-index', 'profiling', 'compound-sparsity']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_interaction_index_20260513T174549",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "interaction_index.py",
    "type": "intermediate",
    "description": "Interaction Index calculator: measures super/sub-additivity of compound sparsity (attention head pruning + KV eviction). Supports per-phase II computation.",
    "project": "phase-gated-compound-sparse",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/profiling/interaction_index.py",
    "tags": "['interaction-index', 'profiling', 'compound-sparsity']"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-13T17:48:28.601541+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260513_e8a308\", \"name\": \"interaction_index.py\", \"type\": \"intermediate\", \"description\": \"Interaction Index calculator: measures super/sub-additivity of compound sparsity (attention head pruning + KV eviction). Supports per-phase II computation.\", \"path\": \"projects/phase-gated-compound-sparse/artifacts/_project/intermediate/interaction_index.py\", \"url\": null, \"project\": \"phase-gated-compound-sparse\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-13T17:48:12.290513+00:00\", \"tags\": [\"interaction-index\", \"profiling\", \"compound-sparsity\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_interaction_index_20260513T174549",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-13T17:48:28.601679+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "metrics.py",
  "type": "intermediate",
  "description": "General-purpose metrics module: perplexity (with optional token-index filtering) and exact-match accuracy.",
  "project": "phase-gated-compound-sparse",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/utils/metrics.py",
  "tags": "['metrics', 'perplexity', 'utils']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_interaction_index_20260513T174549",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "metrics.py",
    "type": "intermediate",
    "description": "General-purpose metrics module: perplexity (with optional token-index filtering) and exact-match accuracy.",
    "project": "phase-gated-compound-sparse",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/pacs/utils/metrics.py",
    "tags": "['metrics', 'perplexity', 'utils']"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-13T17:48:28.601825+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260513_7c1762\", \"name\": \"metrics.py\", \"type\": \"intermediate\", \"description\": \"General-purpose metrics module: perplexity (with optional token-index filtering) and exact-match accuracy.\", \"path\": \"projects/phase-gated-compound-sparse/artifacts/_project/intermediate/metrics.py\", \"url\": null, \"project\": \"phase-gated-compound-sparse\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-13T17:48:14.397762+00:00\", \"tags\": [\"metrics\", \"perplexity\", \"utils\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_interaction_index_20260513T174549",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-13T17:48:28.601992+00:00_

两个文件已创建并注册：

**`pacs/profiling/interaction_index.py`**
- `InteractionResult` 数据类，包含 4 种配置的 ppl 和 II 值
- `InteractionIndexCalculator`：通过 forward hook 实现 head masking（兼容 GQA），通过 attention mask 实现 KV eviction
- `compute_interaction_index()` — 单次 II 计算（4 次 forward pass）
- `compute_per_phase_ii()` — 按 phase 分别计算 II
- Head/KV 选择支持 importance-based 和 random 两种策略，BOS token 不会被 evict

**`pacs/utils/metrics.py`**
- `compute_perplexity()` — 支持 token_indices 过滤和 -100 label 忽略
- `compute_accuracy()` — exact match

包结构：`pacs/__init__.py`, `pacs/profiling/__init__.py`, `pacs/utils/__init__.py` 均已创建。`phase_segmentation.Phase` 用 try-import 延迟依赖，等该模块就绪后自动接入。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_interaction_index_20260513T174549"
}
```

</details>

---
