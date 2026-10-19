# code prepare stat analysis

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/chats/worker_code_prepare_stat_analysis_20260514T150704.jsonl`
- **Structured JSON:** [`0f6f1a764b034ebe1ce7.json`](../../sessions/0f/0f6f1a764b034ebe1ce7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

31 recorded events

### Tool call

_source line 1 · 2026-05-14T15:09:33.744058+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__detect_image,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_prepare_stat_analysis_20260514T150704",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__detect_image,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T15:09:33.744393+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_prepare_stat_analysis_20260514T150704",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T15:09:33.744563+00:00_

called mcp__agent-ml-research__detect_image

<details open><summary>🔧 Tool call — mcp__agent-ml-research__detect_image</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_prepare_stat_analysis_20260514T150704",
  "tool": "mcp__agent-ml-research__detect_image",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T15:09:33.744729+00:00_

{"result":"{\n  \"detected\": false,\n  \"status\": \"unknown\",\n  \"skip_base_setup\": false,\n  \"message\": \"No image marker file found. Use traditional env-setup flow.\"\n}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_prepare_stat_analysis_20260514T150704",
  "tool": "mcp__agent-ml-research__detect_image",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T15:09:33.744858+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls -la /root/runs/m2_full_qwen/ /root/runs/m2_full_starcoder/ 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_prepare_stat_analysis_20260514T150704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "ls -la /root/runs/m2_full_qwen/ /root/runs/m2_full_starcoder/ 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T15:09:33.744981+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_prepare_stat_analysis_20260514T150704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T15:09:33.745100+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls /root/structfuse/analysis/ 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_prepare_stat_analysis_20260514T150704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "ls /root/structfuse/analysis/ 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T15:09:33.745219+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_prepare_stat_analysis_20260514T150704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T15:09:33.745346+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls -la /root/runs/m2_full_qwen/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_prepare_stat_analysis_20260514T150704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "ls -la /root/runs/m2_full_qwen/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T15:09:33.745471+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 16\\ndrwxr-xr-x 2 root root   89 May 14 19:24 .\\ndrwxr-xr-x 6 root root  122 May 14 00:26 ..\\n-rw-r--r-- 1 root root 6979 May 14 19:24 random_s42.log\\n-rw-r--r-- 1 root root 1897 May 14 23:00 random_s43.log\\n-rw-r--r-- 1 root root 2042 May 14 23:00 s43plus_all.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_prepare_stat_analysis_20260514T150704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T15:09:33.745587+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls -la /root/runs/m2_full_starcoder/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_prepare_stat_analysis_20260514T150704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "ls -la /root/runs/m2_full_starcoder/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T15:09:33.745739+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls /root/structfuse/analysis/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_prepare_stat_analysis_20260514T150704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "ls /root/structfuse/analysis/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T15:09:33.745862+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 8\\ndrwxr-xr-x 2 root root   28 May 14 02:30 .\\ndrwxr-xr-x 6 root root  122 May 14 00:26 ..\\n-rw-r--r-- 1 root root 5062 May 14 23:05 random_s42.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_prepare_stat_analysis_20260514T150704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T15:09:33.745982+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"negative_difficulty.py\\nnegative_difficulty_margin.py\\nnegative_difficulty_margin_v2.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_prepare_stat_analysis_20260514T150704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T15:09:33.746107+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "grep \"eval\" /root/runs/m2_full_qwen/random_s42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_prepare_stat_analysis_20260514T150704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "grep \"eval\" /root/runs/m2_full_qwen/random_s42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T15:09:33.746232+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  [eval@500] {'val_loss': 0.486931758338973, 'recall@1': 0.5332214765100671, 'recall@5': 0.9540268456375839, 'recall@10': 1.0}\\n  [eval@1000] {'val_loss': 0.4650662785708504, 'recall@1': 0.5526845637583893, 'recall@5': 0.9593959731543624, 'recall@10': 1.0}\\n  [eval@1500] {'val_loss': 0.5364526285221113, 'recall@1': 0.5228187919463088, 'recall@5': 0.9550335570469799, 'recall@10': 1.0}\\n  [eval@2000] {'val_loss': 0.5162166327238082, 'recall@1': 0.5228187919463088, 'recall@5': 0.9543624161073826, 'recall@10': 1.0}\\n  [eval@2500] {'val_loss': 0.5264100839827685, 'recall@1': 0.5268456375838926, 'recall@5': 0.9563758389261745, 'recall@10': 1.0}\\n  [eval@3000] {'val_loss': 0.5405804200060416, 'recall@1': 0.5355704697986577, 'recall@5': 0.9493288590604027, 'recall@10': 1.0}\\n  [eval@3500] {'val_loss': 0.5600887083367213, 'recall@1': 0.5335570469798657, 'recall@5': 0.9493288590604027, 'recall@10': 1.0}\\n  [eval@4000] {'val_loss': 0.5509598255757517, 'recall@1': 0.5345637583892617, 'recall@5': 0.9439597315436241, 'recall@10': 1.0}\\n[Final eval] {'val_loss': 0.545638095677499, 'recall@1': 0.5503355704697986, 'recall@5': 0.9463087248322147, 'recall@10': 1.0}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_prepare_stat_analysis_20260514T150704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T15:09:33.746356+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "grep \"eval\" /root/runs/m2_full_starcoder/random_s42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_prepare_stat_analysis_20260514T150704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "grep \"eval\" /root/runs/m2_full_starcoder/random_s42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T15:09:33.746477+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  [eval@500] {'val_loss': 0.6194413630354324, 'recall@1': 0.43523489932885906, 'recall@5': 0.9053691275167786, 'recall@10': 1.0}\\n  [eval@1000] {'val_loss': 0.6134329466611746, 'recall@1': 0.45369127516778524, 'recall@5': 0.9201342281879195, 'recall@10': 1.0}\\n  [eval@1500] {'val_loss': 0.6528317997919633, 'recall@1': 0.448993288590604, 'recall@5': 0.9057046979865772, 'recall@10': 1.0}\\n  [eval@2000] {'val_loss': 0.6698005872284806, 'recall@1': 0.44563758389261743, 'recall@5': 0.9006711409395973, 'recall@10': 1.0}\\n  [eval@2500] {'val_loss': 0.63417182392722, 'recall@1': 0.4604026845637584, 'recall@5': 0.911744966442953, 'recall@10': 1.0}\\n  [eval@3000] {'val_loss': 0.6516175848925674, 'recall@1': 0.45436241610738254, 'recall@5': 0.9077181208053692, 'recall@10': 1.0}\\n  [eval@3500] {'val_loss': 0.658796566324746, 'recall@1': 0.4533557046979866, 'recall@5': 0.9057046979865772, 'recall@10': 1.0}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_prepare_stat_analysis_20260514T150704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T15:09:33.746631+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cat /root/runs/m2_full_qwen/random_s43.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_prepare_stat_analysis_20260514T150704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "cat /root/runs/m2_full_qwen/random_s43.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T15:09:33.746793+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"wandb: Tracking run with wandb version 0.26.0\\nwandb: W&B syncing is set to `offline` in this directory. Run `wandb online` or set WANDB_MODE=online to enable cloud syncing.\\nwandb: Run data is saved locally in /root/autodl-tmp/structfuse/wandb_logs/wandb/offline-run-20260514_192418-ejygo7zh\\n\\rLoading checkpoint shards:   0%|          | 0/2 [00:00<?, ?it/s]\\rLoading checkpoint shards:  50%|█████     | 1/2 [00:01<00:01,  1.11s/it]\\rLoading checkpoint shards: 100%|██████████| 2/2 [00:01<00:00,  1.55it/s]\\rLoading checkpoint shards: 100%|██████████| 2/2 [00:01<00:00,  1.40it/s]\\n[Epoch 1] Using pre-mined negatives (random)...\\n  Training loop start: 1405 batches/epoch, total_steps_per_epoch=1405\\n`use_cache=True` is incompatible with gradient checkpointing. Setting `use_cache=False`.\\n  step 50  loss=0.6791  lr=3.56e-06\\n  step 100  loss=0.7159  lr=7.05e-06\\n  step 150  loss=0.4708  lr=1.06e-05\\n  step 200  loss=0.4745  lr=1.41e-05\\n  step 250  loss=0.4925  lr=1.77e-05\\n  step 300  loss=0.2247  lr=2.00e-05\\n  step 350  loss=0.4937  lr=2.00e-05\\n  step 400  loss=0.2275  lr=1.99e-05\\n  step 450  loss=0.3402  lr=1.98e-05\\n  step 500  loss=0.3376  lr=1.96e-05\\n  [eval@500] {'val_loss': 0.4476428985947238, 'recall@1': 0.5357142857142857, 'recall@5': 0.9698558322411533, 'recall@10': 1.0}\\n  New best val_loss=0.4476, saved to /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_val_loss\\n  New best R@1=0.5357, saved to /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1\\n  step 550  loss=0.2363  lr=1.95e-05\\n  step 600  loss=0.2311  lr=1.92e-05\\n  step 650  loss=0.0693  lr=1.90e-05\\n  step 700  loss=0.4121  lr=1.87e-05\\n  step 750  loss=0.2342  lr=1.84e-05\\n  step 800  loss=0.2746  lr=1.80e-05\\n  step 850  loss=0.0410  lr=1.76e-05\\n  step 900  loss=0.1186  lr=1.72e-05\\n  step 950  loss=0.1993  lr=1.68e-05\\n\", \"stderr\": \"\", \"return_
…[truncated 73 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_prepare_stat_analysis_20260514T150704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T15:09:33.746936+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/runs/m2_full_qwen -name \"*.log\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_prepare_stat_analysis_20260514T150704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "find /root/runs/m2_full_qwen -name \"*.log\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T15:09:33.747065+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/runs/m2_full_qwen/random_s42.log\\n/root/runs/m2_full_qwen/s43plus_all.log\\n/root/runs/m2_full_qwen/random_s43.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_prepare_stat_analysis_20260514T150704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T15:09:33.747201+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen -maxdepth 2 -type d",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_prepare_stat_analysis_20260514T150704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "find /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen -maxdepth 2 -type d",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T15:09:33.747327+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_val_loss\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/final\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_val_loss\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_prepare_stat_analysis_20260514T150704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T15:09:33.747527+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cat << 'PYEOF' > /root/structfuse/analysis/m2_stat_analysis.py\n#!/usr/bin/env python3\n\"\"\"M2 Full experiment statistical analysis.\n\nReads eval results from training logs across 3 strategies × 3 seeds × 2 encoders,\nperforms paired t-tests, bootstrap CIs, Cohen's d, and encoder×strategy interaction test.\n\nDependencies: numpy, scipy (both in conda base).\nUsage: python m2_stat_analysis.py [--json PATH] [--help]\n\"\"\"\n\nimport argparse\nimport ast\nimport json\nimport os\nimport re\nimport sys\nfrom collections import defaultdict\nfrom itertools import combinations\n\nimport numpy as np\nfrom scipy import stats\n\n# ─── Configuration ───────────────────────────────────────────────────────────\n\nENCODERS = [\"qwen\", \"starcoder\"]\nSTRATEGIES = [\"random\", \"embedding_distance\", \"dataflow_aware\"]\nSEEDS = [42, 43, 44]\n\nLOG_DIRS = {\n    \"qwen\": \"/root/runs/m2_full_qwen\",\n    \"starcoder\": \"/root/runs/m2_full_starcoder\",\n}\n\nMETRICS = [\"recall@1\", \"val_loss\"]\nBOOTSTRAP_N = 10000\nALPHA = 0.05\n\n\n# ─── Data Loading ────────────────────────────────────────────────────────────\n\ndef parse_eval_lines(log_path):\n    \"\"\"Parse all eval entries from a training log, return list of dicts.\"\"\"\n    evals = []\n    pattern = re.compile(r'\\[(?:eval@(\\d+)|Final eval)\\]\\s*(\\{.*\\})')\n    with open(log_path) as f:\n        for line in f:\n            m = pattern.search(line)\n            if m:\n                step = int(m.group(1)) if m.group(1) else -1\n                metrics = ast.literal_eval(m.group(2))\n                metrics[\"step\"] = step\n                evals.append(metrics)\n    return evals\n\n\ndef extract_best_metrics(evals):\n    \"\"\"From a list of eval dicts, extract best R@1 and best val_loss.\"\"\"\n    if not evals:\n        return None\n    best_r1 = max(evals, key=lambda e: e.get(\"recall@1\", 0))\n    best_vl = min(evals, key=lambda e: e.get(\"val_loss\", float(\"inf\")))\n    return {\n        \"best_recall@1\": best_r1[\"recall@1\"],\n        \"best_recall@1_step\": best_r1[\"step\"],\n        \"best_val_loss\": best_vl[\"val_loss\"],\n        \"best_val_loss_step\": best_vl[\"step\"],\n        \"num_evals\": len(evals),\n        \"is_complete\": any(e[\"step\"] == -1 for e in evals),\n    }\n\n\ndef load_all_results():\n    \"\"\"Load results from all available logs. Returns nested dict: results[encoder][strategy][seed].\"\"\"\n    results = defaultdict(lambda: defaultdict(dict))\n    missing = []\n    for enc in ENCODERS:\n        log_dir = LOG_DIRS[enc]\n        for strat in STRATEGIES:\n            for seed in SEEDS:\n                log_path = os.path.join(log_dir, f\"{strat}_s{seed}.log\")\n                if not os.path.exists(log_path):\n                    missing.append(f\"{enc}/{strat}_s{seed}\")\n                    continue\n                evals = parse_eval_lines(log_path)\n                if not evals:\n                    missing.append(f\"{enc}/{strat}_s{seed} (no eval lines)\")\n                    continue\n                best = extract_best_metrics(evals)\n                results[enc][strat][seed] = best\n    return dict(results), missing\n\n\n# ─── Statistical Tests ───────────────────────────────────────────────────────\n\ndef paired_ttest(vals_a, vals_b):\n    \"\"\"Paired t-test. Returns t-stat, p-value, and n.\"\"\"\n    paired = [(a, b) for a, b in zip(vals_a, vals_b) if a is not None and b is not None]\n    if len(paired) < 2:\n        return {\"t\": np.nan, \"p\": np.nan, \"n\": len(paired), \"insufficient\": True}\n    a, b = zip(*paired)\n    t_stat, p_val = stats.ttest_rel(a, b)\n    return {\"t\": float(t_stat), \"p\": float(p_val), \"n\": len(paired), \"insufficient\": False}\n\n\ndef cohens_d(vals_a, vals_b):\n    \"\"\"Cohen's d for paired samples.\"\"\"\n    diffs = [a - b for a, b in zip(vals_a, vals_b) if a is not None and b is not None]\n    if len(diffs) < 2:\n        return np.nan\n    return float(np.mean(diffs) / np.std(diffs, ddof=1))\n\n\ndef bootstrap_ci(values, n_boot=BOOTSTRAP_N, ci=0.95):\n    \"\"\"Bootstrap confidence interval for the mean.\"\"\"\n    values = [v for v in values if v is not None]\n    if len(values) < 2:\n        return {\"mean\": float(values[0]) if values else np.nan,\n                \"ci_lo\": np.nan, \"ci_hi\": np.nan, \"n\": len(values)}\n    rng = np.random.default_rng(seed=0)\n    boot_means = []\n    arr = np.array(values)\n    for _ in range(n_boot):\n        sample = rng.choice(arr, size=len(arr), replace=True)\n        boot_means.append(np.mean(sample))\n    boot_means = np.array(boot_means)\n    lo = np.percentile(boot_means, (1 - ci) / 2 * 100)\n    hi = np.percentile(boot_means, (1 + ci) / 2 * 100)\n    return {\"mean\": float(np.mean(values)), \"ci_lo\": float(lo), \"ci_hi\": float(hi),\n            \"n\": len(values), \"std\": float(np.std(values, ddof=1))}\n\n\ndef interaction_test(results, metric_key):\n    \"\"\"2-way encoder × strategy interaction via 2-way ANOVA-like permutation test.\n\n    With n=3 we don't have enough power for a proper ANOVA, so we compute\n    the interaction contrast (difference of differences) and report it descriptively.\n    \"\"\"\n    contrasts = {}\n    for strat in [\"embedding_distance\", \"dataflow_aware\"]:\n        diffs = {}\n        for enc in ENCODERS:\n            strat_vals = get_metric_values(results, enc, strat, metric_key)\n            rand_vals = get_metric_values(results, enc, \"random\", metric_key)\n            paired = [(s - r) for s, r in zip(strat_vals, rand_vals) if s is not None and r is not None]\n            diffs[enc] = paired\n        if diffs.get(\"qwen\") and diffs.get(\"starcoder\"):\n            q_mean = np.mean(diffs[\"qwen\"])\n            s_mean = np.mean(diffs[\"starcoder\"])\n            contrasts[strat] = {\n                \"qwen_delta\": float(q_mean),\n                \"starcoder_delta\": float(s_mean),\n                \"interaction\": float(q_mean - s_mean),\n                \"interpretation\": (\n                    f\"Qwen benefit: {q_mean*100:+.2f}pp, StarCoder benefit: {s_mean*100:+.2f}pp, \"\n                    f\"interaction (Qwen-StarCoder): {(q_mean-s_mean)*100:+.2f}pp\"\n                ),\n            }\n        else:\n            contrasts[strat] = {\"insufficient_data\": True}\n    return contrasts\n\n\ndef get_metric_values(results, encoder, strategy, metric_key):\n    \"\"\"Get metric values for all seeds, returning None for missing seeds.\"\"\"\n    vals = []\n    for seed in SEEDS:\n        entry = results.get(encoder, {}).get(strategy, {}).get(seed)\n        if entry:\n            vals.append(entry.get(metric_key))\n        else:\n            vals.append(None)\n    return vals\n\n\n# ─── Analysis ────────────────────────────────────────────────────────────────\n\ndef run_analysis(results):\n    \"\"\"Run all statistical tests. Returns structured dict.\"\"\"\n    output = {\n        \"metadata\": {\n            \"seeds\": SEEDS,\n            \"n_per_cell\": len(SEEDS),\n            \"df\": len(SEEDS) - 1,\n            \"warning\": \"n=3, df=2, high Type II error risk. Non-significant results should NOT be interpreted as null effects.\",\n            \"bootstrap_resamples\": BOOTSTRAP_N,\n            \"alpha\": ALPHA,\n        },\n        \"descriptives\": {},\n        \"pairwise_tests\": {},\n        \"bootstrap_cis\": {},\n        \"interaction\": {},\n        \"claims\": {},\n    }\n\n    metric_key = \"best_recall@1\"\n\n    # Descriptives and bootstrap CIs\n    for enc in ENCODERS:\n        output[\"descriptives\"][enc] = {}\n        output[\"bootstrap_cis\"][enc] = {}\n        for strat in STRATEGIES:\n            vals = get_metric_values(results, enc, strat, metric_key)\n            valid = [v for v in vals if v is not None]\n            output[\"descriptives\"][enc][strat] = {\n                \"values\": [float(v) if v is not None else None for v in vals],\n                \"mean\": float(np.mean(valid)) if valid else None,\n                \"std\": float(np.std(valid, ddof=1)) if len(valid) > 1 else None,\n                \"n\": len(valid),\n            }\n            output[\"bootstrap_cis\"][enc][strat] = bootstrap_ci(valid)\n\n    # Pairwise tests: embedding vs random, dataflow vs random\n    for enc in ENCODERS:\n        output[\"pairwise_tests\"][enc] = {}\n        rand_vals = get_metric_values(results, enc, \"random\", metric_key)\n        for strat in [\"embedding_distance\", \"dataflow_aware\"]:\n            strat_vals = get_metric_values(results, enc, strat, metric_key)\n            tt = paired_ttest(strat_vals, rand_vals)\n            d = cohens_d(strat_vals, rand_vals)\n            output[\"pairwise_tests\"][enc][f\"{strat}_vs_random\"] = {\n                \"paired_ttest\": tt,\n                \"cohens_d\": float(d) if not np.isnan(d) else None,\n                \"mean_diff\": float(np.nanmean([s - r for s, r in zip(strat_vals, rand_vals)\n                                                if s is not None and r is not None])) if any(\n                    s is not None and r is not None for s, r in zip(strat_vals, rand_vals)) else None,\n            }\n\n    # Interaction\n    output[\"interaction\"] = interaction_test(results, metric_key)\n\n    # Claim adjudication\n    output[\"claims\"] = adjudicate_claims(output)\n\n    return output\n\n\ndef adjudicate_claims(output):\n    \"\"\"Evaluate paper claims against statistical evidence.\"\"\"\n    claims = {}\n\n    # Claim 1: embedding_distance > random (both encoders)\n    c1_parts = []\n    for enc in ENCODERS:\n        test = output[\"pairwise_tests\"].get(enc, {}).get(\"embedding_distance_vs_random\", {})\n        tt = test.get(\"paired_ttest\", {})\n        d = test.get(\"mean_diff\")\n        if tt.get(\"insufficient\"):\n            c1_parts.append(f\"{enc}: insufficient data\")\n        else:\n            sig = \"p<0.05\" if tt[\"p\"] < ALPHA else f\"p={tt['p']:.3f} (n.s.)\"\n            direction = \"positive\" if (d is not None and d > 0) else \"negative/zero\"\n            c1_parts.append(f\"{enc}: {sig}, direction={direction}, Δ={d*100:.2f}pp\" if d is not None else f\"{enc}: {sig}\")\n\n    claims[\"claim1_embedding_gt_random\"] = {\n        \"description\": \"embedding_distance > random (expected: consistent positive, pilot +1.6~2.0pp)\",\n        \"per_encoder\": c1_parts,\n    }\n\n    # Claim 2: dataflow conditional benefit (Qwen positive, StarCoder neutral)\n    c2_parts = []\n    inter = output[\"interaction\"].get(\"dataflow_aware\", {})\n    for enc in ENCODERS:\n        test = output[\"pairwise_tests\"].get(enc, {}).get(\"dataflow_aware_vs_random\", {})\n        tt = test.get(\"paired_ttest\", {})\n        d = test.get(\"mean_diff\")\n        if tt.get(\"insufficient\"):\n            c2_parts.append(f\"{enc}: insufficient data\")\n        else:\n            sig = \"p<0.05\" if tt[\"p\"] < ALPHA else f\"p={tt['p']:.3f} (n.s.)\"\n            c2_parts.append(f\"{enc}: {sig}, Δ={d*100:.2f}pp\" if d is not None else f\"{enc}: {sig}\")\n\n    claims[\"claim2_dataflow_conditional\"] = {\n        \"description\": \"dataflow_aware benefit depends on encoder (Qwen positive, StarCoder neutral)\",\n        \"per_encoder\": c2_parts,\n        \"interaction\": inter if not inter.get(\"insufficient_data\") else \"insufficient data\",\n    }\n\n    return claims\n\n\n# ─── Output Formatting ───────────────────────────────────────────────────────\n\ndef print_report(output):\n    \"\"\"Print formatted report to stdout.\"\"\"\n    meta = output[\"metadata\"]\n    print(\"=\" * 78)\n    print(\"M2 Full Experiment — Statistical Analysis Report\")\n    print(\"=\" * 78)\n    print(f\"  Seeds: {meta['seeds']}  |  n={meta['n_per_cell']} per cell  |  df={meta['df']}\")\n    print(f\"  ⚠  {meta['warning']}\")\n    print()\n\n    # Descriptives table\n    print(\"─\" * 78)\n    print(\"R@1 Descriptives (best checkpoint)\")\n    print(\"─\" * 78)\n    print(f\"  {'Encoder':<12} {'Strategy':<22} {'Mean':>8} {'±Std':>8} {'n':>4}  {'95% CI':>20}\")\n    print(f\"  {'─'*12} {'─'*22} {'─'*8} {'─'*8} {'─'*4}  {'─'*20}\")\n    for enc in ENCODERS:\n        for strat in STRATEGIES:\n            desc = output[\"descriptives\"][enc][strat]\n            ci = output[\"bootstrap_cis\"][enc][strat]\n            mean_s = f\"{desc['mean']*100:.2f}%\" if desc[\"mean\"] is not None else \"N/A\"\n            std_s = f\"{desc['std']*100:.2f}\" if desc[\"std\"] is not None else \"N/A\"\n            ci_s = f\"[{ci['ci_lo']*100:.2f}, {ci['ci_hi']*100:.2f}]\" if not np.isnan(ci[\"ci_lo\"]) else \"N/A\"\n            print(f\"  {enc:<12} {strat:<22} {mean_s:>8} {std_s:>8} {desc['n']:>4}  {ci_s:>20}\")\n    print()\n\n    # Pairwise tests\n    print(\"─\" * 78)\n    print(\"Pairwise Comparisons vs Random (paired t-test, R@1)\")\n    print(\"─\" * 78)\n    print(f\"  {'Encoder':<12} {'Comparison':<30} {'Δ(pp)':>8} {'t':>8} {'p':>8} {'d':>8} {'Sig':>6}\")\n    print(f\"  {'─'*12} {'─'*30} {'─'*8} {'─'*8} {'─'*8} {'─'*8} {'─'*6}\")\n    for enc in ENCODERS:\n        for comp_name, comp_data in output[\"pairwise_tests\"][enc].items():\n            tt = comp_data[\"paired_ttest\"]\n            if tt.get(\"insufficient\"):\n                print(f\"  {enc:<12} {comp_name:<30} {'—':>8} {'—':>8} {'—':>8} {'—':>8} {'N/A':>6}\")\n                continue\n            diff_s = f\"{comp_data['mean_diff']*100:+.2f}\" if comp_data[\"mean_diff\"] is not None else \"—\"\n            t_s = f\"{tt['t']:.3f}\"\n            p_s = f\"{tt['p']:.4f}\"\n            d_s = f\"{comp_data['cohens_d']:.3f}\" if comp_data[\"cohens_d\"] is not None else \"—\"\n            sig = \"*\" if tt[\"p\"] < ALPHA else \"n.s.\"\n            print(f\"  {enc:<12} {comp_name:<30} {diff_s:>8} {t_s:>8} {p_s:>8} {d_s:>8} {sig:>6}\")\n    print()\n\n    # Interaction\n    print(\"─\" * 78)\n    print(\"Encoder × Strategy Interaction (R@1)\")\n    print(\"─\" * 78)\n    for strat, inter in output[\"interaction\"].items():\n        if inter.get(\"insufficient_data\"):\n            print(f\"  {strat}: insufficient data\")\n        else:\n            print(f\"  {strat}:\")\n            print(f\"    {inter['interpretation']}\")\n    print()\n\n    # Claims\n    print(\"─\" * 78)\n    print(\"Claim Adjudication\")\n    print(\"─\" * 78)\n    for claim_key, claim_data in output[\"claims\"].items():\n        print(f\"\\n  {claim_key}: {claim_data['description']}\")\n        for line in claim_data[\"per_encoder\"]:\n            print(f\"    • {line}\")\n        if \"interaction\" in claim_data and claim_data[\"interaction\"] != \"insufficient data\":\n            inter = claim_data[\"interaction\"]\n            if isinstance(inter, dict):\n                print(f\"    • interaction: {inter.get('interpretation', 'N/A')}\")\n\n    print()\n    print(\"=\" * 78)\n\n\n# ─── Data Availability Report ────────────────────────────────────────────────\n\ndef print_data_status(results, missing):\n    \"\"\"Print which runs are available and which are missing.\"\"\"\n    print(\"─\" * 78)\n    print(\"Data Availability\")\n    print(\"─\" * 78)\n    total = len(ENCODERS) * len(STRATEGIES) * len(SEEDS)\n    found = sum(1 for enc in results for strat in results[enc] for seed in results[enc][strat])\n    print(f\"  Available: {found}/{total} runs\")\n    if missing:\n        print(f\"  Missing ({len(missing)}):\")\n        for m in missing:\n            print(f\"    • {m}\")\n    else:\n        print(\"  All runs complete.\")\n\n    # Completeness per run\n    for enc in ENCODERS:\n        for strat in STRATEGIES:\n            for seed in SEEDS:\n                entry = results.get(enc, {}).get(strat, {}).get(seed)\n                if entry:\n                    status = \"COMPLETE\" if entry[\"is_complete\"] else f\"IN PROGRESS ({entry['num_evals']} evals)\"\n                    print(f\"    {enc}/{strat}_s{seed}: {status}, best R@1={entry['best_recall@1']*100:.2f}%\")\n    print()\n\n\n# ─── Main ────────────────────────────────────────────────────────────────────\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Statistical analysis for M2 Full experiment (3 strategies × 3 seeds × 2 encoders).\"\n    )\n    parser.add_argument(\"--json\", default=\"/root/structfuse/analysis/m2_stat_results.json\",\n                        help=\"Path to save JSON results (default: %(default)s)\")\n    parser.add_argument(\"--status-only\", action=\"store_true\",\n                        help=\"Only print data availability, skip analysis\")\n    args = parser.parse_args()\n\n    results, missing = load_all_results()\n\n    print_data_status(results, missing)\n\n    if args.status_only:\n        return\n\n    # Need at least 2 seeds for any strategy to run tests\n    can_analyze = False\n    for enc in results:\n        for strat in results[enc]:\n            if len(results[enc][strat]) >= 2:\n                can_analyze = True\n                break\n\n    if not can_analyze:\n        print(\"Not enough data for statistical analysis (need ≥2 seeds per strategy).\")\n        print(\"Re-run when more experiments complete.\")\n        return\n\n    output = run_analysis(results)\n    print_report(output)\n\n    os.makedirs(os.path.dirname(args.json), exist_ok=True)\n    with open(args.json, \"w\") as f:\n        json.dump(output, f, indent=2, default=str)\n    print(f\"JSON results saved to {args.json}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_prepare_stat_analysis_20260514T150704",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "cat << 'PYEOF' > /root/structfuse/analysis/m2_stat_analysis.py\n#!/usr/bin/env python3\n\"\"\"M2 Full experiment statistical analysis.\n\nReads eval results from training logs across 3 strategies × 3 seeds × 2 encoders,\nperforms paired t-tests, bootstrap CIs, Cohen's d, and encoder×strategy interaction test.\n\nDependencies: numpy, scipy (both in conda base).\nUsage: python m2_stat_analysis.py [--json PATH] [--help]\n\"\"\"\n\nimport argparse\nimport ast\nimport json\nimport os\nimport re\nimport sys\nfrom collections import defaultdict\nfrom itertools import combinations\n\nimport numpy as np\nfrom scipy import stats\n\n# ─── Configuration ───────────────────────────────────────────────────────────\n\nENCODERS = [\"qwen\", \"starcoder\"]\nSTRATEGIES = [\"random\", \"embedding_distance\", \"dataflow_aware\"]\nSEEDS = [42, 43, 44]\n\nLOG_DIRS = {\n    \"qwen\": \"/root/runs/m2_full_qwen\",\n    \"starcoder\": \"/root/runs/m2_full_starcoder\",\n}\n\nMETRICS = [\"recall@1\", \"val_loss\"]\nBOOTSTRAP_N = 10000\nALPHA = 0.05\n\n\n# ─── Data Loading ────────────────────────────────────────────────────────────\n\ndef parse_eval_lines(log_path):\n    \"\"\"Parse all eval entries from a training log, return list of dicts.\"\"\"\n    evals = []\n    pattern = re.compile(r'\\[(?:eval@(\\d+)|Final eval)\\]\\s*(\\{.*\\})')\n    with open(log_path) as f:\n        for line in f:\n            m = pattern.search(line)\n            if m:\n                step = int(m.group(1)) if m.group(1) else -1\n                metrics = ast.literal_eval(m.group(2))\n                metrics[\"step\"] = step\n                evals.append(metrics)\n    return evals\n\n\ndef extract_best_metrics(evals):\n    \"\"\"From a list of eval dicts, extract best R@1 and best val_loss.\"\"\"\n    if not evals:\n        return None\n    best_r1 = max(evals, key=lambda e: e.get(\"recall@1\", 0))\n    best_vl = min(evals, key=lambda e: e.get(\"val_loss\", float(\"inf\")))\n    return {\n        \"best_recall@1\": best_r1[\"recall@1\"],\n        \"best_recall@1_step\": best_r1[\"step\"],\n        \"best_val_loss\": best_vl[\"val_loss\"],\n        \"best_val_loss_step\": best_vl[\"step\"],\n        \"num_evals\": len(evals),\n        \"is_complete\": any(e[\"step\"] == -1 for e in evals),\n    }\n\n\ndef load_all_results():\n    \"\"\"Load results from all available logs. Returns nested dict: results[encoder][strategy][seed].\"\"\"\n    results = defaultdict(lambda: defaultdict(dict))\n    missing = []\n    for enc in ENCODERS:\n        log_dir = LOG_DIRS[enc]\n        for strat in STRATEGIES:\n            for seed in SEEDS:\n                log_path = os.path.join(log_dir, f\"{strat}_s{seed}.log\")\n                if not os.path.exists(log_path):\n                    missing.append(f\"{enc}/{strat}_s{seed}\")\n                    continue\n                evals = parse_eval_lines(log_path)\n                if not evals:\n                    missing.append(f\"{enc}/{strat}_s{seed} (no eval lines)\")\n                    continue\n                best = extract_best_metrics(evals)\n                results[enc][strat][seed] = best\n    return dict(results), missing\n\n\n# ─── Statistical Tests ───────────────────────────────────────────────────────\n\ndef paired_ttest(vals_a, vals_b):\n    \"\"\"Paired t-test. Returns t-stat, p-value, and n.\"\"\"\n    paired = [(a, b) for a, b in zip(vals_a, vals_b) if a is not None and b is not None]\n    if len(paired) < 2:\n        return {\"t\": np.nan, \"p\": np.nan, \"n\": len(paired), \"insufficient\": True}\n    a, b = zip(*paired)\n    t_stat, p_val = stats.ttest_rel(a, b)\n    return {\"t\": float(t_stat), \"p\": float(p_val), \"n\": len(paired), \"insufficient\": False}\n\n\ndef cohens_d(vals_a, vals_b):\n    \"\"\"Cohen's d for paired samples.\"\"\"\n    diffs = [a - b for a, b in zip(vals_a, vals_b) if a is not None and b is not None]\n    if len(diffs) < 2:\n        return np.nan\n    return float(np.mean(diffs) / np.std(diffs, ddof=1))\n\n\ndef bootstrap_ci(values, n_boot=BOOTSTRAP_N, ci=0.95):\n    \"\"\"Bootstrap confidence interval for the mean.\"\"\"\n    values = [v for v in values if v is not None]\n    if len(values) < 2:\n        return {\"mean\": float(values[0]) if values else np.nan,\n                \"ci_lo\": np.nan, \"ci_hi\": np.nan, \"n\": len(values)}\n    rng = np.random.default_rng(seed=0)\n    boot_means = []\n    arr = np.array(values)\n    for _ in range(n_boot):\n        sample = rng.choice(arr, size=len(arr), replace=True)\n        boot_means.append(np.mean(sample))\n    boot_means = np.array(boot_means)\n    lo = np.percentile(boot_means, (1 - ci) / 2 * 100)\n    hi = np.percentile(boot_means, (1 + ci) / 2 * 100)\n    return {\"mean\": float(np.mean(values)), \"ci_lo\": float(lo), \"ci_hi\": float(hi),\n            \"n\": len(values), \"std\": float(np.std(values, ddof=1))}\n\n\ndef interaction_test(results, metric_key):\n    \"\"\"2-way encoder × strategy interaction via 2-way ANOVA-like permutation test.\n\n    With n=3 we don't have enough power for a proper ANOVA, so we compute\n    the interaction contrast (difference of differences) and report it descriptively.\n    \"\"\"\n    contrasts = {}\n    for strat in [\"embedding_distance\", \"dataflow_aware\"]:\n        diffs = {}\n        for enc in ENCODERS:\n            strat_vals = get_metric_values(results, enc, strat, metric_key)\n            rand_vals = get_metric_values(results, enc, \"random\", metric_key)\n            paired = [(s - r) for s, r in zip(strat_vals, rand_vals) if s is not None and r is not None]\n            diffs[enc] = paired\n        if diffs.get(\"qwen\") and diffs.get(\"starcoder\"):\n            q_mean = np.mean(diffs[\"qwen\"])\n            s_mean = np.mean(diffs[\"starcoder\"])\n            contrasts[strat] = {\n                \"qwen_delta\": float(q_mean),\n                \"starcoder_delta\": float(s_mean),\n                \"interaction\": float(q_mean - s_mean),\n                \"interpretation\": (\n                    f\"Qwen benefit: {q_mean*100:+.2f}pp, StarCoder benefit: {s_mean*100:+.2f}pp, \"\n                    f\"interaction (Qwen-StarCoder): {(q_mean-s_mean)*100:+.2f}pp\"\n                ),\n            }\n        else:\n            contrasts[strat] = {\"insufficient_data\": True}\n    return contrasts\n\n\ndef get_metric_values(results, encoder, strategy, metric_key):\n    \"\"\"Get metric values for all seeds, returning None for missing seeds.\"\"\"\n    vals = []\n    for seed in SEEDS:\n        entry = results.get(encoder, {}).get(strategy, {}).get(seed)\n        if entry:\n            vals.append(entry.get(metric_key))\n        else:\n            vals.append(None)\n    return vals\n\n\n# ─── Analysis ────────────────────────────────────────────────────────────────\n\ndef run_analysis(results):\n    \"\"\"Run all statistical tests. Returns structured dict.\"\"\"\n    output = {\n        \"metadata\": {\n            \"seeds\": SEEDS,\n            \"n_per_cell\": len(SEEDS),\n            \"df\": len(SEEDS) - 1,\n            \"warning\": \"n=3, df=2, high Type II error risk. Non-significant results should NOT be interpreted as null effects.\",\n            \"bootstrap_resamples\": BOOTSTRAP_N,\n            \"alpha\": ALPHA,\n        },\n        \"descriptives\": {},\n        \"pairwise_tests\": {},\n        \"bootstrap_cis\": {},\n        \"interaction\": {},\n        \"claims\": {},\n    }\n\n    metric_key = \"best_recall@1\"\n\n    # Descriptives and bootstrap CIs\n    for enc in ENCODERS:\n        output[\"descriptives\"][enc] = {}\n        output[\"bootstrap_cis\"][enc] = {}\n        for strat in STRATEGIES:\n            vals = get_metric_values(results, enc, strat, metric_key)\n            valid = [v for v in vals if v is not None]\n            output[\"descriptives\"][enc][strat] = {\n                \"values\": [float(v) if v is not None else None for v in vals],\n                \"mean\": float(np.mean(valid)) if valid else None,\n                \"std\": float(np.std(valid, ddof=1)) if len(valid) > 1 else None,\n                \"n\": len(valid),\n            }\n            output[\"bootstrap_cis\"][enc][strat] = bootstrap_ci(valid)\n\n    # Pairwise tests: embedding vs random, dataflow vs random\n    for enc in ENCODERS:\n        output[\"pairwise_tests\"][enc] = {}\n        rand_vals = get_metric_values(results, enc, \"random\", metric_key)\n        for strat in [\"embedding_distance\", \"dataflow_aware\"]:\n            strat_vals = get_metric_values(results, enc, strat, metric_key)\n            tt = paired_ttest(strat_vals, rand_vals)\n            d = cohens_d(strat_vals, rand_vals)\n            output[\"pairwise_tests\"][enc][f\"{strat}_vs_random\"] = {\n                \"paired_ttest\": tt,\n                \"cohens_d\": float(d) if not np.isnan(d) else None,\n                \"mean_diff\": float(np.nanmean([s - r for s, r in zip(strat_vals, rand_vals)\n                                                if s is not None and r is not None])) if any(\n                    s is not None and r is not None for s, r in zip(strat_vals, rand_vals)) else None,\n            }\n\n    # Interaction\n    output[\"interaction\"] = interaction_test(results, metric_key)\n\n    # Claim adjudication\n    output[\"claims\"] = adjudicate_claims(output)\n\n    return output\n\n\ndef adjudicate_claims(output):\n    \"\"\"Evaluate paper claims against statistical evidence.\"\"\"\n    claims = {}\n\n    # Claim 1: embedding_distance > random (both encoders)\n    c1_parts = []\n    for enc in ENCODERS:\n        test = output[\"pairwise_tests\"].get(enc, {}).get(\"embedding_distance_vs_random\", {})\n        tt = test.get(\"paired_ttest\", {})\n        d = test.get(\"mean_diff\")\n        if tt.get(\"insufficient\"):\n            c1_parts.append(f\"{enc}: insufficient data\")\n        else:\n            sig = \"p<0.05\" if tt[\"p\"] < ALPHA else f\"p={tt['p']:.3f} (n.s.)\"\n            direction = \"positive\" if (d is not None and d > 0) else \"negative/zero\"\n            c1_parts.append(f\"{enc}: {sig}, direction={direction}, Δ={d*100:.2f}pp\" if d is not None else f\"{enc}: {sig}\")\n\n    claims[\"claim1_embedding_gt_random\"] = {\n        \"description\": \"embedding_distance > random (expected: consistent positive, pilot +1.6~2.0pp)\",\n        \"per_encoder\": c1_parts,\n    }\n\n    # Claim 2: dataflow conditional benefit (Qwen positive, StarCoder neutral)\n    c2_parts = []\n    inter = output[\"interaction\"].get(\"dataflow_aware\", {})\n    for enc in ENCODERS:\n        test = output[\"pairwise_tests\"].get(enc, {}).get(\"dataflow_aware_vs_random\", {})\n        tt = test.get(\"paired_ttest\", {})\n        d = test.get(\"mean_diff\")\n        if tt.get(\"insufficient\"):\n            c2_parts.append(f\"{enc}: insufficient data\")\n        else:\n            sig = \"p<0.05\" if tt[\"p\"] < ALPHA else f\"p={tt['p']:.3f} (n.s.)\"\n            c2_parts.append(f\"{enc}: {sig}, Δ={d*100:.2f}pp\" if d is not None else f\"{enc}: {sig}\")\n\n    claims[\"claim2_dataflow_conditional\"] = {\n        \"description\": \"dataflow_aware benefit depends on encoder (Qwen positive, StarCoder neutral)\",\n        \"per_encoder\": c2_parts,\n        \"interaction\": inter if not inter.get(\"insufficient_data\") else \"insufficient data\",\n    }\n\n    return claims\n\n\n# ─── Output Formatting ───────────────────────────────────────────────────────\n\ndef print_report(output):\n    \"\"\"Print formatted report to stdout.\"\"\"\n    meta = output[\"metadata\"]\n    print(\"=\" * 78)\n    print(\"M2 Full Experiment — Statistical Analysis Report\")\n    print(\"=\" * 78)\n    print(f\"  Seeds: {meta['seeds']}  |  n={meta['n_per_cell']} per cell  |  df={meta['df']}\")\n    print(f\"  ⚠  {meta['warning']}\")\n    print()\n\n    # Descriptives table\n    print(\"─\" * 78)\n    print(\"R@1 Descriptives (best checkpoint)\")\n    print(\"─\" * 78)\n    print(f\"  {'Encoder':<12} {'Strategy':<22} {'Mean':>8} {'±Std':>8} {'n':>4}  {'95% CI':>20}\")\n    print(f\"  {'─'*12} {'─'*22} {'─'*8} {'─'*8} {'─'*4}  {'─'*20}\")\n    for enc in ENCODERS:\n        for strat in STRATEGIES:\n            desc = output[\"descriptives\"][enc][strat]\n            ci = output[\"bootstrap_cis\"][enc][strat]\n            mean_s = f\"{desc['mean']*100:.2f}%\" if desc[\"mean\"] is not None else \"N/A\"\n            std_s = f\"{desc['std']*100:.2f}\" if desc[\"std\"] is not None else \"N/A\"\n            ci_s = f\"[{ci['ci_lo']*100:.2f}, {ci['ci_hi']*100:.2f}]\" if not np.isnan(ci[\"ci_lo\"]) else \"N/A\"\n            print(f\"  {enc:<12} {strat:<22} {mean_s:>8} {std_s:>8} {desc['n']:>4}  {ci_s:>20}\")\n    print()\n\n    # Pairwise tests\n    print(\"─\" * 78)\n    print(\"Pairwise Comparisons vs Random (paired t-test, R@1)\")\n    print(\"─\" * 78)\n    print(f\"  {'Encoder':<12} {'Comparison':<30} {'Δ(pp)':>8} {'t':>8} {'p':>8} {'d':>8} {'Sig':>6}\")\n    print(f\"  {'─'*12} {'─'*30} {'─'*8} {'─'*8} {'─'*8} {'─'*8} {'─'*6}\")\n    for enc in ENCODERS:\n        for comp_name, comp_data in output[\"pairwise_tests\"][enc].items():\n            tt = comp_data[\"paired_ttest\"]\n            if tt.get(\"insufficient\"):\n                print(f\"  {enc:<12} {comp_name:<30} {'—':>8} {'—':>8} {'—':>8} {'—':>8} {'N/A':>6}\")\n                continue\n            diff_s = f\"{comp_data['mean_diff']*100:+.2f}\" if comp_data[\"mean_diff\"] is not None else \"—\"\n            t_s = f\"{tt['t']:.3f}\"\n            p_s = f\"{tt['p']:.4f}\"\n            d_s = f\"{comp_data['cohens_d']:.3f}\" if comp_data[\"cohens_d\"] is not None else \"—\"\n            sig = \"*\" if tt[\"p\"] < ALPHA else \"n.s.\"\n            print(f\"  {enc:<12} {comp_name:<30} {diff_s:>8} {t_s:>8} {p_s:>8} {d_s:>8} {sig:>6}\")\n    print()\n\n    # Interaction\n    print(\"─\" * 78)\n    print(\"Encoder × Strategy Interaction (R@1)\")\n    print(\"─\" * 78)\n    for strat, inter in output[\"interaction\"].items():\n        if inter.get(\"insufficient_data\"):\n            print(f\"  {strat}: insufficient data\")\n        else:\n            print(f\"  {strat}:\")\n            print(f\"    {inter['interpretation']}\")\n    print()\n\n    # Claims\n    print(\"─\" * 78)\n    print(\"Claim Adjudication\")\n    print(\"─\" * 78)\n    for claim_key, claim_data in output[\"claims\"].items():\n        print(f\"\\n  {claim_key}: {claim_data['description']}\")\n        for line in claim_data[\"per_encoder\"]:\n            print(f\"    • {line}\")\n        if \"interaction\" in claim_data and claim_data[\"interaction\"] != \"insufficient data\":\n            inter = claim_data[\"interaction\"]\n            if isinstance(inter, dict):\n                print(f\"    • interaction: {inter.get('interpretation', 'N/A')}\")\n\n    print()\n    print(\"=\" * 78)\n\n\n# ─── Data Availability Report ────────────────────────────────────────────────\n\ndef print_data_status(results, missing):\n    \"\"\"Print which runs are available and which are missing.\"\"\"\n    print(\"─\" * 78)\n    print(\"Data Availability\")\n    print(\"─\" * 78)\n    total = len(ENCODERS) * len(STRATEGIES) * len(SEEDS)\n    found = sum(1 for enc in results for strat in results[enc] for seed in results[enc][strat])\n    print(f\"  Available: {found}/{total} runs\")\n    if missing:\n        print(f\"  Missing ({len(missing)}):\")\n        for m in missing:\n            print(f\"    • {m}\")\n    else:\n        print(\"  All runs complete.\")\n\n    # Completeness per run\n    for enc in ENCODERS:\n        for strat in STRATEGIES:\n            for seed in SEEDS:\n                entry = results.get(enc, {}).get(strat, {}).get(seed)\n                if entry:\n                    status = \"COMPLETE\" if entry[\"is_complete\"] else f\"IN PROGRESS ({entry['num_evals']} evals)\"\n                    print(f\"    {enc}/{strat}_s{seed}: {status}, best R@1={entry['best_recall@1']*100:.2f}%\")\n    print()\n\n\n# ─── Main ────────────────────────────────────────────────────────────────────\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Statistical analysis for M2 Full experiment (3 strategies × 3 seeds × 2 encoders).\"\n    )\n    parser.add_argument(\"--json\", default=\"/root/structfuse/analysis/m2_stat_results.json\",\n                        help=\"Path to save JSON results (default: %(default)s)\")\n    parser.add_argument(\"--status-only\", action=\"store_true\",\n                        help=\"Only print data availability, skip analysis\")\n    args = parser.parse_args()\n\n    results, missing = load_all_results()\n\n    print_data_status(results, missing)\n\n    if args.status_only:\n        return\n\n    # Need at least 2 seeds for any strategy to run tests\n    can_analyze = False\n    for enc in results:\n        for strat in results[enc]:\n            if len(results[enc][strat]) >= 2:\n                can_analyze = True\n                break\n\n    if not can_analyze:\n        print(\"Not enough data for statistical analysis (need ≥2 seeds per strategy).\")\n        print(\"Re-run when more experiments complete.\")\n        return\n\n    output = run_analysis(results)\n    print_report(output)\n\n    os.makedirs(os.path.dirname(args.json), exist_ok=True)\n    with open(args.json, \"w\") as f:\n        json.dump(output, f, indent=2, default=str)\n    print(f\"JSON results saved to {args.json}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T15:09:33.747877+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_prepare_stat_analysis_20260514T150704",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T15:09:33.748042+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-42106",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/structfuse/analysis/m2_stat_analysis.py --help",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_prepare_stat_analysis_20260514T150704",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/structfuse/analysis/m2_stat_analysis.py --help",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T15:09:33.748186+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"usage: m2_stat_analysis.py [-h] [--json JSON] [--status-only]\\n\\nStatistical analysis for M2 Full experiment (3 strategies × 3 seeds × 2\\nencoders).\\n\\noptions:\\n  -h, --help     show this help message and exit\\n  --json JSON    Path to save JSON results (default:\\n                 /root/structfuse/analysis/m2_stat_results.json)\\n  --status-only  Only print data availability, skip analysis\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.48}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_prepare_stat_analysis_20260514T150704",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T15:09:33.748372+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-42106",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/structfuse/analysis/m2_stat_analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_prepare_stat_analysis_20260514T150704",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/structfuse/analysis/m2_stat_analysis.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T15:09:33.748579+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"──────────────────────────────────────────────────────────────────────────────\\nData Availability\\n──────────────────────────────────────────────────────────────────────────────\\n  Available: 3/18 runs\\n  Missing (15):\\n    • qwen/random_s44\\n    • qwen/embedding_distance_s42\\n    • qwen/embedding_distance_s43\\n    • qwen/embedding_distance_s44\\n    • qwen/dataflow_aware_s42\\n    • qwen/dataflow_aware_s43\\n    • qwen/dataflow_aware_s44\\n    • starcoder/random_s43\\n    • starcoder/random_s44\\n    • starcoder/embedding_distance_s42\\n    • starcoder/embedding_distance_s43\\n    • starcoder/embedding_distance_s44\\n    • starcoder/dataflow_aware_s42\\n    • starcoder/dataflow_aware_s43\\n    • starcoder/dataflow_aware_s44\\n    qwen/random_s42: COMPLETE, best R@1=55.27%\\n    qwen/random_s43: IN PROGRESS (1 evals), best R@1=53.57%\\n    starcoder/random_s42: IN PROGRESS (7 evals), best R@1=46.04%\\n\\n==============================================================================\\nM2 Full Experiment — Statistical Analysis Report\\n==============================================================================\\n  Seeds: [42, 43, 44]  |  n=3 per cell  |  df=2\\n  ⚠  n=3, df=2, high Type II error risk. Non-significant results should NOT be interpreted as null effects.\\n\\n──────────────────────────────────────────────────────────────────────────────\\nR@1 Descriptives (best checkpoint)\\n───────────────────────────────────────────────���──────────────────────────────\\n  Encoder      Strategy                   Mean     ±Std    n                95% CI\\n  ──────────── ────────────────────── ──────── ──────── ────  ────────────────────\\n  qwen         random                   54.42%     1.20    2        [53.57, 55.27]\\n  qwen         embedding_distance          N/A      N/A    0                   N/A\\n  qwen         dataflow_aware              N/A      N/A    0                   N/A\\n  starcoder    r
…[truncated 2099 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_prepare_stat_analysis_20260514T150704",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-14T15:09:33.748832+00:00_

脚本已创建并验证通过。

**结果**：`/root/structfuse/analysis/m2_stat_analysis.py` 已部署到服务器，dry-run 成功。当前 3/18 runs 有数据（qwen/random_s42 完成、qwen/random_s43 和 starcoder/random_s42 进行中），统计检验因 embedding_distance 和 dataflow_aware 数据尚未到位而跳过，符合预期。

脚本功能：
- `--status-only`：仅查看数据可用性
- 默认运行：数据可用时自动执行 paired t-test、bootstrap CI、Cohen's d、encoder×strategy 交互对比，输出格式化表格 + JSON
- 缺失 run 自动跳过，不会报错

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_prepare_stat_analysis_20260514T150704"
}
```

</details>

---
