# analysis qwen14b bce30 s42 eval

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_analysis_qwen14b_bce30_s42_eval_20260517T224156.jsonl`
- **Structured JSON:** [`49bb37788c0abed1ba1a.json`](../../sessions/49/49bb37788c0abed1ba1a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-17T22:43:13.767276+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b_bce30_s42_eval_20260517T224156",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T22:43:13.767680+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b_bce30_s42_eval_20260517T224156",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T22:43:13.768198+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34887",
  "command": "tail -200 ~/runs/distill_sparse_swiglu/qwen14b_bce30_s42_eval.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b_bce30_s42_eval_20260517T224156",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34887",
    "command": "tail -200 ~/runs/distill_sparse_swiglu/qwen14b_bce30_s42_eval.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T22:43:13.768898+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\r  0%|          | 0/110 [00:00<?, ?it/s]\\r 24%|██▎       | 26/110 [00:00<00:00, 250.56it/s]\\r 47%|████▋     | 52/110 [00:00<00:00, 250.96it/s]\\r 71%|███████   | 78/110 [00:00<00:00, 243.99it/s]\\r 95%|█████████▍| 104/110 [00:00<00:00, 247.04it/s]\\r100%|██████████| 110/110 [00:00<00:00, 247.47it/s]\\n\\r  0%|          | 0/245 [00:00<?, ?it/s]\\r 10%|█         | 25/245 [00:00<00:00, 249.16it/s]\\r 20%|██        | 50/245 [00:00<00:00, 248.79it/s]\\r 31%|███       | 75/245 [00:00<00:00, 246.36it/s]\\r 41%|████      | 100/245 [00:00<00:00, 246.77it/s]\\r 51%|█████     | 125/245 [00:00<00:00, 246.82it/s]\\r 61%|██████    | 150/245 [00:00<00:00, 246.98it/s]\\r 71%|███████▏  | 175/245 [00:00<00:00, 242.83it/s]\\r 82%|████████▏ | 200/245 [00:00<00:00, 244.62it/s]\\r 92%|█████████▏| 225/245 [00:00<00:00, 246.15it/s]\\r100%|██████████| 245/245 [00:00<00:00, 246.36it/s]\\n\\r  0%|          | 0/201 [00:00<?, ?it/s]\\r 13%|█▎        | 26/201 [00:00<00:00, 252.28it/s]\\r 26%|██▌       | 52/201 [00:00<00:00, 252.58it/s]\\r 39%|███▉      | 78/201 [00:00<00:00, 252.13it/s]\\r 52%|█████▏    | 104/201 [00:00<00:00, 252.54it/s]\\r 65%|██████▍   | 130/201 [00:00<00:00, 247.46it/s]\\r 78%|███████▊  | 156/201 [00:00<00:00, 248.83it/s]\\r 91%|█████████ | 182/201 [00:00<00:00, 249.82it/s]\\r100%|██████████| 201/201 [00:00<00:00, 250.26it/s]\\n\\r  0%|          | 0/100 [00:00<?, ?it/s]\\r 26%|██▌       | 26/100 [00:00<00:00, 250.88it/s]\\r 52%|█████▏    | 52/100 [00:00<00:00, 251.28it/s]\\r 78%|███████▊  | 78/100 [00:00<00:00, 251.51it/s]\\r100%|██████████| 100/100 [00:00<00:00, 251.70it/s]\\n\\r  0%|          | 0/126 [00:00<?, ?it/s]\\r 21%|██        | 26/126 [00:00<00:00, 250.60it/s]\\r 41%|████▏     | 52/126 [00:00<00:00, 241.68it/s]\\r 62%|██████▏   | 78/126 [00:00<00:00, 245.50it/s]\\r 83%|████████▎ | 104/126 [00:00<00:00, 247.35it/s]\\r100%|██████████| 126/126 [00:00<00:00, 246.88it/s]\\n\\r  0%|          | 0/165 [00:00<?, ?i
…[truncated 6448 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b_bce30_s42_eval_20260517T224156",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T22:43:13.769383+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34887",
  "command": "grep -i \"ppl\\|perplexity\\|wikitext\" ~/runs/distill_sparse_swiglu/qwen14b_bce30_s42_eval.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b_bce30_s42_eval_20260517T224156",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34887",
    "command": "grep -i \"ppl\\|perplexity\\|wikitext\" ~/runs/distill_sparse_swiglu/qwen14b_bce30_s42_eval.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T22:43:13.769571+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b_bce30_s42_eval_20260517T224156",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T22:43:13.769725+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34887",
  "command": "grep -i \"ppl\" ~/runs/distill_sparse_swiglu/qwen14b_bce30_s42_eval.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b_bce30_s42_eval_20260517T224156",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34887",
    "command": "grep -i \"ppl\" ~/runs/distill_sparse_swiglu/qwen14b_bce30_s42_eval.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T22:43:13.769940+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"--- WikiText-2 PPL ---\\n  PPL = 8.7634  (28.8s)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b_bce30_s42_eval_20260517T224156",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T22:43:13.770153+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "qwen14b_bce30_s42_eval",
  "field": "metrics",
  "value": "{'wikitext2_ppl': 8.7634, 'arc_challenge_acc_norm': 0.5759, 'winogrande_acc': 0.7261, 'mmlu_acc': 0.7167, 'gsm8k_exact_match': 0.5307}",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b_bce30_s42_eval_20260517T224156",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "qwen14b_bce30_s42_eval",
    "field": "metrics",
    "value": "{'wikitext2_ppl': 8.7634, 'arc_challenge_acc_norm': 0.5759, 'winogrande_acc': 0.7261, 'mmlu_acc': 0.7167, 'gsm8k_exact_match': 0.5307}",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T22:43:13.770346+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"qwen14b_bce30_s42_eval\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T16:47:04.947Z\", \"updated_at\": \"2026-05-17T22:42:44.684Z\", \"hypothesis\": \"Qwen-14B BCE predictor at 30% sparsity shows worse downstream performance (MMLU, ARC, WinoGrande, GSM8K) than KL predictor, confirming objective mismatch penalty persists in downstream tasks beyond PPL (KL TEAL PPL=7.62 vs BCE TEAL PPL=8.76)\", \"parent\": \"qwen14b_bce30_s42\", \"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id qwen14b_bce30_s42_eval --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_bce30_s42/predictor_bce.pt --sparsity_mode teal_global --sparsity_target 0.3 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"59122\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_bce30_s42_eval.log\", \"submitted_at\": \"2026-05-17T16:47:51.067Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"pid\": \"59122\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_bce30_s42_eval.log\", \"reproduce\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id qwen14b_bce30_s42_eval --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_bce30_s42/predictor_bce.pt --sparsity_mode teal_global --sparsity_target 0.3 --tasks 
…[truncated 459 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b_bce30_s42_eval_20260517T224156",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T22:43:13.770839+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "qwen14b_bce30_s42_eval",
  "field": "checkpoint_path",
  "value": "checkpoints/qwen14b_bce30_s42/predictor_bce.pt",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b_bce30_s42_eval_20260517T224156",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "qwen14b_bce30_s42_eval",
    "field": "checkpoint_path",
    "value": "checkpoints/qwen14b_bce30_s42/predictor_bce.pt",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-17T22:43:13.771287+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "qwen14b_bce30_s42_eval",
  "field": "completed_at",
  "value": "2026-05-17T22:40:16Z",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b_bce30_s42_eval_20260517T224156",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "qwen14b_bce30_s42_eval",
    "field": "completed_at",
    "value": "2026-05-17T22:40:16Z",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-17T22:43:13.771921+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"qwen14b_bce30_s42_eval\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T16:47:04.947Z\", \"updated_at\": \"2026-05-17T22:42:49.828Z\", \"hypothesis\": \"Qwen-14B BCE predictor at 30% sparsity shows worse downstream performance (MMLU, ARC, WinoGrande, GSM8K) than KL predictor, confirming objective mismatch penalty persists in downstream tasks beyond PPL (KL TEAL PPL=7.62 vs BCE TEAL PPL=8.76)\", \"parent\": \"qwen14b_bce30_s42\", \"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id qwen14b_bce30_s42_eval --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_bce30_s42/predictor_bce.pt --sparsity_mode teal_global --sparsity_target 0.3 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"59122\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_bce30_s42_eval.log\", \"submitted_at\": \"2026-05-17T16:47:51.067Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"pid\": \"59122\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_bce30_s42_eval.log\", \"reproduce\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id qwen14b_bce30_s42_eval --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_bce30_s42/predictor_bce.pt --sparsity_mode teal_global --sparsity_target 0.3 --tasks 
…[truncated 533 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b_bce30_s42_eval_20260517T224156",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T22:43:13.772590+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"qwen14b_bce30_s42_eval\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T16:47:04.947Z\", \"updated_at\": \"2026-05-17T22:42:50.884Z\", \"hypothesis\": \"Qwen-14B BCE predictor at 30% sparsity shows worse downstream performance (MMLU, ARC, WinoGrande, GSM8K) than KL predictor, confirming objective mismatch penalty persists in downstream tasks beyond PPL (KL TEAL PPL=7.62 vs BCE TEAL PPL=8.76)\", \"parent\": \"qwen14b_bce30_s42\", \"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id qwen14b_bce30_s42_eval --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_bce30_s42/predictor_bce.pt --sparsity_mode teal_global --sparsity_target 0.3 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"59122\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_bce30_s42_eval.log\", \"submitted_at\": \"2026-05-17T16:47:51.067Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"pid\": \"59122\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_bce30_s42_eval.log\", \"reproduce\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id qwen14b_bce30_s42_eval --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_bce30_s42/predictor_bce.pt --sparsity_mode teal_global --sparsity_target 0.3 --tasks 
…[truncated 577 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b_bce30_s42_eval_20260517T224156",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T22:43:13.772800+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "qwen14b_bce30_s42_eval",
  "field": "conclusion",
  "value": "negative",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b_bce30_s42_eval_20260517T224156",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "qwen14b_bce30_s42_eval",
    "field": "conclusion",
    "value": "negative",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T22:43:13.773003+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"qwen14b_bce30_s42_eval\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T16:47:04.947Z\", \"updated_at\": \"2026-05-17T22:42:55.270Z\", \"hypothesis\": \"Qwen-14B BCE predictor at 30% sparsity shows worse downstream performance (MMLU, ARC, WinoGrande, GSM8K) than KL predictor, confirming objective mismatch penalty persists in downstream tasks beyond PPL (KL TEAL PPL=7.62 vs BCE TEAL PPL=8.76)\", \"parent\": \"qwen14b_bce30_s42\", \"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id qwen14b_bce30_s42_eval --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_bce30_s42/predictor_bce.pt --sparsity_mode teal_global --sparsity_target 0.3 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"59122\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_bce30_s42_eval.log\", \"submitted_at\": \"2026-05-17T16:47:51.067Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"pid\": \"59122\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_bce30_s42_eval.log\", \"reproduce\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id qwen14b_bce30_s42_eval --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_bce30_s42/predictor_bce.pt --sparsity_mode teal_global --sparsity_target 0.3 --tasks 
…[truncated 607 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b_bce30_s42_eval_20260517T224156",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-17T22:43:13.773240+00:00_

Registry updated. Results summary:

## BCE 30% Metrics (qwen14b_bce30_s42_eval)

| Metric | BCE 30% | KL 30% | Dense | vs Dense | vs KL |
|---|---|---|---|---|---|
| WikiText-2 PPL | **8.7634** | 7.6232 | 5.1854 | +69.0% | +15.0% (worse) |
| ARC-C (acc_norm) | **0.5759** | 0.5717 | 0.6758 | -14.8% | +0.4pp (better) |
| WinoGrande (acc) | **0.7261** | 0.7206 | 0.8106 | -10.4% | +0.6pp (better) |
| MMLU (acc) | **0.7167** | 0.6372 | 0.7977 | -10.2% | **+7.9pp (better)** |
| GSM8K (exact_match) | **0.5307** | 0.4882 | 0.8757 | -39.4% | **+4.3pp (better)** |

## Conclusion: **negative** (refutes hypothesis)

Hypothesis was that BCE should perform worse than KL on downstream tasks. Reality:

- **PPL: BCE worse** (8.76 vs 7.62), consistent with BCE's weaker language modeling objective
- **Downstream: BCE uniformly better**, especially MMLU (+7.9pp) and GSM8K (+4.3pp)

BCE trades off perplexity for better downstream task retention. The PPL gap (15%) does not translate into downstream degradation; instead BCE preserves task-relevant features better than KL despite higher PPL. This is a meaningful finding: **PPL is not a reliable proxy for downstream quality in sparsity predictors**.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_qwen14b_bce30_s42_eval_20260517T224156"
}
```

</details>

---
