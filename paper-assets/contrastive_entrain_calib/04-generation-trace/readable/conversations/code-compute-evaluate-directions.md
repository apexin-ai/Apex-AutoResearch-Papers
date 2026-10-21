# code compute evaluate directions

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_code_compute_evaluate_directions_20260518T064026.jsonl`
- **Structured JSON:** [`97a726c5c1c7c22a5840.json`](../../sessions/97/97a726c5c1c7c22a5840.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-18T06:42:27.176786+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/data/ 2>/dev/null || echo \"directory not found\"",
  "description": "List existing data artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_compute_evaluate_directions_20260518T064026",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/data/ 2>/dev/null || echo \"directory not found\"",
    "description": "List existing data artifacts"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T06:42:27.177270+00:00_

__pycache__
calibration_data.jsonl
extract_activations.py
generate_calibration_data.py
validate_calibration_data.py
validation_report.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_compute_evaluate_directions_20260518T064026",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T06:42:27.177482+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/ 2>/dev/null || echo \"directory not found\"",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_compute_evaluate_directions_20260518T064026",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/ 2>/dev/null || echo \"directory not found\"",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-18T06:42:27.177631+00:00_

_project
data
manifest.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_compute_evaluate_directions_20260518T064026",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T06:42:27.178207+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/data/extract_activations.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_compute_evaluate_directions_20260518T064026",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/data/extract_activations.py"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T06:42:27.178973+00:00_

1	#!/usr/bin/env python3
2	"""Extract hidden-state activations at critical turns from Qwen3-8B.
3	
4	Input:  Phase 1 calibration JSONL — each line has fields:
5	        {id, condition, domain, evidence_strength, correction_turn, turns, ...}
6	        where turns = [{"role": "user"|"assistant", "content": "..."}, ...]
7	Output: activations.pt         — list[dict] with metadata + (num_layers, 2, hidden_dim) tensor
8	        activations_meta.jsonl  — metadata only (no tensors), for quick inspection
9	Deps:   transformers, torch, tqdm
10	"""
11	
12	import argparse
13	import json
14	import logging
15	import sys
16	from pathlib import Path
17	
18	import torch
19	from tqdm import tqdm
20	from transformers import AutoModelForCausalLM, AutoTokenizer
21	
22	logger = logging.getLogger(__name__)
23	
24	
25	def load_samples(path: str, max_samples: int | None = None) -> list[dict]:
26	    """Load calibration samples from JSONL file."""
27	    samples = []
28	    with open(path) as f:
29	        for line in f:
30	            line = line.strip()
31	            if not line:
32	                continue
33	            samples.append(json.loads(line))
34	            if max_samples and len(samples) >= max_samples:
35	                break
36	    return samples
37	
38	
39	def _apply_template(tokenizer, messages: list[dict], **kwargs) -> list[int]:
40	    """apply_chat_template with Qwen3 thinking mode disabled when supported."""
41	    try:
42	        return tokenizer.apply_chat_template(
43	            messages, enable_thinking=False, tokenize=True, **kwargs
44	        )
45	    except TypeError:
46	        return tokenizer.apply_chat_template(messages, tokenize=True, **kwargs)
47	
48	
49	def find_critical_positions(
50	    tokenizer, turns: list[dict], correction_turn: int
51	) -> tuple[int, int, list[int]]:
52	    """Locate user-last-token and assistant-first-token positions in the tokenized conversation.
53	
54	    Token boundary detection strategy:
55	      Step 1: Tokenize through e
…[truncated 12519 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_compute_evaluate_directions_20260518T064026",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T06:42:27.179260+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/data/compute_directions.py",
  "content": "#!/usr/bin/env python3\n\"\"\"Compute contrastive direction vectors (d_syc, d_gen) from paired activations.\n\nInput:  .pt file from extract_activations.py — list[dict] with keys:\n        {pair_id, condition, domain, evidence_strength, correction_turn,\n         activations: Tensor(num_layers, 2, hidden_dim)}\n        Each pair_id has two entries: condition=\"warranted_revision\" and\n        condition=\"sycophantic_capitulation\".\n\nOutput: directions.pt — dict with keys:\n        d_syc              (num_layers, 2, hidden_dim) — L2-normalized\n        d_gen              (num_layers, 2, hidden_dim) — L2-normalized\n        train_pair_ids     list[str]\n        test_pair_ids      list[str]\n        metadata           dict\n\nDeps:   torch, numpy, sklearn (for StratifiedShuffleSplit)\n\"\"\"\n\nimport argparse\nimport logging\nimport sys\nfrom collections import defaultdict\nfrom pathlib import Path\n\nimport numpy as np\nimport torch\nfrom sklearn.model_selection import StratifiedShuffleSplit\n\nlogger = logging.getLogger(__name__)\n\n\ndef load_and_group(path: str) -> dict[str, dict[str, dict]]:\n    \"\"\"Load activation records and group by pair_id.\n\n    Returns {pair_id: {\"warranted_revision\": record, \"sycophantic_capitulation\": record}}.\n    \"\"\"\n    records = torch.load(path, map_location=\"cpu\", weights_only=False)\n    logger.info(\"Loaded %d records from %s\", len(records), path)\n\n    grouped: dict[str, dict[str, dict]] = defaultdict(dict)\n    for rec in records:\n        pid = rec[\"pair_id\"]\n        cond = rec[\"condition\"]\n        if cond in grouped[pid]:\n            logger.warning(\"Duplicate condition '%s' for pair_id '%s'; overwriting\", cond, pid)\n        grouped[pid][cond] = rec\n\n    complete = {}\n    for pid, conds in grouped.items():\n        if \"warranted_revision\" in conds and \"sycophantic_capitulation\" in conds:\n            complete[pid] = conds\n        else:\n            logger.warning(\n                \"Pair '%s' incomplete (conditions: %s); skipping\", pid, list(conds.keys())\n            )\n\n    logger.info(\"Complete pairs: %d\", len(complete))\n    return complete\n\n\ndef stratified_split(\n    pairs: dict[str, dict[str, dict]], test_ratio: float, seed: int\n) -> tuple[list[str], list[str]]:\n    \"\"\"Split pair_ids into train/test with stratification by domain.\n\n    Uses StratifiedShuffleSplit so each domain's proportion is preserved\n    across the split. The split unit is the pair (both conditions stay together).\n    \"\"\"\n    pair_ids = sorted(pairs.keys())\n    domains = [pairs[pid][\"warranted_revision\"][\"domain\"] for pid in pair_ids]\n\n    # Check if stratification is feasible (need >= 2 samples per domain for split)\n    domain_counts = defaultdict(int)\n    for d in domains:\n        domain_counts[d] += 1\n\n    min_count = min(domain_counts.values())\n    if min_count < 2:\n        logger.warning(\n            \"Some domains have < 2 pairs (min=%d); falling back to unstratified shuffle\",\n            min_count,\n        )\n        rng = np.random.RandomState(seed)\n        idx = rng.permutation(len(pair_ids))\n        n_test = max(1, int(len(pair_ids) * test_ratio))\n        test_idx = set(idx[:n_test])\n        train_ids = [pair_ids[i] for i in range(len(pair_ids)) if i not in test_idx]\n        test_ids = [pair_ids[i] for i in range(len(pair_ids)) if i in test_idx]\n        return train_ids, test_ids\n\n    splitter = StratifiedShuffleSplit(n_splits=1, test_size=test_ratio, random_state=seed)\n    pair_ids_arr = np.array(pair_ids)\n    domains_arr = np.array(domains)\n\n    train_idx, test_idx = next(splitter.split(pair_ids_arr, domains_arr))\n    train_ids = pair_ids_arr[train_idx].tolist()\n    test_ids = pair_ids_arr[test_idx].tolist()\n\n    logger.info(\"Split: %d train, %d test\", len(train_ids), len(test_ids))\n    return train_ids, test_ids\n\n\ndef compute_direction(\n    pairs: dict[str, dict[str, dict]],\n    pair_ids: list[str],\n    positive_condition: str,\n    negative_condition: str,\n) -> torch.Tensor:\n    \"\"\"Compute difference-in-means direction: mean(positive) - mean(negative).\n\n    Returns L2-normalized direction of shape (num_layers, 2, hidden_dim).\n    \"\"\"\n    pos_acts = []\n    neg_acts = []\n    for pid in pair_ids:\n        pos_acts.append(pairs[pid][positive_condition][\"activations\"])\n        neg_acts.append(pairs[pid][negative_condition][\"activations\"])\n\n    # Stack: (N, num_layers, 2, hidden_dim)\n    pos_mean = torch.stack(pos_acts).mean(dim=0)\n    neg_mean = torch.stack(neg_acts).mean(dim=0)\n\n    direction = pos_mean - neg_mean\n\n    # L2 normalize per (layer, token_position) slice\n    norms = direction.norm(dim=-1, keepdim=True).clamp(min=1e-8)\n    direction = direction / norms\n\n    return direction\n\n\ndef main() -> None:\n    parser = argparse.ArgumentParser(\n        description=\"Compute contrastive direction vectors from paired activations.\"\n    )\n    parser.add_argument(\"input\", help=\"Path to activations .pt file (Phase 2 output)\")\n    parser.add_argument(\"--output-dir\", default=\".\", help=\"Output directory (default: .)\")\n    parser.add_argument(\n        \"--test-ratio\", type=float, default=0.2, help=\"Test set ratio (default: 0.2)\"\n    )\n    parser.add_argument(\"--seed\", type=int, default=42, help=\"Random seed (default: 42)\")\n    args = parser.parse_args()\n\n    logging.basicConfig(\n        level=logging.INFO,\n        format=\"%(asctime)s [%(levelname)s] %(name)s: %(message)s\",\n    )\n\n    pairs = load_and_group(args.input)\n    if not pairs:\n        logger.error(\"No complete pairs found; exiting\")\n        sys.exit(1)\n\n    train_ids, test_ids = stratified_split(pairs, args.test_ratio, args.seed)\n\n    # d_syc: sycophantic_capitulation - warranted_revision (on train set)\n    logger.info(\"Computing d_syc from %d train pairs\", len(train_ids))\n    d_syc = compute_direction(\n        pairs, train_ids,\n        positive_condition=\"sycophantic_capitulation\",\n        negative_condition=\"warranted_revision\",\n    )\n\n    # d_gen: warranted_revision - sycophantic_capitulation (on train set)\n    # Currently d_gen = -d_syc, but stored separately for future extensibility.\n    logger.info(\"Computing d_gen from %d train pairs\", len(train_ids))\n    d_gen = compute_direction(\n        pairs, train_ids,\n        positive_condition=\"warranted_revision\",\n        negative_condition=\"sycophantic_capitulation\",\n    )\n\n    num_layers, _, hidden_dim = d_syc.shape\n    metadata = {\n        \"num_layers\": num_layers,\n        \"hidden_dim\": hidden_dim,\n        \"test_ratio\": args.test_ratio,\n        \"seed\": args.seed,\n        \"num_train_pairs\": len(train_ids),\n        \"num_test_pairs\": len(test_ids),\n        \"num_total_pairs\": len(pairs),\n    }\n\n    out_dir = Path(args.output_dir)\n    out_dir.mkdir(parents=True, exist_ok=True)\n    out_path = out_dir / \"directions.pt\"\n\n    payload = {\n        \"d_syc\": d_syc,\n        \"d_gen\": d_gen,\n        \"train_pair_ids\": train_ids,\n        \"test_pair_ids\": test_ids,\n        \"metadata\": metadata,\n    }\n    torch.save(payload, out_path)\n    logger.info(\"Saved directions to %s\", out_path)\n    logger.info(\"Metadata: %s\", metadata)\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_compute_evaluate_directions_20260518T064026",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/data/compute_directions.py",
    "content": "#!/usr/bin/env python3\n\"\"\"Compute contrastive direction vectors (d_syc, d_gen) from paired activations.\n\nInput:  .pt file from extract_activations.py — list[dict] with keys:\n        {pair_id, condition, domain, evidence_strength, correction_turn,\n         activations: Tensor(num_layers, 2, hidden_dim)}\n        Each pair_id has two entries: condition=\"warranted_revision\" and\n        condition=\"sycophantic_capitulation\".\n\nOutput: directions.pt — dict with keys:\n        d_syc              (num_layers, 2, hidden_dim) — L2-normalized\n        d_gen              (num_layers, 2, hidden_dim) — L2-normalized\n        train_pair_ids     list[str]\n        test_pair_ids      list[str]\n        metadata           dict\n\nDeps:   torch, numpy, sklearn (for StratifiedShuffleSplit)\n\"\"\"\n\nimport argparse\nimport logging\nimport sys\nfrom collections import defaultdict\nfrom pathlib import Path\n\nimport numpy as np\nimport torch\nfrom sklearn.model_selection import StratifiedShuffleSplit\n\nlogger = logging.getLogger(__name__)\n\n\ndef load_and_group(path: str) -> dict[str, dict[str, dict]]:\n    \"\"\"Load activation records and group by pair_id.\n\n    Returns {pair_id: {\"warranted_revision\": record, \"sycophantic_capitulation\": record}}.\n    \"\"\"\n    records = torch.load(path, map_location=\"cpu\", weights_only=False)\n    logger.info(\"Loaded %d records from %s\", len(records), path)\n\n    grouped: dict[str, dict[str, dict]] = defaultdict(dict)\n    for rec in records:\n        pid = rec[\"pair_id\"]\n        cond = rec[\"condition\"]\n        if cond in grouped[pid]:\n            logger.warning(\"Duplicate condition '%s' for pair_id '%s'; overwriting\", cond, pid)\n        grouped[pid][cond] = rec\n\n    complete = {}\n    for pid, conds in grouped.items():\n        if \"warranted_revision\" in conds and \"sycophantic_capitulation\" in conds:\n            complete[pid] = conds\n        else:\n            logger.warning(\n                \"Pair '%s' incomplete (conditions: %s); skipping\", pid, list(conds.keys())\n            )\n\n    logger.info(\"Complete pairs: %d\", len(complete))\n    return complete\n\n\ndef stratified_split(\n    pairs: dict[str, dict[str, dict]], test_ratio: float, seed: int\n) -> tuple[list[str], list[str]]:\n    \"\"\"Split pair_ids into train/test with stratification by domain.\n\n    Uses StratifiedShuffleSplit so each domain's proportion is preserved\n    across the split. The split unit is the pair (both conditions stay together).\n    \"\"\"\n    pair_ids = sorted(pairs.keys())\n    domains = [pairs[pid][\"warranted_revision\"][\"domain\"] for pid in pair_ids]\n\n    # Check if stratification is feasible (need >= 2 samples per domain for split)\n    domain_counts = defaultdict(int)\n    for d in domains:\n        domain_counts[d] += 1\n\n    min_count = min(domain_counts.values())\n    if min_count < 2:\n        logger.warning(\n            \"Some domains have < 2 pairs (min=%d); falling back to unstratified shuffle\",\n            min_count,\n        )\n        rng = np.random.RandomState(seed)\n        idx = rng.permutation(len(pair_ids))\n        n_test = max(1, int(len(pair_ids) * test_ratio))\n        test_idx = set(idx[:n_test])\n        train_ids = [pair_ids[i] for i in range(len(pair_ids)) if i not in test_idx]\n        test_ids = [pair_ids[i] for i in range(len(pair_ids)) if i in test_idx]\n        return train_ids, test_ids\n\n    splitter = StratifiedShuffleSplit(n_splits=1, test_size=test_ratio, random_state=seed)\n    pair_ids_arr = np.array(pair_ids)\n    domains_arr = np.array(domains)\n\n    train_idx, test_idx = next(splitter.split(pair_ids_arr, domains_arr))\n    train_ids = pair_ids_arr[train_idx].tolist()\n    test_ids = pair_ids_arr[test_idx].tolist()\n\n    logger.info(\"Split: %d train, %d test\", len(train_ids), len(test_ids))\n    return train_ids, test_ids\n\n\ndef compute_direction(\n    pairs: dict[str, dict[str, dict]],\n    pair_ids: list[str],\n    positive_condition: str,\n    negative_condition: str,\n) -> torch.Tensor:\n    \"\"\"Compute difference-in-means direction: mean(positive) - mean(negative).\n\n    Returns L2-normalized direction of shape (num_layers, 2, hidden_dim).\n    \"\"\"\n    pos_acts = []\n    neg_acts = []\n    for pid in pair_ids:\n        pos_acts.append(pairs[pid][positive_condition][\"activations\"])\n        neg_acts.append(pairs[pid][negative_condition][\"activations\"])\n\n    # Stack: (N, num_layers, 2, hidden_dim)\n    pos_mean = torch.stack(pos_acts).mean(dim=0)\n    neg_mean = torch.stack(neg_acts).mean(dim=0)\n\n    direction = pos_mean - neg_mean\n\n    # L2 normalize per (layer, token_position) slice\n    norms = direction.norm(dim=-1, keepdim=True).clamp(min=1e-8)\n    direction = direction / norms\n\n    return direction\n\n\ndef main() -> None:\n    parser = argparse.ArgumentParser(\n        description=\"Compute contrastive direction vectors from paired activations.\"\n    )\n    parser.add_argument(\"input\", help=\"Path to activations .pt file (Phase 2 output)\")\n    parser.add_argument(\"--output-dir\", default=\".\", help=\"Output directory (default: .)\")\n    parser.add_argument(\n        \"--test-ratio\", type=float, default=0.2, help=\"Test set ratio (default: 0.2)\"\n    )\n    parser.add_argument(\"--seed\", type=int, default=42, help=\"Random seed (default: 42)\")\n    args = parser.parse_args()\n\n    logging.basicConfig(\n        level=logging.INFO,\n        format=\"%(asctime)s [%(levelname)s] %(name)s: %(message)s\",\n    )\n\n    pairs = load_and_group(args.input)\n    if not pairs:\n        logger.error(\"No complete pairs found; exiting\")\n        sys.exit(1)\n\n    train_ids, test_ids = stratified_split(pairs, args.test_ratio, args.seed)\n\n    # d_syc: sycophantic_capitulation - warranted_revision (on train set)\n    logger.info(\"Computing d_syc from %d train pairs\", len(train_ids))\n    d_syc = compute_direction(\n        pairs, train_ids,\n        positive_condition=\"sycophantic_capitulation\",\n        negative_condition=\"warranted_revision\",\n    )\n\n    # d_gen: warranted_revision - sycophantic_capitulation (on train set)\n    # Currently d_gen = -d_syc, but stored separately for future extensibility.\n    logger.info(\"Computing d_gen from %d train pairs\", len(train_ids))\n    d_gen = compute_direction(\n        pairs, train_ids,\n        positive_condition=\"warranted_revision\",\n        negative_condition=\"sycophantic_capitulation\",\n    )\n\n    num_layers, _, hidden_dim = d_syc.shape\n    metadata = {\n        \"num_layers\": num_layers,\n        \"hidden_dim\": hidden_dim,\n        \"test_ratio\": args.test_ratio,\n        \"seed\": args.seed,\n        \"num_train_pairs\": len(train_ids),\n        \"num_test_pairs\": len(test_ids),\n        \"num_total_pairs\": len(pairs),\n    }\n\n    out_dir = Path(args.output_dir)\n    out_dir.mkdir(parents=True, exist_ok=True)\n    out_path = out_dir / \"directions.pt\"\n\n    payload = {\n        \"d_syc\": d_syc,\n        \"d_gen\": d_gen,\n        \"train_pair_ids\": train_ids,\n        \"test_pair_ids\": test_ids,\n        \"metadata\": metadata,\n    }\n    torch.save(payload, out_path)\n    logger.info(\"Saved directions to %s\", out_path)\n    logger.info(\"Metadata: %s\", metadata)\n\n\nif __name__ == \"__main__\":\n    main()\n"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T06:42:27.179565+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/data/compute_directions.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_compute_evaluate_directions_20260518T064026",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T06:42:27.179776+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/data/evaluate_directions.py",
  "content": "#!/usr/bin/env python3\n\"\"\"Evaluate contrastive direction vectors on held-out test pairs.\n\nInput:\n  --directions  directions.pt from compute_directions.py\n  --activations activations.pt from extract_activations.py\n  --output-dir  directory for JSON report\n\nOutput:\n  evaluation_report.json — per-layer AUROC, cosine similarity, stratified\n                           breakdown, Go/No-Go verdict\n  Human-readable summary printed to stdout\n\nDeps: torch, numpy, sklearn\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport sys\nfrom collections import defaultdict\nfrom pathlib import Path\n\nimport numpy as np\nimport torch\nfrom sklearn.metrics import roc_auc_score\n\nlogger = logging.getLogger(__name__)\n\n\ndef load_test_samples(\n    activations_path: str, test_pair_ids: list[str]\n) -> list[dict]:\n    \"\"\"Load activation records and keep only those in the test set.\"\"\"\n    records = torch.load(activations_path, map_location=\"cpu\", weights_only=False)\n    test_set = set(test_pair_ids)\n    filtered = [r for r in records if r[\"pair_id\"] in test_set]\n    logger.info(\n        \"Loaded %d total records; %d belong to test set (%d test pair_ids)\",\n        len(records), len(filtered), len(test_set),\n    )\n    return filtered\n\n\ndef compute_auroc_per_layer(\n    samples: list[dict], d_syc: torch.Tensor\n) -> dict[int, dict[int, float]]:\n    \"\"\"Compute AUROC per layer and token position.\n\n    For each sample, project its activation onto d_syc (dot product) to get a\n    scalar score. Label: 1=sycophantic_capitulation, 0=warranted_revision.\n\n    Returns {layer_idx: {token_pos: auroc}}.\n    \"\"\"\n    num_layers = d_syc.shape[0]\n    num_positions = d_syc.shape[1]\n\n    labels = []\n    # scores[layer][pos] -> list of floats\n    scores: dict[int, dict[int, list]] = {\n        l: {p: [] for p in range(num_positions)} for l in range(num_layers)\n    }\n\n    for sample in samples:\n        label = 1 if sample[\"condition\"] == \"sycophantic_capitulation\" else 0\n        labels.append(label)\n        acts = sample[\"activations\"]  # (num_layers, 2, hidden_dim)\n\n        for layer in range(num_layers):\n            for pos in range(num_positions):\n                score = torch.dot(acts[layer, pos], d_syc[layer, pos]).item()\n                scores[layer][pos].append(score)\n\n    labels_arr = np.array(labels)\n    results = {}\n    for layer in range(num_layers):\n        results[layer] = {}\n        for pos in range(num_positions):\n            scores_arr = np.array(scores[layer][pos])\n            if len(np.unique(labels_arr)) < 2:\n                results[layer][pos] = float(\"nan\")\n            else:\n                results[layer][pos] = roc_auc_score(labels_arr, scores_arr)\n\n    return results\n\n\ndef compute_cosine_per_layer(\n    d_syc: torch.Tensor, d_gen: torch.Tensor\n) -> dict[int, dict[int, float]]:\n    \"\"\"Compute cosine similarity between d_syc and d_gen per layer and token position.\"\"\"\n    num_layers = d_syc.shape[0]\n    num_positions = d_syc.shape[1]\n\n    results = {}\n    for layer in range(num_layers):\n        results[layer] = {}\n        for pos in range(num_positions):\n            cos = torch.nn.functional.cosine_similarity(\n                d_syc[layer, pos].unsqueeze(0),\n                d_gen[layer, pos].unsqueeze(0),\n            ).item()\n            results[layer][pos] = cos\n\n    return results\n\n\ndef compute_stratified_auroc(\n    samples: list[dict], d_syc: torch.Tensor, group_key: str, best_layer: int\n) -> dict[str, dict[int, float]]:\n    \"\"\"Compute AUROC broken down by a metadata field (domain, evidence_strength, etc.).\n\n    Uses the best layer only, across all token positions.\n    \"\"\"\n    num_positions = d_syc.shape[1]\n\n    groups: dict[str, list[dict]] = defaultdict(list)\n    for s in samples:\n        groups[str(s[group_key])].append(s)\n\n    results = {}\n    for group_val, group_samples in sorted(groups.items()):\n        labels = []\n        scores_by_pos: dict[int, list] = {p: [] for p in range(num_positions)}\n\n        for sample in group_samples:\n            label = 1 if sample[\"condition\"] == \"sycophantic_capitulation\" else 0\n            labels.append(label)\n            for pos in range(num_positions):\n                score = torch.dot(\n                    sample[\"activations\"][best_layer, pos], d_syc[best_layer, pos]\n                ).item()\n                scores_by_pos[pos].append(score)\n\n        labels_arr = np.array(labels)\n        if len(np.unique(labels_arr)) < 2:\n            results[group_val] = {p: float(\"nan\") for p in range(num_positions)}\n        else:\n            results[group_val] = {\n                p: roc_auc_score(labels_arr, np.array(scores_by_pos[p]))\n                for p in range(num_positions)\n            }\n\n    return results\n\n\ndef go_nogo_verdict(best_auroc: float, best_cosine: float) -> dict:\n    \"\"\"Determine Go/No-Go based on thresholds.\n\n    Criteria:\n      PASS: AUROC >= 0.85 AND cosine(d_syc, d_gen) < 0.3\n      GRAY: AUROC in [0.80, 0.85)\n      FAIL: AUROC < 0.80\n\n    Note: In the current binary setup d_gen = -d_syc, so cosine is always -1.\n    The cosine check becomes meaningful when d_gen is independently defined.\n    \"\"\"\n    cosine_ok = best_cosine < 0.3\n\n    if best_auroc >= 0.85 and cosine_ok:\n        verdict = \"PASS\"\n        reason = f\"AUROC={best_auroc:.4f} >= 0.85 and cosine={best_cosine:.4f} < 0.3\"\n    elif best_auroc >= 0.80:\n        verdict = \"GRAY\"\n        reason = f\"AUROC={best_auroc:.4f} in [0.80, 0.85); needs further investigation\"\n        if not cosine_ok:\n            reason += f\"; cosine={best_cosine:.4f} >= 0.3 (unexpected)\"\n    else:\n        verdict = \"FAIL\"\n        reason = f\"AUROC={best_auroc:.4f} < 0.80\"\n\n    return {\"verdict\": verdict, \"reason\": reason, \"auroc\": best_auroc, \"cosine\": best_cosine}\n\n\ndef main() -> None:\n    parser = argparse.ArgumentParser(\n        description=\"Evaluate contrastive direction vectors on test set.\"\n    )\n    parser.add_argument(\n        \"--directions\", required=True, help=\"Path to directions.pt from compute_directions.py\"\n    )\n    parser.add_argument(\n        \"--activations\", required=True, help=\"Path to activations.pt from extract_activations.py\"\n    )\n    parser.add_argument(\"--output-dir\", default=\".\", help=\"Output directory (default: .)\")\n    args = parser.parse_args()\n\n    logging.basicConfig(\n        level=logging.INFO,\n        format=\"%(asctime)s [%(levelname)s] %(name)s: %(message)s\",\n    )\n\n    logger.info(\"Loading directions from %s\", args.directions)\n    directions = torch.load(args.directions, map_location=\"cpu\", weights_only=False)\n    d_syc = directions[\"d_syc\"]\n    d_gen = directions[\"d_gen\"]\n    test_pair_ids = directions[\"test_pair_ids\"]\n    metadata = directions[\"metadata\"]\n\n    if not test_pair_ids:\n        logger.error(\"No test pair IDs in directions file; exiting\")\n        sys.exit(1)\n\n    test_samples = load_test_samples(args.activations, test_pair_ids)\n    if not test_samples:\n        logger.error(\"No test samples found; exiting\")\n        sys.exit(1)\n\n    # Per-layer AUROC\n    logger.info(\"Computing per-layer AUROC\")\n    auroc_per_layer = compute_auroc_per_layer(test_samples, d_syc)\n\n    # Find best layer (max AUROC across token positions)\n    best_layer = -1\n    best_auroc = -1.0\n    best_pos = -1\n    for layer, pos_dict in auroc_per_layer.items():\n        for pos, auc in pos_dict.items():\n            if not np.isnan(auc) and auc > best_auroc:\n                best_auroc = auc\n                best_layer = layer\n                best_pos = pos\n\n    logger.info(\"Best layer=%d, pos=%d, AUROC=%.4f\", best_layer, best_pos, best_auroc)\n\n    # Cosine similarity\n    logger.info(\"Computing per-layer cosine similarity\")\n    cosine_per_layer = compute_cosine_per_layer(d_syc, d_gen)\n    best_cosine = cosine_per_layer[best_layer][best_pos]\n\n    # Stratified analysis at best layer\n    logger.info(\"Computing stratified AUROC breakdown\")\n    breakdown_domain = compute_stratified_auroc(test_samples, d_syc, \"domain\", best_layer)\n    breakdown_evidence = compute_stratified_auroc(\n        test_samples, d_syc, \"evidence_strength\", best_layer\n    )\n    breakdown_turn = compute_stratified_auroc(\n        test_samples, d_syc, \"correction_turn\", best_layer\n    )\n\n    # Go/No-Go\n    verdict = go_nogo_verdict(best_auroc, best_cosine)\n\n    # Build report\n    report = {\n        \"metadata\": metadata,\n        \"num_test_samples\": len(test_samples),\n        \"num_test_pairs\": len(test_pair_ids),\n        \"best_layer\": best_layer,\n        \"best_token_position\": best_pos,\n        \"best_auroc\": best_auroc,\n        \"best_cosine\": best_cosine,\n        \"per_layer_auroc\": {\n            str(l): {str(p): v for p, v in pos_dict.items()}\n            for l, pos_dict in auroc_per_layer.items()\n        },\n        \"per_layer_cosine\": {\n            str(l): {str(p): v for p, v in pos_dict.items()}\n            for l, pos_dict in cosine_per_layer.items()\n        },\n        \"stratified_auroc\": {\n            \"by_domain\": {\n                k: {str(p): v for p, v in pos_dict.items()}\n                for k, pos_dict in breakdown_domain.items()\n            },\n            \"by_evidence_strength\": {\n                k: {str(p): v for p, v in pos_dict.items()}\n                for k, pos_dict in breakdown_evidence.items()\n            },\n            \"by_correction_turn\": {\n                k: {str(p): v for p, v in pos_dict.items()}\n                for k, pos_dict in breakdown_turn.items()\n            },\n        },\n        \"go_nogo\": verdict,\n        \"note\": (\n            \"In the current binary setup d_gen = -d_syc, so cosine(d_syc, d_gen) = -1.0. \"\n            \"The cosine threshold check (< 0.3) becomes meaningful only when d_gen is \"\n            \"independently defined.\"\n        ),\n    }\n\n    # Save JSON report\n    out_dir = Path(args.output_dir)\n    out_dir.mkdir(parents=True, exist_ok=True)\n    report_path = out_dir / \"evaluation_report.json\"\n    with open(report_path, \"w\") as f:\n        json.dump(report, f, indent=2, ensure_ascii=False)\n    logger.info(\"Saved report to %s\", report_path)\n\n    # Print human-readable summary\n    token_pos_names = {0: \"user_last\", 1: \"asst_first\"}\n    print(\"\\n\" + \"=\" * 60)\n    print(\"DIRECTION EVALUATION SUMMARY\")\n    print(\"=\" * 60)\n    print(f\"Test pairs: {len(test_pair_ids)}  |  Test samples: {len(test_samples)}\")\n    print(f\"Layers: {metadata['num_layers']}  |  Hidden dim: {metadata['hidden_dim']}\")\n    print()\n\n    print(f\"Best layer: {best_layer}  |  Token position: {best_pos} ({token_pos_names.get(best_pos, '?')})\")\n    print(f\"Best AUROC: {best_auroc:.4f}\")\n    print(f\"Cosine(d_syc, d_gen) at best: {best_cosine:.4f}  (expected: -1.0 in binary setup)\")\n    print()\n\n    # Top 5 layers\n    all_layer_auc = []\n    for layer, pos_dict in auroc_per_layer.items():\n        for pos, auc in pos_dict.items():\n            if not np.isnan(auc):\n                all_layer_auc.append((layer, pos, auc))\n    all_layer_auc.sort(key=lambda x: x[2], reverse=True)\n\n    print(\"Top 5 (layer, position, AUROC):\")\n    for layer, pos, auc in all_layer_auc[:5]:\n        print(f\"  Layer {layer:2d}, {token_pos_names.get(pos, f'pos{pos}'):10s}: {auc:.4f}\")\n    print()\n\n    # Stratified breakdown\n    print(\"AUROC by domain (best layer, all positions):\")\n    for domain, pos_dict in sorted(breakdown_domain.items()):\n        vals = [f\"{token_pos_names.get(p, f'pos{p}')}={v:.4f}\" for p, v in sorted(pos_dict.items())]\n        print(f\"  {domain:25s}  {', '.join(vals)}\")\n    print()\n\n    print(\"AUROC by evidence_strength (best layer, all positions):\")\n    for es, pos_dict in sorted(breakdown_evidence.items()):\n        vals = [f\"{token_pos_names.get(p, f'pos{p}')}={v:.4f}\" for p, v in sorted(pos_dict.items())]\n        print(f\"  {es:25s}  {', '.join(vals)}\")\n    print()\n\n    # Go/No-Go\n    print(\"-\" * 60)\n    print(f\"GO/NO-GO VERDICT: {verdict['verdict']}\")\n    print(f\"  {verdict['reason']}\")\n    print(\"=\" * 60)\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_compute_evaluate_directions_20260518T064026",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/data/evaluate_directions.py",
    "content": "#!/usr/bin/env python3\n\"\"\"Evaluate contrastive direction vectors on held-out test pairs.\n\nInput:\n  --directions  directions.pt from compute_directions.py\n  --activations activations.pt from extract_activations.py\n  --output-dir  directory for JSON report\n\nOutput:\n  evaluation_report.json — per-layer AUROC, cosine similarity, stratified\n                           breakdown, Go/No-Go verdict\n  Human-readable summary printed to stdout\n\nDeps: torch, numpy, sklearn\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport sys\nfrom collections import defaultdict\nfrom pathlib import Path\n\nimport numpy as np\nimport torch\nfrom sklearn.metrics import roc_auc_score\n\nlogger = logging.getLogger(__name__)\n\n\ndef load_test_samples(\n    activations_path: str, test_pair_ids: list[str]\n) -> list[dict]:\n    \"\"\"Load activation records and keep only those in the test set.\"\"\"\n    records = torch.load(activations_path, map_location=\"cpu\", weights_only=False)\n    test_set = set(test_pair_ids)\n    filtered = [r for r in records if r[\"pair_id\"] in test_set]\n    logger.info(\n        \"Loaded %d total records; %d belong to test set (%d test pair_ids)\",\n        len(records), len(filtered), len(test_set),\n    )\n    return filtered\n\n\ndef compute_auroc_per_layer(\n    samples: list[dict], d_syc: torch.Tensor\n) -> dict[int, dict[int, float]]:\n    \"\"\"Compute AUROC per layer and token position.\n\n    For each sample, project its activation onto d_syc (dot product) to get a\n    scalar score. Label: 1=sycophantic_capitulation, 0=warranted_revision.\n\n    Returns {layer_idx: {token_pos: auroc}}.\n    \"\"\"\n    num_layers = d_syc.shape[0]\n    num_positions = d_syc.shape[1]\n\n    labels = []\n    # scores[layer][pos] -> list of floats\n    scores: dict[int, dict[int, list]] = {\n        l: {p: [] for p in range(num_positions)} for l in range(num_layers)\n    }\n\n    for sample in samples:\n        label = 1 if sample[\"condition\"] == \"sycophantic_capitulation\" else 0\n        labels.append(label)\n        acts = sample[\"activations\"]  # (num_layers, 2, hidden_dim)\n\n        for layer in range(num_layers):\n            for pos in range(num_positions):\n                score = torch.dot(acts[layer, pos], d_syc[layer, pos]).item()\n                scores[layer][pos].append(score)\n\n    labels_arr = np.array(labels)\n    results = {}\n    for layer in range(num_layers):\n        results[layer] = {}\n        for pos in range(num_positions):\n            scores_arr = np.array(scores[layer][pos])\n            if len(np.unique(labels_arr)) < 2:\n                results[layer][pos] = float(\"nan\")\n            else:\n                results[layer][pos] = roc_auc_score(labels_arr, scores_arr)\n\n    return results\n\n\ndef compute_cosine_per_layer(\n    d_syc: torch.Tensor, d_gen: torch.Tensor\n) -> dict[int, dict[int, float]]:\n    \"\"\"Compute cosine similarity between d_syc and d_gen per layer and token position.\"\"\"\n    num_layers = d_syc.shape[0]\n    num_positions = d_syc.shape[1]\n\n    results = {}\n    for layer in range(num_layers):\n        results[layer] = {}\n        for pos in range(num_positions):\n            cos = torch.nn.functional.cosine_similarity(\n                d_syc[layer, pos].unsqueeze(0),\n                d_gen[layer, pos].unsqueeze(0),\n            ).item()\n            results[layer][pos] = cos\n\n    return results\n\n\ndef compute_stratified_auroc(\n    samples: list[dict], d_syc: torch.Tensor, group_key: str, best_layer: int\n) -> dict[str, dict[int, float]]:\n    \"\"\"Compute AUROC broken down by a metadata field (domain, evidence_strength, etc.).\n\n    Uses the best layer only, across all token positions.\n    \"\"\"\n    num_positions = d_syc.shape[1]\n\n    groups: dict[str, list[dict]] = defaultdict(list)\n    for s in samples:\n        groups[str(s[group_key])].append(s)\n\n    results = {}\n    for group_val, group_samples in sorted(groups.items()):\n        labels = []\n        scores_by_pos: dict[int, list] = {p: [] for p in range(num_positions)}\n\n        for sample in group_samples:\n            label = 1 if sample[\"condition\"] == \"sycophantic_capitulation\" else 0\n            labels.append(label)\n            for pos in range(num_positions):\n                score = torch.dot(\n                    sample[\"activations\"][best_layer, pos], d_syc[best_layer, pos]\n                ).item()\n                scores_by_pos[pos].append(score)\n\n        labels_arr = np.array(labels)\n        if len(np.unique(labels_arr)) < 2:\n            results[group_val] = {p: float(\"nan\") for p in range(num_positions)}\n        else:\n            results[group_val] = {\n                p: roc_auc_score(labels_arr, np.array(scores_by_pos[p]))\n                for p in range(num_positions)\n            }\n\n    return results\n\n\ndef go_nogo_verdict(best_auroc: float, best_cosine: float) -> dict:\n    \"\"\"Determine Go/No-Go based on thresholds.\n\n    Criteria:\n      PASS: AUROC >= 0.85 AND cosine(d_syc, d_gen) < 0.3\n      GRAY: AUROC in [0.80, 0.85)\n      FAIL: AUROC < 0.80\n\n    Note: In the current binary setup d_gen = -d_syc, so cosine is always -1.\n    The cosine check becomes meaningful when d_gen is independently defined.\n    \"\"\"\n    cosine_ok = best_cosine < 0.3\n\n    if best_auroc >= 0.85 and cosine_ok:\n        verdict = \"PASS\"\n        reason = f\"AUROC={best_auroc:.4f} >= 0.85 and cosine={best_cosine:.4f} < 0.3\"\n    elif best_auroc >= 0.80:\n        verdict = \"GRAY\"\n        reason = f\"AUROC={best_auroc:.4f} in [0.80, 0.85); needs further investigation\"\n        if not cosine_ok:\n            reason += f\"; cosine={best_cosine:.4f} >= 0.3 (unexpected)\"\n    else:\n        verdict = \"FAIL\"\n        reason = f\"AUROC={best_auroc:.4f} < 0.80\"\n\n    return {\"verdict\": verdict, \"reason\": reason, \"auroc\": best_auroc, \"cosine\": best_cosine}\n\n\ndef main() -> None:\n    parser = argparse.ArgumentParser(\n        description=\"Evaluate contrastive direction vectors on test set.\"\n    )\n    parser.add_argument(\n        \"--directions\", required=True, help=\"Path to directions.pt from compute_directions.py\"\n    )\n    parser.add_argument(\n        \"--activations\", required=True, help=\"Path to activations.pt from extract_activations.py\"\n    )\n    parser.add_argument(\"--output-dir\", default=\".\", help=\"Output directory (default: .)\")\n    args = parser.parse_args()\n\n    logging.basicConfig(\n        level=logging.INFO,\n        format=\"%(asctime)s [%(levelname)s] %(name)s: %(message)s\",\n    )\n\n    logger.info(\"Loading directions from %s\", args.directions)\n    directions = torch.load(args.directions, map_location=\"cpu\", weights_only=False)\n    d_syc = directions[\"d_syc\"]\n    d_gen = directions[\"d_gen\"]\n    test_pair_ids = directions[\"test_pair_ids\"]\n    metadata = directions[\"metadata\"]\n\n    if not test_pair_ids:\n        logger.error(\"No test pair IDs in directions file; exiting\")\n        sys.exit(1)\n\n    test_samples = load_test_samples(args.activations, test_pair_ids)\n    if not test_samples:\n        logger.error(\"No test samples found; exiting\")\n        sys.exit(1)\n\n    # Per-layer AUROC\n    logger.info(\"Computing per-layer AUROC\")\n    auroc_per_layer = compute_auroc_per_layer(test_samples, d_syc)\n\n    # Find best layer (max AUROC across token positions)\n    best_layer = -1\n    best_auroc = -1.0\n    best_pos = -1\n    for layer, pos_dict in auroc_per_layer.items():\n        for pos, auc in pos_dict.items():\n            if not np.isnan(auc) and auc > best_auroc:\n                best_auroc = auc\n                best_layer = layer\n                best_pos = pos\n\n    logger.info(\"Best layer=%d, pos=%d, AUROC=%.4f\", best_layer, best_pos, best_auroc)\n\n    # Cosine similarity\n    logger.info(\"Computing per-layer cosine similarity\")\n    cosine_per_layer = compute_cosine_per_layer(d_syc, d_gen)\n    best_cosine = cosine_per_layer[best_layer][best_pos]\n\n    # Stratified analysis at best layer\n    logger.info(\"Computing stratified AUROC breakdown\")\n    breakdown_domain = compute_stratified_auroc(test_samples, d_syc, \"domain\", best_layer)\n    breakdown_evidence = compute_stratified_auroc(\n        test_samples, d_syc, \"evidence_strength\", best_layer\n    )\n    breakdown_turn = compute_stratified_auroc(\n        test_samples, d_syc, \"correction_turn\", best_layer\n    )\n\n    # Go/No-Go\n    verdict = go_nogo_verdict(best_auroc, best_cosine)\n\n    # Build report\n    report = {\n        \"metadata\": metadata,\n        \"num_test_samples\": len(test_samples),\n        \"num_test_pairs\": len(test_pair_ids),\n        \"best_layer\": best_layer,\n        \"best_token_position\": best_pos,\n        \"best_auroc\": best_auroc,\n        \"best_cosine\": best_cosine,\n        \"per_layer_auroc\": {\n            str(l): {str(p): v for p, v in pos_dict.items()}\n            for l, pos_dict in auroc_per_layer.items()\n        },\n        \"per_layer_cosine\": {\n            str(l): {str(p): v for p, v in pos_dict.items()}\n            for l, pos_dict in cosine_per_layer.items()\n        },\n        \"stratified_auroc\": {\n            \"by_domain\": {\n                k: {str(p): v for p, v in pos_dict.items()}\n                for k, pos_dict in breakdown_domain.items()\n            },\n            \"by_evidence_strength\": {\n                k: {str(p): v for p, v in pos_dict.items()}\n                for k, pos_dict in breakdown_evidence.items()\n            },\n            \"by_correction_turn\": {\n                k: {str(p): v for p, v in pos_dict.items()}\n                for k, pos_dict in breakdown_turn.items()\n            },\n        },\n        \"go_nogo\": verdict,\n        \"note\": (\n            \"In the current binary setup d_gen = -d_syc, so cosine(d_syc, d_gen) = -1.0. \"\n            \"The cosine threshold check (< 0.3) becomes meaningful only when d_gen is \"\n            \"independently defined.\"\n        ),\n    }\n\n    # Save JSON report\n    out_dir = Path(args.output_dir)\n    out_dir.mkdir(parents=True, exist_ok=True)\n    report_path = out_dir / \"evaluation_report.json\"\n    with open(report_path, \"w\") as f:\n        json.dump(report, f, indent=2, ensure_ascii=False)\n    logger.info(\"Saved report to %s\", report_path)\n\n    # Print human-readable summary\n    token_pos_names = {0: \"user_last\", 1: \"asst_first\"}\n    print(\"\\n\" + \"=\" * 60)\n    print(\"DIRECTION EVALUATION SUMMARY\")\n    print(\"=\" * 60)\n    print(f\"Test pairs: {len(test_pair_ids)}  |  Test samples: {len(test_samples)}\")\n    print(f\"Layers: {metadata['num_layers']}  |  Hidden dim: {metadata['hidden_dim']}\")\n    print()\n\n    print(f\"Best layer: {best_layer}  |  Token position: {best_pos} ({token_pos_names.get(best_pos, '?')})\")\n    print(f\"Best AUROC: {best_auroc:.4f}\")\n    print(f\"Cosine(d_syc, d_gen) at best: {best_cosine:.4f}  (expected: -1.0 in binary setup)\")\n    print()\n\n    # Top 5 layers\n    all_layer_auc = []\n    for layer, pos_dict in auroc_per_layer.items():\n        for pos, auc in pos_dict.items():\n            if not np.isnan(auc):\n                all_layer_auc.append((layer, pos, auc))\n    all_layer_auc.sort(key=lambda x: x[2], reverse=True)\n\n    print(\"Top 5 (layer, position, AUROC):\")\n    for layer, pos, auc in all_layer_auc[:5]:\n        print(f\"  Layer {layer:2d}, {token_pos_names.get(pos, f'pos{pos}'):10s}: {auc:.4f}\")\n    print()\n\n    # Stratified breakdown\n    print(\"AUROC by domain (best layer, all positions):\")\n    for domain, pos_dict in sorted(breakdown_domain.items()):\n        vals = [f\"{token_pos_names.get(p, f'pos{p}')}={v:.4f}\" for p, v in sorted(pos_dict.items())]\n        print(f\"  {domain:25s}  {', '.join(vals)}\")\n    print()\n\n    print(\"AUROC by evidence_strength (best layer, all positions):\")\n    for es, pos_dict in sorted(breakdown_evidence.items()):\n        vals = [f\"{token_pos_names.get(p, f'pos{p}')}={v:.4f}\" for p, v in sorted(pos_dict.items())]\n        print(f\"  {es:25s}  {', '.join(vals)}\")\n    print()\n\n    # Go/No-Go\n    print(\"-\" * 60)\n    print(f\"GO/NO-GO VERDICT: {verdict['verdict']}\")\n    print(f\"  {verdict['reason']}\")\n    print(\"=\" * 60)\n\n\nif __name__ == \"__main__\":\n    main()\n"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T06:42:27.180412+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/data/evaluate_directions.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_compute_evaluate_directions_20260518T064026",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T06:42:27.180611+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/data && python3 compute_directions.py --help",
  "description": "Verify compute_directions.py syntax"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_compute_evaluate_directions_20260518T064026",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/data && python3 compute_directions.py --help",
    "description": "Verify compute_directions.py syntax"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-18T06:42:27.180989+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/data && python3 evaluate_directions.py --help",
  "description": "Verify evaluate_directions.py syntax"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_compute_evaluate_directions_20260518T064026",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/data && python3 evaluate_directions.py --help",
    "description": "Verify evaluate_directions.py syntax"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-18T06:42:27.181712+00:00_

Exit code 1
Traceback (most recent call last):
  File "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/data/compute_directions.py", line 27, in &lt;module>
    import torch
ModuleNotFoundError: No module named 'torch'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_compute_evaluate_directions_20260518T064026",
  "tool": "Bash",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T06:42:27.181904+00:00_

&lt;tool_use_error>Cancelled: parallel tool call Bash(cd /home/ubuntu/.agent-ml-research-be-id…) errored&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_compute_evaluate_directions_20260518T064026",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-18T06:42:27.182071+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/data && python3 -c \"import py_compile; py_compile.compile('compute_directions.py', doraise=True)\" && echo \"OK\"",
  "description": "Syntax check compute_directions.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_compute_evaluate_directions_20260518T064026",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/data && python3 -c \"import py_compile; py_compile.compile('compute_directions.py', doraise=True)\" && echo \"OK\"",
    "description": "Syntax check compute_directions.py"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T06:42:27.182216+00:00_

OK

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_compute_evaluate_directions_20260518T064026",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-18T06:42:27.182960+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"import py_compile; py_compile.compile('evaluate_directions.py', doraise=True)\" && echo \"OK\"",
  "description": "Syntax check evaluate_directions.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_compute_evaluate_directions_20260518T064026",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"import py_compile; py_compile.compile('evaluate_directions.py', doraise=True)\" && echo \"OK\"",
    "description": "Syntax check evaluate_directions.py"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T06:42:27.184787+00:00_

OK

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_compute_evaluate_directions_20260518T064026",
  "tool": "Bash",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-18T06:42:27.185623+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport ast, sys\nfor f in ['compute_directions.py', 'evaluate_directions.py']:\n    tree = ast.parse(open(f).read())\n    # check argparse parse_args exists\n    src = open(f).read()\n    assert 'argparse' in src\n    assert 'parse_args' in src\n    print(f'{f}: valid')\n\"",
  "description": "Verify argparse setup in both scripts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_compute_evaluate_directions_20260518T064026",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport ast, sys\nfor f in ['compute_directions.py', 'evaluate_directions.py']:\n    tree = ast.parse(open(f).read())\n    # check argparse parse_args exists\n    src = open(f).read()\n    assert 'argparse' in src\n    assert 'parse_args' in src\n    print(f'{f}: valid')\n\"",
    "description": "Verify argparse setup in both scripts"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T06:42:27.185946+00:00_

compute_directions.py: valid
evaluate_directions.py: valid

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_compute_evaluate_directions_20260518T064026",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-18T06:42:27.186536+00:00_

两个脚本已编写完成，语法验证通过。

**compute_directions.py**：加载 Phase 2 激活 `.pt` → 按 `pair_id` 配对 → `StratifiedShuffleSplit` 按 domain 分层 80/20 划分 → 在 train set 上 difference-in-means 计算 `d_syc` 和 `d_gen` → L2 归一化 → 保存 `directions.pt`。

**evaluate_directions.py**：加载方向和激活 → 过滤 test set → per-layer/per-position AUROC（投影到 `d_syc` 的 dot product 作为分数）→ cosine(d_syc, d_gen) → 按 domain/evidence_strength/correction_turn 分层 AUROC → Go/No-Go 判定（PASS/GRAY/FAIL）→ 输出 JSON 报告 + stdout 摘要。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_compute_evaluate_directions_20260518T064026"
}
```

</details>

---
