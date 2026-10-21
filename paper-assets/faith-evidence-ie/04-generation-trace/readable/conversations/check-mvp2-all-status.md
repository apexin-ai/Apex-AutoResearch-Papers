# check mvp2 all status

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_check_mvp2_all_status_20260514T145214.jsonl`
- **Structured JSON:** [`38fec1eeb364aa93c0bc.json`](../../sessions/38/38fec1eeb364aa93c0bc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-14T14:53:08.941312+00:00_

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
  "session": "worker_check_mvp2_all_status_20260514T145214",
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

_source line 2 · 2026-05-14T14:53:08.941760+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_mvp2_all_status_20260514T145214",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T14:53:08.942045+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ps -p 53066,55410,53144,53287 -o pid,etime,rss,%cpu,args --no-headers",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_mvp2_all_status_20260514T145214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ps -p 53066,55410,53144,53287 -o pid,etime,rss,%cpu,args --no-headers",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T14:53:08.942322+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \" 53066    02:20:46  3476  0.0 bash -c rm -f /tmp/agent-ml-exit/mvp2_grpo_ced_r5.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/faith-evidence-ie/mvp2_grpo_ced_r5.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/mvp2_grpo_ced_r5.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/autodl-tmp/freige && export CUDA_VISIBLE_DEVICES=0 && timeout 86400 env bash -c 'bash -c \\\"source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.training.grpo_trainer --model_name /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_dir /root/autodl-tmp/data/docred --stage 3 --tau_start 0.3 --tau_end 0.5 --output_dir /root/autodl-tmp/grpo_ced_r5 --num_generations 4 --reward_device cpu --per_device_batch_size 1 --gradient_accumulation_steps 16 --num_epochs 1 --learning_rate 5e-5 --seed 42 --kl_coef 0.0 --save_steps 20 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --num_iterations 1 --wandb_run_name grpo-s3-ced-r5\\\"'; } > ~/runs/faith-evidence-ie/mvp2_grpo_ced_r5.log 2>&1\\n 53144    02:20:43  3608  0.0 bash -c rm -f /tmp/agent-ml-exit/mvp2_grpo_extract_r3.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/faith-evidence-ie/mvp2_grpo_extract_r3.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/mvp2_grpo_extract_r3.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/autodl-tmp/freige && export CUDA_VISIBLE_DEVICES=2 && timeout 86400 env bash -c 'ba
…[truncated 2475 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_mvp2_all_status_20260514T145214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T14:53:08.942550+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_mvp2_all_status_20260514T145214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T14:53:08.942742+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"53071, GPU-7717ada7-a310-5d90-cecf-d3e06c550631, 13068 MiB\\n53149, GPU-5e7d7885-fdf1-b3bc-7704-7e963b3aeb27, 13066 MiB\\n53292, GPU-80915638-bf23-e98d-aa94-e7a54c03b634, 13056 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_mvp2_all_status_20260514T145214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T14:53:08.942935+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tail -50 /root/runs/faith-evidence-ie/mvp2_grpo_ced_r5.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_mvp2_all_status_20260514T145214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tail -50 /root/runs/faith-evidence-ie/mvp2_grpo_ced_r5.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T14:53:08.943206+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{'loss': -0.005, 'grad_norm': 3.203125, 'learning_rate': 3.683862433862434e-05, 'num_tokens': 1683891.0, 'completions/mean_length': 34.0875, 'completions/min_length': 32.2, 'completions/max_length': 35.4, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 34.0875, 'completions/min_terminated_length': 32.2, 'completions/max_terminated_length': 35.4, 'rewards/format_reward_fn/mean': 0.29662501215934756, 'rewards/format_reward_fn/std': 0.013500000536441802, 'rewards/f1_reward_fn/mean': 0.0, 'rewards/f1_reward_fn/std': 0.0, 'rewards/ced_reward/mean': 0.9788446307182312, 'rewards/ced_reward/std': 0.05528133767656982, 'reward': 1.2754696130752563, 'reward_std': 0.06877749341074377, 'frac_reward_zero_std': 0.8, 'entropy': 0.012598223834629607, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'step_time': 13.938240689237137, 'epoch': 0.26}\\n\\r 27%|██▋       | 205/756 [1:17:23<2:05:14, 13.64s/it]\\r 27%|██▋       | 206/756 [1:17:36<2:02:05, 13.32s/it]\\r 27%|██▋       | 207/756 [1:17:52<2:09:40, 14.17s/it]\\r 28%|██▊       | 208/756 [1:18:04<2:05:22, 13.73s/it]\\r 28%|██▊       | 209/756 [1:18:17<2:01:37, 13.34s/it]\\r 28%|██▊       | 210/756 [1:18:30<2:00:27, 13.24s/it]\\r                                                     \\r\\r 28%|██▊       | 210/756 [1:18:30<2:00:27, 13.24s/it]\\r 28%|██▊       | 211/756 [1:18:42<1:57:54, 12.98s/it]\\r 28%|██▊       | 212/756 [1:18:55<1:56:50, 12.89s/it]\\r 28%|██▊       | 213/756 [1:19:08<1:56:59, 12.93s/it]\\r 28%|██▊       | 214/756 [1:19:21<1:57:36, 13.02s/it]\\r 28%|██▊       | 215/756 [1:19:34<1:56:03, 12.87s/it]\\r                                                     \\r\\r 28%|██▊       | 215/756 [1:19:34<1:56:03, 12.87s/it]\\r 29%|██▊       | 216/756 [1:19:47<1:56:05, 12.90s/it]\\r 29%|██▊       | 217/756 [1:20:07<2:14:38, 14.99s/it]\\r 29%|██▉       | 218/7
…[truncated 6438 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_mvp2_all_status_20260514T145214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T14:53:08.943453+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tail -50 /root/runs/faith-evidence-ie/mvp2_sft_eval_r2.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_mvp2_all_status_20260514T145214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tail -50 /root/runs/faith-evidence-ie/mvp2_sft_eval_r2.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T14:53:08.943703+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-14 22:34:07,040 WARNING Failed to parse output for doc Ålgård Line\\n2026-05-14 22:34:07,040 WARNING Failed to parse output for doc Blue River (Colorado)\\n2026-05-14 22:34:07,040 WARNING Failed to parse output for doc Sycamore Canyon Wilderness\\n2026-05-14 22:34:07,041 WARNING Failed to parse output for doc Kahului Airport\\n2026-05-14 22:34:07,041 WARNING Failed to parse output for doc Ulysses (novel)\\n2026-05-14 22:34:07,041 WARNING Failed to parse output for doc John Ripley (USMC)\\n2026-05-14 22:34:07,041 WARNING Failed to parse output for doc Oleg Tinkov\\n2026-05-14 22:34:07,041 WARNING Failed to parse output for doc Henri de Buade\\n2026-05-14 22:34:07,041 WARNING Failed to parse output for doc List of composers of Caribbean descent\\n2026-05-14 22:34:07,042 WARNING Failed to parse output for doc Cy Becker, Edmonton\\n2026-05-14 22:34:07,042 WARNING Failed to parse output for doc Mount Shinn\\n2026-05-14 22:34:07,042 WARNING Failed to parse output for doc John D. McWilliams\\n2026-05-14 22:34:07,042 WARNING Failed to parse output for doc Anthony G. Brown\\n2026-05-14 22:34:07,042 WARNING Failed to parse output for doc Extraordinary Merry Christmas\\n2026-05-14 22:34:07,042 WARNING Failed to parse output for doc Çağlar Söyüncü\\n2026-05-14 22:34:07,043 WARNING Failed to parse output for doc Ne crois pas\\n2026-05-14 22:34:07,043 WARNING Failed to parse output for doc Arcadia (band)\\n2026-05-14 22:34:07,043 WARNING Failed to parse output for doc Anton Erhard Martinelli\\n2026-05-14 22:34:07,043 WARNING Failed to parse output for doc Panlongcheng\\n2026-05-14 22:34:07,043 WARNING Failed to parse output for doc Laurence M. Keitt\\n2026-05-14 22:34:07,043 WARNING Failed to parse output for doc TY.O\\n2026-05-14 22:34:07,043 WARNING Failed to parse output for doc Mendenhall Glacier\\n2026-05-14 22:34:07,043 WARNING Failed to parse output for doc Signaling of the New York City Subway\\n2026-05-14 22
…[truncated 1776 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_mvp2_all_status_20260514T145214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T14:53:08.943923+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tail -50 /root/runs/faith-evidence-ie/mvp2_grpo_extract_r3.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_mvp2_all_status_20260514T145214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tail -50 /root/runs/faith-evidence-ie/mvp2_grpo_extract_r3.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T14:53:08.944193+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 3.617724867724868e-05, 'num_tokens': 1850833.0, 'completions/mean_length': 45.85, 'completions/min_length': 42.0, 'completions/max_length': 50.2, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 45.85, 'completions/min_terminated_length': 42.0, 'completions/max_terminated_length': 50.2, 'rewards/format_reward_fn/mean': 0.30000001192092896, 'rewards/format_reward_fn/std': 0.0, 'rewards/f1_reward_fn/mean': 0.184344020485878, 'rewards/f1_reward_fn/std': 0.198211407661438, 'reward': 0.48434402942657473, 'reward_std': 0.198211407661438, 'frac_reward_zero_std': 1.0, 'entropy': 0.013842725711037928, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'step_time': 12.652254241390619, 'epoch': 0.28}\\n{'loss': -0.0, 'grad_norm': 0.0, 'learning_rate': 3.584656084656085e-05, 'num_tokens': 1889590.0, 'completions/mean_length': 45.3625, 'completions/min_length': 41.2, 'completions/max_length': 48.8, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 45.3625, 'completions/min_terminated_length': 41.2, 'completions/max_terminated_length': 48.8, 'rewards/format_reward_fn/mean': 0.30000001192092896, 'rewards/format_reward_fn/std': 0.0, 'rewards/f1_reward_fn/mean': 0.24031619727611542, 'rewards/f1_reward_fn/std': 0.2987968310713768, 'reward': 0.5403162121772767, 'reward_std': 0.2987968042492867, 'frac_reward_zero_std': 0.95, 'entropy': 0.020305151037609902, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'step_time': 12.319173102203058, 'epoch': 0.28}\\n{'loss': 0.0013, 'grad_norm': 0.0, 'learning_rate': 3.551587301587302e-05, 'num_tokens': 1929820.0, 'completions/mean_length': 43.625, 'completions/min_length': 39.6, 'completions/max_length': 47.6, 'compl
…[truncated 6308 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_mvp2_all_status_20260514T145214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T14:53:08.944430+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tail -50 /root/runs/faith-evidence-ie/mvp2_grpo_flatnli_r3.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_mvp2_all_status_20260514T145214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tail -50 /root/runs/faith-evidence-ie/mvp2_grpo_flatnli_r3.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T14:53:08.944703+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"设置成功\\n注意：仅限于学术用途和加速访问github/huggingface，不承诺稳定性保证\\n/root/miniconda3/lib/python3.12/site-packages/trl/generation/__init__.py:22: UserWarning: TRL currently supports vLLM versions from 0.11.0 to 0.17.1. You have version 0.18.1 installed. We recommend installing a supported version to avoid compatibility issues.\\n  if is_vllm_available():\\n/root/miniconda3/lib/python3.12/site-packages/trl/generation/vllm_client.py:40: UserWarning: TRL currently supports vLLM versions from 0.11.0 to 0.17.1. You have version 0.18.1 installed. We recommend installing a supported version to avoid compatibility issues.\\n  if is_vllm_available():\\n/root/miniconda3/lib/python3.12/site-packages/trl/generation/vllm_generation.py:36: UserWarning: TRL currently supports vLLM versions from 0.11.0 to 0.17.1. You have version 0.18.1 installed. We recommend installing a supported version to avoid compatibility issues.\\n  if is_vllm_available():\\n2026-05-14 20:32:03,908 INFO Loading tokenizer: /root/autodl-tmp/models/Qwen3-4B\\n2026-05-14 20:32:04,216 INFO Preparing dataset...\\n2026-05-14 20:32:04,397 INFO Loaded 3053 documents from /root/autodl-tmp/data/docred/train_annotated.json\\n2026-05-14 20:32:05,163 INFO Processed 38180 relation samples from 3053 documents (17312 samples without hard negatives)\\n2026-05-14 20:32:05,592 INFO Prepared 3027 GRPO prompts\\n2026-05-14 20:32:05,692 INFO Loading model: /root/autodl-tmp/models/Qwen3-4B\\n2026-05-14 20:32:05,692 INFO Using 4-bit QLoRA quantization\\n\\rLoading checkpoint shards:   0%|          | 0/3 [00:00<?, ?it/s]\\rLoading checkpoint shards:  33%|███▎      | 1/3 [00:03<00:06,  3.01s/it]\\rLoading checkpoint shards:  67%|██████▋   | 2/3 [00:06<00:03,  3.28s/it]\\rLoading checkpoint shards: 100%|██████████| 3/3 [00:06<00:00,  2.19s/it]\\n2026-05-14 20:32:12,658 INFO Loading SFT adapter from /root/autodl-tmp/sft_output\\n/root/miniconda3/lib/python3.12/site-packages/peft/tuners/lora/bnb.p
…[truncated 6435 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_mvp2_all_status_20260514T145214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-14T14:53:08.945003+00:00_

## 实验状态汇总

| 实验 | 状态 | 进度 | 速度 | 预估剩余 | GPU 显存 |
|------|------|------|------|----------|---------|
| **mvp2_grpo_ced_r5** | 运行中 | 477/756 (63%) | ~12.7s/it | ~59 min | 13068 MiB |
| **mvp2_sft_eval_r2** | **已完成** (exit 0) | 985/985 | — | — | 已释放 |
| **mvp2_grpo_extract_r3** | 运行中 | 477/756 (63%) | ~12.0s/it | ~56 min | 13066 MiB |
| **mvp2_grpo_flatnli_r3** | 运行中 | 81/756 (11%) | ~124s/it | **~23h** | 13056 MiB |

### 详细指标

**mvp2_grpo_ced_r5** (cuda:0) — epoch 0.58
- reward: 1.199, ced_reward: 0.899, f1_reward: 0.0, format: 0.3
- f1_reward 一直为 0，entropy 已降至 0.0005（近乎坍缩）

**mvp2_sft_eval_r2** (cuda:1) — 成功完成
- F1: **0.4057**, Ign-F1: 0.4057, Evi-F1: **0.7979**, EDCR: **0.7118**
- Format OK: 983/985 (99.8%), Truncated: 367/985 (37.3%)
- 有大量 "Failed to parse output" 警告

**mvp2_grpo_extract_r3** (cuda:2) — epoch 0.60
- reward: 0.502, f1_reward: 0.202, format: 0.3
- f1_reward 在 0.14-0.25 之间波动，有学到但不稳定

**mvp2_grpo_flatnli_r3** (cuda:3) — epoch 0.05
- reward: 1.160, flat_nli_reward: 0.796, f1_reward: 0.067, format: 0.297
- 速度比其他 GRPO 慢 **10 倍**（~124s/it vs ~12s/it），原因是 NLI reward 计算在 CPU 上
- 按当前速度需要再跑约 23 小时

### 值得关注

1. **ced_r5 的 f1_reward=0** — 模型只优化了 ced_reward，三元组抽取能力未提升，entropy 极低说明输出已坍缩到固定模式
2. **flatnli_r3 极慢** — NLI 模型推理在 CPU 上，严重拖慢训练。cuda:1 已空出，如果可以把 NLI 模型放到 GPU 上会快很多
3. **sft_eval 的 truncated 37%** — 超过三分之一的预测被截断，可能影响 F1

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_check_mvp2_all_status_20260514T145214"
}
```

</details>

---
