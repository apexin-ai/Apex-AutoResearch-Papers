# ssh check shuffled control

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/chats/worker_ssh_check-shuffled-control_20260515T194205.jsonl`
- **Structured JSON:** [`5b7b004f4d414ca08483.json`](../../sessions/5b/5b7b004f4d414ca08483.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

29 recorded events

### Tool call

_source line 1 · 2026-05-15T19:43:06.448367+00:00_

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
  "session": "worker_ssh_check-shuffled-control_20260515T194205",
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

_source line 2 · 2026-05-15T19:43:06.448695+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-shuffled-control_20260515T194205",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T19:43:06.448858+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ps aux | grep -E \"train_probes|shuffle\" | grep -v grep"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check-shuffled-control_20260515T194205",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ps aux | grep -E \"train_probes|shuffle\" | grep -v grep"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T19:43:06.449056+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-shuffled-control_20260515T194205",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T19:43:06.449200+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "tmux ls 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check-shuffled-control_20260515T194205",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "tmux ls 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T19:43:06.449326+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-shuffled-control_20260515T194205",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T19:43:06.449444+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "nvidia-smi --query-gpu=index,memory.used,utilization.gpu --format=csv,noheader"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check-shuffled-control_20260515T194205",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "nvidia-smi --query-gpu=index,memory.used,utilization.gpu --format=csv,noheader"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-15T19:43:06.449561+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ps aux | grep pca_linear | grep -v grep"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check-shuffled-control_20260515T194205",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ps aux | grep pca_linear | grep -v grep"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-15T19:43:06.449710+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 561 MiB, 2 %\\n1, 1713 MiB, 0 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-shuffled-control_20260515T194205",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T19:43:06.449847+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-shuffled-control_20260515T194205",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T19:43:06.450077+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check-shuffled-control_20260515T194205",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T19:43:06.450219+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-shuffled-control_20260515T194205",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T19:43:06.450350+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19183",
  "command": "ps aux | grep -E \"train_probes|shuffle\" | grep -v grep",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check-shuffled-control_20260515T194205",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19183",
    "command": "ps aux | grep -E \"train_probes|shuffle\" | grep -v grep",
    "warn": "True"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T19:43:06.450470+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19183",
  "command": "tmux ls 2>/dev/null",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check-shuffled-control_20260515T194205",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19183",
    "command": "tmux ls 2>/dev/null",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T19:43:06.450644+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"root     642367  0.0  0.0   4364  2072 ?        S    03:17   0:00 bash -c cd /root/vla-ssd && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && nohup bash -c ' echo \\\"=== START: $(date) ===\\\"  echo \\\"--- Trained VLA PCA-1024 ---\\\" python scripts/train_probes.py \\\\   --features_dir /root/autodl-tmp/vla-ssd/features/trained_libero_goal/ \\\\   --output_dir /root/autodl-tmp/vla-ssd/results/trained_libero_goal/ \\\\   --probe_type goal_classification \\\\   --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ \\\\   --pca_dim 1024 --gpu 0  echo \\\"--- Untrained VLA PCA-1024 ---\\\" python scripts/train_probes.py \\\\   --features_dir /root/autodl-tmp/vla-ssd/features/untrained_libero_goal/ \\\\   --output_dir /root/autodl-tmp/vla-ssd/results/untrained_libero_goal/ \\\\   --probe_type goal_classification \\\\   --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ \\\\   --pca_dim 1024 --gpu 0  echo \\\"--- DINO PCA-1024 ---\\\" python scripts/train_probes.py \\\\   --features_dir /root/autodl-tmp/vla-ssd/features/dinov2_libero_goal/ \\\\   --output_dir /root/autodl-tmp/vla-ssd/results/dinov2_libero_goal/ \\\\   --probe_type goal_classification \\\\   --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ \\\\   --pca_dim 1024 --gpu 0  echo \\\"=== DONE: $(date) ===\\\" ' > /tmp/pca1024_goal.log 2>&1 & echo $!\\nroot     642372  0.0  0.0   4364  3132 ?        S    03:17   0:00 bash -c  echo \\\"=== START: $(date) ===\\\"  echo \\\"--- Trained VLA PCA-1024 ---\\\" python scripts/train_probes.py \\\\   --features_dir /root/autodl-tmp/vla-ssd/features/trained_libero_goal/ \\\\   --output_dir /root/autodl-tmp/vla-ssd/results/trained_libero_goal/ \\\\   --probe_type goal_classification \\\\   --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ \\\\   --pca_dim 1024 --gpu 0  echo \\\"--- Untrained VLA PCA-1024 ---\\\" python scripts/train_probes.py \\\\   --f
…[truncated 4339 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-shuffled-control_20260515T194205",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T19:43:06.450786+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19183",
  "command": "ps aux | grep pca_linear | grep -v grep",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check-shuffled-control_20260515T194205",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19183",
    "command": "ps aux | grep pca_linear | grep -v grep",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-15T19:43:06.450908+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.59}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-shuffled-control_20260515T194205",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T19:43:06.451098+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"root     649509  0.0  0.0   4364  2096 ?        S    03:38   0:00 bash -c source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && nohup python3 -u /root/vla-ssd/scripts/pca_linear_probe_perlayer.py > /tmp/pca_probe.log 2>&1 & echo \\\"PID=$!\\\"\\nroot     649515  639  3.4 42022036 36568344 ?   Rl   03:38  25:08 python3 -u /root/vla-ssd/scripts/pca_linear_probe_perlayer.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.55}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-shuffled-control_20260515T194205",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T19:43:06.451267+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19183",
  "command": "ls -la /root/autodl-tmp/vla-ssd/results/trained_libero_goal_shuffled/goal_classification/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check-shuffled-control_20260515T194205",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls -la /root/autodl-tmp/vla-ssd/results/trained_libero_goal_shuffled/goal_classification/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
    "warn": "True"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-15T19:43:06.451395+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19183",
  "command": "cat ~/runs/vla-ssd/lg_shuffled_token_control.log 2>/dev/null | tail -30 || echo \"LOG_NOT_FOUND\"",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check-shuffled-control_20260515T194205",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat ~/runs/vla-ssd/lg_shuffled_token_control.log 2>/dev/null | tail -30 || echo \"LOG_NOT_FOUND\"",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-15T19:43:06.451518+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"DIR_NOT_FOUND\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-shuffled-control_20260515T194205",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T19:43:06.451635+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.58}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-shuffled-control_20260515T194205",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T19:43:06.451747+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19183",
  "command": "tail -20 /tmp/pca_probe.log 2>/dev/null || echo \"NO_PCA_LOG\"",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check-shuffled-control_20260515T194205",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19183",
    "command": "tail -20 /tmp/pca_probe.log 2>/dev/null || echo \"NO_PCA_LOG\"",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T19:43:06.451870+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n============================================================\\nModel: trained_vla | layers: 33 | dir: /root/autodl-tmp/vla-ssd/features/trained_libero_goal/\\n============================================================\\n  Loading features from 10 h5 files...\\n  Loaded in 171.7s. Samples: 50880 train / 12848 val\\n/root/miniconda3/lib/python3.12/site-packages/sklearn/decomposition/_pca.py:779: RuntimeWarning: invalid value encountered in divide\\n  self.explained_variance_ratio_ = self.explained_variance_ / total_var\\n  layer  0: acc=0.1582  f1=0.0273  var_expl=0.0000  37.9s\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-shuffled-control_20260515T194205",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T19:43:06.452046+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19183",
  "command": "tail -20 /tmp/pca1024_goal.log 2>/dev/null || echo \"NO_LOG\"",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check-shuffled-control_20260515T194205",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19183",
    "command": "tail -20 /tmp/pca1024_goal.log 2>/dev/null || echo \"NO_LOG\"",
    "warn": "True"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-15T19:43:06.452183+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19183",
  "command": "tail -20 /tmp/linear_probe_run.log 2>/dev/null || echo \"NO_LOG\"",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check-shuffled-control_20260515T194205",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19183",
    "command": "tail -20 /tmp/linear_probe_run.log 2>/dev/null || echo \"NO_LOG\"",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-15T19:43:06.452319+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  PCA 4096 -> 1024: 0.8847 variance retained\\n  Samples: 50880 train / 12848 val\\n  acc=1.0000  traj_acc=1.0000  F1=1.0000  ep=6  24.2s\\n\\nSaved to /root/autodl-tmp/vla-ssd/results/trained_libero_goal_pca1024/goal_classification/\\n--- Untrained VLA PCA-1024 ---\\nPCA mode: reducing to 1024 dims\\n=== Probe Training: goal_classification | device=cuda:0 ===\\nFeatures: 500 trajs, 33 layers, dim=4096\\nTasks (10): ['open_the_middle_drawer_of_the_cabinet', 'open_the_top_drawer_and_put_the_bowl_inside', 'push_the_plate_to_the_front_of_the_stove', 'put_the_bowl_on_the_plate', 'put_the_bowl_on_the_stove', 'put_the_bowl_on_top_of_the_cabinet', 'put_the_cream_cheese_in_the_bowl', 'put_the_wine_bottle_on_the_rack', 'put_the_wine_bottle_on_top_of_the_cabinet', 'turn_on_the_stove']\\nSplit: 400 train trajs / 100 val trajs\\n\\n[Layer 0] (1/33)\\n/root/miniconda3/lib/python3.12/site-packages/sklearn/decomposition/_pca.py:779: RuntimeWarning: invalid value encountered in divide\\n  self.explained_variance_ratio_ = self.explained_variance_ / total_var\\n  PCA 4096 -> 1024: nan variance retained\\n  Samples: 50880 train / 12848 val\\n  acc=0.1582  traj_acc=0.1000  F1=0.0273  ep=6  46.8s\\n\\n[Layer 1] (2/33)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-shuffled-control_20260515T194205",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T19:43:06.452454+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  Samples: 50880 train / 12848 val\\n  acc=0.9987  traj_acc=1.0000  F1=0.9984  ep=50  23.2s\\n\\n[Layer 15] (16/33)\\n  Samples: 50880 train / 12848 val\\n  acc=0.9983  traj_acc=1.0000  F1=0.9980  ep=46  23.6s\\n\\n[Layer 16] (17/33)\\n  Samples: 50880 train / 12848 val\\n  acc=0.9981  traj_acc=1.0000  F1=0.9978  ep=20  21.2s\\n\\n[Layer 17] (18/33)\\n  Samples: 50880 train / 12848 val\\n  acc=0.9970  traj_acc=1.0000  F1=0.9965  ep=23  34.5s\\n\\n[Layer 18] (19/33)\\n  Samples: 50880 train / 12848 val\\n  acc=0.9973  traj_acc=1.0000  F1=0.9968  ep=24  28.0s\\n\\n[Layer 19] (20/33)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.58}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-shuffled-control_20260515T194205",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-15T19:43:06.452633+00:00_

## 汇报

### lg_shuffled_token_control
**未启动。** 无相关进程，结果目录不存在，日志文件为空。

### 当前运行的实验（3 个）

| 实验 | PID | GPU | 启动时间 | 状态 |
|------|-----|-----|---------|------|
| PCA-1024 goal_classification (untrained) | 650060 | GPU 0 | 03:41 | 运行中，untrained 阶段（trained 已完成，acc=1.0000） |
| Linear probe goal_classification (untrained) | 648231 | GPU 1 | 03:33 | 运行中，untrained 阶段，Layer 19/33 |
| **Exp-1 pca_linear_probe_perlayer** | 649515 | — | 03:38 | 运行中，trained_vla Layer 0 完成（acc=0.1582），刚开始 |

### GPU 使用率

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| GPU 0 | 561 MiB | 2% |
| GPU 1 | 1713 MiB | 0% |

利用率低说明当前主要在做 CPU 端工作（PCA 降维、数据加载）。

### 注意
- perlayer sweep 的 layer 0 出现 `RuntimeWarning: invalid value encountered in divide`（PCA variance ratio 为 NaN），acc 仅 0.1582 — layer 0 特征可能全零或接近常数。
- tmux 无 session（进程通过 nohup 后台运行）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ssh_check-shuffled-control_20260515T194205"
}
```

</details>

---
