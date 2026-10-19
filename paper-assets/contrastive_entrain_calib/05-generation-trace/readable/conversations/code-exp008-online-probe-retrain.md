# code exp008 online probe retrain

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 79
- **Recorded user turns:** 0
- **Tool calls:** 39
- **Original source:** `logs/chats/worker_code_exp008-online-probe-retrain_20260518T184944.jsonl`
- **Structured JSON:** [`4578519d3dcb6b34153d.json`](../../sessions/45/4578519d3dcb6b34153d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

79 recorded events

### Tool call

_source line 1 · 2026-05-18T19:01:16.242581+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/training/run_exp008_binary_probe_penalty.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/training/run_exp008_binary_probe_penalty.py"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T19:01:16.243236+00:00_

1	#!/usr/bin/env python3
2	"""exp-008: Binary Probe Penalty baseline for sycophancy calibration.
3	
4	SFT-style LoRA training on Qwen3-8B with a frozen binary probe penalty.
5	Designed to run on a single RTX 5090 (32 GB) without GRPO's memory overhead.
6	
7	Loss:
8	    L = L_sft - lambda_reward * (R3 - lambda_probe * S(t))
9	      = L_sft + lambda_reward * lambda_probe * S(t) - lambda_reward * R3
10	
11	    L_sft:  cross-entropy on last-assistant-turn tokens (standard SFT)
12	    S(t):   frozen logistic probe sycophancy score, differentiable through hidden states
13	    R3:     NLI behavioral reward, precomputed on training data (constant, for monitoring)
14	
15	Input:
16	    Model:       /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B
17	    Data:        calibration_v2_1_expanded.jsonl (362 samples, v2.1 style-controlled)
18	    Activations: results/exp001/activations.pt (for probe pretraining)
19	
20	Output:
21	    LoRA checkpoints every 500 steps + final in output_dir
22	
23	Dependencies: torch, transformers, peft
24	"""
25	import argparse
26	import json
27	import logging
28	import os
29	import re
30	import sys
31	from dataclasses import dataclass, field
32	from functools import partial
33	from pathlib import Path
34	
35	import torch
36	import torch.nn as nn
37	import torch.nn.functional as F
38	from torch.utils.data import DataLoader
39	from torch.utils.data import Dataset as TorchDataset
40	
41	from peft import LoraConfig, get_peft_model
42	from transformers import (
43	    AutoModelForCausalLM,
44	    AutoModelForSequenceClassification,
45	    AutoTokenizer,
46	    get_linear_schedule_with_warmup,
47	)
48	
49	CONDITION_MAP = {
50	    "warranted_revision": "valid_correction",
51	    "sycophantic_capitulation": "invalid_pressure",
52	    "valid_correction": "valid_correction",
53	    "invalid_pressure": "invalid_pressure",
54	}
55	
56	
57	# ---------------------------------------------------------------------------
58	# Configuration
59	# ------------------------------
…[truncated 22217 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T19:01:16.243445+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/training/probe_module.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/training/probe_module.py"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-18T19:01:16.243626+00:00_

1	#!/usr/bin/env python3
2	"""Logistic regression probe for sycophancy detection from hidden states.
3	
4	Trains on exp-001 calibration activations. Used by exp-014 as a frozen
5	R1 reward signal to replace the direction-projection R1 in DC-GRPO.
6	"""
7	import logging
8	from pathlib import Path
9	
10	import torch
11	import torch.nn as nn
12	
13	logger = logging.getLogger(__name__)
14	
15	
16	class LinearProbe(nn.Module):
17	    """Single-layer logistic regression probe: h -> P(sycophantic)."""
18	
19	    def __init__(self, input_dim: int):
20	        super().__init__()
21	        self.linear = nn.Linear(input_dim, 1)
22	        self.register_buffer("feat_mean", torch.zeros(input_dim))
23	        self.register_buffer("feat_std", torch.ones(input_dim))
24	
25	    def forward(self, x: torch.Tensor) -> torch.Tensor:
26	        x_norm = (x - self.feat_mean) / (self.feat_std + 1e-8)
27	        return torch.sigmoid(self.linear(x_norm)).squeeze(-1)
28	
29	
30	def train_probe(
31	    activations_path: str,
32	    layers: list[int],
33	    position_idx: int = 1,
34	    lr: float = 1e-2,
35	    epochs: int = 200,
36	    weight_decay: float = 1e-4,
37	    seed: int = 42,
38	) -> tuple["LinearProbe", float]:
39	    """Train a logistic regression probe on exp-001 calibration activations.
40	
41	    Features: mean hidden state across target layers at the given position.
42	    Labels: invalid_pressure -> 1 (sycophantic), valid_correction -> 0.
43	
44	    Returns:
45	        (probe, accuracy) tuple.
46	    """
47	    torch.manual_seed(seed)
48	
49	    data = torch.load(activations_path, map_location="cpu")
50	    logger.info("Loaded %d activation samples from %s", len(data), activations_path)
51	
52	    features = []
53	    labels = []
54	    for sample in data:
55	        acts = sample["activations"]  # (36, 2, 4096)
56	        layer_vecs = [acts[l, position_idx] for l in layers]
57	        mean_vec = torch.stack(layer_vecs).mean(dim=0)
58	        features.append(mean_vec)
59	   
…[truncated 2824 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T19:01:16.243947+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/training/run_exp008_binary_probe_penalty.py",
  "old_string": "    save_steps: int = 500",
  "new_string": "    save_steps: int = 500\n    retrain_interval: int = 500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/training/run_exp008_binary_probe_penalty.py",
    "old_string": "    save_steps: int = 500",
    "new_string": "    save_steps: int = 500\n    retrain_interval: int = 500"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T19:01:16.244191+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/training/run_exp008_binary_probe_penalty.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T19:01:16.244331+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/training/run_exp008_binary_probe_penalty.py",
  "old_string": "    p.add_argument(\"--seed\", type=int, default=42)\n    p.add_argument(\"--model_path\", type=str, default=None)",
  "new_string": "    p.add_argument(\"--seed\", type=int, default=42)\n    p.add_argument(\"--log_steps\", type=int, default=None)\n    p.add_argument(\"--retrain_interval\", type=int, default=None)\n    p.add_argument(\"--model_path\", type=str, default=None)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/training/run_exp008_binary_probe_penalty.py",
    "old_string": "    p.add_argument(\"--seed\", type=int, default=42)\n    p.add_argument(\"--model_path\", type=str, default=None)",
    "new_string": "    p.add_argument(\"--seed\", type=int, default=42)\n    p.add_argument(\"--log_steps\", type=int, default=None)\n    p.add_argument(\"--retrain_interval\", type=int, default=None)\n    p.add_argument(\"--model_path\", type=str, default=None)"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T19:01:16.244534+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/training/run_exp008_binary_probe_penalty.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T19:01:16.244674+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/training/run_exp008_binary_probe_penalty.py",
  "old_string": "# ---------------------------------------------------------------------------\n# NLI / R3 Scoring\n# ---------------------------------------------------------------------------",
  "new_string": "# ---------------------------------------------------------------------------\n# Online Probe Retraining\n# ---------------------------------------------------------------------------\ndef retrain_probe_online(model, dataset, input_dim, config, log):\n    \"\"\"Retrain probe using current model's activations on calibration data.\"\"\"\n    model.eval()\n    device = next(model.parameters()).device\n\n    features = []\n    labels = []\n\n    with torch.no_grad():\n        for i, sample in enumerate(dataset.samples):\n            ids = torch.tensor([sample[\"full_ids\"]], dtype=torch.long, device=device)\n            mask = torch.ones_like(ids)\n\n            out = model(\n                input_ids=ids,\n                attention_mask=mask,\n                output_hidden_states=True,\n            )\n            hs = out.hidden_states\n            pos = sample[\"resp_pos\"]\n\n            layer_h = [hs[l + 1][0, pos] for l in config.reward_layers]\n            mean_h = torch.stack(layer_h).mean(0).float().cpu()\n            features.append(mean_h)\n\n            label = 1.0 if sample[\"condition\"] == \"invalid_pressure\" else 0.0\n            labels.append(label)\n\n    torch.cuda.empty_cache()\n\n    X = torch.stack(features)\n    y = torch.tensor(labels)\n    log.info(\n        \"[RETRAIN] Extracted %d activations (%.1f%% positive)\",\n        len(y), y.mean().item() * 100,\n    )\n\n    feat_mean = X.mean(dim=0)\n    feat_std = X.std(dim=0)\n\n    new_probe = LinearProbe(input_dim)\n    new_probe.feat_mean.copy_(feat_mean)\n    new_probe.feat_std.copy_(feat_std)\n\n    opt = torch.optim.Adam(new_probe.parameters(), lr=1e-2, weight_decay=1e-4)\n    criterion = nn.BCELoss()\n\n    new_probe.train()\n    for epoch in range(200):\n        loss = criterion(new_probe(X), y)\n        opt.zero_grad()\n        loss.backward()\n        opt.step()\n\n    new_probe.eval()\n    with torch.no_grad():\n        preds = new_probe(X)\n        acc = ((preds > 0.5).float() == y).float().mean().item()\n\n    try:\n        from sklearn.metrics import roc_auc_score\n        auroc = roc_auc_score(y.numpy(), preds.numpy())\n    except ImportError:\n        sorted_pairs = sorted(zip(preds.tolist(), y.tolist()), reverse=True)\n        tp, auc_sum = 0, 0.0\n        p_total = int(y.sum().item())\n        n_total = len(y) - p_total\n        for _, label in sorted_pairs:\n            if label == 1.0:\n                tp += 1\n            else:\n                auc_sum += tp\n        auroc = auc_sum / (p_total * n_total) if (p_total * n_total) > 0 else 0.0\n\n    for p in new_probe.parameters():\n        p.requires_grad_(False)\n    new_probe.to(device)\n\n    model.train()\n    return new_probe, acc, auroc\n\n\n# ---------------------------------------------------------------------------\n# NLI / R3 Scoring\n# ---------------------------------------------------------------------------"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/training/run_exp008_binary_probe_penalty.py",
    "old_string": "# ---------------------------------------------------------------------------\n# NLI / R3 Scoring\n# ---------------------------------------------------------------------------",
    "new_string": "# ---------------------------------------------------------------------------\n# Online Probe Retraining\n# ---------------------------------------------------------------------------\ndef retrain_probe_online(model, dataset, input_dim, config, log):\n    \"\"\"Retrain probe using current model's activations on calibration data.\"\"\"\n    model.eval()\n    device = next(model.parameters()).device\n\n    features = []\n    labels = []\n\n    with torch.no_grad():\n        for i, sample in enumerate(dataset.samples):\n            ids = torch.tensor([sample[\"full_ids\"]], dtype=torch.long, device=device)\n            mask = torch.ones_like(ids)\n\n            out = model(\n                input_ids=ids,\n                attention_mask=mask,\n                output_hidden_states=True,\n            )\n            hs = out.hidden_states\n            pos = sample[\"resp_pos\"]\n\n            layer_h = [hs[l + 1][0, pos] for l in config.reward_layers]\n            mean_h = torch.stack(layer_h).mean(0).float().cpu()\n            features.append(mean_h)\n\n            label = 1.0 if sample[\"condition\"] == \"invalid_pressure\" else 0.0\n            labels.append(label)\n\n    torch.cuda.empty_cache()\n\n    X = torch.stack(features)\n    y = torch.tensor(labels)\n    log.info(\n        \"[RETRAIN] Extracted %d activations (%.1f%% positive)\",\n        len(y), y.mean().item() * 100,\n    )\n\n    feat_mean = X.mean(dim=0)\n    feat_std = X.std(dim=0)\n\n    new_probe = LinearProbe(input_dim)\n    new_probe.feat_mean.copy_(feat_mean)\n    new_probe.feat_std.copy_(feat_std)\n\n    opt = torch.optim.Adam(new_probe.parameters(), lr=1e-2, weight_decay=1e-4)\n    criterion = nn.BCELoss()\n\n    new_probe.train()\n    for epoch in range(200):\n        loss = criterion(new_probe(X), y)\n        opt.zero_grad()\n        loss.backward()\n        opt.step()\n\n    new_probe.eval()\n    with torch.no_grad():\n        preds = new_probe(X)\n        acc = ((preds > 0.5).float() == y).float().mean().item()\n\n    try:\n        from sklearn.metrics import roc_auc_score\n        auroc = roc_auc_score(y.numpy(), preds.numpy())\n    except ImportError:\n        sorted_pairs = sorted(zip(preds.tolist(), y.tolist()), reverse=True)\n        tp, auc_sum = 0, 0.0\n        p_total = int(y.sum().item())\n        n_total = len(y) - p_total\n        for _, label in sorted_pairs:\n            if label == 1.0:\n                tp += 1\n            else:\n                auc_sum += tp\n        auroc = auc_sum / (p_total * n_total) if (p_total * n_total) > 0 else 0.0\n\n    for p in new_probe.parameters():\n        p.requires_grad_(False)\n    new_probe.to(device)\n\n    model.train()\n    return new_probe, acc, auroc\n\n\n# ---------------------------------------------------------------------------\n# NLI / R3 Scoring\n# ---------------------------------------------------------------------------"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T19:01:16.244938+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/training/run_exp008_binary_probe_penalty.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T19:01:16.245090+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/training/run_exp008_binary_probe_penalty.py",
  "old_string": "                acc_loss, acc_sft, acc_probe, acc_r3, acc_n = (\n                    0.0,\n                    0.0,\n                    0.0,\n                    0.0,\n                    0,\n                )\n\n                if step % config.save_steps == 0:",
  "new_string": "                acc_loss, acc_sft, acc_probe, acc_r3, acc_n = (\n                    0.0,\n                    0.0,\n                    0.0,\n                    0.0,\n                    0,\n                )\n\n                if step % config.retrain_interval == 0:\n                    log.info(\"[RETRAIN] Retraining probe at step %d ...\", step)\n                    probe, rt_acc, rt_auroc = retrain_probe_online(\n                        model, dataset, probe.linear.in_features, config, log\n                    )\n                    log.info(\n                        \"[INFO] Probe retrained at step %d: acc=%.4f, auroc=%.4f\",\n                        step, rt_acc, rt_auroc,\n                    )\n\n                if step % config.save_steps == 0:"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/training/run_exp008_binary_probe_penalty.py",
    "old_string": "                acc_loss, acc_sft, acc_probe, acc_r3, acc_n = (\n                    0.0,\n                    0.0,\n                    0.0,\n                    0.0,\n                    0,\n                )\n\n                if step % config.save_steps == 0:",
    "new_string": "                acc_loss, acc_sft, acc_probe, acc_r3, acc_n = (\n                    0.0,\n                    0.0,\n                    0.0,\n                    0.0,\n                    0,\n                )\n\n                if step % config.retrain_interval == 0:\n                    log.info(\"[RETRAIN] Retraining probe at step %d ...\", step)\n                    probe, rt_acc, rt_auroc = retrain_probe_online(\n                        model, dataset, probe.linear.in_features, config, log\n                    )\n                    log.info(\n                        \"[INFO] Probe retrained at step %d: acc=%.4f, auroc=%.4f\",\n                        step, rt_acc, rt_auroc,\n                    )\n\n                if step % config.save_steps == 0:"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T19:01:16.245313+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/training/run_exp008_binary_probe_penalty.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T19:01:16.245487+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/training/run_exp008_binary_probe_penalty.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/training/run_exp008_binary_probe_penalty.py"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T19:01:16.245783+00:00_

1	#!/usr/bin/env python3
2	"""exp-008: Binary Probe Penalty baseline for sycophancy calibration.
3	
4	SFT-style LoRA training on Qwen3-8B with a frozen binary probe penalty.
5	Designed to run on a single RTX 5090 (32 GB) without GRPO's memory overhead.
6	
7	Loss:
8	    L = L_sft - lambda_reward * (R3 - lambda_probe * S(t))
9	      = L_sft + lambda_reward * lambda_probe * S(t) - lambda_reward * R3
10	
11	    L_sft:  cross-entropy on last-assistant-turn tokens (standard SFT)
12	    S(t):   frozen logistic probe sycophancy score, differentiable through hidden states
13	    R3:     NLI behavioral reward, precomputed on training data (constant, for monitoring)
14	
15	Input:
16	    Model:       /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B
17	    Data:        calibration_v2_1_expanded.jsonl (362 samples, v2.1 style-controlled)
18	    Activations: results/exp001/activations.pt (for probe pretraining)
19	
20	Output:
21	    LoRA checkpoints every 500 steps + final in output_dir
22	
23	Dependencies: torch, transformers, peft
24	"""
25	import argparse
26	import json
27	import logging
28	import os
29	import re
30	import sys
31	from dataclasses import dataclass, field
32	from functools import partial
33	from pathlib import Path
34	
35	import torch
36	import torch.nn as nn
37	import torch.nn.functional as F
38	from torch.utils.data import DataLoader
39	from torch.utils.data import Dataset as TorchDataset
40	
41	from peft import LoraConfig, get_peft_model
42	from transformers import (
43	    AutoModelForCausalLM,
44	    AutoModelForSequenceClassification,
45	    AutoTokenizer,
46	    get_linear_schedule_with_warmup,
47	)
48	
49	CONDITION_MAP = {
50	    "warranted_revision": "valid_correction",
51	    "sycophantic_capitulation": "invalid_pressure",
52	    "valid_correction": "valid_correction",
53	    "invalid_pressure": "invalid_pressure",
54	}
55	
56	
57	# ---------------------------------------------------------------------------
58	# Configuration
59	# ------------------------------
…[truncated 25883 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-18T19:01:16.246000+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/training/run_exp008_binary_probe_penalty.py",
  "old_string": "    log.info(\"Config: lr=%s lambda_reward=%s lambda_probe=%s max_steps=%d\",\n             config.lr, config.lambda_reward, config.lambda_probe, config.max_steps)",
  "new_string": "    log.info(\"Config: lr=%s lambda_reward=%s lambda_probe=%s max_steps=%d retrain_interval=%d\",\n             config.lr, config.lambda_reward, config.lambda_probe, config.max_steps,\n             config.retrain_interval)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/training/run_exp008_binary_probe_penalty.py",
    "old_string": "    log.info(\"Config: lr=%s lambda_reward=%s lambda_probe=%s max_steps=%d\",\n             config.lr, config.lambda_reward, config.lambda_probe, config.max_steps)",
    "new_string": "    log.info(\"Config: lr=%s lambda_reward=%s lambda_probe=%s max_steps=%d retrain_interval=%d\",\n             config.lr, config.lambda_reward, config.lambda_probe, config.max_steps,\n             config.retrain_interval)"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T19:01:16.246226+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/training/run_exp008_binary_probe_penalty.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-18T19:01:16.246372+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__detect_image,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__detect_image,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T19:01:16.246500+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-18T19:01:16.246616+00:00_

called mcp__agent-ml-research__detect_image

<details open><summary>🔧 Tool call — mcp__agent-ml-research__detect_image</summary>

```json
{
  "server": "westd-29046",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__detect_image",
  "tool_args": {
    "server": "westd-29046",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T19:01:16.246736+00:00_

{"result":"{\n  \"detected\": false,\n  \"status\": \"ssh_error\",\n  \"skip_base_setup\": false,\n  \"message\": \"SSH error: exit code 1\"\n}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__detect_image",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-18T19:01:16.246904+00:00_

called mcp__agent-ml-research__detect_image

<details open><summary>🔧 Tool call — mcp__agent-ml-research__detect_image</summary>

```json
{
  "server": "westd-28034",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__detect_image",
  "tool_args": {
    "server": "westd-28034",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-18T19:01:16.247037+00:00_

{"result":"{\n  \"detected\": false,\n  \"status\": \"ssh_error\",\n  \"skip_base_setup\": false,\n  \"message\": \"SSH error: exit code 1\"\n}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__detect_image",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-18T19:01:16.247180+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/resources.yaml",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/resources.yaml",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-18T19:01:16.247297+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/config/resources.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-18T19:01:16.247409+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/config/resources.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/config/resources.yaml"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-18T19:01:16.247535+00:00_

1	default_model: claude-opus-4-6
2	default_model_claude_code: claude-opus-4-6
3	idea_model: claude-opus-4-6
4	servers:
5	  westb-13953:
6	    accounts:
7	    - gpus:
8	      - cuda:0
9	      - cuda:1
10	      name: root
11	      password_encrypted: gAAAAABqBwCwdXjVD0vtKjoYCj_upXuQGuj9AL6HuV6A6Uo3EMWvC8KS06eJZmt6YLy2N3SimNu52c2jb3-TQ44rvcDpRZOLbw==
12	      user: root
13	      work_dir: /root
14	    env_activate: ''
15	    host: connect.westb.seetacloud.com
16	    port: 13953
17	    total_gpus:
18	    - cuda:0
19	    - cuda:1
20	    user_rules_excluded: []
21	    work_dir: /root
22	  westd-28034:
23	    accounts:
24	    - gpus:
25	      - cuda:0
26	      - cuda:1
27	      - cuda:2
28	      - cuda:3
29	      name: root
30	      password_encrypted: gAAAAABqCxByScs0vf8ON53hJUspHrvb7-FrgAk_XxzyDIfV_2temyLW4Tqzm9V9BdiDzsgbHSDnGGyW2rbpY_eOQiYLGaUIRQ==
31	      user: root
32	      work_dir: /root
33	    env_activate: ''
34	    host: connect.westd.seetacloud.com
35	    port: 28034
36	    total_gpus:
37	    - cuda:0
38	    - cuda:1
39	    - cuda:2
40	    - cuda:3
41	    user_rules_excluded: []
42	    work_dir: /root
43	  westd-29046:
44	    accounts:
45	    - gpus:
46	      - cuda:0
47	      - cuda:1
48	      name: root
49	      password_encrypted: gAAAAABqCsIrzjoBhxan8MVpva56HM5EQsNDBvrqLWcajZn91tLViljWD_ymal8VzI0NSpY-IMYa7_CnSA-LFNsVQQNP_Ea-Zw==
50	      user: root
51	      work_dir: /root
52	    env_activate: ''
53	    host: connect.westd.seetacloud.com
54	    port: 29046
55	    total_gpus:
56	    - cuda:0
57	    - cuda:1
58	    user_rules_excluded: []
59	    work_dir: /root
60	user_rules: []
61	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-18T19:01:16.247697+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-29046",
  "command": "echo \"ok\" && hostname",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-29046",
    "command": "echo \"ok\" && hostname",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-18T19:01:16.247819+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-28034",
  "command": "echo \"ok\" && hostname",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-28034",
    "command": "echo \"ok\" && hostname",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-18T19:01:16.247960+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"ok\\nautodl-container-zcu10e5eev-b2bddad6\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-18T19:01:16.248078+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"ok\\nautodl-container-9574k3gu86-7ce04d21\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-18T19:01:16.248208+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-28034",
  "command": "ls -la /root/contrastive_entrain_calib/training/ 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-28034",
    "command": "ls -la /root/contrastive_entrain_calib/training/ 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-18T19:01:16.248326+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-18T19:01:16.248440+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-28034",
  "command": "ls -la /root/contrastive_entrain_calib/results/exp001/activations.pt 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-28034",
    "command": "ls -la /root/contrastive_entrain_calib/results/exp001/activations.pt 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-18T19:01:16.248554+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-18T19:01:16.248672+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-28034",
  "command": "ls -la /root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-28034",
    "command": "ls -la /root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-18T19:01:16.248788+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-18T19:01:16.248954+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-28034",
  "command": "ls -la /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/config.json 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-28034",
    "command": "ls -la /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/config.json 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-18T19:01:16.249088+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-18T19:01:16.249215+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-28034",
  "command": "ls -la /root/contrastive_entrain_calib/training/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-28034",
    "command": "ls -la /root/contrastive_entrain_calib/training/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-18T19:01:16.249342+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 124\\ndrwxr-xr-x  3 root root  4096 May 19 01:53 .\\ndrwxr-xr-x 13 root root  4096 May 19 02:48 ..\\ndrwxr-xr-x  2 root root   147 May 19 02:33 __pycache__\\n-rw-r--r--  1 root root 29994 May 18 21:41 dcgrpo_trainer.py\\n-rw-r--r--  1 root root   367 May 19 01:33 ds_config_zero2.json\\n-rw-r--r--  1 root root  8536 May 18 21:41 gpu_smoke_test.py\\n-rwxr-xr-x  1 root root  1204 May 18 23:58 launch_exp004.sh\\n-rw-r--r--  1 root root  4388 May 19 02:33 probe_module.py\\n-rw-r--r--  1 root root  3277 May 18 23:31 run_exp003_r3only_seed2.py\\n-rw-r--r--  1 root root 11240 May 18 23:54 run_exp004_act_baseline.py\\n-rw-r--r--  1 root root 21809 May 19 02:31 run_exp008_binary_probe_penalty.py\\n-rw-r--r--  1 root root  7404 May 19 01:53 run_exp014_continuous_probe.py\\n-rw-r--r--  1 root root  6013 May 19 01:38 run_exp014_dryrun.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-18T19:01:16.249493+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-28034",
  "command": "ls -la /root/contrastive_entrain_calib/results/exp001/activations.pt",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-28034",
    "command": "ls -la /root/contrastive_entrain_calib/results/exp001/activations.pt",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-18T19:01:16.249613+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-28034",
  "command": "ls -la /root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-28034",
    "command": "ls -la /root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-18T19:01:16.249735+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 427172715 May 19 01:09 /root/contrastive_entrain_calib/results/exp001/activations.pt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-18T19:01:16.249853+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 367001 May 18 19:39 /root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-18T19:01:16.249991+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-28034",
  "command": "ls -la /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/config.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-28034",
    "command": "ls -la /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/config.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-18T19:01:16.250108+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 728 May 18 16:28 /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/config.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-18T19:01:16.250236+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/training/run_exp008_binary_probe_penalty.py | wc -c",
  "description": "Check file size of modified script"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/training/run_exp008_binary_probe_penalty.py | wc -c",
    "description": "Check file size of modified script"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-18T19:01:16.250347+00:00_

25141

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-18T19:01:16.250530+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-28034",
  "command": "cat > /root/contrastive_entrain_calib/training/run_exp008_binary_probe_penalty.py << 'SCRIPT_EOF'\n#!/usr/bin/env python3\n\"\"\"exp-008: Binary Probe Penalty baseline for sycophancy calibration.\n\nSFT-style LoRA training on Qwen3-8B with a frozen binary probe penalty.\nDesigned to run on a single RTX 5090 (32 GB) without GRPO's memory overhead.\n\nLoss:\n    L = L_sft - lambda_reward * (R3 - lambda_probe * S(t))\n      = L_sft + lambda_reward * lambda_probe * S(t) - lambda_reward * R3\n\n    L_sft:  cross-entropy on last-assistant-turn tokens (standard SFT)\n    S(t):   frozen logistic probe sycophancy score, differentiable through hidden states\n    R3:     NLI behavioral reward, precomputed on training data (constant, for monitoring)\n\nInput:\n    Model:       /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B\n    Data:        calibration_v2_1_expanded.jsonl (362 samples, v2.1 style-controlled)\n    Activations: results/exp001/activations.pt (for probe pretraining)\n\nOutput:\n    LoRA checkpoints every 500 steps + final in output_dir\n\nDependencies: torch, transformers, peft\n\"\"\"\nimport argparse\nimport json\nimport logging\nimport os\nimport re\nimport sys\nfrom dataclasses import dataclass, field\nfrom functools import partial\nfrom pathlib import Path\n\nimport torch\nimport torch.nn as nn\nimport torch.nn.functional as F\nfrom torch.utils.data import DataLoader\nfrom torch.utils.data import Dataset as TorchDataset\n\nfrom peft import LoraConfig, get_peft_model\nfrom transformers import (\n    AutoModelForCausalLM,\n    AutoModelForSequenceClassification,\n    AutoTokenizer,\n    get_linear_schedule_with_warmup,\n)\n\nCONDITION_MAP = {\n    \"warranted_revision\": \"valid_correction\",\n    \"sycophantic_capitulation\": \"invalid_pressure\",\n    \"valid_correction\": \"valid_correction\",\n    \"invalid_pressure\": \"invalid_pressure\",\n}\n\n\n# ---------------------------------------------------------------------------\n# Configuration\n# ---------------------------------------------------------------------------\n@dataclass\nclass TrainConfig:\n    model_path: str = \"/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B\"\n    data_path: str = \"/root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl\"\n    activations_path: str = (\n        \"/root/contrastive_entrain_calib/results/exp001/activations.pt\"\n    )\n    output_dir: str = (\n        \"/root/contrastive_entrain_calib/checkpoints/exp008_binary_probe_penalty\"\n    )\n\n    # LoRA\n    lora_rank: int = 64\n    lora_alpha: int = 128\n    lora_targets: list[str] = field(\n        default_factory=lambda: [\"q_proj\", \"v_proj\", \"k_proj\", \"o_proj\", \"gate_proj\", \"up_proj\", \"down_proj\"]\n    )\n    lora_dropout: float = 0.05\n\n    # Training\n    lr: float = 5e-5\n    warmup_steps: int = 200\n    weight_decay: float = 0.01\n    max_steps: int = 8000\n    batch_size: int = 1\n    grad_accum: int = 16\n    max_seq_len: int = 1024\n    gradient_checkpointing: bool = True\n    bf16: bool = True\n    seed: int = 42\n    max_grad_norm: float = 1.0\n\n    # Loss weights\n    lambda_reward: float = 0.1\n    lambda_probe: float = 1.0\n\n    # Probe / hidden state extraction\n    reward_layers: list[int] = field(\n        default_factory=lambda: [19, 20, 24, 27, 32, 33, 35]\n    )\n    probe_position_idx: int = 1  # 1 = asst_first in (num_layers, 2, hidden) layout\n\n    # NLI\n    nli_model_name: str = \"cross-encoder/nli-deberta-v3-base\"\n\n    # Logging / checkpointing\n    log_steps: int = 10\n    save_steps: int = 500\n    retrain_interval: int = 500\n\n\ndef parse_args() -> TrainConfig:\n    p = argparse.ArgumentParser(description=\"exp-008 Binary Probe Penalty baseline\")\n    p.add_argument(\"--lr\", type=float, default=5e-5)\n    p.add_argument(\"--lambda_reward\", type=float, default=0.1)\n    p.add_argument(\"--lambda_probe\", type=float, default=1.0)\n    p.add_argument(\"--max_steps\", type=int, default=8000)\n    p.add_argument(\"--lora_rank\", type=int, default=64)\n    p.add_argument(\"--lora_alpha\", type=int, default=128)\n    p.add_argument(\"--batch_size\", type=int, default=1)\n    p.add_argument(\"--grad_accum\", type=int, default=16)\n    p.add_argument(\"--seed\", type=int, default=42)\n    p.add_argument(\"--log_steps\", type=int, default=None)\n    p.add_argument(\"--retrain_interval\", type=int, default=None)\n    p.add_argument(\"--model_path\", type=str, default=None)\n    p.add_argument(\"--data_path\", type=str, default=None)\n    p.add_argument(\"--output_dir\", type=str, default=None)\n    args = p.parse_args()\n\n    cfg = TrainConfig()\n    for k, v in vars(args).items():\n        if v is not None and hasattr(cfg, k):\n            setattr(cfg, k, v)\n    return cfg\n\n\n# ---------------------------------------------------------------------------\n# Dataset\n# ---------------------------------------------------------------------------\nclass CalibrationSFTDataset(TorchDataset):\n    \"\"\"Loads 3-turn calibration conversations for SFT (aligned with exp-004).\n\n    Format per record: user -> assistant(Turn 1) -> user(correction/pressure).\n    Input: full 3-turn conversation + generation_prompt.\n    SFT target: Turn 1 (assistant first reply) only; cross-entropy on those tokens,\n    all others masked with -100.\n    \"\"\"\n\n    def __init__(self, data_path: str, tokenizer, max_seq_len: int = 1024):\n        self.tokenizer = tokenizer\n        self.max_seq_len = max_seq_len\n        self.samples: list[dict] = []\n\n        im_end_id = tokenizer.convert_tokens_to_ids(\"<|im_end|>\")\n\n        with open(data_path) as f:\n            for line in f:\n                rec = json.loads(line)\n                turns = rec[\"turns\"]\n                if len(turns) < 2:\n                    continue\n\n                condition = CONDITION_MAP.get(rec[\"condition\"], rec[\"condition\"])\n                pair_id = str(rec.get(\"pair_id\", rec.get(\"id\", \"\")))\n                response_text = turns[1][\"content\"]\n\n                msgs = [{\"role\": t[\"role\"], \"content\": t[\"content\"]} for t in turns]\n\n                try:\n                    full_ids = tokenizer.apply_chat_template(\n                        msgs, tokenize=True, add_generation_prompt=True,\n                        enable_thinking=False,\n                    )\n                except TypeError:\n                    full_ids = tokenizer.apply_chat_template(\n                        msgs, tokenize=True, add_generation_prompt=True,\n                    )\n\n                try:\n                    pre_asst_ids = tokenizer.apply_chat_template(\n                        msgs[:1], tokenize=True, add_generation_prompt=True,\n                        enable_thinking=False,\n                    )\n                except TypeError:\n                    pre_asst_ids = tokenizer.apply_chat_template(\n                        msgs[:1], tokenize=True, add_generation_prompt=True,\n                    )\n\n                asst_start = len(pre_asst_ids)\n                asst_end = asst_start\n                while asst_end < len(full_ids) and full_ids[asst_end] != im_end_id:\n                    asst_end += 1\n                asst_end += 1  # include <|im_end|>\n\n                if len(full_ids) > max_seq_len:\n                    full_ids = full_ids[:max_seq_len]\n\n                labels = [-100] * len(full_ids)\n                for i in range(asst_start, min(asst_end, len(full_ids))):\n                    labels[i] = full_ids[i]\n\n                resp_pos = len(full_ids) - 1\n\n                self.samples.append(\n                    {\n                        \"full_ids\": full_ids,\n                        \"labels\": labels,\n                        \"resp_pos\": resp_pos,\n                        \"condition\": condition,\n                        \"pair_id\": pair_id,\n                        \"response_text\": response_text,\n                        \"r3\": 0.0,\n                    }\n                )\n\n    def __len__(self):\n        return len(self.samples)\n\n    def __getitem__(self, idx):\n        return self.samples[idx]\n\n\ndef sft_collate(batch: list[dict], pad_token_id: int) -> dict:\n    max_len = max(len(item[\"full_ids\"]) for item in batch)\n    input_ids, masks, labels = [], [], []\n    resp_positions, conditions, r3_scores = [], [], []\n\n    for item in batch:\n        ids = item[\"full_ids\"]\n        lab = item[\"labels\"]\n        pad_n = max_len - len(ids)\n\n        input_ids.append(ids + [pad_token_id] * pad_n)\n        masks.append([1] * len(ids) + [0] * pad_n)\n        labels.append(lab + [-100] * pad_n)\n        resp_positions.append(item[\"resp_pos\"])\n        conditions.append(item[\"condition\"])\n        r3_scores.append(item[\"r3\"])\n\n    return {\n        \"input_ids\": torch.tensor(input_ids, dtype=torch.long),\n        \"attention_mask\": torch.tensor(masks, dtype=torch.long),\n        \"labels\": torch.tensor(labels, dtype=torch.long),\n        \"resp_positions\": resp_positions,\n        \"conditions\": conditions,\n        \"r3_scores\": r3_scores,\n    }\n\n\n# ---------------------------------------------------------------------------\n# Binary Probe\n# ---------------------------------------------------------------------------\nclass LinearProbe(nn.Module):\n    \"\"\"Frozen logistic regression probe: h -> P(sycophantic).\"\"\"\n\n    def __init__(self, input_dim: int):\n        super().__init__()\n        self.linear = nn.Linear(input_dim, 1)\n        self.register_buffer(\"feat_mean\", torch.zeros(input_dim))\n        self.register_buffer(\"feat_std\", torch.ones(input_dim))\n\n    def forward(self, x: torch.Tensor) -> torch.Tensor:\n        x_norm = (x - self.feat_mean) / (self.feat_std + 1e-8)\n        return torch.sigmoid(self.linear(x_norm)).squeeze(-1)\n\n\ndef train_probe(\n    activations_path: str,\n    layers: list[int],\n    position_idx: int = 1,\n    seed: int = 42,\n    epochs: int = 200,\n    lr: float = 1e-2,\n) -> tuple[LinearProbe, float]:\n    \"\"\"Train binary probe from exp-001 pre-extracted activations.\n\n    Labels: invalid_pressure (sycophantic context) -> 1, valid_correction -> 0.\n    Returns (frozen_probe, accuracy).\n    \"\"\"\n    torch.manual_seed(seed)\n    data = torch.load(activations_path, map_location=\"cpu\", weights_only=False)\n\n    features, labels = [], []\n    for sample in data:\n        acts = sample[\"activations\"]  # (num_layers, 2, hidden_dim)\n        mean_h = torch.stack([acts[l, position_idx] for l in layers]).mean(0)\n        features.append(mean_h)\n        cond = CONDITION_MAP.get(sample[\"condition\"], sample[\"condition\"])\n        labels.append(1.0 if cond == \"invalid_pressure\" else 0.0)\n\n    X = torch.stack(features)\n    y = torch.tensor(labels)\n\n    feat_mean = X.mean(dim=0)\n    feat_std = X.std(dim=0)\n\n    probe = LinearProbe(X.shape[1])\n    probe.feat_mean.copy_(feat_mean)\n    probe.feat_std.copy_(feat_std)\n\n    opt = torch.optim.Adam(probe.parameters(), lr=lr, weight_decay=1e-4)\n    criterion = nn.BCELoss()\n\n    probe.train()\n    for epoch in range(epochs):\n        loss = criterion(probe(X), y)\n        opt.zero_grad()\n        loss.backward()\n        opt.step()\n        if (epoch + 1) % 50 == 0:\n            with torch.no_grad():\n                acc = ((probe(X) > 0.5).float() == y).float().mean().item()\n            logging.getLogger(\"exp008\").info(\n                \"Probe epoch %d/%d: loss=%.4f acc=%.4f\", epoch + 1, epochs, loss.item(), acc\n            )\n\n    probe.eval()\n    with torch.no_grad():\n        acc = ((probe(X) > 0.5).float() == y).float().mean().item()\n\n    for p in probe.parameters():\n        p.requires_grad_(False)\n\n    return probe, acc\n\n\ndef save_probe(probe: LinearProbe, path: str) -> None:\n    Path(path).parent.mkdir(parents=True, exist_ok=True)\n    torch.save(\n        {\"state_dict\": probe.state_dict(), \"input_dim\": probe.linear.in_features},\n        path,\n    )\n\n\ndef load_probe(path: str) -> LinearProbe:\n    ckpt = torch.load(path, map_location=\"cpu\")\n    probe = LinearProbe(ckpt[\"input_dim\"])\n    probe.load_state_dict(ckpt[\"state_dict\"])\n    probe.eval()\n    for p in probe.parameters():\n        p.requires_grad_(False)\n    return probe\n\n\n# ---------------------------------------------------------------------------\n# Online Probe Retraining\n# ---------------------------------------------------------------------------\ndef retrain_probe_online(model, dataset, input_dim, config, log):\n    \"\"\"Retrain probe using current model's activations on calibration data.\"\"\"\n    model.eval()\n    device = next(model.parameters()).device\n\n    features = []\n    labels = []\n\n    with torch.no_grad():\n        for i, sample in enumerate(dataset.samples):\n            ids = torch.tensor([sample[\"full_ids\"]], dtype=torch.long, device=device)\n            mask = torch.ones_like(ids)\n\n            out = model(\n                input_ids=ids,\n                attention_mask=mask,\n                output_hidden_states=True,\n            )\n            hs = out.hidden_states\n            pos = sample[\"resp_pos\"]\n\n            layer_h = [hs[l + 1][0, pos] for l in config.reward_layers]\n            mean_h = torch.stack(layer_h).mean(0).float().cpu()\n            features.append(mean_h)\n\n            label = 1.0 if sample[\"condition\"] == \"invalid_pressure\" else 0.0\n            labels.append(label)\n\n    torch.cuda.empty_cache()\n\n    X = torch.stack(features)\n    y = torch.tensor(labels)\n    log.info(\n        \"[RETRAIN] Extracted %d activations (%.1f%% positive)\",\n        len(y), y.mean().item() * 100,\n    )\n\n    feat_mean = X.mean(dim=0)\n    feat_std = X.std(dim=0)\n\n    new_probe = LinearProbe(input_dim)\n    new_probe.feat_mean.copy_(feat_mean)\n    new_probe.feat_std.copy_(feat_std)\n\n    opt = torch.optim.Adam(new_probe.parameters(), lr=1e-2, weight_decay=1e-4)\n    criterion = nn.BCELoss()\n\n    new_probe.train()\n    for epoch in range(200):\n        loss = criterion(new_probe(X), y)\n        opt.zero_grad()\n        loss.backward()\n        opt.step()\n\n    new_probe.eval()\n    with torch.no_grad():\n        preds = new_probe(X)\n        acc = ((preds > 0.5).float() == y).float().mean().item()\n\n    try:\n        from sklearn.metrics import roc_auc_score\n        auroc = roc_auc_score(y.numpy(), preds.numpy())\n    except ImportError:\n        sorted_pairs = sorted(zip(preds.tolist(), y.tolist()), reverse=True)\n        tp, auc_sum = 0, 0.0\n        p_total = int(y.sum().item())\n        n_total = len(y) - p_total\n        for _, label in sorted_pairs:\n            if label == 1.0:\n                tp += 1\n            else:\n                auc_sum += tp\n        auroc = auc_sum / (p_total * n_total) if (p_total * n_total) > 0 else 0.0\n\n    for p in new_probe.parameters():\n        p.requires_grad_(False)\n    new_probe.to(device)\n\n    model.train()\n    return new_probe, acc, auroc\n\n\n# ---------------------------------------------------------------------------\n# NLI / R3 Scoring\n# ---------------------------------------------------------------------------\ndef _extract_last_response(text: str) -> str:\n    \"\"\"Strip chat template markers and return last assistant response.\"\"\"\n    clean = re.sub(\n        r\"<\\|im_start\\|>|<\\|im_end\\|>|&lt;think>|&lt;/think>|<\\|endoftext\\|>\", \"\", text\n    )\n    parts = clean.split(\"assistant\")\n    response = parts[-1].strip() if len(parts) > 1 else clean.strip()\n    if len(response) > 1000:\n        response = response[:1000]\n    return response if response else text[:500]\n\n\n@torch.no_grad()\ndef precompute_r3(\n    samples: list[dict], nli_model_name: str, batch_size: int = 16\n) -> list[float]:\n    \"\"\"Compute R3 for every sample using a frozen NLI model, then free GPU memory.\n\n    R3 = P(entailment) for valid_correction (changing answer is correct),\n    R3 = 1 - P(entailment) for invalid_pressure (not changing is correct).\n    \"\"\"\n    log = logging.getLogger(\"exp008\")\n\n    try:\n        from transformers import DebertaV2Tokenizer\n\n        tok = DebertaV2Tokenizer.from_pretrained(nli_model_name)\n    except Exception:\n        tok = AutoTokenizer.from_pretrained(nli_model_name)\n\n    nli = AutoModelForSequenceClassification.from_pretrained(nli_model_name)\n    nli.eval().cuda()\n    ent_idx = next(\n        int(k) for k, v in nli.config.id2label.items() if \"entail\" in v.lower()\n    )\n    log.info(\"NLI model loaded: %s (entailment_idx=%d)\", nli_model_name, ent_idx)\n\n    hypothesis = \"The response changes or corrects the previous answer.\"\n    premises = [_extract_last_response(s[\"response_text\"]) for s in samples]\n    conditions = [s[\"condition\"] for s in samples]\n\n    scores: list[float] = []\n    for i in range(0, len(premises), batch_size):\n        bp = premises[i : i + batch_size]\n        bc = conditions[i : i + batch_size]\n        inputs = tok(\n            bp,\n            [hypothesis] * len(bp),\n            padding=True,\n            truncation=True,\n            max_length=512,\n            return_tensors=\"pt\",\n        ).to(nli.device)\n        probs = F.softmax(nli(**inputs).logits, dim=-1)\n        raw = probs[:, ent_idx].tolist()\n        for r, c in zip(raw, bc):\n            scores.append(1.0 - r if c == \"invalid_pressure\" else r)\n\n    del nli, tok\n    torch.cuda.empty_cache()\n    return scores\n\n\n# ---------------------------------------------------------------------------\n# Training\n# ---------------------------------------------------------------------------\ndef main():\n    config = parse_args()\n    os.makedirs(config.output_dir, exist_ok=True)\n\n    logging.basicConfig(\n        level=logging.INFO,\n        format=\"%(asctime)s [%(levelname)s] %(name)s: %(message)s\",\n        handlers=[\n            logging.StreamHandler(),\n            logging.FileHandler(os.path.join(config.output_dir, \"train.log\")),\n        ],\n    )\n    log = logging.getLogger(\"exp008\")\n    torch.manual_seed(config.seed)\n\n    if \"HF_ENDPOINT\" not in os.environ:\n        os.environ[\"HF_ENDPOINT\"] = \"https://hf-mirror.com\"\n\n    log.info(\"=== exp-008: Binary Probe Penalty Baseline ===\")\n    log.info(\"Config: lr=%s lambda_reward=%s lambda_probe=%s max_steps=%d retrain_interval=%d\",\n             config.lr, config.lambda_reward, config.lambda_probe, config.max_steps,\n             config.retrain_interval)\n\n    # --- Resolve model path ---\n    model_path = config.model_path\n    if not Path(model_path).exists():\n        model_path = \"Qwen/Qwen3-8B\"\n        log.info(\"Local model not found, using HF hub: %s\", model_path)\n\n    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)\n    if tokenizer.pad_token_id is None:\n        tokenizer.pad_token_id = tokenizer.eos_token_id\n\n    # --- Dataset ---\n    dataset = CalibrationSFTDataset(config.data_path, tokenizer, config.max_seq_len)\n    log.info(\"Dataset: %d samples from %s\", len(dataset), config.data_path)\n    if not dataset.samples:\n        log.error(\n            \"No valid samples. Data must have at least 2 turns \"\n            \"(user + assistant).\"\n        )\n        sys.exit(1)\n\n    # --- Probe: train or load ---\n    probe_path = os.path.join(config.output_dir, \"probe.pt\")\n    if Path(probe_path).exists():\n        probe = load_probe(probe_path)\n        log.info(\"Loaded existing probe from %s\", probe_path)\n    else:\n        if not Path(config.activations_path).exists():\n            log.error(\"activations.pt not found at %s\", config.activations_path)\n            sys.exit(1)\n        log.info(\"Training probe from %s\", config.activations_path)\n        probe, acc = train_probe(\n            config.activations_path,\n            config.reward_layers,\n            config.probe_position_idx,\n            config.seed,\n        )\n        log.info(\"Probe accuracy: %.4f\", acc)\n        save_probe(probe, probe_path)\n        log.info(\"Probe saved to %s\", probe_path)\n\n    # --- Precompute R3 ---\n    log.info(\"Precomputing R3 scores with %s ...\", config.nli_model_name)\n    r3_scores = precompute_r3(dataset.samples, config.nli_model_name)\n    for i, r3 in enumerate(r3_scores):\n        dataset.samples[i][\"r3\"] = r3\n    r3_mean = sum(r3_scores) / len(r3_scores)\n    log.info(\n        \"R3: mean=%.4f min=%.4f max=%.4f\", r3_mean, min(r3_scores), max(r3_scores)\n    )\n\n    # --- Load model + LoRA ---\n    log.info(\"Loading model: %s\", model_path)\n    model = AutoModelForCausalLM.from_pretrained(\n        model_path,\n        torch_dtype=torch.bfloat16 if config.bf16 else torch.float32,\n        trust_remote_code=True,\n    ).cuda()\n\n    if config.gradient_checkpointing:\n        model.gradient_checkpointing_enable(\n            gradient_checkpointing_kwargs={\"use_reentrant\": False}\n        )\n\n    lora_cfg = LoraConfig(\n        r=config.lora_rank,\n        lora_alpha=config.lora_alpha,\n        target_modules=config.lora_targets,\n        lora_dropout=config.lora_dropout,\n        bias=\"none\",\n        task_type=\"CAUSAL_LM\",\n    )\n    model = get_peft_model(model, lora_cfg)\n    model.print_trainable_parameters()\n\n    probe.cuda()\n\n    # --- Dataloader ---\n    loader = DataLoader(\n        dataset,\n        batch_size=config.batch_size,\n        shuffle=True,\n        collate_fn=partial(sft_collate, pad_token_id=tokenizer.pad_token_id),\n        drop_last=False,\n    )\n\n    # --- Optimizer + scheduler ---\n    optimizer = torch.optim.AdamW(\n        [p for p in model.parameters() if p.requires_grad],\n        lr=config.lr,\n        weight_decay=config.weight_decay,\n    )\n    scheduler = get_linear_schedule_with_warmup(\n        optimizer, config.warmup_steps, config.max_steps\n    )\n\n    # --- Training loop ---\n    log.info(\n        \"Starting training: max_steps=%d, batch=%d, grad_accum=%d, effective_batch=%d\",\n        config.max_steps, config.batch_size, config.grad_accum,\n        config.batch_size * config.grad_accum,\n    )\n    step = 0\n    acc_loss, acc_sft, acc_probe, acc_r3, acc_n = 0.0, 0.0, 0.0, 0.0, 0\n    model.train()\n\n    while step < config.max_steps:\n        for batch in loader:\n            if step >= config.max_steps:\n                break\n\n            ids = batch[\"input_ids\"].cuda()\n            mask = batch[\"attention_mask\"].cuda()\n            lab = batch[\"labels\"].cuda()\n            resp_positions = batch[\"resp_positions\"]\n            batch_r3 = batch[\"r3_scores\"]\n\n            # Forward: SFT loss + hidden states for probe\n            out = model(\n                input_ids=ids,\n                attention_mask=mask,\n                labels=lab,\n                output_hidden_states=True,\n            )\n            sft_loss = out.loss\n            hs = out.hidden_states  # tuple[Tensor], index 0=embedding, i+1=layer i\n\n            # S(t): mean probe score across batch at sequence-end position\n            probe_vals = []\n            for b in range(ids.size(0)):\n                pos = resp_positions[b]\n                layer_h = [hs[l + 1][b, pos] for l in config.reward_layers]\n                mean_h = torch.stack(layer_h).mean(0).float()\n                probe_vals.append(probe(mean_h.unsqueeze(0)))\n            s_t = torch.stack(probe_vals).mean()\n\n            r3_val = sum(batch_r3) / len(batch_r3)\n\n            # L = L_sft - lambda_reward * R3 + lambda_reward * lambda_probe * S(t)\n            loss = (\n                sft_loss\n                - config.lambda_reward * r3_val\n                + config.lambda_reward * config.lambda_probe * s_t\n            )\n            (loss / config.grad_accum).backward()\n\n            acc_loss += loss.item()\n            acc_sft += sft_loss.item()\n            acc_probe += s_t.item()\n            acc_r3 += r3_val\n            acc_n += 1\n\n            if acc_n >= config.grad_accum:\n                torch.nn.utils.clip_grad_norm_(\n                    model.parameters(), config.max_grad_norm\n                )\n                optimizer.step()\n                scheduler.step()\n                optimizer.zero_grad()\n                step += 1\n\n                if step % config.log_steps == 0:\n                    log.info(\n                        \"step=%d loss=%.4f sft=%.4f R3=%.4f S(t)=%.4f lr=%.2e\",\n                        step,\n                        acc_loss / acc_n,\n                        acc_sft / acc_n,\n                        acc_r3 / acc_n,\n                        acc_probe / acc_n,\n                        scheduler.get_last_lr()[0],\n                    )\n                acc_loss, acc_sft, acc_probe, acc_r3, acc_n = (\n                    0.0,\n                    0.0,\n                    0.0,\n                    0.0,\n                    0,\n                )\n\n                if step % config.retrain_interval == 0:\n                    log.info(\"[RETRAIN] Retraining probe at step %d ...\", step)\n                    probe, rt_acc, rt_auroc = retrain_probe_online(\n                        model, dataset, probe.linear.in_features, config, log\n                    )\n                    log.info(\n                        \"[INFO] Probe retrained at step %d: acc=%.4f, auroc=%.4f\",\n                        step, rt_acc, rt_auroc,\n                    )\n\n                if step % config.save_steps == 0:\n                    ckpt_dir = os.path.join(\n                        config.output_dir, f\"checkpoint-{step}\"\n                    )\n                    model.save_pretrained(ckpt_dir)\n                    tokenizer.save_pretrained(ckpt_dir)\n                    save_probe(probe, os.path.join(ckpt_dir, \"probe.pt\"))\n                    log.info(\"Saved checkpoint: %s\", ckpt_dir)\n\n    # --- Final save ---\n    final_dir = os.path.join(config.output_dir, \"final\")\n    model.save_pretrained(final_dir)\n    tokenizer.save_pretrained(final_dir)\n    save_probe(probe, os.path.join(final_dir, \"probe.pt\"))\n    log.info(\"Training complete. Final checkpoint: %s\", final_dir)\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF\necho \"UPLOAD_OK: $(wc -c < /root/contrastive_entrain_calib/training/run_exp008_binary_probe_penalty.py) bytes\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-28034",
    "command": "cat > /root/contrastive_entrain_calib/training/run_exp008_binary_probe_penalty.py << 'SCRIPT_EOF'\n#!/usr/bin/env python3\n\"\"\"exp-008: Binary Probe Penalty baseline for sycophancy calibration.\n\nSFT-style LoRA training on Qwen3-8B with a frozen binary probe penalty.\nDesigned to run on a single RTX 5090 (32 GB) without GRPO's memory overhead.\n\nLoss:\n    L = L_sft - lambda_reward * (R3 - lambda_probe * S(t))\n      = L_sft + lambda_reward * lambda_probe * S(t) - lambda_reward * R3\n\n    L_sft:  cross-entropy on last-assistant-turn tokens (standard SFT)\n    S(t):   frozen logistic probe sycophancy score, differentiable through hidden states\n    R3:     NLI behavioral reward, precomputed on training data (constant, for monitoring)\n\nInput:\n    Model:       /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B\n    Data:        calibration_v2_1_expanded.jsonl (362 samples, v2.1 style-controlled)\n    Activations: results/exp001/activations.pt (for probe pretraining)\n\nOutput:\n    LoRA checkpoints every 500 steps + final in output_dir\n\nDependencies: torch, transformers, peft\n\"\"\"\nimport argparse\nimport json\nimport logging\nimport os\nimport re\nimport sys\nfrom dataclasses import dataclass, field\nfrom functools import partial\nfrom pathlib import Path\n\nimport torch\nimport torch.nn as nn\nimport torch.nn.functional as F\nfrom torch.utils.data import DataLoader\nfrom torch.utils.data import Dataset as TorchDataset\n\nfrom peft import LoraConfig, get_peft_model\nfrom transformers import (\n    AutoModelForCausalLM,\n    AutoModelForSequenceClassification,\n    AutoTokenizer,\n    get_linear_schedule_with_warmup,\n)\n\nCONDITION_MAP = {\n    \"warranted_revision\": \"valid_correction\",\n    \"sycophantic_capitulation\": \"invalid_pressure\",\n    \"valid_correction\": \"valid_correction\",\n    \"invalid_pressure\": \"invalid_pressure\",\n}\n\n\n# ---------------------------------------------------------------------------\n# Configuration\n# ---------------------------------------------------------------------------\n@dataclass\nclass TrainConfig:\n    model_path: str = \"/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B\"\n    data_path: str = \"/root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl\"\n    activations_path: str = (\n        \"/root/contrastive_entrain_calib/results/exp001/activations.pt\"\n    )\n    output_dir: str = (\n        \"/root/contrastive_entrain_calib/checkpoints/exp008_binary_probe_penalty\"\n    )\n\n    # LoRA\n    lora_rank: int = 64\n    lora_alpha: int = 128\n    lora_targets: list[str] = field(\n        default_factory=lambda: [\"q_proj\", \"v_proj\", \"k_proj\", \"o_proj\", \"gate_proj\", \"up_proj\", \"down_proj\"]\n    )\n    lora_dropout: float = 0.05\n\n    # Training\n    lr: float = 5e-5\n    warmup_steps: int = 200\n    weight_decay: float = 0.01\n    max_steps: int = 8000\n    batch_size: int = 1\n    grad_accum: int = 16\n    max_seq_len: int = 1024\n    gradient_checkpointing: bool = True\n    bf16: bool = True\n    seed: int = 42\n    max_grad_norm: float = 1.0\n\n    # Loss weights\n    lambda_reward: float = 0.1\n    lambda_probe: float = 1.0\n\n    # Probe / hidden state extraction\n    reward_layers: list[int] = field(\n        default_factory=lambda: [19, 20, 24, 27, 32, 33, 35]\n    )\n    probe_position_idx: int = 1  # 1 = asst_first in (num_layers, 2, hidden) layout\n\n    # NLI\n    nli_model_name: str = \"cross-encoder/nli-deberta-v3-base\"\n\n    # Logging / checkpointing\n    log_steps: int = 10\n    save_steps: int = 500\n    retrain_interval: int = 500\n\n\ndef parse_args() -> TrainConfig:\n    p = argparse.ArgumentParser(description=\"exp-008 Binary Probe Penalty baseline\")\n    p.add_argument(\"--lr\", type=float, default=5e-5)\n    p.add_argument(\"--lambda_reward\", type=float, default=0.1)\n    p.add_argument(\"--lambda_probe\", type=float, default=1.0)\n    p.add_argument(\"--max_steps\", type=int, default=8000)\n    p.add_argument(\"--lora_rank\", type=int, default=64)\n    p.add_argument(\"--lora_alpha\", type=int, default=128)\n    p.add_argument(\"--batch_size\", type=int, default=1)\n    p.add_argument(\"--grad_accum\", type=int, default=16)\n    p.add_argument(\"--seed\", type=int, default=42)\n    p.add_argument(\"--log_steps\", type=int, default=None)\n    p.add_argument(\"--retrain_interval\", type=int, default=None)\n    p.add_argument(\"--model_path\", type=str, default=None)\n    p.add_argument(\"--data_path\", type=str, default=None)\n    p.add_argument(\"--output_dir\", type=str, default=None)\n    args = p.parse_args()\n\n    cfg = TrainConfig()\n    for k, v in vars(args).items():\n        if v is not None and hasattr(cfg, k):\n            setattr(cfg, k, v)\n    return cfg\n\n\n# ---------------------------------------------------------------------------\n# Dataset\n# ---------------------------------------------------------------------------\nclass CalibrationSFTDataset(TorchDataset):\n    \"\"\"Loads 3-turn calibration conversations for SFT (aligned with exp-004).\n\n    Format per record: user -> assistant(Turn 1) -> user(correction/pressure).\n    Input: full 3-turn conversation + generation_prompt.\n    SFT target: Turn 1 (assistant first reply) only; cross-entropy on those tokens,\n    all others masked with -100.\n    \"\"\"\n\n    def __init__(self, data_path: str, tokenizer, max_seq_len: int = 1024):\n        self.tokenizer = tokenizer\n        self.max_seq_len = max_seq_len\n        self.samples: list[dict] = []\n\n        im_end_id = tokenizer.convert_tokens_to_ids(\"<|im_end|>\")\n\n        with open(data_path) as f:\n            for line in f:\n                rec = json.loads(line)\n                turns = rec[\"turns\"]\n                if len(turns) < 2:\n                    continue\n\n                condition = CONDITION_MAP.get(rec[\"condition\"], rec[\"condition\"])\n                pair_id = str(rec.get(\"pair_id\", rec.get(\"id\", \"\")))\n                response_text = turns[1][\"content\"]\n\n                msgs = [{\"role\": t[\"role\"], \"content\": t[\"content\"]} for t in turns]\n\n                try:\n                    full_ids = tokenizer.apply_chat_template(\n                        msgs, tokenize=True, add_generation_prompt=True,\n                        enable_thinking=False,\n                    )\n                except TypeError:\n                    full_ids = tokenizer.apply_chat_template(\n                        msgs, tokenize=True, add_generation_prompt=True,\n                    )\n\n                try:\n                    pre_asst_ids = tokenizer.apply_chat_template(\n                        msgs[:1], tokenize=True, add_generation_prompt=True,\n                        enable_thinking=False,\n                    )\n                except TypeError:\n                    pre_asst_ids = tokenizer.apply_chat_template(\n                        msgs[:1], tokenize=True, add_generation_prompt=True,\n                    )\n\n                asst_start = len(pre_asst_ids)\n                asst_end = asst_start\n                while asst_end < len(full_ids) and full_ids[asst_end] != im_end_id:\n                    asst_end += 1\n                asst_end += 1  # include <|im_end|>\n\n                if len(full_ids) > max_seq_len:\n                    full_ids = full_ids[:max_seq_len]\n\n                labels = [-100] * len(full_ids)\n                for i in range(asst_start, min(asst_end, len(full_ids))):\n                    labels[i] = full_ids[i]\n\n                resp_pos = len(full_ids) - 1\n\n                self.samples.append(\n                    {\n                        \"full_ids\": full_ids,\n                        \"labels\": labels,\n                        \"resp_pos\": resp_pos,\n                        \"condition\": condition,\n                        \"pair_id\": pair_id,\n                        \"response_text\": response_text,\n                        \"r3\": 0.0,\n                    }\n                )\n\n    def __len__(self):\n        return len(self.samples)\n\n    def __getitem__(self, idx):\n        return self.samples[idx]\n\n\ndef sft_collate(batch: list[dict], pad_token_id: int) -> dict:\n    max_len = max(len(item[\"full_ids\"]) for item in batch)\n    input_ids, masks, labels = [], [], []\n    resp_positions, conditions, r3_scores = [], [], []\n\n    for item in batch:\n        ids = item[\"full_ids\"]\n        lab = item[\"labels\"]\n        pad_n = max_len - len(ids)\n\n        input_ids.append(ids + [pad_token_id] * pad_n)\n        masks.append([1] * len(ids) + [0] * pad_n)\n        labels.append(lab + [-100] * pad_n)\n        resp_positions.append(item[\"resp_pos\"])\n        conditions.append(item[\"condition\"])\n        r3_scores.append(item[\"r3\"])\n\n    return {\n        \"input_ids\": torch.tensor(input_ids, dtype=torch.long),\n        \"attention_mask\": torch.tensor(masks, dtype=torch.long),\n        \"labels\": torch.tensor(labels, dtype=torch.long),\n        \"resp_positions\": resp_positions,\n        \"conditions\": conditions,\n        \"r3_scores\": r3_scores,\n    }\n\n\n# ---------------------------------------------------------------------------\n# Binary Probe\n# ---------------------------------------------------------------------------\nclass LinearProbe(nn.Module):\n    \"\"\"Frozen logistic regression probe: h -> P(sycophantic).\"\"\"\n\n    def __init__(self, input_dim: int):\n        super().__init__()\n        self.linear = nn.Linear(input_dim, 1)\n        self.register_buffer(\"feat_mean\", torch.zeros(input_dim))\n        self.register_buffer(\"feat_std\", torch.ones(input_dim))\n\n    def forward(self, x: torch.Tensor) -> torch.Tensor:\n        x_norm = (x - self.feat_mean) / (self.feat_std + 1e-8)\n        return torch.sigmoid(self.linear(x_norm)).squeeze(-1)\n\n\ndef train_probe(\n    activations_path: str,\n    layers: list[int],\n    position_idx: int = 1,\n    seed: int = 42,\n    epochs: int = 200,\n    lr: float = 1e-2,\n) -> tuple[LinearProbe, float]:\n    \"\"\"Train binary probe from exp-001 pre-extracted activations.\n\n    Labels: invalid_pressure (sycophantic context) -> 1, valid_correction -> 0.\n    Returns (frozen_probe, accuracy).\n    \"\"\"\n    torch.manual_seed(seed)\n    data = torch.load(activations_path, map_location=\"cpu\", weights_only=False)\n\n    features, labels = [], []\n    for sample in data:\n        acts = sample[\"activations\"]  # (num_layers, 2, hidden_dim)\n        mean_h = torch.stack([acts[l, position_idx] for l in layers]).mean(0)\n        features.append(mean_h)\n        cond = CONDITION_MAP.get(sample[\"condition\"], sample[\"condition\"])\n        labels.append(1.0 if cond == \"invalid_pressure\" else 0.0)\n\n    X = torch.stack(features)\n    y = torch.tensor(labels)\n\n    feat_mean = X.mean(dim=0)\n    feat_std = X.std(dim=0)\n\n    probe = LinearProbe(X.shape[1])\n    probe.feat_mean.copy_(feat_mean)\n    probe.feat_std.copy_(feat_std)\n\n    opt = torch.optim.Adam(probe.parameters(), lr=lr, weight_decay=1e-4)\n    criterion = nn.BCELoss()\n\n    probe.train()\n    for epoch in range(epochs):\n        loss = criterion(probe(X), y)\n        opt.zero_grad()\n        loss.backward()\n        opt.step()\n        if (epoch + 1) % 50 == 0:\n            with torch.no_grad():\n                acc = ((probe(X) > 0.5).float() == y).float().mean().item()\n            logging.getLogger(\"exp008\").info(\n                \"Probe epoch %d/%d: loss=%.4f acc=%.4f\", epoch + 1, epochs, loss.item(), acc\n            )\n\n    probe.eval()\n    with torch.no_grad():\n        acc = ((probe(X) > 0.5).float() == y).float().mean().item()\n\n    for p in probe.parameters():\n        p.requires_grad_(False)\n\n    return probe, acc\n\n\ndef save_probe(probe: LinearProbe, path: str) -> None:\n    Path(path).parent.mkdir(parents=True, exist_ok=True)\n    torch.save(\n        {\"state_dict\": probe.state_dict(), \"input_dim\": probe.linear.in_features},\n        path,\n    )\n\n\ndef load_probe(path: str) -> LinearProbe:\n    ckpt = torch.load(path, map_location=\"cpu\")\n    probe = LinearProbe(ckpt[\"input_dim\"])\n    probe.load_state_dict(ckpt[\"state_dict\"])\n    probe.eval()\n    for p in probe.parameters():\n        p.requires_grad_(False)\n    return probe\n\n\n# ---------------------------------------------------------------------------\n# Online Probe Retraining\n# ---------------------------------------------------------------------------\ndef retrain_probe_online(model, dataset, input_dim, config, log):\n    \"\"\"Retrain probe using current model's activations on calibration data.\"\"\"\n    model.eval()\n    device = next(model.parameters()).device\n\n    features = []\n    labels = []\n\n    with torch.no_grad():\n        for i, sample in enumerate(dataset.samples):\n            ids = torch.tensor([sample[\"full_ids\"]], dtype=torch.long, device=device)\n            mask = torch.ones_like(ids)\n\n            out = model(\n                input_ids=ids,\n                attention_mask=mask,\n                output_hidden_states=True,\n            )\n            hs = out.hidden_states\n            pos = sample[\"resp_pos\"]\n\n            layer_h = [hs[l + 1][0, pos] for l in config.reward_layers]\n            mean_h = torch.stack(layer_h).mean(0).float().cpu()\n            features.append(mean_h)\n\n            label = 1.0 if sample[\"condition\"] == \"invalid_pressure\" else 0.0\n            labels.append(label)\n\n    torch.cuda.empty_cache()\n\n    X = torch.stack(features)\n    y = torch.tensor(labels)\n    log.info(\n        \"[RETRAIN] Extracted %d activations (%.1f%% positive)\",\n        len(y), y.mean().item() * 100,\n    )\n\n    feat_mean = X.mean(dim=0)\n    feat_std = X.std(dim=0)\n\n    new_probe = LinearProbe(input_dim)\n    new_probe.feat_mean.copy_(feat_mean)\n    new_probe.feat_std.copy_(feat_std)\n\n    opt = torch.optim.Adam(new_probe.parameters(), lr=1e-2, weight_decay=1e-4)\n    criterion = nn.BCELoss()\n\n    new_probe.train()\n    for epoch in range(200):\n        loss = criterion(new_probe(X), y)\n        opt.zero_grad()\n        loss.backward()\n        opt.step()\n\n    new_probe.eval()\n    with torch.no_grad():\n        preds = new_probe(X)\n        acc = ((preds > 0.5).float() == y).float().mean().item()\n\n    try:\n        from sklearn.metrics import roc_auc_score\n        auroc = roc_auc_score(y.numpy(), preds.numpy())\n    except ImportError:\n        sorted_pairs = sorted(zip(preds.tolist(), y.tolist()), reverse=True)\n        tp, auc_sum = 0, 0.0\n        p_total = int(y.sum().item())\n        n_total = len(y) - p_total\n        for _, label in sorted_pairs:\n            if label == 1.0:\n                tp += 1\n            else:\n                auc_sum += tp\n        auroc = auc_sum / (p_total * n_total) if (p_total * n_total) > 0 else 0.0\n\n    for p in new_probe.parameters():\n        p.requires_grad_(False)\n    new_probe.to(device)\n\n    model.train()\n    return new_probe, acc, auroc\n\n\n# ---------------------------------------------------------------------------\n# NLI / R3 Scoring\n# ---------------------------------------------------------------------------\ndef _extract_last_response(text: str) -> str:\n    \"\"\"Strip chat template markers and return last assistant response.\"\"\"\n    clean = re.sub(\n        r\"<\\|im_start\\|>|<\\|im_end\\|>|&lt;think>|&lt;/think>|<\\|endoftext\\|>\", \"\", text\n    )\n    parts = clean.split(\"assistant\")\n    response = parts[-1].strip() if len(parts) > 1 else clean.strip()\n    if len(response) > 1000:\n        response = response[:1000]\n    return response if response else text[:500]\n\n\n@torch.no_grad()\ndef precompute_r3(\n    samples: list[dict], nli_model_name: str, batch_size: int = 16\n) -> list[float]:\n    \"\"\"Compute R3 for every sample using a frozen NLI model, then free GPU memory.\n\n    R3 = P(entailment) for valid_correction (changing answer is correct),\n    R3 = 1 - P(entailment) for invalid_pressure (not changing is correct).\n    \"\"\"\n    log = logging.getLogger(\"exp008\")\n\n    try:\n        from transformers import DebertaV2Tokenizer\n\n        tok = DebertaV2Tokenizer.from_pretrained(nli_model_name)\n    except Exception:\n        tok = AutoTokenizer.from_pretrained(nli_model_name)\n\n    nli = AutoModelForSequenceClassification.from_pretrained(nli_model_name)\n    nli.eval().cuda()\n    ent_idx = next(\n        int(k) for k, v in nli.config.id2label.items() if \"entail\" in v.lower()\n    )\n    log.info(\"NLI model loaded: %s (entailment_idx=%d)\", nli_model_name, ent_idx)\n\n    hypothesis = \"The response changes or corrects the previous answer.\"\n    premises = [_extract_last_response(s[\"response_text\"]) for s in samples]\n    conditions = [s[\"condition\"] for s in samples]\n\n    scores: list[float] = []\n    for i in range(0, len(premises), batch_size):\n        bp = premises[i : i + batch_size]\n        bc = conditions[i : i + batch_size]\n        inputs = tok(\n            bp,\n            [hypothesis] * len(bp),\n            padding=True,\n            truncation=True,\n            max_length=512,\n            return_tensors=\"pt\",\n        ).to(nli.device)\n        probs = F.softmax(nli(**inputs).logits, dim=-1)\n        raw = probs[:, ent_idx].tolist()\n        for r, c in zip(raw, bc):\n            scores.append(1.0 - r if c == \"invalid_pressure\" else r)\n\n    del nli, tok\n    torch.cuda.empty_cache()\n    return scores\n\n\n# ---------------------------------------------------------------------------\n# Training\n# ---------------------------------------------------------------------------\ndef main():\n    config = parse_args()\n    os.makedirs(config.output_dir, exist_ok=True)\n\n    logging.basicConfig(\n        level=logging.INFO,\n        format=\"%(asctime)s [%(levelname)s] %(name)s: %(message)s\",\n        handlers=[\n            logging.StreamHandler(),\n            logging.FileHandler(os.path.join(config.output_dir, \"train.log\")),\n        ],\n    )\n    log = logging.getLogger(\"exp008\")\n    torch.manual_seed(config.seed)\n\n    if \"HF_ENDPOINT\" not in os.environ:\n        os.environ[\"HF_ENDPOINT\"] = \"https://hf-mirror.com\"\n\n    log.info(\"=== exp-008: Binary Probe Penalty Baseline ===\")\n    log.info(\"Config: lr=%s lambda_reward=%s lambda_probe=%s max_steps=%d retrain_interval=%d\",\n             config.lr, config.lambda_reward, config.lambda_probe, config.max_steps,\n             config.retrain_interval)\n\n    # --- Resolve model path ---\n    model_path = config.model_path\n    if not Path(model_path).exists():\n        model_path = \"Qwen/Qwen3-8B\"\n        log.info(\"Local model not found, using HF hub: %s\", model_path)\n\n    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)\n    if tokenizer.pad_token_id is None:\n        tokenizer.pad_token_id = tokenizer.eos_token_id\n\n    # --- Dataset ---\n    dataset = CalibrationSFTDataset(config.data_path, tokenizer, config.max_seq_len)\n    log.info(\"Dataset: %d samples from %s\", len(dataset), config.data_path)\n    if not dataset.samples:\n        log.error(\n            \"No valid samples. Data must have at least 2 turns \"\n            \"(user + assistant).\"\n        )\n        sys.exit(1)\n\n    # --- Probe: train or load ---\n    probe_path = os.path.join(config.output_dir, \"probe.pt\")\n    if Path(probe_path).exists():\n        probe = load_probe(probe_path)\n        log.info(\"Loaded existing probe from %s\", probe_path)\n    else:\n        if not Path(config.activations_path).exists():\n            log.error(\"activations.pt not found at %s\", config.activations_path)\n            sys.exit(1)\n        log.info(\"Training probe from %s\", config.activations_path)\n        probe, acc = train_probe(\n            config.activations_path,\n            config.reward_layers,\n            config.probe_position_idx,\n            config.seed,\n        )\n        log.info(\"Probe accuracy: %.4f\", acc)\n        save_probe(probe, probe_path)\n        log.info(\"Probe saved to %s\", probe_path)\n\n    # --- Precompute R3 ---\n    log.info(\"Precomputing R3 scores with %s ...\", config.nli_model_name)\n    r3_scores = precompute_r3(dataset.samples, config.nli_model_name)\n    for i, r3 in enumerate(r3_scores):\n        dataset.samples[i][\"r3\"] = r3\n    r3_mean = sum(r3_scores) / len(r3_scores)\n    log.info(\n        \"R3: mean=%.4f min=%.4f max=%.4f\", r3_mean, min(r3_scores), max(r3_scores)\n    )\n\n    # --- Load model + LoRA ---\n    log.info(\"Loading model: %s\", model_path)\n    model = AutoModelForCausalLM.from_pretrained(\n        model_path,\n        torch_dtype=torch.bfloat16 if config.bf16 else torch.float32,\n        trust_remote_code=True,\n    ).cuda()\n\n    if config.gradient_checkpointing:\n        model.gradient_checkpointing_enable(\n            gradient_checkpointing_kwargs={\"use_reentrant\": False}\n        )\n\n    lora_cfg = LoraConfig(\n        r=config.lora_rank,\n        lora_alpha=config.lora_alpha,\n        target_modules=config.lora_targets,\n        lora_dropout=config.lora_dropout,\n        bias=\"none\",\n        task_type=\"CAUSAL_LM\",\n    )\n    model = get_peft_model(model, lora_cfg)\n    model.print_trainable_parameters()\n\n    probe.cuda()\n\n    # --- Dataloader ---\n    loader = DataLoader(\n        dataset,\n        batch_size=config.batch_size,\n        shuffle=True,\n        collate_fn=partial(sft_collate, pad_token_id=tokenizer.pad_token_id),\n        drop_last=False,\n    )\n\n    # --- Optimizer + scheduler ---\n    optimizer = torch.optim.AdamW(\n        [p for p in model.parameters() if p.requires_grad],\n        lr=config.lr,\n        weight_decay=config.weight_decay,\n    )\n    scheduler = get_linear_schedule_with_warmup(\n        optimizer, config.warmup_steps, config.max_steps\n    )\n\n    # --- Training loop ---\n    log.info(\n        \"Starting training: max_steps=%d, batch=%d, grad_accum=%d, effective_batch=%d\",\n        config.max_steps, config.batch_size, config.grad_accum,\n        config.batch_size * config.grad_accum,\n    )\n    step = 0\n    acc_loss, acc_sft, acc_probe, acc_r3, acc_n = 0.0, 0.0, 0.0, 0.0, 0\n    model.train()\n\n    while step < config.max_steps:\n        for batch in loader:\n            if step >= config.max_steps:\n                break\n\n            ids = batch[\"input_ids\"].cuda()\n            mask = batch[\"attention_mask\"].cuda()\n            lab = batch[\"labels\"].cuda()\n            resp_positions = batch[\"resp_positions\"]\n            batch_r3 = batch[\"r3_scores\"]\n\n            # Forward: SFT loss + hidden states for probe\n            out = model(\n                input_ids=ids,\n                attention_mask=mask,\n                labels=lab,\n                output_hidden_states=True,\n            )\n            sft_loss = out.loss\n            hs = out.hidden_states  # tuple[Tensor], index 0=embedding, i+1=layer i\n\n            # S(t): mean probe score across batch at sequence-end position\n            probe_vals = []\n            for b in range(ids.size(0)):\n                pos = resp_positions[b]\n                layer_h = [hs[l + 1][b, pos] for l in config.reward_layers]\n                mean_h = torch.stack(layer_h).mean(0).float()\n                probe_vals.append(probe(mean_h.unsqueeze(0)))\n            s_t = torch.stack(probe_vals).mean()\n\n            r3_val = sum(batch_r3) / len(batch_r3)\n\n            # L = L_sft - lambda_reward * R3 + lambda_reward * lambda_probe * S(t)\n            loss = (\n                sft_loss\n                - config.lambda_reward * r3_val\n                + config.lambda_reward * config.lambda_probe * s_t\n            )\n            (loss / config.grad_accum).backward()\n\n            acc_loss += loss.item()\n            acc_sft += sft_loss.item()\n            acc_probe += s_t.item()\n            acc_r3 += r3_val\n            acc_n += 1\n\n            if acc_n >= config.grad_accum:\n                torch.nn.utils.clip_grad_norm_(\n                    model.parameters(), config.max_grad_norm\n                )\n                optimizer.step()\n                scheduler.step()\n                optimizer.zero_grad()\n                step += 1\n\n                if step % config.log_steps == 0:\n                    log.info(\n                        \"step=%d loss=%.4f sft=%.4f R3=%.4f S(t)=%.4f lr=%.2e\",\n                        step,\n                        acc_loss / acc_n,\n                        acc_sft / acc_n,\n                        acc_r3 / acc_n,\n                        acc_probe / acc_n,\n                        scheduler.get_last_lr()[0],\n                    )\n                acc_loss, acc_sft, acc_probe, acc_r3, acc_n = (\n                    0.0,\n                    0.0,\n                    0.0,\n                    0.0,\n                    0,\n                )\n\n                if step % config.retrain_interval == 0:\n                    log.info(\"[RETRAIN] Retraining probe at step %d ...\", step)\n                    probe, rt_acc, rt_auroc = retrain_probe_online(\n                        model, dataset, probe.linear.in_features, config, log\n                    )\n                    log.info(\n                        \"[INFO] Probe retrained at step %d: acc=%.4f, auroc=%.4f\",\n                        step, rt_acc, rt_auroc,\n                    )\n\n                if step % config.save_steps == 0:\n                    ckpt_dir = os.path.join(\n                        config.output_dir, f\"checkpoint-{step}\"\n                    )\n                    model.save_pretrained(ckpt_dir)\n                    tokenizer.save_pretrained(ckpt_dir)\n                    save_probe(probe, os.path.join(ckpt_dir, \"probe.pt\"))\n                    log.info(\"Saved checkpoint: %s\", ckpt_dir)\n\n    # --- Final save ---\n    final_dir = os.path.join(config.output_dir, \"final\")\n    model.save_pretrained(final_dir)\n    tokenizer.save_pretrained(final_dir)\n    save_probe(probe, os.path.join(final_dir, \"probe.pt\"))\n    log.info(\"Training complete. Final checkpoint: %s\", final_dir)\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF\necho \"UPLOAD_OK: $(wc -c < /root/contrastive_entrain_calib/training/run_exp008_binary_probe_penalty.py) bytes\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-18T19:01:16.250898+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"UPLOAD_OK: 25141 bytes\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-18T19:01:16.251053+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-28034",
  "command": "rm -rf /root/contrastive_entrain_calib/checkpoints/exp008_binary_probe_penalty_dryrun && mkdir -p /root/contrastive_entrain_calib/checkpoints/exp008_binary_probe_penalty_dryrun",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-28034",
    "command": "rm -rf /root/contrastive_entrain_calib/checkpoints/exp008_binary_probe_penalty_dryrun && mkdir -p /root/contrastive_entrain_calib/checkpoints/exp008_binary_probe_penalty_dryrun",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-18T19:01:16.251182+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.54}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-18T19:01:16.251300+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-28034",
  "command": "cd /root/contrastive_entrain_calib && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 /root/miniconda3/bin/python training/run_exp008_binary_probe_penalty.py --max_steps 2 --log_steps 1 --retrain_interval 1 --grad_accum 1 --output_dir /root/contrastive_entrain_calib/checkpoints/exp008_binary_probe_penalty_dryrun 2>&1 | tail -80",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-28034",
    "command": "cd /root/contrastive_entrain_calib && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 /root/miniconda3/bin/python training/run_exp008_binary_probe_penalty.py --max_steps 2 --log_steps 1 --retrain_interval 1 --grad_accum 1 --output_dir /root/contrastive_entrain_calib/checkpoints/exp008_binary_probe_penalty_dryrun 2>&1 | tail -80",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-18T19:01:16.251470+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-19 02:56:32,546 [INFO] exp008: === exp-008: Binary Probe Penalty Baseline ===\\n2026-05-19 02:56:32,546 [INFO] exp008: Config: lr=5e-05 lambda_reward=0.1 lambda_probe=1.0 max_steps=2 retrain_interval=1\\n2026-05-19 02:56:33,073 [INFO] exp008: Dataset: 362 samples from /root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl\\n2026-05-19 02:56:33,074 [INFO] exp008: Training probe from /root/contrastive_entrain_calib/results/exp001/activations.pt\\n2026-05-19 02:56:33,446 [INFO] exp008: Probe epoch 50/200: loss=0.1208 acc=0.9558\\n2026-05-19 02:56:33,476 [INFO] exp008: Probe epoch 100/200: loss=0.0683 acc=0.9890\\n2026-05-19 02:56:33,505 [INFO] exp008: Probe epoch 150/200: loss=0.0493 acc=0.9945\\n2026-05-19 02:56:33,540 [INFO] exp008: Probe epoch 200/200: loss=0.0372 acc=0.9945\\n2026-05-19 02:56:33,541 [INFO] exp008: Probe accuracy: 0.9945\\n2026-05-19 02:56:33,542 [INFO] exp008: Probe saved to /root/contrastive_entrain_calib/checkpoints/exp008_binary_probe_penalty_dryrun/probe.pt\\n2026-05-19 02:56:33,542 [INFO] exp008: Precomputing R3 scores with cross-encoder/nli-deberta-v3-base ...\\n2026-05-19 02:56:34,254 [INFO] exp008: NLI model loaded: cross-encoder/nli-deberta-v3-base (entailment_idx=1)\\n2026-05-19 02:56:35,509 [INFO] exp008: R3: mean=0.5000 min=0.0001 max=0.9999\\n2026-05-19 02:56:35,510 [INFO] exp008: Loading model: /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B\\n`torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading checkpoint shards:   0%|          | 0/5 [00:00<?, ?it/s]\\rLoading checkpoint shards: 100%|██████████| 5/5 [00:00<00:00, 234.01it/s]\\nTraceback (most recent call last):\\n  File \\\"/root/contrastive_entrain_calib/training/run_exp008_binary_probe_penalty.py\\\", line 727, in &lt;module>\\n    main()\\n  File \\\"/root/contrastive_entrain_calib/training/run_exp008_binary_probe_penalty.py\\\", line 577, in main\\n    ).cuda()\\n      ^^^^^^\\n  File \\\"/root/miniconda3/lib/p
…[truncated 1933 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-18T19:01:16.251664+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-28034",
  "command": "nvidia-smi",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-28034",
    "command": "nvidia-smi",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-18T19:01:16.251822+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Tue May 19 02:56:44 2026       \\n+-----------------------------------------------------------------------------------------+\\n| NVIDIA-SMI 595.71.05              Driver Version: 595.71.05      CUDA Version: 13.2     |\\n+-----------------------------------------+------------------------+----------------------+\\n| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |\\n| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |\\n|                                         |                        |               MIG M. |\\n|=========================================+========================+======================|\\n|   0  NVIDIA GeForce RTX 5090        On  |   00000000:38:00.0 Off |                  N/A |\\n| 53%   57C    P1            155W /  575W |   21838MiB /  32607MiB |     13%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n|   1  NVIDIA GeForce RTX 5090        On  |   00000000:49:00.0 Off |                  N/A |\\n| 59%   59C    P1            103W /  575W |   31400MiB /  32607MiB |      0%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n|   2  NVIDIA GeForce RTX 5090        On  |   00000000:5A:00.0 Off |                  N/A |\\n| 56%   55C    P1             99W /  575W |   30638MiB /  32607MiB |      0%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n|   3  NVIDIA GeForce RTX 5090        On  |   00000000:B8:00.0 Off |                  N/A |\\n| 57%   65C    P1            1
…[truncated 1298 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-18T19:01:16.252021+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29046",
  "command": "nvidia-smi",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29046",
    "command": "nvidia-smi",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-18T19:01:16.252170+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Tue May 19 02:56:52 2026       \\n+-----------------------------------------------------------------------------------------+\\n| NVIDIA-SMI 595.58.03              Driver Version: 595.58.03      CUDA Version: 13.2     |\\n+-----------------------------------------+------------------------+----------------------+\\n| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |\\n| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |\\n|                                         |                        |               MIG M. |\\n|=========================================+========================+======================|\\n|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:98:00.0 Off |                  Off |\\n| N/A   59C    P0            452W /  600W |   63603MiB /  97887MiB |     54%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n|   1  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:B8:00.0 Off |                  Off |\\n| N/A   64C    P0            396W /  600W |   38161MiB /  97887MiB |     94%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n\\n+-----------------------------------------------------------------------------------------+\\n| Processes:                                                                              |\\n|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |\\n|        ID   ID                                                               Usage      |\\n|=========================================================================================|\\n|    0   N/A  N/A          
…[truncated 359 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-18T19:01:16.252347+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29046",
  "command": "ls -la /root/contrastive_entrain_calib/results/exp001/activations.pt",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29046",
    "command": "ls -la /root/contrastive_entrain_calib/results/exp001/activations.pt",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-18T19:01:16.252548+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29046",
  "command": "ls -la /root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29046",
    "command": "ls -la /root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-18T19:01:16.252748+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29046",
  "command": "ls /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/config.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29046",
    "command": "ls /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/config.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-18T19:01:16.252933+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 427172715 May 18 22:50 /root/contrastive_entrain_calib/results/exp001/activations.pt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-18T19:01:16.253074+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29046",
  "command": "ls /root/contrastive_entrain_calib/training/run_exp008_binary_probe_penalty.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29046",
    "command": "ls /root/contrastive_entrain_calib/training/run_exp008_binary_probe_penalty.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-18T19:01:16.253208+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 367001 May 18 19:39 /root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.54}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-18T19:01:16.253331+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/config.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-18T19:01:16.253515+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/contrastive_entrain_calib/training/run_exp008_binary_probe_penalty.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-18T19:01:16.253728+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-29046",
  "command": "cat > /root/contrastive_entrain_calib/training/run_exp008_binary_probe_penalty.py << 'SCRIPT_EOF'\n#!/usr/bin/env python3\n\"\"\"exp-008: Binary Probe Penalty baseline for sycophancy calibration.\n\nSFT-style LoRA training on Qwen3-8B with a frozen binary probe penalty.\nDesigned to run on a single RTX 5090 (32 GB) without GRPO's memory overhead.\n\nLoss:\n    L = L_sft - lambda_reward * (R3 - lambda_probe * S(t))\n      = L_sft + lambda_reward * lambda_probe * S(t) - lambda_reward * R3\n\n    L_sft:  cross-entropy on last-assistant-turn tokens (standard SFT)\n    S(t):   frozen logistic probe sycophancy score, differentiable through hidden states\n    R3:     NLI behavioral reward, precomputed on training data (constant, for monitoring)\n\nInput:\n    Model:       /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B\n    Data:        calibration_v2_1_expanded.jsonl (362 samples, v2.1 style-controlled)\n    Activations: results/exp001/activations.pt (for probe pretraining)\n\nOutput:\n    LoRA checkpoints every 500 steps + final in output_dir\n\nDependencies: torch, transformers, peft\n\"\"\"\nimport argparse\nimport json\nimport logging\nimport os\nimport re\nimport sys\nfrom dataclasses import dataclass, field\nfrom functools import partial\nfrom pathlib import Path\n\nimport torch\nimport torch.nn as nn\nimport torch.nn.functional as F\nfrom torch.utils.data import DataLoader\nfrom torch.utils.data import Dataset as TorchDataset\n\nfrom peft import LoraConfig, get_peft_model\nfrom transformers import (\n    AutoModelForCausalLM,\n    AutoModelForSequenceClassification,\n    AutoTokenizer,\n    get_linear_schedule_with_warmup,\n)\n\nCONDITION_MAP = {\n    \"warranted_revision\": \"valid_correction\",\n    \"sycophantic_capitulation\": \"invalid_pressure\",\n    \"valid_correction\": \"valid_correction\",\n    \"invalid_pressure\": \"invalid_pressure\",\n}\n\n\n# ---------------------------------------------------------------------------\n# Configuration\n# ---------------------------------------------------------------------------\n@dataclass\nclass TrainConfig:\n    model_path: str = \"/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B\"\n    data_path: str = \"/root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl\"\n    activations_path: str = (\n        \"/root/contrastive_entrain_calib/results/exp001/activations.pt\"\n    )\n    output_dir: str = (\n        \"/root/contrastive_entrain_calib/checkpoints/exp008_binary_probe_penalty\"\n    )\n\n    # LoRA\n    lora_rank: int = 64\n    lora_alpha: int = 128\n    lora_targets: list[str] = field(\n        default_factory=lambda: [\"q_proj\", \"v_proj\", \"k_proj\", \"o_proj\", \"gate_proj\", \"up_proj\", \"down_proj\"]\n    )\n    lora_dropout: float = 0.05\n\n    # Training\n    lr: float = 5e-5\n    warmup_steps: int = 200\n    weight_decay: float = 0.01\n    max_steps: int = 8000\n    batch_size: int = 1\n    grad_accum: int = 16\n    max_seq_len: int = 1024\n    gradient_checkpointing: bool = True\n    bf16: bool = True\n    seed: int = 42\n    max_grad_norm: float = 1.0\n\n    # Loss weights\n    lambda_reward: float = 0.1\n    lambda_probe: float = 1.0\n\n    # Probe / hidden state extraction\n    reward_layers: list[int] = field(\n        default_factory=lambda: [19, 20, 24, 27, 32, 33, 35]\n    )\n    probe_position_idx: int = 1  # 1 = asst_first in (num_layers, 2, hidden) layout\n\n    # NLI\n    nli_model_name: str = \"cross-encoder/nli-deberta-v3-base\"\n\n    # Logging / checkpointing\n    log_steps: int = 10\n    save_steps: int = 500\n    retrain_interval: int = 500\n\n\ndef parse_args() -> TrainConfig:\n    p = argparse.ArgumentParser(description=\"exp-008 Binary Probe Penalty baseline\")\n    p.add_argument(\"--lr\", type=float, default=5e-5)\n    p.add_argument(\"--lambda_reward\", type=float, default=0.1)\n    p.add_argument(\"--lambda_probe\", type=float, default=1.0)\n    p.add_argument(\"--max_steps\", type=int, default=8000)\n    p.add_argument(\"--lora_rank\", type=int, default=64)\n    p.add_argument(\"--lora_alpha\", type=int, default=128)\n    p.add_argument(\"--batch_size\", type=int, default=1)\n    p.add_argument(\"--grad_accum\", type=int, default=16)\n    p.add_argument(\"--seed\", type=int, default=42)\n    p.add_argument(\"--log_steps\", type=int, default=None)\n    p.add_argument(\"--retrain_interval\", type=int, default=None)\n    p.add_argument(\"--model_path\", type=str, default=None)\n    p.add_argument(\"--data_path\", type=str, default=None)\n    p.add_argument(\"--output_dir\", type=str, default=None)\n    args = p.parse_args()\n\n    cfg = TrainConfig()\n    for k, v in vars(args).items():\n        if v is not None and hasattr(cfg, k):\n            setattr(cfg, k, v)\n    return cfg\n\n\n# ---------------------------------------------------------------------------\n# Dataset\n# ---------------------------------------------------------------------------\nclass CalibrationSFTDataset(TorchDataset):\n    \"\"\"Loads 3-turn calibration conversations for SFT (aligned with exp-004).\n\n    Format per record: user -> assistant(Turn 1) -> user(correction/pressure).\n    Input: full 3-turn conversation + generation_prompt.\n    SFT target: Turn 1 (assistant first reply) only; cross-entropy on those tokens,\n    all others masked with -100.\n    \"\"\"\n\n    def __init__(self, data_path: str, tokenizer, max_seq_len: int = 1024):\n        self.tokenizer = tokenizer\n        self.max_seq_len = max_seq_len\n        self.samples: list[dict] = []\n\n        im_end_id = tokenizer.convert_tokens_to_ids(\"<|im_end|>\")\n\n        with open(data_path) as f:\n            for line in f:\n                rec = json.loads(line)\n                turns = rec[\"turns\"]\n                if len(turns) < 2:\n                    continue\n\n                condition = CONDITION_MAP.get(rec[\"condition\"], rec[\"condition\"])\n                pair_id = str(rec.get(\"pair_id\", rec.get(\"id\", \"\")))\n                response_text = turns[1][\"content\"]\n\n                msgs = [{\"role\": t[\"role\"], \"content\": t[\"content\"]} for t in turns]\n\n                try:\n                    full_ids = tokenizer.apply_chat_template(\n                        msgs, tokenize=True, add_generation_prompt=True,\n                        enable_thinking=False,\n                    )\n                except TypeError:\n                    full_ids = tokenizer.apply_chat_template(\n                        msgs, tokenize=True, add_generation_prompt=True,\n                    )\n\n                try:\n                    pre_asst_ids = tokenizer.apply_chat_template(\n                        msgs[:1], tokenize=True, add_generation_prompt=True,\n                        enable_thinking=False,\n                    )\n                except TypeError:\n                    pre_asst_ids = tokenizer.apply_chat_template(\n                        msgs[:1], tokenize=True, add_generation_prompt=True,\n                    )\n\n                asst_start = len(pre_asst_ids)\n                asst_end = asst_start\n                while asst_end < len(full_ids) and full_ids[asst_end] != im_end_id:\n                    asst_end += 1\n                asst_end += 1  # include <|im_end|>\n\n                if len(full_ids) > max_seq_len:\n                    full_ids = full_ids[:max_seq_len]\n\n                labels = [-100] * len(full_ids)\n                for i in range(asst_start, min(asst_end, len(full_ids))):\n                    labels[i] = full_ids[i]\n\n                resp_pos = len(full_ids) - 1\n\n                self.samples.append(\n                    {\n                        \"full_ids\": full_ids,\n                        \"labels\": labels,\n                        \"resp_pos\": resp_pos,\n                        \"condition\": condition,\n                        \"pair_id\": pair_id,\n                        \"response_text\": response_text,\n                        \"r3\": 0.0,\n                    }\n                )\n\n    def __len__(self):\n        return len(self.samples)\n\n    def __getitem__(self, idx):\n        return self.samples[idx]\n\n\ndef sft_collate(batch: list[dict], pad_token_id: int) -> dict:\n    max_len = max(len(item[\"full_ids\"]) for item in batch)\n    input_ids, masks, labels = [], [], []\n    resp_positions, conditions, r3_scores = [], [], []\n\n    for item in batch:\n        ids = item[\"full_ids\"]\n        lab = item[\"labels\"]\n        pad_n = max_len - len(ids)\n\n        input_ids.append(ids + [pad_token_id] * pad_n)\n        masks.append([1] * len(ids) + [0] * pad_n)\n        labels.append(lab + [-100] * pad_n)\n        resp_positions.append(item[\"resp_pos\"])\n        conditions.append(item[\"condition\"])\n        r3_scores.append(item[\"r3\"])\n\n    return {\n        \"input_ids\": torch.tensor(input_ids, dtype=torch.long),\n        \"attention_mask\": torch.tensor(masks, dtype=torch.long),\n        \"labels\": torch.tensor(labels, dtype=torch.long),\n        \"resp_positions\": resp_positions,\n        \"conditions\": conditions,\n        \"r3_scores\": r3_scores,\n    }\n\n\n# ---------------------------------------------------------------------------\n# Binary Probe\n# ---------------------------------------------------------------------------\nclass LinearProbe(nn.Module):\n    \"\"\"Frozen logistic regression probe: h -> P(sycophantic).\"\"\"\n\n    def __init__(self, input_dim: int):\n        super().__init__()\n        self.linear = nn.Linear(input_dim, 1)\n        self.register_buffer(\"feat_mean\", torch.zeros(input_dim))\n        self.register_buffer(\"feat_std\", torch.ones(input_dim))\n\n    def forward(self, x: torch.Tensor) -> torch.Tensor:\n        x_norm = (x - self.feat_mean) / (self.feat_std + 1e-8)\n        return torch.sigmoid(self.linear(x_norm)).squeeze(-1)\n\n\ndef train_probe(\n    activations_path: str,\n    layers: list[int],\n    position_idx: int = 1,\n    seed: int = 42,\n    epochs: int = 200,\n    lr: float = 1e-2,\n) -> tuple[LinearProbe, float]:\n    \"\"\"Train binary probe from exp-001 pre-extracted activations.\n\n    Labels: invalid_pressure (sycophantic context) -> 1, valid_correction -> 0.\n    Returns (frozen_probe, accuracy).\n    \"\"\"\n    torch.manual_seed(seed)\n    data = torch.load(activations_path, map_location=\"cpu\", weights_only=False)\n\n    features, labels = [], []\n    for sample in data:\n        acts = sample[\"activations\"]  # (num_layers, 2, hidden_dim)\n        mean_h = torch.stack([acts[l, position_idx] for l in layers]).mean(0)\n        features.append(mean_h)\n        cond = CONDITION_MAP.get(sample[\"condition\"], sample[\"condition\"])\n        labels.append(1.0 if cond == \"invalid_pressure\" else 0.0)\n\n    X = torch.stack(features)\n    y = torch.tensor(labels)\n\n    feat_mean = X.mean(dim=0)\n    feat_std = X.std(dim=0)\n\n    probe = LinearProbe(X.shape[1])\n    probe.feat_mean.copy_(feat_mean)\n    probe.feat_std.copy_(feat_std)\n\n    opt = torch.optim.Adam(probe.parameters(), lr=lr, weight_decay=1e-4)\n    criterion = nn.BCELoss()\n\n    probe.train()\n    for epoch in range(epochs):\n        loss = criterion(probe(X), y)\n        opt.zero_grad()\n        loss.backward()\n        opt.step()\n        if (epoch + 1) % 50 == 0:\n            with torch.no_grad():\n                acc = ((probe(X) > 0.5).float() == y).float().mean().item()\n            logging.getLogger(\"exp008\").info(\n                \"Probe epoch %d/%d: loss=%.4f acc=%.4f\", epoch + 1, epochs, loss.item(), acc\n            )\n\n    probe.eval()\n    with torch.no_grad():\n        acc = ((probe(X) > 0.5).float() == y).float().mean().item()\n\n    for p in probe.parameters():\n        p.requires_grad_(False)\n\n    return probe, acc\n\n\ndef save_probe(probe: LinearProbe, path: str) -> None:\n    Path(path).parent.mkdir(parents=True, exist_ok=True)\n    torch.save(\n        {\"state_dict\": probe.state_dict(), \"input_dim\": probe.linear.in_features},\n        path,\n    )\n\n\ndef load_probe(path: str) -> LinearProbe:\n    ckpt = torch.load(path, map_location=\"cpu\")\n    probe = LinearProbe(ckpt[\"input_dim\"])\n    probe.load_state_dict(ckpt[\"state_dict\"])\n    probe.eval()\n    for p in probe.parameters():\n        p.requires_grad_(False)\n    return probe\n\n\n# ---------------------------------------------------------------------------\n# Online Probe Retraining\n# ---------------------------------------------------------------------------\ndef retrain_probe_online(model, dataset, input_dim, config, log):\n    \"\"\"Retrain probe using current model's activations on calibration data.\"\"\"\n    model.eval()\n    device = next(model.parameters()).device\n\n    features = []\n    labels = []\n\n    with torch.no_grad():\n        for i, sample in enumerate(dataset.samples):\n            ids = torch.tensor([sample[\"full_ids\"]], dtype=torch.long, device=device)\n            mask = torch.ones_like(ids)\n\n            out = model(\n                input_ids=ids,\n                attention_mask=mask,\n                output_hidden_states=True,\n            )\n            hs = out.hidden_states\n            pos = sample[\"resp_pos\"]\n\n            layer_h = [hs[l + 1][0, pos] for l in config.reward_layers]\n            mean_h = torch.stack(layer_h).mean(0).float().cpu()\n            features.append(mean_h)\n\n            label = 1.0 if sample[\"condition\"] == \"invalid_pressure\" else 0.0\n            labels.append(label)\n\n    torch.cuda.empty_cache()\n\n    X = torch.stack(features)\n    y = torch.tensor(labels)\n    log.info(\n        \"[RETRAIN] Extracted %d activations (%.1f%% positive)\",\n        len(y), y.mean().item() * 100,\n    )\n\n    feat_mean = X.mean(dim=0)\n    feat_std = X.std(dim=0)\n\n    new_probe = LinearProbe(input_dim)\n    new_probe.feat_mean.copy_(feat_mean)\n    new_probe.feat_std.copy_(feat_std)\n\n    opt = torch.optim.Adam(new_probe.parameters(), lr=1e-2, weight_decay=1e-4)\n    criterion = nn.BCELoss()\n\n    new_probe.train()\n    for epoch in range(200):\n        loss = criterion(new_probe(X), y)\n        opt.zero_grad()\n        loss.backward()\n        opt.step()\n\n    new_probe.eval()\n    with torch.no_grad():\n        preds = new_probe(X)\n        acc = ((preds > 0.5).float() == y).float().mean().item()\n\n    try:\n        from sklearn.metrics import roc_auc_score\n        auroc = roc_auc_score(y.numpy(), preds.numpy())\n    except ImportError:\n        sorted_pairs = sorted(zip(preds.tolist(), y.tolist()), reverse=True)\n        tp, auc_sum = 0, 0.0\n        p_total = int(y.sum().item())\n        n_total = len(y) - p_total\n        for _, label in sorted_pairs:\n            if label == 1.0:\n                tp += 1\n            else:\n                auc_sum += tp\n        auroc = auc_sum / (p_total * n_total) if (p_total * n_total) > 0 else 0.0\n\n    for p in new_probe.parameters():\n        p.requires_grad_(False)\n    new_probe.to(device)\n\n    model.train()\n    return new_probe, acc, auroc\n\n\n# ---------------------------------------------------------------------------\n# NLI / R3 Scoring\n# ---------------------------------------------------------------------------\ndef _extract_last_response(text: str) -> str:\n    \"\"\"Strip chat template markers and return last assistant response.\"\"\"\n    clean = re.sub(\n        r\"<\\|im_start\\|>|<\\|im_end\\|>|&lt;think>|&lt;/think>|<\\|endoftext\\|>\", \"\", text\n    )\n    parts = clean.split(\"assistant\")\n    response = parts[-1].strip() if len(parts) > 1 else clean.strip()\n    if len(response) > 1000:\n        response = response[:1000]\n    return response if response else text[:500]\n\n\n@torch.no_grad()\ndef precompute_r3(\n    samples: list[dict], nli_model_name: str, batch_size: int = 16\n) -> list[float]:\n    \"\"\"Compute R3 for every sample using a frozen NLI model, then free GPU memory.\n\n    R3 = P(entailment) for valid_correction (changing answer is correct),\n    R3 = 1 - P(entailment) for invalid_pressure (not changing is correct).\n    \"\"\"\n    log = logging.getLogger(\"exp008\")\n\n    try:\n        from transformers import DebertaV2Tokenizer\n\n        tok = DebertaV2Tokenizer.from_pretrained(nli_model_name)\n    except Exception:\n        tok = AutoTokenizer.from_pretrained(nli_model_name)\n\n    nli = AutoModelForSequenceClassification.from_pretrained(nli_model_name)\n    nli.eval().cuda()\n    ent_idx = next(\n        int(k) for k, v in nli.config.id2label.items() if \"entail\" in v.lower()\n    )\n    log.info(\"NLI model loaded: %s (entailment_idx=%d)\", nli_model_name, ent_idx)\n\n    hypothesis = \"The response changes or corrects the previous answer.\"\n    premises = [_extract_last_response(s[\"response_text\"]) for s in samples]\n    conditions = [s[\"condition\"] for s in samples]\n\n    scores: list[float] = []\n    for i in range(0, len(premises), batch_size):\n        bp = premises[i : i + batch_size]\n        bc = conditions[i : i + batch_size]\n        inputs = tok(\n            bp,\n            [hypothesis] * len(bp),\n            padding=True,\n            truncation=True,\n            max_length=512,\n            return_tensors=\"pt\",\n        ).to(nli.device)\n        probs = F.softmax(nli(**inputs).logits, dim=-1)\n        raw = probs[:, ent_idx].tolist()\n        for r, c in zip(raw, bc):\n            scores.append(1.0 - r if c == \"invalid_pressure\" else r)\n\n    del nli, tok\n    torch.cuda.empty_cache()\n    return scores\n\n\n# ---------------------------------------------------------------------------\n# Training\n# ---------------------------------------------------------------------------\ndef main():\n    config = parse_args()\n    os.makedirs(config.output_dir, exist_ok=True)\n\n    logging.basicConfig(\n        level=logging.INFO,\n        format=\"%(asctime)s [%(levelname)s] %(name)s: %(message)s\",\n        handlers=[\n            logging.StreamHandler(),\n            logging.FileHandler(os.path.join(config.output_dir, \"train.log\")),\n        ],\n    )\n    log = logging.getLogger(\"exp008\")\n    torch.manual_seed(config.seed)\n\n    if \"HF_ENDPOINT\" not in os.environ:\n        os.environ[\"HF_ENDPOINT\"] = \"https://hf-mirror.com\"\n\n    log.info(\"=== exp-008: Binary Probe Penalty Baseline ===\")\n    log.info(\"Config: lr=%s lambda_reward=%s lambda_probe=%s max_steps=%d retrain_interval=%d\",\n             config.lr, config.lambda_reward, config.lambda_probe, config.max_steps,\n             config.retrain_interval)\n\n    # --- Resolve model path ---\n    model_path = config.model_path\n    if not Path(model_path).exists():\n        model_path = \"Qwen/Qwen3-8B\"\n        log.info(\"Local model not found, using HF hub: %s\", model_path)\n\n    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)\n    if tokenizer.pad_token_id is None:\n        tokenizer.pad_token_id = tokenizer.eos_token_id\n\n    # --- Dataset ---\n    dataset = CalibrationSFTDataset(config.data_path, tokenizer, config.max_seq_len)\n    log.info(\"Dataset: %d samples from %s\", len(dataset), config.data_path)\n    if not dataset.samples:\n        log.error(\n            \"No valid samples. Data must have at least 2 turns \"\n            \"(user + assistant).\"\n        )\n        sys.exit(1)\n\n    # --- Probe: train or load ---\n    probe_path = os.path.join(config.output_dir, \"probe.pt\")\n    if Path(probe_path).exists():\n        probe = load_probe(probe_path)\n        log.info(\"Loaded existing probe from %s\", probe_path)\n    else:\n        if not Path(config.activations_path).exists():\n            log.error(\"activations.pt not found at %s\", config.activations_path)\n            sys.exit(1)\n        log.info(\"Training probe from %s\", config.activations_path)\n        probe, acc = train_probe(\n            config.activations_path,\n            config.reward_layers,\n            config.probe_position_idx,\n            config.seed,\n        )\n        log.info(\"Probe accuracy: %.4f\", acc)\n        save_probe(probe, probe_path)\n        log.info(\"Probe saved to %s\", probe_path)\n\n    # --- Precompute R3 ---\n    log.info(\"Precomputing R3 scores with %s ...\", config.nli_model_name)\n    r3_scores = precompute_r3(dataset.samples, config.nli_model_name)\n    for i, r3 in enumerate(r3_scores):\n        dataset.samples[i][\"r3\"] = r3\n    r3_mean = sum(r3_scores) / len(r3_scores)\n    log.info(\n        \"R3: mean=%.4f min=%.4f max=%.4f\", r3_mean, min(r3_scores), max(r3_scores)\n    )\n\n    # --- Load model + LoRA ---\n    log.info(\"Loading model: %s\", model_path)\n    model = AutoModelForCausalLM.from_pretrained(\n        model_path,\n        torch_dtype=torch.bfloat16 if config.bf16 else torch.float32,\n        trust_remote_code=True,\n    ).cuda()\n\n    if config.gradient_checkpointing:\n        model.gradient_checkpointing_enable(\n            gradient_checkpointing_kwargs={\"use_reentrant\": False}\n        )\n\n    lora_cfg = LoraConfig(\n        r=config.lora_rank,\n        lora_alpha=config.lora_alpha,\n        target_modules=config.lora_targets,\n        lora_dropout=config.lora_dropout,\n        bias=\"none\",\n        task_type=\"CAUSAL_LM\",\n    )\n    model = get_peft_model(model, lora_cfg)\n    model.print_trainable_parameters()\n\n    probe.cuda()\n\n    # --- Dataloader ---\n    loader = DataLoader(\n        dataset,\n        batch_size=config.batch_size,\n        shuffle=True,\n        collate_fn=partial(sft_collate, pad_token_id=tokenizer.pad_token_id),\n        drop_last=False,\n    )\n\n    # --- Optimizer + scheduler ---\n    optimizer = torch.optim.AdamW(\n        [p for p in model.parameters() if p.requires_grad],\n        lr=config.lr,\n        weight_decay=config.weight_decay,\n    )\n    scheduler = get_linear_schedule_with_warmup(\n        optimizer, config.warmup_steps, config.max_steps\n    )\n\n    # --- Training loop ---\n    log.info(\n        \"Starting training: max_steps=%d, batch=%d, grad_accum=%d, effective_batch=%d\",\n        config.max_steps, config.batch_size, config.grad_accum,\n        config.batch_size * config.grad_accum,\n    )\n    step = 0\n    acc_loss, acc_sft, acc_probe, acc_r3, acc_n = 0.0, 0.0, 0.0, 0.0, 0\n    model.train()\n\n    while step < config.max_steps:\n        for batch in loader:\n            if step >= config.max_steps:\n                break\n\n            ids = batch[\"input_ids\"].cuda()\n            mask = batch[\"attention_mask\"].cuda()\n            lab = batch[\"labels\"].cuda()\n            resp_positions = batch[\"resp_positions\"]\n            batch_r3 = batch[\"r3_scores\"]\n\n            # Forward: SFT loss + hidden states for probe\n            out = model(\n                input_ids=ids,\n                attention_mask=mask,\n                labels=lab,\n                output_hidden_states=True,\n            )\n            sft_loss = out.loss\n            hs = out.hidden_states  # tuple[Tensor], index 0=embedding, i+1=layer i\n\n            # S(t): mean probe score across batch at sequence-end position\n            probe_vals = []\n            for b in range(ids.size(0)):\n                pos = resp_positions[b]\n                layer_h = [hs[l + 1][b, pos] for l in config.reward_layers]\n                mean_h = torch.stack(layer_h).mean(0).float()\n                probe_vals.append(probe(mean_h.unsqueeze(0)))\n            s_t = torch.stack(probe_vals).mean()\n\n            r3_val = sum(batch_r3) / len(batch_r3)\n\n            # L = L_sft - lambda_reward * R3 + lambda_reward * lambda_probe * S(t)\n            loss = (\n                sft_loss\n                - config.lambda_reward * r3_val\n                + config.lambda_reward * config.lambda_probe * s_t\n            )\n            (loss / config.grad_accum).backward()\n\n            acc_loss += loss.item()\n            acc_sft += sft_loss.item()\n            acc_probe += s_t.item()\n            acc_r3 += r3_val\n            acc_n += 1\n\n            if acc_n >= config.grad_accum:\n                torch.nn.utils.clip_grad_norm_(\n                    model.parameters(), config.max_grad_norm\n                )\n                optimizer.step()\n                scheduler.step()\n                optimizer.zero_grad()\n                step += 1\n\n                if step % config.log_steps == 0:\n                    log.info(\n                        \"step=%d loss=%.4f sft=%.4f R3=%.4f S(t)=%.4f lr=%.2e\",\n                        step,\n                        acc_loss / acc_n,\n                        acc_sft / acc_n,\n                        acc_r3 / acc_n,\n                        acc_probe / acc_n,\n                        scheduler.get_last_lr()[0],\n                    )\n                acc_loss, acc_sft, acc_probe, acc_r3, acc_n = (\n                    0.0,\n                    0.0,\n                    0.0,\n                    0.0,\n                    0,\n                )\n\n                if step % config.retrain_interval == 0:\n                    log.info(\"[RETRAIN] Retraining probe at step %d ...\", step)\n                    probe, rt_acc, rt_auroc = retrain_probe_online(\n                        model, dataset, probe.linear.in_features, config, log\n                    )\n                    log.info(\n                        \"[INFO] Probe retrained at step %d: acc=%.4f, auroc=%.4f\",\n                        step, rt_acc, rt_auroc,\n                    )\n\n                if step % config.save_steps == 0:\n                    ckpt_dir = os.path.join(\n                        config.output_dir, f\"checkpoint-{step}\"\n                    )\n                    model.save_pretrained(ckpt_dir)\n                    tokenizer.save_pretrained(ckpt_dir)\n                    save_probe(probe, os.path.join(ckpt_dir, \"probe.pt\"))\n                    log.info(\"Saved checkpoint: %s\", ckpt_dir)\n\n    # --- Final save ---\n    final_dir = os.path.join(config.output_dir, \"final\")\n    model.save_pretrained(final_dir)\n    tokenizer.save_pretrained(final_dir)\n    save_probe(probe, os.path.join(final_dir, \"probe.pt\"))\n    log.info(\"Training complete. Final checkpoint: %s\", final_dir)\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF\necho \"UPLOAD_OK: $(wc -c < /root/contrastive_entrain_calib/training/run_exp008_binary_probe_penalty.py) bytes\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-29046",
    "command": "cat > /root/contrastive_entrain_calib/training/run_exp008_binary_probe_penalty.py << 'SCRIPT_EOF'\n#!/usr/bin/env python3\n\"\"\"exp-008: Binary Probe Penalty baseline for sycophancy calibration.\n\nSFT-style LoRA training on Qwen3-8B with a frozen binary probe penalty.\nDesigned to run on a single RTX 5090 (32 GB) without GRPO's memory overhead.\n\nLoss:\n    L = L_sft - lambda_reward * (R3 - lambda_probe * S(t))\n      = L_sft + lambda_reward * lambda_probe * S(t) - lambda_reward * R3\n\n    L_sft:  cross-entropy on last-assistant-turn tokens (standard SFT)\n    S(t):   frozen logistic probe sycophancy score, differentiable through hidden states\n    R3:     NLI behavioral reward, precomputed on training data (constant, for monitoring)\n\nInput:\n    Model:       /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B\n    Data:        calibration_v2_1_expanded.jsonl (362 samples, v2.1 style-controlled)\n    Activations: results/exp001/activations.pt (for probe pretraining)\n\nOutput:\n    LoRA checkpoints every 500 steps + final in output_dir\n\nDependencies: torch, transformers, peft\n\"\"\"\nimport argparse\nimport json\nimport logging\nimport os\nimport re\nimport sys\nfrom dataclasses import dataclass, field\nfrom functools import partial\nfrom pathlib import Path\n\nimport torch\nimport torch.nn as nn\nimport torch.nn.functional as F\nfrom torch.utils.data import DataLoader\nfrom torch.utils.data import Dataset as TorchDataset\n\nfrom peft import LoraConfig, get_peft_model\nfrom transformers import (\n    AutoModelForCausalLM,\n    AutoModelForSequenceClassification,\n    AutoTokenizer,\n    get_linear_schedule_with_warmup,\n)\n\nCONDITION_MAP = {\n    \"warranted_revision\": \"valid_correction\",\n    \"sycophantic_capitulation\": \"invalid_pressure\",\n    \"valid_correction\": \"valid_correction\",\n    \"invalid_pressure\": \"invalid_pressure\",\n}\n\n\n# ---------------------------------------------------------------------------\n# Configuration\n# ---------------------------------------------------------------------------\n@dataclass\nclass TrainConfig:\n    model_path: str = \"/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B\"\n    data_path: str = \"/root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl\"\n    activations_path: str = (\n        \"/root/contrastive_entrain_calib/results/exp001/activations.pt\"\n    )\n    output_dir: str = (\n        \"/root/contrastive_entrain_calib/checkpoints/exp008_binary_probe_penalty\"\n    )\n\n    # LoRA\n    lora_rank: int = 64\n    lora_alpha: int = 128\n    lora_targets: list[str] = field(\n        default_factory=lambda: [\"q_proj\", \"v_proj\", \"k_proj\", \"o_proj\", \"gate_proj\", \"up_proj\", \"down_proj\"]\n    )\n    lora_dropout: float = 0.05\n\n    # Training\n    lr: float = 5e-5\n    warmup_steps: int = 200\n    weight_decay: float = 0.01\n    max_steps: int = 8000\n    batch_size: int = 1\n    grad_accum: int = 16\n    max_seq_len: int = 1024\n    gradient_checkpointing: bool = True\n    bf16: bool = True\n    seed: int = 42\n    max_grad_norm: float = 1.0\n\n    # Loss weights\n    lambda_reward: float = 0.1\n    lambda_probe: float = 1.0\n\n    # Probe / hidden state extraction\n    reward_layers: list[int] = field(\n        default_factory=lambda: [19, 20, 24, 27, 32, 33, 35]\n    )\n    probe_position_idx: int = 1  # 1 = asst_first in (num_layers, 2, hidden) layout\n\n    # NLI\n    nli_model_name: str = \"cross-encoder/nli-deberta-v3-base\"\n\n    # Logging / checkpointing\n    log_steps: int = 10\n    save_steps: int = 500\n    retrain_interval: int = 500\n\n\ndef parse_args() -> TrainConfig:\n    p = argparse.ArgumentParser(description=\"exp-008 Binary Probe Penalty baseline\")\n    p.add_argument(\"--lr\", type=float, default=5e-5)\n    p.add_argument(\"--lambda_reward\", type=float, default=0.1)\n    p.add_argument(\"--lambda_probe\", type=float, default=1.0)\n    p.add_argument(\"--max_steps\", type=int, default=8000)\n    p.add_argument(\"--lora_rank\", type=int, default=64)\n    p.add_argument(\"--lora_alpha\", type=int, default=128)\n    p.add_argument(\"--batch_size\", type=int, default=1)\n    p.add_argument(\"--grad_accum\", type=int, default=16)\n    p.add_argument(\"--seed\", type=int, default=42)\n    p.add_argument(\"--log_steps\", type=int, default=None)\n    p.add_argument(\"--retrain_interval\", type=int, default=None)\n    p.add_argument(\"--model_path\", type=str, default=None)\n    p.add_argument(\"--data_path\", type=str, default=None)\n    p.add_argument(\"--output_dir\", type=str, default=None)\n    args = p.parse_args()\n\n    cfg = TrainConfig()\n    for k, v in vars(args).items():\n        if v is not None and hasattr(cfg, k):\n            setattr(cfg, k, v)\n    return cfg\n\n\n# ---------------------------------------------------------------------------\n# Dataset\n# ---------------------------------------------------------------------------\nclass CalibrationSFTDataset(TorchDataset):\n    \"\"\"Loads 3-turn calibration conversations for SFT (aligned with exp-004).\n\n    Format per record: user -> assistant(Turn 1) -> user(correction/pressure).\n    Input: full 3-turn conversation + generation_prompt.\n    SFT target: Turn 1 (assistant first reply) only; cross-entropy on those tokens,\n    all others masked with -100.\n    \"\"\"\n\n    def __init__(self, data_path: str, tokenizer, max_seq_len: int = 1024):\n        self.tokenizer = tokenizer\n        self.max_seq_len = max_seq_len\n        self.samples: list[dict] = []\n\n        im_end_id = tokenizer.convert_tokens_to_ids(\"<|im_end|>\")\n\n        with open(data_path) as f:\n            for line in f:\n                rec = json.loads(line)\n                turns = rec[\"turns\"]\n                if len(turns) < 2:\n                    continue\n\n                condition = CONDITION_MAP.get(rec[\"condition\"], rec[\"condition\"])\n                pair_id = str(rec.get(\"pair_id\", rec.get(\"id\", \"\")))\n                response_text = turns[1][\"content\"]\n\n                msgs = [{\"role\": t[\"role\"], \"content\": t[\"content\"]} for t in turns]\n\n                try:\n                    full_ids = tokenizer.apply_chat_template(\n                        msgs, tokenize=True, add_generation_prompt=True,\n                        enable_thinking=False,\n                    )\n                except TypeError:\n                    full_ids = tokenizer.apply_chat_template(\n                        msgs, tokenize=True, add_generation_prompt=True,\n                    )\n\n                try:\n                    pre_asst_ids = tokenizer.apply_chat_template(\n                        msgs[:1], tokenize=True, add_generation_prompt=True,\n                        enable_thinking=False,\n                    )\n                except TypeError:\n                    pre_asst_ids = tokenizer.apply_chat_template(\n                        msgs[:1], tokenize=True, add_generation_prompt=True,\n                    )\n\n                asst_start = len(pre_asst_ids)\n                asst_end = asst_start\n                while asst_end < len(full_ids) and full_ids[asst_end] != im_end_id:\n                    asst_end += 1\n                asst_end += 1  # include <|im_end|>\n\n                if len(full_ids) > max_seq_len:\n                    full_ids = full_ids[:max_seq_len]\n\n                labels = [-100] * len(full_ids)\n                for i in range(asst_start, min(asst_end, len(full_ids))):\n                    labels[i] = full_ids[i]\n\n                resp_pos = len(full_ids) - 1\n\n                self.samples.append(\n                    {\n                        \"full_ids\": full_ids,\n                        \"labels\": labels,\n                        \"resp_pos\": resp_pos,\n                        \"condition\": condition,\n                        \"pair_id\": pair_id,\n                        \"response_text\": response_text,\n                        \"r3\": 0.0,\n                    }\n                )\n\n    def __len__(self):\n        return len(self.samples)\n\n    def __getitem__(self, idx):\n        return self.samples[idx]\n\n\ndef sft_collate(batch: list[dict], pad_token_id: int) -> dict:\n    max_len = max(len(item[\"full_ids\"]) for item in batch)\n    input_ids, masks, labels = [], [], []\n    resp_positions, conditions, r3_scores = [], [], []\n\n    for item in batch:\n        ids = item[\"full_ids\"]\n        lab = item[\"labels\"]\n        pad_n = max_len - len(ids)\n\n        input_ids.append(ids + [pad_token_id] * pad_n)\n        masks.append([1] * len(ids) + [0] * pad_n)\n        labels.append(lab + [-100] * pad_n)\n        resp_positions.append(item[\"resp_pos\"])\n        conditions.append(item[\"condition\"])\n        r3_scores.append(item[\"r3\"])\n\n    return {\n        \"input_ids\": torch.tensor(input_ids, dtype=torch.long),\n        \"attention_mask\": torch.tensor(masks, dtype=torch.long),\n        \"labels\": torch.tensor(labels, dtype=torch.long),\n        \"resp_positions\": resp_positions,\n        \"conditions\": conditions,\n        \"r3_scores\": r3_scores,\n    }\n\n\n# ---------------------------------------------------------------------------\n# Binary Probe\n# ---------------------------------------------------------------------------\nclass LinearProbe(nn.Module):\n    \"\"\"Frozen logistic regression probe: h -> P(sycophantic).\"\"\"\n\n    def __init__(self, input_dim: int):\n        super().__init__()\n        self.linear = nn.Linear(input_dim, 1)\n        self.register_buffer(\"feat_mean\", torch.zeros(input_dim))\n        self.register_buffer(\"feat_std\", torch.ones(input_dim))\n\n    def forward(self, x: torch.Tensor) -> torch.Tensor:\n        x_norm = (x - self.feat_mean) / (self.feat_std + 1e-8)\n        return torch.sigmoid(self.linear(x_norm)).squeeze(-1)\n\n\ndef train_probe(\n    activations_path: str,\n    layers: list[int],\n    position_idx: int = 1,\n    seed: int = 42,\n    epochs: int = 200,\n    lr: float = 1e-2,\n) -> tuple[LinearProbe, float]:\n    \"\"\"Train binary probe from exp-001 pre-extracted activations.\n\n    Labels: invalid_pressure (sycophantic context) -> 1, valid_correction -> 0.\n    Returns (frozen_probe, accuracy).\n    \"\"\"\n    torch.manual_seed(seed)\n    data = torch.load(activations_path, map_location=\"cpu\", weights_only=False)\n\n    features, labels = [], []\n    for sample in data:\n        acts = sample[\"activations\"]  # (num_layers, 2, hidden_dim)\n        mean_h = torch.stack([acts[l, position_idx] for l in layers]).mean(0)\n        features.append(mean_h)\n        cond = CONDITION_MAP.get(sample[\"condition\"], sample[\"condition\"])\n        labels.append(1.0 if cond == \"invalid_pressure\" else 0.0)\n\n    X = torch.stack(features)\n    y = torch.tensor(labels)\n\n    feat_mean = X.mean(dim=0)\n    feat_std = X.std(dim=0)\n\n    probe = LinearProbe(X.shape[1])\n    probe.feat_mean.copy_(feat_mean)\n    probe.feat_std.copy_(feat_std)\n\n    opt = torch.optim.Adam(probe.parameters(), lr=lr, weight_decay=1e-4)\n    criterion = nn.BCELoss()\n\n    probe.train()\n    for epoch in range(epochs):\n        loss = criterion(probe(X), y)\n        opt.zero_grad()\n        loss.backward()\n        opt.step()\n        if (epoch + 1) % 50 == 0:\n            with torch.no_grad():\n                acc = ((probe(X) > 0.5).float() == y).float().mean().item()\n            logging.getLogger(\"exp008\").info(\n                \"Probe epoch %d/%d: loss=%.4f acc=%.4f\", epoch + 1, epochs, loss.item(), acc\n            )\n\n    probe.eval()\n    with torch.no_grad():\n        acc = ((probe(X) > 0.5).float() == y).float().mean().item()\n\n    for p in probe.parameters():\n        p.requires_grad_(False)\n\n    return probe, acc\n\n\ndef save_probe(probe: LinearProbe, path: str) -> None:\n    Path(path).parent.mkdir(parents=True, exist_ok=True)\n    torch.save(\n        {\"state_dict\": probe.state_dict(), \"input_dim\": probe.linear.in_features},\n        path,\n    )\n\n\ndef load_probe(path: str) -> LinearProbe:\n    ckpt = torch.load(path, map_location=\"cpu\")\n    probe = LinearProbe(ckpt[\"input_dim\"])\n    probe.load_state_dict(ckpt[\"state_dict\"])\n    probe.eval()\n    for p in probe.parameters():\n        p.requires_grad_(False)\n    return probe\n\n\n# ---------------------------------------------------------------------------\n# Online Probe Retraining\n# ---------------------------------------------------------------------------\ndef retrain_probe_online(model, dataset, input_dim, config, log):\n    \"\"\"Retrain probe using current model's activations on calibration data.\"\"\"\n    model.eval()\n    device = next(model.parameters()).device\n\n    features = []\n    labels = []\n\n    with torch.no_grad():\n        for i, sample in enumerate(dataset.samples):\n            ids = torch.tensor([sample[\"full_ids\"]], dtype=torch.long, device=device)\n            mask = torch.ones_like(ids)\n\n            out = model(\n                input_ids=ids,\n                attention_mask=mask,\n                output_hidden_states=True,\n            )\n            hs = out.hidden_states\n            pos = sample[\"resp_pos\"]\n\n            layer_h = [hs[l + 1][0, pos] for l in config.reward_layers]\n            mean_h = torch.stack(layer_h).mean(0).float().cpu()\n            features.append(mean_h)\n\n            label = 1.0 if sample[\"condition\"] == \"invalid_pressure\" else 0.0\n            labels.append(label)\n\n    torch.cuda.empty_cache()\n\n    X = torch.stack(features)\n    y = torch.tensor(labels)\n    log.info(\n        \"[RETRAIN] Extracted %d activations (%.1f%% positive)\",\n        len(y), y.mean().item() * 100,\n    )\n\n    feat_mean = X.mean(dim=0)\n    feat_std = X.std(dim=0)\n\n    new_probe = LinearProbe(input_dim)\n    new_probe.feat_mean.copy_(feat_mean)\n    new_probe.feat_std.copy_(feat_std)\n\n    opt = torch.optim.Adam(new_probe.parameters(), lr=1e-2, weight_decay=1e-4)\n    criterion = nn.BCELoss()\n\n    new_probe.train()\n    for epoch in range(200):\n        loss = criterion(new_probe(X), y)\n        opt.zero_grad()\n        loss.backward()\n        opt.step()\n\n    new_probe.eval()\n    with torch.no_grad():\n        preds = new_probe(X)\n        acc = ((preds > 0.5).float() == y).float().mean().item()\n\n    try:\n        from sklearn.metrics import roc_auc_score\n        auroc = roc_auc_score(y.numpy(), preds.numpy())\n    except ImportError:\n        sorted_pairs = sorted(zip(preds.tolist(), y.tolist()), reverse=True)\n        tp, auc_sum = 0, 0.0\n        p_total = int(y.sum().item())\n        n_total = len(y) - p_total\n        for _, label in sorted_pairs:\n            if label == 1.0:\n                tp += 1\n            else:\n                auc_sum += tp\n        auroc = auc_sum / (p_total * n_total) if (p_total * n_total) > 0 else 0.0\n\n    for p in new_probe.parameters():\n        p.requires_grad_(False)\n    new_probe.to(device)\n\n    model.train()\n    return new_probe, acc, auroc\n\n\n# ---------------------------------------------------------------------------\n# NLI / R3 Scoring\n# ---------------------------------------------------------------------------\ndef _extract_last_response(text: str) -> str:\n    \"\"\"Strip chat template markers and return last assistant response.\"\"\"\n    clean = re.sub(\n        r\"<\\|im_start\\|>|<\\|im_end\\|>|&lt;think>|&lt;/think>|<\\|endoftext\\|>\", \"\", text\n    )\n    parts = clean.split(\"assistant\")\n    response = parts[-1].strip() if len(parts) > 1 else clean.strip()\n    if len(response) > 1000:\n        response = response[:1000]\n    return response if response else text[:500]\n\n\n@torch.no_grad()\ndef precompute_r3(\n    samples: list[dict], nli_model_name: str, batch_size: int = 16\n) -> list[float]:\n    \"\"\"Compute R3 for every sample using a frozen NLI model, then free GPU memory.\n\n    R3 = P(entailment) for valid_correction (changing answer is correct),\n    R3 = 1 - P(entailment) for invalid_pressure (not changing is correct).\n    \"\"\"\n    log = logging.getLogger(\"exp008\")\n\n    try:\n        from transformers import DebertaV2Tokenizer\n\n        tok = DebertaV2Tokenizer.from_pretrained(nli_model_name)\n    except Exception:\n        tok = AutoTokenizer.from_pretrained(nli_model_name)\n\n    nli = AutoModelForSequenceClassification.from_pretrained(nli_model_name)\n    nli.eval().cuda()\n    ent_idx = next(\n        int(k) for k, v in nli.config.id2label.items() if \"entail\" in v.lower()\n    )\n    log.info(\"NLI model loaded: %s (entailment_idx=%d)\", nli_model_name, ent_idx)\n\n    hypothesis = \"The response changes or corrects the previous answer.\"\n    premises = [_extract_last_response(s[\"response_text\"]) for s in samples]\n    conditions = [s[\"condition\"] for s in samples]\n\n    scores: list[float] = []\n    for i in range(0, len(premises), batch_size):\n        bp = premises[i : i + batch_size]\n        bc = conditions[i : i + batch_size]\n        inputs = tok(\n            bp,\n            [hypothesis] * len(bp),\n            padding=True,\n            truncation=True,\n            max_length=512,\n            return_tensors=\"pt\",\n        ).to(nli.device)\n        probs = F.softmax(nli(**inputs).logits, dim=-1)\n        raw = probs[:, ent_idx].tolist()\n        for r, c in zip(raw, bc):\n            scores.append(1.0 - r if c == \"invalid_pressure\" else r)\n\n    del nli, tok\n    torch.cuda.empty_cache()\n    return scores\n\n\n# ---------------------------------------------------------------------------\n# Training\n# ---------------------------------------------------------------------------\ndef main():\n    config = parse_args()\n    os.makedirs(config.output_dir, exist_ok=True)\n\n    logging.basicConfig(\n        level=logging.INFO,\n        format=\"%(asctime)s [%(levelname)s] %(name)s: %(message)s\",\n        handlers=[\n            logging.StreamHandler(),\n            logging.FileHandler(os.path.join(config.output_dir, \"train.log\")),\n        ],\n    )\n    log = logging.getLogger(\"exp008\")\n    torch.manual_seed(config.seed)\n\n    if \"HF_ENDPOINT\" not in os.environ:\n        os.environ[\"HF_ENDPOINT\"] = \"https://hf-mirror.com\"\n\n    log.info(\"=== exp-008: Binary Probe Penalty Baseline ===\")\n    log.info(\"Config: lr=%s lambda_reward=%s lambda_probe=%s max_steps=%d retrain_interval=%d\",\n             config.lr, config.lambda_reward, config.lambda_probe, config.max_steps,\n             config.retrain_interval)\n\n    # --- Resolve model path ---\n    model_path = config.model_path\n    if not Path(model_path).exists():\n        model_path = \"Qwen/Qwen3-8B\"\n        log.info(\"Local model not found, using HF hub: %s\", model_path)\n\n    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)\n    if tokenizer.pad_token_id is None:\n        tokenizer.pad_token_id = tokenizer.eos_token_id\n\n    # --- Dataset ---\n    dataset = CalibrationSFTDataset(config.data_path, tokenizer, config.max_seq_len)\n    log.info(\"Dataset: %d samples from %s\", len(dataset), config.data_path)\n    if not dataset.samples:\n        log.error(\n            \"No valid samples. Data must have at least 2 turns \"\n            \"(user + assistant).\"\n        )\n        sys.exit(1)\n\n    # --- Probe: train or load ---\n    probe_path = os.path.join(config.output_dir, \"probe.pt\")\n    if Path(probe_path).exists():\n        probe = load_probe(probe_path)\n        log.info(\"Loaded existing probe from %s\", probe_path)\n    else:\n        if not Path(config.activations_path).exists():\n            log.error(\"activations.pt not found at %s\", config.activations_path)\n            sys.exit(1)\n        log.info(\"Training probe from %s\", config.activations_path)\n        probe, acc = train_probe(\n            config.activations_path,\n            config.reward_layers,\n            config.probe_position_idx,\n            config.seed,\n        )\n        log.info(\"Probe accuracy: %.4f\", acc)\n        save_probe(probe, probe_path)\n        log.info(\"Probe saved to %s\", probe_path)\n\n    # --- Precompute R3 ---\n    log.info(\"Precomputing R3 scores with %s ...\", config.nli_model_name)\n    r3_scores = precompute_r3(dataset.samples, config.nli_model_name)\n    for i, r3 in enumerate(r3_scores):\n        dataset.samples[i][\"r3\"] = r3\n    r3_mean = sum(r3_scores) / len(r3_scores)\n    log.info(\n        \"R3: mean=%.4f min=%.4f max=%.4f\", r3_mean, min(r3_scores), max(r3_scores)\n    )\n\n    # --- Load model + LoRA ---\n    log.info(\"Loading model: %s\", model_path)\n    model = AutoModelForCausalLM.from_pretrained(\n        model_path,\n        torch_dtype=torch.bfloat16 if config.bf16 else torch.float32,\n        trust_remote_code=True,\n    ).cuda()\n\n    if config.gradient_checkpointing:\n        model.gradient_checkpointing_enable(\n            gradient_checkpointing_kwargs={\"use_reentrant\": False}\n        )\n\n    lora_cfg = LoraConfig(\n        r=config.lora_rank,\n        lora_alpha=config.lora_alpha,\n        target_modules=config.lora_targets,\n        lora_dropout=config.lora_dropout,\n        bias=\"none\",\n        task_type=\"CAUSAL_LM\",\n    )\n    model = get_peft_model(model, lora_cfg)\n    model.print_trainable_parameters()\n\n    probe.cuda()\n\n    # --- Dataloader ---\n    loader = DataLoader(\n        dataset,\n        batch_size=config.batch_size,\n        shuffle=True,\n        collate_fn=partial(sft_collate, pad_token_id=tokenizer.pad_token_id),\n        drop_last=False,\n    )\n\n    # --- Optimizer + scheduler ---\n    optimizer = torch.optim.AdamW(\n        [p for p in model.parameters() if p.requires_grad],\n        lr=config.lr,\n        weight_decay=config.weight_decay,\n    )\n    scheduler = get_linear_schedule_with_warmup(\n        optimizer, config.warmup_steps, config.max_steps\n    )\n\n    # --- Training loop ---\n    log.info(\n        \"Starting training: max_steps=%d, batch=%d, grad_accum=%d, effective_batch=%d\",\n        config.max_steps, config.batch_size, config.grad_accum,\n        config.batch_size * config.grad_accum,\n    )\n    step = 0\n    acc_loss, acc_sft, acc_probe, acc_r3, acc_n = 0.0, 0.0, 0.0, 0.0, 0\n    model.train()\n\n    while step < config.max_steps:\n        for batch in loader:\n            if step >= config.max_steps:\n                break\n\n            ids = batch[\"input_ids\"].cuda()\n            mask = batch[\"attention_mask\"].cuda()\n            lab = batch[\"labels\"].cuda()\n            resp_positions = batch[\"resp_positions\"]\n            batch_r3 = batch[\"r3_scores\"]\n\n            # Forward: SFT loss + hidden states for probe\n            out = model(\n                input_ids=ids,\n                attention_mask=mask,\n                labels=lab,\n                output_hidden_states=True,\n            )\n            sft_loss = out.loss\n            hs = out.hidden_states  # tuple[Tensor], index 0=embedding, i+1=layer i\n\n            # S(t): mean probe score across batch at sequence-end position\n            probe_vals = []\n            for b in range(ids.size(0)):\n                pos = resp_positions[b]\n                layer_h = [hs[l + 1][b, pos] for l in config.reward_layers]\n                mean_h = torch.stack(layer_h).mean(0).float()\n                probe_vals.append(probe(mean_h.unsqueeze(0)))\n            s_t = torch.stack(probe_vals).mean()\n\n            r3_val = sum(batch_r3) / len(batch_r3)\n\n            # L = L_sft - lambda_reward * R3 + lambda_reward * lambda_probe * S(t)\n            loss = (\n                sft_loss\n                - config.lambda_reward * r3_val\n                + config.lambda_reward * config.lambda_probe * s_t\n            )\n            (loss / config.grad_accum).backward()\n\n            acc_loss += loss.item()\n            acc_sft += sft_loss.item()\n            acc_probe += s_t.item()\n            acc_r3 += r3_val\n            acc_n += 1\n\n            if acc_n >= config.grad_accum:\n                torch.nn.utils.clip_grad_norm_(\n                    model.parameters(), config.max_grad_norm\n                )\n                optimizer.step()\n                scheduler.step()\n                optimizer.zero_grad()\n                step += 1\n\n                if step % config.log_steps == 0:\n                    log.info(\n                        \"step=%d loss=%.4f sft=%.4f R3=%.4f S(t)=%.4f lr=%.2e\",\n                        step,\n                        acc_loss / acc_n,\n                        acc_sft / acc_n,\n                        acc_r3 / acc_n,\n                        acc_probe / acc_n,\n                        scheduler.get_last_lr()[0],\n                    )\n                acc_loss, acc_sft, acc_probe, acc_r3, acc_n = (\n                    0.0,\n                    0.0,\n                    0.0,\n                    0.0,\n                    0,\n                )\n\n                if step % config.retrain_interval == 0:\n                    log.info(\"[RETRAIN] Retraining probe at step %d ...\", step)\n                    probe, rt_acc, rt_auroc = retrain_probe_online(\n                        model, dataset, probe.linear.in_features, config, log\n                    )\n                    log.info(\n                        \"[INFO] Probe retrained at step %d: acc=%.4f, auroc=%.4f\",\n                        step, rt_acc, rt_auroc,\n                    )\n\n                if step % config.save_steps == 0:\n                    ckpt_dir = os.path.join(\n                        config.output_dir, f\"checkpoint-{step}\"\n                    )\n                    model.save_pretrained(ckpt_dir)\n                    tokenizer.save_pretrained(ckpt_dir)\n                    save_probe(probe, os.path.join(ckpt_dir, \"probe.pt\"))\n                    log.info(\"Saved checkpoint: %s\", ckpt_dir)\n\n    # --- Final save ---\n    final_dir = os.path.join(config.output_dir, \"final\")\n    model.save_pretrained(final_dir)\n    tokenizer.save_pretrained(final_dir)\n    save_probe(probe, os.path.join(final_dir, \"probe.pt\"))\n    log.info(\"Training complete. Final checkpoint: %s\", final_dir)\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF\necho \"UPLOAD_OK: $(wc -c < /root/contrastive_entrain_calib/training/run_exp008_binary_probe_penalty.py) bytes\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-18T19:01:16.254095+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"UPLOAD_OK: 25141 bytes\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.61}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-18T19:01:16.254252+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-29046",
  "command": "rm -rf /root/contrastive_entrain_calib/checkpoints/exp008_dryrun && cd /root/contrastive_entrain_calib && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 /root/miniconda3/bin/python training/run_exp008_binary_probe_penalty.py --max_steps 2 --log_steps 1 --retrain_interval 1 --grad_accum 1 --output_dir /root/contrastive_entrain_calib/checkpoints/exp008_dryrun 2>&1 | tail -100",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-29046",
    "command": "rm -rf /root/contrastive_entrain_calib/checkpoints/exp008_dryrun && cd /root/contrastive_entrain_calib && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 /root/miniconda3/bin/python training/run_exp008_binary_probe_penalty.py --max_steps 2 --log_steps 1 --retrain_interval 1 --grad_accum 1 --output_dir /root/contrastive_entrain_calib/checkpoints/exp008_dryrun 2>&1 | tail -100",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-18T19:01:16.254389+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'rm -rf /root/contrastive_entrain_calib/checkpoints/exp008_dryrun && cd /root/contrastive_entrain_calib && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 /root/miniconda3/bin/python training/run_exp008_binary_probe_penalty.py --max_steps 2 --log_steps 1 --retrain_interval 1 --grad_accum 1 --output_dir /root/contrastive_entrain_calib/checkpoints/exp008_dryrun 2>&1 | tail -100'\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-18T19:01:16.254545+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-29046",
  "command": "rm -rf /root/contrastive_entrain_calib/checkpoints/exp008_dryrun && mkdir -p /root/contrastive_entrain_calib/checkpoints/exp008_dryrun && cd /root/contrastive_entrain_calib && nohup bash -c 'CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 /root/miniconda3/bin/python training/run_exp008_binary_probe_penalty.py --max_steps 2 --log_steps 1 --retrain_interval 1 --grad_accum 1 --output_dir /root/contrastive_entrain_calib/checkpoints/exp008_dryrun' > /root/contrastive_entrain_calib/checkpoints/exp008_dryrun/nohup.log 2>&1 &\necho \"PID=$!\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-29046",
    "command": "rm -rf /root/contrastive_entrain_calib/checkpoints/exp008_dryrun && mkdir -p /root/contrastive_entrain_calib/checkpoints/exp008_dryrun && cd /root/contrastive_entrain_calib && nohup bash -c 'CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 /root/miniconda3/bin/python training/run_exp008_binary_probe_penalty.py --max_steps 2 --log_steps 1 --retrain_interval 1 --grad_accum 1 --output_dir /root/contrastive_entrain_calib/checkpoints/exp008_dryrun' > /root/contrastive_entrain_calib/checkpoints/exp008_dryrun/nohup.log 2>&1 &\necho \"PID=$!\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-18T19:01:16.254683+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'rm -rf /root/contrastive_entrain_calib/checkpoints/exp008_dryrun && mkdir -p /root/contrastive_entrain_calib/checkpoints/exp008_dryrun && cd /root/contrastive_entrain_calib && nohup bash -c \\\\'CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 /root/miniconda3/bin/python training/run_exp008_binary_probe_penalty.py --max_steps 2 --log_steps 1 --retrain_interval 1 --grad_accum 1 --output_dir /root/contrastive_entrain_calib/checkpoints/exp008_dryrun\\\\' > /root/contrastive_entrain_calib/checkpoints/exp008_dryrun/nohup.log 2>&1 &\\\\necho \\\"PID=$!\\\"'\\n\\nStdout:\\n\\nPID=78964\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 31.2}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-18T19:01:16.254838+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-29046",
  "command": "sleep 60 && cat /root/contrastive_entrain_calib/checkpoints/exp008_dryrun/nohup.log",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-29046",
    "command": "sleep 60 && cat /root/contrastive_entrain_calib/checkpoints/exp008_dryrun/nohup.log",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-18T19:01:16.254989+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'sleep 60 && cat /root/contrastive_entrain_calib/checkpoints/exp008_dryrun/nohup.log'\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 31.03}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-18T19:01:16.255129+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29046",
  "command": "cat /root/contrastive_entrain_calib/checkpoints/exp008_dryrun/nohup.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29046",
    "command": "cat /root/contrastive_entrain_calib/checkpoints/exp008_dryrun/nohup.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-18T19:01:16.255285+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-19 02:59:44,470 [INFO] exp008: === exp-008: Binary Probe Penalty Baseline ===\\n2026-05-19 02:59:44,470 [INFO] exp008: Config: lr=5e-05 lambda_reward=0.1 lambda_probe=1.0 max_steps=2 retrain_interval=1\\n2026-05-19 02:59:44,994 [INFO] exp008: Dataset: 362 samples from /root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl\\n2026-05-19 02:59:44,995 [INFO] exp008: Training probe from /root/contrastive_entrain_calib/results/exp001/activations.pt\\n2026-05-19 02:59:45,342 [INFO] exp008: Probe epoch 50/200: loss=0.1208 acc=0.9558\\n2026-05-19 02:59:45,423 [INFO] exp008: Probe epoch 100/200: loss=0.0683 acc=0.9890\\n2026-05-19 02:59:45,453 [INFO] exp008: Probe epoch 150/200: loss=0.0493 acc=0.9945\\n2026-05-19 02:59:45,539 [INFO] exp008: Probe epoch 200/200: loss=0.0372 acc=0.9945\\n2026-05-19 02:59:45,540 [INFO] exp008: Probe accuracy: 0.9945\\n2026-05-19 02:59:45,541 [INFO] exp008: Probe saved to /root/contrastive_entrain_calib/checkpoints/exp008_dryrun/probe.pt\\n2026-05-19 02:59:45,541 [INFO] exp008: Precomputing R3 scores with cross-encoder/nli-deberta-v3-base ...\\n2026-05-19 02:59:46,755 [INFO] exp008: NLI model loaded: cross-encoder/nli-deberta-v3-base (entailment_idx=1)\\n2026-05-19 02:59:48,768 [INFO] exp008: R3: mean=0.5000 min=0.0001 max=0.9999\\n2026-05-19 02:59:48,769 [INFO] exp008: Loading model: /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B\\n`torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading checkpoint shards:   0%|          | 0/5 [00:00<?, ?it/s]\\rLoading checkpoint shards: 100%|██████████| 5/5 [00:00<00:00, 225.65it/s]\\n2026-05-19 02:59:56,898 [INFO] exp008: Starting training: max_steps=2, batch=1, grad_accum=1, effective_batch=1\\n`use_cache=True` is incompatible with gradient checkpointing. Setting `use_cache=False`.\\n2026-05-19 02:59:57,744 [INFO] exp008: step=1 loss=2.2827 sft=2.2828 R3=0.9998 S(t)=0.9997 lr=2.50e-07\\n2026-05-19 02:59:57,744 [INFO] exp008: [RETRAIN] Ret
…[truncated 515 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-18T19:01:16.255462+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29046",
  "command": "tail -20 /root/contrastive_entrain_calib/checkpoints/exp008_dryrun/nohup.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29046",
    "command": "tail -20 /root/contrastive_entrain_calib/checkpoints/exp008_dryrun/nohup.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-18T19:01:16.255615+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-19 02:59:45,540 [INFO] exp008: Probe accuracy: 0.9945\\n2026-05-19 02:59:45,541 [INFO] exp008: Probe saved to /root/contrastive_entrain_calib/checkpoints/exp008_dryrun/probe.pt\\n2026-05-19 02:59:45,541 [INFO] exp008: Precomputing R3 scores with cross-encoder/nli-deberta-v3-base ...\\n2026-05-19 02:59:46,755 [INFO] exp008: NLI model loaded: cross-encoder/nli-deberta-v3-base (entailment_idx=1)\\n2026-05-19 02:59:48,768 [INFO] exp008: R3: mean=0.5000 min=0.0001 max=0.9999\\n2026-05-19 02:59:48,769 [INFO] exp008: Loading model: /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B\\n`torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading checkpoint shards:   0%|          | 0/5 [00:00<?, ?it/s]\\rLoading checkpoint shards: 100%|██████████| 5/5 [00:00<00:00, 225.65it/s]\\n2026-05-19 02:59:56,898 [INFO] exp008: Starting training: max_steps=2, batch=1, grad_accum=1, effective_batch=1\\n`use_cache=True` is incompatible with gradient checkpointing. Setting `use_cache=False`.\\n2026-05-19 02:59:57,744 [INFO] exp008: step=1 loss=2.2827 sft=2.2828 R3=0.9998 S(t)=0.9997 lr=2.50e-07\\n2026-05-19 02:59:57,744 [INFO] exp008: [RETRAIN] Retraining probe at step 1 ...\\n2026-05-19 03:00:34,433 [INFO] exp008: [RETRAIN] Extracted 362 activations (50.0% positive)\\n2026-05-19 03:00:34,668 [INFO] exp008: [INFO] Probe retrained at step 1: acc=0.9945, auroc=1.0000\\n2026-05-19 03:00:34,991 [INFO] exp008: step=2 loss=1.8777 sft=1.9106 R3=0.4268 S(t)=0.0977 lr=5.00e-07\\n2026-05-19 03:00:34,992 [INFO] exp008: [RETRAIN] Retraining probe at step 2 ...\\n2026-05-19 03:01:02,137 [INFO] exp008: [RETRAIN] Extracted 362 activations (50.0% positive)\\n2026-05-19 03:01:02,372 [INFO] exp008: [INFO] Probe retrained at step 2: acc=1.0000, auroc=1.0000\\n2026-05-19 03:01:04,103 [INFO] exp008: Training complete. Final checkpoint: /root/contrastive_entrain_calib/checkpoints/exp008_dryrun/final\\ntrainable params: 174,587,904 || all params: 8,365,323,
…[truncated 132 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 79 · 2026-05-18T19:01:16.255803+00:00_

Dry-run 完成，所有验证点通过：

| 检查项 | 结果 |
|--------|------|
| 初始 probe 训练 | acc=0.9945 ✓ |
| Step 1 在线重训练 | acc=0.9945, auroc=1.0000 ✓ |
| Step 2 在线重训练 | acc=1.0000, auroc=1.0000 ✓ |
| S(t) 非零 | step1=0.9997, step2=0.0977 ✓ |
| 无 OOM | 正常完成 ✓ |
| 重训练耗时 | ~37s/次（362 forward passes + 200 epoch probe train） |

现在恢复正式参数。脚本默认值已经是 `max_steps=8000, retrain_interval=500, log_steps=10`，无需额外修改。

**总结**：

修改内容：
1. `TrainConfig` 新增 `retrain_interval: int = 500`
2. `parse_args` 新增 `--retrain_interval` 和 `--log_steps` 参数
3. 新增 `retrain_probe_online()` 函数：用 `torch.no_grad()` 遍历 362 个 calibration samples 提取当前模型 hidden states，重训 200 epoch linear probe，返回 (probe, acc, auroc)
4. 训练循环中每 `retrain_interval` 步触发重训练，替换 probe 并 log 精度

脚本已同步到 westd-28034 和 westd-29046 的 `/root/contrastive_entrain_calib/training/run_exp008_binary_probe_penalty.py`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_exp008-online-probe-retrain_20260518T184944"
}
```

</details>

---
