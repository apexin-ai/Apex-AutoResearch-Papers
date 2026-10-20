# analysis paper main table compilation

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/chats/worker_analysis_paper-main-table-compilation_20260518T212919.jsonl`
- **Structured JSON:** [`b0ebc45fd9cca32eb19b.json`](../../sessions/b0/b0ebc45fd9cca32eb19b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

25 recorded events

### Tool call

_source line 1 · 2026-05-18T21:34:05.369981+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper-main-table-compilation_20260518T212919",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T21:34:05.370495+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper-main-table-compilation_20260518T212919",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T21:34:05.370736+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'DONE'}",
  "fields": "['*']",
  "limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper-main-table-compilation_20260518T212919",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'DONE'}",
    "fields": "['*']",
    "limit": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-18T21:34:05.371335+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"contamination_60_random_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T08:57:57.040Z\", \"updated_at\": \"2026-05-18T09:01:04.795Z\", \"checkpoint_path\": \"/root/autodl-tmp/output/models/contamination_60_random_seed42/final\", \"log_path\": \"/root/autodl-tmp/output/models/contamination_60_random_seed42/train_resume.log\", \"spec\": {\"command\": \"python train_weighted.py --config configs/contamination_60_random_seed42.yaml (resumed from checkpoint-1000)\", \"server\": \"westd-30476\", \"data_path\": \"data/human/train_contaminated_60.jsonl\", \"data_count\": 23176, \"model_name\": \"Qwen/Qwen2.5-0.5B\", \"seed\": 42}, \"metrics\": {\"eval_ppl_holdout\": 17.832, \"eval_loss_holdout\": 2.881, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048 --stride 1024 --fp16\", \"note\": \"resume from checkpoint-1000 with ~20% LR offset; checkpoint-1000 no longer available (cleaned up)\"}, \"hypothesis\": \"Random (uniform) weighting on 60% contaminated data serves as baseline; without provenance-aware reweighting, the model treats all data equally regardless of contamination level\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T09:01:00.559Z\"}, \"rho02_adaptive_tau09_r5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:11:17.034Z\", \"updated_at\": \"2026-05-17T18:11:55.221Z\", \"hypothesis\": \"Adaptive weighting with τ=0.9 on ρ=0.2 (low contamination): even at 20% contamination, stricter α_eff threshold should find non-trivial b* and outperform uniform, demonstrating proportion-robustness (Claim 3). If adaptive fails here, Claim 3 may need to be scoped to medium-high contamination levels.\", \"spec\": {\"command\": \"bash scripts/run_rho02_adaptive_tau09.sh\", \"server\": \"westd-30476\", \"model_name\": \"Qwen/Qwen3-0.6B\", \"data_path\": \"data/scored_data_rho02.jsonl\", \"data_c
…[truncated 12838 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper-main-table-compilation_20260518T212919",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T21:34:05.371606+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/registry.yaml",
  "description": "Count lines in registry file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper-main-table-compilation_20260518T212919",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/registry.yaml",
    "description": "Count lines in registry file"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T21:34:05.371813+00:00_

6367 /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/registry.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper-main-table-compilation_20260518T212919",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T21:34:05.374189+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport yaml, json\n\nwith open('registry.yaml', 'r') as f:\n    data = yaml.safe_load(f)\n\nexperiments = data.get('experiments', {})\ndone = {}\nfor eid, exp in experiments.items():\n    if exp.get('status') == 'DONE':\n        done[eid] = {\n            'conclusion': exp.get('conclusion'),\n            'metrics': exp.get('metrics', {}),\n            'spec': exp.get('spec', {}),\n        }\n\nprint(f'Total DONE experiments: {len(done)}')\nprint('---')\nfor eid, exp in sorted(done.items()):\n    m = exp['metrics']\n    s = exp['spec']\n    ppl = m.get('eval_ppl_holdout') or m.get('ppl')\n    seed = s.get('seed')\n    method = s.get('weighting_method', '')\n    model = s.get('model_name', '')\n    conc = exp['conclusion']\n    print(f'{eid} | ppl={ppl} | seed={seed} | method={method} | model={model} | conclusion={conc}')\n\" 2>&1",
  "description": "Parse registry.yaml for all DONE experiments",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper-main-table-compilation_20260518T212919",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport yaml, json\n\nwith open('registry.yaml', 'r') as f:\n    data = yaml.safe_load(f)\n\nexperiments = data.get('experiments', {})\ndone = {}\nfor eid, exp in experiments.items():\n    if exp.get('status') == 'DONE':\n        done[eid] = {\n            'conclusion': exp.get('conclusion'),\n            'metrics': exp.get('metrics', {}),\n            'spec': exp.get('spec', {}),\n        }\n\nprint(f'Total DONE experiments: {len(done)}')\nprint('---')\nfor eid, exp in sorted(done.items()):\n    m = exp['metrics']\n    s = exp['spec']\n    ppl = m.get('eval_ppl_holdout') or m.get('ppl')\n    seed = s.get('seed')\n    method = s.get('weighting_method', '')\n    model = s.get('model_name', '')\n    conc = exp['conclusion']\n    print(f'{eid} | ppl={ppl} | seed={seed} | method={method} | model={model} | conclusion={conc}')\n\" 2>&1",
    "description": "Parse registry.yaml for all DONE experiments",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T21:34:05.374556+00:00_

Total DONE experiments: 133
---
adaptive_1_7b_seed42 | ppl=None | seed=None | method= | model= | conclusion=success
adaptive_fix_seed123 | ppl=17.6432 | seed=None | method= | model= | conclusion=success
adaptive_fix_seed42 | ppl=17.6527 | seed=None | method= | model= | conclusion=success
adaptive_fix_seed456 | ppl=17.6566 | seed=None | method= | model= | conclusion=success
adaptive_seed123 | ppl=17.6308 | seed=123 | method= | model=Qwen/Qwen3-0.6B | conclusion=success
adaptive_seed42 | ppl=17.644 | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=success
adaptive_seed456 | ppl=17.6419 | seed=456 | method= | model=Qwen/Qwen3-0.6B | conclusion=success
adaptive_v2_seed123 | ppl=None | seed=None | method= | model= | conclusion=killed
adaptive_v2_seed42 | ppl=None | seed=None | method= | model= | conclusion=killed
adaptive_v2_seed456 | ppl=None | seed=None | method= | model= | conclusion=killed
baseline_qwen3_0.6b | ppl=22.97 | seed=0 | method= | model=Qwen3-0.6B | conclusion=success
batch_adaptive_tau_rho04_seed42 | ppl=17.681 | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=negative
batch_adaptive_tau_rho06_r2 | ppl=None | seed=None | method= | model= | conclusion=failed
batch_adaptive_tau_rho06_r3 | ppl=None | seed=None | method= | model= | conclusion=failed
batch_adaptive_tau_rho06_r5 | ppl=17.73 | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=negative
batch_adaptive_tau_rho06_seed42 | ppl=None | seed=42 | method=batch_adaptive_tau | model=Qwen/Qwen3-0.6B | conclusion=failed
batchsize16_nmin8_r2 | ppl=None | seed=None | method= | model= | conclusion=killed
batchsize16_nmin8_r3 | ppl=17.65 | seed=42 | method=adaptive | model=Qwen/Qwen3-0.6B | conclusion=success
batchsize16_nmin8_seed42 | ppl=None | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=failed
bs8_auto_nmin_r2 | ppl=None | seed=None | method= | model= | conclusion=failed
bs8_auto_nmin_r3 | ppl=None | seed=None | method= | model= | conclusion=failed
bs8_auto_nmin_r5 | ppl=17.66 | 
…[truncated 10644 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper-main-table-compilation_20260518T212919",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T21:34:05.374902+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport yaml, json\n\nwith open('registry.yaml', 'r') as f:\n    data = yaml.safe_load(f)\n\nexperiments = data.get('experiments', {})\n\n# Experiments we need full details for\nneed_details = [\n    'adaptive_1_7b_seed42', 'uniform_1_7b_seed42',\n    'ngram_adaptive_seed42', 'ngram_uniform_seed42',\n    'ess_only_seed42', 'grid_b_seed42_batch',\n    'contamination_60_grid_b0_5_seed42',\n    'llama3b_adaptive_seed42', 'llama3b_uniform_seed42',\n    'detect_remove_baseline_seed42', 'detect_remove_q05_seed123', 'detect_remove_q05_seed456',\n    'detect_remove_q05_epoch_matched_seed42', 'detect_remove_q07_seed42', 'detect_remove_q09_seed42',\n    'threshold_q03_seed42',\n    'adaptive_fix_seed42', 'adaptive_fix_seed123', 'adaptive_fix_seed456',\n    'detector_tfidf_lr',\n    'golden_ratio_seed42', 'nmin1_seed42', 'nmin4_seed42',\n    'hybrid_rho04_seed42', 'hybrid_rho06_seed42',\n    'rho02_uniform_seed42', 'rho02_adaptive_tau08_seed42',\n    'batchsize16_nmin8_r3',\n    'qwen06b_uniform_seed42',\n    'grid_b0_3_seed42',\n    'baseline_qwen3_0.6b',\n]\n\nfor eid in need_details:\n    exp = experiments.get(eid)\n    if exp:\n        m = exp.get('metrics', {})\n        s = exp.get('spec', {})\n        print(f'=== {eid} ===')\n        print(f'  conclusion: {exp.get(\\\"conclusion\\\")}')\n        print(f'  spec: seed={s.get(\\\"seed\\\")}, model={s.get(\\\"model_name\\\")}, method={s.get(\\\"weighting_method\\\")}, data={s.get(\\\"data_path\\\")}, b_star={s.get(\\\"b_star\\\")}')\n        print(f'  metrics: {json.dumps(m, indent=None)}')\n        print()\n    else:\n        print(f'=== {eid} === NOT FOUND')\n        print()\n\" 2>&1",
  "description": "Get full details for key experiments",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper-main-table-compilation_20260518T212919",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport yaml, json\n\nwith open('registry.yaml', 'r') as f:\n    data = yaml.safe_load(f)\n\nexperiments = data.get('experiments', {})\n\n# Experiments we need full details for\nneed_details = [\n    'adaptive_1_7b_seed42', 'uniform_1_7b_seed42',\n    'ngram_adaptive_seed42', 'ngram_uniform_seed42',\n    'ess_only_seed42', 'grid_b_seed42_batch',\n    'contamination_60_grid_b0_5_seed42',\n    'llama3b_adaptive_seed42', 'llama3b_uniform_seed42',\n    'detect_remove_baseline_seed42', 'detect_remove_q05_seed123', 'detect_remove_q05_seed456',\n    'detect_remove_q05_epoch_matched_seed42', 'detect_remove_q07_seed42', 'detect_remove_q09_seed42',\n    'threshold_q03_seed42',\n    'adaptive_fix_seed42', 'adaptive_fix_seed123', 'adaptive_fix_seed456',\n    'detector_tfidf_lr',\n    'golden_ratio_seed42', 'nmin1_seed42', 'nmin4_seed42',\n    'hybrid_rho04_seed42', 'hybrid_rho06_seed42',\n    'rho02_uniform_seed42', 'rho02_adaptive_tau08_seed42',\n    'batchsize16_nmin8_r3',\n    'qwen06b_uniform_seed42',\n    'grid_b0_3_seed42',\n    'baseline_qwen3_0.6b',\n]\n\nfor eid in need_details:\n    exp = experiments.get(eid)\n    if exp:\n        m = exp.get('metrics', {})\n        s = exp.get('spec', {})\n        print(f'=== {eid} ===')\n        print(f'  conclusion: {exp.get(\\\"conclusion\\\")}')\n        print(f'  spec: seed={s.get(\\\"seed\\\")}, model={s.get(\\\"model_name\\\")}, method={s.get(\\\"weighting_method\\\")}, data={s.get(\\\"data_path\\\")}, b_star={s.get(\\\"b_star\\\")}')\n        print(f'  metrics: {json.dumps(m, indent=None)}')\n        print()\n    else:\n        print(f'=== {eid} === NOT FOUND')\n        print()\n\" 2>&1",
    "description": "Get full details for key experiments",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T21:34:05.375324+00:00_

=== adaptive_1_7b_seed42 ===
  conclusion: success
  spec: seed=None, model=None, method=None, data=None, b_star=None
  metrics: {}

=== uniform_1_7b_seed42 ===
  conclusion: failed
  spec: seed=None, model=None, method=None, data=None, b_star=None
  metrics: {}

=== ngram_adaptive_seed42 ===
  conclusion: success
  spec: seed=None, model=None, method=None, data=None, b_star=None
  metrics: {}

=== ngram_uniform_seed42 ===
  conclusion: success
  spec: seed=None, model=None, method=None, data=None, b_star=None
  metrics: {}

=== ess_only_seed42 ===
  conclusion: success
  spec: seed=None, model=None, method=ess_only, data=None, b_star=None
  metrics: {"eval_ppl": 17.73, "eval_loss": 2.875, "b_star_median": 1.58, "b_star_mean": 3.51, "vs_uniform_ppl_delta": "+0.038", "vs_adaptive_ppl_delta": "+0.08"}

=== grid_b_seed42_batch ===
  conclusion: success
  spec: seed=42, model=Qwen/Qwen3-0.6B, method=None, data=/root/provenance_weight_training/data/scored_data.jsonl, b_star=None
  metrics: {"b_values": [0.5, 1, 1.5, 2, 3, 5], "b0_5_train_loss": 9.598, "b0_5_completed": true, "b1_0_completed": true, "b1_5_completed": true, "b2_0_current_step": 5149, "b2_0_total_steps": 6103, "completed_b_values": [0.5, 1, 1.5, 2, 3], "current_b": 5, "total_steps": 6103, "current_step": 3422, "b5_0_progress_pct": 56, "eta_minutes": 95, "b2_0_completed": true, "b2_0_train_loss": 10.621, "b2_0_train_runtime_s": 13034, "b3_0_completed": true, "b3_0_train_loss": 10.754, "b3_0_train_runtime_s": 13036, "all_completed": true, "b1_0_train_loss": 10.223, "b1_5_train_loss": 10.485, "b5_0_train_loss": 10.858, "b0_5_runtime_s": 13036, "b1_0_runtime_s": 12968, "b1_5_runtime_s": 14789, "b2_0_runtime_s": 13034, "b3_0_runtime_s": 13036, "b5_0_runtime_s": 13115, "note": "eval_ppl missing - no --eval_data_path in batch script, post-hoc eval pending", "b0_5_eval_ppl": 17.651, "b1_0_eval_ppl": 17.692, "b1_5_eval_ppl": 17.718, "b2_0_eval_ppl": 17.741, "b3_0_eval_ppl": 17.774, "b5_0_eval_ppl": 17.818, "eval_hol
…[truncated 11179 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper-main-table-compilation_20260518T212919",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T21:34:05.375616+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport yaml, json\n\nwith open('registry.yaml', 'r') as f:\n    data = yaml.safe_load(f)\n\nexperiments = data.get('experiments', {})\n\n# Get more details\nneed = ['adaptive_1_7b_seed42', 'uniform_1_7b_seed42', 'ngram_adaptive_seed42', 'ngram_uniform_seed42',\n        'ess_only_seed42', 'ess_only_seed123', 'ess_only_seed123_r2', 'ess_only_seed456', 'ess_only_seed456_r2',\n        'contamination_60_uniform_seed42', 'contamination_60_seed123', 'contamination_60_seed42_r2',\n        'contamination_60_adaptive_seed456',\n        'adaptive_seed42', 'adaptive_seed123', 'adaptive_seed456',\n        'random_reweight_v2_seed42', 'random_reweight_seed456',\n        'llama3b_adaptive_seed42', 'llama3b_uniform_seed42']\n\nfor eid in need:\n    exp = experiments.get(eid, {})\n    print(f'=== {eid} ===')\n    print(json.dumps(exp, indent=2, default=str))\n    print()\n\" 2>&1 | head -500",
  "description": "Get full YAML entries for remaining experiments",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper-main-table-compilation_20260518T212919",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport yaml, json\n\nwith open('registry.yaml', 'r') as f:\n    data = yaml.safe_load(f)\n\nexperiments = data.get('experiments', {})\n\n# Get more details\nneed = ['adaptive_1_7b_seed42', 'uniform_1_7b_seed42', 'ngram_adaptive_seed42', 'ngram_uniform_seed42',\n        'ess_only_seed42', 'ess_only_seed123', 'ess_only_seed123_r2', 'ess_only_seed456', 'ess_only_seed456_r2',\n        'contamination_60_uniform_seed42', 'contamination_60_seed123', 'contamination_60_seed42_r2',\n        'contamination_60_adaptive_seed456',\n        'adaptive_seed42', 'adaptive_seed123', 'adaptive_seed456',\n        'random_reweight_v2_seed42', 'random_reweight_seed456',\n        'llama3b_adaptive_seed42', 'llama3b_uniform_seed42']\n\nfor eid in need:\n    exp = experiments.get(eid, {})\n    print(f'=== {eid} ===')\n    print(json.dumps(exp, indent=2, default=str))\n    print()\n\" 2>&1 | head -500",
    "description": "Get full YAML entries for remaining experiments",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T21:34:05.378206+00:00_

=== adaptive_1_7b_seed42 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-18T11:47:25.251Z",
  "updated_at": "2026-05-18T19:07:03.284Z",
  "hypothesis": "Scale validation: adaptive provenance weighting on Qwen3-1.7B (2.8x larger than 0.6B). If adaptive still outperforms uniform at 1.7B scale, demonstrates method generality beyond small models. Key for Main conference upgrade (D079 Line B). Expected: adaptive < uniform by \u22650.03 PPL (consistent with 0.6B gap).",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/bin/activate && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --model_name models/Qwen/Qwen3-1.7B --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/adaptive_1_7b_seed42 --weighting_method adaptive --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --resume_from_checkpoint /root/autodl-tmp/provenance_weight_training/output/models/adaptive_1_7b_seed42/checkpoint-2500\"",
    "server": "westd-41312",
    "gpu": [
      "cuda:1"
    ],
    "pid": "226766",
    "log_path": "~/runs/provenance_weight_training/adaptive_1_7b_seed42.log",
    "submitted_at": "2026-05-18T15:00:59.483Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "checkpoint_path": "/root/autodl-tmp/provenance_weight_training/output/models/adaptive_1_7b_seed42/final",
    "train_loss": 5.36,
    "train_runtime_s": 10990,
    "total_steps": 6103,
    "wall_clock_seconds": 14763.8,
    "gpu_hours": 4.1
  },
  "conclusion": "success",
  "completed_at": "2026-05-18T19:07:03.284Z"
}

=== uniform_1_7b_seed42 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-18T11:47:26.566Z",
  "updated_at": "2026-05-18T15:45:29.875Z",
…[truncated 22059 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper-main-table-compilation_20260518T212919",
  "tool": "Bash",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T21:34:05.378568+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport yaml, json\n\nwith open('registry.yaml', 'r') as f:\n    data = yaml.safe_load(f)\n\nexperiments = data.get('experiments', {})\n\nneed = ['contamination_60_seed42_r2', 'contamination_60_adaptive_seed456',\n        'contamination_60_random_seed42', 'contamination_60_random_seed123', 'contamination_60_random_seed456',\n        'contamination_60_ess_only_seed42', 'contamination_60_ess_only_seed123', 'contamination_60_ess_only_seed456',\n        'contamination_60_uniform_seed123', 'contamination_60_uniform_seed456',\n        'adaptive_seed42', 'adaptive_seed123', 'adaptive_seed456',\n        'random_reweight_v2_seed42', 'random_reweight_seed456', 'random_reweight_seed123_r5',\n        'grid_b0_5_seed123', 'grid_b0_5_seed456',\n        'tau_05_seed42', 'tau_06_seed42', 'tau_07_seed42', 'tau_095_seed42', 'tau_09_seed42',\n        'contamination_60_tau06_seed42', 'contamination_60_tau07_seed42',\n        'detect_remove_q03_seed42',\n        ]\n\nfor eid in need:\n    exp = experiments.get(eid, {})\n    if not exp:\n        print(f'=== {eid} === NOT FOUND')\n        continue\n    m = exp.get('metrics', {})\n    s = exp.get('spec', {})\n    print(f'{eid} | conclusion={exp.get(\\\"conclusion\\\")} | ppl={m.get(\\\"eval_ppl_holdout\\\") or m.get(\\\"ppl\\\") or m.get(\\\"eval_ppl\\\")} | seed={s.get(\\\"seed\\\")} | method={s.get(\\\"weighting_method\\\")}')\n    # Print select metrics\n    if m:\n        keys = ['eval_ppl_holdout', 'ppl', 'eval_ppl', 'lm_eval_mmlu_5shot', 'vs_uniform_ppl_delta']\n        for k in keys:\n            if k in m:\n                print(f'  {k}: {m[k]}')\n    print()\n\" 2>&1",
  "description": "Get remaining experiment PPL values",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper-main-table-compilation_20260518T212919",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport yaml, json\n\nwith open('registry.yaml', 'r') as f:\n    data = yaml.safe_load(f)\n\nexperiments = data.get('experiments', {})\n\nneed = ['contamination_60_seed42_r2', 'contamination_60_adaptive_seed456',\n        'contamination_60_random_seed42', 'contamination_60_random_seed123', 'contamination_60_random_seed456',\n        'contamination_60_ess_only_seed42', 'contamination_60_ess_only_seed123', 'contamination_60_ess_only_seed456',\n        'contamination_60_uniform_seed123', 'contamination_60_uniform_seed456',\n        'adaptive_seed42', 'adaptive_seed123', 'adaptive_seed456',\n        'random_reweight_v2_seed42', 'random_reweight_seed456', 'random_reweight_seed123_r5',\n        'grid_b0_5_seed123', 'grid_b0_5_seed456',\n        'tau_05_seed42', 'tau_06_seed42', 'tau_07_seed42', 'tau_095_seed42', 'tau_09_seed42',\n        'contamination_60_tau06_seed42', 'contamination_60_tau07_seed42',\n        'detect_remove_q03_seed42',\n        ]\n\nfor eid in need:\n    exp = experiments.get(eid, {})\n    if not exp:\n        print(f'=== {eid} === NOT FOUND')\n        continue\n    m = exp.get('metrics', {})\n    s = exp.get('spec', {})\n    print(f'{eid} | conclusion={exp.get(\\\"conclusion\\\")} | ppl={m.get(\\\"eval_ppl_holdout\\\") or m.get(\\\"ppl\\\") or m.get(\\\"eval_ppl\\\")} | seed={s.get(\\\"seed\\\")} | method={s.get(\\\"weighting_method\\\")}')\n    # Print select metrics\n    if m:\n        keys = ['eval_ppl_holdout', 'ppl', 'eval_ppl', 'lm_eval_mmlu_5shot', 'vs_uniform_ppl_delta']\n        for k in keys:\n            if k in m:\n                print(f'  {k}: {m[k]}')\n    print()\n\" 2>&1",
    "description": "Get remaining experiment PPL values",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T21:34:05.378873+00:00_

contamination_60_seed42_r2 | conclusion=success | ppl=17.74 | seed=None | method=None
  eval_ppl_holdout: 17.74

contamination_60_adaptive_seed456 | conclusion=success | ppl=17.735 | seed=456 | method=None
  eval_ppl_holdout: 17.735

contamination_60_random_seed42 | conclusion=success | ppl=17.832 | seed=42 | method=None
  eval_ppl_holdout: 17.832

contamination_60_random_seed123 | conclusion=success | ppl=17.87 | seed=123 | method=None
  eval_ppl_holdout: 17.87

contamination_60_random_seed456 | conclusion=success | ppl=17.88 | seed=456 | method=None
  eval_ppl_holdout: 17.88

contamination_60_ess_only_seed42 | conclusion=success | ppl=17.77 | seed=42 | method=None
  eval_ppl_holdout: 17.77

contamination_60_ess_only_seed123 | conclusion=success | ppl=17.763 | seed=123 | method=None
  eval_ppl_holdout: 17.763

contamination_60_ess_only_seed456 | conclusion=success | ppl=17.762 | seed=456 | method=None
  eval_ppl_holdout: 17.762

contamination_60_uniform_seed123 | conclusion=success | ppl=17.754 | seed=123 | method=None
  eval_ppl_holdout: 17.754

contamination_60_uniform_seed456 | conclusion=success | ppl=17.77 | seed=456 | method=None
  eval_ppl_holdout: 17.77

adaptive_seed42 | conclusion=success | ppl=17.644 | seed=42 | method=None
  eval_ppl_holdout: 17.644

adaptive_seed123 | conclusion=success | ppl=17.6308 | seed=123 | method=None
  eval_ppl_holdout: 17.6308

adaptive_seed456 | conclusion=success | ppl=17.6419 | seed=456 | method=None
  eval_ppl_holdout: 17.6419

random_reweight_v2_seed42 | conclusion=success | ppl=17.83 | seed=42 | method=random
  eval_ppl_holdout: 17.83

random_reweight_seed456 | conclusion=success | ppl=17.777 | seed=None | method=None
  eval_ppl_holdout: 17.777

random_reweight_seed123_r5 | conclusion=success | ppl=17.8 | seed=123 | method=None
  eval_ppl_holdout: 17.8

grid_b0_5_seed123 | conclusion=success | ppl=17.638 | seed=123 | method=None
  eval_ppl_holdout: 17.638

grid_b0_5_seed456 | conclusion=success | ppl=17.65 | seed=456 | m
…[truncated 860 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper-main-table-compilation_20260518T212919",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-18T21:34:05.379248+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport yaml, json\n\nwith open('registry.yaml', 'r') as f:\n    data = yaml.safe_load(f)\n\nexperiments = data.get('experiments', {})\n\n# Look for gpt2 detector experiments\nfor eid, exp in experiments.items():\n    if 'gpt2' in eid.lower() or 'gpt-2' in eid.lower():\n        m = exp.get('metrics', {})\n        print(f'{eid} | status={exp.get(\\\"status\\\")} | conclusion={exp.get(\\\"conclusion\\\")} | metrics={json.dumps(m)}')\n        \nprint()\nprint('--- RUNNING experiments ---')\nfor eid, exp in experiments.items():\n    if exp.get('status') == 'RUNNING':\n        s = exp.get('spec', {})\n        print(f'{eid} | method={s.get(\\\"weighting_method\\\")} | model={s.get(\\\"model_name\\\")} | data={s.get(\\\"data_path\\\")}')\n\n# Also check llama reeval details\nprint()\nprint('--- llama3b API reeval data (from earlier API call) ---')\nprint('llama3b_adaptive_seed42: PPL=10.58, MMLU=53.42%, HellaSwag=72.49%')\nprint('llama3b_uniform_seed42: PPL=10.53, MMLU=51.85%')\nprint('(reeval_v2: unified eval params, 4017316 tokens)')\n\" 2>&1",
  "description": "Check GPT-2 and running experiments",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper-main-table-compilation_20260518T212919",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport yaml, json\n\nwith open('registry.yaml', 'r') as f:\n    data = yaml.safe_load(f)\n\nexperiments = data.get('experiments', {})\n\n# Look for gpt2 detector experiments\nfor eid, exp in experiments.items():\n    if 'gpt2' in eid.lower() or 'gpt-2' in eid.lower():\n        m = exp.get('metrics', {})\n        print(f'{eid} | status={exp.get(\\\"status\\\")} | conclusion={exp.get(\\\"conclusion\\\")} | metrics={json.dumps(m)}')\n        \nprint()\nprint('--- RUNNING experiments ---')\nfor eid, exp in experiments.items():\n    if exp.get('status') == 'RUNNING':\n        s = exp.get('spec', {})\n        print(f'{eid} | method={s.get(\\\"weighting_method\\\")} | model={s.get(\\\"model_name\\\")} | data={s.get(\\\"data_path\\\")}')\n\n# Also check llama reeval details\nprint()\nprint('--- llama3b API reeval data (from earlier API call) ---')\nprint('llama3b_adaptive_seed42: PPL=10.58, MMLU=53.42%, HellaSwag=72.49%')\nprint('llama3b_uniform_seed42: PPL=10.53, MMLU=51.85%')\nprint('(reeval_v2: unified eval params, 4017316 tokens)')\n\" 2>&1",
    "description": "Check GPT-2 and running experiments",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T21:34:05.379514+00:00_

gpt2_adaptive_seed42 | status=PREPARING | conclusion=None | metrics={}
gpt2_uniform_seed42 | status=PREPARING | conclusion=None | metrics={}

--- RUNNING experiments ---
detect_remove_q01_seed42 | method=None | model=Qwen/Qwen3-0.6B | data=data/scored_data_filtered_q01.jsonl
eval_uniform_1_7b_v3 | method=None | model=Qwen3-1.7B (uniform) | data=data/human/eval_holdout.jsonl
eval_adaptive_1_7b_v2 | method=None | model=Qwen3-1.7B (adaptive) | data=data/human/eval_holdout.jsonl
detect_remove_q08_seed42 | method=None | model=Qwen/Qwen3-0.6B | data=data/scored_data_filtered_q08.jsonl
adaptive_1_7b_seed123 | method=None | model=Qwen/Qwen3-1.7B | data=data/scored_data.jsonl

--- llama3b API reeval data (from earlier API call) ---
llama3b_adaptive_seed42: PPL=10.58, MMLU=53.42%, HellaSwag=72.49%
llama3b_uniform_seed42: PPL=10.53, MMLU=51.85%
(reeval_v2: unified eval params, 4017316 tokens)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper-main-table-compilation_20260518T212919",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-18T21:34:05.379790+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper-main-table-compilation_20260518T212919",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T21:34:05.382139+00:00_

_project
ablation_summary.csv
adaptive_fix_seed42
all_success_summary.md
alpha_eff_analysis.json
alpha_eff_batch_size_sweep.json
alpha_eff_binding_rate_rho_comparison.pdf
alpha_eff_binding_rate_rho_comparison.png
analyze_tau_sweep.py
binding_diagnosis_rho06_vs_04.md
bootstrap_test.py
bstar_distribution_analysis.md
bstar_distribution_rho_comparison.pdf
bstar_distribution_rho_comparison.png
bstar_trajectory_adaptive_fix.pdf
convergence_speed_comparison.pdf
convergence_speed_comparison.png
data_generation
detector
diag_contamination_60_random_seed42.md
diagnose_batchsize16_nmin8_seed42.md
diagnosis_exit127_20260518.md
diagnosis_threshold_q03_seed42.md
diagnosis_westd41312_failures.md
drayson_comparison.md
dream_reports
dynamics
ess_only_analysis_template.md
ess_only_implementation.md
ess_only_seed42
evaluation
experiment_data.csv
experiment_results_summary.csv
experiment_results_summary.md
experiment_setup_draft.md
experiment_status_summary.md
experiment_summary.md
experiment_summary_table.md
experiment_tables.md
fig_b_landscape.csv
fig_contamination_comparison.csv
fig_method_comparison.csv
fig_nmin_ablation.csv
fig_tau_sweep.csv
figures
full_experiment_data.md
full_results_summary.csv
full_results_summary.md
generate_full_results.py
grid_b5_0_seed123
grid_b_shift.csv
grid_b_trend_stats.json
grid_eval_source_audit.md
interim_mvp_analysis.md
literature_diff_drayson.md
literature_notes.md
literature_scan_20260516.md
literature_scan_results.md
literature_tau_sensitivity.md
manifest.yaml
mechanism_decomposition_stats.json
method_section_draft.md
metrics_summary.csv
metrics_summary.md
mvp_analysis_draft.md
mvp_analysis_summary.md
new_scripts_manifest.md
nmin1_seed42
novelty_drayson_analysis.md
paper_tables.md
paper_tables_data.md
plot_training_dynamics.py
q1_ess_equivalence_analysis.md
related_work_notes.md
report_tables.md
results_table_ablation.csv
results_table_contamination.csv
results_table_grid_b_curve.csv
results_table_main.csv
review_issues.yaml
review_reports
rho06
…[truncated 769 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper-main-table-compilation_20260518T212919",
  "tool": "Bash",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-18T21:34:05.382453+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/paper_main_table_data.md",
  "content": "# Paper Main Table Data — Compiled 2026-05-18\n\nAll PPL values are `eval_ppl_holdout` on `data/human/eval_holdout.jsonl` (sliding window, stride=1024, max_docs=5000, fp16, ~4.08M tokens).\n\nPretrained baseline (no continued training): **Qwen3-0.6B = 22.97** (`baseline_qwen3_0.6b`)\n\n---\n\n## Table 1: Main Results (ρ=0.4, Qwen3-0.6B)\n\n| Method | Seed 42 | Seed 123 | Seed 456 | Mean | Δ vs Uniform |\n|--------|---------|----------|----------|------|-------------|\n| Uniform | 17.6939 (`uniform_seed42`) | 17.6861 (`uniform_seed123`) | 17.7015 (`uniform_seed456`) | 17.694 | — |\n| **Adaptive (fix)** | 17.6527 (`adaptive_fix_seed42`) | 17.6432 (`adaptive_fix_seed123`) | 17.6566 (`adaptive_fix_seed456`) | **17.651** | **-0.043** |\n| ESS-only | 17.73 (`ess_only_seed42`) | 17.72 (`ess_only_seed123`) | 17.76 (`ess_only_seed456`) | 17.737 | +0.043 |\n| Random reweight | 17.83 (`random_reweight_v2_seed42`) | 17.801 (`random_reweight_seed123_r5`) | 17.777 (`random_reweight_seed456`) | 17.803 | +0.109 |\n\n**Notes:**\n- \"Adaptive (fix)\" = dual-constraint min-intervention (τ=0.8, n_min=2). Used as reference in all cross-experiment comparisons.\n- Earlier \"adaptive_seed{42,123,456}\" runs produced slightly better PPL (17.644/17.631/17.642, mean=17.639), but adaptive_fix is the canonical version referenced throughout.\n- ESS-only = max-intervention (b* = max{b : ESS(b) ≥ n_min}), ignores α_eff quality constraint.\n- Random reweight = random (non-provenance) weights applied to samples.\n- Random > Uniform > ESS-only > Adaptive confirms detector signal is load-bearing.\n\n---\n\n## Table 2: Grid-b Sweep (ρ=0.4, Qwen3-0.6B)\n\n### Seed 42 (from `grid_b_seed42_batch` + individual runs)\n\n| b | PPL | exp_id |\n|---|-----|--------|\n| 0.1 | 17.657 | `grid_b0_1_seed42` |\n| 0.2 | 17.64 | `grid_b0_2_seed42` |\n| 0.3 | 17.64 | `grid_b0_3_seed42` |\n| 0.5 | 17.651 | `grid_b_seed42_batch` (b0.5) |\n| 1.0 | 17.692 | `grid_b_seed42_batch` (b1.0) |\n| 1.5 | 17.718 | `grid_b_seed42_batch` (b1.5) |\n| 2.0 | 17.741 | `grid_b_seed42_batch` (b2.0) |\n| 3.0 | 17.774 | `grid_b_seed42_batch` (b3.0) |\n| 5.0 | 17.818 | `grid_b_seed42_batch` (b5.0) |\n\n### Multi-seed (seed 123 & 456)\n\n| b | Seed 123 | Seed 456 | exp_ids |\n|---|----------|----------|---------|\n| 0.1 | 17.646 | 17.663 | `grid_b0_1_seed{123,456}` |\n| 0.2 | 17.637 | 17.645 | `grid_b0_2_seed{123,456}` |\n| 0.3 | 17.579 | 17.64 | `grid_b0_3_seed123_r2`, `grid_b0_3_seed456_r2` |\n| 0.5 | 17.638 | 17.65 | `grid_b0_5_seed{123,456}` |\n| 1.0 | 17.674 | 17.68 | `grid_b1_0_seed{123,456}` |\n| 1.5 | 17.701 | 17.71 | `grid_b1_5_seed{123,456}` |\n| 2.0 | 17.725 | 17.989 | `grid_b2_0_seed{123,456}` |\n| 3.0 | 17.76 | 17.921 | `grid_b3_0_seed{123,456}` |\n| 5.0 | 17.804 | 17.993 | `grid_b5_0_seed{123,456}` |\n\n**Notes:**\n- grid_b0_3_seed123_r2 = 17.579 is an outlier (lowest in entire sweep). Verify before using.\n- grid_b2_0_seed456 = 17.989 and grid_b3_0_seed456 = 17.921 are outliers (much higher than seed123). May indicate training instability at high b.\n- Best grid-b ≈ 0.2-0.3, consistent with adaptive b* median ≈ 0.88.\n- Adaptive PPL (17.651) matches grid-best region, validating auto-tuning (Claim 2).\n\n---\n\n## Table 3: Detect & Remove (D&R) Threshold Sensitivity (ρ=0.4, seed=42)\n\n| Threshold | PPL | Data Retained | Training | exp_id |\n|-----------|-----|---------------|----------|--------|\n| q=0.3 | 17.253 | ~70% (remove top 30%) | Multi-epoch | `threshold_q03_seed42` |\n| q=0.5 | 17.29 | ~50% (remove top 50%) | Multi-epoch | `detect_remove_baseline_seed42` |\n| q=0.5 (epoch-matched) | 17.65 | ~50% | Single pass | `detect_remove_q05_epoch_matched_seed42` |\n| q=0.7 | 17.32 | ~30% retained | Multi-epoch | `detect_remove_q07_seed42` |\n| q=0.9 | 17.42 | ~10% retained | Multi-epoch | `detect_remove_q09_seed42` |\n\n**Multi-seed D&R q=0.5 (multi-epoch):**\n\n| Seed | PPL | exp_id |\n|------|-----|--------|\n| 42 | 17.29 | `detect_remove_baseline_seed42` |\n| 123 | 17.27 | `detect_remove_q05_seed123` |\n| 456 | 17.28 | `detect_remove_q05_seed456` |\n| Mean | **17.28** | |\n\n**Epoch-matched D&R q=0.5:**\n\n| Seed | PPL | exp_id |\n|------|-----|--------|\n| 42 | 17.65 | `detect_remove_q05_epoch_matched_seed42` |\n| 123 | 17.66 | `epoch_matched_dr_seed123` |\n| 456 | 17.66 | `epoch_matched_dr_seed456` |\n| Mean | **17.66** | |\n\n**Notes:**\n- D&R multi-epoch PPL is much lower (17.28) but trains multiple epochs on filtered clean data.\n- Epoch-matched D&R (17.66) is comparable to Adaptive (17.651), confirming advantage is from multi-epoch, not filtering.\n- D&R discards data; Adaptive retains all data with reweighting.\n- **RUNNING:** q=0.1 (`detect_remove_q01_seed42`), q=0.8 (`detect_remove_q08_seed42`)\n\n---\n\n## Table 4: Contamination Rate (ρ) Sensitivity\n\n### ρ=0.2 (seed=42 only)\n\n| Method | PPL | exp_id | Note |\n|--------|-----|--------|------|\n| Uniform | 17.336 | `rho02_uniform_seed42` | |\n| Adaptive (τ=0.8) | 17.382 | `rho02_adaptive_tau08_seed42` | **NEGATIVE** (+0.046) |\n| Adaptive (τ=0.9) | 17.45 | `rho02_adaptive_tau09_r5` | **NEGATIVE** (+0.114) |\n\n### ρ=0.4 (3 seeds)\n\n| Method | Seed 42 | Seed 123 | Seed 456 | Mean |\n|--------|---------|----------|----------|------|\n| Uniform | 17.694 | 17.686 | 17.702 | 17.694 |\n| Adaptive | 17.653 | 17.643 | 17.657 | 17.651 |\n| Δ | -0.041 | -0.043 | -0.045 | **-0.043** |\n\n### ρ=0.6 (3 seeds)\n\n| Method | Seed 42 | Seed 123 | Seed 456 | Mean |\n|--------|---------|----------|----------|------|\n| Uniform | 17.766 (`contamination_60_uniform_seed42`) | 17.754 (`contamination_60_uniform_seed123`) | 17.770 (`contamination_60_uniform_seed456`) | 17.763 |\n| Adaptive | 17.740 (`contamination_60_seed42_r2`) | 17.732 (`contamination_60_seed123`) | 17.735 (`contamination_60_adaptive_seed456`) | 17.736 |\n| Δ | -0.026 | -0.022 | -0.035 | **-0.028** |\n\n### ρ=0.6 Additional Methods\n\n| Method | Seed 42 | Seed 123 | Seed 456 | Mean |\n|--------|---------|----------|----------|------|\n| ESS-only | 17.77 | 17.763 | 17.762 | 17.765 |\n| Random | 17.832 | 17.87 | 17.88 | 17.861 |\n| Hybrid (filter+reweight) | 17.53 (`hybrid_rho06_seed42`) | — | — | 17.53 |\n| Grid b=0.3 | 17.634 (`contamination_60_grid_b0_3_seed42`) | — | — | |\n| Grid b=0.5 | 17.704 (`contamination_60_grid_b0_5_seed42`) | — | — | |\n\nexp_ids for ρ=0.6 ESS-only: `contamination_60_ess_only_seed{42,123,456}`\nexp_ids for ρ=0.6 Random: `contamination_60_random_seed{42,123,456}`\n\n**Summary:**\n- ρ=0.2: Adaptive HURTS (data already clean, reweighting over-penalizes)\n- ρ=0.4: Adaptive improves by -0.043 PPL (consistent across seeds)\n- ρ=0.6: Adaptive improves by -0.028 PPL (smaller gap, consistent across seeds)\n- Hybrid (filter q>0.95 + reweight) at ρ=0.6 achieves 17.53 (best), but single-seed only\n- ρ=0.4 also has hybrid: 17.514 (`hybrid_rho04_seed42`) — also single-seed\n\n---\n\n## Table 5: Multi-Detector Validation (ρ=0.4, seed=42, Qwen3-0.6B)\n\n| Detector | Adaptive PPL | Uniform PPL | Δ | exp_ids |\n|----------|-------------|-------------|---|---------|\n| TF-IDF+LR (q_score, AUC=0.939) | 17.653 | 17.694 | -0.041 | `adaptive_fix_seed42` / `uniform_seed42` |\n| N-gram PPL (AUC=0.73) | **NO EVAL** | **NO EVAL** | — | `ngram_adaptive_seed42` / `ngram_uniform_seed42` |\n| GPT-2 PPL | **NOT STARTED** | **NOT STARTED** | — | `gpt2_adaptive_seed42` / `gpt2_uniform_seed42` (PREPARING) |\n\n**Notes:**\n- N-gram experiments completed training but eval PPL not yet computed. Models saved at:\n  - `/root/autodl-tmp/provenance_weight_training/output/models/ngram_adaptive_seed42/final`\n  - `/root/autodl-tmp/provenance_weight_training/output/models/ngram_uniform_seed42/final`\n- GPT-2 detector experiments still in PREPARING status.\n\n---\n\n## Table 6: Model Scale — Qwen3-1.7B (ρ=0.4, seed=42)\n\n| Method | PPL | exp_id | Status |\n|--------|-----|--------|--------|\n| Adaptive | **EVAL RUNNING** | `adaptive_1_7b_seed42` | Training done, eval in progress (`eval_adaptive_1_7b_v2`) |\n| Uniform | **EVAL RUNNING** | `uniform_1_7b_seed42` | Training FAILED (checkpoint issue); eval running on available checkpoint (`eval_uniform_1_7b_v3`) |\n\n**Notes:**\n- uniform_1_7b_seed42 training failed due to FileNotFoundError on checkpoint-3000/trainer_state.json during resume.\n- Eval is running on whatever checkpoint exists.\n- adaptive_1_7b_seed123 is also RUNNING (additional seed).\n\n---\n\n## Table 7: Cross-Architecture — Llama-3.2-3B (ρ=0.4, seed=42)\n\n| Method | PPL | MMLU (5-shot) | HellaSwag (10-shot) | exp_id |\n|--------|-----|---------------|---------------------|--------|\n| Uniform | 10.53 | 51.85% | — | `llama3b_uniform_seed42` |\n| Adaptive | 10.58 | **53.42%** | 72.49% | `llama3b_adaptive_seed42` |\n| Δ | +0.05 | **+1.57pp** (3.9σ) | — | |\n\n**Notes:**\n- PPL: adaptive slightly WORSE (+0.05), but within noise range.\n- MMLU: adaptive significantly BETTER (+1.57pp, 3.9σ), suggesting reweighting improves knowledge retention.\n- Conclusion: \"neutral-to-positive\" — PPL parity with downstream task improvement.\n- YAML shows conclusion=negative (PPL worse), API shows conclusion=success (considering MMLU gain).\n- eval_tokens=4,017,316 (reeval_v2 unified params).\n\n---\n\n## Table 8: τ Sensitivity (ρ=0.4, seed=42, Qwen3-0.6B)\n\n| τ | PPL | Δ vs Uniform | exp_id | Conclusion |\n|---|-----|-------------|--------|------------|\n| 0.5 | 17.688 | -0.006 | `tau_05_seed42` | success |\n| 0.6 | 17.681 | -0.013 | `tau_06_seed42` | success |\n| 0.7 | 17.679 | -0.015 | `tau_07_seed42` | success |\n| 0.8 | 17.653 | -0.041 | `adaptive_fix_seed42` | success |\n| 0.9 | 17.712 | +0.018 | `tau_09_seed42` | **negative** |\n| 0.95 | 17.723 | +0.029 | `tau_095_seed42` | **negative** |\n\n**τ sweep at ρ=0.6 (seed=42):**\n\n| τ | PPL | exp_id |\n|---|-----|--------|\n| 0.6 | 17.736 | `contamination_60_tau06_seed42` |\n| 0.7 | 17.73 | `contamination_60_tau07_seed42` |\n| 0.8 | 17.74 | `contamination_60_seed42_r2` |\n\n---\n\n## Table 9: Batch Size & n_min Ablation (ρ=0.4, seed=42, Qwen3-0.6B)\n\n| Config | PPL | Δ vs Uniform | exp_id |\n|--------|-----|-------------|--------|\n| bs=4, n_min=2 (default) | 17.653 | -0.041 | `adaptive_fix_seed42` |\n| bs=4, n_min=1 | 17.789 | +0.095 | `nmin1_seed42` |\n| bs=4, n_min=4 | 17.695 | +0.001 | `nmin4_seed42` |\n| bs=8, n_min=2 | 17.73 | +0.036 | `bs8_nmin2_seed42_r2` |\n| bs=8, n_min=4 (coupling rule) | 17.66 | -0.034 | `bs8_auto_nmin_r5` |\n| bs=16, n_min=8 (coupling rule) | 17.65 | -0.044 | `batchsize16_nmin8_r3` |\n| Golden ratio (b*=φ−1≈0.618) | 17.654 | -0.040 | `golden_ratio_seed42` |\n\n**Notes:**\n- Coupling rule: n_min = max(2, bs//2).\n- bs=8 without coupling (n_min=2) degrades; coupling (n_min=4) restores performance.\n- bs=16 with n_min=8 matches default performance.\n- n_min=1 is too loose, n_min=4 at bs=4 is too strict (forces b*=0 for 100% of batches).\n\n---\n\n## Batch-Adaptive τ (negative results)\n\n| Setting | PPL | exp_id | Conclusion |\n|---------|-----|--------|------------|\n| Batch-adaptive τ, ρ=0.4 | 17.681 | `batch_adaptive_tau_rho04_seed42` | **negative** |\n| Batch-adaptive τ, ρ=0.6 | 17.73 | `batch_adaptive_tau_rho06_r5` | **negative** |\n\nNo improvement over fixed τ at either contamination level. Path abandoned.\n\n---\n\n## Summary of Missing / In-Progress Data\n\n| Item | Status | Blocking? |\n|------|--------|-----------|\n| N-gram detector eval (adaptive + uniform) | Training done, **eval needed** | Yes — Table 5 |\n| GPT-2 detector (adaptive + uniform) | PREPARING | Yes — Table 5 |\n| 1.7B eval (adaptive + uniform) | RUNNING | Yes — Table 6 |\n| D&R q=0.1 | RUNNING | Minor — Table 3 |\n| D&R q=0.8 | RUNNING | Minor — Table 3 |\n| 1.7B seed 123 | RUNNING | Desirable — Table 6 multi-seed |\n| Llama-3.2-3B multi-seed | Not started | Desirable — Table 7 robustness |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper-main-table-compilation_20260518T212919",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/paper_main_table_data.md",
    "content": "# Paper Main Table Data — Compiled 2026-05-18\n\nAll PPL values are `eval_ppl_holdout` on `data/human/eval_holdout.jsonl` (sliding window, stride=1024, max_docs=5000, fp16, ~4.08M tokens).\n\nPretrained baseline (no continued training): **Qwen3-0.6B = 22.97** (`baseline_qwen3_0.6b`)\n\n---\n\n## Table 1: Main Results (ρ=0.4, Qwen3-0.6B)\n\n| Method | Seed 42 | Seed 123 | Seed 456 | Mean | Δ vs Uniform |\n|--------|---------|----------|----------|------|-------------|\n| Uniform | 17.6939 (`uniform_seed42`) | 17.6861 (`uniform_seed123`) | 17.7015 (`uniform_seed456`) | 17.694 | — |\n| **Adaptive (fix)** | 17.6527 (`adaptive_fix_seed42`) | 17.6432 (`adaptive_fix_seed123`) | 17.6566 (`adaptive_fix_seed456`) | **17.651** | **-0.043** |\n| ESS-only | 17.73 (`ess_only_seed42`) | 17.72 (`ess_only_seed123`) | 17.76 (`ess_only_seed456`) | 17.737 | +0.043 |\n| Random reweight | 17.83 (`random_reweight_v2_seed42`) | 17.801 (`random_reweight_seed123_r5`) | 17.777 (`random_reweight_seed456`) | 17.803 | +0.109 |\n\n**Notes:**\n- \"Adaptive (fix)\" = dual-constraint min-intervention (τ=0.8, n_min=2). Used as reference in all cross-experiment comparisons.\n- Earlier \"adaptive_seed{42,123,456}\" runs produced slightly better PPL (17.644/17.631/17.642, mean=17.639), but adaptive_fix is the canonical version referenced throughout.\n- ESS-only = max-intervention (b* = max{b : ESS(b) ≥ n_min}), ignores α_eff quality constraint.\n- Random reweight = random (non-provenance) weights applied to samples.\n- Random > Uniform > ESS-only > Adaptive confirms detector signal is load-bearing.\n\n---\n\n## Table 2: Grid-b Sweep (ρ=0.4, Qwen3-0.6B)\n\n### Seed 42 (from `grid_b_seed42_batch` + individual runs)\n\n| b | PPL | exp_id |\n|---|-----|--------|\n| 0.1 | 17.657 | `grid_b0_1_seed42` |\n| 0.2 | 17.64 | `grid_b0_2_seed42` |\n| 0.3 | 17.64 | `grid_b0_3_seed42` |\n| 0.5 | 17.651 | `grid_b_seed42_batch` (b0.5) |\n| 1.0 | 17.692 | `grid_b_seed42_batch` (b1.0) |\n| 1.5 | 17.718 | `grid_b_seed42_batch` (b1.5) |\n| 2.0 | 17.741 | `grid_b_seed42_batch` (b2.0) |\n| 3.0 | 17.774 | `grid_b_seed42_batch` (b3.0) |\n| 5.0 | 17.818 | `grid_b_seed42_batch` (b5.0) |\n\n### Multi-seed (seed 123 & 456)\n\n| b | Seed 123 | Seed 456 | exp_ids |\n|---|----------|----------|---------|\n| 0.1 | 17.646 | 17.663 | `grid_b0_1_seed{123,456}` |\n| 0.2 | 17.637 | 17.645 | `grid_b0_2_seed{123,456}` |\n| 0.3 | 17.579 | 17.64 | `grid_b0_3_seed123_r2`, `grid_b0_3_seed456_r2` |\n| 0.5 | 17.638 | 17.65 | `grid_b0_5_seed{123,456}` |\n| 1.0 | 17.674 | 17.68 | `grid_b1_0_seed{123,456}` |\n| 1.5 | 17.701 | 17.71 | `grid_b1_5_seed{123,456}` |\n| 2.0 | 17.725 | 17.989 | `grid_b2_0_seed{123,456}` |\n| 3.0 | 17.76 | 17.921 | `grid_b3_0_seed{123,456}` |\n| 5.0 | 17.804 | 17.993 | `grid_b5_0_seed{123,456}` |\n\n**Notes:**\n- grid_b0_3_seed123_r2 = 17.579 is an outlier (lowest in entire sweep). Verify before using.\n- grid_b2_0_seed456 = 17.989 and grid_b3_0_seed456 = 17.921 are outliers (much higher than seed123). May indicate training instability at high b.\n- Best grid-b ≈ 0.2-0.3, consistent with adaptive b* median ≈ 0.88.\n- Adaptive PPL (17.651) matches grid-best region, validating auto-tuning (Claim 2).\n\n---\n\n## Table 3: Detect & Remove (D&R) Threshold Sensitivity (ρ=0.4, seed=42)\n\n| Threshold | PPL | Data Retained | Training | exp_id |\n|-----------|-----|---------------|----------|--------|\n| q=0.3 | 17.253 | ~70% (remove top 30%) | Multi-epoch | `threshold_q03_seed42` |\n| q=0.5 | 17.29 | ~50% (remove top 50%) | Multi-epoch | `detect_remove_baseline_seed42` |\n| q=0.5 (epoch-matched) | 17.65 | ~50% | Single pass | `detect_remove_q05_epoch_matched_seed42` |\n| q=0.7 | 17.32 | ~30% retained | Multi-epoch | `detect_remove_q07_seed42` |\n| q=0.9 | 17.42 | ~10% retained | Multi-epoch | `detect_remove_q09_seed42` |\n\n**Multi-seed D&R q=0.5 (multi-epoch):**\n\n| Seed | PPL | exp_id |\n|------|-----|--------|\n| 42 | 17.29 | `detect_remove_baseline_seed42` |\n| 123 | 17.27 | `detect_remove_q05_seed123` |\n| 456 | 17.28 | `detect_remove_q05_seed456` |\n| Mean | **17.28** | |\n\n**Epoch-matched D&R q=0.5:**\n\n| Seed | PPL | exp_id |\n|------|-----|--------|\n| 42 | 17.65 | `detect_remove_q05_epoch_matched_seed42` |\n| 123 | 17.66 | `epoch_matched_dr_seed123` |\n| 456 | 17.66 | `epoch_matched_dr_seed456` |\n| Mean | **17.66** | |\n\n**Notes:**\n- D&R multi-epoch PPL is much lower (17.28) but trains multiple epochs on filtered clean data.\n- Epoch-matched D&R (17.66) is comparable to Adaptive (17.651), confirming advantage is from multi-epoch, not filtering.\n- D&R discards data; Adaptive retains all data with reweighting.\n- **RUNNING:** q=0.1 (`detect_remove_q01_seed42`), q=0.8 (`detect_remove_q08_seed42`)\n\n---\n\n## Table 4: Contamination Rate (ρ) Sensitivity\n\n### ρ=0.2 (seed=42 only)\n\n| Method | PPL | exp_id | Note |\n|--------|-----|--------|------|\n| Uniform | 17.336 | `rho02_uniform_seed42` | |\n| Adaptive (τ=0.8) | 17.382 | `rho02_adaptive_tau08_seed42` | **NEGATIVE** (+0.046) |\n| Adaptive (τ=0.9) | 17.45 | `rho02_adaptive_tau09_r5` | **NEGATIVE** (+0.114) |\n\n### ρ=0.4 (3 seeds)\n\n| Method | Seed 42 | Seed 123 | Seed 456 | Mean |\n|--------|---------|----------|----------|------|\n| Uniform | 17.694 | 17.686 | 17.702 | 17.694 |\n| Adaptive | 17.653 | 17.643 | 17.657 | 17.651 |\n| Δ | -0.041 | -0.043 | -0.045 | **-0.043** |\n\n### ρ=0.6 (3 seeds)\n\n| Method | Seed 42 | Seed 123 | Seed 456 | Mean |\n|--------|---------|----------|----------|------|\n| Uniform | 17.766 (`contamination_60_uniform_seed42`) | 17.754 (`contamination_60_uniform_seed123`) | 17.770 (`contamination_60_uniform_seed456`) | 17.763 |\n| Adaptive | 17.740 (`contamination_60_seed42_r2`) | 17.732 (`contamination_60_seed123`) | 17.735 (`contamination_60_adaptive_seed456`) | 17.736 |\n| Δ | -0.026 | -0.022 | -0.035 | **-0.028** |\n\n### ρ=0.6 Additional Methods\n\n| Method | Seed 42 | Seed 123 | Seed 456 | Mean |\n|--------|---------|----------|----------|------|\n| ESS-only | 17.77 | 17.763 | 17.762 | 17.765 |\n| Random | 17.832 | 17.87 | 17.88 | 17.861 |\n| Hybrid (filter+reweight) | 17.53 (`hybrid_rho06_seed42`) | — | — | 17.53 |\n| Grid b=0.3 | 17.634 (`contamination_60_grid_b0_3_seed42`) | — | — | |\n| Grid b=0.5 | 17.704 (`contamination_60_grid_b0_5_seed42`) | — | — | |\n\nexp_ids for ρ=0.6 ESS-only: `contamination_60_ess_only_seed{42,123,456}`\nexp_ids for ρ=0.6 Random: `contamination_60_random_seed{42,123,456}`\n\n**Summary:**\n- ρ=0.2: Adaptive HURTS (data already clean, reweighting over-penalizes)\n- ρ=0.4: Adaptive improves by -0.043 PPL (consistent across seeds)\n- ρ=0.6: Adaptive improves by -0.028 PPL (smaller gap, consistent across seeds)\n- Hybrid (filter q>0.95 + reweight) at ρ=0.6 achieves 17.53 (best), but single-seed only\n- ρ=0.4 also has hybrid: 17.514 (`hybrid_rho04_seed42`) — also single-seed\n\n---\n\n## Table 5: Multi-Detector Validation (ρ=0.4, seed=42, Qwen3-0.6B)\n\n| Detector | Adaptive PPL | Uniform PPL | Δ | exp_ids |\n|----------|-------------|-------------|---|---------|\n| TF-IDF+LR (q_score, AUC=0.939) | 17.653 | 17.694 | -0.041 | `adaptive_fix_seed42` / `uniform_seed42` |\n| N-gram PPL (AUC=0.73) | **NO EVAL** | **NO EVAL** | — | `ngram_adaptive_seed42` / `ngram_uniform_seed42` |\n| GPT-2 PPL | **NOT STARTED** | **NOT STARTED** | — | `gpt2_adaptive_seed42` / `gpt2_uniform_seed42` (PREPARING) |\n\n**Notes:**\n- N-gram experiments completed training but eval PPL not yet computed. Models saved at:\n  - `/root/autodl-tmp/provenance_weight_training/output/models/ngram_adaptive_seed42/final`\n  - `/root/autodl-tmp/provenance_weight_training/output/models/ngram_uniform_seed42/final`\n- GPT-2 detector experiments still in PREPARING status.\n\n---\n\n## Table 6: Model Scale — Qwen3-1.7B (ρ=0.4, seed=42)\n\n| Method | PPL | exp_id | Status |\n|--------|-----|--------|--------|\n| Adaptive | **EVAL RUNNING** | `adaptive_1_7b_seed42` | Training done, eval in progress (`eval_adaptive_1_7b_v2`) |\n| Uniform | **EVAL RUNNING** | `uniform_1_7b_seed42` | Training FAILED (checkpoint issue); eval running on available checkpoint (`eval_uniform_1_7b_v3`) |\n\n**Notes:**\n- uniform_1_7b_seed42 training failed due to FileNotFoundError on checkpoint-3000/trainer_state.json during resume.\n- Eval is running on whatever checkpoint exists.\n- adaptive_1_7b_seed123 is also RUNNING (additional seed).\n\n---\n\n## Table 7: Cross-Architecture — Llama-3.2-3B (ρ=0.4, seed=42)\n\n| Method | PPL | MMLU (5-shot) | HellaSwag (10-shot) | exp_id |\n|--------|-----|---------------|---------------------|--------|\n| Uniform | 10.53 | 51.85% | — | `llama3b_uniform_seed42` |\n| Adaptive | 10.58 | **53.42%** | 72.49% | `llama3b_adaptive_seed42` |\n| Δ | +0.05 | **+1.57pp** (3.9σ) | — | |\n\n**Notes:**\n- PPL: adaptive slightly WORSE (+0.05), but within noise range.\n- MMLU: adaptive significantly BETTER (+1.57pp, 3.9σ), suggesting reweighting improves knowledge retention.\n- Conclusion: \"neutral-to-positive\" — PPL parity with downstream task improvement.\n- YAML shows conclusion=negative (PPL worse), API shows conclusion=success (considering MMLU gain).\n- eval_tokens=4,017,316 (reeval_v2 unified params).\n\n---\n\n## Table 8: τ Sensitivity (ρ=0.4, seed=42, Qwen3-0.6B)\n\n| τ | PPL | Δ vs Uniform | exp_id | Conclusion |\n|---|-----|-------------|--------|------------|\n| 0.5 | 17.688 | -0.006 | `tau_05_seed42` | success |\n| 0.6 | 17.681 | -0.013 | `tau_06_seed42` | success |\n| 0.7 | 17.679 | -0.015 | `tau_07_seed42` | success |\n| 0.8 | 17.653 | -0.041 | `adaptive_fix_seed42` | success |\n| 0.9 | 17.712 | +0.018 | `tau_09_seed42` | **negative** |\n| 0.95 | 17.723 | +0.029 | `tau_095_seed42` | **negative** |\n\n**τ sweep at ρ=0.6 (seed=42):**\n\n| τ | PPL | exp_id |\n|---|-----|--------|\n| 0.6 | 17.736 | `contamination_60_tau06_seed42` |\n| 0.7 | 17.73 | `contamination_60_tau07_seed42` |\n| 0.8 | 17.74 | `contamination_60_seed42_r2` |\n\n---\n\n## Table 9: Batch Size & n_min Ablation (ρ=0.4, seed=42, Qwen3-0.6B)\n\n| Config | PPL | Δ vs Uniform | exp_id |\n|--------|-----|-------------|--------|\n| bs=4, n_min=2 (default) | 17.653 | -0.041 | `adaptive_fix_seed42` |\n| bs=4, n_min=1 | 17.789 | +0.095 | `nmin1_seed42` |\n| bs=4, n_min=4 | 17.695 | +0.001 | `nmin4_seed42` |\n| bs=8, n_min=2 | 17.73 | +0.036 | `bs8_nmin2_seed42_r2` |\n| bs=8, n_min=4 (coupling rule) | 17.66 | -0.034 | `bs8_auto_nmin_r5` |\n| bs=16, n_min=8 (coupling rule) | 17.65 | -0.044 | `batchsize16_nmin8_r3` |\n| Golden ratio (b*=φ−1≈0.618) | 17.654 | -0.040 | `golden_ratio_seed42` |\n\n**Notes:**\n- Coupling rule: n_min = max(2, bs//2).\n- bs=8 without coupling (n_min=2) degrades; coupling (n_min=4) restores performance.\n- bs=16 with n_min=8 matches default performance.\n- n_min=1 is too loose, n_min=4 at bs=4 is too strict (forces b*=0 for 100% of batches).\n\n---\n\n## Batch-Adaptive τ (negative results)\n\n| Setting | PPL | exp_id | Conclusion |\n|---------|-----|--------|------------|\n| Batch-adaptive τ, ρ=0.4 | 17.681 | `batch_adaptive_tau_rho04_seed42` | **negative** |\n| Batch-adaptive τ, ρ=0.6 | 17.73 | `batch_adaptive_tau_rho06_r5` | **negative** |\n\nNo improvement over fixed τ at either contamination level. Path abandoned.\n\n---\n\n## Summary of Missing / In-Progress Data\n\n| Item | Status | Blocking? |\n|------|--------|-----------|\n| N-gram detector eval (adaptive + uniform) | Training done, **eval needed** | Yes — Table 5 |\n| GPT-2 detector (adaptive + uniform) | PREPARING | Yes — Table 5 |\n| 1.7B eval (adaptive + uniform) | RUNNING | Yes — Table 6 |\n| D&R q=0.1 | RUNNING | Minor — Table 3 |\n| D&R q=0.8 | RUNNING | Minor — Table 3 |\n| 1.7B seed 123 | RUNNING | Desirable — Table 6 multi-seed |\n| Llama-3.2-3B multi-seed | Not started | Desirable — Table 7 robustness |\n"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T21:34:05.382951+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/paper_main_table_data.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper-main-table-compilation_20260518T212919",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-18T21:34:05.383205+00:00_

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
  "session": "worker_analysis_paper-main-table-compilation_20260518T212919",
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

_source line 22 · 2026-05-18T21:34:05.383413+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper-main-table-compilation_20260518T212919",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-18T21:34:05.383611+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "paper_main_table_data",
  "type": "data",
  "description": "Complete PPL results compilation for all paper tables (Tables 1-9): main results, grid-b sweep, D&R threshold, contamination rate sensitivity, multi-detector, scale, cross-architecture, τ sensitivity, batch size ablation. Includes exp_id traceability and missing data tracker.",
  "project": "provenance_weight_training",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/paper_main_table_data.md",
  "tags": "['paper', 'tables', 'ppl', 'compilation']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper-main-table-compilation_20260518T212919",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "paper_main_table_data",
    "type": "data",
    "description": "Complete PPL results compilation for all paper tables (Tables 1-9): main results, grid-b sweep, D&R threshold, contamination rate sensitivity, multi-detector, scale, cross-architecture, τ sensitivity, batch size ablation. Includes exp_id traceability and missing data tracker.",
    "project": "provenance_weight_training",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/paper_main_table_data.md",
    "tags": "['paper', 'tables', 'ppl', 'compilation']"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-18T21:34:05.385183+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260518_87a413\", \"name\": \"paper_main_table_data\", \"type\": \"data\", \"description\": \"Complete PPL results compilation for all paper tables (Tables 1-9): main results, grid-b sweep, D&R threshold, contamination rate sensitivity, multi-detector, scale, cross-architecture, τ sensitivity, batch size ablation. Includes exp_id traceability and missing data tracker.\", \"path\": \"projects/provenance_weight_training/artifacts/_project/data/paper_main_table_data.md\", \"url\": null, \"project\": \"provenance_weight_training\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-18T21:33:52.961503+00:00\", \"tags\": [\"paper\", \"tables\", \"ppl\", \"compilation\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper-main-table-compilation_20260518T212919",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 1
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-18T21:34:05.385519+00:00_

已写入 `artifacts/paper_main_table_data.md`，包含 9 张表格数据。

**核心发现汇总：**

| 表格 | 关键结论 |
|------|---------|
| Table 1 (Main) | Adaptive -0.043 PPL vs Uniform (3 seeds), Random +0.109 证实 detector signal load-bearing |
| Table 2 (Grid-b) | 最优 b≈0.2-0.3，Adaptive 自动匹配 grid-best |
| Table 3 (D&R) | 多 epoch D&R=17.28，epoch-matched D&R=17.66 ≈ Adaptive=17.651 |
| Table 4 (ρ) | ρ=0.2 adaptive 反而有害；ρ=0.4 有效 (-0.043)；ρ=0.6 有效 (-0.028) |
| Table 5 (Multi-det) | TF-IDF 已验证；N-gram 训练完缺 eval；GPT-2 未开始 |
| Table 6 (1.7B) | Eval 正在跑 |
| Table 7 (Llama-3B) | PPL +0.05 (微劣)，MMLU +1.57pp (3.9σ 显著提升) |
| Table 8 (τ) | 最优 τ=0.8；τ≥0.9 有害 |
| Table 9 (bs/n_min) | coupling rule n_min=max(2,bs//2) 验证有效 |

**阻塞项：** N-gram eval、GPT-2 实验、1.7B eval 尚未完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_paper-main-table-compilation_20260518T212919"
}
```

</details>

---
