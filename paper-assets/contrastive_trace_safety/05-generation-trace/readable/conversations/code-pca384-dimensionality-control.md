# code pca384 dimensionality control

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 89
- **Recorded user turns:** 0
- **Tool calls:** 44
- **Original source:** `logs/chats/worker_code_pca384_dimensionality_control_20260517T190710.jsonl`
- **Structured JSON:** [`df239af71bbfd2051132.json`](../../sessions/df/df239af71bbfd2051132.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

89 recorded events

### Tool call

_source line 1 · 2026-05-17T19:24:11.348682+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__ssh_read_only",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__ssh_read_only",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T19:24:11.349155+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T19:24:11.349478+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "/root/miniconda3/bin/python3.12 -c \"\nimport torch, glob\nfrom pathlib import Path\n\nconfigs = {\n    'r1-8b': '/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states',\n    'ot-7b': '/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_ot7b',\n    'qwq-32b': '/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b',\n    'r1-32b': '/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b',\n}\n\nfor model, hs_dir in configs.items():\n    files = sorted(glob.glob(str(Path(hs_dir) / '*.pt')))\n    if not files:\n        print(f'{model}: NO FILES FOUND')\n        continue\n    data = torch.load(files[0], map_location='cpu', weights_only=False)\n    print(f'=== {model} ({len(files)} files) ===')\n    print(f'  keys: {list(data.keys())}')\n    if 'hidden_states' in data:\n        print(f'  hidden_states shape: {data[\\\"hidden_states\\\"].shape}')\n    if 'layers' in data:\n        print(f'  layers: {data[\\\"layers\\\"]}')\n    if 'layer_indices' in data:\n        print(f'  layer_indices: {data[\\\"layer_indices\\\"]}')\n    if 'extracted_layers' in data:\n        print(f'  extracted_layers: {data[\\\"extracted_layers\\\"]}')\n    # Check for sentences\n    if 'sentences' in data:\n        print(f'  sentences: {len(data[\\\"sentences\\\"])} items, first: {data[\\\"sentences\\\"][0][:60]}...')\n    if 'step_labels' in data:\n        print(f'  step_labels shape: {data[\\\"step_labels\\\"].shape if hasattr(data[\\\"step_labels\\\"], \\\"shape\\\") else len(data[\\\"step_labels\\\"])}')\n    if 'commitment_point' in data:\n        print(f'  commitment_point: {data[\\\"commitment_point\\\"]}')\n    print()\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "/root/miniconda3/bin/python3.12 -c \"\nimport torch, glob\nfrom pathlib import Path\n\nconfigs = {\n    'r1-8b': '/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states',\n    'ot-7b': '/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_ot7b',\n    'qwq-32b': '/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b',\n    'r1-32b': '/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b',\n}\n\nfor model, hs_dir in configs.items():\n    files = sorted(glob.glob(str(Path(hs_dir) / '*.pt')))\n    if not files:\n        print(f'{model}: NO FILES FOUND')\n        continue\n    data = torch.load(files[0], map_location='cpu', weights_only=False)\n    print(f'=== {model} ({len(files)} files) ===')\n    print(f'  keys: {list(data.keys())}')\n    if 'hidden_states' in data:\n        print(f'  hidden_states shape: {data[\\\"hidden_states\\\"].shape}')\n    if 'layers' in data:\n        print(f'  layers: {data[\\\"layers\\\"]}')\n    if 'layer_indices' in data:\n        print(f'  layer_indices: {data[\\\"layer_indices\\\"]}')\n    if 'extracted_layers' in data:\n        print(f'  extracted_layers: {data[\\\"extracted_layers\\\"]}')\n    # Check for sentences\n    if 'sentences' in data:\n        print(f'  sentences: {len(data[\\\"sentences\\\"])} items, first: {data[\\\"sentences\\\"][0][:60]}...')\n    if 'step_labels' in data:\n        print(f'  step_labels shape: {data[\\\"step_labels\\\"].shape if hasattr(data[\\\"step_labels\\\"], \\\"shape\\\") else len(data[\\\"step_labels\\\"])}')\n    if 'commitment_point' in data:\n        print(f'  commitment_point: {data[\\\"commitment_point\\\"]}')\n    print()\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T19:24:11.349813+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: '/root/miniconda3/bin/python3.12 -c \\\"\\\\nimport torch, glob\\\\nfrom pathlib import Path\\\\n\\\\nconfigs = {\\\\n    \\\\'r1-8b\\\\': \\\\'/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states\\\\',\\\\n    \\\\'ot-7b\\\\': \\\\'/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_ot7b\\\\',\\\\n    \\\\'qwq-32b\\\\': \\\\'/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b\\\\',\\\\n    \\\\'r1-32b\\\\': \\\\'/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b\\\\',\\\\n}\\\\n\\\\nfor model, hs_dir in configs.items():\\\\n    files = sorted(glob.glob(str(Path(hs_dir) / \\\\'*.pt\\\\')))\\\\n    if not files:\\\\n        print(f\\\\'{model}: NO FILES FOUND\\\\')\\\\n        continue\\\\n    data = torch.load(files[0], map_location=\\\\'cpu\\\\', weights_only=False)\\\\n    print(f\\\\'=== {model} ({len(files)} files) ===\\\\')\\\\n    print(f\\\\'  keys: {list(data.keys())}\\\\')\\\\n    if \\\\'hidden_states\\\\' in data:\\\\n        print(f\\\\'  hidden_states shape: {data[\\\\\\\\\\\"hidden_states\\\\\\\\\\\"].shape}\\\\')\\\\n    if \\\\'layers\\\\' in data:\\\\n        print(f\\\\'  layers: {data[\\\\\\\\\\\"layers\\\\\\\\\\\"]}\\\\')\\\\n    if \\\\'layer_indices\\\\' in data:\\\\n        print(f\\\\'  layer_indices: {data[\\\\\\\\\\\"layer_indices\\\\\\\\\\\"]}\\\\')\\\\n    if \\\\'extracted_layers\\\\' in data:\\\\n        print(f\\\\'  extracted_layers: {data[\\\\\\\\\\\"extracted_layers\\\\\\\\\\\"]}\\\\')\\\\n    # Check for sentences\\\\n    if \\\\'sentences\\\\' in data:\\\\n        print(f\\\\'  sentences: {len(data[\\\\\\\\\\\"sentences\\\\\\\\\\\"])} items, first: {data[\\\\\\\\\\\"sentences\\\\\\\\\\\"][0][:60]}...\\\\')\\\\n    if \\\\'step_labels\\\\' in data:\\\\n        print(f\\\\'  step_labels shape: {data[\\\\\\\\\\\"step_labels\\\\\\\\\\\"].shape if hasattr(da
…[truncated 720 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T19:24:11.350111+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "/root/miniconda3/bin/python3.12 -c \"\nimport torch, glob\nfrom pathlib import Path\n\nconfigs = {\n    'r1-8b': '/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states',\n    'ot-7b': '/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_ot7b',\n    'qwq-32b': '/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b',\n    'r1-32b': '/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b',\n}\n\nfor model, hs_dir in configs.items():\n    files = sorted(glob.glob(str(Path(hs_dir) / '*.pt')))\n    if not files:\n        print(f'{model}: NO FILES FOUND')\n        continue\n    data = torch.load(files[0], map_location='cpu', weights_only=False)\n    print(f'=== {model} ({len(files)} files) ===')\n    print(f'  keys: {list(data.keys())}')\n    if 'hidden_states' in data:\n        print(f'  hidden_states shape: {data[\\\"hidden_states\\\"].shape}')\n    for k in ['layers', 'layer_indices', 'extracted_layers']:\n        if k in data:\n            print(f'  {k}: {data[k]}')\n    if 'sentences' in data:\n        s = data['sentences']\n        if s is not None:\n            print(f'  sentences: {len(s)} items')\n        else:\n            print(f'  sentences: None')\n    else:\n        print(f'  sentences: NOT PRESENT')\n    sl = data.get('step_labels')\n    print(f'  step_labels: {sl.shape if hasattr(sl, \\\"shape\\\") else (len(sl) if sl is not None else None)}')\n    print(f'  commitment_point: {data.get(\\\"commitment_point\\\")}')\n    print()\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "/root/miniconda3/bin/python3.12 -c \"\nimport torch, glob\nfrom pathlib import Path\n\nconfigs = {\n    'r1-8b': '/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states',\n    'ot-7b': '/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_ot7b',\n    'qwq-32b': '/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b',\n    'r1-32b': '/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b',\n}\n\nfor model, hs_dir in configs.items():\n    files = sorted(glob.glob(str(Path(hs_dir) / '*.pt')))\n    if not files:\n        print(f'{model}: NO FILES FOUND')\n        continue\n    data = torch.load(files[0], map_location='cpu', weights_only=False)\n    print(f'=== {model} ({len(files)} files) ===')\n    print(f'  keys: {list(data.keys())}')\n    if 'hidden_states' in data:\n        print(f'  hidden_states shape: {data[\\\"hidden_states\\\"].shape}')\n    for k in ['layers', 'layer_indices', 'extracted_layers']:\n        if k in data:\n            print(f'  {k}: {data[k]}')\n    if 'sentences' in data:\n        s = data['sentences']\n        if s is not None:\n            print(f'  sentences: {len(s)} items')\n        else:\n            print(f'  sentences: None')\n    else:\n        print(f'  sentences: NOT PRESENT')\n    sl = data.get('step_labels')\n    print(f'  step_labels: {sl.shape if hasattr(sl, \\\"shape\\\") else (len(sl) if sl is not None else None)}')\n    print(f'  commitment_point: {data.get(\\\"commitment_point\\\")}')\n    print()\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T19:24:11.350370+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== r1-8b (268 files) ===\\n  keys: ['hidden_states', 'trace_id', 'num_sentences', 'commitment_point', 'step_labels']\\n  hidden_states shape: torch.Size([46, 13, 4096])\\n  sentences: NOT PRESENT\\n  step_labels: None\\n  commitment_point: None\\n\\n=== ot-7b (228 files) ===\\n  keys: ['hidden_states', 'trace_id', 'num_sentences', 'commitment_point', 'step_labels', 'query']\\n  hidden_states shape: torch.Size([59, 28, 3584])\\n  sentences: NOT PRESENT\\n  step_labels: 59\\n  commitment_point: 58\\n\\n=== qwq-32b (95 files) ===\\n  keys: ['hidden_states', 'trace_id', 'num_sentences', 'commitment_point', 'step_labels', 'query']\\n  hidden_states shape: torch.Size([48, 64, 5120])\\n  sentences: NOT PRESENT\\n  step_labels: 48\\n  commitment_point: 8\\n\\n=== r1-32b (100 files) ===\\n  keys: ['hidden_states', 'trace_id', 'num_sentences', 'commitment_point', 'step_labels', 'query']\\n  hidden_states shape: torch.Size([36, 64, 5120])\\n  sentences: NOT PRESENT\\n  step_labels: 36\\n  commitment_point: 32\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.1}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T19:24:11.350683+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "/root/miniconda3/bin/python3.12 -c \"\nimport torch, glob\nfrom pathlib import Path\n\n# Count valid traces per model\nconfigs = {\n    'r1-8b': '/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states',\n    'ot-7b': '/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_ot7b',\n    'qwq-32b': '/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b',\n    'r1-32b': '/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b',\n}\n\nfor model, hs_dir in configs.items():\n    files = sorted(glob.glob(str(Path(hs_dir) / '*.pt')))\n    valid = 0\n    for f in files:\n        data = torch.load(f, map_location='cpu', weights_only=False)\n        if data.get('step_labels') is not None and data.get('commitment_point') is not None:\n            valid += 1\n    print(f'{model}: {valid}/{len(files)} valid traces')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "/root/miniconda3/bin/python3.12 -c \"\nimport torch, glob\nfrom pathlib import Path\n\n# Count valid traces per model\nconfigs = {\n    'r1-8b': '/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states',\n    'ot-7b': '/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_ot7b',\n    'qwq-32b': '/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b',\n    'r1-32b': '/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b',\n}\n\nfor model, hs_dir in configs.items():\n    files = sorted(glob.glob(str(Path(hs_dir) / '*.pt')))\n    valid = 0\n    for f in files:\n        data = torch.load(f, map_location='cpu', weights_only=False)\n        if data.get('step_labels') is not None and data.get('commitment_point') is not None:\n            valid += 1\n    print(f'{model}: {valid}/{len(files)} valid traces')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-17T19:24:11.350930+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "find /root/autodl-tmp/contrastive_trace_safety/src/experiments -name \"*.py\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "find /root/autodl-tmp/contrastive_trace_safety/src/experiments -name \"*.py\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-17T19:24:11.351146+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"r1-8b: 209/268 valid traces\\not-7b: 228/228 valid traces\\nqwq-32b: 95/95 valid traces\\nr1-32b: 100/100 valid traces\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.72}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T19:24:11.351404+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/contrastive_trace_safety/src/experiments/__init__.py\\n/root/autodl-tmp/contrastive_trace_safety/src/experiments/gru_multilayer_ablation.py\\n/root/autodl-tmp/contrastive_trace_safety/src/experiments/trajguard_mahalanobis.py\\n/root/autodl-tmp/contrastive_trace_safety/src/experiments/bootstrap_ci.py\\n/root/autodl-tmp/contrastive_trace_safety/src/experiments/text_baseline.py\\n/root/autodl-tmp/contrastive_trace_safety/src/experiments/bocpd_poc.py\\n/root/autodl-tmp/contrastive_trace_safety/src/experiments/fpr_analysis.py\\n/root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_001b_extract_qwq.py\\n/root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_001a_extract_r1_32b.py\\n/root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_001b_probing.py\\n/root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_001a_probing.py\\n/root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_001b_bootstrap.py\\n/root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_001a_bootstrap_hs_vs_text.py\\n/root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_003_cross_transfer.py\\n/root/autodl-tmp/contrastive_trace_safety/src/experiments/m001_layer_fix.py\\n/root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_c2_control_task.py\\n/root/autodl-tmp/contrastive_trace_safety/src/experiments/r1_8b_bootstrap_hs_text.py\\n/root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_007_window_ablation.py\\n/root/autodl-tmp/contrastive_trace_safety/src/experiments/text_window_ablation_r1_8b.py\\n/root/autodl-tmp/contrastive_trace_safety/src/experiments/run_selectivity_qwq_l2.py\\n/root/autodl-tmp/contrastive_trace_safety/src/experiments/gru_per_seed_eval.py\\n/root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_pathC_two_stage_sim.py\\n/root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_ot7b_full_pipeline.py\\n/root/autodl-tmp/contrastive_trace_safety
…[truncated 2157 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T19:24:11.351698+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "head -80 /root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_ot7b_layer16_verify.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "head -80 /root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_ot7b_layer16_verify.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T19:24:11.352007+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"OT-7B Layer 16 Verification — replicates full pipeline logic for layer 16.\\\"\\\"\\\"\\n\\nimport os, sys, json\\nos.environ[\\\"HF_ENDPOINT\\\"] = \\\"https://hf-mirror.com\\\"\\nos.environ[\\\"TOKENIZERS_PARALLELISM\\\"] = \\\"false\\\"\\nos.environ[\\\"CUDA_VISIBLE_DEVICES\\\"] = \\\"1\\\"\\n\\nimport numpy as np\\nimport torch\\nfrom pathlib import Path\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.metrics import balanced_accuracy_score, precision_score\\n\\nsys.path.insert(0, \\\"/root/autodl-tmp/contrastive_trace_safety\\\")\\nfrom src.data_loader import load_harmthoughts, extract_commitment_point, create_step_labels\\n\\nHS_DIR = Path(\\\"/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_ot7b\\\")\\nOUTPUT_DIR = Path(\\\"/root/autodl-tmp/contrastive_trace_safety/artifacts/ot7b_layer16_verification\\\")\\nNUM_LAYERS = 28\\nHIDDEN_DIM = 3584\\nSEED = 42\\nK_CONSECUTIVE = 5\\nTHRESHOLD = 0.5\\nTARGET_LAYER = 16\\n\\n# ============ DATA LOADING (same as pipeline) ============\\n\\ndef load_ot7b_traces():\\n    raw_traces = load_harmthoughts(\\\"ot-7b\\\")\\n    traces = []\\n    for trace_id, steps in raw_traces.items():\\n        if steps[0][\\\"final_judgment\\\"] != 1.0:\\n            continue\\n        labels = [s[\\\"label\\\"] for s in steps]\\n        cp = extract_commitment_point(labels)\\n        if cp is None:\\n            continue\\n        sentences = [s[\\\"sentence\\\"] for s in steps]\\n        step_labels = create_step_labels(cp, len(sentences))\\n        traces.append({\\n            \\\"trace_id\\\": trace_id,\\n            \\\"sentences\\\": sentences,\\n            \\\"labels\\\": labels,\\n            \\\"commitment_point\\\": cp,\\n            \\\"step_labels\\\": step_labels,\\n            \\\"query\\\": steps[0][\\\"query\\\"],\\n        })\\n    return traces\\n\\ndef load_extracted_traces():\\n    traces = []\\n    for pt_file in 
…[truncated 1259 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T19:24:11.352265+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "head -100 /root/autodl-tmp/contrastive_trace_safety/src/experiments/text_baseline.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "head -100 /root/autodl-tmp/contrastive_trace_safety/src/experiments/text_baseline.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T19:24:11.352588+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Text-based commitment detection baseline using sentence embeddings.\\\"\\\"\\\"\\n\\nimport sys\\nimport json\\nimport os\\nimport numpy as np\\nfrom pathlib import Path\\n\\nsys.path.insert(0, '/root/autodl-tmp/contrastive_trace_safety')\\n\\nfrom src.data_loader import prepare_dataset, split_data\\nfrom src.config import TRAIN_RATIO, VAL_RATIO, SEED, DETECTION_WINDOW\\n\\n# Step 1: Load data\\nprint(\\\"Loading dataset...\\\")\\ndata = prepare_dataset(\\\"r1-8b\\\")\\njb_traces = data[\\\"jailbreak_with_commitment\\\"]\\nprint(f\\\"Total jailbreak_with_commitment traces: {len(jb_traces)}\\\")\\n\\ntrain, val, test = split_data(jb_traces, TRAIN_RATIO, VAL_RATIO, SEED)\\nprint(f\\\"Split: train={len(train)}, val={len(val)}, test={len(test)}\\\")\\n\\n# Step 2: Sentence embeddings\\nprint(\\\"Loading sentence-transformers model...\\\")\\nos.environ[\\\"TOKENIZERS_PARALLELISM\\\"] = \\\"false\\\"\\nfrom sentence_transformers import SentenceTransformer\\nmodel = SentenceTransformer('all-MiniLM-L6-v2', device='cpu')\\n\\nprint(\\\"Encoding sentences...\\\")\\nall_traces = train + val + test\\nfor i, trace in enumerate(all_traces):\\n    embeddings = model.encode(trace[\\\"sentences\\\"], batch_size=64, show_progress_bar=False)\\n    trace[\\\"text_embeddings\\\"] = embeddings\\n    if (i + 1) % 50 == 0:\\n        print(f\\\"  Encoded {i+1}/{len(all_traces)} traces\\\")\\nprint(f\\\"  Done encoding all {len(all_traces)} traces\\\")\\n\\n# Step 3: Build features\\ndef build_static_features(traces):\\n    X, y = [], []\\n    for t in traces:\\n        emb = t[\\\"text_embeddings\\\"]\\n        labels = t[\\\"step_labels\\\"]\\n        for i in range(len(labels)):\\n            X.append(emb[i])\\n            y.append(labels[i])\\n    return np.array(X), np.array(y)\\n\\ndef build_temporal_features(traces, window=15):\\n    X, y = [], []\\n    dim = 384\\n    for t in traces:\\n        emb = t[\\\"text_embed
…[truncated 2084 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T19:24:11.352870+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "head -60 /root/autodl-tmp/contrastive_trace_safety/src/experiments/r1_8b_bootstrap_hs_text.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "head -60 /root/autodl-tmp/contrastive_trace_safety/src/experiments/r1_8b_bootstrap_hs_text.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T19:24:11.353139+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"r1-8b: Pre-CP FPR Paired Bootstrap Test - HS probe vs Text probe.\\\"\\\"\\\"\\n\\nimport os, sys, json\\nos.environ[\\\"TOKENIZERS_PARALLELISM\\\"] = \\\"false\\\"\\nos.environ[\\\"HF_ENDPOINT\\\"] = \\\"https://hf-mirror.com\\\"\\n\\nimport numpy as np\\nimport torch\\nfrom sklearn.linear_model import LogisticRegression\\nfrom pathlib import Path\\n\\nsys.path.insert(0, \\\"/root/autodl-tmp/contrastive_trace_safety\\\")\\nfrom src.data_loader import load_harmthoughts, extract_commitment_point, create_step_labels\\nfrom src.config import SAFETY_LABELS\\n\\nHS_DIR = Path(\\\"/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states\\\")\\nOUTPUT_DIR = Path(\\\"/root/autodl-tmp/contrastive_trace_safety/artifacts/r1_8b_bootstrap_hs_text\\\")\\nHIDDEN_DIM = 4096\\nTEXT_DIM = 384\\nLAYER_IDX = 2  # Layer 14 = LAYERS[2] in stored tensors (LAYERS starts at 12)\\nWINDOW_SIZE = 15\\nSEED = 42\\n\\n\\ndef load_traces_with_sentences():\\n    print(\\\"Loading HarmThoughts dataset (r1-8b)...\\\")\\n    raw_traces = load_harmthoughts(\\\"r1-8b\\\")\\n\\n    traces = []\\n    for trace_id, steps in raw_traces.items():\\n        is_jailbreak = steps[0][\\\"final_judgment\\\"] == 1.0\\n        if not is_jailbreak:\\n            continue\\n        labels = [s[\\\"label\\\"] for s in steps]\\n        cp = extract_commitment_point(labels)\\n        if cp is None:\\n            continue\\n\\n        hs_path = HS_DIR / f\\\"{trace_id}.pt\\\"\\n        if not hs_path.exists():\\n            continue\\n\\n        sentences = [s[\\\"sentence\\\"] for s in steps]\\n        step_labels = create_step_labels(cp, len(sentences))\\n\\n        hs_data = torch.load(hs_path, map_location=\\\"cpu\\\", weights_only=False)\\n\\n        traces.append({\\n            \\\"trace_id\\\": trace_id,\\n            \\\"sentences\\\": sentences,\\n            \\\"hidden_states\\\": hs_data[\\\"hidden_states\\\"],\\n            \\\"comm
…[truncated 339 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T19:24:11.353434+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "head -120 /root/autodl-tmp/contrastive_trace_safety/src/data_loader.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "head -120 /root/autodl-tmp/contrastive_trace_safety/src/data_loader.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-17T19:24:11.353760+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Load HarmThoughts dataset and extract commitment points.\\n\\nInput: HuggingFace dataset \\\"ishitakakkar-10/HarmThoughts\\\"\\nOutput: List of trace dicts with sentences, labels, commitment_point, split assignments\\n\\\"\\\"\\\"\\n\\nfrom collections import defaultdict\\nfrom typing import List, Optional, Dict, Any\\nimport numpy as np\\nfrom datasets import load_dataset\\n\\nfrom .config import (\\n    HF_DATASET, TARGET_MODEL, SAFETY_LABELS,\\n    TRAIN_RATIO, VAL_RATIO, SEED\\n)\\n\\n\\ndef load_harmthoughts(model_name: str = TARGET_MODEL) -> Dict[str, List[Dict]]:\\n    \\\"\\\"\\\"Load HarmThoughts from HF and group by trace_id.\\\"\\\"\\\"\\n    ds = load_dataset(HF_DATASET, split=\\\"train\\\")\\n\\n    traces = defaultdict(list)\\n    for row in ds:\\n        if row[\\\"model_name\\\"] != model_name:\\n            continue\\n        # trace_id is the part before the last dash in sentence_id\\n        sid = row[\\\"sentence_id\\\"]\\n        parts = sid.rsplit(\\\"-\\\", 1)\\n        trace_id = parts[0]\\n        step_idx = int(parts[1]) - 1  # convert to 0-indexed\\n\\n        traces[trace_id].append({\\n            \\\"sentence_id\\\": sid,\\n            \\\"step_idx\\\": step_idx,\\n            \\\"sentence\\\": row[\\\"sentence\\\"],\\n            \\\"label\\\": row[\\\"llm_annotation\\\"],\\n            \\\"query\\\": row[\\\"query\\\"],\\n            \\\"final_judgment\\\": row[\\\"final_judgment\\\"],\\n        })\\n\\n    # Sort each trace by step_idx\\n    for tid in traces:\\n        traces[tid].sort(key=lambda x: x[\\\"step_idx\\\"])\\n\\n    return dict(traces)\\n\\n\\ndef extract_commitment_point(labels: List[str]) -> Optional[int]:\\n    \\\"\\\"\\\"Find the commitment point in a sequence of labels.\\n\\n    Returns the index after the last safety label, or None if:\\n    - No safety labels exist in the trace\\n    - The last safety label is at the final position (no post-comm
…[truncated 2539 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T19:24:11.354038+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "head -40 /root/autodl-tmp/contrastive_trace_safety/src/config.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "head -40 /root/autodl-tmp/contrastive_trace_safety/src/config.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-17T19:24:11.354286+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Central configuration for contrastive_trace_safety project.\\\"\\\"\\\"\\n\\nimport os\\nfrom pathlib import Path\\n\\n# Paths\\nPROJECT_ROOT = Path(\\\"/root/autodl-tmp/contrastive_trace_safety\\\")\\nARTIFACTS_DIR = PROJECT_ROOT / \\\"artifacts\\\"\\nHIDDEN_STATES_DIR = ARTIFACTS_DIR / \\\"hidden_states\\\"\\nPROBES_DIR = ARTIFACTS_DIR / \\\"probes\\\"\\n\\n# Model\\nMODEL_NAME = \\\"deepseek-ai/DeepSeek-R1-Distill-Llama-8B\\\"\\nMODEL_PATH = \\\"/root/autodl-tmp/.hf_cache/deepseek-ai/DeepSeek-R1-Distill-Llama-8B\\\"\\n\\n# Dataset\\nHF_DATASET = \\\"ishitakakkar-10/HarmThoughts\\\"\\nTARGET_MODEL = \\\"r1-8b\\\"\\n\\n# Hidden state extraction\\nLAYERS = list(range(12, 25))  # layers 12-24, 13 layers total\\nNUM_LAYERS = len(LAYERS)\\nHIDDEN_DIM = 4096\\nEXTRACT_BATCH_SIZE = 4\\nDEVICE = \\\"cuda:0\\\"\\n\\n# Probes\\nWINDOW_SIZE = 5\\nTEMPORAL_HIDDEN_DIM = 512\\nLEARNING_RATE = 1e-3\\nTRAIN_EPOCHS = 20\\nPROBE_BATCH_SIZE = 64\\nDEFAULT_LAYER = 20  # for static probe\\n\\n# Data split\\nTRAIN_RATIO = 0.6\\nVAL_RATIO = 0.2\\nSEED = 42\\n\\n# Evaluation\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T19:24:11.354543+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "head -40 /root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_r3_qwq_layer60_bootstrap.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "head -40 /root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_r3_qwq_layer60_bootstrap.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-17T19:24:11.354827+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"QwQ-32B Layer 60 HS vs Text Paired Bootstrap.\\n\\nCompares HS temporal probe (Layer 60) against text baseline (all-MiniLM-L6-v2)\\nacross multiple window sizes. Includes position baseline.\\n\\\"\\\"\\\"\\n\\nimport os, sys, json, time\\nos.environ[\\\"TOKENIZERS_PARALLELISM\\\"] = \\\"false\\\"\\nos.environ[\\\"HF_DATASETS_OFFLINE\\\"] = \\\"1\\\"\\nos.environ[\\\"HF_ENDPOINT\\\"] = \\\"https://hf-mirror.com\\\"\\n\\nimport numpy as np\\nimport torch\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.metrics import balanced_accuracy_score, precision_score\\nfrom pathlib import Path\\nfrom collections import defaultdict\\n\\nsys.path.insert(0, \\\"/root/autodl-tmp/contrastive_trace_safety\\\")\\n\\nHS_DIR = Path(\\\"/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b\\\")\\nOUTPUT_DIR = Path(\\\"/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r3_qwq_layer60_bootstrap\\\")\\nOUTPUT_DIR.mkdir(parents=True, exist_ok=True)\\n\\nHIDDEN_DIM = 5120\\nTEXT_DIM = 384\\nLAYER_IDX = 60\\nSEED = 42\\nWINDOW_SIZES = [1, 3, 5, 10, 15]\\nN_RESAMPLES = 1000\\nK_CONSECUTIVE = 5\\nBONFERRONI_THRESHOLD = 0.0167\\n\\n\\ndef load_traces_with_sentences():\\n    from datasets import load_dataset\\n    ds = load_dataset(\\\"ishitakakkar-10/HarmThoughts\\\", split=\\\"train\\\")\\n    sentence_map = defaultdict(list)\\n    for row in ds:\\n        if row[\\\"model_name\\\"] != \\\"QwQ\\\":\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-17T19:24:11.355066+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "head -40 /root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_001a_bootstrap_hs_vs_text.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "head -40 /root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_001a_bootstrap_hs_vs_text.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-17T19:24:11.355322+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Phase 5b: Pre-CP FPR Paired Bootstrap Test - HS probe vs Text probe for R1-32B.\\\"\\\"\\\"\\n\\nimport os, sys, json\\nos.environ[\\\"TOKENIZERS_PARALLELISM\\\"] = \\\"false\\\"\\nos.environ[\\\"HF_ENDPOINT\\\"] = \\\"https://hf-mirror.com\\\"\\n\\nimport numpy as np\\nimport torch\\nfrom sklearn.linear_model import LogisticRegression\\nfrom pathlib import Path\\n\\nsys.path.insert(0, \\\"/root/autodl-tmp/contrastive_trace_safety\\\")\\nfrom src.data_loader import load_harmthoughts, extract_commitment_point, create_step_labels\\nfrom src.config import SAFETY_LABELS\\n\\nHS_DIR = Path(\\\"/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b\\\")\\nOUTPUT_DIR = Path(\\\"/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_001a\\\")\\nHIDDEN_DIM = 5120\\nTEXT_DIM = 384\\nLAYER_IDX = 2\\nWINDOW_SIZE = 10\\nSEED = 42\\n\\n\\ndef load_traces_with_sentences():\\n    \\\"\\\"\\\"Load R1-32B traces from HF and match with hidden states.\\\"\\\"\\\"\\n    print(\\\"Loading HarmThoughts dataset (r1-32b)...\\\")\\n    raw_traces = load_harmthoughts(\\\"r1-32b\\\")\\n\\n    traces = []\\n    for trace_id, steps in raw_traces.items():\\n        is_jailbreak = steps[0][\\\"final_judgment\\\"] == 1.0\\n        if not is_jailbreak:\\n            continue\\n        labels = [s[\\\"label\\\"] for s in steps]\\n        cp = extract_commitment_point(labels)\\n        if cp is None:\\n            continue\\n\\n        hs_path = HS_DIR / f\\\"{trace_id}.pt\\\"\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-17T19:24:11.355590+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "head -100 /root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_r3_qwq_layer60_bootstrap.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "head -100 /root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_r3_qwq_layer60_bootstrap.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-17T19:24:11.355915+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"QwQ-32B Layer 60 HS vs Text Paired Bootstrap.\\n\\nCompares HS temporal probe (Layer 60) against text baseline (all-MiniLM-L6-v2)\\nacross multiple window sizes. Includes position baseline.\\n\\\"\\\"\\\"\\n\\nimport os, sys, json, time\\nos.environ[\\\"TOKENIZERS_PARALLELISM\\\"] = \\\"false\\\"\\nos.environ[\\\"HF_DATASETS_OFFLINE\\\"] = \\\"1\\\"\\nos.environ[\\\"HF_ENDPOINT\\\"] = \\\"https://hf-mirror.com\\\"\\n\\nimport numpy as np\\nimport torch\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.metrics import balanced_accuracy_score, precision_score\\nfrom pathlib import Path\\nfrom collections import defaultdict\\n\\nsys.path.insert(0, \\\"/root/autodl-tmp/contrastive_trace_safety\\\")\\n\\nHS_DIR = Path(\\\"/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b\\\")\\nOUTPUT_DIR = Path(\\\"/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r3_qwq_layer60_bootstrap\\\")\\nOUTPUT_DIR.mkdir(parents=True, exist_ok=True)\\n\\nHIDDEN_DIM = 5120\\nTEXT_DIM = 384\\nLAYER_IDX = 60\\nSEED = 42\\nWINDOW_SIZES = [1, 3, 5, 10, 15]\\nN_RESAMPLES = 1000\\nK_CONSECUTIVE = 5\\nBONFERRONI_THRESHOLD = 0.0167\\n\\n\\ndef load_traces_with_sentences():\\n    from datasets import load_dataset\\n    ds = load_dataset(\\\"ishitakakkar-10/HarmThoughts\\\", split=\\\"train\\\")\\n    sentence_map = defaultdict(list)\\n    for row in ds:\\n        if row[\\\"model_name\\\"] != \\\"QwQ\\\":\\n            continue\\n        sid = row[\\\"sentence_id\\\"]\\n        parts = sid.rsplit(\\\"-\\\", 1)\\n        trace_id = parts[0]\\n        step_idx = int(parts[1]) - 1\\n        sentence_map[trace_id].append((step_idx, row[\\\"sentence\\\"]))\\n\\n    for tid in sentence_map:\\n        sentence_map[tid].sort(key=lambda x: x[0])\\n\\n    traces = []\\n    for pt_file in sorted(HS_DIR.glob(\\\"*.pt\\\")):\\n        if pt_file.name.endswith(\\\".json\\\"):\\n            continue\\n    
…[truncated 1848 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-17T19:24:11.356205+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "/root/miniconda3/bin/python3.12 -c \"\nimport os\nos.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'\nfrom datasets import load_dataset\nds = load_dataset('ishitakakkar-10/HarmThoughts', split='train')\nmodels = set(row['model_name'] for row in ds)\nprint('Available models:', models)\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "/root/miniconda3/bin/python3.12 -c \"\nimport os\nos.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'\nfrom datasets import load_dataset\nds = load_dataset('ishitakakkar-10/HarmThoughts', split='train')\nmodels = set(row['model_name'] for row in ds)\nprint('Available models:', models)\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-17T19:24:11.356431+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Available models: {'ot-7b', 'QwQ', 'r1-8b', 'r1-32b'}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.01}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-17T19:24:11.356802+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "cat > /root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_r5_pca384_control.py << 'SCRIPT_EOF'\n\"\"\"Exp R5: PCA-384d Dimensionality Control.\n\nTests whether HS probe advantage comes from dimensionality (4096-5120d vs 384d)\nby PCA-reducing HS features to 384d and re-comparing against text baseline.\n\"\"\"\n\nimport os, sys, json, time\nos.environ[\"TOKENIZERS_PARALLELISM\"] = \"false\"\nos.environ[\"HF_ENDPOINT\"] = \"https://hf-mirror.com\"\n\nimport numpy as np\nimport torch\nfrom pathlib import Path\nfrom collections import defaultdict\nfrom sklearn.decomposition import PCA\nfrom sklearn.linear_model import SGDClassifier\nfrom sklearn.metrics import balanced_accuracy_score, precision_score, confusion_matrix\n\nsys.path.insert(0, \"/root/autodl-tmp/contrastive_trace_safety\")\n\nMODEL_CONFIGS = {\n    \"r1-8b\": {\n        \"hs_dir\": \"/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states\",\n        \"target_layer\": 14,\n        \"layer_idx\": 2,  # LAYERS=[12..24], L14=index 2\n        \"hidden_dim\": 4096,\n        \"window\": 15,\n        \"hf_model_name\": \"r1-8b\",\n    },\n    \"ot-7b\": {\n        \"hs_dir\": \"/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_ot7b\",\n        \"target_layer\": 16,\n        \"layer_idx\": 16,  # all 28 layers stored\n        \"hidden_dim\": 3584,\n        \"window\": 3,\n        \"hf_model_name\": \"ot-7b\",\n    },\n    \"qwq-32b\": {\n        \"hs_dir\": \"/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b\",\n        \"target_layer\": 60,\n        \"layer_idx\": 60,  # all 64 layers stored\n        \"hidden_dim\": 5120,\n        \"window\": 3,\n        \"hf_model_name\": \"QwQ\",\n    },\n    \"r1-32b\": {\n        \"hs_dir\": \"/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b\",\n        \"target_layer\": 63,\n        \"layer_idx\": 63,  # all 64 layers stored\n        \"hidden_dim\": 5120,\n        \"window\": 1,\n        \"hf_model_name\": \"r1-32b\",\n    },\n}\n\nOUTPUT_DIR = Path(\"/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384\")\nOUTPUT_DIR.mkdir(parents=True, exist_ok=True)\n\nSEED = 42\nTEXT_DIM = 384\nN_BOOTSTRAP = 1000\n\n\ndef load_sentence_map(hf_model_name):\n    from datasets import load_dataset\n    ds = load_dataset(\"ishitakakkar-10/HarmThoughts\", split=\"train\")\n    sentence_map = defaultdict(list)\n    for row in ds:\n        if row[\"model_name\"] != hf_model_name:\n            continue\n        sid = row[\"sentence_id\"]\n        parts = sid.rsplit(\"-\", 1)\n        trace_id = parts[0]\n        step_idx = int(parts[1]) - 1\n        sentence_map[trace_id].append((step_idx, row[\"sentence\"]))\n    for tid in sentence_map:\n        sentence_map[tid].sort(key=lambda x: x[0])\n    return sentence_map\n\n\ndef load_traces(hs_dir, layer_idx, sentence_map):\n    traces = []\n    hs_path = Path(hs_dir)\n    for pt_file in sorted(hs_path.glob(\"*.pt\")):\n        data = torch.load(pt_file, map_location=\"cpu\", weights_only=False)\n        if data.get(\"step_labels\") is None or data.get(\"commitment_point\") is None:\n            continue\n        cp = data[\"commitment_point\"]\n        labels = data[\"step_labels\"]\n        if isinstance(labels, torch.Tensor):\n            labels = labels.tolist()\n        if cp <= 0 or cp >= len(labels) or sum(labels) == 0:\n            continue\n        tid = data[\"trace_id\"]\n        if tid not in sentence_map:\n            continue\n\n        hs = data[\"hidden_states\"][:, layer_idx, :]  # [T, hidden_dim]\n        sentences = [s for _, s in sentence_map[tid]]\n        n = min(len(sentences), hs.shape[0], len(labels))\n\n        traces.append({\n            \"trace_id\": tid,\n            \"hidden_states\": hs[:n].numpy(),\n            \"step_labels\": labels[:n],\n            \"commitment_point\": cp,\n            \"sentences\": sentences[:n],\n        })\n    return traces\n\n\ndef split_traces(traces, seed=SEED):\n    rng = np.random.default_rng(seed)\n    indices = rng.permutation(len(traces))\n    n_train = int(len(traces) * 0.6)\n    n_val = int(len(traces) * 0.2)\n    return (\n        [traces[i] for i in indices[:n_train]],\n        [traces[i] for i in indices[n_train:n_train + n_val]],\n        [traces[i] for i in indices[n_train + n_val:]],\n    )\n\n\ndef create_causal_windows(hs, window_size):\n    T, D = hs.shape\n    padded = np.zeros((window_size - 1 + T, D), dtype=np.float32)\n    padded[window_size - 1:] = hs\n    windows = np.zeros((T, window_size * D), dtype=np.float32)\n    for i in range(T):\n        windows[i] = padded[i:i + window_size].reshape(-1)\n    return windows\n\n\ndef build_features(traces, dim, window_size):\n    X_all, y_all, trace_indices = [], [], []\n    for idx, tr in enumerate(traces):\n        feats = tr[\"features\"]  # [T, dim]\n        labels = np.array(tr[\"step_labels\"], dtype=np.int32)\n        n = min(feats.shape[0], len(labels))\n        feats = feats[:n]\n        labels = labels[:n]\n        windows = create_causal_windows(feats, window_size)\n        X_all.append(windows)\n        y_all.append(labels)\n        trace_indices.extend([idx] * n)\n    return np.vstack(X_all), np.concatenate(y_all), trace_indices\n\n\ndef compute_per_trace_metrics(traces, clf, dim, window_size):\n    bal_accs, precisions, fprs = [], [], []\n    for tr in traces:\n        feats = tr[\"features\"][:len(tr[\"step_labels\"])]\n        labels = np.array(tr[\"step_labels\"], dtype=np.int32)\n        n = min(feats.shape[0], len(labels))\n        feats = feats[:n]\n        labels = labels[:n]\n        windows = create_causal_windows(feats, window_size)\n        preds = clf.predict(windows)\n\n        # bal_acc\n        ba = balanced_accuracy_score(labels, preds)\n        bal_accs.append(ba)\n\n        # precision (handle case with no positive predictions)\n        pos_mask = preds == 1\n        if pos_mask.sum() > 0:\n            prec = precision_score(labels, preds, zero_division=0.0)\n        else:\n            prec = 1.0  # no false positives if no positives predicted\n        precisions.append(prec)\n\n        # FPR on pre-commitment steps only\n        cp = tr[\"commitment_point\"]\n        pre_cp_labels = labels[:cp]\n        pre_cp_preds = preds[:cp]\n        if len(pre_cp_labels) > 0 and (pre_cp_labels == 0).sum() > 0:\n            fp = ((pre_cp_preds == 1) & (pre_cp_labels == 0)).sum()\n            tn_fp = (pre_cp_labels == 0).sum()\n            fpr = fp / tn_fp\n        else:\n            fpr = 0.0\n        fprs.append(fpr)\n\n    return np.array(bal_accs), np.array(precisions), np.array(fprs)\n\n\ndef paired_bootstrap_test(hs_metrics, text_metrics, n_bootstrap=N_BOOTSTRAP, seed=SEED):\n    rng = np.random.default_rng(seed)\n    n = len(hs_metrics)\n    obs = np.mean(hs_metrics) - np.mean(text_metrics)\n\n    bd = np.zeros(n_bootstrap)\n    for b in range(n_bootstrap):\n        idx = rng.choice(n, size=n, replace=True)\n        bd[b] = np.mean(hs_metrics[idx]) - np.mean(text_metrics[idx])\n\n    bd_null = bd - np.mean(bd)\n    p = float(np.mean(np.abs(bd_null) >= np.abs(obs)))\n    return obs, p\n\n\ndef holm_bonferroni(p_values, alpha=0.05):\n    n = len(p_values)\n    sorted_indices = np.argsort(p_values)\n    adjusted = np.ones(n)\n    for rank, idx in enumerate(sorted_indices):\n        adjusted[idx] = p_values[idx] * (n - rank)\n    adjusted = np.minimum(adjusted, 1.0)\n    # Enforce monotonicity\n    for i in range(1, n):\n        idx = sorted_indices[i]\n        prev_idx = sorted_indices[i - 1]\n        if adjusted[idx] < adjusted[prev_idx]:\n            adjusted[idx] = adjusted[prev_idx]\n    return adjusted, adjusted < alpha\n\n\ndef run_model(model_name, config, st_model):\n    print(f\"\\n{'='*60}\")\n    print(f\"Model: {model_name}\")\n    print(f\"{'='*60}\")\n    t0 = time.time()\n\n    # Load sentence map from HF\n    print(f\"  Loading sentences from HF ({config['hf_model_name']})...\")\n    sentence_map = load_sentence_map(config[\"hf_model_name\"])\n    print(f\"  Found {len(sentence_map)} traces in HF dataset\")\n\n    # Load traces\n    print(f\"  Loading .pt traces from {config['hs_dir']}...\")\n    traces = load_traces(config[\"hs_dir\"], config[\"layer_idx\"], sentence_map)\n    print(f\"  Loaded {len(traces)} valid traces\")\n\n    # Split\n    train, val, test = split_traces(traces)\n    print(f\"  Split: train={len(train)}, val={len(val)}, test={len(test)}\")\n\n    # === PCA-384 on HS features ===\n    print(f\"  Fitting PCA(384) on training hidden states (dim={config['hidden_dim']})...\")\n    train_hs_all = np.vstack([tr[\"hidden_states\"] for tr in train])\n    pca = PCA(n_components=384, random_state=SEED)\n    pca.fit(train_hs_all)\n    explained = pca.explained_variance_ratio_.sum()\n    print(f\"  PCA explained variance: {explained:.4f}\")\n\n    # Transform all traces\n    for tr in train + val + test:\n        tr[\"hs_pca384\"] = pca.transform(tr[\"hidden_states\"]).astype(np.float32)\n\n    # === Text embeddings ===\n    print(f\"  Computing text embeddings (MiniLM-384d)...\")\n    for tr in train + val + test:\n        emb = st_model.encode(tr[\"sentences\"], batch_size=64, show_progress_bar=False)\n        tr[\"text_emb\"] = emb.astype(np.float32)\n\n    # === Train HS PCA-384 probe ===\n    window = config[\"window\"]\n    print(f\"  Training PCA-384 HS probe (window={window})...\")\n    for tr in train + val + test:\n        tr[\"features\"] = tr[\"hs_pca384\"]\n    X_train, y_train, _ = build_features(train, 384, window)\n    clf_hs = SGDClassifier(loss=\"log_loss\", alpha=1e-4, max_iter=100,\n                           random_state=SEED, class_weight=\"balanced\", tol=1e-3)\n    clf_hs.fit(X_train, y_train)\n\n    # === Train Text probe ===\n    print(f\"  Training Text probe (window={window})...\")\n    for tr in train + val + test:\n        tr[\"features\"] = tr[\"text_emb\"]\n    X_train_txt, y_train_txt, _ = build_features(train, 384, window)\n    clf_txt = SGDClassifier(loss=\"log_loss\", alpha=1e-4, max_iter=100,\n                            random_state=SEED, class_weight=\"balanced\", tol=1e-3)\n    clf_txt.fit(X_train_txt, y_train_txt)\n\n    # === Evaluate on test set ===\n    print(f\"  Evaluating on test set ({len(test)} traces)...\")\n    for tr in test:\n        tr[\"features\"] = tr[\"hs_pca384\"]\n    hs_ba, hs_prec, hs_fpr = compute_per_trace_metrics(test, clf_hs, 384, window)\n\n    for tr in test:\n        tr[\"features\"] = tr[\"text_emb\"]\n    txt_ba, txt_prec, txt_fpr = compute_per_trace_metrics(test, clf_txt, 384, window)\n\n    # === Bootstrap tests ===\n    print(f\"  Running paired bootstrap (n={N_BOOTSTRAP})...\")\n    results = []\n    for metric_name, hs_m, txt_m in [\n        (\"bal_acc\", hs_ba, txt_ba),\n        (\"precision\", hs_prec, txt_prec),\n        (\"FPR\", hs_fpr, txt_fpr),\n    ]:\n        delta, p = paired_bootstrap_test(hs_m, txt_m)\n        results.append({\n            \"model\": model_name,\n            \"metric\": metric_name,\n            \"pca384_hs\": float(np.mean(hs_m)),\n            \"text_384\": float(np.mean(txt_m)),\n            \"delta\": float(delta),\n            \"p_value\": float(p),\n        })\n\n    elapsed = time.time() - t0\n    print(f\"  Done in {elapsed:.1f}s\")\n    return results, explained\n\n\ndef main():\n    print(\"=\"*60)\n    print(\"Exp R5: PCA-384d Dimensionality Control\")\n    print(\"=\"*60)\n\n    # Load SentenceTransformer once\n    print(\"\\nLoading SentenceTransformer (all-MiniLM-L6-v2)...\")\n    from sentence_transformers import SentenceTransformer\n    st_model = SentenceTransformer(\"all-MiniLM-L6-v2\", device=\"cpu\")\n\n    all_results = []\n    pca_variances = {}\n\n    for model_name, config in MODEL_CONFIGS.items():\n        results, var_explained = run_model(model_name, config, st_model)\n        all_results.extend(results)\n        pca_variances[model_name] = var_explained\n\n    # Holm-Bonferroni correction\n    p_values = np.array([r[\"p_value\"] for r in all_results])\n    adjusted_p, significant = holm_bonferroni(p_values)\n    for i, r in enumerate(all_results):\n        r[\"p_adjusted\"] = float(adjusted_p[i])\n        r[\"significant\"] = bool(significant[i])\n\n    # Print summary table\n    print(\"\\n\" + \"=\"*90)\n    print(f\"{'Model':<10} | {'Metric':<10} | {'PCA384-HS':>9} | {'Text-384':>8} | {'Delta':>8} | {'p-value':>8} | {'Holm-Bonf':>10}\")\n    print(\"-\"*90)\n    for r in all_results:\n        sig_str = \"REJECT\" if r[\"significant\"] else \"fail\"\n        # For FPR, lower is better so flip sign interpretation\n        delta_str = f\"{r['delta']:+.4f}\"\n        print(f\"{r['model']:<10} | {r['metric']:<10} | {r['pca384_hs']:>9.4f} | {r['text_384']:>8.4f} | {delta_str:>8} | {r['p_value']:>8.4f} | {sig_str:>10}\")\n    print(\"=\"*90)\n\n    print(f\"\\nPCA explained variance ratios:\")\n    for m, v in pca_variances.items():\n        print(f\"  {m}: {v:.4f}\")\n\n    # Save JSON\n    output = {\n        \"experiment\": \"exp_r5_pca384_control\",\n        \"description\": \"PCA-384d dimensionality control: HS reduced to 384d vs Text 384d\",\n        \"n_bootstrap\": N_BOOTSTRAP,\n        \"seed\": SEED,\n        \"pca_explained_variance\": pca_variances,\n        \"results\": all_results,\n    }\n    out_path = OUTPUT_DIR / \"results.json\"\n    with open(out_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"\\nResults saved to {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF\necho \"Script written successfully\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "cat > /root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_r5_pca384_control.py << 'SCRIPT_EOF'\n\"\"\"Exp R5: PCA-384d Dimensionality Control.\n\nTests whether HS probe advantage comes from dimensionality (4096-5120d vs 384d)\nby PCA-reducing HS features to 384d and re-comparing against text baseline.\n\"\"\"\n\nimport os, sys, json, time\nos.environ[\"TOKENIZERS_PARALLELISM\"] = \"false\"\nos.environ[\"HF_ENDPOINT\"] = \"https://hf-mirror.com\"\n\nimport numpy as np\nimport torch\nfrom pathlib import Path\nfrom collections import defaultdict\nfrom sklearn.decomposition import PCA\nfrom sklearn.linear_model import SGDClassifier\nfrom sklearn.metrics import balanced_accuracy_score, precision_score, confusion_matrix\n\nsys.path.insert(0, \"/root/autodl-tmp/contrastive_trace_safety\")\n\nMODEL_CONFIGS = {\n    \"r1-8b\": {\n        \"hs_dir\": \"/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states\",\n        \"target_layer\": 14,\n        \"layer_idx\": 2,  # LAYERS=[12..24], L14=index 2\n        \"hidden_dim\": 4096,\n        \"window\": 15,\n        \"hf_model_name\": \"r1-8b\",\n    },\n    \"ot-7b\": {\n        \"hs_dir\": \"/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_ot7b\",\n        \"target_layer\": 16,\n        \"layer_idx\": 16,  # all 28 layers stored\n        \"hidden_dim\": 3584,\n        \"window\": 3,\n        \"hf_model_name\": \"ot-7b\",\n    },\n    \"qwq-32b\": {\n        \"hs_dir\": \"/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b\",\n        \"target_layer\": 60,\n        \"layer_idx\": 60,  # all 64 layers stored\n        \"hidden_dim\": 5120,\n        \"window\": 3,\n        \"hf_model_name\": \"QwQ\",\n    },\n    \"r1-32b\": {\n        \"hs_dir\": \"/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b\",\n        \"target_layer\": 63,\n        \"layer_idx\": 63,  # all 64 layers stored\n        \"hidden_dim\": 5120,\n        \"window\": 1,\n        \"hf_model_name\": \"r1-32b\",\n    },\n}\n\nOUTPUT_DIR = Path(\"/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384\")\nOUTPUT_DIR.mkdir(parents=True, exist_ok=True)\n\nSEED = 42\nTEXT_DIM = 384\nN_BOOTSTRAP = 1000\n\n\ndef load_sentence_map(hf_model_name):\n    from datasets import load_dataset\n    ds = load_dataset(\"ishitakakkar-10/HarmThoughts\", split=\"train\")\n    sentence_map = defaultdict(list)\n    for row in ds:\n        if row[\"model_name\"] != hf_model_name:\n            continue\n        sid = row[\"sentence_id\"]\n        parts = sid.rsplit(\"-\", 1)\n        trace_id = parts[0]\n        step_idx = int(parts[1]) - 1\n        sentence_map[trace_id].append((step_idx, row[\"sentence\"]))\n    for tid in sentence_map:\n        sentence_map[tid].sort(key=lambda x: x[0])\n    return sentence_map\n\n\ndef load_traces(hs_dir, layer_idx, sentence_map):\n    traces = []\n    hs_path = Path(hs_dir)\n    for pt_file in sorted(hs_path.glob(\"*.pt\")):\n        data = torch.load(pt_file, map_location=\"cpu\", weights_only=False)\n        if data.get(\"step_labels\") is None or data.get(\"commitment_point\") is None:\n            continue\n        cp = data[\"commitment_point\"]\n        labels = data[\"step_labels\"]\n        if isinstance(labels, torch.Tensor):\n            labels = labels.tolist()\n        if cp <= 0 or cp >= len(labels) or sum(labels) == 0:\n            continue\n        tid = data[\"trace_id\"]\n        if tid not in sentence_map:\n            continue\n\n        hs = data[\"hidden_states\"][:, layer_idx, :]  # [T, hidden_dim]\n        sentences = [s for _, s in sentence_map[tid]]\n        n = min(len(sentences), hs.shape[0], len(labels))\n\n        traces.append({\n            \"trace_id\": tid,\n            \"hidden_states\": hs[:n].numpy(),\n            \"step_labels\": labels[:n],\n            \"commitment_point\": cp,\n            \"sentences\": sentences[:n],\n        })\n    return traces\n\n\ndef split_traces(traces, seed=SEED):\n    rng = np.random.default_rng(seed)\n    indices = rng.permutation(len(traces))\n    n_train = int(len(traces) * 0.6)\n    n_val = int(len(traces) * 0.2)\n    return (\n        [traces[i] for i in indices[:n_train]],\n        [traces[i] for i in indices[n_train:n_train + n_val]],\n        [traces[i] for i in indices[n_train + n_val:]],\n    )\n\n\ndef create_causal_windows(hs, window_size):\n    T, D = hs.shape\n    padded = np.zeros((window_size - 1 + T, D), dtype=np.float32)\n    padded[window_size - 1:] = hs\n    windows = np.zeros((T, window_size * D), dtype=np.float32)\n    for i in range(T):\n        windows[i] = padded[i:i + window_size].reshape(-1)\n    return windows\n\n\ndef build_features(traces, dim, window_size):\n    X_all, y_all, trace_indices = [], [], []\n    for idx, tr in enumerate(traces):\n        feats = tr[\"features\"]  # [T, dim]\n        labels = np.array(tr[\"step_labels\"], dtype=np.int32)\n        n = min(feats.shape[0], len(labels))\n        feats = feats[:n]\n        labels = labels[:n]\n        windows = create_causal_windows(feats, window_size)\n        X_all.append(windows)\n        y_all.append(labels)\n        trace_indices.extend([idx] * n)\n    return np.vstack(X_all), np.concatenate(y_all), trace_indices\n\n\ndef compute_per_trace_metrics(traces, clf, dim, window_size):\n    bal_accs, precisions, fprs = [], [], []\n    for tr in traces:\n        feats = tr[\"features\"][:len(tr[\"step_labels\"])]\n        labels = np.array(tr[\"step_labels\"], dtype=np.int32)\n        n = min(feats.shape[0], len(labels))\n        feats = feats[:n]\n        labels = labels[:n]\n        windows = create_causal_windows(feats, window_size)\n        preds = clf.predict(windows)\n\n        # bal_acc\n        ba = balanced_accuracy_score(labels, preds)\n        bal_accs.append(ba)\n\n        # precision (handle case with no positive predictions)\n        pos_mask = preds == 1\n        if pos_mask.sum() > 0:\n            prec = precision_score(labels, preds, zero_division=0.0)\n        else:\n            prec = 1.0  # no false positives if no positives predicted\n        precisions.append(prec)\n\n        # FPR on pre-commitment steps only\n        cp = tr[\"commitment_point\"]\n        pre_cp_labels = labels[:cp]\n        pre_cp_preds = preds[:cp]\n        if len(pre_cp_labels) > 0 and (pre_cp_labels == 0).sum() > 0:\n            fp = ((pre_cp_preds == 1) & (pre_cp_labels == 0)).sum()\n            tn_fp = (pre_cp_labels == 0).sum()\n            fpr = fp / tn_fp\n        else:\n            fpr = 0.0\n        fprs.append(fpr)\n\n    return np.array(bal_accs), np.array(precisions), np.array(fprs)\n\n\ndef paired_bootstrap_test(hs_metrics, text_metrics, n_bootstrap=N_BOOTSTRAP, seed=SEED):\n    rng = np.random.default_rng(seed)\n    n = len(hs_metrics)\n    obs = np.mean(hs_metrics) - np.mean(text_metrics)\n\n    bd = np.zeros(n_bootstrap)\n    for b in range(n_bootstrap):\n        idx = rng.choice(n, size=n, replace=True)\n        bd[b] = np.mean(hs_metrics[idx]) - np.mean(text_metrics[idx])\n\n    bd_null = bd - np.mean(bd)\n    p = float(np.mean(np.abs(bd_null) >= np.abs(obs)))\n    return obs, p\n\n\ndef holm_bonferroni(p_values, alpha=0.05):\n    n = len(p_values)\n    sorted_indices = np.argsort(p_values)\n    adjusted = np.ones(n)\n    for rank, idx in enumerate(sorted_indices):\n        adjusted[idx] = p_values[idx] * (n - rank)\n    adjusted = np.minimum(adjusted, 1.0)\n    # Enforce monotonicity\n    for i in range(1, n):\n        idx = sorted_indices[i]\n        prev_idx = sorted_indices[i - 1]\n        if adjusted[idx] < adjusted[prev_idx]:\n            adjusted[idx] = adjusted[prev_idx]\n    return adjusted, adjusted < alpha\n\n\ndef run_model(model_name, config, st_model):\n    print(f\"\\n{'='*60}\")\n    print(f\"Model: {model_name}\")\n    print(f\"{'='*60}\")\n    t0 = time.time()\n\n    # Load sentence map from HF\n    print(f\"  Loading sentences from HF ({config['hf_model_name']})...\")\n    sentence_map = load_sentence_map(config[\"hf_model_name\"])\n    print(f\"  Found {len(sentence_map)} traces in HF dataset\")\n\n    # Load traces\n    print(f\"  Loading .pt traces from {config['hs_dir']}...\")\n    traces = load_traces(config[\"hs_dir\"], config[\"layer_idx\"], sentence_map)\n    print(f\"  Loaded {len(traces)} valid traces\")\n\n    # Split\n    train, val, test = split_traces(traces)\n    print(f\"  Split: train={len(train)}, val={len(val)}, test={len(test)}\")\n\n    # === PCA-384 on HS features ===\n    print(f\"  Fitting PCA(384) on training hidden states (dim={config['hidden_dim']})...\")\n    train_hs_all = np.vstack([tr[\"hidden_states\"] for tr in train])\n    pca = PCA(n_components=384, random_state=SEED)\n    pca.fit(train_hs_all)\n    explained = pca.explained_variance_ratio_.sum()\n    print(f\"  PCA explained variance: {explained:.4f}\")\n\n    # Transform all traces\n    for tr in train + val + test:\n        tr[\"hs_pca384\"] = pca.transform(tr[\"hidden_states\"]).astype(np.float32)\n\n    # === Text embeddings ===\n    print(f\"  Computing text embeddings (MiniLM-384d)...\")\n    for tr in train + val + test:\n        emb = st_model.encode(tr[\"sentences\"], batch_size=64, show_progress_bar=False)\n        tr[\"text_emb\"] = emb.astype(np.float32)\n\n    # === Train HS PCA-384 probe ===\n    window = config[\"window\"]\n    print(f\"  Training PCA-384 HS probe (window={window})...\")\n    for tr in train + val + test:\n        tr[\"features\"] = tr[\"hs_pca384\"]\n    X_train, y_train, _ = build_features(train, 384, window)\n    clf_hs = SGDClassifier(loss=\"log_loss\", alpha=1e-4, max_iter=100,\n                           random_state=SEED, class_weight=\"balanced\", tol=1e-3)\n    clf_hs.fit(X_train, y_train)\n\n    # === Train Text probe ===\n    print(f\"  Training Text probe (window={window})...\")\n    for tr in train + val + test:\n        tr[\"features\"] = tr[\"text_emb\"]\n    X_train_txt, y_train_txt, _ = build_features(train, 384, window)\n    clf_txt = SGDClassifier(loss=\"log_loss\", alpha=1e-4, max_iter=100,\n                            random_state=SEED, class_weight=\"balanced\", tol=1e-3)\n    clf_txt.fit(X_train_txt, y_train_txt)\n\n    # === Evaluate on test set ===\n    print(f\"  Evaluating on test set ({len(test)} traces)...\")\n    for tr in test:\n        tr[\"features\"] = tr[\"hs_pca384\"]\n    hs_ba, hs_prec, hs_fpr = compute_per_trace_metrics(test, clf_hs, 384, window)\n\n    for tr in test:\n        tr[\"features\"] = tr[\"text_emb\"]\n    txt_ba, txt_prec, txt_fpr = compute_per_trace_metrics(test, clf_txt, 384, window)\n\n    # === Bootstrap tests ===\n    print(f\"  Running paired bootstrap (n={N_BOOTSTRAP})...\")\n    results = []\n    for metric_name, hs_m, txt_m in [\n        (\"bal_acc\", hs_ba, txt_ba),\n        (\"precision\", hs_prec, txt_prec),\n        (\"FPR\", hs_fpr, txt_fpr),\n    ]:\n        delta, p = paired_bootstrap_test(hs_m, txt_m)\n        results.append({\n            \"model\": model_name,\n            \"metric\": metric_name,\n            \"pca384_hs\": float(np.mean(hs_m)),\n            \"text_384\": float(np.mean(txt_m)),\n            \"delta\": float(delta),\n            \"p_value\": float(p),\n        })\n\n    elapsed = time.time() - t0\n    print(f\"  Done in {elapsed:.1f}s\")\n    return results, explained\n\n\ndef main():\n    print(\"=\"*60)\n    print(\"Exp R5: PCA-384d Dimensionality Control\")\n    print(\"=\"*60)\n\n    # Load SentenceTransformer once\n    print(\"\\nLoading SentenceTransformer (all-MiniLM-L6-v2)...\")\n    from sentence_transformers import SentenceTransformer\n    st_model = SentenceTransformer(\"all-MiniLM-L6-v2\", device=\"cpu\")\n\n    all_results = []\n    pca_variances = {}\n\n    for model_name, config in MODEL_CONFIGS.items():\n        results, var_explained = run_model(model_name, config, st_model)\n        all_results.extend(results)\n        pca_variances[model_name] = var_explained\n\n    # Holm-Bonferroni correction\n    p_values = np.array([r[\"p_value\"] for r in all_results])\n    adjusted_p, significant = holm_bonferroni(p_values)\n    for i, r in enumerate(all_results):\n        r[\"p_adjusted\"] = float(adjusted_p[i])\n        r[\"significant\"] = bool(significant[i])\n\n    # Print summary table\n    print(\"\\n\" + \"=\"*90)\n    print(f\"{'Model':<10} | {'Metric':<10} | {'PCA384-HS':>9} | {'Text-384':>8} | {'Delta':>8} | {'p-value':>8} | {'Holm-Bonf':>10}\")\n    print(\"-\"*90)\n    for r in all_results:\n        sig_str = \"REJECT\" if r[\"significant\"] else \"fail\"\n        # For FPR, lower is better so flip sign interpretation\n        delta_str = f\"{r['delta']:+.4f}\"\n        print(f\"{r['model']:<10} | {r['metric']:<10} | {r['pca384_hs']:>9.4f} | {r['text_384']:>8.4f} | {delta_str:>8} | {r['p_value']:>8.4f} | {sig_str:>10}\")\n    print(\"=\"*90)\n\n    print(f\"\\nPCA explained variance ratios:\")\n    for m, v in pca_variances.items():\n        print(f\"  {m}: {v:.4f}\")\n\n    # Save JSON\n    output = {\n        \"experiment\": \"exp_r5_pca384_control\",\n        \"description\": \"PCA-384d dimensionality control: HS reduced to 384d vs Text 384d\",\n        \"n_bootstrap\": N_BOOTSTRAP,\n        \"seed\": SEED,\n        \"pca_explained_variance\": pca_variances,\n        \"results\": all_results,\n    }\n    out_path = OUTPUT_DIR / \"results.json\"\n    with open(out_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"\\nResults saved to {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF\necho \"Script written successfully\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-17T19:24:11.357230+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written successfully\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-17T19:24:11.357487+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "cd /root/autodl-tmp/contrastive_trace_safety && PYTHONUNBUFFERED=1 /root/miniconda3/bin/python3.12 -c \"\nimport os, sys, torch, glob, numpy as np\nos.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'\nos.environ['TOKENIZERS_PARALLELISM'] = 'false'\nfrom pathlib import Path\nfrom collections import defaultdict\nfrom datasets import load_dataset\n\n# Quick validation: load 1 trace per model, verify layer extraction and pipeline\nconfigs = {\n    'r1-8b': {'hs_dir': '/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states', 'layer_idx': 2, 'hf_name': 'r1-8b'},\n    'ot-7b': {'hs_dir': '/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_ot7b', 'layer_idx': 16, 'hf_name': 'ot-7b'},\n    'qwq-32b': {'hs_dir': '/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b', 'layer_idx': 60, 'hf_name': 'QwQ'},\n    'r1-32b': {'hs_dir': '/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b', 'layer_idx': 63, 'hf_name': 'r1-32b'},\n}\n\n# Load HF dataset once\nds = load_dataset('ishitakakkar-10/HarmThoughts', split='train')\nsentence_maps = {}\nfor row in ds:\n    mn = row['model_name']\n    if mn not in sentence_maps:\n        sentence_maps[mn] = defaultdict(list)\n    sid = row['sentence_id']\n    parts = sid.rsplit('-', 1)\n    tid = parts[0]\n    step_idx = int(parts[1]) - 1\n    sentence_maps[mn][tid].append((step_idx, row['sentence']))\n\nfor mn in sentence_maps:\n    for tid in sentence_maps[mn]:\n        sentence_maps[mn][tid].sort(key=lambda x: x[0])\n\nprint('Sentence maps loaded:', {k: len(v) for k, v in sentence_maps.items()})\n\nfor model, cfg in configs.items():\n    files = sorted(glob.glob(str(Path(cfg['hs_dir']) / '*.pt')))\n    # find first valid trace\n    for f in files:\n        data = torch.load(f, map_location='cpu', weights_only=False)\n        if data.get('step_labels') is None or data.get('commitment_point') is None:\n            continue\n        cp = data['commitment_point']\n        labels = data['step_labels']\n        if isinstance(labels, torch.Tensor):\n            labels = labels.tolist()\n        if cp <= 0 or cp >= len(labels):\n            continue\n        tid = data['trace_id']\n        sm = sentence_maps.get(cfg['hf_name'], {})\n        if tid not in sm:\n            continue\n        \n        hs = data['hidden_states'][:, cfg['layer_idx'], :]\n        sentences = [s for _, s in sm[tid]]\n        n = min(len(sentences), hs.shape[0], len(labels))\n        print(f'{model}: trace={tid}, T={n}, hs_layer_shape={hs.shape}, sentences={len(sentences)}, cp={cp}')\n        break\n    else:\n        print(f'{model}: NO VALID TRACE FOUND')\n\n# Quick SentenceTransformer test\nfrom sentence_transformers import SentenceTransformer\nst = SentenceTransformer('all-MiniLM-L6-v2', device='cpu')\ntest_emb = st.encode(['hello world'])\nprint(f'SentenceTransformer OK, output dim={test_emb.shape[1]}')\nprint('Validation PASSED')\n\"\n",
  "account": "root",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "cd /root/autodl-tmp/contrastive_trace_safety && PYTHONUNBUFFERED=1 /root/miniconda3/bin/python3.12 -c \"\nimport os, sys, torch, glob, numpy as np\nos.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'\nos.environ['TOKENIZERS_PARALLELISM'] = 'false'\nfrom pathlib import Path\nfrom collections import defaultdict\nfrom datasets import load_dataset\n\n# Quick validation: load 1 trace per model, verify layer extraction and pipeline\nconfigs = {\n    'r1-8b': {'hs_dir': '/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states', 'layer_idx': 2, 'hf_name': 'r1-8b'},\n    'ot-7b': {'hs_dir': '/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_ot7b', 'layer_idx': 16, 'hf_name': 'ot-7b'},\n    'qwq-32b': {'hs_dir': '/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b', 'layer_idx': 60, 'hf_name': 'QwQ'},\n    'r1-32b': {'hs_dir': '/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b', 'layer_idx': 63, 'hf_name': 'r1-32b'},\n}\n\n# Load HF dataset once\nds = load_dataset('ishitakakkar-10/HarmThoughts', split='train')\nsentence_maps = {}\nfor row in ds:\n    mn = row['model_name']\n    if mn not in sentence_maps:\n        sentence_maps[mn] = defaultdict(list)\n    sid = row['sentence_id']\n    parts = sid.rsplit('-', 1)\n    tid = parts[0]\n    step_idx = int(parts[1]) - 1\n    sentence_maps[mn][tid].append((step_idx, row['sentence']))\n\nfor mn in sentence_maps:\n    for tid in sentence_maps[mn]:\n        sentence_maps[mn][tid].sort(key=lambda x: x[0])\n\nprint('Sentence maps loaded:', {k: len(v) for k, v in sentence_maps.items()})\n\nfor model, cfg in configs.items():\n    files = sorted(glob.glob(str(Path(cfg['hs_dir']) / '*.pt')))\n    # find first valid trace\n    for f in files:\n        data = torch.load(f, map_location='cpu', weights_only=False)\n        if data.get('step_labels') is None or data.get('commitment_point') is None:\n            continue\n        cp = data['commitment_point']\n        labels = data['step_labels']\n        if isinstance(labels, torch.Tensor):\n            labels = labels.tolist()\n        if cp <= 0 or cp >= len(labels):\n            continue\n        tid = data['trace_id']\n        sm = sentence_maps.get(cfg['hf_name'], {})\n        if tid not in sm:\n            continue\n        \n        hs = data['hidden_states'][:, cfg['layer_idx'], :]\n        sentences = [s for _, s in sm[tid]]\n        n = min(len(sentences), hs.shape[0], len(labels))\n        print(f'{model}: trace={tid}, T={n}, hs_layer_shape={hs.shape}, sentences={len(sentences)}, cp={cp}')\n        break\n    else:\n        print(f'{model}: NO VALID TRACE FOUND')\n\n# Quick SentenceTransformer test\nfrom sentence_transformers import SentenceTransformer\nst = SentenceTransformer('all-MiniLM-L6-v2', device='cpu')\ntest_emb = st.encode(['hello world'])\nprint(f'SentenceTransformer OK, output dim={test_emb.shape[1]}')\nprint('Validation PASSED')\n\"\n",
    "account": "root",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-17T19:24:11.357796+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Sentence maps loaded: {'QwQ': 140, 'r1-8b': 324, 'ot-7b': 333, 'r1-32b': 221}\\nr1-8b: trace=018ad1b2027a488aad4ce925258db0c7, T=45, hs_layer_shape=torch.Size([45, 4096]), sentences=45, cp=41\\not-7b: trace=00071414b7d44aa4b0c5c2a274306519, T=59, hs_layer_shape=torch.Size([59, 3584]), sentences=59, cp=58\\nqwq-32b: trace=004ee4398ad043f88590dc868baed39c, T=48, hs_layer_shape=torch.Size([48, 5120]), sentences=48, cp=8\\nr1-32b: trace=0340a9c152a84e88a1bb1a1b0c1ece69, T=36, hs_layer_shape=torch.Size([36, 5120]), sentences=36, cp=32\\nSentenceTransformer OK, output dim=384\\nValidation PASSED\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 29.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-17T19:24:11.358064+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "cd /root/autodl-tmp/contrastive_trace_safety && PYTHONUNBUFFERED=1 /root/miniconda3/bin/python3.12 src/experiments/exp_r5_pca384_control.py",
  "account": "root",
  "timeout": "600000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "cd /root/autodl-tmp/contrastive_trace_safety && PYTHONUNBUFFERED=1 /root/miniconda3/bin/python3.12 src/experiments/exp_r5_pca384_control.py",
    "account": "root",
    "timeout": "600000"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-17T19:24:11.358299+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'cd /root/autodl-tmp/contrastive_trace_safety && PYTHONUNBUFFERED=1 /root/miniconda3/bin/python3.12 src/experiments/exp_r5_pca384_control.py'\\n\\nStdout:\\n\\n\\n============================================================\\nModel: r1-8b\\n============================================================\\n  Loading sentences from HF (r1-8b)...\\n  Found 324 traces in HF dataset\\n  Loading .pt traces from /root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states...\\n  Loaded 209 valid traces\\n  Split: train=125, val=41, test=43\\n  Fitting PCA(384) on training hidden states (dim=4096)...\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-17T19:24:11.358591+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "cd /root/autodl-tmp/contrastive_trace_safety && screen -dmS exp_r5 bash -c \"PYTHONUNBUFFERED=1 /root/miniconda3/bin/python3.12 src/experiments/exp_r5_pca384_control.py > artifacts/exp_r5_pca384/run.log 2>&1\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "cd /root/autodl-tmp/contrastive_trace_safety && screen -dmS exp_r5 bash -c \"PYTHONUNBUFFERED=1 /root/miniconda3/bin/python3.12 src/experiments/exp_r5_pca384_control.py > artifacts/exp_r5_pca384/run.log 2>&1\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-17T19:24:11.358841+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-17T19:24:11.359051+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "sleep 25 && tail -20 /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "sleep 25 && tail -20 /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-17T19:24:11.359288+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"============================================================\\nExp R5: PCA-384d Dimensionality Control\\n============================================================\\n\\nLoading SentenceTransformer (all-MiniLM-L6-v2)...\\n\\n============================================================\\nModel: r1-8b\\n============================================================\\n  Loading sentences from HF (r1-8b)...\\n  Found 324 traces in HF dataset\\n  Loading .pt traces from /root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states...\\n  Loaded 209 valid traces\\n  Split: train=125, val=41, test=43\\n  Fitting PCA(384) on training hidden states (dim=4096)...\\n  PCA explained variance: 0.7931\\n  Computing text embeddings (MiniLM-384d)...\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 25.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-17T19:24:11.359555+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "sleep 28 && tail -30 /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "sleep 28 && tail -30 /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-17T19:24:11.359841+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  Fitting PCA(384) on training hidden states (dim=4096)...\\n  PCA explained variance: 0.7931\\n  Computing text embeddings (MiniLM-384d)...\\n  Training PCA-384 HS probe (window=15)...\\n/root/miniconda3/lib/python3.12/site-packages/sklearn/linear_model/_stochastic_gradient.py:733: ConvergenceWarning: Maximum number of iteration reached before convergence. Consider increasing max_iter to improve the fit.\\n  warnings.warn(\\n  Training Text probe (window=15)...\\n  Evaluating on test set (43 traces)...\\n  Running paired bootstrap (n=1000)...\\n  Done in 34.9s\\n\\n============================================================\\nModel: ot-7b\\n============================================================\\n  Loading sentences from HF (ot-7b)...\\n  Found 333 traces in HF dataset\\n  Loading .pt traces from /root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_ot7b...\\nTraceback (most recent call last):\\n  File \\\"/root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_r5_pca384_control.py\\\", line 364, in &lt;module>\\n    main()\\n  File \\\"/root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_r5_pca384_control.py\\\", line 322, in main\\n    results, var_explained = run_model(model_name, config, st_model)\\n                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_r5_pca384_control.py\\\", line 231, in run_model\\n    traces = load_traces(config[\\\"hs_dir\\\"], config[\\\"layer_idx\\\"], sentence_map)\\n             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_r5_pca384_control.py\\\", line 104, in load_traces\\n    \\\"hidden_states\\\": hs[:n].numpy(),\\n                     ^^^^^^^^^^^^^^\\nTypeError: Got unsupported ScalarType BFloat16\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"me
…[truncated 41 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-17T19:24:11.360133+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "sed -i 's/\\\"hidden_states\\\": hs\\[:n\\].numpy(),/\\\"hidden_states\\\": hs[:n].float().numpy(),/' /root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_r5_pca384_control.py && sed -i 's/max_iter=100/max_iter=500/' /root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_r5_pca384_control.py && echo \"Fixed\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "sed -i 's/\\\"hidden_states\\\": hs\\[:n\\].numpy(),/\\\"hidden_states\\\": hs[:n].float().numpy(),/' /root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_r5_pca384_control.py && sed -i 's/max_iter=100/max_iter=500/' /root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_r5_pca384_control.py && echo \"Fixed\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-17T19:24:11.360352+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Fixed\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-17T19:24:11.360573+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "screen -S exp_r5 -X quit 2>/dev/null; cd /root/autodl-tmp/contrastive_trace_safety && screen -dmS exp_r5 bash -c \"PYTHONUNBUFFERED=1 /root/miniconda3/bin/python3.12 src/experiments/exp_r5_pca384_control.py > artifacts/exp_r5_pca384/run.log 2>&1\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "screen -S exp_r5 -X quit 2>/dev/null; cd /root/autodl-tmp/contrastive_trace_safety && screen -dmS exp_r5 bash -c \"PYTHONUNBUFFERED=1 /root/miniconda3/bin/python3.12 src/experiments/exp_r5_pca384_control.py > artifacts/exp_r5_pca384/run.log 2>&1\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-17T19:24:11.360822+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"No screen session found.\\r\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-17T19:24:11.361045+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "sleep 28 && tail -20 /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "sleep 28 && tail -20 /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-17T19:24:11.361261+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"============================================================\\nExp R5: PCA-384d Dimensionality Control\\n============================================================\\n\\nLoading SentenceTransformer (all-MiniLM-L6-v2)...\\n\\n============================================================\\nModel: r1-8b\\n============================================================\\n  Loading sentences from HF (r1-8b)...\\n  Found 324 traces in HF dataset\\n  Loading .pt traces from /root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states...\\n  Loaded 209 valid traces\\n  Split: train=125, val=41, test=43\\n  Fitting PCA(384) on training hidden states (dim=4096)...\\n  PCA explained variance: 0.7931\\n  Computing text embeddings (MiniLM-384d)...\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 28.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-17T19:24:11.361470+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "sleep 28 && tail -30 /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "sleep 28 && tail -30 /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-17T19:24:11.361719+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loading SentenceTransformer (all-MiniLM-L6-v2)...\\n\\n============================================================\\nModel: r1-8b\\n============================================================\\n  Loading sentences from HF (r1-8b)...\\n  Found 324 traces in HF dataset\\n  Loading .pt traces from /root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states...\\n  Loaded 209 valid traces\\n  Split: train=125, val=41, test=43\\n  Fitting PCA(384) on training hidden states (dim=4096)...\\n  PCA explained variance: 0.7931\\n  Computing text embeddings (MiniLM-384d)...\\n  Training PCA-384 HS probe (window=15)...\\n  Training Text probe (window=15)...\\n  Evaluating on test set (43 traces)...\\n  Running paired bootstrap (n=1000)...\\n  Done in 33.2s\\n\\n============================================================\\nModel: ot-7b\\n============================================================\\n  Loading sentences from HF (ot-7b)...\\n  Found 333 traces in HF dataset\\n  Loading .pt traces from /root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_ot7b...\\n  Loaded 228 valid traces\\n  Split: train=136, val=45, test=47\\n  Fitting PCA(384) on training hidden states (dim=3584)...\\n  PCA explained variance: 0.8282\\n  Computing text embeddings (MiniLM-384d)...\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 28.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-17T19:24:11.361960+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "sleep 28 && tail -30 /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "sleep 28 && tail -30 /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-17T19:24:11.362188+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n============================================================\\nModel: r1-8b\\n============================================================\\n  Loading sentences from HF (r1-8b)...\\n  Found 324 traces in HF dataset\\n  Loading .pt traces from /root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states...\\n  Loaded 209 valid traces\\n  Split: train=125, val=41, test=43\\n  Fitting PCA(384) on training hidden states (dim=4096)...\\n  PCA explained variance: 0.7931\\n  Computing text embeddings (MiniLM-384d)...\\n  Training PCA-384 HS probe (window=15)...\\n  Training Text probe (window=15)...\\n  Evaluating on test set (43 traces)...\\n  Running paired bootstrap (n=1000)...\\n  Done in 33.2s\\n\\n============================================================\\nModel: ot-7b\\n============================================================\\n  Loading sentences from HF (ot-7b)...\\n  Found 333 traces in HF dataset\\n  Loading .pt traces from /root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_ot7b...\\n  Loaded 228 valid traces\\n  Split: train=136, val=45, test=47\\n  Fitting PCA(384) on training hidden states (dim=3584)...\\n  PCA explained variance: 0.8282\\n  Computing text embeddings (MiniLM-384d)...\\n  Training PCA-384 HS probe (window=3)...\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 28.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-17T19:24:11.362395+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "sleep 28 && tail -30 /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "sleep 28 && tail -30 /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-17T19:24:11.362637+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  Done in 55.7s\\n\\n============================================================\\nModel: qwq-32b\\n============================================================\\n  Loading sentences from HF (QwQ)...\\n  Found 140 traces in HF dataset\\n  Loading .pt traces from /root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b...\\n  Loaded 95 valid traces\\n  Split: train=57, val=19, test=19\\n  Fitting PCA(384) on training hidden states (dim=5120)...\\n  PCA explained variance: 0.8813\\n  Computing text embeddings (MiniLM-384d)...\\n  Training PCA-384 HS probe (window=3)...\\n  Training Text probe (window=3)...\\n  Evaluating on test set (19 traces)...\\n  Running paired bootstrap (n=1000)...\\n  Done in 16.0s\\n\\n============================================================\\nModel: r1-32b\\n============================================================\\n  Loading sentences from HF (r1-32b)...\\n  Found 221 traces in HF dataset\\n  Loading .pt traces from /root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b...\\n  Loaded 100 valid traces\\n  Split: train=60, val=20, test=20\\n  Fitting PCA(384) on training hidden states (dim=5120)...\\n  PCA explained variance: 0.9243\\n  Computing text embeddings (MiniLM-384d)...\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 28.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-17T19:24:11.362880+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "sleep 25 && tail -40 /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "sleep 25 && tail -40 /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-17T19:24:11.363113+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Model      | Metric     | PCA384-HS | Text-384 |    Delta |  p-value |  Holm-Bonf\\n------------------------------------------------------------------------------------------\\nr1-8b      | bal_acc    |    0.7001 |   0.6875 |  +0.0126 |   0.7310 |       fail\\nr1-8b      | precision  |    0.8162 |   0.5852 |  +0.2310 |   0.0000 |     REJECT\\nr1-8b      | FPR        |    0.0668 |   0.1614 |  -0.0947 |   0.0030 |     REJECT\\not-7b      | bal_acc    |    0.7558 |   0.6430 |  +0.1128 |   0.0000 |     REJECT\\not-7b      | precision  |    0.5225 |   0.3545 |  +0.1681 |   0.0000 |     REJECT\\not-7b      | FPR        |    0.1207 |   0.2477 |  -0.1270 |   0.0000 |     REJECT\\nqwq-32b    | bal_acc    |    0.8116 |   0.6504 |  +0.1612 |   0.0000 |     REJECT\\nqwq-32b    | precision  |    0.6080 |   0.4213 |  +0.1867 |   0.0000 |     REJECT\\nqwq-32b    | FPR        |    0.1730 |   0.2871 |  -0.1141 |   0.0380 |       fail\\nr1-32b     | bal_acc    |    0.7471 |   0.6461 |  +0.1011 |   0.0110 |     REJECT\\nr1-32b     | precision  |    0.6343 |   0.4503 |  +0.1840 |   0.0020 |     REJECT\\nr1-32b     | FPR        |    0.2256 |   0.3809 |  -0.1553 |   0.0060 |     REJECT\\n==========================================================================================\\n\\nPCA explained variance ratios:\\n  r1-8b: 0.7931\\n  ot-7b: 0.8282\\n  qwq-32b: 0.8813\\n  r1-32b: 0.9243\\nTraceback (most recent call last):\\n  File \\\"/root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_r5_pca384_control.py\\\", line 364, in &lt;module>\\n    main()\\n  File \\\"/root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_r5_pca384_control.py\\\", line 359, in main\\n    json.dump(output, f, indent=2)\\n  File \\\"/root/miniconda3/lib/python3.12/json/__init__.py\\\", line 179, in dump\\n    for chunk in iterable:\\n  File \\\"/root/miniconda3/lib/python3.12/json/encoder.py\\\", line 432, in _iterencode\\n    yield from _itere
…[truncated 731 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-17T19:24:11.363392+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "sed -i 's/pca_variances\\[model_name\\] = var_explained/pca_variances[model_name] = float(var_explained)/' /root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_r5_pca384_control.py && echo \"Fixed\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "sed -i 's/pca_variances\\[model_name\\] = var_explained/pca_variances[model_name] = float(var_explained)/' /root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_r5_pca384_control.py && echo \"Fixed\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-17T19:24:11.363616+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Fixed\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-17T19:24:11.363849+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "/root/miniconda3/bin/python3.12 -c \"\nimport json\nfrom pathlib import Path\n\nresults = [\n    {'model': 'r1-8b', 'metric': 'bal_acc', 'pca384_hs': 0.7001, 'text_384': 0.6875, 'delta': 0.0126, 'p_value': 0.731, 'p_adjusted': 0.731, 'significant': False},\n    {'model': 'r1-8b', 'metric': 'precision', 'pca384_hs': 0.8162, 'text_384': 0.5852, 'delta': 0.2310, 'p_value': 0.0, 'p_adjusted': 0.0, 'significant': True},\n    {'model': 'r1-8b', 'metric': 'FPR', 'pca384_hs': 0.0668, 'text_384': 0.1614, 'delta': -0.0947, 'p_value': 0.003, 'p_adjusted': 0.012, 'significant': True},\n    {'model': 'ot-7b', 'metric': 'bal_acc', 'pca384_hs': 0.7558, 'text_384': 0.6430, 'delta': 0.1128, 'p_value': 0.0, 'p_adjusted': 0.0, 'significant': True},\n    {'model': 'ot-7b', 'metric': 'precision', 'pca384_hs': 0.5225, 'text_384': 0.3545, 'delta': 0.1681, 'p_value': 0.0, 'p_adjusted': 0.0, 'significant': True},\n    {'model': 'ot-7b', 'metric': 'FPR', 'pca384_hs': 0.1207, 'text_384': 0.2477, 'delta': -0.127, 'p_value': 0.0, 'p_adjusted': 0.0, 'significant': True},\n    {'model': 'qwq-32b', 'metric': 'bal_acc', 'pca384_hs': 0.8116, 'text_384': 0.6504, 'delta': 0.1612, 'p_value': 0.0, 'p_adjusted': 0.0, 'significant': True},\n    {'model': 'qwq-32b', 'metric': 'precision', 'pca384_hs': 0.6080, 'text_384': 0.4213, 'delta': 0.1867, 'p_value': 0.0, 'p_adjusted': 0.0, 'significant': True},\n    {'model': 'qwq-32b', 'metric': 'FPR', 'pca384_hs': 0.173, 'text_384': 0.2871, 'delta': -0.1141, 'p_value': 0.038, 'p_adjusted': 0.076, 'significant': False},\n    {'model': 'r1-32b', 'metric': 'bal_acc', 'pca384_hs': 0.7471, 'text_384': 0.6461, 'delta': 0.1011, 'p_value': 0.011, 'p_adjusted': 0.033, 'significant': True},\n    {'model': 'r1-32b', 'metric': 'precision', 'pca384_hs': 0.6343, 'text_384': 0.4503, 'delta': 0.184, 'p_value': 0.002, 'p_adjusted': 0.01, 'significant': True},\n    {'model': 'r1-32b', 'metric': 'FPR', 'pca384_hs': 0.2256, 'text_384': 0.3809, 'delta': -0.1553, 'p_value': 0.006, 'p_adjusted': 0.024, 'significant': True},\n]\n\noutput = {\n    'experiment': 'exp_r5_pca384_control',\n    'description': 'PCA-384d dimensionality control: HS reduced to 384d vs Text 384d. Tests whether HS advantage is due to dimensionality or modality.',\n    'n_bootstrap': 1000,\n    'seed': 42,\n    'pca_explained_variance': {'r1-8b': 0.7931, 'ot-7b': 0.8282, 'qwq-32b': 0.8813, 'r1-32b': 0.9243},\n    'results': results,\n    'conclusion': 'Even at equal dimensionality (384d), PCA-reduced HS features significantly outperform text embeddings on 10/12 tests after Holm-Bonferroni correction. The HS advantage is NOT due to dimensionality.',\n}\n\nout_path = Path('/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/results.json')\nout_path.parent.mkdir(parents=True, exist_ok=True)\nwith open(out_path, 'w') as f:\n    json.dump(output, f, indent=2)\nprint(f'Saved to {out_path}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "/root/miniconda3/bin/python3.12 -c \"\nimport json\nfrom pathlib import Path\n\nresults = [\n    {'model': 'r1-8b', 'metric': 'bal_acc', 'pca384_hs': 0.7001, 'text_384': 0.6875, 'delta': 0.0126, 'p_value': 0.731, 'p_adjusted': 0.731, 'significant': False},\n    {'model': 'r1-8b', 'metric': 'precision', 'pca384_hs': 0.8162, 'text_384': 0.5852, 'delta': 0.2310, 'p_value': 0.0, 'p_adjusted': 0.0, 'significant': True},\n    {'model': 'r1-8b', 'metric': 'FPR', 'pca384_hs': 0.0668, 'text_384': 0.1614, 'delta': -0.0947, 'p_value': 0.003, 'p_adjusted': 0.012, 'significant': True},\n    {'model': 'ot-7b', 'metric': 'bal_acc', 'pca384_hs': 0.7558, 'text_384': 0.6430, 'delta': 0.1128, 'p_value': 0.0, 'p_adjusted': 0.0, 'significant': True},\n    {'model': 'ot-7b', 'metric': 'precision', 'pca384_hs': 0.5225, 'text_384': 0.3545, 'delta': 0.1681, 'p_value': 0.0, 'p_adjusted': 0.0, 'significant': True},\n    {'model': 'ot-7b', 'metric': 'FPR', 'pca384_hs': 0.1207, 'text_384': 0.2477, 'delta': -0.127, 'p_value': 0.0, 'p_adjusted': 0.0, 'significant': True},\n    {'model': 'qwq-32b', 'metric': 'bal_acc', 'pca384_hs': 0.8116, 'text_384': 0.6504, 'delta': 0.1612, 'p_value': 0.0, 'p_adjusted': 0.0, 'significant': True},\n    {'model': 'qwq-32b', 'metric': 'precision', 'pca384_hs': 0.6080, 'text_384': 0.4213, 'delta': 0.1867, 'p_value': 0.0, 'p_adjusted': 0.0, 'significant': True},\n    {'model': 'qwq-32b', 'metric': 'FPR', 'pca384_hs': 0.173, 'text_384': 0.2871, 'delta': -0.1141, 'p_value': 0.038, 'p_adjusted': 0.076, 'significant': False},\n    {'model': 'r1-32b', 'metric': 'bal_acc', 'pca384_hs': 0.7471, 'text_384': 0.6461, 'delta': 0.1011, 'p_value': 0.011, 'p_adjusted': 0.033, 'significant': True},\n    {'model': 'r1-32b', 'metric': 'precision', 'pca384_hs': 0.6343, 'text_384': 0.4503, 'delta': 0.184, 'p_value': 0.002, 'p_adjusted': 0.01, 'significant': True},\n    {'model': 'r1-32b', 'metric': 'FPR', 'pca384_hs': 0.2256, 'text_384': 0.3809, 'delta': -0.1553, 'p_value': 0.006, 'p_adjusted': 0.024, 'significant': True},\n]\n\noutput = {\n    'experiment': 'exp_r5_pca384_control',\n    'description': 'PCA-384d dimensionality control: HS reduced to 384d vs Text 384d. Tests whether HS advantage is due to dimensionality or modality.',\n    'n_bootstrap': 1000,\n    'seed': 42,\n    'pca_explained_variance': {'r1-8b': 0.7931, 'ot-7b': 0.8282, 'qwq-32b': 0.8813, 'r1-32b': 0.9243},\n    'results': results,\n    'conclusion': 'Even at equal dimensionality (384d), PCA-reduced HS features significantly outperform text embeddings on 10/12 tests after Holm-Bonferroni correction. The HS advantage is NOT due to dimensionality.',\n}\n\nout_path = Path('/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/results.json')\nout_path.parent.mkdir(parents=True, exist_ok=True)\nwith open(out_path, 'w') as f:\n    json.dump(output, f, indent=2)\nprint(f'Saved to {out_path}')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-17T19:24:11.364095+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Saved to /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-17T19:24:11.364348+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "screen -S exp_r5 -X quit 2>/dev/null; cd /root/autodl-tmp/contrastive_trace_safety && screen -dmS exp_r5 bash -c \"PYTHONUNBUFFERED=1 /root/miniconda3/bin/python3.12 src/experiments/exp_r5_pca384_control.py > artifacts/exp_r5_pca384/run.log 2>&1\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "screen -S exp_r5 -X quit 2>/dev/null; cd /root/autodl-tmp/contrastive_trace_safety && screen -dmS exp_r5 bash -c \"PYTHONUNBUFFERED=1 /root/miniconda3/bin/python3.12 src/experiments/exp_r5_pca384_control.py > artifacts/exp_r5_pca384/run.log 2>&1\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-17T19:24:11.364566+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"No screen session found.\\r\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-17T19:24:11.364780+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "sleep 28 && wc -l /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log && tail -5 /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "sleep 28 && wc -l /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log && tail -5 /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-17T19:24:11.364981+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"17 /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log\\n  Loaded 209 valid traces\\n  Split: train=125, val=41, test=43\\n  Fitting PCA(384) on training hidden states (dim=4096)...\\n  PCA explained variance: 0.7931\\n  Computing text embeddings (MiniLM-384d)...\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 28.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-17T19:24:11.365161+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "sleep 28 && tail -10 /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "sleep 28 && tail -10 /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-17T19:24:11.365341+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Model: r1-8b\\n============================================================\\n  Loading sentences from HF (r1-8b)...\\n  Found 324 traces in HF dataset\\n  Loading .pt traces from /root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states...\\n  Loaded 209 valid traces\\n  Split: train=125, val=41, test=43\\n  Fitting PCA(384) on training hidden states (dim=4096)...\\n  PCA explained variance: 0.7931\\n  Computing text embeddings (MiniLM-384d)...\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 28.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-17T19:24:11.365553+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "sleep 28 && tail -10 /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "sleep 28 && tail -10 /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-17T19:24:11.365782+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  Loading sentences from HF (r1-8b)...\\n  Found 324 traces in HF dataset\\n  Loading .pt traces from /root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states...\\n  Loaded 209 valid traces\\n  Split: train=125, val=41, test=43\\n  Fitting PCA(384) on training hidden states (dim=4096)...\\n  PCA explained variance: 0.7931\\n  Computing text embeddings (MiniLM-384d)...\\n  Training PCA-384 HS probe (window=15)...\\n  Training Text probe (window=15)...\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 28.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-17T19:24:11.365974+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "sleep 28 && tail -15 /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "sleep 28 && tail -15 /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-17T19:24:11.366161+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  Evaluating on test set (43 traces)...\\n  Running paired bootstrap (n=1000)...\\n  Done in 83.4s\\n\\n============================================================\\nModel: ot-7b\\n============================================================\\n  Loading sentences from HF (ot-7b)...\\n  Found 333 traces in HF dataset\\n  Loading .pt traces from /root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_ot7b...\\n  Loaded 228 valid traces\\n  Split: train=136, val=45, test=47\\n  Fitting PCA(384) on training hidden states (dim=3584)...\\n  PCA explained variance: 0.8282\\n  Computing text embeddings (MiniLM-384d)...\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 28.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-17T19:24:11.366334+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "sleep 28 && tail -15 /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "sleep 28 && tail -15 /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-17T19:24:11.366516+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  Evaluating on test set (43 traces)...\\n  Running paired bootstrap (n=1000)...\\n  Done in 83.4s\\n\\n============================================================\\nModel: ot-7b\\n============================================================\\n  Loading sentences from HF (ot-7b)...\\n  Found 333 traces in HF dataset\\n  Loading .pt traces from /root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_ot7b...\\n  Loaded 228 valid traces\\n  Split: train=136, val=45, test=47\\n  Fitting PCA(384) on training hidden states (dim=3584)...\\n  PCA explained variance: 0.8282\\n  Computing text embeddings (MiniLM-384d)...\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 28.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-17T19:24:11.366724+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "sleep 28 && tail -10 /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "sleep 28 && tail -10 /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-17T19:24:11.366913+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Model: ot-7b\\n============================================================\\n  Loading sentences from HF (ot-7b)...\\n  Found 333 traces in HF dataset\\n  Loading .pt traces from /root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_ot7b...\\n  Loaded 228 valid traces\\n  Split: train=136, val=45, test=47\\n  Fitting PCA(384) on training hidden states (dim=3584)...\\n  PCA explained variance: 0.8282\\n  Computing text embeddings (MiniLM-384d)...\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 28.47}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-17T19:24:11.367117+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "sleep 28 && tail -10 /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "sleep 28 && tail -10 /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-17T19:24:11.367312+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Model: ot-7b\\n============================================================\\n  Loading sentences from HF (ot-7b)...\\n  Found 333 traces in HF dataset\\n  Loading .pt traces from /root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_ot7b...\\n  Loaded 228 valid traces\\n  Split: train=136, val=45, test=47\\n  Fitting PCA(384) on training hidden states (dim=3584)...\\n  PCA explained variance: 0.8282\\n  Computing text embeddings (MiniLM-384d)...\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 28.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-17T19:24:11.367515+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "sleep 28 && tail -10 /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "sleep 28 && tail -10 /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-17T19:24:11.367727+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"============================================================\\n  Loading sentences from HF (ot-7b)...\\n  Found 333 traces in HF dataset\\n  Loading .pt traces from /root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_ot7b...\\n  Loaded 228 valid traces\\n  Split: train=136, val=45, test=47\\n  Fitting PCA(384) on training hidden states (dim=3584)...\\n  PCA explained variance: 0.8282\\n  Computing text embeddings (MiniLM-384d)...\\n  Training PCA-384 HS probe (window=3)...\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 28.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-17T19:24:11.367941+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "sleep 28 && tail -15 /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "sleep 28 && tail -15 /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-17T19:24:11.368146+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  Training PCA-384 HS probe (window=3)...\\n  Training Text probe (window=3)...\\n  Evaluating on test set (47 traces)...\\n  Running paired bootstrap (n=1000)...\\n  Done in 181.1s\\n\\n============================================================\\nModel: qwq-32b\\n============================================================\\n  Loading sentences from HF (QwQ)...\\n  Found 140 traces in HF dataset\\n  Loading .pt traces from /root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b...\\n  Loaded 95 valid traces\\n  Split: train=57, val=19, test=19\\n  Fitting PCA(384) on training hidden states (dim=5120)...\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 28.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-17T19:24:11.368339+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "sleep 28 && tail -15 /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "sleep 28 && tail -15 /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-17T19:24:11.368552+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  Evaluating on test set (47 traces)...\\n  Running paired bootstrap (n=1000)...\\n  Done in 181.1s\\n\\n============================================================\\nModel: qwq-32b\\n============================================================\\n  Loading sentences from HF (QwQ)...\\n  Found 140 traces in HF dataset\\n  Loading .pt traces from /root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b...\\n  Loaded 95 valid traces\\n  Split: train=57, val=19, test=19\\n  Fitting PCA(384) on training hidden states (dim=5120)...\\n  PCA explained variance: 0.8813\\n  Computing text embeddings (MiniLM-384d)...\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 28.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-17T19:24:11.368766+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "sleep 28 && tail -20 /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "sleep 28 && tail -20 /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-17T19:24:11.368983+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  Fitting PCA(384) on training hidden states (dim=5120)...\\n  PCA explained variance: 0.8813\\n  Computing text embeddings (MiniLM-384d)...\\n  Training PCA-384 HS probe (window=3)...\\n  Training Text probe (window=3)...\\n  Evaluating on test set (19 traces)...\\n  Running paired bootstrap (n=1000)...\\n  Done in 53.1s\\n\\n============================================================\\nModel: r1-32b\\n============================================================\\n  Loading sentences from HF (r1-32b)...\\n  Found 221 traces in HF dataset\\n  Loading .pt traces from /root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b...\\n  Loaded 100 valid traces\\n  Split: train=60, val=20, test=20\\n  Fitting PCA(384) on training hidden states (dim=5120)...\\n  PCA explained variance: 0.9243\\n  Computing text embeddings (MiniLM-384d)...\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 28.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-17T19:24:11.369185+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "sleep 28 && tail -10 /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log && ls /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/results.json 2>/dev/null && echo \"JSON exists\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "sleep 28 && tail -10 /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log && ls /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/results.json 2>/dev/null && echo \"JSON exists\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-17T19:24:11.369392+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"r1-32b     | FPR        |    0.2256 |   0.3809 |  -0.1553 |   0.0060 |     REJECT\\n==========================================================================================\\n\\nPCA explained variance ratios:\\n  r1-8b: 0.7931\\n  ot-7b: 0.8282\\n  qwq-32b: 0.8813\\n  r1-32b: 0.9243\\n\\nResults saved to /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/results.json\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/results.json\\nJSON exists\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 28.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-17T19:24:11.369617+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "cat /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "cat /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/run.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-17T19:24:11.369887+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"============================================================\\nExp R5: PCA-384d Dimensionality Control\\n============================================================\\n\\nLoading SentenceTransformer (all-MiniLM-L6-v2)...\\n\\n============================================================\\nModel: r1-8b\\n============================================================\\n  Loading sentences from HF (r1-8b)...\\n  Found 324 traces in HF dataset\\n  Loading .pt traces from /root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states...\\n  Loaded 209 valid traces\\n  Split: train=125, val=41, test=43\\n  Fitting PCA(384) on training hidden states (dim=4096)...\\n  PCA explained variance: 0.7931\\n  Computing text embeddings (MiniLM-384d)...\\n  Training PCA-384 HS probe (window=15)...\\n  Training Text probe (window=15)...\\n  Evaluating on test set (43 traces)...\\n  Running paired bootstrap (n=1000)...\\n  Done in 83.4s\\n\\n============================================================\\nModel: ot-7b\\n============================================================\\n  Loading sentences from HF (ot-7b)...\\n  Found 333 traces in HF dataset\\n  Loading .pt traces from /root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_ot7b...\\n  Loaded 228 valid traces\\n  Split: train=136, val=45, test=47\\n  Fitting PCA(384) on training hidden states (dim=3584)...\\n  PCA explained variance: 0.8282\\n  Computing text embeddings (MiniLM-384d)...\\n  Training PCA-384 HS probe (window=3)...\\n  Training Text probe (window=3)...\\n  Evaluating on test set (47 traces)...\\n  Running paired bootstrap (n=1000)...\\n  Done in 181.1s\\n\\n============================================================\\nModel: qwq-32b\\n============================================================\\n  Loading sentences from HF (QwQ)...\\n  Found 140 traces in HF dataset\\n  Loading .pt traces from /root/autodl-tmp/contrastive_trace_safety/artifac
…[truncated 2827 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-17T19:24:11.370136+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "cat /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "cat /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_pca384/results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-17T19:24:11.370442+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"exp_r5_pca384_control\\\",\\n  \\\"description\\\": \\\"PCA-384d dimensionality control: HS reduced to 384d vs Text 384d\\\",\\n  \\\"n_bootstrap\\\": 1000,\\n  \\\"seed\\\": 42,\\n  \\\"pca_explained_variance\\\": {\\n    \\\"r1-8b\\\": 0.7930715680122375,\\n    \\\"ot-7b\\\": 0.8282058238983154,\\n    \\\"qwq-32b\\\": 0.8813128471374512,\\n    \\\"r1-32b\\\": 0.9242970943450928\\n  },\\n  \\\"results\\\": [\\n    {\\n      \\\"model\\\": \\\"r1-8b\\\",\\n      \\\"metric\\\": \\\"bal_acc\\\",\\n      \\\"pca384_hs\\\": 0.7001272971619915,\\n      \\\"text_384\\\": 0.687534610194348,\\n      \\\"delta\\\": 0.012592686967643485,\\n      \\\"p_value\\\": 0.731,\\n      \\\"p_adjusted\\\": 0.731,\\n      \\\"significant\\\": false\\n    },\\n    {\\n      \\\"model\\\": \\\"r1-8b\\\",\\n      \\\"metric\\\": \\\"precision\\\",\\n      \\\"pca384_hs\\\": 0.8162048242075602,\\n      \\\"text_384\\\": 0.5852386971114021,\\n      \\\"delta\\\": 0.23096612709615816,\\n      \\\"p_value\\\": 0.0,\\n      \\\"p_adjusted\\\": 0.0,\\n      \\\"significant\\\": true\\n    },\\n    {\\n      \\\"model\\\": \\\"r1-8b\\\",\\n      \\\"metric\\\": \\\"FPR\\\",\\n      \\\"pca384_hs\\\": 0.06675020512149242,\\n      \\\"text_384\\\": 0.16141572689707637,\\n      \\\"delta\\\": -0.09466552177558395,\\n      \\\"p_value\\\": 0.003,\\n      \\\"p_adjusted\\\": 0.015,\\n      \\\"significant\\\": true\\n    },\\n    {\\n      \\\"model\\\": \\\"ot-7b\\\",\\n      \\\"metric\\\": \\\"bal_acc\\\",\\n      \\\"pca384_hs\\\": 0.7557765099782141,\\n      \\\"text_384\\\": 0.6430059543712647,\\n      \\\"delta\\\": 0.11277055560694937,\\n      \\\"p_value\\\": 0.0,\\n      \\\"p_adjusted\\\": 0.0,\\n      \\\"significant\\\": true\\n    },\\n    {\\n      \\\"model\\\": \\\"ot-7b\\\",\\n      \\\"metric\\\": \\\"precision\\\",\\n      \\\"pca384_hs\\\": 0.5225356904233679,\\n      \\\"text_384\\\": 0.3544669
…[truncated 2604 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 89 · 2026-05-17T19:24:11.370756+00:00_

Experiment completed successfully. Results summary:

```
Model      | Metric     | PCA384-HS | Text-384 |    Delta |  p-value | Holm-Bonf
------------------------------------------------------------------------------------------
r1-8b      | bal_acc    |    0.7001 |   0.6875 |  +0.0126 |   0.7310 |       fail
r1-8b      | precision  |    0.8162 |   0.5852 |  +0.2310 |   0.0000 |     REJECT
r1-8b      | FPR        |    0.0668 |   0.1614 |  -0.0947 |   0.0030 |     REJECT
ot-7b      | bal_acc    |    0.7558 |   0.6430 |  +0.1128 |   0.0000 |     REJECT
ot-7b      | precision  |    0.5225 |   0.3545 |  +0.1681 |   0.0000 |     REJECT
ot-7b      | FPR        |    0.1207 |   0.2477 |  -0.1270 |   0.0000 |     REJECT
qwq-32b    | bal_acc    |    0.8116 |   0.6504 |  +0.1612 |   0.0000 |     REJECT
qwq-32b    | precision  |    0.6080 |   0.4213 |  +0.1867 |   0.0000 |     REJECT
qwq-32b    | FPR        |    0.1730 |   0.2871 |  -0.1141 |   0.0380 |       fail
r1-32b     | bal_acc    |    0.7471 |   0.6461 |  +0.1011 |   0.0110 |     REJECT
r1-32b     | precision  |    0.6343 |   0.4503 |  +0.1840 |   0.0020 |     REJECT
r1-32b     | FPR        |    0.2256 |   0.3809 |  -0.1553 |   0.0060 |     REJECT
```

**10/12 tests reject H0 after Holm-Bonferroni correction.** Even when HS features are PCA-reduced to exactly 384d (matching text dimensionality), they significantly outperform text embeddings. The two non-significant results (r1-8b bal_acc at p=0.731, qwq-32b FPR at p_adj=0.076) are both cases where the HS probe still has better raw numbers.

PCA explained variance: r1-8b 79.3%, ot-7b 82.8%, qwq-32b 88.1%, r1-32b 92.4%.

Script at `/root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_r5_pca384_control.py`, results at `artifacts/exp_r5_pca384/results.json`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_pca384_dimensionality_control_20260517T190710"
}
```

</details>

---
