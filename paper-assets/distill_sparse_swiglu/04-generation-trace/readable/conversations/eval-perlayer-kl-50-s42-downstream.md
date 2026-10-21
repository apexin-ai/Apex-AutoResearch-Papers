# eval perlayer kl 50 s42 downstream

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_eval_perlayer_kl_50_s42_downstream_20260522T065238.jsonl`
- **Structured JSON:** [`cdd39d0dff29ead73e30.json`](../../sessions/cd/cdd39d0dff29ead73e30.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Assistant

_source line 1 · 2026-05-22T06:52:52.743438+00:00_

You've hit your limit · resets 6pm (UTC)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_eval_perlayer_kl_50_s42_downstream_20260522T065238"
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T06:54:06.943315+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/distill_sparse_swiglu/checkpoints/perlayer_kl_50_s42/predictor_perlayer_kl.pt': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 1.21}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_perlayer_kl_50_s42_downstream_20260522T065238",
  "tool": "unknown"
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T06:54:06.943642+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34887",
  "command": "ls -la /root/distill_sparse_swiglu/checkpoints/perlayer_kl_50_s42/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_perlayer_kl_50_s42_downstream_20260522T065238",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34887",
    "command": "ls -la /root/distill_sparse_swiglu/checkpoints/perlayer_kl_50_s42/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T06:54:06.943932+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/distill_sparse_swiglu/checkpoints/perlayer_kl_50_s42/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_perlayer_kl_50_s42_downstream_20260522T065238",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T06:54:06.944247+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41718",
  "command": "ls -la /root/distill_sparse_swiglu/checkpoints/perlayer_kl_50_s42/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_perlayer_kl_50_s42_downstream_20260522T065238",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41718",
    "command": "ls -la /root/distill_sparse_swiglu/checkpoints/perlayer_kl_50_s42/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-22T06:54:06.944598+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41718",
  "command": "tail -5 /root/runs/distill_sparse_swiglu/perlayer_kl_50_s42_downstream.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_perlayer_kl_50_s42_downstream_20260522T065238",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41718",
    "command": "tail -5 /root/runs/distill_sparse_swiglu/perlayer_kl_50_s42_downstream.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T06:54:06.944759+00:00_

called mcp__agent-ml-research__submit_training_job

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_training_job</summary>

```json
{
  "server": "westd-41718",
  "gpu_ids": "['cuda:1']",
  "exp_id": "perlayer_kl_50_s42_downstream",
  "command": "bash -c \"cd /root/distill_sparse_swiglu && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1 && CUDA_VISIBLE_DEVICES=1 python -u src/benchmark_eval.py --exp_id perlayer_kl_50_s42_downstream --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/perlayer_kl_50_s42/predictor_perlayer_kl.pt --sparsity_mode teal_global --sparsity_target 0.5 --allocation uniform --tasks arc_challenge,winogrande,mmlu,gsm8k,hellaswag,piqa --seq_len 2048 --gpu 0\"",
  "account": "root",
  "project": "distill_sparse_swiglu",
  "timeout_hours": "12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_perlayer_kl_50_s42_downstream_20260522T065238",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "tool_args": {
    "server": "westd-41718",
    "gpu_ids": "['cuda:1']",
    "exp_id": "perlayer_kl_50_s42_downstream",
    "command": "bash -c \"cd /root/distill_sparse_swiglu && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1 && CUDA_VISIBLE_DEVICES=1 python -u src/benchmark_eval.py --exp_id perlayer_kl_50_s42_downstream --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/perlayer_kl_50_s42/predictor_perlayer_kl.pt --sparsity_mode teal_global --sparsity_target 0.5 --allocation uniform --tasks arc_challenge,winogrande,mmlu,gsm8k,hellaswag,piqa --seq_len 2048 --gpu 0\"",
    "account": "root",
    "project": "distill_sparse_swiglu",
    "timeout_hours": "12"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T06:54:06.944938+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Failed to submit job: duplicate session: perlayer_kl_50_s42_downstream\\n\", \"metadata\": {\"elapsed_seconds\": 1.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_perlayer_kl_50_s42_downstream_20260522T065238",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T06:54:06.945143+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41718",
  "command": "ls -la /root/distill_sparse_swiglu/logs/ | grep perlayer_kl_50_s42_downstream",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_perlayer_kl_50_s42_downstream_20260522T065238",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41718",
    "command": "ls -la /root/distill_sparse_swiglu/logs/ | grep perlayer_kl_50_s42_downstream",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T06:54:06.945298+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_perlayer_kl_50_s42_downstream_20260522T065238",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T06:54:06.945425+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41718",
  "command": "find /root/distill_sparse_swiglu/logs/ -name \"*perlayer_kl_50_s42_downstream*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_perlayer_kl_50_s42_downstream_20260522T065238",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41718",
    "command": "find /root/distill_sparse_swiglu/logs/ -name \"*perlayer_kl_50_s42_downstream*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T06:54:06.945550+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_perlayer_kl_50_s42_downstream_20260522T065238",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T06:54:06.945680+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__kill_job",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_perlayer_kl_50_s42_downstream_20260522T065238",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__kill_job",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T06:54:06.945799+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_perlayer_kl_50_s42_downstream_20260522T065238",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T06:54:06.945912+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-41718",
  "command": "tmux ls 2>/dev/null | grep perlayer_kl_50_s42_downstream",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_perlayer_kl_50_s42_downstream_20260522T065238",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-41718",
    "command": "tmux ls 2>/dev/null | grep perlayer_kl_50_s42_downstream",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T06:54:06.946067+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"perlayer_kl_50_s42_downstream: 1 windows (created Fri May 22 14:53:19 2026)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_perlayer_kl_50_s42_downstream_20260522T065238",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T06:54:06.946213+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-41718",
  "command": "tmux capture-pane -t perlayer_kl_50_s42_downstream -p -S -50",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_perlayer_kl_50_s42_downstream_20260522T065238",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-41718",
    "command": "tmux capture-pane -t perlayer_kl_50_s42_downstream -p -S -50",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T06:54:06.946337+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_perlayer_kl_50_s42_downstream_20260522T065238",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T06:54:06.946454+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-41718",
  "command": "ps -ef | grep -E \"benchmark_eval.*perlayer_kl_50_s42_downstream\" | grep -v grep",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_perlayer_kl_50_s42_downstream_20260522T065238",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-41718",
    "command": "ps -ef | grep -E \"benchmark_eval.*perlayer_kl_50_s42_downstream\" | grep -v grep",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T06:54:06.946628+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"root     374284 374126  0 14:53 pts/1    00:00:00 bash -c rm -f /tmp/agent-ml-exit/perlayer_kl_50_s42_downstream.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/distill_sparse_swiglu/perlayer_kl_50_s42_downstream.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/perlayer_kl_50_s42_downstream.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/distill_sparse_swiglu/ && export CUDA_VISIBLE_DEVICES=1 && timeout 21600 env bash -c 'bash -c \\\"cd /root/distill_sparse_swiglu && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1 && CUDA_VISIBLE_DEVICES=1 python -u src/benchmark_eval.py --exp_id perlayer_kl_50_s42_downstream --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/perlayer_kl_50_s42/predictor_perlayer_kl.pt --sparsity_mode teal_global --sparsity_target 0.5 --allocation uniform --tasks arc_challenge,winogrande,mmlu,gsm8k,hellaswag,piqa --seq_len 2048 --gpu 0\\\"'; } > ~/runs/distill_sparse_swiglu/perlayer_kl_50_s42_downstream.log 2>&1\\nroot     374288 374284  0 14:53 pts/1    00:00:00 timeout 21600 env bash -c bash -c \\\"cd /root/distill_sparse_swiglu && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1 && CUDA_VISIBLE_DEVICES=1 python -u src/benchmark_eval.py --exp_id perlayer_kl_50_s42_downstream --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/perlayer_kl_50_s42/predictor_perlayer_kl.pt --sparsity_mode teal_global --sparsity_target 0.5 --allocation uniform --tasks arc_challenge,winogrande,mmlu,gsm8k,hellaswag,piqa --seq_len 2048 --gpu 0\\\"\\nroo
…[truncated 504 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_perlayer_kl_50_s42_downstream_20260522T065238",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T06:54:06.946792+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41718",
  "command": "tail -20 /root/runs/distill_sparse_swiglu/perlayer_kl_50_s42_downstream.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_perlayer_kl_50_s42_downstream_20260522T065238",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41718",
    "command": "tail -20 /root/runs/distill_sparse_swiglu/perlayer_kl_50_s42_downstream.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-22T06:54:06.947010+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  Layer 22: 0.500\\n  Layer 23: 0.496\\n  Layer 24: 0.496\\n  Layer 25: 0.496\\n  Layer 26: 0.496\\n  Layer 27: 0.500\\n  Layer 28: 0.500\\n  Layer 29: 0.500\\n  Layer 30: 0.500\\n  Layer 31: 0.500\\n  Model-level: 0.496\\n\\n--- lm-eval: ['arc_challenge', 'winogrande', 'mmlu', 'gsm8k', 'hellaswag', 'piqa'] ---\\n`pretrained` model kwarg is not of type `str`. Many other model arguments may be ignored. Please do not launch via accelerate or use `parallelize=True` if passing an existing model this way.\\nPassed an already-initialized model through `pretrained`, assuming single-process call to evaluate() or custom distributed integration\\n  Running ['arc_challenge'] (num_fewshot=25) ...\\nUsing the latest cached version of the dataset since allenai/ai2_arc couldn't be found on the Hugging Face Hub (offline mode is enabled).\\nFound the latest cached dataset configuration 'ARC-Challenge' at /root/autodl-tmp/.hf_cache/datasets/allenai___ai2_arc/ARC-Challenge/0.0.0/210d026faf9955653af8916fad021475a3f00453 (last modified on Sat May 16 06:10:24 2026).\\nOverwriting default num_fewshot of arc_challenge from None to 25\\n\\r  0%|          | 0/1172 [00:00<?, ?it/s]\\r  0%|          | 5/1172 [00:00<00:24, 47.28it/s]\\r  1%|          | 10/1172 [00:00<00:24, 47.59it/s]\\r  1%|▏         | 15/1172 [00:00<00:24, 47.74it/s]\\r  2%|▏         | 20/1172 [00:00<00:24, 47.83it/s]\\r  2%|▏         | 25/1172 [00:00<00:24, 47.56it/s]\\r  3%|▎         | 30/1172 [00:00<00:24, 47.16it/s]\\r  3%|▎         | 35/1172 [00:00<00:23, 47.41it/s]\\r  3%|▎         | 40/1172 [00:00<00:23, 47.63it/s]\\r  4%|▍         | 45/1172 [00:00<00:23, 47.45it/s]\\r  4%|▍         | 50/1172 [00:01<00:23, 47.65it/s]\\r  5%|▍         | 55/1172 [00:01<00:23, 47.72it/s]\\r  5%|▌         | 60/1172 [00:01<00:23, 47.28it/s]\\r  6%|▌         | 65/1172 [00:01<00:23, 47.23it/s]\\r  6%|▌         | 70/1172 [00:01<00:23, 47.35it/s]\\r  6%|▋         | 75/1172 [00:01<00:23, 47
…[truncated 6510 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_perlayer_kl_50_s42_downstream_20260522T065238",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-22T06:54:06.947252+00:00_

Job is running successfully on westd-41718 cuda:1.

- **PID**: 374289 (python)
- **tmux session**: `perlayer_kl_50_s42_downstream`
- **日志**: `/root/runs/distill_sparse_swiglu/perlayer_kl_50_s42_downstream.log`
- **状态**: 已加载 checkpoint，稀疏度配置正确（model-level 0.496），arc_challenge 进行中 ~92%，6 个 task 顺序评测中。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_eval_perlayer_kl_50_s42_downstream_20260522T065238"
}
```

</details>

---
