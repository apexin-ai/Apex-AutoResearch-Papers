# code exp ot7b full pipeline

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 0
- **Tool calls:** 21
- **Original source:** `logs/chats/worker_code_exp_ot7b_full_pipeline_20260517T061417.jsonl`
- **Structured JSON:** [`a6854ad80d672d2e7b15.json`](../../sessions/a6/a6854ad80d672d2e7b15.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

43 recorded events

### Tool call

_source line 1 · 2026-05-17T06:20:38.715659+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__ssh_read_only",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__ssh_read_only",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T06:20:38.716042+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T06:20:38.716231+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "ls /root/autodl-tmp/contrastive_trace_safety/src/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "ls /root/autodl-tmp/contrastive_trace_safety/src/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-17T06:20:38.716369+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "ls /root/autodl-tmp/contrastive_trace_safety/src/experiments/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "ls /root/autodl-tmp/contrastive_trace_safety/src/experiments/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-17T06:20:38.716509+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"__init__.py\\n__pycache__\\nbaselines\\nconfig.py\\ncrta\\ndata_loader.py\\ndiagnostics\\neval\\nexperiments\\nextract_hidden_states.py\\nrun_pipeline.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T06:20:38.716752+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"__init__.py\\n__pycache__\\nbocpd_poc.py\\nbootstrap_ci.py\\nexp_001a_bootstrap_hs_vs_text.py\\nexp_001a_extract_r1_32b.py\\nexp_001a_probing.py\\nexp_001b_bootstrap.py\\nexp_001b_extract_qwq.py\\nexp_001b_probing.py\\nexp_003_cross_transfer.py\\nexp_007_window_ablation.py\\nexp_c2_control_task.py\\nexp_pathC_two_stage_sim.py\\nfpr_analysis.py\\ngru_multilayer_ablation.py\\ngru_per_seed_eval.py\\nm001_layer_fix.py\\nr1_8b_bootstrap_hs_text.py\\nrun_selectivity_qwq_l2.py\\ntext_baseline.py\\ntext_window_ablation_r1_8b.py\\ntrajguard_mahalanobis.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T06:20:38.716916+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "cat /root/autodl-tmp/contrastive_trace_safety/src/data_loader.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "cat /root/autodl-tmp/contrastive_trace_safety/src/data_loader.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T06:20:38.717126+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Load HarmThoughts dataset and extract commitment points.\\n\\nInput: HuggingFace dataset \\\"ishitakakkar-10/HarmThoughts\\\"\\nOutput: List of trace dicts with sentences, labels, commitment_point, split assignments\\n\\\"\\\"\\\"\\n\\nfrom collections import defaultdict\\nfrom typing import List, Optional, Dict, Any\\nimport numpy as np\\nfrom datasets import load_dataset\\n\\nfrom .config import (\\n    HF_DATASET, TARGET_MODEL, SAFETY_LABELS,\\n    TRAIN_RATIO, VAL_RATIO, SEED\\n)\\n\\n\\ndef load_harmthoughts(model_name: str = TARGET_MODEL) -> Dict[str, List[Dict]]:\\n    \\\"\\\"\\\"Load HarmThoughts from HF and group by trace_id.\\\"\\\"\\\"\\n    ds = load_dataset(HF_DATASET, split=\\\"train\\\")\\n\\n    traces = defaultdict(list)\\n    for row in ds:\\n        if row[\\\"model_name\\\"] != model_name:\\n            continue\\n        # trace_id is the part before the last dash in sentence_id\\n        sid = row[\\\"sentence_id\\\"]\\n        parts = sid.rsplit(\\\"-\\\", 1)\\n        trace_id = parts[0]\\n        step_idx = int(parts[1]) - 1  # convert to 0-indexed\\n\\n        traces[trace_id].append({\\n            \\\"sentence_id\\\": sid,\\n            \\\"step_idx\\\": step_idx,\\n            \\\"sentence\\\": row[\\\"sentence\\\"],\\n            \\\"label\\\": row[\\\"llm_annotation\\\"],\\n            \\\"query\\\": row[\\\"query\\\"],\\n            \\\"final_judgment\\\": row[\\\"final_judgment\\\"],\\n        })\\n\\n    # Sort each trace by step_idx\\n    for tid in traces:\\n        traces[tid].sort(key=lambda x: x[\\\"step_idx\\\"])\\n\\n    return dict(traces)\\n\\n\\ndef extract_commitment_point(labels: List[str]) -> Optional[int]:\\n    \\\"\\\"\\\"Find the commitment point in a sequence of labels.\\n\\n    Returns the index after the last safety label, or None if:\\n    - No safety labels exist in the trace\\n    - The last safety label is at the final position (no post-comm
…[truncated 4406 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T06:20:38.717293+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "head -100 /root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_001a_extract_r1_32b.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "head -100 /root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_001a_extract_r1_32b.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T06:20:38.717470+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Phase 1: Extract hidden states from DeepSeek-R1-Distill-Qwen-32B for all 64 layers.\\\"\\\"\\\"\\n\\nimport os, sys, json, time\\nos.environ[\\\"HF_ENDPOINT\\\"] = \\\"https://hf-mirror.com\\\"\\n\\nimport torch\\nfrom pathlib import Path\\nfrom transformers import AutoTokenizer, AutoModelForCausalLM\\nfrom tqdm import tqdm\\n\\nsys.path.insert(0, \\\"/root/autodl-tmp/contrastive_trace_safety\\\")\\nfrom src.data_loader import load_harmthoughts, extract_commitment_point, create_step_labels\\nfrom src.config import SAFETY_LABELS\\n\\nMODEL_PATH = \\\"/root/autodl-tmp/.hf_cache/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B\\\"\\nOUTPUT_DIR = Path(\\\"/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b\\\")\\nNUM_LAYERS = 64\\nHIDDEN_DIM = 5120\\nDEVICE = \\\"cuda:0\\\"\\nMAX_LENGTH = 8192\\n\\n\\ndef load_model():\\n    print(\\\"Loading R1-32B tokenizer...\\\")\\n    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)\\n    if tokenizer.pad_token is None:\\n        tokenizer.pad_token = tokenizer.eos_token\\n\\n    print(\\\"Loading R1-32B model (fp16)...\\\")\\n    t0 = time.time()\\n    model = AutoModelForCausalLM.from_pretrained(\\n        MODEL_PATH,\\n        torch_dtype=torch.float16,\\n        device_map=DEVICE,\\n        trust_remote_code=True,\\n    )\\n    model.eval()\\n    print(f\\\"Model loaded in {time.time()-t0:.1f}s\\\")\\n    return model, tokenizer\\n\\n\\ndef find_sentence_boundaries(tokenizer, sentences):\\n    full_text = \\\" \\\".join(sentences)\\n    encoding = tokenizer(\\n        full_text,\\n        return_offsets_mapping=True,\\n        return_tensors=\\\"pt\\\",\\n        truncation=True,\\n        max_length=MAX_LENGTH,\\n    )\\n    offsets = encoding[\\\"offset_mapping\\\"][0]\\n\\n    boundaries = []\\n    char_pos = 0\\n    for sent in sentences:\\n        char_end = char_pos + len(sent)\\n        last_token_idx = 0\\n     
…[truncated 1509 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T06:20:38.717652+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "cat /root/autodl-tmp/contrastive_trace_safety/src/config.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "cat /root/autodl-tmp/contrastive_trace_safety/src/config.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T06:20:38.717826+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Central configuration for contrastive_trace_safety project.\\\"\\\"\\\"\\n\\nimport os\\nfrom pathlib import Path\\n\\n# Paths\\nPROJECT_ROOT = Path(\\\"/root/autodl-tmp/contrastive_trace_safety\\\")\\nARTIFACTS_DIR = PROJECT_ROOT / \\\"artifacts\\\"\\nHIDDEN_STATES_DIR = ARTIFACTS_DIR / \\\"hidden_states\\\"\\nPROBES_DIR = ARTIFACTS_DIR / \\\"probes\\\"\\n\\n# Model\\nMODEL_NAME = \\\"deepseek-ai/DeepSeek-R1-Distill-Llama-8B\\\"\\nMODEL_PATH = \\\"/root/autodl-tmp/.hf_cache/deepseek-ai/DeepSeek-R1-Distill-Llama-8B\\\"\\n\\n# Dataset\\nHF_DATASET = \\\"ishitakakkar-10/HarmThoughts\\\"\\nTARGET_MODEL = \\\"r1-8b\\\"\\n\\n# Hidden state extraction\\nLAYERS = list(range(12, 25))  # layers 12-24, 13 layers total\\nNUM_LAYERS = len(LAYERS)\\nHIDDEN_DIM = 4096\\nEXTRACT_BATCH_SIZE = 4\\nDEVICE = \\\"cuda:0\\\"\\n\\n# Probes\\nWINDOW_SIZE = 5\\nTEMPORAL_HIDDEN_DIM = 512\\nLEARNING_RATE = 1e-3\\nTRAIN_EPOCHS = 20\\nPROBE_BATCH_SIZE = 64\\nDEFAULT_LAYER = 20  # for static probe\\n\\n# Data split\\nTRAIN_RATIO = 0.6\\nVAL_RATIO = 0.2\\nSEED = 42\\n\\n# Evaluation\\nDETECTION_THRESHOLD = 0.9\\nDETECTION_WINDOW = 5\\n\\n# Safety labels that define commitment point\\nSAFETY_LABELS = {\\\"RA\\\", \\\"AL\\\", \\\"CC\\\", \\\"ED\\\", \\\"IA\\\"}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T06:20:38.717964+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "tail -100 /root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_001a_extract_r1_32b.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "tail -100 /root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_001a_extract_r1_32b.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T06:20:38.718154+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    return result, num_tokens\\n\\n\\ndef load_r1_32b_traces():\\n    raw_traces = load_harmthoughts(\\\"r1-32b\\\")\\n    traces = []\\n    for trace_id, steps in raw_traces.items():\\n        is_jailbreak = steps[0][\\\"final_judgment\\\"] == 1.0\\n        if not is_jailbreak:\\n            continue\\n        labels = [s[\\\"label\\\"] for s in steps]\\n        cp = extract_commitment_point(labels)\\n        if cp is None:\\n            continue\\n        sentences = [s[\\\"sentence\\\"] for s in steps]\\n        step_labels = create_step_labels(cp, len(sentences))\\n        traces.append({\\n            \\\"trace_id\\\": trace_id,\\n            \\\"sentences\\\": sentences,\\n            \\\"labels\\\": labels,\\n            \\\"commitment_point\\\": cp,\\n            \\\"step_labels\\\": step_labels,\\n            \\\"query\\\": steps[0][\\\"query\\\"],\\n        })\\n    return traces\\n\\n\\ndef main():\\n    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)\\n\\n    print(\\\"Loading R1-32B traces from HarmThoughts...\\\")\\n    traces = load_r1_32b_traces()\\n    print(f\\\"Found {len(traces)} jailbreak traces with commitment points\\\")\\n\\n    existing = {f.stem for f in OUTPUT_DIR.glob(\\\"*.pt\\\")}\\n    remaining = [t for t in traces if t[\\\"trace_id\\\"] not in existing]\\n    print(f\\\"Already extracted: {len(existing)}, remaining: {len(remaining)}\\\")\\n\\n    if not remaining:\\n        print(\\\"All traces already extracted.\\\")\\n        return\\n\\n    model, tokenizer = load_model()\\n\\n    total_steps = 0\\n    total_tokens = 0\\n    errors = []\\n\\n    for i, trace in enumerate(tqdm(remaining, desc=\\\"Extracting\\\")):\\n        trace_id = trace[\\\"trace_id\\\"]\\n        sentences = trace[\\\"sentences\\\"]\\n\\n        try:\\n            hidden_states, num_tokens = extract_trace(model, tokenizer, sentences)\\n            total_steps += len(sentences)\\n            total_tokens += 
…[truncated 2004 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T06:20:38.718342+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "head -150 /root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_001a_probing.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "head -150 /root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_001a_probing.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T06:20:38.718543+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"exp_001a Phases 2-5: Layer sweep, temporal LR, GRU 3-seed, bootstrap FPR.\\\"\\\"\\\"\\n\\nimport os, sys, json, time, glob\\nimport numpy as np\\nimport torch\\nimport torch.nn as nn\\nfrom torch.utils.data import Dataset, DataLoader\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.metrics import accuracy_score, f1_score\\nfrom pathlib import Path\\n\\nsys.path.insert(0, \\\"/root/autodl-tmp/contrastive_trace_safety\\\")\\n\\nHS_DIR = Path(\\\"/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b\\\")\\nOUTPUT_DIR = Path(\\\"/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_001a\\\")\\nNUM_LAYERS = 64\\nHIDDEN_DIM = 5120\\nDEVICE = \\\"cuda:0\\\"\\nK_CONSECUTIVE = 5\\nTHRESHOLD = 0.5\\n\\n\\ndef load_traces():\\n    traces = []\\n    for pt_file in sorted(HS_DIR.glob(\\\"*.pt\\\")):\\n        data = torch.load(pt_file, map_location=\\\"cpu\\\", weights_only=False)\\n        if data.get(\\\"step_labels\\\") is None or data.get(\\\"commitment_point\\\") is None:\\n            continue\\n        traces.append(data)\\n    return traces\\n\\n\\ndef split_traces(traces, train_ratio=0.6, val_ratio=0.2, seed=42):\\n    rng = np.random.default_rng(seed)\\n    indices = rng.permutation(len(traces))\\n    n_train = int(len(traces) * train_ratio)\\n    n_val = int(len(traces) * val_ratio)\\n    return (\\n        [traces[i] for i in indices[:n_train]],\\n        [traces[i] for i in indices[n_train:n_train+n_val]],\\n        [traces[i] for i in indices[n_train+n_val:]],\\n    )\\n\\n\\ndef first_crossing(probs, threshold=0.5, k=5):\\n    for i in range(len(probs) - k + 1):\\n        if all(p > threshold for p in probs[i:i+k]):\\n            return i\\n    return None\\n\\n\\ndef extract_layer_data(traces, layer_idx):\\n    X_list, y_list = [], []\\n    for t in traces:\\n        hs = t[\\\"hidden_states\\\"][:, layer_idx, :].float().numpy()\\n        labels = np.arra
…[truncated 4189 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T06:20:38.718751+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "head -80 /root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_001a_bootstrap_hs_vs_text.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "head -80 /root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_001a_bootstrap_hs_vs_text.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-17T06:20:38.718934+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Phase 5b: Pre-CP FPR Paired Bootstrap Test - HS probe vs Text probe for R1-32B.\\\"\\\"\\\"\\n\\nimport os, sys, json\\nos.environ[\\\"TOKENIZERS_PARALLELISM\\\"] = \\\"false\\\"\\nos.environ[\\\"HF_ENDPOINT\\\"] = \\\"https://hf-mirror.com\\\"\\n\\nimport numpy as np\\nimport torch\\nfrom sklearn.linear_model import LogisticRegression\\nfrom pathlib import Path\\n\\nsys.path.insert(0, \\\"/root/autodl-tmp/contrastive_trace_safety\\\")\\nfrom src.data_loader import load_harmthoughts, extract_commitment_point, create_step_labels\\nfrom src.config import SAFETY_LABELS\\n\\nHS_DIR = Path(\\\"/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b\\\")\\nOUTPUT_DIR = Path(\\\"/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_001a\\\")\\nHIDDEN_DIM = 5120\\nTEXT_DIM = 384\\nLAYER_IDX = 2\\nWINDOW_SIZE = 10\\nSEED = 42\\n\\n\\ndef load_traces_with_sentences():\\n    \\\"\\\"\\\"Load R1-32B traces from HF and match with hidden states.\\\"\\\"\\\"\\n    print(\\\"Loading HarmThoughts dataset (r1-32b)...\\\")\\n    raw_traces = load_harmthoughts(\\\"r1-32b\\\")\\n\\n    traces = []\\n    for trace_id, steps in raw_traces.items():\\n        is_jailbreak = steps[0][\\\"final_judgment\\\"] == 1.0\\n        if not is_jailbreak:\\n            continue\\n        labels = [s[\\\"label\\\"] for s in steps]\\n        cp = extract_commitment_point(labels)\\n        if cp is None:\\n            continue\\n\\n        hs_path = HS_DIR / f\\\"{trace_id}.pt\\\"\\n        if not hs_path.exists():\\n            continue\\n\\n        sentences = [s[\\\"sentence\\\"] for s in steps]\\n        step_labels = create_step_labels(cp, len(sentences))\\n\\n        hs_data = torch.load(hs_path, map_location=\\\"cpu\\\", weights_only=False)\\n\\n        traces.append({\\n            \\\"trace_id\\\": trace_id,\\n            \\\"sentences\\\": sentences,\\n            \\\"hidden_states\\\": hs_data[\\\"hidden_stat
…[truncated 1144 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T06:20:38.719085+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "cat /root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_001a_bootstrap_hs_vs_text.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "cat /root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_001a_bootstrap_hs_vs_text.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-17T06:20:38.719353+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Phase 5b: Pre-CP FPR Paired Bootstrap Test - HS probe vs Text probe for R1-32B.\\\"\\\"\\\"\\n\\nimport os, sys, json\\nos.environ[\\\"TOKENIZERS_PARALLELISM\\\"] = \\\"false\\\"\\nos.environ[\\\"HF_ENDPOINT\\\"] = \\\"https://hf-mirror.com\\\"\\n\\nimport numpy as np\\nimport torch\\nfrom sklearn.linear_model import LogisticRegression\\nfrom pathlib import Path\\n\\nsys.path.insert(0, \\\"/root/autodl-tmp/contrastive_trace_safety\\\")\\nfrom src.data_loader import load_harmthoughts, extract_commitment_point, create_step_labels\\nfrom src.config import SAFETY_LABELS\\n\\nHS_DIR = Path(\\\"/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b\\\")\\nOUTPUT_DIR = Path(\\\"/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_001a\\\")\\nHIDDEN_DIM = 5120\\nTEXT_DIM = 384\\nLAYER_IDX = 2\\nWINDOW_SIZE = 10\\nSEED = 42\\n\\n\\ndef load_traces_with_sentences():\\n    \\\"\\\"\\\"Load R1-32B traces from HF and match with hidden states.\\\"\\\"\\\"\\n    print(\\\"Loading HarmThoughts dataset (r1-32b)...\\\")\\n    raw_traces = load_harmthoughts(\\\"r1-32b\\\")\\n\\n    traces = []\\n    for trace_id, steps in raw_traces.items():\\n        is_jailbreak = steps[0][\\\"final_judgment\\\"] == 1.0\\n        if not is_jailbreak:\\n            continue\\n        labels = [s[\\\"label\\\"] for s in steps]\\n        cp = extract_commitment_point(labels)\\n        if cp is None:\\n            continue\\n\\n        hs_path = HS_DIR / f\\\"{trace_id}.pt\\\"\\n        if not hs_path.exists():\\n            continue\\n\\n        sentences = [s[\\\"sentence\\\"] for s in steps]\\n        step_labels = create_step_labels(cp, len(sentences))\\n\\n        hs_data = torch.load(hs_path, map_location=\\\"cpu\\\", weights_only=False)\\n\\n        traces.append({\\n            \\\"trace_id\\\": trace_id,\\n            \\\"sentences\\\": sentences,\\n            \\\"hidden_states\\\": hs_data[\\\"hidden_stat
…[truncated 7148 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T06:20:38.719551+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "df -h /root/autodl-tmp",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "df -h /root/autodl-tmp",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-17T06:20:38.719734+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Filesystem      Size  Used Avail Use% Mounted on\\n/dev/md0        250G  161G   90G  65% /root/autodl-tmp\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-17T06:20:38.719870+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "nvidia-smi --query-gpu=name,memory.total,memory.used,memory.free --format=csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "nvidia-smi --query-gpu=name,memory.total,memory.used,memory.free --format=csv",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-17T06:20:38.719998+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"name, memory.total [MiB], memory.used [MiB], memory.free [MiB]\\nNVIDIA RTX PRO 6000 Blackwell Server Edition, 97887 MiB, 0 MiB, 97253 MiB\\nNVIDIA RTX PRO 6000 Blackwell Server Edition, 97887 MiB, 0 MiB, 97253 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-17T06:20:38.720120+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "ls /root/autodl-tmp/contrastive_trace_safety/artifacts/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "ls /root/autodl-tmp/contrastive_trace_safety/artifacts/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-17T06:20:38.720261+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"acc_precision_bootstrap\\ndiagnostics\\neval_results.json\\nexp_001a\\nexp_001a_extraction.log\\nexp_001a_probing.log\\nexp_001b\\nexp_003_cross_transfer\\nexp_005_trajguard\\nexp_006_bootstrap\\nexp_007_window_ablation\\nexp_013_text_baseline\\nexp_014_bocpd\\nexp_015_fpr\\nexp_c2_control\\nexp_pathC_two_stage\\nfigures\\nhidden_states\\nhidden_states_qwq_32b\\nhidden_states_r1_32b\\nhs_vs_text_acc_prec.json\\nm001_layer_fix\\nmetric_correlation\\npaper_data\\nprobes\\nqwq_paired_bootstrap_w5\\nqwq_text_verify\\nr1_32b_paired_bootstrap\\nr1_8b_balanced_recompute\\nr1_8b_bootstrap_hs_text\\nr1_8b_bootstrap_run.log\\nreport_hs_vs_text_acc.md\\nreport_r1_32b_selectivity_l10.md\\ntext_window_ablation_r1_8b\\ntext_window_ablation_r1_8b_run.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-17T06:20:38.720414+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "ls /root/autodl-tmp/.hf_cache/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "ls /root/autodl-tmp/.hf_cache/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-17T06:20:38.720656+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Qwen\\ndatasets\\ndeepseek-ai\\nhub\\nishitakakkar-10___harm_thoughts\\nmodels--deepseek-ai--DeepSeek-R1-Distill-Qwen-7B\\nmodels--microsoft--unixcoder-base\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-17T06:20:38.720832+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "cd /root/autodl-tmp/contrastive_trace_safety && HF_ENDPOINT=https://hf-mirror.com /root/miniconda3/bin/python3.12 -c \"\nfrom datasets import load_dataset\nds = load_dataset('ishitakakkar-10/HarmThoughts', split='train')\nmodels = set(ds['model_name'])\nprint('Models in dataset:', models)\nfor m in models:\n    subset = ds.filter(lambda x: x['model_name'] == m)\n    jb = subset.filter(lambda x: x['final_judgment'] == 1.0)\n    print(f'  {m}: total={len(subset)}, jailbreak_steps={len(jb)}')\n\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "cd /root/autodl-tmp/contrastive_trace_safety && HF_ENDPOINT=https://hf-mirror.com /root/miniconda3/bin/python3.12 -c \"\nfrom datasets import load_dataset\nds = load_dataset('ishitakakkar-10/HarmThoughts', split='train')\nmodels = set(ds['model_name'])\nprint('Models in dataset:', models)\nfor m in models:\n    subset = ds.filter(lambda x: x['model_name'] == m)\n    jb = subset.filter(lambda x: x['final_judgment'] == 1.0)\n    print(f'  {m}: total={len(subset)}, jailbreak_steps={len(jb)}')\n\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-17T06:20:38.721000+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Models in dataset: {'r1-32b', 'r1-8b', 'QwQ', 'ot-7b'}\\n  r1-32b: total=8525, jailbreak_steps=5739\\n  r1-8b: total=14746, jailbreak_steps=12505\\n  QwQ: total=7007, jailbreak_steps=5108\\n  ot-7b: total=26653, jailbreak_steps=22171\\n\", \"stderr\": \"\\rFilter:   0%|          | 0/56931 [00:00<?, ? examples/s]\\rFilter:  30%|██▉       | 17000/56931 [00:00<00:00, 162483.98 examples/s]\\rFilter:  74%|███████▍  | 42000/56931 [00:00<00:00, 160770.35 examples/s]\\rFilter: 100%|██████████| 56931/56931 [00:00<00:00, 159256.33 examples/s]\\n\\rFilter:   0%|          | 0/8525 [00:00<?, ? examples/s]\\rFilter:  94%|█████████▍| 8000/8525 [00:00<00:00, 70272.68 examples/s]\\rFilter: 100%|██████████| 8525/8525 [00:00<00:00, 68815.45 examples/s]\\n\\rFilter:   0%|          | 0/56931 [00:00<?, ? examples/s]\\rFilter:  32%|███▏      | 18000/56931 [00:00<00:00, 167947.20 examples/s]\\rFilter:  61%|██████▏   | 35000/56931 [00:00<00:00, 162759.88 examples/s]\\rFilter:  91%|█████████▏| 52000/56931 [00:00<00:00, 162994.82 examples/s]\\rFilter: 100%|██████████| 56931/56931 [00:00<00:00, 164635.78 examples/s]\\n\\rFilter:   0%|          | 0/14746 [00:00<?, ? examples/s]\\rFilter:  54%|█████▍    | 8000/14746 [00:00<00:00, 73950.47 examples/s]\\rFilter: 100%|██████████| 14746/14746 [00:00<00:00, 72767.88 examples/s]\\n\\rFilter:   0%|          | 0/56931 [00:00<?, ? examples/s]\\rFilter:  32%|███▏      | 18000/56931 [00:00<00:00, 174194.52 examples/s]\\rFilter:  63%|██████▎   | 36000/56931 [00:00<00:00, 170607.07 examples/s]\\rFilter:  95%|█████████▍| 54000/56931 [00:00<00:00, 169006.60 examples/s]\\rFilter: 100%|██████████| 56931/56931 [00:00<00:00, 170211.83 examples/s]\\n\\rFilter:   0%|          | 0/7007 [00:00<?, ? examples/s]\\rFilter: 100%|██████████| 7007/7007 [00:00<00:00, 61628.43 examples/s]\\rFilter: 100%|██████████| 7007/7007 [00:00<00:00, 60961.65 examples/s]\\n\\rFilter:   0%|          | 0/56931 [00:00<?, ? examples/s]\
…[truncated 670 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-17T06:20:38.721197+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "cd /root/autodl-tmp/contrastive_trace_safety && HF_ENDPOINT=https://hf-mirror.com /root/miniconda3/bin/python3.12 -c \"\nimport sys\nsys.path.insert(0, '/root/autodl-tmp/contrastive_trace_safety')\nfrom src.data_loader import load_harmthoughts, extract_commitment_point\nfrom src.config import SAFETY_LABELS\nprint('SAFETY_LABELS:', SAFETY_LABELS)\n\nraw = load_harmthoughts('ot-7b')\nprint(f'Total ot-7b traces: {len(raw)}')\n\n# Count jailbreak with CP\njb_with_cp = 0\njb_no_cp = 0\nlengths = []\nfor tid, steps in raw.items():\n    if steps[0]['final_judgment'] != 1.0:\n        continue\n    labels = [s['label'] for s in steps]\n    cp = extract_commitment_point(labels)\n    if cp is not None:\n        jb_with_cp += 1\n        lengths.append(len(steps))\n    else:\n        jb_no_cp += 1\n\nimport numpy as np\nprint(f'Jailbreak with CP: {jb_with_cp}')\nprint(f'Jailbreak no CP: {jb_no_cp}')\nprint(f'Mean trace length: {np.mean(lengths):.1f}')\nprint(f'Max trace length: {max(lengths)}')\nprint(f'Min trace length: {min(lengths)}')\nprint(f'Median: {np.median(lengths):.1f}')\n\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "cd /root/autodl-tmp/contrastive_trace_safety && HF_ENDPOINT=https://hf-mirror.com /root/miniconda3/bin/python3.12 -c \"\nimport sys\nsys.path.insert(0, '/root/autodl-tmp/contrastive_trace_safety')\nfrom src.data_loader import load_harmthoughts, extract_commitment_point\nfrom src.config import SAFETY_LABELS\nprint('SAFETY_LABELS:', SAFETY_LABELS)\n\nraw = load_harmthoughts('ot-7b')\nprint(f'Total ot-7b traces: {len(raw)}')\n\n# Count jailbreak with CP\njb_with_cp = 0\njb_no_cp = 0\nlengths = []\nfor tid, steps in raw.items():\n    if steps[0]['final_judgment'] != 1.0:\n        continue\n    labels = [s['label'] for s in steps]\n    cp = extract_commitment_point(labels)\n    if cp is not None:\n        jb_with_cp += 1\n        lengths.append(len(steps))\n    else:\n        jb_no_cp += 1\n\nimport numpy as np\nprint(f'Jailbreak with CP: {jb_with_cp}')\nprint(f'Jailbreak no CP: {jb_no_cp}')\nprint(f'Mean trace length: {np.mean(lengths):.1f}')\nprint(f'Max trace length: {max(lengths)}')\nprint(f'Min trace length: {min(lengths)}')\nprint(f'Median: {np.median(lengths):.1f}')\n\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-17T06:20:38.721367+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"SAFETY_LABELS: {'RA', 'ED', 'CC', 'IA', 'AL'}\\nTotal ot-7b traces: 333\\nJailbreak with CP: 228\\nJailbreak no CP: 42\\nMean trace length: 80.1\\nMax trace length: 234\\nMin trace length: 21\\nMedian: 73.0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.85}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-17T06:20:38.721712+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "cat > /root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_ot7b_full_pipeline.py << 'SCRIPT'\n\"\"\"OpenThinker-7B Full Commitment Detection Pipeline.\"\"\"\n\nimport os, sys, json, time\nos.environ[\"HF_ENDPOINT\"] = \"https://hf-mirror.com\"\nos.environ[\"TOKENIZERS_PARALLELISM\"] = \"false\"\nos.environ[\"CUDA_VISIBLE_DEVICES\"] = \"0\"\n\nimport numpy as np\nimport torch\nfrom pathlib import Path\nfrom transformers import AutoTokenizer, AutoModelForCausalLM\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import balanced_accuracy_score, precision_score\nfrom tqdm import tqdm\n\nsys.path.insert(0, \"/root/autodl-tmp/contrastive_trace_safety\")\nfrom src.data_loader import load_harmthoughts, extract_commitment_point, create_step_labels\nfrom src.config import SAFETY_LABELS\n\nMODEL_NAME = \"open-thoughts/OpenThinker-7B\"\nMODEL_CACHE = \"/root/autodl-tmp/.hf_cache/open-thoughts/OpenThinker-7B\"\nHS_DIR = Path(\"/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_ot7b\")\nOUTPUT_DIR = Path(\"/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_ot7b_full_pipeline\")\nNUM_LAYERS = 28\nHIDDEN_DIM = 3584\nDEVICE = \"cuda:0\"\nMAX_LENGTH = 8192\nSEED = 42\nK_CONSECUTIVE = 5\nTHRESHOLD = 0.5\n\n# ============ DATA LOADING ============\n\ndef load_ot7b_traces():\n    raw_traces = load_harmthoughts(\"ot-7b\")\n    traces = []\n    for trace_id, steps in raw_traces.items():\n        if steps[0][\"final_judgment\"] != 1.0:\n            continue\n        labels = [s[\"label\"] for s in steps]\n        cp = extract_commitment_point(labels)\n        if cp is None:\n            continue\n        sentences = [s[\"sentence\"] for s in steps]\n        step_labels = create_step_labels(cp, len(sentences))\n        traces.append({\n            \"trace_id\": trace_id,\n            \"sentences\": sentences,\n            \"labels\": labels,\n            \"commitment_point\": cp,\n            \"step_labels\": step_labels,\n            \"query\": steps[0][\"query\"],\n        })\n    return traces\n\n# ============ HIDDEN STATE EXTRACTION ============\n\ndef find_sentence_boundaries(tokenizer, sentences):\n    full_text = \" \".join(sentences)\n    encoding = tokenizer(\n        full_text,\n        return_offsets_mapping=True,\n        return_tensors=\"pt\",\n        truncation=True,\n        max_length=MAX_LENGTH,\n    )\n    offsets = encoding[\"offset_mapping\"][0]\n    boundaries = []\n    char_pos = 0\n    for sent in sentences:\n        char_end = char_pos + len(sent)\n        last_token_idx = 0\n        for tok_idx, (start, end) in enumerate(offsets):\n            if start < char_end:\n                last_token_idx = tok_idx\n        boundaries.append(last_token_idx)\n        char_pos = char_end + 1\n    return boundaries\n\n\ndef extract_trace(model, tokenizer, sentences):\n    boundary_positions = find_sentence_boundaries(tokenizer, sentences)\n    full_text = \" \".join(sentences)\n    inputs = tokenizer(\n        full_text, return_tensors=\"pt\", truncation=True, max_length=MAX_LENGTH\n    ).to(DEVICE)\n\n    num_tokens = inputs[\"input_ids\"].shape[1]\n    boundary_positions = [min(p, num_tokens - 1) for p in boundary_positions]\n\n    with torch.no_grad():\n        outputs = model(**inputs, output_hidden_states=True)\n\n    hidden_states = outputs.hidden_states\n    num_sentences = len(sentences)\n    result = torch.zeros(num_sentences, NUM_LAYERS, HIDDEN_DIM, dtype=torch.bfloat16)\n\n    for sent_idx, pos in enumerate(boundary_positions):\n        for layer_idx in range(NUM_LAYERS):\n            hs = hidden_states[layer_idx + 1][0, pos, :]\n            result[sent_idx, layer_idx, :] = hs.cpu()\n\n    del outputs, hidden_states\n    torch.cuda.empty_cache()\n    return result, num_tokens\n\n\ndef phase1_extract(traces):\n    \"\"\"Extract hidden states for all traces.\"\"\"\n    HS_DIR.mkdir(parents=True, exist_ok=True)\n    \n    existing = {f.stem for f in HS_DIR.glob(\"*.pt\")}\n    remaining = [t for t in traces if t[\"trace_id\"] not in existing]\n    print(f\"Already extracted: {len(existing)}, remaining: {len(remaining)}\")\n    \n    if not remaining:\n        print(\"All traces already extracted.\")\n        return\n    \n    print(\"Loading OpenThinker-7B model...\")\n    t0 = time.time()\n    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True, cache_dir=\"/root/autodl-tmp/.hf_cache\")\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n    \n    model = AutoModelForCausalLM.from_pretrained(\n        MODEL_NAME, torch_dtype=torch.bfloat16, device_map=DEVICE,\n        trust_remote_code=True, cache_dir=\"/root/autodl-tmp/.hf_cache\"\n    )\n    model.eval()\n    print(f\"Model loaded in {time.time()-t0:.1f}s\")\n    \n    errors = []\n    for i, trace in enumerate(tqdm(remaining, desc=\"Extracting HS\")):\n        try:\n            hs, ntok = extract_trace(model, tokenizer, trace[\"sentences\"])\n            save_dict = {\n                \"hidden_states\": hs,\n                \"trace_id\": trace[\"trace_id\"],\n                \"num_sentences\": len(trace[\"sentences\"]),\n                \"commitment_point\": trace[\"commitment_point\"],\n                \"step_labels\": trace[\"step_labels\"],\n                \"query\": trace[\"query\"],\n            }\n            torch.save(save_dict, HS_DIR / f\"{trace['trace_id']}.pt\")\n        except Exception as e:\n            errors.append({\"trace_id\": trace[\"trace_id\"], \"error\": str(e)})\n            print(f\"\\nError on {trace['trace_id']}: {e}\")\n            torch.cuda.empty_cache()\n        \n        if (i + 1) % 20 == 0:\n            mem = torch.cuda.memory_allocated() / 1e9\n            print(f\"\\n  [{i+1}/{len(remaining)}] GPU mem: {mem:.1f}GB\")\n    \n    print(f\"\\nExtraction done. Errors: {len(errors)}\")\n    if errors:\n        for e in errors[:5]:\n            print(f\"  {e['trace_id']}: {e['error']}\")\n    \n    # Free GPU memory\n    del model, tokenizer\n    torch.cuda.empty_cache()\n    \n    return errors\n\n# ============ ANALYSIS FUNCTIONS ============\n\ndef load_extracted_traces():\n    traces = []\n    for pt_file in sorted(HS_DIR.glob(\"*.pt\")):\n        data = torch.load(pt_file, map_location=\"cpu\", weights_only=False)\n        if data.get(\"step_labels\") is None or data.get(\"commitment_point\") is None:\n            continue\n        traces.append(data)\n    return traces\n\n\ndef split_traces(traces, seed=SEED):\n    rng = np.random.default_rng(seed)\n    indices = rng.permutation(len(traces))\n    n_train = int(len(traces) * 0.6)\n    n_val = int(len(traces) * 0.2)\n    return (\n        [traces[i] for i in indices[:n_train]],\n        [traces[i] for i in indices[n_train:n_train+n_val]],\n        [traces[i] for i in indices[n_train+n_val:]],\n    )\n\n\ndef extract_layer_data(traces, layer_idx):\n    X_list, y_list = [], []\n    for t in traces:\n        hs = t[\"hidden_states\"][:, layer_idx, :].float().numpy()\n        labels = np.array(t[\"step_labels\"])\n        n = min(hs.shape[0], len(labels))\n        X_list.append(hs[:n])\n        y_list.append(labels[:n])\n    return np.concatenate(X_list), np.concatenate(y_list)\n\n\ndef first_crossing(probs, threshold=THRESHOLD, k=K_CONSECUTIVE):\n    for i in range(len(probs) - k + 1):\n        if all(p > threshold for p in probs[i:i+k]):\n            return i\n    return None\n\n\ndef evaluate_crossing(clf, traces, layer_idx):\n    lead_times = []\n    n_crossings = 0\n    for t in traces:\n        hs = t[\"hidden_states\"][:, layer_idx, :].float().numpy()\n        labels = np.array(t[\"step_labels\"])\n        n = min(hs.shape[0], len(labels))\n        probs = clf.predict_proba(hs[:n])[:, 1]\n        cp = t[\"commitment_point\"]\n        fc = first_crossing(probs.tolist())\n        if fc is not None and fc < cp:\n            lead_times.append(cp - fc)\n            n_crossings += 1\n    crossing_rate = n_crossings / len(traces) if traces else 0\n    mean_lead = float(np.mean(lead_times)) if lead_times else 0.0\n    return crossing_rate, mean_lead\n\n\ndef compute_pre_cp_fpr(clf, traces, layer_idx=None, use_text=False, window_size=None):\n    \"\"\"Compute trace-level pre-CP FPR.\"\"\"\n    fprs = []\n    for t in traces:\n        cp = t[\"commitment_point\"]\n        if cp <= 0:\n            continue\n        if use_text:\n            emb = t[\"text_embeddings\"][:cp]\n            if window_size:\n                X = build_window_features_single(emb, window_size, emb.shape[1])\n            else:\n                X = emb\n        else:\n            hs = t[\"hidden_states\"][:cp, layer_idx, :].float().numpy()\n            if window_size:\n                X = build_window_features_single(hs, window_size, hs.shape[1])\n            else:\n                X = hs\n        preds = clf.predict(X)\n        fpr = float(np.mean(preds)) if len(preds) > 0 else 0.0\n        fprs.append(fpr)\n    return fprs\n\n\ndef build_window_features_single(features, window_size, dim):\n    \"\"\"Build windowed features for a single sequence.\"\"\"\n    n = features.shape[0]\n    X = []\n    for i in range(n):\n        start = max(0, i - window_size + 1)\n        window = features[start:i+1]\n        if len(window) < window_size:\n            pad = np.zeros((window_size - len(window), dim), dtype=np.float32)\n            window = np.concatenate([pad, window], axis=0)\n        X.append(window.flatten())\n    return np.array(X, dtype=np.float32)\n\n\ndef make_temporal_features(traces, layer_idx, window_size):\n    X_list, y_list = [], []\n    for t in traces:\n        hs = t[\"hidden_states\"][:, layer_idx, :].float().numpy()\n        labels = np.array(t[\"step_labels\"])\n        n = min(hs.shape[0], len(labels))\n        hs = hs[:n]\n        labels = labels[:n]\n        X = build_window_features_single(hs, window_size, HIDDEN_DIM)\n        X_list.append(X)\n        y_list.append(labels)\n    return np.vstack(X_list), np.concatenate(y_list)\n\n\ndef make_text_temporal_features(traces, window_size):\n    X_list, y_list = [], []\n    for t in traces:\n        emb = t[\"text_embeddings\"]\n        labels = np.array(t[\"step_labels\"])\n        n = min(emb.shape[0], len(labels))\n        emb = emb[:n]\n        labels = labels[:n]\n        X = build_window_features_single(emb, window_size, emb.shape[1])\n        X_list.append(X)\n        y_list.append(labels)\n    return np.vstack(X_list), np.concatenate(y_list)\n\n\n# ============ PHASE 2: LAYER SWEEP ============\n\ndef phase2_layer_sweep(train, val, test):\n    print(\"\\n\" + \"=\"*60)\n    print(\"PHASE 2: Layer Sweep (28 layers)\")\n    print(\"=\"*60)\n    \n    results = []\n    for layer_idx in range(NUM_LAYERS):\n        X_train, y_train = extract_layer_data(train, layer_idx)\n        X_test, y_test = extract_layer_data(test, layer_idx)\n        \n        clf = LogisticRegression(solver='liblinear', C=1.0, max_iter=1000,\n                                 class_weight='balanced', random_state=SEED)\n        clf.fit(X_train, y_train)\n        \n        y_pred = clf.predict(X_test)\n        bal_acc = balanced_accuracy_score(y_test, y_pred)\n        crossing_rate, lead_mean = evaluate_crossing(clf, test, layer_idx)\n        \n        # Pre-CP FPR\n        fprs = compute_pre_cp_fpr(clf, test, layer_idx=layer_idx)\n        pre_cp_fpr = float(np.mean(fprs)) if fprs else 0.0\n        \n        score = bal_acc * crossing_rate\n        results.append({\n            \"layer_idx\": layer_idx,\n            \"bal_acc\": float(bal_acc),\n            \"crossing_rate\": float(crossing_rate),\n            \"lead_mean\": float(lead_mean),\n            \"pre_cp_fpr\": float(pre_cp_fpr),\n            \"score\": float(score),\n        })\n        \n        if layer_idx % 4 == 0 or layer_idx == NUM_LAYERS - 1:\n            print(f\"  Layer {layer_idx:2d}: bal_acc={bal_acc:.4f} cross={crossing_rate:.4f} lead={lead_mean:.1f} fpr={pre_cp_fpr:.4f} score={score:.4f}\")\n    \n    sorted_results = sorted(results, key=lambda x: x[\"score\"], reverse=True)\n    best = sorted_results[0]\n    print(f\"\\nBest layer: {best['layer_idx']} (depth={best['layer_idx']/NUM_LAYERS*100:.0f}%)\")\n    print(f\"  bal_acc={best['bal_acc']:.4f}, crossing_rate={best['crossing_rate']:.4f}, lead_mean={best['lead_mean']:.1f}\")\n    \n    return best[\"layer_idx\"], results\n\n\n# ============ PHASE 3: TEMPORAL PROBES ============\n\ndef phase3_temporal_probes(train, val, test, best_layer):\n    print(\"\\n\" + \"=\"*60)\n    print(f\"PHASE 3: Temporal LR Probes (layer={best_layer})\")\n    print(\"=\"*60)\n    \n    windows = [1, 3, 5, 10, 15, 20, 25]\n    results = []\n    \n    for w in windows:\n        X_train, y_train = make_temporal_features(train, best_layer, w)\n        X_val, y_val = make_temporal_features(val, best_layer, w)\n        X_test, y_test = make_temporal_features(test, best_layer, w)\n        \n        clf = LogisticRegression(solver='liblinear', C=1.0, max_iter=1000,\n                                 class_weight='balanced', random_state=SEED)\n        clf.fit(X_train, y_train)\n        \n        y_pred = clf.predict(X_test)\n        bal_acc = balanced_accuracy_score(y_test, y_pred)\n        prec = precision_score(y_test, y_pred, zero_division=0)\n        \n        # Coverage (fraction of test traces where crossing happens before end)\n        n_cover = 0\n        for t in test:\n            hs = t[\"hidden_states\"][:, best_layer, :].float().numpy()\n            labels = np.array(t[\"step_labels\"])\n            n = min(hs.shape[0], len(labels))\n            X_t = build_window_features_single(hs[:n], w, HIDDEN_DIM)\n            probs = clf.predict_proba(X_t)[:, 1]\n            fc = first_crossing(probs.tolist())\n            if fc is not None:\n                n_cover += 1\n        coverage = n_cover / len(test)\n        \n        # Pre-CP FPR (trace-level)\n        fprs = []\n        for t in test:\n            cp = t[\"commitment_point\"]\n            if cp <= 0:\n                continue\n            hs = t[\"hidden_states\"][:cp, best_layer, :].float().numpy()\n            X_pre = build_window_features_single(hs, w, HIDDEN_DIM)\n            preds = clf.predict(X_pre)\n            fprs.append(float(np.mean(preds)))\n        pre_cp_fpr = float(np.mean(fprs))\n        \n        # Lead mean\n        leads = []\n        for t in test:\n            hs = t[\"hidden_states\"][:, best_layer, :].float().numpy()\n            labels = np.array(t[\"step_labels\"])\n            n = min(hs.shape[0], len(labels))\n            X_t = build_window_features_single(hs[:n], w, HIDDEN_DIM)\n            probs = clf.predict_proba(X_t)[:, 1]\n            cp = t[\"commitment_point\"]\n            fc = first_crossing(probs.tolist())\n            if fc is not None and fc < cp:\n                leads.append(cp - fc)\n        lead_mean = float(np.mean(leads)) if leads else 0.0\n        \n        results.append({\n            \"window\": w,\n            \"bal_acc\": float(bal_acc),\n            \"precision\": float(prec),\n            \"coverage\": float(coverage),\n            \"pre_cp_fpr\": float(pre_cp_fpr),\n            \"lead_mean\": float(lead_mean),\n        })\n        print(f\"  W={w:2d}: bal_acc={bal_acc:.4f} prec={prec:.4f} cov={coverage:.4f} fpr={pre_cp_fpr:.4f} lead={lead_mean:.1f}\")\n    \n    best_w_result = max(results, key=lambda x: x[\"bal_acc\"])\n    print(f\"\\nBest W={best_w_result['window']} (bal_acc={best_w_result['bal_acc']:.4f})\")\n    return results, best_w_result[\"window\"]\n\n\n# ============ PHASE 4: TEXT PROBES ============\n\ndef phase4_text_probes(train, val, test):\n    print(\"\\n\" + \"=\"*60)\n    print(\"PHASE 4: Text Probes (all-MiniLM-L6-v2)\")\n    print(\"=\"*60)\n    \n    from sentence_transformers import SentenceTransformer\n    st_model = SentenceTransformer('all-MiniLM-L6-v2', device='cpu')\n    TEXT_DIM = 384\n    \n    print(\"Encoding text embeddings...\")\n    all_traces = train + val + test\n    for i, t in enumerate(all_traces):\n        emb = st_model.encode(t[\"sentences\"], batch_size=64, show_progress_bar=False)\n        t[\"text_embeddings\"] = emb.astype(np.float32)\n        if (i + 1) % 50 == 0:\n            print(f\"  Encoded {i+1}/{len(all_traces)}\")\n    print(f\"  Done encoding {len(all_traces)} traces\")\n    \n    del st_model\n    \n    windows = [1, 3, 5, 10, 15, 20, 25]\n    results = []\n    \n    for w in windows:\n        X_train, y_train = make_text_temporal_features(train, w)\n        X_test, y_test = make_text_temporal_features(test, w)\n        \n        clf = LogisticRegression(solver='liblinear', C=1.0, max_iter=1000,\n                                 class_weight='balanced', random_state=SEED)\n        clf.fit(X_train, y_train)\n        \n        y_pred = clf.predict(X_test)\n        bal_acc = balanced_accuracy_score(y_test, y_pred)\n        prec = precision_score(y_test, y_pred, zero_division=0)\n        \n        # Coverage\n        n_cover = 0\n        for t in test:\n            emb = t[\"text_embeddings\"]\n            labels = np.array(t[\"step_labels\"])\n            n = min(emb.shape[0], len(labels))\n            X_t = build_window_features_single(emb[:n], w, TEXT_DIM)\n            probs = clf.predict_proba(X_t)[:, 1]\n            fc = first_crossing(probs.tolist())\n            if fc is not None:\n                n_cover += 1\n        coverage = n_cover / len(test)\n        \n        # Pre-CP FPR\n        fprs = []\n        for t in test:\n            cp = t[\"commitment_point\"]\n            if cp <= 0:\n                continue\n            emb = t[\"text_embeddings\"][:cp]\n            X_pre = build_window_features_single(emb, w, TEXT_DIM)\n            preds = clf.predict(X_pre)\n            fprs.append(float(np.mean(preds)))\n        pre_cp_fpr = float(np.mean(fprs))\n        \n        # Lead mean\n        leads = []\n        for t in test:\n            emb = t[\"text_embeddings\"]\n            labels = np.array(t[\"step_labels\"])\n            n = min(emb.shape[0], len(labels))\n            X_t = build_window_features_single(emb[:n], w, TEXT_DIM)\n            probs = clf.predict_proba(X_t)[:, 1]\n            cp = t[\"commitment_point\"]\n            fc = first_crossing(probs.tolist())\n            if fc is not None and fc < cp:\n                leads.append(cp - fc)\n        lead_mean = float(np.mean(leads)) if leads else 0.0\n        \n        results.append({\n            \"window\": w,\n            \"bal_acc\": float(bal_acc),\n            \"precision\": float(prec),\n            \"coverage\": float(coverage),\n            \"pre_cp_fpr\": float(pre_cp_fpr),\n            \"lead_mean\": float(lead_mean),\n        })\n        print(f\"  W={w:2d}: bal_acc={bal_acc:.4f} prec={prec:.4f} cov={coverage:.4f} fpr={pre_cp_fpr:.4f} lead={lead_mean:.1f}\")\n    \n    return results\n\n\n# ============ PHASE 5: PAIRED BOOTSTRAP ============\n\ndef phase5_bootstrap(train, test, best_layer, best_w):\n    print(\"\\n\" + \"=\"*60)\n    print(f\"PHASE 5: Paired Bootstrap (layer={best_layer}, W={best_w})\")\n    print(\"=\"*60)\n    \n    TEXT_DIM = 384\n    N_RESAMPLES = 1000\n    \n    # Train both probes\n    X_train_hs, y_train_hs = make_temporal_features(train, best_layer, best_w)\n    clf_hs = LogisticRegression(solver='liblinear', C=1.0, max_iter=1000,\n                                class_weight='balanced', random_state=SEED)\n    clf_hs.fit(X_train_hs, y_train_hs)\n    \n    X_train_text, y_train_text = make_text_temporal_features(train, best_w)\n    clf_text = LogisticRegression(solver='liblinear', C=1.0, max_iter=1000,\n                                  class_weight='balanced', random_state=SEED)\n    clf_text.fit(X_train_text, y_train_text)\n    \n    # Get per-trace metrics\n    hs_bal_accs, text_bal_accs = [], []\n    hs_precs, text_precs = [], []\n    hs_fprs, text_fprs = [], []\n    \n    for t in test:\n        cp = t[\"commitment_point\"]\n        hs = t[\"hidden_states\"][:, best_layer, :].float().numpy()\n        labels = np.array(t[\"step_labels\"])\n        n = min(hs.shape[0], len(labels))\n        \n        # HS predictions\n        X_hs = build_window_features_single(hs[:n], best_w, HIDDEN_DIM)\n        hs_pred = clf_hs.predict(X_hs)\n        hs_ba = balanced_accuracy_score(labels[:n], hs_pred)\n        hs_p = precision_score(labels[:n], hs_pred, zero_division=0)\n        hs_fpr_val = float(np.mean(hs_pred[:cp])) if cp > 0 else 0.0\n        \n        # Text predictions\n        emb = t[\"text_embeddings\"]\n        X_text = build_window_features_single(emb[:n], best_w, TEXT_DIM)\n        text_pred = clf_text.predict(X_text)\n        text_ba = balanced_accuracy_score(labels[:n], text_pred)\n        text_p = precision_score(labels[:n], text_pred, zero_division=0)\n        text_fpr_val = float(np.mean(text_pred[:cp])) if cp > 0 else 0.0\n        \n        hs_bal_accs.append(hs_ba)\n        text_bal_accs.append(text_ba)\n        hs_precs.append(hs_p)\n        text_precs.append(text_p)\n        hs_fprs.append(hs_fpr_val)\n        text_fprs.append(text_fpr_val)\n    \n    hs_bal_accs = np.array(hs_bal_accs)\n    text_bal_accs = np.array(text_bal_accs)\n    hs_precs = np.array(hs_precs)\n    text_precs = np.array(text_precs)\n    hs_fprs = np.array(hs_fprs)\n    text_fprs = np.array(text_fprs)\n    \n    def paired_bootstrap(metric_a, metric_b, n_resamples=N_RESAMPLES):\n        n = len(metric_a)\n        observed_diff = float(np.mean(metric_a) - np.mean(metric_b))\n        rng = np.random.default_rng(SEED)\n        diffs = []\n        for _ in range(n_resamples):\n            idx = rng.integers(0, n, size=n)\n            diffs.append(np.mean(metric_a[idx]) - np.mean(metric_b[idx]))\n        diffs = np.array(diffs)\n        # Two-sided p-value\n        p_value = float(np.mean(np.abs(diffs - np.mean(diffs)) >= np.abs(observed_diff)))\n        ci_lower = float(np.percentile(diffs, 2.5))\n        ci_upper = float(np.percentile(diffs, 97.5))\n        return observed_diff, ci_lower, ci_upper, p_value\n    \n    results = {}\n    for metric_name, hs_arr, text_arr in [\n        (\"bal_acc\", hs_bal_accs, text_bal_accs),\n        (\"precision\", hs_precs, text_precs),\n        (\"pre_cp_fpr\", hs_fprs, text_fprs),\n    ]:\n        diff, ci_lo, ci_hi, p = paired_bootstrap(hs_arr, text_arr)\n        bonferroni_sig = \"Yes\" if p < 0.017 else \"No\"\n        results[metric_name] = {\n            \"hs_mean\": float(np.mean(hs_arr)),\n            \"text_mean\": float(np.mean(text_arr)),\n            \"delta\": diff,\n            \"ci_95\": [ci_lo, ci_hi],\n            \"p_value\": p,\n            \"bonferroni_sig\": bonferroni_sig,\n        }\n        print(f\"  {metric_name}: HS={np.mean(hs_arr):.4f} Text={np.mean(text_arr):.4f} delta={diff:.4f} p={p:.4f} Bonf={bonferroni_sig}\")\n    \n    return results\n\n\n# ============ PHASE 6: SELECTIVITY CONTROL ============\n\ndef phase6_selectivity(train, test, best_layer, best_w):\n    print(\"\\n\" + \"=\"*60)\n    print(f\"PHASE 6: Selectivity Control (layer={best_layer}, W={best_w})\")\n    print(\"=\"*60)\n    \n    # Real accuracy\n    X_train, y_train = make_temporal_features(train, best_layer, best_w)\n    X_test, y_test = make_temporal_features(test, best_layer, best_w)\n    \n    clf = LogisticRegression(solver='liblinear', C=1.0, max_iter=1000,\n                             class_weight='balanced', random_state=SEED)\n    clf.fit(X_train, y_train)\n    real_acc = balanced_accuracy_score(y_test, clf.predict(X_test))\n    \n    # Random permutation control\n    n_perms = 10\n    random_accs = []\n    rng = np.random.default_rng(SEED)\n    for perm_i in range(n_perms):\n        y_train_perm = rng.permutation(y_train)\n        clf_rand = LogisticRegression(solver='liblinear', C=1.0, max_iter=1000,\n                                      class_weight='balanced', random_state=SEED+perm_i)\n        clf_rand.fit(X_train, y_train_perm)\n        rand_acc = balanced_accuracy_score(y_test, clf_rand.predict(X_test))\n        random_accs.append(rand_acc)\n    \n    random_mean = float(np.mean(random_accs))\n    random_std = float(np.std(random_accs))\n    selectivity = float(real_acc - random_mean) * 100  # in pp\n    \n    print(f\"  real_acc: {real_acc:.4f}\")\n    print(f\"  random_mean +/- std: {random_mean:.4f} +/- {random_std:.4f}\")\n    print(f\"  selectivity: {selectivity:.1f} pp\")\n    \n    return {\n        \"real_acc\": float(real_acc),\n        \"random_mean\": random_mean,\n        \"random_std\": random_std,\n        \"selectivity_pp\": selectivity,\n        \"n_perms\": n_perms,\n        \"random_accs\": random_accs,\n    }\n\n\n# ============ MAIN ============\n\ndef main():\n    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)\n    \n    print(\"=\"*60)\n    print(\"OpenThinker-7B Full Pipeline (exp_ot7b_full_pipeline)\")\n    print(\"=\"*60)\n    \n    # Step 1: Load data\n    print(\"\\nStep 1: Loading ot-7b traces...\")\n    traces = load_ot7b_traces()\n    print(f\"  Found {len(traces)} jailbreak traces with commitment points\")\n    lengths = [len(t[\"sentences\"]) for t in traces]\n    print(f\"  Mean trace length: {np.mean(lengths):.1f} sentences\")\n    \n    # Step 2: Extract hidden states\n    print(\"\\nStep 2: Extracting hidden states...\")\n    errors = phase1_extract(traces)\n    \n    # Verify extraction\n    print(\"\\nVerifying extraction...\")\n    extracted = list(HS_DIR.glob(\"*.pt\"))\n    print(f\"  Total .pt files: {len(extracted)}\")\n    \n    # Spot check 3 random files\n    import random\n    random.seed(42)\n    checks = random.sample(extracted, min(3, len(extracted)))\n    for f in checks:\n        d = torch.load(f, map_location=\"cpu\", weights_only=False)\n        print(f\"  {f.stem}: shape={list(d['hidden_states'].shape)} CP={d['commitment_point']} n_sent={d['num_sentences']}\")\n    \n    # Step 3: Load extracted traces for analysis\n    print(\"\\nStep 3: Loading extracted hidden states...\")\n    all_traces = load_extracted_traces()\n    print(f\"  Loaded {len(all_traces)} traces\")\n    \n    train, val, test = split_traces(all_traces)\n    print(f\"  Split: train={len(train)}, val={len(val)}, test={len(test)}\")\n    \n    # Step 4: Layer sweep\n    best_layer, layer_results = phase2_layer_sweep(train, val, test)\n    \n    # Step 5: Temporal probes\n    hs_probe_results, best_w = phase3_temporal_probes(train, val, test, best_layer)\n    \n    # Step 6: Text probes\n    text_probe_results = phase4_text_probes(train, val, test)\n    \n    # Step 7: Bootstrap\n    bootstrap_results = phase5_bootstrap(train, test, best_layer, best_w)\n    \n    # Step 8: Selectivity\n    selectivity_results = phase6_selectivity(train, test, best_layer, best_w)\n    \n    # ============ SAVE RESULTS ============\n    print(\"\\n\" + \"=\"*60)\n    print(\"Saving results...\")\n    \n    final_results = {\n        \"experiment_id\": \"exp_ot7b_full_pipeline\",\n        \"model\": \"OpenThinker-7B (open-thoughts/OpenThinker-7B)\",\n        \"base_model\": \"Qwen2.5-7B\",\n        \"num_layers\": NUM_LAYERS,\n        \"hidden_dim\": HIDDEN_DIM,\n        \"data\": {\n            \"total_traces\": len(all_traces),\n            \"train\": len(train),\n            \"val\": len(val),\n            \"test\": len(test),\n            \"mean_trace_length\": float(np.mean([t[\"num_sentences\"] for t in all_traces])),\n        },\n        \"best_layer\": {\n            \"layer_idx\": best_layer,\n            \"depth_pct\": float(best_layer / NUM_LAYERS * 100),\n        },\n        \"layer_sweep\": layer_results,\n        \"hs_temporal_probes\": hs_probe_results,\n        \"text_temporal_probes\": text_probe_results,\n        \"best_window\": best_w,\n        \"bootstrap\": bootstrap_results,\n        \"selectivity\": selectivity_results,\n        \"config\": {\n            \"safety_labels\": list(SAFETY_LABELS),\n            \"solver\": \"liblinear\",\n            \"seed\": SEED,\n            \"k_consecutive\": K_CONSECUTIVE,\n            \"threshold\": THRESHOLD,\n            \"bootstrap_resamples\": 1000,\n            \"bonferroni_threshold\": 0.017,\n        },\n    }\n    \n    with open(OUTPUT_DIR / \"results.json\", \"w\") as f:\n        json.dump(final_results, f, indent=2)\n    print(f\"  Saved: {OUTPUT_DIR / 'results.json'}\")\n    \n    # Generate report\n    best_layer_info = next(r for r in layer_results if r[\"layer_idx\"] == best_layer)\n    report = f\"\"\"# OpenThinker-7B Results\n\n## Data\n- Total traces: {len(all_traces)} (jailbreak+CP)\n- Train/Val/Test split: {len(train)}/{len(val)}/{len(test)}\n- Mean trace length: {np.mean([t['num_sentences'] for t in all_traces]):.1f} sentences\n\n## Best Layer\n- Layer: {best_layer} (depth: {best_layer/NUM_LAYERS*100:.0f}%)\n- bal_acc: {best_layer_info['bal_acc']:.4f}, crossing_rate: {best_layer_info['crossing_rate']:.4f}\n\n## Temporal Probes (HS, layer={best_layer})\n| W | bal_acc | precision | coverage | pre_cp_fpr | lead_mean |\n|---|---------|-----------|----------|------------|-----------|\n\"\"\"\n    for r in hs_probe_results:\n        report += f\"| {r['window']} | {r['bal_acc']:.4f} | {r['precision']:.4f} | {r['coverage']:.4f} | {r['pre_cp_fpr']:.4f} | {r['lead_mean']:.1f} |\\n\"\n    \n    report += f\"\"\"\n## Text Probes (all-MiniLM-L6-v2)\n| W | bal_acc | precision | coverage | pre_cp_fpr | lead_mean |\n|---|---------|-----------|----------|------------|-----------|\n\"\"\"\n    for r in text_probe_results:\n        report += f\"| {r['window']} | {r['bal_acc']:.4f} | {r['precision']:.4f} | {r['coverage']:.4f} | {r['pre_cp_fpr']:.4f} | {r['lead_mean']:.1f} |\\n\"\n    \n    report += f\"\"\"\n## HS vs Text Bootstrap (W={best_w})\n| Metric | HS | Text | Delta | p-value | Bonferroni |\n|--------|-----|------|-------|---------|------------|\n\"\"\"\n    for metric_name in [\"bal_acc\", \"precision\", \"pre_cp_fpr\"]:\n        b = bootstrap_results[metric_name]\n        report += f\"| {metric_name} | {b['hs_mean']:.4f} | {b['text_mean']:.4f} | {b['delta']:.4f} | {b['p_value']:.4f} | {b['bonferroni_sig']} |\\n\"\n    \n    report += f\"\"\"\n## Selectivity Control\n- real_acc: {selectivity_results['real_acc']:.4f}\n- random_mean +/- std: {selectivity_results['random_mean']:.4f} +/- {selectivity_results['random_std']:.4f}\n- selectivity: {selectivity_results['selectivity_pp']:.1f} pp\n\"\"\"\n    \n    with open(OUTPUT_DIR / \"report.md\", \"w\") as f:\n        f.write(report)\n    print(f\"  Saved: {OUTPUT_DIR / 'report.md'}\")\n    \n    print(\"\\n\" + \"=\"*60)\n    print(\"PIPELINE COMPLETE\")\n    print(\"=\"*60)\n    print(report)\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT\necho \"Script written successfully\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "cat > /root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_ot7b_full_pipeline.py << 'SCRIPT'\n\"\"\"OpenThinker-7B Full Commitment Detection Pipeline.\"\"\"\n\nimport os, sys, json, time\nos.environ[\"HF_ENDPOINT\"] = \"https://hf-mirror.com\"\nos.environ[\"TOKENIZERS_PARALLELISM\"] = \"false\"\nos.environ[\"CUDA_VISIBLE_DEVICES\"] = \"0\"\n\nimport numpy as np\nimport torch\nfrom pathlib import Path\nfrom transformers import AutoTokenizer, AutoModelForCausalLM\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import balanced_accuracy_score, precision_score\nfrom tqdm import tqdm\n\nsys.path.insert(0, \"/root/autodl-tmp/contrastive_trace_safety\")\nfrom src.data_loader import load_harmthoughts, extract_commitment_point, create_step_labels\nfrom src.config import SAFETY_LABELS\n\nMODEL_NAME = \"open-thoughts/OpenThinker-7B\"\nMODEL_CACHE = \"/root/autodl-tmp/.hf_cache/open-thoughts/OpenThinker-7B\"\nHS_DIR = Path(\"/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_ot7b\")\nOUTPUT_DIR = Path(\"/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_ot7b_full_pipeline\")\nNUM_LAYERS = 28\nHIDDEN_DIM = 3584\nDEVICE = \"cuda:0\"\nMAX_LENGTH = 8192\nSEED = 42\nK_CONSECUTIVE = 5\nTHRESHOLD = 0.5\n\n# ============ DATA LOADING ============\n\ndef load_ot7b_traces():\n    raw_traces = load_harmthoughts(\"ot-7b\")\n    traces = []\n    for trace_id, steps in raw_traces.items():\n        if steps[0][\"final_judgment\"] != 1.0:\n            continue\n        labels = [s[\"label\"] for s in steps]\n        cp = extract_commitment_point(labels)\n        if cp is None:\n            continue\n        sentences = [s[\"sentence\"] for s in steps]\n        step_labels = create_step_labels(cp, len(sentences))\n        traces.append({\n            \"trace_id\": trace_id,\n            \"sentences\": sentences,\n            \"labels\": labels,\n            \"commitment_point\": cp,\n            \"step_labels\": step_labels,\n            \"query\": steps[0][\"query\"],\n        })\n    return traces\n\n# ============ HIDDEN STATE EXTRACTION ============\n\ndef find_sentence_boundaries(tokenizer, sentences):\n    full_text = \" \".join(sentences)\n    encoding = tokenizer(\n        full_text,\n        return_offsets_mapping=True,\n        return_tensors=\"pt\",\n        truncation=True,\n        max_length=MAX_LENGTH,\n    )\n    offsets = encoding[\"offset_mapping\"][0]\n    boundaries = []\n    char_pos = 0\n    for sent in sentences:\n        char_end = char_pos + len(sent)\n        last_token_idx = 0\n        for tok_idx, (start, end) in enumerate(offsets):\n            if start < char_end:\n                last_token_idx = tok_idx\n        boundaries.append(last_token_idx)\n        char_pos = char_end + 1\n    return boundaries\n\n\ndef extract_trace(model, tokenizer, sentences):\n    boundary_positions = find_sentence_boundaries(tokenizer, sentences)\n    full_text = \" \".join(sentences)\n    inputs = tokenizer(\n        full_text, return_tensors=\"pt\", truncation=True, max_length=MAX_LENGTH\n    ).to(DEVICE)\n\n    num_tokens = inputs[\"input_ids\"].shape[1]\n    boundary_positions = [min(p, num_tokens - 1) for p in boundary_positions]\n\n    with torch.no_grad():\n        outputs = model(**inputs, output_hidden_states=True)\n\n    hidden_states = outputs.hidden_states\n    num_sentences = len(sentences)\n    result = torch.zeros(num_sentences, NUM_LAYERS, HIDDEN_DIM, dtype=torch.bfloat16)\n\n    for sent_idx, pos in enumerate(boundary_positions):\n        for layer_idx in range(NUM_LAYERS):\n            hs = hidden_states[layer_idx + 1][0, pos, :]\n            result[sent_idx, layer_idx, :] = hs.cpu()\n\n    del outputs, hidden_states\n    torch.cuda.empty_cache()\n    return result, num_tokens\n\n\ndef phase1_extract(traces):\n    \"\"\"Extract hidden states for all traces.\"\"\"\n    HS_DIR.mkdir(parents=True, exist_ok=True)\n    \n    existing = {f.stem for f in HS_DIR.glob(\"*.pt\")}\n    remaining = [t for t in traces if t[\"trace_id\"] not in existing]\n    print(f\"Already extracted: {len(existing)}, remaining: {len(remaining)}\")\n    \n    if not remaining:\n        print(\"All traces already extracted.\")\n        return\n    \n    print(\"Loading OpenThinker-7B model...\")\n    t0 = time.time()\n    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True, cache_dir=\"/root/autodl-tmp/.hf_cache\")\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n    \n    model = AutoModelForCausalLM.from_pretrained(\n        MODEL_NAME, torch_dtype=torch.bfloat16, device_map=DEVICE,\n        trust_remote_code=True, cache_dir=\"/root/autodl-tmp/.hf_cache\"\n    )\n    model.eval()\n    print(f\"Model loaded in {time.time()-t0:.1f}s\")\n    \n    errors = []\n    for i, trace in enumerate(tqdm(remaining, desc=\"Extracting HS\")):\n        try:\n            hs, ntok = extract_trace(model, tokenizer, trace[\"sentences\"])\n            save_dict = {\n                \"hidden_states\": hs,\n                \"trace_id\": trace[\"trace_id\"],\n                \"num_sentences\": len(trace[\"sentences\"]),\n                \"commitment_point\": trace[\"commitment_point\"],\n                \"step_labels\": trace[\"step_labels\"],\n                \"query\": trace[\"query\"],\n            }\n            torch.save(save_dict, HS_DIR / f\"{trace['trace_id']}.pt\")\n        except Exception as e:\n            errors.append({\"trace_id\": trace[\"trace_id\"], \"error\": str(e)})\n            print(f\"\\nError on {trace['trace_id']}: {e}\")\n            torch.cuda.empty_cache()\n        \n        if (i + 1) % 20 == 0:\n            mem = torch.cuda.memory_allocated() / 1e9\n            print(f\"\\n  [{i+1}/{len(remaining)}] GPU mem: {mem:.1f}GB\")\n    \n    print(f\"\\nExtraction done. Errors: {len(errors)}\")\n    if errors:\n        for e in errors[:5]:\n            print(f\"  {e['trace_id']}: {e['error']}\")\n    \n    # Free GPU memory\n    del model, tokenizer\n    torch.cuda.empty_cache()\n    \n    return errors\n\n# ============ ANALYSIS FUNCTIONS ============\n\ndef load_extracted_traces():\n    traces = []\n    for pt_file in sorted(HS_DIR.glob(\"*.pt\")):\n        data = torch.load(pt_file, map_location=\"cpu\", weights_only=False)\n        if data.get(\"step_labels\") is None or data.get(\"commitment_point\") is None:\n            continue\n        traces.append(data)\n    return traces\n\n\ndef split_traces(traces, seed=SEED):\n    rng = np.random.default_rng(seed)\n    indices = rng.permutation(len(traces))\n    n_train = int(len(traces) * 0.6)\n    n_val = int(len(traces) * 0.2)\n    return (\n        [traces[i] for i in indices[:n_train]],\n        [traces[i] for i in indices[n_train:n_train+n_val]],\n        [traces[i] for i in indices[n_train+n_val:]],\n    )\n\n\ndef extract_layer_data(traces, layer_idx):\n    X_list, y_list = [], []\n    for t in traces:\n        hs = t[\"hidden_states\"][:, layer_idx, :].float().numpy()\n        labels = np.array(t[\"step_labels\"])\n        n = min(hs.shape[0], len(labels))\n        X_list.append(hs[:n])\n        y_list.append(labels[:n])\n    return np.concatenate(X_list), np.concatenate(y_list)\n\n\ndef first_crossing(probs, threshold=THRESHOLD, k=K_CONSECUTIVE):\n    for i in range(len(probs) - k + 1):\n        if all(p > threshold for p in probs[i:i+k]):\n            return i\n    return None\n\n\ndef evaluate_crossing(clf, traces, layer_idx):\n    lead_times = []\n    n_crossings = 0\n    for t in traces:\n        hs = t[\"hidden_states\"][:, layer_idx, :].float().numpy()\n        labels = np.array(t[\"step_labels\"])\n        n = min(hs.shape[0], len(labels))\n        probs = clf.predict_proba(hs[:n])[:, 1]\n        cp = t[\"commitment_point\"]\n        fc = first_crossing(probs.tolist())\n        if fc is not None and fc < cp:\n            lead_times.append(cp - fc)\n            n_crossings += 1\n    crossing_rate = n_crossings / len(traces) if traces else 0\n    mean_lead = float(np.mean(lead_times)) if lead_times else 0.0\n    return crossing_rate, mean_lead\n\n\ndef compute_pre_cp_fpr(clf, traces, layer_idx=None, use_text=False, window_size=None):\n    \"\"\"Compute trace-level pre-CP FPR.\"\"\"\n    fprs = []\n    for t in traces:\n        cp = t[\"commitment_point\"]\n        if cp <= 0:\n            continue\n        if use_text:\n            emb = t[\"text_embeddings\"][:cp]\n            if window_size:\n                X = build_window_features_single(emb, window_size, emb.shape[1])\n            else:\n                X = emb\n        else:\n            hs = t[\"hidden_states\"][:cp, layer_idx, :].float().numpy()\n            if window_size:\n                X = build_window_features_single(hs, window_size, hs.shape[1])\n            else:\n                X = hs\n        preds = clf.predict(X)\n        fpr = float(np.mean(preds)) if len(preds) > 0 else 0.0\n        fprs.append(fpr)\n    return fprs\n\n\ndef build_window_features_single(features, window_size, dim):\n    \"\"\"Build windowed features for a single sequence.\"\"\"\n    n = features.shape[0]\n    X = []\n    for i in range(n):\n        start = max(0, i - window_size + 1)\n        window = features[start:i+1]\n        if len(window) < window_size:\n            pad = np.zeros((window_size - len(window), dim), dtype=np.float32)\n            window = np.concatenate([pad, window], axis=0)\n        X.append(window.flatten())\n    return np.array(X, dtype=np.float32)\n\n\ndef make_temporal_features(traces, layer_idx, window_size):\n    X_list, y_list = [], []\n    for t in traces:\n        hs = t[\"hidden_states\"][:, layer_idx, :].float().numpy()\n        labels = np.array(t[\"step_labels\"])\n        n = min(hs.shape[0], len(labels))\n        hs = hs[:n]\n        labels = labels[:n]\n        X = build_window_features_single(hs, window_size, HIDDEN_DIM)\n        X_list.append(X)\n        y_list.append(labels)\n    return np.vstack(X_list), np.concatenate(y_list)\n\n\ndef make_text_temporal_features(traces, window_size):\n    X_list, y_list = [], []\n    for t in traces:\n        emb = t[\"text_embeddings\"]\n        labels = np.array(t[\"step_labels\"])\n        n = min(emb.shape[0], len(labels))\n        emb = emb[:n]\n        labels = labels[:n]\n        X = build_window_features_single(emb, window_size, emb.shape[1])\n        X_list.append(X)\n        y_list.append(labels)\n    return np.vstack(X_list), np.concatenate(y_list)\n\n\n# ============ PHASE 2: LAYER SWEEP ============\n\ndef phase2_layer_sweep(train, val, test):\n    print(\"\\n\" + \"=\"*60)\n    print(\"PHASE 2: Layer Sweep (28 layers)\")\n    print(\"=\"*60)\n    \n    results = []\n    for layer_idx in range(NUM_LAYERS):\n        X_train, y_train = extract_layer_data(train, layer_idx)\n        X_test, y_test = extract_layer_data(test, layer_idx)\n        \n        clf = LogisticRegression(solver='liblinear', C=1.0, max_iter=1000,\n                                 class_weight='balanced', random_state=SEED)\n        clf.fit(X_train, y_train)\n        \n        y_pred = clf.predict(X_test)\n        bal_acc = balanced_accuracy_score(y_test, y_pred)\n        crossing_rate, lead_mean = evaluate_crossing(clf, test, layer_idx)\n        \n        # Pre-CP FPR\n        fprs = compute_pre_cp_fpr(clf, test, layer_idx=layer_idx)\n        pre_cp_fpr = float(np.mean(fprs)) if fprs else 0.0\n        \n        score = bal_acc * crossing_rate\n        results.append({\n            \"layer_idx\": layer_idx,\n            \"bal_acc\": float(bal_acc),\n            \"crossing_rate\": float(crossing_rate),\n            \"lead_mean\": float(lead_mean),\n            \"pre_cp_fpr\": float(pre_cp_fpr),\n            \"score\": float(score),\n        })\n        \n        if layer_idx % 4 == 0 or layer_idx == NUM_LAYERS - 1:\n            print(f\"  Layer {layer_idx:2d}: bal_acc={bal_acc:.4f} cross={crossing_rate:.4f} lead={lead_mean:.1f} fpr={pre_cp_fpr:.4f} score={score:.4f}\")\n    \n    sorted_results = sorted(results, key=lambda x: x[\"score\"], reverse=True)\n    best = sorted_results[0]\n    print(f\"\\nBest layer: {best['layer_idx']} (depth={best['layer_idx']/NUM_LAYERS*100:.0f}%)\")\n    print(f\"  bal_acc={best['bal_acc']:.4f}, crossing_rate={best['crossing_rate']:.4f}, lead_mean={best['lead_mean']:.1f}\")\n    \n    return best[\"layer_idx\"], results\n\n\n# ============ PHASE 3: TEMPORAL PROBES ============\n\ndef phase3_temporal_probes(train, val, test, best_layer):\n    print(\"\\n\" + \"=\"*60)\n    print(f\"PHASE 3: Temporal LR Probes (layer={best_layer})\")\n    print(\"=\"*60)\n    \n    windows = [1, 3, 5, 10, 15, 20, 25]\n    results = []\n    \n    for w in windows:\n        X_train, y_train = make_temporal_features(train, best_layer, w)\n        X_val, y_val = make_temporal_features(val, best_layer, w)\n        X_test, y_test = make_temporal_features(test, best_layer, w)\n        \n        clf = LogisticRegression(solver='liblinear', C=1.0, max_iter=1000,\n                                 class_weight='balanced', random_state=SEED)\n        clf.fit(X_train, y_train)\n        \n        y_pred = clf.predict(X_test)\n        bal_acc = balanced_accuracy_score(y_test, y_pred)\n        prec = precision_score(y_test, y_pred, zero_division=0)\n        \n        # Coverage (fraction of test traces where crossing happens before end)\n        n_cover = 0\n        for t in test:\n            hs = t[\"hidden_states\"][:, best_layer, :].float().numpy()\n            labels = np.array(t[\"step_labels\"])\n            n = min(hs.shape[0], len(labels))\n            X_t = build_window_features_single(hs[:n], w, HIDDEN_DIM)\n            probs = clf.predict_proba(X_t)[:, 1]\n            fc = first_crossing(probs.tolist())\n            if fc is not None:\n                n_cover += 1\n        coverage = n_cover / len(test)\n        \n        # Pre-CP FPR (trace-level)\n        fprs = []\n        for t in test:\n            cp = t[\"commitment_point\"]\n            if cp <= 0:\n                continue\n            hs = t[\"hidden_states\"][:cp, best_layer, :].float().numpy()\n            X_pre = build_window_features_single(hs, w, HIDDEN_DIM)\n            preds = clf.predict(X_pre)\n            fprs.append(float(np.mean(preds)))\n        pre_cp_fpr = float(np.mean(fprs))\n        \n        # Lead mean\n        leads = []\n        for t in test:\n            hs = t[\"hidden_states\"][:, best_layer, :].float().numpy()\n            labels = np.array(t[\"step_labels\"])\n            n = min(hs.shape[0], len(labels))\n            X_t = build_window_features_single(hs[:n], w, HIDDEN_DIM)\n            probs = clf.predict_proba(X_t)[:, 1]\n            cp = t[\"commitment_point\"]\n            fc = first_crossing(probs.tolist())\n            if fc is not None and fc < cp:\n                leads.append(cp - fc)\n        lead_mean = float(np.mean(leads)) if leads else 0.0\n        \n        results.append({\n            \"window\": w,\n            \"bal_acc\": float(bal_acc),\n            \"precision\": float(prec),\n            \"coverage\": float(coverage),\n            \"pre_cp_fpr\": float(pre_cp_fpr),\n            \"lead_mean\": float(lead_mean),\n        })\n        print(f\"  W={w:2d}: bal_acc={bal_acc:.4f} prec={prec:.4f} cov={coverage:.4f} fpr={pre_cp_fpr:.4f} lead={lead_mean:.1f}\")\n    \n    best_w_result = max(results, key=lambda x: x[\"bal_acc\"])\n    print(f\"\\nBest W={best_w_result['window']} (bal_acc={best_w_result['bal_acc']:.4f})\")\n    return results, best_w_result[\"window\"]\n\n\n# ============ PHASE 4: TEXT PROBES ============\n\ndef phase4_text_probes(train, val, test):\n    print(\"\\n\" + \"=\"*60)\n    print(\"PHASE 4: Text Probes (all-MiniLM-L6-v2)\")\n    print(\"=\"*60)\n    \n    from sentence_transformers import SentenceTransformer\n    st_model = SentenceTransformer('all-MiniLM-L6-v2', device='cpu')\n    TEXT_DIM = 384\n    \n    print(\"Encoding text embeddings...\")\n    all_traces = train + val + test\n    for i, t in enumerate(all_traces):\n        emb = st_model.encode(t[\"sentences\"], batch_size=64, show_progress_bar=False)\n        t[\"text_embeddings\"] = emb.astype(np.float32)\n        if (i + 1) % 50 == 0:\n            print(f\"  Encoded {i+1}/{len(all_traces)}\")\n    print(f\"  Done encoding {len(all_traces)} traces\")\n    \n    del st_model\n    \n    windows = [1, 3, 5, 10, 15, 20, 25]\n    results = []\n    \n    for w in windows:\n        X_train, y_train = make_text_temporal_features(train, w)\n        X_test, y_test = make_text_temporal_features(test, w)\n        \n        clf = LogisticRegression(solver='liblinear', C=1.0, max_iter=1000,\n                                 class_weight='balanced', random_state=SEED)\n        clf.fit(X_train, y_train)\n        \n        y_pred = clf.predict(X_test)\n        bal_acc = balanced_accuracy_score(y_test, y_pred)\n        prec = precision_score(y_test, y_pred, zero_division=0)\n        \n        # Coverage\n        n_cover = 0\n        for t in test:\n            emb = t[\"text_embeddings\"]\n            labels = np.array(t[\"step_labels\"])\n            n = min(emb.shape[0], len(labels))\n            X_t = build_window_features_single(emb[:n], w, TEXT_DIM)\n            probs = clf.predict_proba(X_t)[:, 1]\n            fc = first_crossing(probs.tolist())\n            if fc is not None:\n                n_cover += 1\n        coverage = n_cover / len(test)\n        \n        # Pre-CP FPR\n        fprs = []\n        for t in test:\n            cp = t[\"commitment_point\"]\n            if cp <= 0:\n                continue\n            emb = t[\"text_embeddings\"][:cp]\n            X_pre = build_window_features_single(emb, w, TEXT_DIM)\n            preds = clf.predict(X_pre)\n            fprs.append(float(np.mean(preds)))\n        pre_cp_fpr = float(np.mean(fprs))\n        \n        # Lead mean\n        leads = []\n        for t in test:\n            emb = t[\"text_embeddings\"]\n            labels = np.array(t[\"step_labels\"])\n            n = min(emb.shape[0], len(labels))\n            X_t = build_window_features_single(emb[:n], w, TEXT_DIM)\n            probs = clf.predict_proba(X_t)[:, 1]\n            cp = t[\"commitment_point\"]\n            fc = first_crossing(probs.tolist())\n            if fc is not None and fc < cp:\n                leads.append(cp - fc)\n        lead_mean = float(np.mean(leads)) if leads else 0.0\n        \n        results.append({\n            \"window\": w,\n            \"bal_acc\": float(bal_acc),\n            \"precision\": float(prec),\n            \"coverage\": float(coverage),\n            \"pre_cp_fpr\": float(pre_cp_fpr),\n            \"lead_mean\": float(lead_mean),\n        })\n        print(f\"  W={w:2d}: bal_acc={bal_acc:.4f} prec={prec:.4f} cov={coverage:.4f} fpr={pre_cp_fpr:.4f} lead={lead_mean:.1f}\")\n    \n    return results\n\n\n# ============ PHASE 5: PAIRED BOOTSTRAP ============\n\ndef phase5_bootstrap(train, test, best_layer, best_w):\n    print(\"\\n\" + \"=\"*60)\n    print(f\"PHASE 5: Paired Bootstrap (layer={best_layer}, W={best_w})\")\n    print(\"=\"*60)\n    \n    TEXT_DIM = 384\n    N_RESAMPLES = 1000\n    \n    # Train both probes\n    X_train_hs, y_train_hs = make_temporal_features(train, best_layer, best_w)\n    clf_hs = LogisticRegression(solver='liblinear', C=1.0, max_iter=1000,\n                                class_weight='balanced', random_state=SEED)\n    clf_hs.fit(X_train_hs, y_train_hs)\n    \n    X_train_text, y_train_text = make_text_temporal_features(train, best_w)\n    clf_text = LogisticRegression(solver='liblinear', C=1.0, max_iter=1000,\n                                  class_weight='balanced', random_state=SEED)\n    clf_text.fit(X_train_text, y_train_text)\n    \n    # Get per-trace metrics\n    hs_bal_accs, text_bal_accs = [], []\n    hs_precs, text_precs = [], []\n    hs_fprs, text_fprs = [], []\n    \n    for t in test:\n        cp = t[\"commitment_point\"]\n        hs = t[\"hidden_states\"][:, best_layer, :].float().numpy()\n        labels = np.array(t[\"step_labels\"])\n        n = min(hs.shape[0], len(labels))\n        \n        # HS predictions\n        X_hs = build_window_features_single(hs[:n], best_w, HIDDEN_DIM)\n        hs_pred = clf_hs.predict(X_hs)\n        hs_ba = balanced_accuracy_score(labels[:n], hs_pred)\n        hs_p = precision_score(labels[:n], hs_pred, zero_division=0)\n        hs_fpr_val = float(np.mean(hs_pred[:cp])) if cp > 0 else 0.0\n        \n        # Text predictions\n        emb = t[\"text_embeddings\"]\n        X_text = build_window_features_single(emb[:n], best_w, TEXT_DIM)\n        text_pred = clf_text.predict(X_text)\n        text_ba = balanced_accuracy_score(labels[:n], text_pred)\n        text_p = precision_score(labels[:n], text_pred, zero_division=0)\n        text_fpr_val = float(np.mean(text_pred[:cp])) if cp > 0 else 0.0\n        \n        hs_bal_accs.append(hs_ba)\n        text_bal_accs.append(text_ba)\n        hs_precs.append(hs_p)\n        text_precs.append(text_p)\n        hs_fprs.append(hs_fpr_val)\n        text_fprs.append(text_fpr_val)\n    \n    hs_bal_accs = np.array(hs_bal_accs)\n    text_bal_accs = np.array(text_bal_accs)\n    hs_precs = np.array(hs_precs)\n    text_precs = np.array(text_precs)\n    hs_fprs = np.array(hs_fprs)\n    text_fprs = np.array(text_fprs)\n    \n    def paired_bootstrap(metric_a, metric_b, n_resamples=N_RESAMPLES):\n        n = len(metric_a)\n        observed_diff = float(np.mean(metric_a) - np.mean(metric_b))\n        rng = np.random.default_rng(SEED)\n        diffs = []\n        for _ in range(n_resamples):\n            idx = rng.integers(0, n, size=n)\n            diffs.append(np.mean(metric_a[idx]) - np.mean(metric_b[idx]))\n        diffs = np.array(diffs)\n        # Two-sided p-value\n        p_value = float(np.mean(np.abs(diffs - np.mean(diffs)) >= np.abs(observed_diff)))\n        ci_lower = float(np.percentile(diffs, 2.5))\n        ci_upper = float(np.percentile(diffs, 97.5))\n        return observed_diff, ci_lower, ci_upper, p_value\n    \n    results = {}\n    for metric_name, hs_arr, text_arr in [\n        (\"bal_acc\", hs_bal_accs, text_bal_accs),\n        (\"precision\", hs_precs, text_precs),\n        (\"pre_cp_fpr\", hs_fprs, text_fprs),\n    ]:\n        diff, ci_lo, ci_hi, p = paired_bootstrap(hs_arr, text_arr)\n        bonferroni_sig = \"Yes\" if p < 0.017 else \"No\"\n        results[metric_name] = {\n            \"hs_mean\": float(np.mean(hs_arr)),\n            \"text_mean\": float(np.mean(text_arr)),\n            \"delta\": diff,\n            \"ci_95\": [ci_lo, ci_hi],\n            \"p_value\": p,\n            \"bonferroni_sig\": bonferroni_sig,\n        }\n        print(f\"  {metric_name}: HS={np.mean(hs_arr):.4f} Text={np.mean(text_arr):.4f} delta={diff:.4f} p={p:.4f} Bonf={bonferroni_sig}\")\n    \n    return results\n\n\n# ============ PHASE 6: SELECTIVITY CONTROL ============\n\ndef phase6_selectivity(train, test, best_layer, best_w):\n    print(\"\\n\" + \"=\"*60)\n    print(f\"PHASE 6: Selectivity Control (layer={best_layer}, W={best_w})\")\n    print(\"=\"*60)\n    \n    # Real accuracy\n    X_train, y_train = make_temporal_features(train, best_layer, best_w)\n    X_test, y_test = make_temporal_features(test, best_layer, best_w)\n    \n    clf = LogisticRegression(solver='liblinear', C=1.0, max_iter=1000,\n                             class_weight='balanced', random_state=SEED)\n    clf.fit(X_train, y_train)\n    real_acc = balanced_accuracy_score(y_test, clf.predict(X_test))\n    \n    # Random permutation control\n    n_perms = 10\n    random_accs = []\n    rng = np.random.default_rng(SEED)\n    for perm_i in range(n_perms):\n        y_train_perm = rng.permutation(y_train)\n        clf_rand = LogisticRegression(solver='liblinear', C=1.0, max_iter=1000,\n                                      class_weight='balanced', random_state=SEED+perm_i)\n        clf_rand.fit(X_train, y_train_perm)\n        rand_acc = balanced_accuracy_score(y_test, clf_rand.predict(X_test))\n        random_accs.append(rand_acc)\n    \n    random_mean = float(np.mean(random_accs))\n    random_std = float(np.std(random_accs))\n    selectivity = float(real_acc - random_mean) * 100  # in pp\n    \n    print(f\"  real_acc: {real_acc:.4f}\")\n    print(f\"  random_mean +/- std: {random_mean:.4f} +/- {random_std:.4f}\")\n    print(f\"  selectivity: {selectivity:.1f} pp\")\n    \n    return {\n        \"real_acc\": float(real_acc),\n        \"random_mean\": random_mean,\n        \"random_std\": random_std,\n        \"selectivity_pp\": selectivity,\n        \"n_perms\": n_perms,\n        \"random_accs\": random_accs,\n    }\n\n\n# ============ MAIN ============\n\ndef main():\n    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)\n    \n    print(\"=\"*60)\n    print(\"OpenThinker-7B Full Pipeline (exp_ot7b_full_pipeline)\")\n    print(\"=\"*60)\n    \n    # Step 1: Load data\n    print(\"\\nStep 1: Loading ot-7b traces...\")\n    traces = load_ot7b_traces()\n    print(f\"  Found {len(traces)} jailbreak traces with commitment points\")\n    lengths = [len(t[\"sentences\"]) for t in traces]\n    print(f\"  Mean trace length: {np.mean(lengths):.1f} sentences\")\n    \n    # Step 2: Extract hidden states\n    print(\"\\nStep 2: Extracting hidden states...\")\n    errors = phase1_extract(traces)\n    \n    # Verify extraction\n    print(\"\\nVerifying extraction...\")\n    extracted = list(HS_DIR.glob(\"*.pt\"))\n    print(f\"  Total .pt files: {len(extracted)}\")\n    \n    # Spot check 3 random files\n    import random\n    random.seed(42)\n    checks = random.sample(extracted, min(3, len(extracted)))\n    for f in checks:\n        d = torch.load(f, map_location=\"cpu\", weights_only=False)\n        print(f\"  {f.stem}: shape={list(d['hidden_states'].shape)} CP={d['commitment_point']} n_sent={d['num_sentences']}\")\n    \n    # Step 3: Load extracted traces for analysis\n    print(\"\\nStep 3: Loading extracted hidden states...\")\n    all_traces = load_extracted_traces()\n    print(f\"  Loaded {len(all_traces)} traces\")\n    \n    train, val, test = split_traces(all_traces)\n    print(f\"  Split: train={len(train)}, val={len(val)}, test={len(test)}\")\n    \n    # Step 4: Layer sweep\n    best_layer, layer_results = phase2_layer_sweep(train, val, test)\n    \n    # Step 5: Temporal probes\n    hs_probe_results, best_w = phase3_temporal_probes(train, val, test, best_layer)\n    \n    # Step 6: Text probes\n    text_probe_results = phase4_text_probes(train, val, test)\n    \n    # Step 7: Bootstrap\n    bootstrap_results = phase5_bootstrap(train, test, best_layer, best_w)\n    \n    # Step 8: Selectivity\n    selectivity_results = phase6_selectivity(train, test, best_layer, best_w)\n    \n    # ============ SAVE RESULTS ============\n    print(\"\\n\" + \"=\"*60)\n    print(\"Saving results...\")\n    \n    final_results = {\n        \"experiment_id\": \"exp_ot7b_full_pipeline\",\n        \"model\": \"OpenThinker-7B (open-thoughts/OpenThinker-7B)\",\n        \"base_model\": \"Qwen2.5-7B\",\n        \"num_layers\": NUM_LAYERS,\n        \"hidden_dim\": HIDDEN_DIM,\n        \"data\": {\n            \"total_traces\": len(all_traces),\n            \"train\": len(train),\n            \"val\": len(val),\n            \"test\": len(test),\n            \"mean_trace_length\": float(np.mean([t[\"num_sentences\"] for t in all_traces])),\n        },\n        \"best_layer\": {\n            \"layer_idx\": best_layer,\n            \"depth_pct\": float(best_layer / NUM_LAYERS * 100),\n        },\n        \"layer_sweep\": layer_results,\n        \"hs_temporal_probes\": hs_probe_results,\n        \"text_temporal_probes\": text_probe_results,\n        \"best_window\": best_w,\n        \"bootstrap\": bootstrap_results,\n        \"selectivity\": selectivity_results,\n        \"config\": {\n            \"safety_labels\": list(SAFETY_LABELS),\n            \"solver\": \"liblinear\",\n            \"seed\": SEED,\n            \"k_consecutive\": K_CONSECUTIVE,\n            \"threshold\": THRESHOLD,\n            \"bootstrap_resamples\": 1000,\n            \"bonferroni_threshold\": 0.017,\n        },\n    }\n    \n    with open(OUTPUT_DIR / \"results.json\", \"w\") as f:\n        json.dump(final_results, f, indent=2)\n    print(f\"  Saved: {OUTPUT_DIR / 'results.json'}\")\n    \n    # Generate report\n    best_layer_info = next(r for r in layer_results if r[\"layer_idx\"] == best_layer)\n    report = f\"\"\"# OpenThinker-7B Results\n\n## Data\n- Total traces: {len(all_traces)} (jailbreak+CP)\n- Train/Val/Test split: {len(train)}/{len(val)}/{len(test)}\n- Mean trace length: {np.mean([t['num_sentences'] for t in all_traces]):.1f} sentences\n\n## Best Layer\n- Layer: {best_layer} (depth: {best_layer/NUM_LAYERS*100:.0f}%)\n- bal_acc: {best_layer_info['bal_acc']:.4f}, crossing_rate: {best_layer_info['crossing_rate']:.4f}\n\n## Temporal Probes (HS, layer={best_layer})\n| W | bal_acc | precision | coverage | pre_cp_fpr | lead_mean |\n|---|---------|-----------|----------|------------|-----------|\n\"\"\"\n    for r in hs_probe_results:\n        report += f\"| {r['window']} | {r['bal_acc']:.4f} | {r['precision']:.4f} | {r['coverage']:.4f} | {r['pre_cp_fpr']:.4f} | {r['lead_mean']:.1f} |\\n\"\n    \n    report += f\"\"\"\n## Text Probes (all-MiniLM-L6-v2)\n| W | bal_acc | precision | coverage | pre_cp_fpr | lead_mean |\n|---|---------|-----------|----------|------------|-----------|\n\"\"\"\n    for r in text_probe_results:\n        report += f\"| {r['window']} | {r['bal_acc']:.4f} | {r['precision']:.4f} | {r['coverage']:.4f} | {r['pre_cp_fpr']:.4f} | {r['lead_mean']:.1f} |\\n\"\n    \n    report += f\"\"\"\n## HS vs Text Bootstrap (W={best_w})\n| Metric | HS | Text | Delta | p-value | Bonferroni |\n|--------|-----|------|-------|---------|------------|\n\"\"\"\n    for metric_name in [\"bal_acc\", \"precision\", \"pre_cp_fpr\"]:\n        b = bootstrap_results[metric_name]\n        report += f\"| {metric_name} | {b['hs_mean']:.4f} | {b['text_mean']:.4f} | {b['delta']:.4f} | {b['p_value']:.4f} | {b['bonferroni_sig']} |\\n\"\n    \n    report += f\"\"\"\n## Selectivity Control\n- real_acc: {selectivity_results['real_acc']:.4f}\n- random_mean +/- std: {selectivity_results['random_mean']:.4f} +/- {selectivity_results['random_std']:.4f}\n- selectivity: {selectivity_results['selectivity_pp']:.1f} pp\n\"\"\"\n    \n    with open(OUTPUT_DIR / \"report.md\", \"w\") as f:\n        f.write(report)\n    print(f\"  Saved: {OUTPUT_DIR / 'report.md'}\")\n    \n    print(\"\\n\" + \"=\"*60)\n    print(\"PIPELINE COMPLETE\")\n    print(\"=\"*60)\n    print(report)\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT\necho \"Script written successfully\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-17T06:20:38.722152+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written successfully\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-17T06:20:38.722310+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "cd /root/autodl-tmp/contrastive_trace_safety && CUDA_VISIBLE_DEVICES=0 HF_ENDPOINT=https://hf-mirror.com /root/miniconda3/bin/python3.12 src/experiments/exp_ot7b_full_pipeline.py 2>&1 | head -80",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "cd /root/autodl-tmp/contrastive_trace_safety && CUDA_VISIBLE_DEVICES=0 HF_ENDPOINT=https://hf-mirror.com /root/miniconda3/bin/python3.12 src/experiments/exp_ot7b_full_pipeline.py 2>&1 | head -80",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-17T06:20:38.722721+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'cd /root/autodl-tmp/contrastive_trace_safety && CUDA_VISIBLE_DEVICES=0 HF_ENDPOINT=https://hf-mirror.com /root/miniconda3/bin/python3.12 src/experiments/exp_ot7b_full_pipeline.py 2>&1 | head -80'\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-17T06:20:38.722884+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "cd /root/autodl-tmp/contrastive_trace_safety && nohup /root/miniconda3/bin/python3.12 -u src/experiments/exp_ot7b_full_pipeline.py > artifacts/exp_ot7b_full_pipeline.log 2>&1 &\necho \"PID: $!\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "cd /root/autodl-tmp/contrastive_trace_safety && nohup /root/miniconda3/bin/python3.12 -u src/experiments/exp_ot7b_full_pipeline.py > artifacts/exp_ot7b_full_pipeline.log 2>&1 &\necho \"PID: $!\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-17T06:20:38.723026+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'cd /root/autodl-tmp/contrastive_trace_safety && nohup /root/miniconda3/bin/python3.12 -u src/experiments/exp_ot7b_full_pipeline.py > artifacts/exp_ot7b_full_pipeline.log 2>&1 &\\\\necho \\\"PID: $!\\\"'\\n\\nStdout:\\n\\nPID: 60094\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.94}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-17T06:20:38.723180+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "tail -30 /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_ot7b_full_pipeline.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "tail -30 /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_ot7b_full_pipeline.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-17T06:20:38.723312+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"============================================================\\nOpenThinker-7B Full Pipeline (exp_ot7b_full_pipeline)\\n============================================================\\n\\nStep 1: Loading ot-7b traces...\\n  Found 228 jailbreak traces with commitment points\\n  Mean trace length: 80.1 sentences\\n\\nStep 2: Extracting hidden states...\\nAlready extracted: 0, remaining: 228\\nLoading OpenThinker-7B model...\\n`torch_dtype` is deprecated! Use `dtype` instead!\\n\\rFetching 4 files:   0%|          | 0/4 [00:00<?, ?it/s]\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.89}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-17T06:20:38.723469+00:00_

called ScheduleWakeup

<details open><summary>🔧 Tool call — ScheduleWakeup</summary>

````json
{
  "delaySeconds": "180",
  "reason": "Waiting for OT-7B model download to complete before extraction starts",
  "prompt": "## 任务：OpenThinker-7B 全量 Pipeline 执行（Path A 核心实验）\n\n### 目标\n在 autodl-rtx6000 cuda:0 上执行 OpenThinker-7B (open-thoughts/OpenThinker-7B, Qwen2.5-7B, 28 layers, hidden_dim=3584) 的完整 commitment detection pipeline。端到端约 30-50 分钟。\n\n### 实验 ID: `exp_ot7b_full_pipeline`\n\n---\n\n### Pipeline 步骤\n\n#### Step 0: 环境确认\n- Python: `/root/miniconda3/bin/python3.12`\n- GPU: cuda:0\n- 项目路径: `/root/autodl-tmp/contrastive_trace_safety/`\n- 设置 `export HF_ENDPOINT=https://hf-mirror.com`\n- 设置 `export CUDA_VISIBLE_DEVICES=0`\n\n#### Step 1: 加载数据 + 定义 Commitment Point\n```python\nfrom datasets import load_dataset\nimport os\nos.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'\n\nds = load_dataset(\"ishitakakkar-10/HarmThoughts\")\n# 筛选 ot-7b 的 jailbreak traces\not7b = ds['train'].filter(lambda x: x['model_name'] == 'ot-7b' and x['final_judgment'] == 1.0)\n```\n\n**CP 定义（硬规则）**: CP = 最后一个 safety label 出现的 step + 1。\n- 先看现有代码的 safety label 定义（检查 `src/data_loader.py` 或相关文件中的 SAFETY_LABELS）\n- 如果找不到，使用: SAFETY_LABELS = {'RA', 'AL', 'CC', 'ED', 'IA', 'CR', 'PS', 'RS', 'IR'}（所有非有害/非中性的标签）\n- **不要用 \"首个 DKE\" 作为 CP**，必须用 \"最后 safety label + 1\"\n\n#### Step 2: 下载模型\n```python\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\nmodel_name = \"open-thoughts/OpenThinker-7B\"  # 确认 HuggingFace 上的准确 repo name\n# 如果找不到，尝试 \"mithrilai/OpenThinker-7B\" 或 WebSearch 确认\ntokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)\nmodel = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16, device_map=\"cuda:0\", trust_remote_code=True)\n```\n\n#### Step 3: Hidden State 提取\n参考现有脚本 `src/experiments/exp_001a_extract_r1_32b.py` 的逻辑：\n- 对每条 trace 的每个 sentence：tokenize，forward pass，提取所有 28 层的 last-token hidden state\n- 保存格式与现有一致: `hidden_states` tensor [num_sentences, 28, 3584]\n- 输出目录: `artifacts/hidden_states_ot7b/`\n- 每条 trace 一个 .pt 文件，包含: hidden_states, trace_id, num_sentences, commitment_point, step_labels, query\n\n#### Step 4: Layer Sweep\n- 对所有 28 层，用 LogisticRegression(solver='liblinear', class_weight='balanced') 做 static probe\n- Split: 60/20/20 (train/val/test)，seed=42\n- 选层指标: balanced_accuracy × crossing_rate（与其他模型一致）\n- 报告: 每层的 bal_acc, crossing_rate, lead_mean, pre_cp_fpr\n\n#### Step 5: 主 Probe Pipeline（在最优层上）\n- **Temporal LR probes**: W=1,3,5,10,15,20,25，solver='liblinear', class_weight='balanced'\n- **Text probes**: 用 all-MiniLM-L6-v2 对同样的 sentences 做 embedding，然后相同 W 做 LR probe\n- 指标: bal_acc, precision, coverage, pre_cp_fpr (trace-level + step-level), lead_mean\n- **Selectivity control task**: \n  - 10 次 random label permutation，计算 random_acc mean ± std\n  - selectivity = real_acc - random_mean (要求 >5pp)\n\n#### Step 6: Paired Bootstrap\n- 1000 resamples, two-sided permutation test\n- 在最佳 W 下对比 HS vs Text: balanced_accuracy, precision, pre_cp_fpr\n- solver='liblinear'\n- 报告 p-values + 95% CI for each metric delta\n- Bonferroni threshold: 0.017 (3 comparisons)\n\n#### Step 7: 保存结果\n- 所有结果保存到 `artifacts/exp_ot7b_full_pipeline/results.json`\n- 格式与 exp_001a/exp_001b 一致\n- 同时保存 per-W metrics table\n\n---\n\n### 输出格式（最终报告）\n\n```\n# OpenThinker-7B Results\n\n## Data\n- Total traces: X (jailbreak+CP)\n- Train/Val/Test split: X/X/X\n- Mean trace length: X sentences\n\n## Best Layer\n- Layer: X (depth: X%)\n- bal_acc: X, crossing_rate: X\n\n## Temporal Probes (best W)\n| W | bal_acc | precision | coverage | pre_cp_fpr | lead_mean |\n|---|---------|-----------|----------|------------|-----------|\n...\n\n## HS vs Text Bootstrap (W=best)\n| Metric | HS | Text | Delta | p-value | Bonferroni |\n|--------|-----|------|-------|---------|------------|\n| bal_acc | ... | ... | ... | ... | ... |\n| precision | ... | ... | ... | ... | ... |\n| pre_cp_fpr | ... | ... | ... | ... | ... |\n\n## Selectivity Control\n- real_acc: X\n- random_mean ± std: X ± X\n- selectivity: X pp\n```\n\n写完整结果到 `artifacts/exp_ot7b_full_pipeline/results.json` 和 `artifacts/exp_ot7b_full_pipeline/report.md`。\n\n然后用 `update_registry` 更新 exp_ot7b_full_pipeline 状态和 metrics。\n\n---\n\n### 重要注意事项\n1. **CP 用 \"last safety label + 1\"**，不是 \"first DKE\"。先看现有代码确认 SAFETY_LABELS 定义\n2. **solver 必须是 'liblinear'**（项目统一标准）\n3. **bootstrap 必须 two-sided**\n4. 如果模型 HF repo 名有误，WebSearch 确认正确的 repo\n5. 参考现有代码结构：`src/experiments/exp_001a_extract_r1_32b.py`, `src/data_loader.py`\n6. hidden_states 提取时注意 OT-7B 的 traces 更长（avg 80 sentences），可能需要 batch 处理避免 OOM\n7. 提取完成后立即验证: 随机抽 3 个 .pt 文件检查 shape 和 CP 位置合理性\n\n### 环境\n- 服务器: autodl-rtx6000\n- Python: /root/miniconda3/bin/python3.12\n- GPU: cuda:0 (CUDA_VISIBLE_DEVICES=0)\n- HF_ENDPOINT=https://hf-mirror.com\n- 项目路径: /root/autodl-tmp/contrastive_trace_safety/\n- sklearn solver: liblinear\n- torch dtype: bfloat16"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417",
  "tool": "ScheduleWakeup",
  "tool_args": {
    "delaySeconds": "180",
    "reason": "Waiting for OT-7B model download to complete before extraction starts",
    "prompt": "## 任务：OpenThinker-7B 全量 Pipeline 执行（Path A 核心实验）\n\n### 目标\n在 autodl-rtx6000 cuda:0 上执行 OpenThinker-7B (open-thoughts/OpenThinker-7B, Qwen2.5-7B, 28 layers, hidden_dim=3584) 的完整 commitment detection pipeline。端到端约 30-50 分钟。\n\n### 实验 ID: `exp_ot7b_full_pipeline`\n\n---\n\n### Pipeline 步骤\n\n#### Step 0: 环境确认\n- Python: `/root/miniconda3/bin/python3.12`\n- GPU: cuda:0\n- 项目路径: `/root/autodl-tmp/contrastive_trace_safety/`\n- 设置 `export HF_ENDPOINT=https://hf-mirror.com`\n- 设置 `export CUDA_VISIBLE_DEVICES=0`\n\n#### Step 1: 加载数据 + 定义 Commitment Point\n```python\nfrom datasets import load_dataset\nimport os\nos.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'\n\nds = load_dataset(\"ishitakakkar-10/HarmThoughts\")\n# 筛选 ot-7b 的 jailbreak traces\not7b = ds['train'].filter(lambda x: x['model_name'] == 'ot-7b' and x['final_judgment'] == 1.0)\n```\n\n**CP 定义（硬规则）**: CP = 最后一个 safety label 出现的 step + 1。\n- 先看现有代码的 safety label 定义（检查 `src/data_loader.py` 或相关文件中的 SAFETY_LABELS）\n- 如果找不到，使用: SAFETY_LABELS = {'RA', 'AL', 'CC', 'ED', 'IA', 'CR', 'PS', 'RS', 'IR'}（所有非有害/非中性的标签）\n- **不要用 \"首个 DKE\" 作为 CP**，必须用 \"最后 safety label + 1\"\n\n#### Step 2: 下载模型\n```python\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\nmodel_name = \"open-thoughts/OpenThinker-7B\"  # 确认 HuggingFace 上的准确 repo name\n# 如果找不到，尝试 \"mithrilai/OpenThinker-7B\" 或 WebSearch 确认\ntokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)\nmodel = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16, device_map=\"cuda:0\", trust_remote_code=True)\n```\n\n#### Step 3: Hidden State 提取\n参考现有脚本 `src/experiments/exp_001a_extract_r1_32b.py` 的逻辑：\n- 对每条 trace 的每个 sentence：tokenize，forward pass，提取所有 28 层的 last-token hidden state\n- 保存格式与现有一致: `hidden_states` tensor [num_sentences, 28, 3584]\n- 输出目录: `artifacts/hidden_states_ot7b/`\n- 每条 trace 一个 .pt 文件，包含: hidden_states, trace_id, num_sentences, commitment_point, step_labels, query\n\n#### Step 4: Layer Sweep\n- 对所有 28 层，用 LogisticRegression(solver='liblinear', class_weight='balanced') 做 static probe\n- Split: 60/20/20 (train/val/test)，seed=42\n- 选层指标: balanced_accuracy × crossing_rate（与其他模型一致）\n- 报告: 每层的 bal_acc, crossing_rate, lead_mean, pre_cp_fpr\n\n#### Step 5: 主 Probe Pipeline（在最优层上）\n- **Temporal LR probes**: W=1,3,5,10,15,20,25，solver='liblinear', class_weight='balanced'\n- **Text probes**: 用 all-MiniLM-L6-v2 对同样的 sentences 做 embedding，然后相同 W 做 LR probe\n- 指标: bal_acc, precision, coverage, pre_cp_fpr (trace-level + step-level), lead_mean\n- **Selectivity control task**: \n  - 10 次 random label permutation，计算 random_acc mean ± std\n  - selectivity = real_acc - random_mean (要求 >5pp)\n\n#### Step 6: Paired Bootstrap\n- 1000 resamples, two-sided permutation test\n- 在最佳 W 下对比 HS vs Text: balanced_accuracy, precision, pre_cp_fpr\n- solver='liblinear'\n- 报告 p-values + 95% CI for each metric delta\n- Bonferroni threshold: 0.017 (3 comparisons)\n\n#### Step 7: 保存结果\n- 所有结果保存到 `artifacts/exp_ot7b_full_pipeline/results.json`\n- 格式与 exp_001a/exp_001b 一致\n- 同时保存 per-W metrics table\n\n---\n\n### 输出格式（最终报告）\n\n```\n# OpenThinker-7B Results\n\n## Data\n- Total traces: X (jailbreak+CP)\n- Train/Val/Test split: X/X/X\n- Mean trace length: X sentences\n\n## Best Layer\n- Layer: X (depth: X%)\n- bal_acc: X, crossing_rate: X\n\n## Temporal Probes (best W)\n| W | bal_acc | precision | coverage | pre_cp_fpr | lead_mean |\n|---|---------|-----------|----------|------------|-----------|\n...\n\n## HS vs Text Bootstrap (W=best)\n| Metric | HS | Text | Delta | p-value | Bonferroni |\n|--------|-----|------|-------|---------|------------|\n| bal_acc | ... | ... | ... | ... | ... |\n| precision | ... | ... | ... | ... | ... |\n| pre_cp_fpr | ... | ... | ... | ... | ... |\n\n## Selectivity Control\n- real_acc: X\n- random_mean ± std: X ± X\n- selectivity: X pp\n```\n\n写完整结果到 `artifacts/exp_ot7b_full_pipeline/results.json` 和 `artifacts/exp_ot7b_full_pipeline/report.md`。\n\n然后用 `update_registry` 更新 exp_ot7b_full_pipeline 状态和 metrics。\n\n---\n\n### 重要注意事项\n1. **CP 用 \"last safety label + 1\"**，不是 \"first DKE\"。先看现有代码确认 SAFETY_LABELS 定义\n2. **solver 必须是 'liblinear'**（项目统一标准）\n3. **bootstrap 必须 two-sided**\n4. 如果模型 HF repo 名有误，WebSearch 确认正确的 repo\n5. 参考现有代码结构：`src/experiments/exp_001a_extract_r1_32b.py`, `src/data_loader.py`\n6. hidden_states 提取时注意 OT-7B 的 traces 更长（avg 80 sentences），可能需要 batch 处理避免 OOM\n7. 提取完成后立即验证: 随机抽 3 个 .pt 文件检查 shape 和 CP 位置合理性\n\n### 环境\n- 服务器: autodl-rtx6000\n- Python: /root/miniconda3/bin/python3.12\n- GPU: cuda:0 (CUDA_VISIBLE_DEVICES=0)\n- HF_ENDPOINT=https://hf-mirror.com\n- 项目路径: /root/autodl-tmp/contrastive_trace_safety/\n- sklearn solver: liblinear\n- torch dtype: bfloat16"
  }
}
````

</details>

---

### Tool result

_source line 42 · 2026-05-17T06:20:38.723788+00:00_

Next wakeup scheduled for 06:24:00 (in 205s).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417",
  "tool": "ScheduleWakeup",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-17T06:20:38.724187+00:00_

Pipeline is running in the background (PID 60094). Model download is in progress. Will check back in 3 minutes to monitor extraction progress.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_exp_ot7b_full_pipeline_20260517T061417"
}
```

</details>

---
