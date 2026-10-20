# code cka fh reliability

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/chats/worker_code_cka_fh_reliability_20260515T031935.jsonl`
- **Structured JSON:** [`bca7a51c454e0f1627f3.json`](../../sessions/bc/bca7a51c454e0f1627f3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

13 recorded events

### Tool call

_source line 1 · 2026-05-15T03:25:05.192567+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/run_cka_reliability.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cka_fh_reliability_20260515T031935",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/run_cka_reliability.py"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T03:25:05.193179+00:00_

1	"""
2	CKA Reliability Analysis for RASP.
3	
4	Validates the stability of cross-model CKA scores (original vs pruned) by:
5	1. Split-half reliability: Spearman rho between CKA scores on two data halves
6	2. Calibration size sensitivity: Spearman rho at different sample sizes vs full
7	
8	Addresses Claim 2: CKA-based structural scoring is reliable and stable.
9	"""
10	
11	import argparse
12	import json
13	import logging
14	import os
15	import random
16	import sys
17	
18	import numpy as np
19	import scipy.stats as stats
20	import torch
21	from datasets import load_dataset
22	from transformers import AutoModelForCausalLM, AutoTokenizer
23	
24	logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
25	logger = logging.getLogger(__name__)
26	
27	
28	def set_seed(seed):
29	    random.seed(seed)
30	    np.random.seed(seed)
31	    torch.manual_seed(seed)
32	    torch.cuda.manual_seed_all(seed)
33	
34	
35	def linear_cka(X, Y):
36	    """Linear CKA between two activation matrices. X: [n, p], Y: [n, q]."""
37	    X = X - X.mean(0)
38	    Y = Y - Y.mean(0)
39	    hsic_xy = torch.norm(X.T @ Y, "fro") ** 2
40	    hsic_xx = torch.norm(X.T @ X, "fro") ** 2
41	    hsic_yy = torch.norm(Y.T @ Y, "fro") ** 2
42	    return (hsic_xy / (torch.sqrt(hsic_xx) * torch.sqrt(hsic_yy) + 1e-8)).item()
43	
44	
45	def load_calibration_data(tokenizer, n_samples, max_length=512, seed=42):
46	    ds = load_dataset("openai/gsm8k", "main", split="train")
47	    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))
48	    encodings = []
49	    for example in ds:
50	        prompt = f"Question: {example['question']}\nAnswer: Let me think step by step.\n"
51	        ids = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=max_length)
52	        encodings.append(ids)
53	    return encodings
54	
55	
56	def collect_qproj_activations(model, calibration_data, device):
57	    """Collect per-head q_proj activations, mean-pooled over seq length.
58	   
…[truncated 14147 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cka_fh_reliability_20260515T031935",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T03:25:05.193523+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/cka_overlap.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cka_fh_reliability_20260515T031935",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/cka_overlap.py"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T03:25:05.193965+00:00_

1	"""
2	CKA Overlap Computation for RASP.
3	
4	Computes intra-layer functional overlap F(h) for each attention head and MLP channel group
5	using linear CKA (Centered Kernel Alignment via HSIC).
6	
7	Input:  model + calibration data (GSM8K train subset)
8	Output: per-structure F(h) scores saved as dict in .pt file
9	        Keys: 'attn_overlap' (dict[layer_idx -> tensor[n_heads]]),
10	              'mlp_overlap'  (dict[layer_idx -> tensor[n_groups]])
11	"""
12	
13	import argparse
14	import logging
15	import math
16	import os
17	import random
18	
19	import numpy as np
20	import torch
21	from datasets import load_dataset
22	from transformers import AutoModelForCausalLM, AutoTokenizer
23	
24	logging.basicConfig(
25	    level=logging.INFO,
26	    format="%(asctime)s [%(levelname)s] %(message)s",
27	)
28	logger = logging.getLogger(__name__)
29	
30	
31	def set_seed(seed: int):
32	    random.seed(seed)
33	    np.random.seed(seed)
34	    torch.manual_seed(seed)
35	    torch.cuda.manual_seed_all(seed)
36	
37	
38	def linear_cka(X: torch.Tensor, Y: torch.Tensor) -> float:
39	    """Linear CKA between two activation matrices.
40	    X: [n, p], Y: [n, q]. Returns scalar similarity in [0, 1].
41	    """
42	    X = X - X.mean(0)
43	    Y = Y - Y.mean(0)
44	    hsic_xy = torch.norm(X.T @ Y, "fro") ** 2
45	    hsic_xx = torch.norm(X.T @ X, "fro") ** 2
46	    hsic_yy = torch.norm(Y.T @ Y, "fro") ** 2
47	    return (hsic_xy / (torch.sqrt(hsic_xx) * torch.sqrt(hsic_yy) + 1e-8)).item()
48	
49	
50	def load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):
51	    """Load GSM8K train questions as calibration prompts."""
52	    ds = load_dataset("openai/gsm8k", "main", split="train")
53	    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))
54	
55	    encodings = []
56	    for example in ds:
57	        prompt = f"Question: {example['question']}\nAnswer: Let me think step by step.\n"
58	        ids = tokenizer(prompt, return_tensors="pt", trun
…[truncated 9232 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cka_fh_reliability_20260515T031935",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T03:25:05.194409+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/run_cka_reliability.py",
  "content": "\"\"\"\nCKA Reliability Analysis for RASP.\n\nValidates the stability of structural scoring by:\n1-3. Cross-model CKA split-half reliability (original vs pruned, per GQA group)\n4.   F(h) split-half reliability for attention heads (intra-layer overlap)\n5.   F(h) split-half reliability for MLP groups (intra-layer overlap)\n\nPhases 1-3 address cross-model CKA stability.\nPhases 4-5 address intra-layer F(h) stability (Claim 2 core metric).\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport random\nimport sys\n\nimport numpy as np\nimport scipy.stats as stats\nimport torch\nfrom datasets import load_dataset\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\nlogging.basicConfig(level=logging.INFO, format=\"%(asctime)s [%(levelname)s] %(message)s\")\nlogger = logging.getLogger(__name__)\n\n\ndef set_seed(seed):\n    random.seed(seed)\n    np.random.seed(seed)\n    torch.manual_seed(seed)\n    torch.cuda.manual_seed_all(seed)\n\n\ndef linear_cka(X, Y):\n    \"\"\"Linear CKA between two activation matrices. X: [n, p], Y: [n, q].\"\"\"\n    X = X - X.mean(0)\n    Y = Y - Y.mean(0)\n    hsic_xy = torch.norm(X.T @ Y, \"fro\") ** 2\n    hsic_xx = torch.norm(X.T @ X, \"fro\") ** 2\n    hsic_yy = torch.norm(Y.T @ Y, \"fro\") ** 2\n    return (hsic_xy / (torch.sqrt(hsic_xx) * torch.sqrt(hsic_yy) + 1e-8)).item()\n\n\ndef load_calibration_data(tokenizer, n_samples, max_length=512, seed=42):\n    ds = load_dataset(\"openai/gsm8k\", \"main\", split=\"train\")\n    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))\n    encodings = []\n    for example in ds:\n        prompt = f\"Question: {example['question']}\\nAnswer: Let me think step by step.\\n\"\n        ids = tokenizer(prompt, return_tensors=\"pt\", truncation=True, max_length=max_length)\n        encodings.append(ids)\n    return encodings\n\n\ndef collect_qproj_activations(model, calibration_data, device):\n    \"\"\"Collect per-head q_proj activations, mean-pooled over seq length.\n    Returns dict[layer_idx] -> tensor[n_samples, n_heads_in_layer, head_dim] on CPU float32.\n    \"\"\"\n    n_layers = model.config.num_hidden_layers\n    head_dim = model.config.hidden_size // model.config.num_attention_heads\n\n    q_outputs = {i: [] for i in range(n_layers)}\n    hooks = []\n\n    def make_hook(layer_idx):\n        def fn(module, inp, out):\n            q_outputs[layer_idx].append(out.detach().cpu())\n        return fn\n\n    for i in range(n_layers):\n        h = model.model.layers[i].self_attn.q_proj.register_forward_hook(make_hook(i))\n        hooks.append(h)\n\n    model.eval()\n    with torch.no_grad():\n        for idx, enc in enumerate(calibration_data):\n            input_ids = enc[\"input_ids\"].to(device)\n            attention_mask = enc[\"attention_mask\"].to(device)\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\n            if (idx + 1) % 200 == 0:\n                logger.info(f\"  Forward pass {idx + 1}/{len(calibration_data)}\")\n\n    for h in hooks:\n        h.remove()\n\n    activations = {}\n    for layer_idx in range(n_layers):\n        out_dim = q_outputs[layer_idx][0].squeeze(0).shape[-1]\n        n_heads = out_dim // head_dim\n        per_head = []\n        for t in q_outputs[layer_idx]:\n            t = t.squeeze(0)  # [seq, n_heads * head_dim]\n            t = t.view(t.shape[0], n_heads, head_dim)  # [seq, n_heads, head_dim]\n            t = t.mean(dim=0)  # [n_heads, head_dim]\n            per_head.append(t)\n        activations[layer_idx] = torch.stack(per_head, dim=0).float()\n        q_outputs[layer_idx] = None\n\n    return activations\n\n\ndef collect_mlp_activations(model, calibration_data, device, n_groups=28):\n    \"\"\"Collect MLP gate_proj activations grouped into channel groups.\n    Returns dict[layer_idx] -> tensor[n_samples, n_groups, group_dim] on CPU float32.\n    \"\"\"\n    n_layers = model.config.num_hidden_layers\n    intermediate_size = model.config.intermediate_size\n    group_size = intermediate_size // n_groups\n\n    gate_outputs = {i: [] for i in range(n_layers)}\n    hooks = []\n\n    def make_hook(layer_idx):\n        def fn(module, inp, out):\n            gate_outputs[layer_idx].append(out.detach().cpu())\n        return fn\n\n    for i in range(n_layers):\n        h = model.model.layers[i].mlp.gate_proj.register_forward_hook(make_hook(i))\n        hooks.append(h)\n\n    model.eval()\n    with torch.no_grad():\n        for idx, enc in enumerate(calibration_data):\n            input_ids = enc[\"input_ids\"].to(device)\n            attention_mask = enc[\"attention_mask\"].to(device)\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\n            if (idx + 1) % 200 == 0:\n                logger.info(f\"  Forward pass {idx + 1}/{len(calibration_data)}\")\n\n    for h in hooks:\n        h.remove()\n\n    activations = {}\n    for layer_idx in range(n_layers):\n        per_group = []\n        for t in gate_outputs[layer_idx]:\n            t = t.squeeze(0)  # [seq, intermediate_size]\n            t = t.mean(dim=0)  # [intermediate_size]\n            usable = n_groups * group_size\n            t = t[:usable].view(n_groups, group_size)\n            per_group.append(t)\n        activations[layer_idx] = torch.stack(per_group, dim=0).float()\n        gate_outputs[layer_idx] = None\n\n    return activations\n\n\ndef load_pruned_model_with_meta(base_model_path, pruned_model_path, torch_dtype, device):\n    \"\"\"Load structurally pruned model via base model reconstruction + saved weights.\"\"\"\n    meta_path = os.path.join(pruned_model_path, \"pruning_metadata.pt\")\n    pruning_meta = torch.load(meta_path, map_location=\"cpu\", weights_only=True)\n\n    src_dir = os.path.dirname(os.path.abspath(__file__))\n    if src_dir not in sys.path:\n        sys.path.insert(0, src_dir)\n    from prune import prune_attention_heads, prune_mlp_channels\n\n    logging.getLogger(\"prune\").setLevel(logging.WARNING)\n    model = AutoModelForCausalLM.from_pretrained(\n        base_model_path, torch_dtype=torch_dtype, device_map=\"cpu\", trust_remote_code=True\n    )\n    prune_attention_heads(model, pruning_meta[\"attn_keep_masks\"])\n    prune_mlp_channels(model, pruning_meta[\"mlp_keep_masks\"])\n\n    safetensor_files = sorted(\n        [f for f in os.listdir(pruned_model_path) if f.endswith(\".safetensors\")]\n    )\n    if safetensor_files:\n        from safetensors.torch import load_file\n        state_dict = {}\n        for f in safetensor_files:\n            state_dict.update(load_file(os.path.join(pruned_model_path, f)))\n    else:\n        state_dict = torch.load(\n            os.path.join(pruned_model_path, \"pytorch_model.bin\"),\n            map_location=\"cpu\", weights_only=True,\n        )\n    model.load_state_dict(state_dict)\n    model.to(device)\n    return model, pruning_meta\n\n\ndef compute_group_cka(orig_acts, pruned_acts, keep_masks, n_heads_orig, n_kv_heads,\n                      sample_indices=None):\n    \"\"\"Compute per-GQA-group CKA between original and pruned representations.\n\n    For each KV group, concatenates retained Q head activations from both models\n    and computes linear CKA. Original uses all Q heads in the group, pruned uses\n    only retained Q heads (CKA handles different feature dimensions).\n\n    Returns dict[(layer, group)] -> float (or NaN if group fully pruned).\n    \"\"\"\n    heads_per_kv = n_heads_orig // n_kv_heads\n    n_layers = len(orig_acts)\n    scores = {}\n\n    for layer_idx in range(n_layers):\n        orig_layer = orig_acts[layer_idx]   # [N, n_heads_orig, head_dim]\n        pruned_layer = pruned_acts[layer_idx]  # [N, n_retained, head_dim]\n        retained = keep_masks[layer_idx]\n\n        if sample_indices is not None:\n            orig_layer = orig_layer[sample_indices]\n            pruned_layer = pruned_layer[sample_indices]\n\n        for g in range(n_kv_heads):\n            orig_head_range = list(range(g * heads_per_kv, (g + 1) * heads_per_kv))\n            pruned_positions = [i for i, h in enumerate(retained) if h in orig_head_range]\n\n            if not pruned_positions:\n                scores[(layer_idx, g)] = float(\"nan\")\n                continue\n\n            n = orig_layer.shape[0]\n            orig_flat = orig_layer[:, orig_head_range, :].reshape(n, -1)\n            pruned_flat = pruned_layer[:, pruned_positions, :].reshape(n, -1)\n            scores[(layer_idx, g)] = linear_cka(orig_flat, pruned_flat)\n\n    return scores\n\n\ndef scores_to_aligned_arrays(scores_a, scores_b):\n    \"\"\"Extract aligned non-NaN value arrays from two score dicts.\"\"\"\n    common = sorted(set(scores_a.keys()) & set(scores_b.keys()))\n    a_vals, b_vals = [], []\n    for k in common:\n        va, vb = scores_a[k], scores_b[k]\n        if (isinstance(va, float) and va != va) or (isinstance(vb, float) and vb != vb):\n            continue\n        a_vals.append(va)\n        b_vals.append(vb)\n    return np.array(a_vals), np.array(b_vals)\n\n\ndef compute_fh_scores(acts_dict, sample_indices=None):\n    \"\"\"Compute intra-layer F(h) for each structure.\n    acts_dict: dict[layer_idx] -> tensor[n_samples, n_structs, dim]\n    Returns dict[layer_idx] -> tensor[n_structs] of F(h) values.\n    \"\"\"\n    fh = {}\n    for layer_idx, acts in acts_dict.items():\n        if sample_indices is not None:\n            acts = acts[sample_indices]\n        n_samples, n_structs, dim = acts.shape\n        matrix = torch.zeros(n_structs, n_structs)\n        for i in range(n_structs):\n            matrix[i, i] = 1.0\n            for j in range(i + 1, n_structs):\n                val = linear_cka(acts[:, i, :].float(), acts[:, j, :].float())\n                matrix[i, j] = val\n                matrix[j, i] = val\n        scores = (matrix.sum(dim=1) - 1.0) / max(n_structs - 1, 1)\n        fh[layer_idx] = scores\n    return fh\n\n\ndef compute_fh_reliability(acts_dict, n_splits, seed, structure_name):\n    \"\"\"Split-half reliability of F(h) rankings across all layers.\n    Returns list of per-split result dicts with Spearman rho.\n    \"\"\"\n    n_total = next(iter(acts_dict.values())).shape[0]\n    split_results = []\n    for i in range(n_splits):\n        rng = np.random.RandomState(seed + i)\n        perm = rng.permutation(n_total)\n        half = n_total // 2\n        idx_a = sorted(perm[:half].tolist())\n        idx_b = sorted(perm[half:2 * half].tolist())\n\n        logger.info(f\"  Split {i}: computing F(h) on half A ({len(idx_a)} samples)...\")\n        fh_a = compute_fh_scores(acts_dict, idx_a)\n        logger.info(f\"  Split {i}: computing F(h) on half B ({len(idx_b)} samples)...\")\n        fh_b = compute_fh_scores(acts_dict, idx_b)\n\n        vals_a, vals_b = [], []\n        for layer_idx in sorted(fh_a.keys()):\n            vals_a.extend(fh_a[layer_idx].tolist())\n            vals_b.extend(fh_b[layer_idx].tolist())\n\n        rho, p = stats.spearmanr(vals_a, vals_b)\n        split_results.append({\"split\": i, \"rho\": float(rho), \"p_value\": float(p),\n                              \"n_structures\": len(vals_a)})\n        logger.info(f\"  Split {i} {structure_name}: rho={rho:.4f}, p={p:.2e}, n={len(vals_a)}\")\n    return split_results\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"CKA Reliability Analysis for RASP scoring\")\n    parser.add_argument(\"--original_model\", type=str, required=True)\n    parser.add_argument(\"--pruned_model\", type=str, default=None)\n    parser.add_argument(\"--gpu_id\", type=int, default=0)\n    parser.add_argument(\"--num_samples\", type=int, default=1024)\n    parser.add_argument(\"--max_length\", type=int, default=512)\n    parser.add_argument(\"--n_splits\", type=int, default=5)\n    parser.add_argument(\"--output\", type=str, required=True)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--dtype\", type=str, default=\"bfloat16\",\n                        choices=[\"float16\", \"bfloat16\", \"float32\"])\n    parser.add_argument(\"--mlp_groups\", type=int, default=28,\n                        help=\"Number of MLP channel groups per layer\")\n    parser.add_argument(\"--skip_cross_model\", action=\"store_true\",\n                        help=\"Skip Phase 1-3 (cross-model CKA); only run F(h) reliability\")\n    args = parser.parse_args()\n\n    if not args.skip_cross_model and not args.pruned_model:\n        parser.error(\"--pruned_model is required unless --skip_cross_model is set\")\n\n    set_seed(args.seed)\n    device = torch.device(f\"cuda:{args.gpu_id}\" if torch.cuda.is_available() else \"cpu\")\n    torch_dtype = {\"float16\": torch.float16, \"bfloat16\": torch.bfloat16,\n                   \"float32\": torch.float32}[args.dtype]\n\n    logger.info(\"Loading tokenizer and calibration data...\")\n    tokenizer = AutoTokenizer.from_pretrained(args.original_model, trust_remote_code=True)\n    calibration_data = load_calibration_data(tokenizer, args.num_samples, args.max_length,\n                                             args.seed)\n    n_total = len(calibration_data)\n    logger.info(f\"Loaded {n_total} calibration samples\")\n\n    # --- Load original model and collect all activations ---\n    logger.info(\"Loading original model...\")\n    orig_model = AutoModelForCausalLM.from_pretrained(\n        args.original_model, torch_dtype=torch_dtype, device_map=device, trust_remote_code=True\n    )\n    config = orig_model.config\n    n_heads_orig = config.num_attention_heads\n    n_kv_heads = config.num_key_value_heads\n    n_layers = config.num_hidden_layers\n    heads_per_kv = n_heads_orig // n_kv_heads\n    logger.info(f\"Architecture: {n_layers}L x {n_heads_orig}Q x {n_kv_heads}KV \"\n                f\"({heads_per_kv} Q/KV group, {n_layers * n_kv_heads} total groups)\")\n\n    logger.info(\"Collecting original model q_proj activations...\")\n    orig_acts = collect_qproj_activations(orig_model, calibration_data, device)\n\n    logger.info(\"Collecting original model MLP gate_proj activations...\")\n    orig_mlp_acts = collect_mlp_activations(orig_model, calibration_data, device, args.mlp_groups)\n\n    del orig_model\n    torch.cuda.empty_cache()\n    logger.info(\"Original model freed. All activations cached on CPU.\")\n\n    output = {\n        \"config\": {\n            \"original_model\": args.original_model,\n            \"num_samples\": n_total,\n            \"n_layers\": n_layers,\n            \"n_heads_original\": n_heads_orig,\n            \"n_kv_heads\": n_kv_heads,\n            \"heads_per_kv\": heads_per_kv,\n            \"total_gqa_groups\": n_layers * n_kv_heads,\n            \"mlp_groups\": args.mlp_groups,\n            \"seed\": args.seed,\n        },\n    }\n\n    # --- Phase 1-3: Cross-model CKA (optional) ---\n    if not args.skip_cross_model:\n        logger.info(\"Loading pruned model...\")\n        pruned_model, pruning_meta = load_pruned_model_with_meta(\n            args.original_model, args.pruned_model, torch_dtype, device\n        )\n        keep_masks = pruning_meta[\"attn_keep_masks\"]\n        logger.info(\"Collecting pruned model activations...\")\n        pruned_acts = collect_qproj_activations(pruned_model, calibration_data, device)\n        del pruned_model\n        torch.cuda.empty_cache()\n        logger.info(\"Pruned model freed.\")\n\n        # Phase 1: Full CKA scores\n        logger.info(\"=\" * 50)\n        logger.info(\"Phase 1: Full CKA scores (N=%d)...\", n_total)\n        full_scores = compute_group_cka(orig_acts, pruned_acts, keep_masks,\n                                        n_heads_orig, n_kv_heads)\n        valid_scores = {k: v for k, v in full_scores.items()\n                        if not (isinstance(v, float) and v != v)}\n        vals = np.array(list(valid_scores.values()))\n        logger.info(f\"Valid groups: {len(valid_scores)}/{n_layers * n_kv_heads}\")\n        logger.info(f\"CKA: mean={vals.mean():.4f}, std={vals.std():.4f}, \"\n                    f\"range=[{vals.min():.4f}, {vals.max():.4f}]\")\n\n        # Phase 2: Split-half reliability (cross-model)\n        logger.info(\"=\" * 50)\n        logger.info(\"Phase 2: Split-half reliability (%d splits)...\", args.n_splits)\n        cross_split_results = []\n        for i in range(args.n_splits):\n            rng = np.random.RandomState(args.seed + i)\n            perm = rng.permutation(n_total)\n            half = n_total // 2\n            idx_a = sorted(perm[:half].tolist())\n            idx_b = sorted(perm[half:2 * half].tolist())\n\n            scores_a = compute_group_cka(orig_acts, pruned_acts, keep_masks,\n                                         n_heads_orig, n_kv_heads, idx_a)\n            scores_b = compute_group_cka(orig_acts, pruned_acts, keep_masks,\n                                         n_heads_orig, n_kv_heads, idx_b)\n            arr_a, arr_b = scores_to_aligned_arrays(scores_a, scores_b)\n            rho, p = stats.spearmanr(arr_a, arr_b)\n            cross_split_results.append({\"split\": i, \"rho\": float(rho), \"p_value\": float(p),\n                                        \"n_groups\": len(arr_a)})\n            logger.info(f\"  Split {i}: rho={rho:.4f}, p={p:.2e}\")\n\n        cross_mean_rho = float(np.mean([r[\"rho\"] for r in cross_split_results]))\n        cross_std_rho = float(np.std([r[\"rho\"] for r in cross_split_results]))\n\n        # Phase 3: Calibration size sensitivity\n        logger.info(\"=\" * 50)\n        logger.info(\"Phase 3: Calibration size sensitivity...\")\n        size_results = []\n        for n_sub in [128, 256, 512]:\n            if n_sub >= n_total:\n                continue\n            rng = np.random.RandomState(args.seed)\n            sub_idx = sorted(rng.permutation(n_total)[:n_sub].tolist())\n\n            sub_scores = compute_group_cka(orig_acts, pruned_acts, keep_masks,\n                                           n_heads_orig, n_kv_heads, sub_idx)\n            ref_vals, sub_vals = scores_to_aligned_arrays(full_scores, sub_scores)\n            rho, p = stats.spearmanr(ref_vals, sub_vals)\n            size_results.append({\"n_samples\": n_sub, \"rho_vs_full\": float(rho),\n                                 \"p_value\": float(p)})\n            logger.info(f\"  N={n_sub}: rho={rho:.4f} vs N={n_total}\")\n\n        del pruned_acts\n        torch.cuda.empty_cache()\n\n        per_group = {}\n        for (l, g), v in full_scores.items():\n            key = f\"layer{l}_group{g}\"\n            per_group[key] = None if (isinstance(v, float) and v != v) else float(v)\n\n        output[\"config\"][\"pruned_model\"] = args.pruned_model\n        output[\"config\"][\"valid_gqa_groups\"] = len(valid_scores)\n        output[\"per_group_cka_scores\"] = per_group\n        output[\"cka_summary\"] = {\n            \"mean\": float(vals.mean()),\n            \"std\": float(vals.std()),\n            \"min\": float(vals.min()),\n            \"max\": float(vals.max()),\n            \"median\": float(np.median(vals)),\n        }\n        output[\"split_half_reliability\"] = {\n            \"per_split\": cross_split_results,\n            \"mean_rho\": cross_mean_rho,\n            \"std_rho\": cross_std_rho,\n            \"pass\": cross_mean_rho > 0.9,\n        }\n        output[\"size_sensitivity\"] = {\n            \"reference_n\": n_total,\n            \"per_size\": size_results,\n            \"all_pass_0.9\": all(s[\"rho_vs_full\"] > 0.9 for s in size_results),\n        }\n\n    # --- Phase 4: F(h) attention head split-half reliability ---\n    logger.info(\"=\" * 50)\n    logger.info(\"Phase 4: F(h) attention head split-half reliability (%d splits)...\",\n                args.n_splits)\n    attn_fh_results = compute_fh_reliability(orig_acts, args.n_splits, args.seed, \"attn_heads\")\n    attn_mean_rho = float(np.mean([r[\"rho\"] for r in attn_fh_results]))\n    attn_std_rho = float(np.std([r[\"rho\"] for r in attn_fh_results]))\n    attn_pass = attn_mean_rho > 0.9\n    logger.info(f\"Attn F(h) reliability: mean_rho={attn_mean_rho:.4f} +/- {attn_std_rho:.4f} \"\n                f\"{'PASS' if attn_pass else 'FAIL'}\")\n\n    output[\"fh_attn_reliability\"] = {\n        \"per_split\": attn_fh_results,\n        \"mean_rho\": attn_mean_rho,\n        \"std_rho\": attn_std_rho,\n        \"pass\": attn_pass,\n    }\n\n    del orig_acts\n    torch.cuda.empty_cache()\n\n    # --- Phase 5: F(h) MLP group split-half reliability ---\n    logger.info(\"=\" * 50)\n    logger.info(\"Phase 5: F(h) MLP group split-half reliability (%d splits)...\", args.n_splits)\n    mlp_fh_results = compute_fh_reliability(orig_mlp_acts, args.n_splits, args.seed, \"mlp_groups\")\n    mlp_mean_rho = float(np.mean([r[\"rho\"] for r in mlp_fh_results]))\n    mlp_std_rho = float(np.std([r[\"rho\"] for r in mlp_fh_results]))\n    mlp_pass = mlp_mean_rho > 0.9\n    logger.info(f\"MLP F(h) reliability: mean_rho={mlp_mean_rho:.4f} +/- {mlp_std_rho:.4f} \"\n                f\"{'PASS' if mlp_pass else 'FAIL'}\")\n\n    output[\"fh_mlp_reliability\"] = {\n        \"per_split\": mlp_fh_results,\n        \"mean_rho\": mlp_mean_rho,\n        \"std_rho\": mlp_std_rho,\n        \"pass\": mlp_pass,\n    }\n\n    del orig_mlp_acts\n    torch.cuda.empty_cache()\n\n    # --- Save results ---\n    os.makedirs(os.path.dirname(args.output) or \".\", exist_ok=True)\n    with open(args.output, \"w\") as f:\n        json.dump(output, f, indent=2)\n    logger.info(f\"Results saved to {args.output}\")\n\n    # --- Print summary ---\n    print(f\"\\n{'=' * 60}\")\n    print(\"CKA Reliability Analysis\")\n    print(f\"{'=' * 60}\")\n\n    if not args.skip_cross_model:\n        print(f\"\\nCross-model CKA (Phase 1-3):\")\n        print(f\"  GQA groups: {len(valid_scores)}/{n_layers * n_kv_heads} valid\")\n        print(f\"  CKA scores: {vals.mean():.4f} +/- {vals.std():.4f} \"\n              f\"[{vals.min():.4f}, {vals.max():.4f}]\")\n        sh_pass = \"PASS\" if cross_mean_rho > 0.9 else \"FAIL\"\n        print(f\"  Split-half reliability ({args.n_splits} splits):\")\n        print(f\"    rho = {cross_mean_rho:.4f} +/- {cross_std_rho:.4f}  {sh_pass} \"\n              f\"(threshold: 0.9)\")\n        for r in cross_split_results:\n            print(f\"      Split {r['split']}: rho={r['rho']:.4f}\")\n        print(f\"  Size sensitivity (vs N={n_total}):\")\n        for s in size_results:\n            sv = \"PASS\" if s[\"rho_vs_full\"] > 0.9 else \"FAIL\"\n            print(f\"    N={s['n_samples']:4d}: rho={s['rho_vs_full']:.4f}  {sv}\")\n\n    print(f\"\\nF(h) Attention head reliability (Phase 4):\")\n    ah_label = \"PASS\" if attn_pass else \"FAIL\"\n    print(f\"  rho = {attn_mean_rho:.4f} +/- {attn_std_rho:.4f}  {ah_label} (threshold: 0.9)\")\n    for r in attn_fh_results:\n        print(f\"    Split {r['split']}: rho={r['rho']:.4f}\")\n\n    print(f\"\\nF(h) MLP group reliability (Phase 5):\")\n    mh_label = \"PASS\" if mlp_pass else \"FAIL\"\n    print(f\"  rho = {mlp_mean_rho:.4f} +/- {mlp_std_rho:.4f}  {mh_label} (threshold: 0.9)\")\n    for r in mlp_fh_results:\n        print(f\"    Split {r['split']}: rho={r['rho']:.4f}\")\n\n    print(f\"{'=' * 60}\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cka_fh_reliability_20260515T031935",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/run_cka_reliability.py",
    "content": "\"\"\"\nCKA Reliability Analysis for RASP.\n\nValidates the stability of structural scoring by:\n1-3. Cross-model CKA split-half reliability (original vs pruned, per GQA group)\n4.   F(h) split-half reliability for attention heads (intra-layer overlap)\n5.   F(h) split-half reliability for MLP groups (intra-layer overlap)\n\nPhases 1-3 address cross-model CKA stability.\nPhases 4-5 address intra-layer F(h) stability (Claim 2 core metric).\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport random\nimport sys\n\nimport numpy as np\nimport scipy.stats as stats\nimport torch\nfrom datasets import load_dataset\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\nlogging.basicConfig(level=logging.INFO, format=\"%(asctime)s [%(levelname)s] %(message)s\")\nlogger = logging.getLogger(__name__)\n\n\ndef set_seed(seed):\n    random.seed(seed)\n    np.random.seed(seed)\n    torch.manual_seed(seed)\n    torch.cuda.manual_seed_all(seed)\n\n\ndef linear_cka(X, Y):\n    \"\"\"Linear CKA between two activation matrices. X: [n, p], Y: [n, q].\"\"\"\n    X = X - X.mean(0)\n    Y = Y - Y.mean(0)\n    hsic_xy = torch.norm(X.T @ Y, \"fro\") ** 2\n    hsic_xx = torch.norm(X.T @ X, \"fro\") ** 2\n    hsic_yy = torch.norm(Y.T @ Y, \"fro\") ** 2\n    return (hsic_xy / (torch.sqrt(hsic_xx) * torch.sqrt(hsic_yy) + 1e-8)).item()\n\n\ndef load_calibration_data(tokenizer, n_samples, max_length=512, seed=42):\n    ds = load_dataset(\"openai/gsm8k\", \"main\", split=\"train\")\n    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))\n    encodings = []\n    for example in ds:\n        prompt = f\"Question: {example['question']}\\nAnswer: Let me think step by step.\\n\"\n        ids = tokenizer(prompt, return_tensors=\"pt\", truncation=True, max_length=max_length)\n        encodings.append(ids)\n    return encodings\n\n\ndef collect_qproj_activations(model, calibration_data, device):\n    \"\"\"Collect per-head q_proj activations, mean-pooled over seq length.\n    Returns dict[layer_idx] -> tensor[n_samples, n_heads_in_layer, head_dim] on CPU float32.\n    \"\"\"\n    n_layers = model.config.num_hidden_layers\n    head_dim = model.config.hidden_size // model.config.num_attention_heads\n\n    q_outputs = {i: [] for i in range(n_layers)}\n    hooks = []\n\n    def make_hook(layer_idx):\n        def fn(module, inp, out):\n            q_outputs[layer_idx].append(out.detach().cpu())\n        return fn\n\n    for i in range(n_layers):\n        h = model.model.layers[i].self_attn.q_proj.register_forward_hook(make_hook(i))\n        hooks.append(h)\n\n    model.eval()\n    with torch.no_grad():\n        for idx, enc in enumerate(calibration_data):\n            input_ids = enc[\"input_ids\"].to(device)\n            attention_mask = enc[\"attention_mask\"].to(device)\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\n            if (idx + 1) % 200 == 0:\n                logger.info(f\"  Forward pass {idx + 1}/{len(calibration_data)}\")\n\n    for h in hooks:\n        h.remove()\n\n    activations = {}\n    for layer_idx in range(n_layers):\n        out_dim = q_outputs[layer_idx][0].squeeze(0).shape[-1]\n        n_heads = out_dim // head_dim\n        per_head = []\n        for t in q_outputs[layer_idx]:\n            t = t.squeeze(0)  # [seq, n_heads * head_dim]\n            t = t.view(t.shape[0], n_heads, head_dim)  # [seq, n_heads, head_dim]\n            t = t.mean(dim=0)  # [n_heads, head_dim]\n            per_head.append(t)\n        activations[layer_idx] = torch.stack(per_head, dim=0).float()\n        q_outputs[layer_idx] = None\n\n    return activations\n\n\ndef collect_mlp_activations(model, calibration_data, device, n_groups=28):\n    \"\"\"Collect MLP gate_proj activations grouped into channel groups.\n    Returns dict[layer_idx] -> tensor[n_samples, n_groups, group_dim] on CPU float32.\n    \"\"\"\n    n_layers = model.config.num_hidden_layers\n    intermediate_size = model.config.intermediate_size\n    group_size = intermediate_size // n_groups\n\n    gate_outputs = {i: [] for i in range(n_layers)}\n    hooks = []\n\n    def make_hook(layer_idx):\n        def fn(module, inp, out):\n            gate_outputs[layer_idx].append(out.detach().cpu())\n        return fn\n\n    for i in range(n_layers):\n        h = model.model.layers[i].mlp.gate_proj.register_forward_hook(make_hook(i))\n        hooks.append(h)\n\n    model.eval()\n    with torch.no_grad():\n        for idx, enc in enumerate(calibration_data):\n            input_ids = enc[\"input_ids\"].to(device)\n            attention_mask = enc[\"attention_mask\"].to(device)\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\n            if (idx + 1) % 200 == 0:\n                logger.info(f\"  Forward pass {idx + 1}/{len(calibration_data)}\")\n\n    for h in hooks:\n        h.remove()\n\n    activations = {}\n    for layer_idx in range(n_layers):\n        per_group = []\n        for t in gate_outputs[layer_idx]:\n            t = t.squeeze(0)  # [seq, intermediate_size]\n            t = t.mean(dim=0)  # [intermediate_size]\n            usable = n_groups * group_size\n            t = t[:usable].view(n_groups, group_size)\n            per_group.append(t)\n        activations[layer_idx] = torch.stack(per_group, dim=0).float()\n        gate_outputs[layer_idx] = None\n\n    return activations\n\n\ndef load_pruned_model_with_meta(base_model_path, pruned_model_path, torch_dtype, device):\n    \"\"\"Load structurally pruned model via base model reconstruction + saved weights.\"\"\"\n    meta_path = os.path.join(pruned_model_path, \"pruning_metadata.pt\")\n    pruning_meta = torch.load(meta_path, map_location=\"cpu\", weights_only=True)\n\n    src_dir = os.path.dirname(os.path.abspath(__file__))\n    if src_dir not in sys.path:\n        sys.path.insert(0, src_dir)\n    from prune import prune_attention_heads, prune_mlp_channels\n\n    logging.getLogger(\"prune\").setLevel(logging.WARNING)\n    model = AutoModelForCausalLM.from_pretrained(\n        base_model_path, torch_dtype=torch_dtype, device_map=\"cpu\", trust_remote_code=True\n    )\n    prune_attention_heads(model, pruning_meta[\"attn_keep_masks\"])\n    prune_mlp_channels(model, pruning_meta[\"mlp_keep_masks\"])\n\n    safetensor_files = sorted(\n        [f for f in os.listdir(pruned_model_path) if f.endswith(\".safetensors\")]\n    )\n    if safetensor_files:\n        from safetensors.torch import load_file\n        state_dict = {}\n        for f in safetensor_files:\n            state_dict.update(load_file(os.path.join(pruned_model_path, f)))\n    else:\n        state_dict = torch.load(\n            os.path.join(pruned_model_path, \"pytorch_model.bin\"),\n            map_location=\"cpu\", weights_only=True,\n        )\n    model.load_state_dict(state_dict)\n    model.to(device)\n    return model, pruning_meta\n\n\ndef compute_group_cka(orig_acts, pruned_acts, keep_masks, n_heads_orig, n_kv_heads,\n                      sample_indices=None):\n    \"\"\"Compute per-GQA-group CKA between original and pruned representations.\n\n    For each KV group, concatenates retained Q head activations from both models\n    and computes linear CKA. Original uses all Q heads in the group, pruned uses\n    only retained Q heads (CKA handles different feature dimensions).\n\n    Returns dict[(layer, group)] -> float (or NaN if group fully pruned).\n    \"\"\"\n    heads_per_kv = n_heads_orig // n_kv_heads\n    n_layers = len(orig_acts)\n    scores = {}\n\n    for layer_idx in range(n_layers):\n        orig_layer = orig_acts[layer_idx]   # [N, n_heads_orig, head_dim]\n        pruned_layer = pruned_acts[layer_idx]  # [N, n_retained, head_dim]\n        retained = keep_masks[layer_idx]\n\n        if sample_indices is not None:\n            orig_layer = orig_layer[sample_indices]\n            pruned_layer = pruned_layer[sample_indices]\n\n        for g in range(n_kv_heads):\n            orig_head_range = list(range(g * heads_per_kv, (g + 1) * heads_per_kv))\n            pruned_positions = [i for i, h in enumerate(retained) if h in orig_head_range]\n\n            if not pruned_positions:\n                scores[(layer_idx, g)] = float(\"nan\")\n                continue\n\n            n = orig_layer.shape[0]\n            orig_flat = orig_layer[:, orig_head_range, :].reshape(n, -1)\n            pruned_flat = pruned_layer[:, pruned_positions, :].reshape(n, -1)\n            scores[(layer_idx, g)] = linear_cka(orig_flat, pruned_flat)\n\n    return scores\n\n\ndef scores_to_aligned_arrays(scores_a, scores_b):\n    \"\"\"Extract aligned non-NaN value arrays from two score dicts.\"\"\"\n    common = sorted(set(scores_a.keys()) & set(scores_b.keys()))\n    a_vals, b_vals = [], []\n    for k in common:\n        va, vb = scores_a[k], scores_b[k]\n        if (isinstance(va, float) and va != va) or (isinstance(vb, float) and vb != vb):\n            continue\n        a_vals.append(va)\n        b_vals.append(vb)\n    return np.array(a_vals), np.array(b_vals)\n\n\ndef compute_fh_scores(acts_dict, sample_indices=None):\n    \"\"\"Compute intra-layer F(h) for each structure.\n    acts_dict: dict[layer_idx] -> tensor[n_samples, n_structs, dim]\n    Returns dict[layer_idx] -> tensor[n_structs] of F(h) values.\n    \"\"\"\n    fh = {}\n    for layer_idx, acts in acts_dict.items():\n        if sample_indices is not None:\n            acts = acts[sample_indices]\n        n_samples, n_structs, dim = acts.shape\n        matrix = torch.zeros(n_structs, n_structs)\n        for i in range(n_structs):\n            matrix[i, i] = 1.0\n            for j in range(i + 1, n_structs):\n                val = linear_cka(acts[:, i, :].float(), acts[:, j, :].float())\n                matrix[i, j] = val\n                matrix[j, i] = val\n        scores = (matrix.sum(dim=1) - 1.0) / max(n_structs - 1, 1)\n        fh[layer_idx] = scores\n    return fh\n\n\ndef compute_fh_reliability(acts_dict, n_splits, seed, structure_name):\n    \"\"\"Split-half reliability of F(h) rankings across all layers.\n    Returns list of per-split result dicts with Spearman rho.\n    \"\"\"\n    n_total = next(iter(acts_dict.values())).shape[0]\n    split_results = []\n    for i in range(n_splits):\n        rng = np.random.RandomState(seed + i)\n        perm = rng.permutation(n_total)\n        half = n_total // 2\n        idx_a = sorted(perm[:half].tolist())\n        idx_b = sorted(perm[half:2 * half].tolist())\n\n        logger.info(f\"  Split {i}: computing F(h) on half A ({len(idx_a)} samples)...\")\n        fh_a = compute_fh_scores(acts_dict, idx_a)\n        logger.info(f\"  Split {i}: computing F(h) on half B ({len(idx_b)} samples)...\")\n        fh_b = compute_fh_scores(acts_dict, idx_b)\n\n        vals_a, vals_b = [], []\n        for layer_idx in sorted(fh_a.keys()):\n            vals_a.extend(fh_a[layer_idx].tolist())\n            vals_b.extend(fh_b[layer_idx].tolist())\n\n        rho, p = stats.spearmanr(vals_a, vals_b)\n        split_results.append({\"split\": i, \"rho\": float(rho), \"p_value\": float(p),\n                              \"n_structures\": len(vals_a)})\n        logger.info(f\"  Split {i} {structure_name}: rho={rho:.4f}, p={p:.2e}, n={len(vals_a)}\")\n    return split_results\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"CKA Reliability Analysis for RASP scoring\")\n    parser.add_argument(\"--original_model\", type=str, required=True)\n    parser.add_argument(\"--pruned_model\", type=str, default=None)\n    parser.add_argument(\"--gpu_id\", type=int, default=0)\n    parser.add_argument(\"--num_samples\", type=int, default=1024)\n    parser.add_argument(\"--max_length\", type=int, default=512)\n    parser.add_argument(\"--n_splits\", type=int, default=5)\n    parser.add_argument(\"--output\", type=str, required=True)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--dtype\", type=str, default=\"bfloat16\",\n                        choices=[\"float16\", \"bfloat16\", \"float32\"])\n    parser.add_argument(\"--mlp_groups\", type=int, default=28,\n                        help=\"Number of MLP channel groups per layer\")\n    parser.add_argument(\"--skip_cross_model\", action=\"store_true\",\n                        help=\"Skip Phase 1-3 (cross-model CKA); only run F(h) reliability\")\n    args = parser.parse_args()\n\n    if not args.skip_cross_model and not args.pruned_model:\n        parser.error(\"--pruned_model is required unless --skip_cross_model is set\")\n\n    set_seed(args.seed)\n    device = torch.device(f\"cuda:{args.gpu_id}\" if torch.cuda.is_available() else \"cpu\")\n    torch_dtype = {\"float16\": torch.float16, \"bfloat16\": torch.bfloat16,\n                   \"float32\": torch.float32}[args.dtype]\n\n    logger.info(\"Loading tokenizer and calibration data...\")\n    tokenizer = AutoTokenizer.from_pretrained(args.original_model, trust_remote_code=True)\n    calibration_data = load_calibration_data(tokenizer, args.num_samples, args.max_length,\n                                             args.seed)\n    n_total = len(calibration_data)\n    logger.info(f\"Loaded {n_total} calibration samples\")\n\n    # --- Load original model and collect all activations ---\n    logger.info(\"Loading original model...\")\n    orig_model = AutoModelForCausalLM.from_pretrained(\n        args.original_model, torch_dtype=torch_dtype, device_map=device, trust_remote_code=True\n    )\n    config = orig_model.config\n    n_heads_orig = config.num_attention_heads\n    n_kv_heads = config.num_key_value_heads\n    n_layers = config.num_hidden_layers\n    heads_per_kv = n_heads_orig // n_kv_heads\n    logger.info(f\"Architecture: {n_layers}L x {n_heads_orig}Q x {n_kv_heads}KV \"\n                f\"({heads_per_kv} Q/KV group, {n_layers * n_kv_heads} total groups)\")\n\n    logger.info(\"Collecting original model q_proj activations...\")\n    orig_acts = collect_qproj_activations(orig_model, calibration_data, device)\n\n    logger.info(\"Collecting original model MLP gate_proj activations...\")\n    orig_mlp_acts = collect_mlp_activations(orig_model, calibration_data, device, args.mlp_groups)\n\n    del orig_model\n    torch.cuda.empty_cache()\n    logger.info(\"Original model freed. All activations cached on CPU.\")\n\n    output = {\n        \"config\": {\n            \"original_model\": args.original_model,\n            \"num_samples\": n_total,\n            \"n_layers\": n_layers,\n            \"n_heads_original\": n_heads_orig,\n            \"n_kv_heads\": n_kv_heads,\n            \"heads_per_kv\": heads_per_kv,\n            \"total_gqa_groups\": n_layers * n_kv_heads,\n            \"mlp_groups\": args.mlp_groups,\n            \"seed\": args.seed,\n        },\n    }\n\n    # --- Phase 1-3: Cross-model CKA (optional) ---\n    if not args.skip_cross_model:\n        logger.info(\"Loading pruned model...\")\n        pruned_model, pruning_meta = load_pruned_model_with_meta(\n            args.original_model, args.pruned_model, torch_dtype, device\n        )\n        keep_masks = pruning_meta[\"attn_keep_masks\"]\n        logger.info(\"Collecting pruned model activations...\")\n        pruned_acts = collect_qproj_activations(pruned_model, calibration_data, device)\n        del pruned_model\n        torch.cuda.empty_cache()\n        logger.info(\"Pruned model freed.\")\n\n        # Phase 1: Full CKA scores\n        logger.info(\"=\" * 50)\n        logger.info(\"Phase 1: Full CKA scores (N=%d)...\", n_total)\n        full_scores = compute_group_cka(orig_acts, pruned_acts, keep_masks,\n                                        n_heads_orig, n_kv_heads)\n        valid_scores = {k: v for k, v in full_scores.items()\n                        if not (isinstance(v, float) and v != v)}\n        vals = np.array(list(valid_scores.values()))\n        logger.info(f\"Valid groups: {len(valid_scores)}/{n_layers * n_kv_heads}\")\n        logger.info(f\"CKA: mean={vals.mean():.4f}, std={vals.std():.4f}, \"\n                    f\"range=[{vals.min():.4f}, {vals.max():.4f}]\")\n\n        # Phase 2: Split-half reliability (cross-model)\n        logger.info(\"=\" * 50)\n        logger.info(\"Phase 2: Split-half reliability (%d splits)...\", args.n_splits)\n        cross_split_results = []\n        for i in range(args.n_splits):\n            rng = np.random.RandomState(args.seed + i)\n            perm = rng.permutation(n_total)\n            half = n_total // 2\n            idx_a = sorted(perm[:half].tolist())\n            idx_b = sorted(perm[half:2 * half].tolist())\n\n            scores_a = compute_group_cka(orig_acts, pruned_acts, keep_masks,\n                                         n_heads_orig, n_kv_heads, idx_a)\n            scores_b = compute_group_cka(orig_acts, pruned_acts, keep_masks,\n                                         n_heads_orig, n_kv_heads, idx_b)\n            arr_a, arr_b = scores_to_aligned_arrays(scores_a, scores_b)\n            rho, p = stats.spearmanr(arr_a, arr_b)\n            cross_split_results.append({\"split\": i, \"rho\": float(rho), \"p_value\": float(p),\n                                        \"n_groups\": len(arr_a)})\n            logger.info(f\"  Split {i}: rho={rho:.4f}, p={p:.2e}\")\n\n        cross_mean_rho = float(np.mean([r[\"rho\"] for r in cross_split_results]))\n        cross_std_rho = float(np.std([r[\"rho\"] for r in cross_split_results]))\n\n        # Phase 3: Calibration size sensitivity\n        logger.info(\"=\" * 50)\n        logger.info(\"Phase 3: Calibration size sensitivity...\")\n        size_results = []\n        for n_sub in [128, 256, 512]:\n            if n_sub >= n_total:\n                continue\n            rng = np.random.RandomState(args.seed)\n            sub_idx = sorted(rng.permutation(n_total)[:n_sub].tolist())\n\n            sub_scores = compute_group_cka(orig_acts, pruned_acts, keep_masks,\n                                           n_heads_orig, n_kv_heads, sub_idx)\n            ref_vals, sub_vals = scores_to_aligned_arrays(full_scores, sub_scores)\n            rho, p = stats.spearmanr(ref_vals, sub_vals)\n            size_results.append({\"n_samples\": n_sub, \"rho_vs_full\": float(rho),\n                                 \"p_value\": float(p)})\n            logger.info(f\"  N={n_sub}: rho={rho:.4f} vs N={n_total}\")\n\n        del pruned_acts\n        torch.cuda.empty_cache()\n\n        per_group = {}\n        for (l, g), v in full_scores.items():\n            key = f\"layer{l}_group{g}\"\n            per_group[key] = None if (isinstance(v, float) and v != v) else float(v)\n\n        output[\"config\"][\"pruned_model\"] = args.pruned_model\n        output[\"config\"][\"valid_gqa_groups\"] = len(valid_scores)\n        output[\"per_group_cka_scores\"] = per_group\n        output[\"cka_summary\"] = {\n            \"mean\": float(vals.mean()),\n            \"std\": float(vals.std()),\n            \"min\": float(vals.min()),\n            \"max\": float(vals.max()),\n            \"median\": float(np.median(vals)),\n        }\n        output[\"split_half_reliability\"] = {\n            \"per_split\": cross_split_results,\n            \"mean_rho\": cross_mean_rho,\n            \"std_rho\": cross_std_rho,\n            \"pass\": cross_mean_rho > 0.9,\n        }\n        output[\"size_sensitivity\"] = {\n            \"reference_n\": n_total,\n            \"per_size\": size_results,\n            \"all_pass_0.9\": all(s[\"rho_vs_full\"] > 0.9 for s in size_results),\n        }\n\n    # --- Phase 4: F(h) attention head split-half reliability ---\n    logger.info(\"=\" * 50)\n    logger.info(\"Phase 4: F(h) attention head split-half reliability (%d splits)...\",\n                args.n_splits)\n    attn_fh_results = compute_fh_reliability(orig_acts, args.n_splits, args.seed, \"attn_heads\")\n    attn_mean_rho = float(np.mean([r[\"rho\"] for r in attn_fh_results]))\n    attn_std_rho = float(np.std([r[\"rho\"] for r in attn_fh_results]))\n    attn_pass = attn_mean_rho > 0.9\n    logger.info(f\"Attn F(h) reliability: mean_rho={attn_mean_rho:.4f} +/- {attn_std_rho:.4f} \"\n                f\"{'PASS' if attn_pass else 'FAIL'}\")\n\n    output[\"fh_attn_reliability\"] = {\n        \"per_split\": attn_fh_results,\n        \"mean_rho\": attn_mean_rho,\n        \"std_rho\": attn_std_rho,\n        \"pass\": attn_pass,\n    }\n\n    del orig_acts\n    torch.cuda.empty_cache()\n\n    # --- Phase 5: F(h) MLP group split-half reliability ---\n    logger.info(\"=\" * 50)\n    logger.info(\"Phase 5: F(h) MLP group split-half reliability (%d splits)...\", args.n_splits)\n    mlp_fh_results = compute_fh_reliability(orig_mlp_acts, args.n_splits, args.seed, \"mlp_groups\")\n    mlp_mean_rho = float(np.mean([r[\"rho\"] for r in mlp_fh_results]))\n    mlp_std_rho = float(np.std([r[\"rho\"] for r in mlp_fh_results]))\n    mlp_pass = mlp_mean_rho > 0.9\n    logger.info(f\"MLP F(h) reliability: mean_rho={mlp_mean_rho:.4f} +/- {mlp_std_rho:.4f} \"\n                f\"{'PASS' if mlp_pass else 'FAIL'}\")\n\n    output[\"fh_mlp_reliability\"] = {\n        \"per_split\": mlp_fh_results,\n        \"mean_rho\": mlp_mean_rho,\n        \"std_rho\": mlp_std_rho,\n        \"pass\": mlp_pass,\n    }\n\n    del orig_mlp_acts\n    torch.cuda.empty_cache()\n\n    # --- Save results ---\n    os.makedirs(os.path.dirname(args.output) or \".\", exist_ok=True)\n    with open(args.output, \"w\") as f:\n        json.dump(output, f, indent=2)\n    logger.info(f\"Results saved to {args.output}\")\n\n    # --- Print summary ---\n    print(f\"\\n{'=' * 60}\")\n    print(\"CKA Reliability Analysis\")\n    print(f\"{'=' * 60}\")\n\n    if not args.skip_cross_model:\n        print(f\"\\nCross-model CKA (Phase 1-3):\")\n        print(f\"  GQA groups: {len(valid_scores)}/{n_layers * n_kv_heads} valid\")\n        print(f\"  CKA scores: {vals.mean():.4f} +/- {vals.std():.4f} \"\n              f\"[{vals.min():.4f}, {vals.max():.4f}]\")\n        sh_pass = \"PASS\" if cross_mean_rho > 0.9 else \"FAIL\"\n        print(f\"  Split-half reliability ({args.n_splits} splits):\")\n        print(f\"    rho = {cross_mean_rho:.4f} +/- {cross_std_rho:.4f}  {sh_pass} \"\n              f\"(threshold: 0.9)\")\n        for r in cross_split_results:\n            print(f\"      Split {r['split']}: rho={r['rho']:.4f}\")\n        print(f\"  Size sensitivity (vs N={n_total}):\")\n        for s in size_results:\n            sv = \"PASS\" if s[\"rho_vs_full\"] > 0.9 else \"FAIL\"\n            print(f\"    N={s['n_samples']:4d}: rho={s['rho_vs_full']:.4f}  {sv}\")\n\n    print(f\"\\nF(h) Attention head reliability (Phase 4):\")\n    ah_label = \"PASS\" if attn_pass else \"FAIL\"\n    print(f\"  rho = {attn_mean_rho:.4f} +/- {attn_std_rho:.4f}  {ah_label} (threshold: 0.9)\")\n    for r in attn_fh_results:\n        print(f\"    Split {r['split']}: rho={r['rho']:.4f}\")\n\n    print(f\"\\nF(h) MLP group reliability (Phase 5):\")\n    mh_label = \"PASS\" if mlp_pass else \"FAIL\"\n    print(f\"  rho = {mlp_mean_rho:.4f} +/- {mlp_std_rho:.4f}  {mh_label} (threshold: 0.9)\")\n    for r in mlp_fh_results:\n        print(f\"    Split {r['split']}: rho={r['rho']:.4f}\")\n\n    print(f\"{'=' * 60}\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T03:25:05.195002+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/run_cka_reliability.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cka_fh_reliability_20260515T031935",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T03:25:05.195175+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python src/run_cka_reliability.py --help",
  "description": "Verify argument parsing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cka_fh_reliability_20260515T031935",
  "tool": "Bash",
  "tool_args": {
    "command": "python src/run_cka_reliability.py --help",
    "description": "Verify argument parsing"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T03:25:05.195347+00:00_

Exit code 127
/bin/bash: line 1: python: command not found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cka_fh_reliability_20260515T031935",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T03:25:05.195483+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 src/run_cka_reliability.py --help",
  "description": "Verify argument parsing with python3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cka_fh_reliability_20260515T031935",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 src/run_cka_reliability.py --help",
    "description": "Verify argument parsing with python3"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T03:25:05.195746+00:00_

Exit code 1
Traceback (most recent call last):
  File "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/run_cka_reliability.py", line 22, in &lt;module>
    import torch
ModuleNotFoundError: No module named 'torch'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cka_fh_reliability_20260515T031935",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T03:25:05.195900+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport ast, sys\nwith open('src/run_cka_reliability.py') as f:\n    tree = ast.parse(f.read())\nprint('Syntax OK')\n# Check argparse args\nsource = open('src/run_cka_reliability.py').read()\nfor arg in ['--mlp_groups', '--skip_cross_model', '--original_model', '--pruned_model', '--output']:\n    if arg in source:\n        print(f'  Found arg: {arg}')\n    else:\n        print(f'  MISSING arg: {arg}')\n\"",
  "description": "Verify syntax and arg presence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cka_fh_reliability_20260515T031935",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport ast, sys\nwith open('src/run_cka_reliability.py') as f:\n    tree = ast.parse(f.read())\nprint('Syntax OK')\n# Check argparse args\nsource = open('src/run_cka_reliability.py').read()\nfor arg in ['--mlp_groups', '--skip_cross_model', '--original_model', '--pruned_model', '--output']:\n    if arg in source:\n        print(f'  Found arg: {arg}')\n    else:\n        print(f'  MISSING arg: {arg}')\n\"",
    "description": "Verify syntax and arg presence"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T03:25:05.196030+00:00_

Syntax OK
  Found arg: --mlp_groups
  Found arg: --skip_cross_model
  Found arg: --original_model
  Found arg: --pruned_model
  Found arg: --output

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cka_fh_reliability_20260515T031935",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-15T03:25:05.196187+00:00_

语法正确，所有新参数都在。

修改总结：
- **Phase 4** (`fh_attn_reliability`): 对原始模型 attention heads 做 split-half F(h) 排名 Spearman ρ，阈值 0.9
- **Phase 5** (`fh_mlp_reliability`): 对 MLP groups 做同样的 split-half F(h) reliability
- 新增 `collect_mlp_activations` 收集 gate_proj 激活（与 `cka_overlap.py` 一致）
- 新增 `compute_fh_scores` 计算 intra-layer pairwise CKA → F(h)
- 新增 `compute_fh_reliability` 做 n_splits 次 split-half 并报告 Spearman ρ
- `--pruned_model` 改为可选（`--skip_cross_model` 时不需要）
- `--mlp_groups` 默认 28
- 原始模型加载一次，两次 forward pass 分别收集 q_proj 和 gate_proj 激活
- Phase 1-3 保留不变，仅在未设 `--skip_cross_model` 时执行

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_cka_fh_reliability_20260515T031935"
}
```

</details>

---
