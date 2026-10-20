# check running experiments

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_check_running_experiments_20260524T095747.jsonl`
- **Structured JSON:** [`2d42b170866a97118ec4.json`](../../sessions/2d/2d42b170866a97118ec4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-24T09:59:05.831163+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_running_experiments_20260524T095747",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-24T09:59:05.831482+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_running_experiments_20260524T095747",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-24T09:59:05.831647+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "ps -p 165918,167297,169724 -o pid,stat,etime,cmd",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_running_experiments_20260524T095747",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "ps -p 165918,167297,169724 -o pid,stat,etime,cmd",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-24T09:59:05.831801+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "nvidia-smi --query-gpu=index,utilization.gpu,memory.used,memory.total --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_running_experiments_20260524T095747",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "nvidia-smi --query-gpu=index,utilization.gpu,memory.used,memory.total --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-24T09:59:05.831959+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"   PID STAT     ELAPSED CMD\\n167297 S          35:23 bash -c cd /root/autodl-tmp/gen-depth-contamination && nohup bash scripts/run_code_olmo1b.sh > results/exp_code_olmo.log 2>&1 & echo \\\"PID=$!\\\"\\n169724 S          10:48 bash -c cd /root/autodl-tmp/gen-depth-contamination && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && mkdir -p logs/exp_gemma27b_filtering && nohup bash -c ' export HF_HOME=/root/autodl-tmp/.hf_cache export HF_ENDPOINT=https://hf-mirror.com export HF_DATASETS_OFFLINE=1 export HF_HUB_OFFLINE=1 export TRANSFORMERS_OFFLINE=1  cd /root/autodl-tmp/gen-depth-contamination source /root/miniconda3/etc/profile.d/conda.sh && conda activate base  STRATEGIES=\\\"no_filter binary_ours graduated_a09\\\" SEEDS=\\\"42 123 456\\\"  echo \\\"=== START $(date) ===\\\" for strategy in $STRATEGIES; do     for seed in $SEEDS; do         echo \\\">>> $strategy seed=$seed $(date)\\\"         python scripts/exp_gemma27b_filtering.py --strategy $strategy --seed $seed --device cuda:3 2>&1         echo \\\"<<< $strategy seed=$seed $(date)\\\"     done done echo \\\"=== DONE $(date) ===\\\" ' > logs/exp_gemma27b_filtering/run_all.log 2>&1 & echo \\\"PID=$!\\\"\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.77}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_running_experiments_20260524T095747",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-24T09:59:05.832101+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 36 %, 12139 MiB, 97887 MiB\\n1, 85 %, 14308 MiB, 97887 MiB\\n2, 36 %, 8729 MiB, 97887 MiB\\n3, 35 %, 8729 MiB, 97887 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_running_experiments_20260524T095747",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-24T09:59:05.832242+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "tail -30 /root/autodl-tmp/gen-depth-contamination/results/exp_code_olmo.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_running_experiments_20260524T095747",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "tail -30 /root/autodl-tmp/gen-depth-contamination/results/exp_code_olmo.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-24T09:59:05.832450+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Scorer:    /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B-Instruct\\nSeed:      data/code_python_seed\\nData:      data/exp_code_olmo\\nResults:   results/exp_code_olmo\\nGPU:       CUDA_VISIBLE_DEVICES=1\\n\\n=== Phase 1: Generating depth chain with OLMo-1B ===\\n17:22:41 [INFO] Model: /root/autodl-tmp/.hf_cache/allenai/OLMo-1B-hf\\n17:22:41 [INFO] Data dir: data/exp_code_olmo\\n17:22:41 [INFO] Samples: 5500, Max depth: 5\\n17:22:41 [INFO] Decoding: do_sample=True, top_p=0.95, temperature=1.0\\n17:22:41 [INFO] Generation mode: continuation\\n17:22:44 [INFO] Loading tokenizer ...\\n17:22:44 [INFO] Loading model ...\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n17:22:44 [WARNING] Skipping import of cpp extensions due to incompatible torch version. Please upgrade to torch >= 2.11.0 (found 2.8.0+cu128).\\n\\rLoading weights:   0%|          | 0/113 [00:00<?, ?it/s]\\rLoading weights:   8%|▊         | 9/113 [00:00<00:01, 74.37it/s]\\rLoading weights:  27%|██▋       | 30/113 [00:00<00:00, 142.22it/s]\\rLoading weights:  46%|████▌     | 52/113 [00:00<00:00, 172.05it/s]\\rLoading weights:  64%|██████▎   | 72/113 [00:00<00:00, 179.06it/s]\\rLoading weights:  81%|████████  | 91/113 [00:00<00:00, 177.61it/s]\\rLoading weights:  96%|█████████▋| 109/113 [00:00<00:00, 152.08it/s]\\rLoading weights: 100%|██████████| 113/113 [00:00<00:00, 160.79it/s]\\n17:22:46 [INFO] Model loaded on cuda:0\\n17:22:46 [INFO] ======================================== Step 2: Seed Data ========================================\\n17:22:46 [INFO] depth_0.jsonl already exists with enough samples — skipping\\n17:22:46 [INFO] ======================================== Step 3: Depth Chain ========================================\\n17:22:46 [INFO] Generating depth 1 (5500 docs, batch_size=16) ...\\n\\rdepth 1:   0%|          | 0/344 [00:00<?, ?it/s][transformers] Ignoring clean_up_tokenization_spaces=True for BPE tokenizer GPTNeoXT
…[truncated 6462 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_running_experiments_20260524T095747",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-24T09:59:05.832612+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "tail -30 /root/autodl-tmp/gen-depth-contamination/logs/exp_gemma27b_filtering/run_all.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_running_experiments_20260524T095747",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "tail -30 /root/autodl-tmp/gen-depth-contamination/logs/exp_gemma27b_filtering/run_all.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-24T09:59:05.832835+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"17:54:24 [INFO] Data: /root/autodl-tmp/gen-depth-contamination/data/exp_gemma27b_c4\\n17:54:24 [INFO] Features: /root/autodl-tmp/gen-depth-contamination/data/exp_gemma27b_c4_qwen_scorer/features.csv\\n17:54:24 [INFO] LoRA: rank=4, alpha=8\\n17:54:24 [INFO] Contamination rate: 50%\\n17:54:24 [INFO] ============================================================\\n17:54:25 [INFO] Corpus: 5000 docs, 2500 human, 2500 synthetic\\n17:54:27 [WARNING] Skipping import of cpp extensions due to incompatible torch version. Please upgrade to torch >= 2.11.0 (found 2.8.0+cu128).\\n17:54:29 [INFO] Tokenizing 5000 texts...\\n17:54:32 [INFO] Loading Qwen2.5-1.5B...\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/338 [00:00<?, ?it/s]\\rLoading weights: 100%|██████████| 338/338 [00:00<00:00, 8529.21it/s]\\n17:54:40 [INFO] LoRA r=4: 544,768 trainable / 1,544,259,072 total (0.04%)\\n[transformers] warmup_ratio is deprecated and will be removed in v5.2. Use `warmup_steps` instead.\\n17:54:40 [INFO] Training: 5000 samples, bs=4x4, lr=0.0002, device=cuda:3\\n\\r  0%|          | 0/79 [00:00<?, ?it/s]/root/miniconda3/lib/python3.12/site-packages/torch/nn/parallel/_functions.py:71: UserWarning: Was asked to gather along dimension 0, but all input tensors were scalars; will instead unsqueeze and return a vector.\\n  warnings.warn(\\n\\r  1%|▏         | 1/79 [00:04<05:34,  4.29s/it]\\r  3%|▎         | 2/79 [00:06<04:06,  3.21s/it]\\r  4%|▍         | 3/79 [00:09<03:37,  2.86s/it]\\r  5%|▌         | 4/79 [00:11<03:28,  2.78s/it]\\r  6%|▋         | 5/79 [00:14<03:18,  2.68s/it]\\r  8%|▊         | 6/79 [00:16<03:12,  2.63s/it]\\r  9%|▉         | 7/79 [00:19<03:09,  2.63s/it]\\r 10%|█         | 8/79 [00:22<03:04,  2.60s/it]\\r 11%|█▏        | 9/79 [00:24<03:00,  2.58s/it]\\r 13%|█▎        | 10/79 [00:27<02:58,  2.59s/it]\\r 14%|█▍        | 11/79 [00:29<02:51,  2.52s/it]\\r 15%|█▌        |
…[truncated 5865 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_running_experiments_20260524T095747",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-24T09:59:05.833007+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "ls /root/autodl-tmp/gen-depth-contamination/results/exp_024_arxiv/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_running_experiments_20260524T095747",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "ls /root/autodl-tmp/gen-depth-contamination/results/exp_024_arxiv/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-24T09:59:05.833142+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"feature_importance.json\\njsd.json\\nordinal_results.json\\npairwise_auc.json\\nsummary.txt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_running_experiments_20260524T095747",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-24T09:59:05.833281+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_024_arxiv/summary.txt",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_running_experiments_20260524T095747",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_024_arxiv/summary.txt",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-24T09:59:05.833432+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"============================================================\\nMVP Pilot Saturation Study — Results Summary\\n============================================================\\n\\nPairwise AUC (adjacent depths):\\n  depth 0 vs 1: AUC = 0.9948 ± 0.0008  folds=[0.9956, 0.9955, 0.9938, 0.9938, 0.9952]\\n  depth 1 vs 2: AUC = 0.8581 ± 0.0123  folds=[0.8763, 0.8669, 0.8411, 0.8515, 0.8549]\\n  depth 2 vs 3: AUC = 0.6436 ± 0.0219  folds=[0.6738, 0.6349, 0.6479, 0.6537, 0.6078]\\n  depth 3 vs 4: AUC = 0.544 ± 0.0164  folds=[0.52, 0.5346, 0.5491, 0.5471, 0.5693]\\n  depth 4 vs 5: AUC = 0.5299 ± 0.0242  folds=[0.5517, 0.5419, 0.5413, 0.5312, 0.4832]\\n\\nPairwise JSD (adjacent depths):\\n  depth 0 vs 1: JSD = 0.203016\\n  depth 1 vs 2: JSD = 0.077297\\n  depth 2 vs 3: JSD = 0.019837\\n  depth 3 vs 4: JSD = 0.008281\\n  depth 4 vs 5: JSD = 0.007694\\n\\nK* (max depth with AUC > 0.60): 3\\n\\nOrdinal Classification (6-class, 5-fold CV):\\n  MAE = 0.8256\\n  Accuracy = 0.4767\\n\\nTop-10 Feature Importance:\\n  freq_entropy         9880.4\\n  surp_std             8424.6\\n  surp_mean            7643.0\\n  surp_d1_skew         7490.8\\n  surp_d1_mean         7241.8\\n  freq_kurtosis        7099.2\\n  surp_d1_std          6852.8\\n  surp_d2_mean         6705.8\\n  surp_kurt            6622.4\\n  hapax_ratio          5905.6\\n\\n============================================================\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_running_experiments_20260524T095747",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-24T09:59:05.833570+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_024_arxiv/jsd.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_running_experiments_20260524T095747",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_024_arxiv/jsd.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-24T09:59:05.833726+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"0v1\\\": 0.203016,\\n  \\\"1v2\\\": 0.077297,\\n  \\\"2v3\\\": 0.019837,\\n  \\\"3v4\\\": 0.008281,\\n  \\\"4v5\\\": 0.007694\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.63}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_running_experiments_20260524T095747",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-24T09:59:05.833885+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_024_arxiv/pairwise_auc.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_running_experiments_20260524T095747",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_024_arxiv/pairwise_auc.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-24T09:59:05.834031+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mean\\\": {\\n    \\\"0v1\\\": 0.9948,\\n    \\\"1v2\\\": 0.8581,\\n    \\\"2v3\\\": 0.6436,\\n    \\\"3v4\\\": 0.544,\\n    \\\"4v5\\\": 0.5299\\n  },\\n  \\\"per_fold\\\": {\\n    \\\"0v1\\\": [\\n      0.9956,\\n      0.9955,\\n      0.9938,\\n      0.9938,\\n      0.9952\\n    ],\\n    \\\"1v2\\\": [\\n      0.8763,\\n      0.8669,\\n      0.8411,\\n      0.8515,\\n      0.8549\\n    ],\\n    \\\"2v3\\\": [\\n      0.6738,\\n      0.6349,\\n      0.6479,\\n      0.6537,\\n      0.6078\\n    ],\\n    \\\"3v4\\\": [\\n      0.52,\\n      0.5346,\\n      0.5491,\\n      0.5471,\\n      0.5693\\n    ],\\n    \\\"4v5\\\": [\\n      0.5517,\\n      0.5419,\\n      0.5413,\\n      0.5312,\\n      0.4832\\n    ]\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_running_experiments_20260524T095747",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-24T09:59:05.834158+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "ls /root/autodl-tmp/gen-depth-contamination/results/exp_gemma27b_filtering/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_running_experiments_20260524T095747",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "ls /root/autodl-tmp/gen-depth-contamination/results/exp_gemma27b_filtering/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-24T09:59:05.834281+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"binary_ours_seed42\\ngraduated_a09_seed42\\nno_filter_seed123\\nno_filter_seed42\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_running_experiments_20260524T095747",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-24T09:59:05.834462+00:00_

## 实验状态

- **arxiv_multi_source**: **DONE** | PID 165918 已退出
  - K* = 3（max depth with AUC > 0.60）
  - Pairwise AUC: 0v1=0.9948, 1v2=0.8581, 2v3=0.6436, 3v4=0.544, 4v5=0.5299
  - Pairwise JSD: 0v1=0.203, 1v2=0.077, 2v3=0.020, 3v4=0.008, 4v5=0.008
  - Ordinal 6-class: MAE=0.826, Acc=47.7%
  - Top features: freq_entropy, surp_std, surp_mean

- **code_domain_olmo**: **RUNNING** | 已运行 35min | depth 3 生成中 180/344 batches (52%)
  - depth 0-2 已完成，depth 3 进行中，还剩 depth 4-5
  - 速度 ~3.2s/it，depth 3 剩余约 9min，整体预计还需 ~40-50min

- **gemma27b_filtering**: **RUNNING** | 已运行 11min | 3 strategies × 3 seeds = 9 runs
  - 已完成: no_filter_seed42, binary_ours_seed42, graduated_a09_seed42 (3/9)
  - 进行中: no_filter_seed123（训练完成，eval 加载中）(4/9)
  - 剩余: 5 runs，每 run ~4min，预计还需 ~20-25min

## GPU 状态
```
cuda:0:  36% util | 12,139 / 97,887 MiB  (arxiv 已完成，残留显存或其他进程)
cuda:1:  85% util | 14,308 / 97,887 MiB  (code_domain_olmo 活跃)
cuda:2:  36% util |  8,729 / 97,887 MiB  (无实验，可能有其他进程)
cuda:3:  35% util |  8,729 / 97,887 MiB  (gemma27b_filtering 活跃)
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_check_running_experiments_20260524T095747"
}
```

</details>

---
