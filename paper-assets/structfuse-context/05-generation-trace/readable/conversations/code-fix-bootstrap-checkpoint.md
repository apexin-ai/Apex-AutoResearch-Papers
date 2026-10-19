# code fix bootstrap checkpoint

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 75
- **Recorded user turns:** 0
- **Tool calls:** 37
- **Original source:** `logs/chats/worker_code_fix_bootstrap_checkpoint_20260515T150138.jsonl`
- **Structured JSON:** [`db88da4f0ee3de6e21f6.json`](../../sessions/db/db88da4f0ee3de6e21f6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

75 recorded events

### Tool call

_source line 1 · 2026-05-15T15:07:41.156878+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T15:07:41.157221+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T15:07:41.157391+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/structfuse -name \"bootstrap_paired_test.py\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "find /root/structfuse -name \"bootstrap_paired_test.py\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T15:07:41.157524+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/structfuse -name \"train_contrastive.py\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "find /root/structfuse -name \"train_contrastive.py\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-15T15:07:41.157694+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.08}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T15:07:41.157832+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T15:07:41.157981+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/structfuse -type f -name \"*.py\" ",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "find /root/structfuse -type f -name \"*.py\" ",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T15:07:41.158105+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.65}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T15:07:41.158232+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls -la /root/structfuse/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "ls -la /root/structfuse/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T15:07:41.158421+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 188\\ndrwxr-xr-x 11 root root  4096 May 15 22:24 .\\ndrwx------  1 root root  4096 May 14 05:06 ..\\ndrwxr-xr-x  2 root root   192 May 14 23:09 analysis\\ndrwxr-xr-x  5 root root   112 May 14 18:33 artifacts\\n-rwxr-xr-x  1 root root  1246 May 14 07:58 auto_start_dataflow.sh\\ndrwxr-xr-x  2 root root    48 May 14 08:56 configs\\n-rw-r--r--  1 root root  7963 May 15 03:38 eval_checkpoint.py\\ndrwxr-xr-x  3 root root  4096 May 15 10:17 evaluation\\ndrwxr-xr-x  4 root root   182 May 14 07:58 extraction\\n-rwxr-xr-x  1 root root 20089 May 14 07:58 mvp_phase1.py\\n-rwxr-xr-x  1 root root 17489 May 12 19:39 mvp_phase1.py.bak\\n-rw-r--r--  1 root root   611 May 12 18:23 requirements.txt\\ndrwxr-xr-x  3 root root  4096 May 15 22:10 results\\n-rwxr-xr-x  1 root root  1730 May 15 02:05 run_m2_bm25_qwen_s42.sh\\n-rwxr-xr-x  1 root root  2524 May 14 07:58 run_m2_early_pilot.sh\\n-rwxr-xr-x  1 root root  2484 May 14 07:58 run_m2_embed_verify.sh\\n-rwxr-xr-x  1 root root  3309 May 14 07:58 run_m2_embed_verify_continuation.sh\\n-rw-r--r--  1 root root  5679 May 15 21:06 run_m2_full_qwen.sh\\n-rw-r--r--  1 root root  5624 May 15 21:06 run_m2_full_qwen.sh.bak\\n-rwxr-xr-x  1 root root  7504 May 14 19:17 run_m2_full_starcoder.sh\\n-rwxr-xr-x  1 root root  4055 May 15 22:23 run_m2_full_starcoder_resume.sh\\n-rwxr-xr-x  1 root root  4016 May 15 21:06 run_m2_full_starcoder_resume.sh.bak\\n-rwxr-xr-x  1 root root  4016 May 15 22:23 run_m2_full_starcoder_resume.sh.bak.d050\\n-rwxr-xr-x  1 root root  3093 May 14 19:20 run_m2_full_starcoder_s43plus.sh\\n-rwxr-xr-x  1 root root  7169 May 15 22:24 run_m2_s42_supplement.sh\\n-rwxr-xr-x  1 root root  7151 May 15 22:23 run_m2_s42_supplement.sh.bak.d050\\n-rwxr-xr-x  1 root root  1438 May 13 17:09 run_plan013_dataflow_retry.sh\\n-rw-r--r--  1 root root  2463 May 14 07:58 run_plan013_starcoder.sh\\n-rwxr-xr-x  1 root root  3826 May 14 09:04 run_plan014_temp_ablation.sh\\n-rwxr-xr-x  1 r
…[truncated 750 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T15:07:41.158589+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls -la /root/structfuse/scripts/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "ls -la /root/structfuse/scripts/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T15:07:41.158780+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 388\\ndrwxr-xr-x  3 root root  4096 May 15 22:47 .\\ndrwxr-xr-x 11 root root  4096 May 15 22:24 ..\\ndrwxr-xr-x  2 root root   101 May 14 08:47 __pycache__\\n-rw-r--r--  1 root root  5446 May 15 01:06 analyze_bm25_overlap_stratified.py\\n-rw-r--r--  1 root root 21027 May 15 04:36 analyze_confound.py\\n-rw-r--r--  1 root root 34339 May 15 22:09 analyze_m2_stats.py\\n-rw-r--r--  1 root root 17382 May 15 13:08 analyze_stratified.py\\n-rw-r--r--  1 root root  9957 May 15 22:47 bootstrap_paired_test.py\\n-rwxr-xr-x  1 root root  3453 May 13 19:47 build_full_m2_data.sh\\n-rw-r--r--  1 root root 21053 May 14 00:39 build_m1_training_data.py\\n-rw-r--r--  1 root root 17398 May 13 12:18 build_m1_training_data.py.bak\\n-rw-r--r--  1 root root  8304 May 14 07:58 build_p2b_data.py\\n-rwxr-xr-x  1 root root  1708 May 13 19:45 clone_repos.sh\\n-rw-r--r--  1 root root  2607 May 12 20:35 collect_p2b_results.py\\n-rw-r--r--  1 root root  5829 May 14 07:58 compute_full_z_percent.py\\n-rw-r--r--  1 root root  2540 May 13 04:02 download_metadata.py\\n-rw-r--r--  1 root root  4049 May 14 07:58 eval_p2b.py\\n-rw-r--r--  1 root root  5689 May 14 07:58 eval_p2b_pooled.py\\n-rw-r--r--  1 root root 20137 May 15 03:38 eval_swebench_e2e.py\\n-rw-r--r--  1 root root  9448 May 15 13:04 evaluate_stratified.py\\n-rw-r--r--  1 root root  2528 May 13 04:05 fix_metadata.py\\n-rw-r--r--  1 root root  3395 May 13 04:07 fix_metadata_arrow.py\\n-rw-r--r--  1 root root 19067 May 15 09:19 m2_statistical_analysis.py\\n-rwxr-xr-x  1 root root  1884 May 13 18:53 migrate_m1_data.sh\\n-rw-r--r--  1 root root 10467 May 15 01:07 mine_bm25_negatives.py\\n-rw-r--r--  1 root root  7014 May 15 01:07 plot_neg_difficulty.py\\n-rw-r--r--  1 root root 16107 May 15 10:03 plot_per_seed_delta.py\\n-rw-r--r--  1 root root  3906 May 14 03:32 prepare_m1_rerun.py\\n-rw-r--r--  1 root root  4950 May 15 13:04 prepare_stratification_index.py\\n-rwxr-xr-x  1 root root  41
…[truncated 926 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T15:07:41.158924+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls -la /root/structfuse/evaluation/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "ls -la /root/structfuse/evaluation/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T15:07:41.159049+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls -la /root/structfuse/training/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "ls -la /root/structfuse/training/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T15:07:41.159179+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 276\\ndrwxr-xr-x  3 root root  4096 May 15 10:17 .\\ndrwxr-xr-x 11 root root  4096 May 15 22:24 ..\\ndrwxr-xr-x  2 root root   140 May 15 10:18 __pycache__\\n-rw-r--r--  1 root root 55321 May 15 05:05 analyze_stratified.py\\n-rw-r--r--  1 root root 52505 May 15 05:00 analyze_stratified.py.bak\\n-rw-r--r--  1 root root 36698 May 15 04:49 analyze_stratified.py.bak_v2\\n-rw-r--r--  1 root root 17655 May 15 03:38 eval_repobench.py\\n-rw-r--r--  1 root root 17159 May 15 03:38 eval_retrieval.py\\n-rw-r--r--  1 root root 20654 May 15 03:38 eval_swebench.py\\n-rw-r--r--  1 root root 18098 May 14 02:54 eval_swebench.py.bak\\n-rw-r--r--  1 root root  9591 May 15 10:17 evaluate_pool50.py\\n-rw-r--r--  1 root root 14097 May 14 07:58 linear_proxy.py\\n-rw-r--r--  1 root root  3073 May 12 19:39 linear_proxy_results.json\\n-rw-r--r--  1 root root  6468 May 14 23:31 plot_neg_difficulty.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T15:07:41.159308+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 68\\ndrwxr-xr-x  3 root root   144 May 15 01:55 .\\ndrwxr-xr-x 11 root root  4096 May 15 22:24 ..\\ndrwxr-xr-x  2 root root   136 May 15 01:56 __pycache__\\n-rw-r--r--  1 root root  7195 May 14 08:56 contrastive_model.py\\n-rw-r--r--  1 root root  7871 May 15 01:55 hard_negative_mining.py\\n-rw-r--r--  1 root root 25494 May 15 03:38 train.py\\n-rw-r--r--  1 root root 19060 May 13 08:38 train.py.bak\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T15:07:41.159452+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cat /root/structfuse/scripts/bootstrap_paired_test.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "cat /root/structfuse/scripts/bootstrap_paired_test.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T15:07:41.159569+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cat /root/structfuse/training/train.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "cat /root/structfuse/training/train.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T15:07:41.159856+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nInstance-level cluster bootstrap: embedding_distance vs random mining (s43).\\nEvaluates both checkpoints on val_random_s43.jsonl (common eval set),\\ncomputes per-instance R@1, and runs cluster bootstrap clustered by repo.\\n\\\"\\\"\\\"\\n\\nimport json\\nimport os\\nimport sys\\nimport time\\nimport numpy as np\\nimport torch\\nimport torch.nn.functional as F\\nfrom pathlib import Path\\nfrom collections import defaultdict\\n\\nsys.path.insert(0, \\\"/root/structfuse/training\\\")\\nfrom contrastive_model import StructFuseEncoder\\nfrom transformers import AutoTokenizer\\n\\nRANDOM_CKPT = \\\"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1\\\"\\nEMBED_CKPT = \\\"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s43/best_by_recall_at_1\\\"\\nBASE_MODEL = \\\"/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B\\\"\\nVAL_FILE = \\\"/root/autodl-tmp/structfuse/full_m2_training_data/val_random_s43.jsonl\\\"\\nDEVICE = \\\"cuda:0\\\"\\nMAX_SEQ_LEN = 2048\\nNUM_NEGATIVES = 7\\nENCODE_BATCH = 8\\nN_BOOTSTRAP = 10000\\nOUTPUT_PATH = \\\"/root/structfuse/results/bootstrap_s43_paired.json\\\"\\n\\n\\ndef load_model(ckpt_dir, base_model, device):\\n    config_path = Path(ckpt_dir) / \\\"training_config.json\\\"\\n    with open(config_path) as f:\\n        cfg = json.load(f)\\n    model = StructFuseEncoder(\\n        model_name=base_model,\\n        proj_dim=cfg.get(\\\"proj_dim\\\", 256),\\n        use_lora=cfg.get(\\\"use_lora\\\", True),\\n        lora_r=cfg.get(\\\"lora_r\\\", 16),\\n        use_fusion_head=cfg.get(\\\"use_fusion_head\\\", False),\\n    )\\n    state_dict = torch.load(Path(ckpt_dir) / \\\"model.pt\\\", map_location=\\\"cpu\\\")\\n    result = model.load_state_dict(state_dict, strict=False)\\n    if result.unexpected_keys:\\n        print(f\\\"WARNING: unexpected keys: {result.unexpected_keys[:5]}\\\")\\n    if result.missin
…[truncated 7210 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T15:07:41.160141+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"from __future__ import annotations\\n\\nimport os\\n\\n\\\"\\\"\\\"StructFuse contrastive training entry point.\\n\\nTrains a bi-encoder (Qwen2.5-Coder-3B) with InfoNCE loss, data-flow-weighted\\npositives, and configurable hard-negative mining.  Supports single/multi-GPU\\nvia HuggingFace Accelerate, LoRA, gradient checkpointing, and W&B logging.\\n\\\"\\\"\\\"\\n\\n\\nimport argparse\\nimport sys\\nimport json\\nimport math\\nimport os\\nimport random\\nimport shutil\\nfrom pathlib import Path\\nfrom typing import Any, Dict, List\\n\\nimport numpy as np\\nimport torch\\nfrom torch.utils.data import DataLoader, Dataset\\nfrom transformers import AutoTokenizer, get_cosine_schedule_with_warmup\\n\\nfrom accelerate import Accelerator\\nfrom accelerate.utils import set_seed\\n\\nfrom contrastive_model import StructFuseEncoder\\nfrom hard_negative_mining import build_miner, mine_batch\\n\\n\\n\\ndef _print_flush(*args, **kwargs):\\n    \\\"\\\"\\\"Print with explicit flush for file-redirect compatibility.\\\"\\\"\\\"\\n    kwargs['flush'] = True\\n    print(*args, **kwargs)\\n\\n# ── Dataset ──���───────────────────────────────────────────────────────\\n\\nclass ContrastiveDataset(Dataset):\\n    \\\"\\\"\\\"\\n    Each sample: {query, positive, negatives[], pos_weight, features[]}.\\n\\n    The raw data file is JSONL with fields:\\n        query_id, query_tokens, pos_id, pos_tokens, pos_dataflow_distance,\\n        neg_candidates (list of file ids), features (dict per candidate).\\n\\n    Negatives are mined dynamically per epoch via `refresh_negatives()`.\\n    \\\"\\\"\\\"\\n\\n    def __init__(\\n        self,\\n        data_path: str,\\n        tokenizer: AutoTokenizer,\\n        max_seq_length: int,\\n        num_negatives: int,\\n        pos_weight_alpha: float,\\n        use_fusion_head: bool,\\n    ):\\n        self.tokenizer = tokenizer\\n        self.max_seq_length = max_seq_length\\n        self.num_neg
…[truncated 7076 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T15:07:41.160343+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cat /root/structfuse/training/contrastive_model.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "cat /root/structfuse/training/contrastive_model.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T15:07:41.160679+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"StructFuse contrastive bi-encoder with fusion head.\\n\\nBi-encoder over Qwen2.5-Coder-3B with InfoNCE loss, weighted positives\\n(data-flow path distance), and an optional lightweight fusion head that\\ncombines embedding similarity with explicit structural features.\\n\\\"\\\"\\\"\\n\\nimport math\\nimport torch\\nimport torch.nn as nn\\nimport torch.nn.functional as F\\nfrom transformers import AutoModel, AutoConfig\\n\\n\\nclass FusionHead(nn.Module):\\n    \\\"\\\"\\\"MLP that fuses embedding similarity with explicit features into a relevance score.\\\"\\\"\\\"\\n\\n    FEATURE_NAMES = [\\n        \\\"dataflow_distance\\\",\\n        \\\"bm25_score\\\",\\n        \\\"co_change_freq\\\",\\n        \\\"inter_procedural_flag\\\",\\n        \\\"path_count\\\",\\n    ]\\n    NUM_EXPLICIT = len(FEATURE_NAMES)\\n\\n    def __init__(self, hidden_dim: int = 128):\\n        super().__init__()\\n        input_dim = 1 + self.NUM_EXPLICIT  # embed_similarity + explicit features\\n        self.net = nn.Sequential(\\n            nn.Linear(input_dim, hidden_dim),\\n            nn.GELU(),\\n            nn.Linear(hidden_dim, hidden_dim),\\n            nn.GELU(),\\n            nn.Linear(hidden_dim, 1),\\n        )\\n\\n    def forward(self, embed_similarity: torch.Tensor, features: torch.Tensor) -> torch.Tensor:\\n        \\\"\\\"\\\"\\n        Args:\\n            embed_similarity: (B,) or (B, K) cosine similarities.\\n            features: same leading dims + NUM_EXPLICIT trailing dim.\\n        Returns:\\n            scores with same shape as embed_similarity.\\n        \\\"\\\"\\\"\\n        orig_shape = embed_similarity.shape\\n        sim = embed_similarity.unsqueeze(-1)  # (..., 1)\\n        x = torch.cat([sim, features], dim=-1)  # (..., 1+NUM_EXPLICIT)\\n        x = x.view(-1, x.size(-1))\\n        out = self.net(x).squeeze(-1)\\n        return out.view(orig_shape)\\n\\n\\nclass StructFuseEncoder(nn.Modul
…[truncated 5901 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T15:07:41.160873+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls -la /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s43/best_by_recall_at_1/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "ls -la /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s43/best_by_recall_at_1/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T15:07:41.161014+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 48420\\ndrwxr-xr-x 2 root root     4096 May 15 14:28 .\\ndrwxr-xr-x 5 root root       86 May 15 14:50 ..\\n-rw-r--r-- 1 root root      605 May 15 14:28 added_tokens.json\\n-rw-r--r-- 1 root root     2427 May 15 14:28 chat_template.jinja\\n-rw-r--r-- 1 root root  1671853 May 15 14:28 merges.txt\\n-rw-r--r-- 1 root root 33674015 May 15 14:28 model.pt\\n-rw-r--r-- 1 root root      616 May 15 14:28 special_tokens_map.json\\n-rw-r--r-- 1 root root 11421896 May 15 14:28 tokenizer.json\\n-rw-r--r-- 1 root root     4688 May 15 14:28 tokenizer_config.json\\n-rw-r--r-- 1 root root     1051 May 15 14:28 training_config.json\\n-rw-r--r-- 1 root root  2776833 May 15 14:28 vocab.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T15:07:41.161149+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/autodl-tmp/structfuse/checkpoints/ -name \"adapter_config.json\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "find /root/autodl-tmp/structfuse/checkpoints/ -name \"adapter_config.json\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T15:07:41.161271+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.64}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T15:07:41.161426+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cat /root/structfuse/eval_checkpoint.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "cat /root/structfuse/eval_checkpoint.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T15:07:41.161664+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Eval a saved StructFuse checkpoint on the val set (val_loss + recall@1/5/10).\\\"\\\"\\\"\\nimport json, math, random, sys, os\\nfrom pathlib import Path\\nfrom typing import Any, Dict, List\\n\\nimport torch\\nimport torch.nn.functional as F\\nfrom torch.utils.data import DataLoader, Dataset\\nfrom transformers import AutoTokenizer\\n\\nsys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), \\\"training\\\"))\\nfrom contrastive_model import StructFuseEncoder\\n\\n\\nclass ContrastiveDataset(Dataset):\\n    def __init__(self, data_path, tokenizer, max_seq_length, num_negatives, pos_weight_alpha, use_fusion_head):\\n        self.tokenizer = tokenizer\\n        self.max_seq_length = max_seq_length\\n        self.num_negatives = num_negatives\\n        self.alpha = pos_weight_alpha\\n        self.use_fusion_head = use_fusion_head\\n        self.samples = []\\n        with open(data_path) as f:\\n            for line in f:\\n                if line.strip():\\n                    self.samples.append(json.loads(line))\\n        self._negatives = {}\\n\\n    def __len__(self):\\n        return len(self.samples)\\n\\n    def __getitem__(self, idx):\\n        s = self.samples[idx]\\n        query_enc = self.tokenizer(s[\\\"query_tokens\\\"], truncation=True, max_length=self.max_seq_length, padding=False, return_tensors=None)\\n        pos_enc = self.tokenizer(s[\\\"pos_tokens\\\"], truncation=True, max_length=self.max_seq_length, padding=False, return_tensors=None)\\n        dist = s.get(\\\"pos_dataflow_distance\\\", 1.0)\\n        pos_weight = math.exp(-self.alpha * dist)\\n\\n        neg_pool = self._negatives.get(idx, [])\\n        if len(neg_pool) < self.num_negatives:\\n            fallback = list(s.get(\\\"neg_candidates\\\", []))\\n            random.shuffle(fallback)\\n            while len(neg_pool) < self.num_negatives and fallback:\\n                cid = fallback.pop()\\n   
…[truncated 7064 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T15:07:41.161828+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cat /root/structfuse/scripts/bootstrap_paired_test.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "cat /root/structfuse/scripts/bootstrap_paired_test.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T15:07:41.162124+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nInstance-level cluster bootstrap: embedding_distance vs random mining (s43).\\nEvaluates both checkpoints on val_random_s43.jsonl (common eval set),\\ncomputes per-instance R@1, and runs cluster bootstrap clustered by repo.\\n\\\"\\\"\\\"\\n\\nimport json\\nimport os\\nimport sys\\nimport time\\nimport numpy as np\\nimport torch\\nimport torch.nn.functional as F\\nfrom pathlib import Path\\nfrom collections import defaultdict\\n\\nsys.path.insert(0, \\\"/root/structfuse/training\\\")\\nfrom contrastive_model import StructFuseEncoder\\nfrom transformers import AutoTokenizer\\n\\nRANDOM_CKPT = \\\"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1\\\"\\nEMBED_CKPT = \\\"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s43/best_by_recall_at_1\\\"\\nBASE_MODEL = \\\"/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B\\\"\\nVAL_FILE = \\\"/root/autodl-tmp/structfuse/full_m2_training_data/val_random_s43.jsonl\\\"\\nDEVICE = \\\"cuda:0\\\"\\nMAX_SEQ_LEN = 2048\\nNUM_NEGATIVES = 7\\nENCODE_BATCH = 8\\nN_BOOTSTRAP = 10000\\nOUTPUT_PATH = \\\"/root/structfuse/results/bootstrap_s43_paired.json\\\"\\n\\n\\ndef load_model(ckpt_dir, base_model, device):\\n    config_path = Path(ckpt_dir) / \\\"training_config.json\\\"\\n    with open(config_path) as f:\\n        cfg = json.load(f)\\n    model = StructFuseEncoder(\\n        model_name=base_model,\\n        proj_dim=cfg.get(\\\"proj_dim\\\", 256),\\n        use_lora=cfg.get(\\\"use_lora\\\", True),\\n        lora_r=cfg.get(\\\"lora_r\\\", 16),\\n        use_fusion_head=cfg.get(\\\"use_fusion_head\\\", False),\\n    )\\n    state_dict = torch.load(Path(ckpt_dir) / \\\"model.pt\\\", map_location=\\\"cpu\\\")\\n    result = model.load_state_dict(state_dict, strict=False)\\n    if result.unexpected_keys:\\n        print(f\\\"WARNING: unexpected keys: {result.unexpected_keys[:5]}\\\")\\n    if result.missin
…[truncated 7210 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T15:07:41.162345+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cat /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s43/best_by_recall_at_1/training_config.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "cat /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s43/best_by_recall_at_1/training_config.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T15:07:41.162505+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_name\\\": \\\"/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B\\\",\\n  \\\"train_file\\\": \\\"/root/autodl-tmp/structfuse/full_m2_training_data/train_embedding_distance_s43.jsonl\\\",\\n  \\\"val_file\\\": \\\"/root/autodl-tmp/structfuse/full_m2_training_data/val_embedding_distance_s43.jsonl\\\",\\n  \\\"output_dir\\\": \\\"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s43\\\",\\n  \\\"batch_size\\\": 8,\\n  \\\"learning_rate\\\": 2e-05,\\n  \\\"num_epochs\\\": 2,\\n  \\\"warmup_ratio\\\": 0.1,\\n  \\\"num_negatives\\\": 7,\\n  \\\"hard_negative_strategy\\\": \\\"embedding_distance\\\",\\n  \\\"hard_negative_ratio\\\": 0.5,\\n  \\\"temperature\\\": 0.07,\\n  \\\"pos_weight_alpha\\\": 1.0,\\n  \\\"use_fusion_head\\\": false,\\n  \\\"use_lora\\\": true,\\n  \\\"lora_r\\\": 16,\\n  \\\"proj_dim\\\": 256,\\n  \\\"gradient_checkpointing\\\": true,\\n  \\\"eval_steps\\\": 500,\\n  \\\"save_steps\\\": 1000,\\n  \\\"max_seq_length\\\": 2048,\\n  \\\"seed\\\": 43,\\n  \\\"wandb_project\\\": \\\"structfuse\\\",\\n  \\\"wandb_run_name\\\": \\\"m2_full_embedding_distance_s43\\\",\\n  \\\"dataflow_graph_file\\\": null,\\n  \\\"embeddings_file\\\": null,\\n  \\\"dynamic_mining\\\": false,\\n  \\\"candidate_pool_file\\\": null,\\n  \\\"early_stopping_patience\\\": 2\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T15:07:41.162678+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/autodl-tmp/structfuse/checkpoints/ -maxdepth 4 -type d",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "find /root/autodl-tmp/structfuse/checkpoints/ -maxdepth 4 -type d",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T15:07:41.162849+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/structfuse/checkpoints/\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_val_loss\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_val_loss\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_val_loss\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/final\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s43\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s43/best_by_val_loss\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s43/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s43/final\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s44\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s44/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s44/best_by_val_loss\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_val_loss\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s43\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/rand
…[truncated 548 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T15:07:41.163014+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/autodl-tmp/structfuse/checkpoints/ -maxdepth 5 -type d",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "find /root/autodl-tmp/structfuse/checkpoints/ -maxdepth 5 -type d",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T15:07:41.163167+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/structfuse/checkpoints/\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_val_loss\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_val_loss\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_val_loss\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/final\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s43\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s43/best_by_val_loss\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s43/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s43/final\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s44\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s44/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s44/best_by_val_loss\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_val_loss\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s43\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/rand
…[truncated 548 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T15:07:41.163304+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls -la /root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_recall_at_1/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "ls -la /root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_recall_at_1/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T15:07:41.163433+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 5981280\\ndrwxr-xr-x 2 root root       4096 May 14 16:26 .\\ndrwxr-xr-x 4 root root         69 May 14 16:26 ..\\n-rw-r--r-- 1 root root     441705 May 14 16:26 merges.txt\\n-rw-r--r-- 1 root root 6120106631 May 14 16:26 model.pt\\n-rw-r--r-- 1 root root       1332 May 14 16:26 special_tokens_map.json\\n-rw-r--r-- 1 root root    3478235 May 14 16:26 tokenizer.json\\n-rw-r--r-- 1 root root       7939 May 14 16:26 tokenizer_config.json\\n-rw-r--r-- 1 root root       1013 May 14 16:26 training_config.json\\n-rw-r--r-- 1 root root     777202 May 14 16:26 vocab.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-15T15:07:41.163575+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cat /root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_recall_at_1/training_config.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "cat /root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_recall_at_1/training_config.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T15:07:41.163751+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_name\\\": \\\"/root/autodl-tmp/models/bigcode/starcoder2-3b/bigcode/starcoder2-3b\\\",\\n  \\\"train_file\\\": \\\"/root/autodl-tmp/structfuse/full_m2_starcoder_data/train_random_s42.jsonl\\\",\\n  \\\"val_file\\\": \\\"/root/autodl-tmp/structfuse/full_m2_starcoder_data/val_random_s42.jsonl\\\",\\n  \\\"output_dir\\\": \\\"/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42\\\",\\n  \\\"batch_size\\\": 8,\\n  \\\"learning_rate\\\": 2e-05,\\n  \\\"num_epochs\\\": 3,\\n  \\\"warmup_ratio\\\": 0.1,\\n  \\\"num_negatives\\\": 7,\\n  \\\"hard_negative_strategy\\\": \\\"random\\\",\\n  \\\"hard_negative_ratio\\\": 0.5,\\n  \\\"temperature\\\": 0.07,\\n  \\\"pos_weight_alpha\\\": 1.0,\\n  \\\"use_fusion_head\\\": false,\\n  \\\"use_lora\\\": true,\\n  \\\"lora_r\\\": 16,\\n  \\\"proj_dim\\\": 256,\\n  \\\"gradient_checkpointing\\\": true,\\n  \\\"eval_steps\\\": 500,\\n  \\\"save_steps\\\": 1000,\\n  \\\"max_seq_length\\\": 2048,\\n  \\\"seed\\\": 42,\\n  \\\"wandb_project\\\": \\\"structfuse\\\",\\n  \\\"wandb_run_name\\\": \\\"m2_full_sc2_random_s42\\\",\\n  \\\"dataflow_graph_file\\\": null,\\n  \\\"embeddings_file\\\": null,\\n  \\\"dynamic_mining\\\": false,\\n  \\\"candidate_pool_file\\\": null,\\n  \\\"early_stopping_patience\\\": 0\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-15T15:07:41.163925+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "python3 -c \"\nimport torch\nsd = torch.load('/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s43/best_by_recall_at_1/model.pt', map_location='cpu')\nprint('Num keys:', len(sd))\nprint('Size MB:', sum(v.numel()*v.element_size() for v in sd.values()) / 1024**2)\nfor k in sorted(sd.keys())[:20]:\n    print(f'  {k}: {sd[k].shape}')\nprint('...')\nfor k in sorted(sd.keys())[-5:]:\n    print(f'  {k}: {sd[k].shape}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "python3 -c \"\nimport torch\nsd = torch.load('/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s43/best_by_recall_at_1/model.pt', map_location='cpu')\nprint('Num keys:', len(sd))\nprint('Size MB:', sum(v.numel()*v.element_size() for v in sd.values()) / 1024**2)\nfor k in sorted(sd.keys())[:20]:\n    print(f'  {k}: {sd[k].shape}')\nprint('...')\nfor k in sorted(sd.keys())[-5:]:\n    print(f'  {k}: {sd[k].shape}')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-15T15:07:41.164062+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"bash: line 1: python3: command not found\\n\", \"return_code\": 127}, \"error\": \"exit code 127\", \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-15T15:07:41.164182+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls /root/miniconda3/bin/python",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "ls /root/miniconda3/bin/python",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-15T15:07:41.164300+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/bin/python\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-15T15:07:41.164422+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-42106",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -c \"\nimport torch\nsd = torch.load('/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s43/best_by_recall_at_1/model.pt', map_location='cpu')\nprint('Num keys:', len(sd))\nprint('Size MB:', round(sum(v.numel()*v.element_size() for v in sd.values()) / 1024**2, 1))\nfor k in sorted(sd.keys())[:15]:\n    print(f'  {k}: {sd[k].shape}')\nprint('...')\nfor k in sorted(sd.keys())[-5:]:\n    print(f'  {k}: {sd[k].shape}')\n# Check if any key has 'lora' in it\nlora_keys = [k for k in sd if 'lora' in k]\nprint(f'\\nLoRA keys: {len(lora_keys)}')\nnon_backbone = [k for k in sd if not k.startswith('backbone.')]\nprint(f'Non-backbone keys: {non_backbone}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -c \"\nimport torch\nsd = torch.load('/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s43/best_by_recall_at_1/model.pt', map_location='cpu')\nprint('Num keys:', len(sd))\nprint('Size MB:', round(sum(v.numel()*v.element_size() for v in sd.values()) / 1024**2, 1))\nfor k in sorted(sd.keys())[:15]:\n    print(f'  {k}: {sd[k].shape}')\nprint('...')\nfor k in sorted(sd.keys())[-5:]:\n    print(f'  {k}: {sd[k].shape}')\n# Check if any key has 'lora' in it\nlora_keys = [k for k in sd if 'lora' in k]\nprint(f'\\nLoRA keys: {len(lora_keys)}')\nnon_backbone = [k for k in sd if not k.startswith('backbone.')]\nprint(f'Non-backbone keys: {non_backbone}')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-15T15:07:41.164589+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Num keys: 149\\nSize MB: 32.1\\n  backbone.base_model.model.layers.0.self_attn.q_proj.lora_A.default.weight: torch.Size([16, 2048])\\n  backbone.base_model.model.layers.0.self_attn.q_proj.lora_B.default.weight: torch.Size([2048, 16])\\n  backbone.base_model.model.layers.0.self_attn.v_proj.lora_A.default.weight: torch.Size([16, 2048])\\n  backbone.base_model.model.layers.0.self_attn.v_proj.lora_B.default.weight: torch.Size([256, 16])\\n  backbone.base_model.model.layers.1.self_attn.q_proj.lora_A.default.weight: torch.Size([16, 2048])\\n  backbone.base_model.model.layers.1.self_attn.q_proj.lora_B.default.weight: torch.Size([2048, 16])\\n  backbone.base_model.model.layers.1.self_attn.v_proj.lora_A.default.weight: torch.Size([16, 2048])\\n  backbone.base_model.model.layers.1.self_attn.v_proj.lora_B.default.weight: torch.Size([256, 16])\\n  backbone.base_model.model.layers.10.self_attn.q_proj.lora_A.default.weight: torch.Size([16, 2048])\\n  backbone.base_model.model.layers.10.self_attn.q_proj.lora_B.default.weight: torch.Size([2048, 16])\\n  backbone.base_model.model.layers.10.self_attn.v_proj.lora_A.default.weight: torch.Size([16, 2048])\\n  backbone.base_model.model.layers.10.self_attn.v_proj.lora_B.default.weight: torch.Size([256, 16])\\n  backbone.base_model.model.layers.11.self_attn.q_proj.lora_A.default.weight: torch.Size([16, 2048])\\n  backbone.base_model.model.layers.11.self_attn.q_proj.lora_B.default.weight: torch.Size([2048, 16])\\n  backbone.base_model.model.layers.11.self_attn.v_proj.lora_A.default.weight: torch.Size([16, 2048])\\n...\\n  log_temperature: torch.Size([])\\n  projection.0.bias: torch.Size([2048])\\n  projection.0.weight: torch.Size([2048, 2048])\\n  projection.2.bias: torch.Size([256])\\n  projection.2.weight: torch.Size([256, 2048])\\n\\nLoRA keys: 144\\nNon-backbone keys: ['log_temperature', 'projection.0.weight', 'projection.0.bias', 'projection.2.weight', 'projection.2.bias']\\n\", \
…[truncated 99 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-15T15:07:41.164782+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-42106",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -c \"\nimport sys, json, torch\nfrom pathlib import Path\nsys.path.insert(0, '/root/structfuse/training')\nfrom contrastive_model import StructFuseEncoder\n\nckpt_dir = '/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s43/best_by_recall_at_1'\nbase_model = '/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B'\n\nwith open(Path(ckpt_dir) / 'training_config.json') as f:\n    cfg = json.load(f)\n\nprint('Creating StructFuseEncoder...', flush=True)\nmodel = StructFuseEncoder(\n    model_name=base_model,\n    proj_dim=cfg.get('proj_dim', 256),\n    use_lora=cfg.get('use_lora', True),\n    lora_r=cfg.get('lora_r', 16),\n    use_fusion_head=cfg.get('use_fusion_head', False),\n)\n\nprint('Loading state dict...', flush=True)\nstate_dict = torch.load(Path(ckpt_dir) / 'model.pt', map_location='cpu')\nresult = model.load_state_dict(state_dict, strict=False)\nprint(f'Missing keys: {len(result.missing_keys)}')\nprint(f'Unexpected keys: {len(result.unexpected_keys)}')\nif result.unexpected_keys:\n    print(f'  Unexpected: {result.unexpected_keys[:5]}')\nprint('SUCCESS: model loaded', flush=True)\n\" 2>&1 | tail -20\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -c \"\nimport sys, json, torch\nfrom pathlib import Path\nsys.path.insert(0, '/root/structfuse/training')\nfrom contrastive_model import StructFuseEncoder\n\nckpt_dir = '/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s43/best_by_recall_at_1'\nbase_model = '/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B'\n\nwith open(Path(ckpt_dir) / 'training_config.json') as f:\n    cfg = json.load(f)\n\nprint('Creating StructFuseEncoder...', flush=True)\nmodel = StructFuseEncoder(\n    model_name=base_model,\n    proj_dim=cfg.get('proj_dim', 256),\n    use_lora=cfg.get('use_lora', True),\n    lora_r=cfg.get('lora_r', 16),\n    use_fusion_head=cfg.get('use_fusion_head', False),\n)\n\nprint('Loading state dict...', flush=True)\nstate_dict = torch.load(Path(ckpt_dir) / 'model.pt', map_location='cpu')\nresult = model.load_state_dict(state_dict, strict=False)\nprint(f'Missing keys: {len(result.missing_keys)}')\nprint(f'Unexpected keys: {len(result.unexpected_keys)}')\nif result.unexpected_keys:\n    print(f'  Unexpected: {result.unexpected_keys[:5]}')\nprint('SUCCESS: model loaded', flush=True)\n\" 2>&1 | tail -20\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-15T15:07:41.164934+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Creating StructFuseEncoder...\\n\\rLoading checkpoint shards:   0%|          | 0/2 [00:00<?, ?it/s]\\rLoading checkpoint shards:  50%|█████     | 1/2 [00:01<00:01,  1.01s/it]\\rLoading checkpoint shards: 100%|██████████| 2/2 [00:01<00:00,  1.91it/s]\\rLoading checkpoint shards: 100%|██████████| 2/2 [00:01<00:00,  1.68it/s]\\nLoading state dict...\\nMissing keys: 434\\nUnexpected keys: 0\\nSUCCESS: model loaded\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-15T15:07:41.165092+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/autodl-tmp/structfuse/ -maxdepth 4 -name \"model.pt\" -type f -newer /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s43/best_by_recall_at_1/model.pt",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "find /root/autodl-tmp/structfuse/ -maxdepth 4 -name \"model.pt\" -type f -newer /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s43/best_by_recall_at_1/model.pt",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-15T15:07:41.165218+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-15T15:07:41.165336+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/autodl-tmp/structfuse/ -maxdepth 5 -name \"adapter_config.json\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "find /root/autodl-tmp/structfuse/ -maxdepth 5 -name \"adapter_config.json\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-15T15:07:41.165453+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-15T15:07:41.165577+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/autodl-tmp/structfuse/ -maxdepth 3 -name \"model.pt\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "find /root/autodl-tmp/structfuse/ -maxdepth 3 -name \"model.pt\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-15T15:07:41.165719+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-15T15:07:41.165840+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/autodl-tmp/structfuse/ -maxdepth 5 -name \"model.pt\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "find /root/autodl-tmp/structfuse/ -maxdepth 5 -name \"model.pt\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-15T15:07:41.165971+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_val_loss/model.pt\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1/model.pt\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_val_loss/model.pt\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1/model.pt\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_val_loss/model.pt\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_recall_at_1/model.pt\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/final/model.pt\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s43/best_by_val_loss/model.pt\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s43/best_by_recall_at_1/model.pt\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s43/final/model.pt\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s44/best_by_recall_at_1/model.pt\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s44/best_by_val_loss/model.pt\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_val_loss/model.pt\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_recall_at_1/model.pt\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s43/best_by_val_loss/model.pt\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s43/best_by_recall_at_1/model.pt\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s43/final/model.pt\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s44/best_by_val_loss/model.pt\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s44/best_by_recall_at_1/model.pt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-15T15:07:41.166108+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/autodl-tmp/structfuse/checkpoints/ -name \"model.pt\" -type f -exec du -h {} \\;",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "find /root/autodl-tmp/structfuse/checkpoints/ -name \"model.pt\" -type f -exec du -h {} \\;",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-15T15:07:41.166223+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-15T15:07:41.166335+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/autodl-tmp/structfuse/checkpoints/ -name \"model.pt\" -type f -ls",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "find /root/autodl-tmp/structfuse/checkpoints/ -name \"model.pt\" -type f -ls",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-15T15:07:41.166475+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2167328449 6060344 -rw-r--r--   1 root     root     6205790987 May 14 05:49 /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_val_loss/model.pt\\n4310608493 6060344 -rw-r--r--   1 root     root     6205790987 May 14 05:50 /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1/model.pt\\n3249478708 6060344 -rw-r--r--   1 root     root     6205790987 May 14 21:29 /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_val_loss/model.pt\\n9664973673 6060344 -rw-r--r--   1 root     root     6205790987 May 15 01:36 /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1/model.pt\\n3264984504 6060344 -rw-r--r--   1 root     root     6205790987 May 15 04:03 /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_val_loss/model.pt\\n6453822913 6060344 -rw-r--r--   1 root     root     6205790987 May 15 04:04 /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_recall_at_1/model.pt\\n21478571911 6060344 -rw-r--r--   1 root     root     6205790987 May 15 08:32 /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/final/model.pt\\n25774953018   32888 -rw-r--r--   1 root     root       33674015 May 15 10:30 /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s43/best_by_val_loss/model.pt\\n 1091929815   32888 -rw-r--r--   1 root     root       33674015 May 15 14:28 /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s43/best_by_recall_at_1/model.pt\\n23623641930   32888 -rw-r--r--   1 root     root       33674015 May 15 14:50 /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s43/final/model.pt\\n11812839407   32888 -rw-r--r--   1 root     root       33674015 May 15 16:47 /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s44/best_by_recall_at_1/model.pt\\n 2182768337   32888 -rw-r--r--   1 root     root  
…[truncated 1451 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-15T15:07:41.166676+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-42106",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -c \"\nimport sys, json, torch\nfrom pathlib import Path\nsys.path.insert(0, '/root/structfuse/training')\nfrom contrastive_model import StructFuseEncoder\n\n# Full model checkpoint (random_s43, 6.2GB)\nckpt_dir = '/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1'\nbase_model = '/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B'\n\nwith open(Path(ckpt_dir) / 'training_config.json') as f:\n    cfg = json.load(f)\n\nprint('Testing FULL model checkpoint (random_s43)...', flush=True)\nprint(f'use_lora in config: {cfg.get(\\\"use_lora\\\", True)}', flush=True)\n\nmodel = StructFuseEncoder(\n    model_name=base_model,\n    proj_dim=cfg.get('proj_dim', 256),\n    use_lora=cfg.get('use_lora', True),\n    lora_r=cfg.get('lora_r', 16),\n    use_fusion_head=cfg.get('use_fusion_head', False),\n)\n\nstate_dict = torch.load(Path(ckpt_dir) / 'model.pt', map_location='cpu')\nprint(f'Checkpoint keys: {len(state_dict)}', flush=True)\nprint(f'Checkpoint size: {sum(v.numel()*v.element_size() for v in state_dict.values()) / 1024**3:.2f} GB', flush=True)\n\nresult = model.load_state_dict(state_dict, strict=False)\nprint(f'Missing keys: {len(result.missing_keys)}')\nprint(f'Unexpected keys: {len(result.unexpected_keys)}')\nif result.unexpected_keys:\n    print(f'  First 5 unexpected: {result.unexpected_keys[:5]}')\nprint('Load result: OK', flush=True)\n\" 2>&1 | tail -15\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -c \"\nimport sys, json, torch\nfrom pathlib import Path\nsys.path.insert(0, '/root/structfuse/training')\nfrom contrastive_model import StructFuseEncoder\n\n# Full model checkpoint (random_s43, 6.2GB)\nckpt_dir = '/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1'\nbase_model = '/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B'\n\nwith open(Path(ckpt_dir) / 'training_config.json') as f:\n    cfg = json.load(f)\n\nprint('Testing FULL model checkpoint (random_s43)...', flush=True)\nprint(f'use_lora in config: {cfg.get(\\\"use_lora\\\", True)}', flush=True)\n\nmodel = StructFuseEncoder(\n    model_name=base_model,\n    proj_dim=cfg.get('proj_dim', 256),\n    use_lora=cfg.get('use_lora', True),\n    lora_r=cfg.get('lora_r', 16),\n    use_fusion_head=cfg.get('use_fusion_head', False),\n)\n\nstate_dict = torch.load(Path(ckpt_dir) / 'model.pt', map_location='cpu')\nprint(f'Checkpoint keys: {len(state_dict)}', flush=True)\nprint(f'Checkpoint size: {sum(v.numel()*v.element_size() for v in state_dict.values()) / 1024**3:.2f} GB', flush=True)\n\nresult = model.load_state_dict(state_dict, strict=False)\nprint(f'Missing keys: {len(result.missing_keys)}')\nprint(f'Unexpected keys: {len(result.unexpected_keys)}')\nif result.unexpected_keys:\n    print(f'  First 5 unexpected: {result.unexpected_keys[:5]}')\nprint('Load result: OK', flush=True)\n\" 2>&1 | tail -15\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-15T15:07:41.166837+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Testing FULL model checkpoint (random_s43)...\\nuse_lora in config: True\\n\\rLoading checkpoint shards:   0%|          | 0/2 [00:00<?, ?it/s]\\rLoading checkpoint shards:  50%|█████     | 1/2 [00:00<00:00,  1.01it/s]\\rLoading checkpoint shards: 100%|██████████| 2/2 [00:01<00:00,  1.92it/s]\\rLoading checkpoint shards: 100%|██████████| 2/2 [00:01<00:00,  1.69it/s]\\nCheckpoint keys: 583\\nCheckpoint size: 5.78 GB\\nMissing keys: 0\\nUnexpected keys: 0\\nLoad result: OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 12.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-15T15:07:41.167013+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "head -n 150 /root/structfuse/scripts/bootstrap_paired_test.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "head -n 150 /root/structfuse/scripts/bootstrap_paired_test.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-15T15:07:41.167203+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nInstance-level cluster bootstrap: embedding_distance vs random mining (s43).\\nEvaluates both checkpoints on val_random_s43.jsonl (common eval set),\\ncomputes per-instance R@1, and runs cluster bootstrap clustered by repo.\\n\\\"\\\"\\\"\\n\\nimport json\\nimport os\\nimport sys\\nimport time\\nimport numpy as np\\nimport torch\\nimport torch.nn.functional as F\\nfrom pathlib import Path\\nfrom collections import defaultdict\\n\\nsys.path.insert(0, \\\"/root/structfuse/training\\\")\\nfrom contrastive_model import StructFuseEncoder\\nfrom transformers import AutoTokenizer\\n\\nRANDOM_CKPT = \\\"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1\\\"\\nEMBED_CKPT = \\\"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s43/best_by_recall_at_1\\\"\\nBASE_MODEL = \\\"/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B\\\"\\nVAL_FILE = \\\"/root/autodl-tmp/structfuse/full_m2_training_data/val_random_s43.jsonl\\\"\\nDEVICE = \\\"cuda:0\\\"\\nMAX_SEQ_LEN = 2048\\nNUM_NEGATIVES = 7\\nENCODE_BATCH = 8\\nN_BOOTSTRAP = 10000\\nOUTPUT_PATH = \\\"/root/structfuse/results/bootstrap_s43_paired.json\\\"\\n\\n\\ndef load_model(ckpt_dir, base_model, device):\\n    config_path = Path(ckpt_dir) / \\\"training_config.json\\\"\\n    with open(config_path) as f:\\n        cfg = json.load(f)\\n    model = StructFuseEncoder(\\n        model_name=base_model,\\n        proj_dim=cfg.get(\\\"proj_dim\\\", 256),\\n        use_lora=cfg.get(\\\"use_lora\\\", True),\\n        lora_r=cfg.get(\\\"lora_r\\\", 16),\\n        use_fusion_head=cfg.get(\\\"use_fusion_head\\\", False),\\n    )\\n    state_dict = torch.load(Path(ckpt_dir) / \\\"model.pt\\\", map_location=\\\"cpu\\\")\\n    result = model.load_state_dict(state_dict, strict=False)\\n    if result.unexpected_keys:\\n        print(f\\\"WARNING: unexpected keys: {result.unexpected_keys[:5]}\\\")\\n    if result.missin
…[truncated 3995 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-15T15:07:41.167349+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "tail -n +150 /root/structfuse/scripts/bootstrap_paired_test.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "tail -n +150 /root/structfuse/scripts/bootstrap_paired_test.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-15T15:07:41.167544+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"        for repo in sampled:\\n            total_sum += repo_means[repo] * repo_sizes[repo]\\n            total_n += repo_sizes[repo]\\n        bootstrap_means[b] = total_sum / total_n\\n\\n    mean_delta = float(deltas.mean())\\n    ci_lower = float(np.percentile(bootstrap_means, 2.5))\\n    ci_upper = float(np.percentile(bootstrap_means, 97.5))\\n    p_one_sided = float(np.mean(bootstrap_means <= 0))\\n    p_two_sided = float(2 * min(np.mean(bootstrap_means <= 0), np.mean(bootstrap_means >= 0)))\\n\\n    return {\\n        \\\"mean_delta\\\": mean_delta,\\n        \\\"ci_95\\\": [ci_lower, ci_upper],\\n        \\\"p_value_one_sided\\\": p_one_sided,\\n        \\\"p_value_two_sided\\\": p_two_sided,\\n        \\\"bootstrap_std\\\": float(bootstrap_means.std()),\\n    }\\n\\n\\ndef main():\\n    t_start = time.time()\\n\\n    print(\\\"Loading val data...\\\", flush=True)\\n    samples = load_val_data(VAL_FILE, NUM_NEGATIVES)\\n    print(f\\\"Loaded {len(samples)} instances\\\", flush=True)\\n\\n    pool_sizes = [len(s[\\\"pool_texts\\\"]) for s in samples]\\n    print(f\\\"Pool sizes: min={min(pool_sizes)}, max={max(pool_sizes)}, mean={np.mean(pool_sizes):.1f}\\\", flush=True)\\n\\n    tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL, trust_remote_code=True)\\n    if tokenizer.pad_token is None:\\n        tokenizer.pad_token = tokenizer.eos_token\\n\\n    # Model 1: random_s43\\n    print(f\\\"\\\\n{'='*60}\\\", flush=True)\\n    print(\\\"Model 1: random_s43\\\", flush=True)\\n    model = load_model(RANDOM_CKPT, BASE_MODEL, DEVICE)\\n    r1_random = compute_per_instance_r1(model, tokenizer, samples, DEVICE, MAX_SEQ_LEN, ENCODE_BATCH)\\n    print(f\\\"R@1 = {np.mean(r1_random):.4f}\\\", flush=True)\\n    del model\\n    torch.cuda.empty_cache()\\n\\n    # Model 2: embedding_distance_s43\\n    print(f\\\"\\\\n{'='*60}\\\", flush=True)\\n    print(\\\"Model 2: embedding_distance_s43\\\", flush=True)\\n    mo
…[truncated 3483 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-15T15:07:41.167773+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-42106",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cat > /tmp/fix_load_model.py << 'PYEOF'\n\"\"\"Patch load_model in bootstrap_paired_test.py with adapter-only detection.\"\"\"\nimport re\n\nscript_path = \"/root/structfuse/scripts/bootstrap_paired_test.py\"\nwith open(script_path) as f:\n    content = f.read()\n\n# The old load_model function\nold_func = '''def load_model(ckpt_dir, base_model, device):\n    config_path = Path(ckpt_dir) / \"training_config.json\"\n    with open(config_path) as f:\n        cfg = json.load(f)\n    model = StructFuseEncoder(\n        model_name=base_model,\n        proj_dim=cfg.get(\"proj_dim\", 256),\n        use_lora=cfg.get(\"use_lora\", True),\n        lora_r=cfg.get(\"lora_r\", 16),\n        use_fusion_head=cfg.get(\"use_fusion_head\", False),\n    )\n    state_dict = torch.load(Path(ckpt_dir) / \"model.pt\", map_location=\"cpu\")\n    result = model.load_state_dict(state_dict, strict=False)\n    if result.unexpected_keys:\n        print(f\"WARNING: unexpected keys: {result.unexpected_keys[:5]}\")\n    if result.missing_keys:\n        print(f\"  Note: {len(result.missing_keys)} missing keys (base model weights from pretrained, expected for LoRA-only checkpoints)\")\n    model = model.to(device).eval()\n    return model'''\n\nnew_func = '''ADAPTER_ONLY_SIZE_THRESHOLD = 500 * 1024 * 1024  # 500MB\n\n\ndef _is_adapter_only(ckpt_dir):\n    \"\"\"Adapter-only checkpoints are <500MB (LoRA weights + projection only).\n    Full-model checkpoints include all backbone weights and are multi-GB.\"\"\"\n    model_pt = Path(ckpt_dir) / \"model.pt\"\n    if (Path(ckpt_dir) / \"adapter_config.json\").exists():\n        return True\n    return model_pt.stat().st_size < ADAPTER_ONLY_SIZE_THRESHOLD\n\n\ndef load_model(ckpt_dir, base_model, device):\n    config_path = Path(ckpt_dir) / \"training_config.json\"\n    with open(config_path) as f:\n        cfg = json.load(f)\n\n    adapter_only = _is_adapter_only(ckpt_dir)\n    ckpt_label = \"adapter-only\" if adapter_only else \"full-model\"\n    model_pt = Path(ckpt_dir) / \"model.pt\"\n    size_mb = model_pt.stat().st_size / 1024**2\n    print(f\"  Checkpoint: {ckpt_dir} ({ckpt_label}, {size_mb:.0f}MB)\", flush=True)\n\n    model = StructFuseEncoder(\n        model_name=base_model,\n        proj_dim=cfg.get(\"proj_dim\", 256),\n        use_lora=cfg.get(\"use_lora\", True),\n        lora_r=cfg.get(\"lora_r\", 16),\n        use_fusion_head=cfg.get(\"use_fusion_head\", False),\n    )\n\n    state_dict = torch.load(model_pt, map_location=\"cpu\")\n\n    if adapter_only:\n        result = model.load_state_dict(state_dict, strict=False)\n        if result.unexpected_keys:\n            raise RuntimeError(f\"Unexpected keys in adapter-only checkpoint: {result.unexpected_keys[:10]}\")\n        n_missing = len(result.missing_keys)\n        non_backbone_missing = [k for k in result.missing_keys if not k.startswith(\"backbone.\")]\n        if non_backbone_missing:\n            raise RuntimeError(f\"Adapter-only checkpoint missing non-backbone keys: {non_backbone_missing[:10]}\")\n        print(f\"  Loaded {len(state_dict)} adapter keys ({n_missing} base-model keys from pretrained)\", flush=True)\n    else:\n        result = model.load_state_dict(state_dict, strict=False)\n        if result.unexpected_keys:\n            print(f\"  WARNING: unexpected keys: {result.unexpected_keys[:5]}\", flush=True)\n        if result.missing_keys:\n            print(f\"  WARNING: {len(result.missing_keys)} missing keys in full-model checkpoint\", flush=True)\n\n    model = model.to(device).eval()\n    return model'''\n\nassert old_func in content, \"Could not find old load_model function\"\nnew_content = content.replace(old_func, new_func)\nassert new_content != content, \"Replacement failed\"\n\nwith open(script_path, 'w') as f:\n    f.write(new_content)\n\nprint(\"Patched successfully\")\nPYEOF\npython /tmp/fix_load_model.py\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cat > /tmp/fix_load_model.py << 'PYEOF'\n\"\"\"Patch load_model in bootstrap_paired_test.py with adapter-only detection.\"\"\"\nimport re\n\nscript_path = \"/root/structfuse/scripts/bootstrap_paired_test.py\"\nwith open(script_path) as f:\n    content = f.read()\n\n# The old load_model function\nold_func = '''def load_model(ckpt_dir, base_model, device):\n    config_path = Path(ckpt_dir) / \"training_config.json\"\n    with open(config_path) as f:\n        cfg = json.load(f)\n    model = StructFuseEncoder(\n        model_name=base_model,\n        proj_dim=cfg.get(\"proj_dim\", 256),\n        use_lora=cfg.get(\"use_lora\", True),\n        lora_r=cfg.get(\"lora_r\", 16),\n        use_fusion_head=cfg.get(\"use_fusion_head\", False),\n    )\n    state_dict = torch.load(Path(ckpt_dir) / \"model.pt\", map_location=\"cpu\")\n    result = model.load_state_dict(state_dict, strict=False)\n    if result.unexpected_keys:\n        print(f\"WARNING: unexpected keys: {result.unexpected_keys[:5]}\")\n    if result.missing_keys:\n        print(f\"  Note: {len(result.missing_keys)} missing keys (base model weights from pretrained, expected for LoRA-only checkpoints)\")\n    model = model.to(device).eval()\n    return model'''\n\nnew_func = '''ADAPTER_ONLY_SIZE_THRESHOLD = 500 * 1024 * 1024  # 500MB\n\n\ndef _is_adapter_only(ckpt_dir):\n    \"\"\"Adapter-only checkpoints are <500MB (LoRA weights + projection only).\n    Full-model checkpoints include all backbone weights and are multi-GB.\"\"\"\n    model_pt = Path(ckpt_dir) / \"model.pt\"\n    if (Path(ckpt_dir) / \"adapter_config.json\").exists():\n        return True\n    return model_pt.stat().st_size < ADAPTER_ONLY_SIZE_THRESHOLD\n\n\ndef load_model(ckpt_dir, base_model, device):\n    config_path = Path(ckpt_dir) / \"training_config.json\"\n    with open(config_path) as f:\n        cfg = json.load(f)\n\n    adapter_only = _is_adapter_only(ckpt_dir)\n    ckpt_label = \"adapter-only\" if adapter_only else \"full-model\"\n    model_pt = Path(ckpt_dir) / \"model.pt\"\n    size_mb = model_pt.stat().st_size / 1024**2\n    print(f\"  Checkpoint: {ckpt_dir} ({ckpt_label}, {size_mb:.0f}MB)\", flush=True)\n\n    model = StructFuseEncoder(\n        model_name=base_model,\n        proj_dim=cfg.get(\"proj_dim\", 256),\n        use_lora=cfg.get(\"use_lora\", True),\n        lora_r=cfg.get(\"lora_r\", 16),\n        use_fusion_head=cfg.get(\"use_fusion_head\", False),\n    )\n\n    state_dict = torch.load(model_pt, map_location=\"cpu\")\n\n    if adapter_only:\n        result = model.load_state_dict(state_dict, strict=False)\n        if result.unexpected_keys:\n            raise RuntimeError(f\"Unexpected keys in adapter-only checkpoint: {result.unexpected_keys[:10]}\")\n        n_missing = len(result.missing_keys)\n        non_backbone_missing = [k for k in result.missing_keys if not k.startswith(\"backbone.\")]\n        if non_backbone_missing:\n            raise RuntimeError(f\"Adapter-only checkpoint missing non-backbone keys: {non_backbone_missing[:10]}\")\n        print(f\"  Loaded {len(state_dict)} adapter keys ({n_missing} base-model keys from pretrained)\", flush=True)\n    else:\n        result = model.load_state_dict(state_dict, strict=False)\n        if result.unexpected_keys:\n            print(f\"  WARNING: unexpected keys: {result.unexpected_keys[:5]}\", flush=True)\n        if result.missing_keys:\n            print(f\"  WARNING: {len(result.missing_keys)} missing keys in full-model checkpoint\", flush=True)\n\n    model = model.to(device).eval()\n    return model'''\n\nassert old_func in content, \"Could not find old load_model function\"\nnew_content = content.replace(old_func, new_func)\nassert new_content != content, \"Replacement failed\"\n\nwith open(script_path, 'w') as f:\n    f.write(new_content)\n\nprint(\"Patched successfully\")\nPYEOF\npython /tmp/fix_load_model.py\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-15T15:07:41.167942+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Patched successfully\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-15T15:07:41.168088+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-42106",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -c \"\nimport sys, json, torch\nimport torch.nn.functional as F\nfrom pathlib import Path\nsys.path.insert(0, '/root/structfuse/training')\nfrom contrastive_model import StructFuseEncoder\nfrom transformers import AutoTokenizer\n\n# Import the patched load_model\nsys.path.insert(0, '/root/structfuse/scripts')\nexec(open('/root/structfuse/scripts/bootstrap_paired_test.py').read().split('def load_val_data')[0])\n\nBASE_MODEL = '/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B'\nDEVICE = 'cpu'\n\n# Test 1: adapter-only checkpoint\nprint('=== Test 1: adapter-only checkpoint ===', flush=True)\nmodel1 = load_model(\n    '/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s43/best_by_recall_at_1',\n    BASE_MODEL, DEVICE)\n\ntokenizer = AutoTokenizer.from_pretrained(BASE_MODEL, trust_remote_code=True)\nif tokenizer.pad_token is None:\n    tokenizer.pad_token = tokenizer.eos_token\n\nenc = tokenizer('def hello(): return 42', truncation=True, max_length=512, padding=True, return_tensors='pt')\nwith torch.no_grad():\n    emb = model1.encode(enc['input_ids'], enc['attention_mask'])\nprint(f'  Embedding shape: {emb.shape}, norm: {emb.norm().item():.4f}', flush=True)\ndel model1\n\n# Test 2: full-model checkpoint\nprint('=== Test 2: full-model checkpoint ===', flush=True)\nmodel2 = load_model(\n    '/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1',\n    BASE_MODEL, DEVICE)\nwith torch.no_grad():\n    emb2 = model2.encode(enc['input_ids'], enc['attention_mask'])\nprint(f'  Embedding shape: {emb2.shape}, norm: {emb2.norm().item():.4f}', flush=True)\ndel model2\n\nprint('\\\\nAll tests passed.', flush=True)\n\" 2>&1\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -c \"\nimport sys, json, torch\nimport torch.nn.functional as F\nfrom pathlib import Path\nsys.path.insert(0, '/root/structfuse/training')\nfrom contrastive_model import StructFuseEncoder\nfrom transformers import AutoTokenizer\n\n# Import the patched load_model\nsys.path.insert(0, '/root/structfuse/scripts')\nexec(open('/root/structfuse/scripts/bootstrap_paired_test.py').read().split('def load_val_data')[0])\n\nBASE_MODEL = '/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B'\nDEVICE = 'cpu'\n\n# Test 1: adapter-only checkpoint\nprint('=== Test 1: adapter-only checkpoint ===', flush=True)\nmodel1 = load_model(\n    '/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s43/best_by_recall_at_1',\n    BASE_MODEL, DEVICE)\n\ntokenizer = AutoTokenizer.from_pretrained(BASE_MODEL, trust_remote_code=True)\nif tokenizer.pad_token is None:\n    tokenizer.pad_token = tokenizer.eos_token\n\nenc = tokenizer('def hello(): return 42', truncation=True, max_length=512, padding=True, return_tensors='pt')\nwith torch.no_grad():\n    emb = model1.encode(enc['input_ids'], enc['attention_mask'])\nprint(f'  Embedding shape: {emb.shape}, norm: {emb.norm().item():.4f}', flush=True)\ndel model1\n\n# Test 2: full-model checkpoint\nprint('=== Test 2: full-model checkpoint ===', flush=True)\nmodel2 = load_model(\n    '/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1',\n    BASE_MODEL, DEVICE)\nwith torch.no_grad():\n    emb2 = model2.encode(enc['input_ids'], enc['attention_mask'])\nprint(f'  Embedding shape: {emb2.shape}, norm: {emb2.norm().item():.4f}', flush=True)\ndel model2\n\nprint('\\\\nAll tests passed.', flush=True)\n\" 2>&1\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-15T15:07:41.168246+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== Test 1: adapter-only checkpoint ===\\n  Checkpoint: /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s43/best_by_recall_at_1 (adapter-only, 32MB)\\n\\rLoading checkpoint shards:   0%|          | 0/2 [00:00<?, ?it/s]\\rLoading checkpoint shards:  50%|█████     | 1/2 [00:01<00:01,  1.09s/it]\\rLoading checkpoint shards: 100%|██████████| 2/2 [00:01<00:00,  1.78it/s]\\rLoading checkpoint shards: 100%|██████████| 2/2 [00:01<00:00,  1.56it/s]\\n  Loaded 149 adapter keys (434 base-model keys from pretrained)\\n  Embedding shape: torch.Size([1, 256]), norm: 1.0000\\n=== Test 2: full-model checkpoint ===\\n  Checkpoint: /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1 (full-model, 5918MB)\\n\\rLoading checkpoint shards:   0%|          | 0/2 [00:00<?, ?it/s]\\rLoading checkpoint shards:  50%|█████     | 1/2 [00:01<00:01,  1.04s/it]\\rLoading checkpoint shards: 100%|██████████| 2/2 [00:01<00:00,  1.86it/s]\\rLoading checkpoint shards: 100%|██████████| 2/2 [00:01<00:00,  1.63it/s]\\n  Embedding shape: torch.Size([1, 256]), norm: 1.0000\\n\\nAll tests passed.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 16.14}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-15T15:07:41.168396+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "head -n 65 /root/structfuse/scripts/bootstrap_paired_test.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "head -n 65 /root/structfuse/scripts/bootstrap_paired_test.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-15T15:07:41.168577+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nInstance-level cluster bootstrap: embedding_distance vs random mining (s43).\\nEvaluates both checkpoints on val_random_s43.jsonl (common eval set),\\ncomputes per-instance R@1, and runs cluster bootstrap clustered by repo.\\n\\\"\\\"\\\"\\n\\nimport json\\nimport os\\nimport sys\\nimport time\\nimport numpy as np\\nimport torch\\nimport torch.nn.functional as F\\nfrom pathlib import Path\\nfrom collections import defaultdict\\n\\nsys.path.insert(0, \\\"/root/structfuse/training\\\")\\nfrom contrastive_model import StructFuseEncoder\\nfrom transformers import AutoTokenizer\\n\\nRANDOM_CKPT = \\\"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1\\\"\\nEMBED_CKPT = \\\"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s43/best_by_recall_at_1\\\"\\nBASE_MODEL = \\\"/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B\\\"\\nVAL_FILE = \\\"/root/autodl-tmp/structfuse/full_m2_training_data/val_random_s43.jsonl\\\"\\nDEVICE = \\\"cuda:0\\\"\\nMAX_SEQ_LEN = 2048\\nNUM_NEGATIVES = 7\\nENCODE_BATCH = 8\\nN_BOOTSTRAP = 10000\\nOUTPUT_PATH = \\\"/root/structfuse/results/bootstrap_s43_paired.json\\\"\\n\\n\\nADAPTER_ONLY_SIZE_THRESHOLD = 500 * 1024 * 1024  # 500MB\\n\\n\\ndef _is_adapter_only(ckpt_dir):\\n    \\\"\\\"\\\"Adapter-only checkpoints are <500MB (LoRA weights + projection only).\\n    Full-model checkpoints include all backbone weights and are multi-GB.\\\"\\\"\\\"\\n    model_pt = Path(ckpt_dir) / \\\"model.pt\\\"\\n    if (Path(ckpt_dir) / \\\"adapter_config.json\\\").exists():\\n        return True\\n    return model_pt.stat().st_size < ADAPTER_ONLY_SIZE_THRESHOLD\\n\\n\\ndef load_model(ckpt_dir, base_model, device):\\n    config_path = Path(ckpt_dir) / \\\"training_config.json\\\"\\n    with open(config_path) as f:\\n        cfg = json.load(f)\\n\\n    adapter_only = _is_adapter_only(ckpt_dir)\\n    ckpt_label = \\\"adapter-only\\\" if
…[truncated 701 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-15T15:07:41.168765+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "tail -n +65 /root/structfuse/scripts/bootstrap_paired_test.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "tail -n +65 /root/structfuse/scripts/bootstrap_paired_test.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-15T15:07:41.169029+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n    if adapter_only:\\n        result = model.load_state_dict(state_dict, strict=False)\\n        if result.unexpected_keys:\\n            raise RuntimeError(f\\\"Unexpected keys in adapter-only checkpoint: {result.unexpected_keys[:10]}\\\")\\n        n_missing = len(result.missing_keys)\\n        non_backbone_missing = [k for k in result.missing_keys if not k.startswith(\\\"backbone.\\\")]\\n        if non_backbone_missing:\\n            raise RuntimeError(f\\\"Adapter-only checkpoint missing non-backbone keys: {non_backbone_missing[:10]}\\\")\\n        print(f\\\"  Loaded {len(state_dict)} adapter keys ({n_missing} base-model keys from pretrained)\\\", flush=True)\\n    else:\\n        result = model.load_state_dict(state_dict, strict=False)\\n        if result.unexpected_keys:\\n            print(f\\\"  WARNING: unexpected keys: {result.unexpected_keys[:5]}\\\", flush=True)\\n        if result.missing_keys:\\n            print(f\\\"  WARNING: {len(result.missing_keys)} missing keys in full-model checkpoint\\\", flush=True)\\n\\n    model = model.to(device).eval()\\n    return model\\n\\n\\ndef load_val_data(val_file, num_negatives):\\n    samples = []\\n    with open(val_file) as f:\\n        for line in f:\\n            if not line.strip():\\n                continue\\n            d = json.loads(line)\\n            neg_candidates = d.get(\\\"neg_candidates\\\", [])\\n            candidate_tokens = d.get(\\\"candidate_tokens\\\", {})\\n            neg_texts = []\\n            for cid in neg_candidates:\\n                t = candidate_tokens.get(cid, \\\"\\\")\\n                if t:\\n                    neg_texts.append(t)\\n                if len(neg_texts) >= num_negatives:\\n                    break\\n            pool_texts = [d[\\\"pos_tokens\\\"]] + neg_texts\\n            samples.append({\\n                \\\"query_id\\\": d[\\\"query_id\\\"],\\n                \\\"query_text\\\": d[\\\"query_tok
…[truncated 7143 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 75 · 2026-05-15T15:07:41.169227+00:00_

修改完成，dry-run 验证通过。

**修改内容** (`/root/structfuse/scripts/bootstrap_paired_test.py`)：

1. 新增 `_is_adapter_only(ckpt_dir)` — 通过文件大小 (<500MB) 或 `adapter_config.json` 存在检测 adapter-only checkpoint
2. 重写 `load_model` 的加载逻辑：
   - **Adapter-only** (如 embedding_distance_s43, 32MB)：`strict=False` 加载，验证无 unexpected keys，验证 missing keys 只是 backbone 权重（非 backbone 的 missing key 会 raise）
   - **Full-model** (如 random_s43, 5.9GB)：`strict=False` 加载，warning 提示异常
3. 加载时打印 checkpoint 类型和大小，方便排查

**Dry-run 验证**：
- adapter-only checkpoint (`embedding_distance_s43/best_by_recall_at_1`, 32MB) — 加载 149 adapter keys, 434 base-model keys 从 pretrained 获取，embedding shape [1,256], norm=1.0
- full-model checkpoint (`random_s43/best_by_recall_at_1`, 5918MB) — 583 keys 全部匹配，embedding shape [1,256], norm=1.0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_fix_bootstrap_checkpoint_20260515T150138"
}
```

</details>

---
