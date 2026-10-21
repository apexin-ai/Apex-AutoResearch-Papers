# deploy k2 adaptive spatial cqa1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 78
- **Recorded user turns:** 0
- **Tool calls:** 38
- **Original source:** `logs/chats/worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156.jsonl`
- **Structured JSON:** [`a5391c41cbedbc25998a.json`](../../sessions/a5/a5391c41cbedbc25998a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

78 recorded events

### Assistant

_source line 1 · 2026-05-25T02:52:05.187134+00:00_

Not logged in · Please run /login

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-25T02:57:52.829868+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry",
    "max_results": "10"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-25T02:57:52.830151+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-25T02:57:52.830338+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "submit training job",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "submit training job",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-25T02:57:52.830521+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-25T02:57:52.830664+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "submit_training_job",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "submit_training_job",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-25T02:57:52.830785+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-25T02:57:52.830900+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "tmux training run experiment",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "tmux training run experiment",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-25T02:57:52.831016+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-25T02:57:52.831153+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "nvidia-smi --query-gpu=index,utilization.gpu,memory.used --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "nvidia-smi --query-gpu=index,utilization.gpu,memory.used --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-25T02:57:52.831306+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 0 %, 0 MiB\\n1, 0 %, 0 MiB\\n2, 0 %, 0 MiB\\n3, 0 %, 0 MiB\\n4, 0 %, 0 MiB\\n5, 0 %, 0 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-25T02:57:52.831447+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "ls /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "ls /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-25T02:57:52.831569+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.64}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-25T02:57:52.831684+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "ls /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "ls /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-25T02:57:52.831816+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/src/evaluate.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-25T02:57:52.831955+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k2-adaptive-spatial-s42",
  "field": "hypothesis",
  "value": "K=2 Adaptive Spatial (τ=0.25) 同服务器配对。K=2 是正确采样数（两次前向推理算 L2 距离做 gating）。配对 cqa1-32758 VLA-only baseline 用于 paired t-test。",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k2-adaptive-spatial-s42",
    "field": "hypothesis",
    "value": "K=2 Adaptive Spatial (τ=0.25) 同服务器配对。K=2 是正确采样数（两次前向推理算 L2 距离做 gating）。配对 cqa1-32758 VLA-only baseline 用于 paired t-test。",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-25T02:57:52.832081+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k2-adaptive-spatial-s43",
  "field": "hypothesis",
  "value": "K=2 Adaptive Spatial (τ=0.25) 同服务器配对。K=2 是正确采样数（两次前向推理算 L2 距离做 gating）。配对 cqa1-32758 VLA-only baseline 用于 paired t-test。",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k2-adaptive-spatial-s43",
    "field": "hypothesis",
    "value": "K=2 Adaptive Spatial (τ=0.25) 同服务器配对。K=2 是正确采样数（两次前向推理算 L2 距离做 gating）。配对 cqa1-32758 VLA-only baseline 用于 paired t-test。",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-25T02:57:52.832202+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k2-adaptive-spatial-s44",
  "field": "hypothesis",
  "value": "K=2 Adaptive Spatial (τ=0.25) 同服务器配对。K=2 是正确采样数（两次前向推理算 L2 距离做 gating）。配对 cqa1-32758 VLA-only baseline 用于 paired t-test。",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k2-adaptive-spatial-s44",
    "field": "hypothesis",
    "value": "K=2 Adaptive Spatial (τ=0.25) 同服务器配对。K=2 是正确采样数（两次前向推理算 L2 距离做 gating）。配对 cqa1-32758 VLA-only baseline 用于 paired t-test。",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-25T02:57:52.832355+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-cqa1-s42",
  "field": "hypothesis",
  "value": "VLA-only baseline Spatial s42 on cqa1-32758. 同服务器配对数据用于 K=2 Adaptive paired t-test。",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-cqa1-s42",
    "field": "hypothesis",
    "value": "VLA-only baseline Spatial s42 on cqa1-32758. 同服务器配对数据用于 K=2 Adaptive paired t-test。",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-25T02:57:52.832493+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k2-adaptive-spatial-s42\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:52:57.415Z\", \"updated_at\": \"2026-05-25T02:52:57.415Z\", \"hypothesis\": \"K=2 Adaptive Spatial (τ=0.25) 同服务器配对。K=2 是正确采样数（两次前向推理算 L2 距离做 gating）。配对 cqa1-32758 VLA-only baseline 用于 paired t-test。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.9887}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-25T02:57:52.832618+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-cqa1-s43",
  "field": "hypothesis",
  "value": "VLA-only baseline Spatial s43 on cqa1-32758. 同服务器配对数据用于 K=2 Adaptive paired t-test。",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-cqa1-s43",
    "field": "hypothesis",
    "value": "VLA-only baseline Spatial s43 on cqa1-32758. 同服务器配对数据用于 K=2 Adaptive paired t-test。",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-25T02:57:52.832737+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-cqa1-s44",
  "field": "hypothesis",
  "value": "VLA-only baseline Spatial s44 on cqa1-32758. 同服务器配对数据用于 K=2 Adaptive paired t-test。",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-cqa1-s44",
    "field": "hypothesis",
    "value": "VLA-only baseline Spatial s44 on cqa1-32758. 同服务器配对数据用于 K=2 Adaptive paired t-test。",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-25T02:57:52.832875+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k2-adaptive-spatial-s43\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:53:11.261Z\", \"updated_at\": \"2026-05-25T02:53:11.261Z\", \"hypothesis\": \"K=2 Adaptive Spatial (τ=0.25) 同服务器配对。K=2 是正确采样数（两次前向推理算 L2 距离做 gating）。配对 cqa1-32758 VLA-only baseline 用于 paired t-test。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 13.0368}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-25T02:57:52.833006+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k2-adaptive-spatial-s44\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:53:18.842Z\", \"updated_at\": \"2026-05-25T02:53:18.842Z\", \"hypothesis\": \"K=2 Adaptive Spatial (τ=0.25) 同服务器配对。K=2 是正确采样数（两次前向推理算 L2 距离做 gating）。配对 cqa1-32758 VLA-only baseline 用于 paired t-test。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.2232}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-25T02:57:52.833132+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-cqa1-s42\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:53:26.220Z\", \"updated_at\": \"2026-05-25T02:53:26.220Z\", \"hypothesis\": \"VLA-only baseline Spatial s42 on cqa1-32758. 同服务器配对数据用于 K=2 Adaptive paired t-test。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.3185}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-25T02:57:52.833256+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-cqa1-s43\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:53:33.714Z\", \"updated_at\": \"2026-05-25T02:53:33.714Z\", \"hypothesis\": \"VLA-only baseline Spatial s43 on cqa1-32758. 同服务器配对数据用于 K=2 Adaptive paired t-test。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.6053}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-25T02:57:52.833411+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-cqa1-s44\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:53:41.130Z\", \"updated_at\": \"2026-05-25T02:53:41.130Z\", \"hypothesis\": \"VLA-only baseline Spatial s44 on cqa1-32758. 同服务器配对数据用于 K=2 Adaptive paired t-test。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.3331}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-25T02:57:52.833570+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-32758",
  "command": "mkdir -p /root/autodl-tmp/logs && tmux new-session -d -s eval-k2-adaptive-spatial-s42 \"CUDA_VISIBLE_DEVICES=0 bash -lc 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee /root/autodl-tmp/logs/eval-k2-adaptive-spatial-s42.log'\" && tmux new-session -d -s eval-vla-only-spatial-cqa1-s42 \"CUDA_VISIBLE_DEVICES=1 bash -lc 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20 2>&1 | tee /root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s42.log'\" && tmux new-session -d -s eval-k2-adaptive-spatial-s43 \"CUDA_VISIBLE_DEVICES=2 bash -lc 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 43 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee /root/autodl-tmp/logs/eval-k2-adaptive-spatial-s43.log'\" && tmux new-session -d -s eval-vla-only-spatial-cqa1-s43 \"CUDA_VISIBLE_DEVICES=3 bash -lc 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 43 --n_rollouts 20 2>&1 | tee /root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s43.log'\" && tmux new-session -d -s eval-k2-adaptive-spatial-s44 \"CUDA_VISIBLE_DEVICES=4 bash -lc 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 44 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee /root/autodl-tmp/logs/eval-k2-adaptive-spatial-s44.log'\" && tmux new-session -d -s eval-vla-only-spatial-cqa1-s44 \"CUDA_VISIBLE_DEVICES=5 bash -lc 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 44 --n_rollouts 20 2>&1 | tee /root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s44.log'\" && tmux ls",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "mkdir -p /root/autodl-tmp/logs && tmux new-session -d -s eval-k2-adaptive-spatial-s42 \"CUDA_VISIBLE_DEVICES=0 bash -lc 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee /root/autodl-tmp/logs/eval-k2-adaptive-spatial-s42.log'\" && tmux new-session -d -s eval-vla-only-spatial-cqa1-s42 \"CUDA_VISIBLE_DEVICES=1 bash -lc 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20 2>&1 | tee /root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s42.log'\" && tmux new-session -d -s eval-k2-adaptive-spatial-s43 \"CUDA_VISIBLE_DEVICES=2 bash -lc 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 43 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee /root/autodl-tmp/logs/eval-k2-adaptive-spatial-s43.log'\" && tmux new-session -d -s eval-vla-only-spatial-cqa1-s43 \"CUDA_VISIBLE_DEVICES=3 bash -lc 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 43 --n_rollouts 20 2>&1 | tee /root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s43.log'\" && tmux new-session -d -s eval-k2-adaptive-spatial-s44 \"CUDA_VISIBLE_DEVICES=4 bash -lc 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 44 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee /root/autodl-tmp/logs/eval-k2-adaptive-spatial-s44.log'\" && tmux new-session -d -s eval-vla-only-spatial-cqa1-s44 \"CUDA_VISIBLE_DEVICES=5 bash -lc 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 44 --n_rollouts 20 2>&1 | tee /root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s44.log'\" && tmux ls",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-25T02:57:52.833719+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"eval-k2-adaptive-spatial-s42: 1 windows (created Mon May 25 10:54:07 2026)\\neval-k2-adaptive-spatial-s43: 1 windows (created Mon May 25 10:54:07 2026)\\neval-k2-adaptive-spatial-s44: 1 windows (created Mon May 25 10:54:07 2026)\\neval-vla-only-spatial-cqa1-s42: 1 windows (created Mon May 25 10:54:07 2026)\\neval-vla-only-spatial-cqa1-s43: 1 windows (created Mon May 25 10:54:07 2026)\\neval-vla-only-spatial-cqa1-s44: 1 windows (created Mon May 25 10:54:07 2026)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-25T02:57:52.833869+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k2-adaptive-spatial-s42",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2', 'server': 'cqa1-32758', 'data_path': 'libero_spatial', 'data_count': 20, 'model_name': 'smolvla+crm', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'libero_spatial', 'log_path': '/root/autodl-tmp/logs/eval-k2-adaptive-spatial-s42.log', 'tmux_session': 'eval-k2-adaptive-spatial-s42'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k2-adaptive-spatial-s42",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2', 'server': 'cqa1-32758', 'data_path': 'libero_spatial', 'data_count': 20, 'model_name': 'smolvla+crm', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'libero_spatial', 'log_path': '/root/autodl-tmp/logs/eval-k2-adaptive-spatial-s42.log', 'tmux_session': 'eval-k2-adaptive-spatial-s42'}"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-25T02:57:52.834016+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 2.1641}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-25T02:57:52.834141+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k2-adaptive-spatial-s43",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 43 --n_rollouts 20 --max_correction_norm 0.2', 'server': 'cqa1-32758', 'data_path': 'libero_spatial', 'data_count': 20, 'model_name': 'smolvla+crm', 'seed': 43, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'libero_spatial', 'log_path': '/root/autodl-tmp/logs/eval-k2-adaptive-spatial-s43.log', 'tmux_session': 'eval-k2-adaptive-spatial-s43'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k2-adaptive-spatial-s43",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 43 --n_rollouts 20 --max_correction_norm 0.2', 'server': 'cqa1-32758', 'data_path': 'libero_spatial', 'data_count': 20, 'model_name': 'smolvla+crm', 'seed': 43, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'libero_spatial', 'log_path': '/root/autodl-tmp/logs/eval-k2-adaptive-spatial-s43.log', 'tmux_session': 'eval-k2-adaptive-spatial-s43'}"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-25T02:57:52.834292+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 2.1806}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-25T02:57:52.834420+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k2-adaptive-spatial-s44",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 44 --n_rollouts 20 --max_correction_norm 0.2', 'server': 'cqa1-32758', 'data_path': 'libero_spatial', 'data_count': 20, 'model_name': 'smolvla+crm', 'seed': 44, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'libero_spatial', 'log_path': '/root/autodl-tmp/logs/eval-k2-adaptive-spatial-s44.log', 'tmux_session': 'eval-k2-adaptive-spatial-s44'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k2-adaptive-spatial-s44",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 44 --n_rollouts 20 --max_correction_norm 0.2', 'server': 'cqa1-32758', 'data_path': 'libero_spatial', 'data_count': 20, 'model_name': 'smolvla+crm', 'seed': 44, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'libero_spatial', 'log_path': '/root/autodl-tmp/logs/eval-k2-adaptive-spatial-s44.log', 'tmux_session': 'eval-k2-adaptive-spatial-s44'}"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-25T02:57:52.834553+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 2.7837}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-25T02:57:52.834680+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-cqa1-s42",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20', 'server': 'cqa1-32758', 'data_path': 'libero_spatial', 'data_count': 20, 'model_name': 'smolvla', 'seed': 42, 'checkpoint_source': 'smolvla_base', 'eval_data': 'libero_spatial', 'log_path': '/root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s42.log', 'tmux_session': 'eval-vla-only-spatial-cqa1-s42'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-cqa1-s42",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20', 'server': 'cqa1-32758', 'data_path': 'libero_spatial', 'data_count': 20, 'model_name': 'smolvla', 'seed': 42, 'checkpoint_source': 'smolvla_base', 'eval_data': 'libero_spatial', 'log_path': '/root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s42.log', 'tmux_session': 'eval-vla-only-spatial-cqa1-s42'}"
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-25T02:57:52.834810+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-cqa1-s43",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 43 --n_rollouts 20', 'server': 'cqa1-32758', 'data_path': 'libero_spatial', 'data_count': 20, 'model_name': 'smolvla', 'seed': 43, 'checkpoint_source': 'smolvla_base', 'eval_data': 'libero_spatial', 'log_path': '/root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s43.log', 'tmux_session': 'eval-vla-only-spatial-cqa1-s43'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-cqa1-s43",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 43 --n_rollouts 20', 'server': 'cqa1-32758', 'data_path': 'libero_spatial', 'data_count': 20, 'model_name': 'smolvla', 'seed': 43, 'checkpoint_source': 'smolvla_base', 'eval_data': 'libero_spatial', 'log_path': '/root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s43.log', 'tmux_session': 'eval-vla-only-spatial-cqa1-s43'}"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-25T02:57:52.834938+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 4.2359}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-25T02:57:52.835056+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-cqa1-s44",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 44 --n_rollouts 20', 'server': 'cqa1-32758', 'data_path': 'libero_spatial', 'data_count': 20, 'model_name': 'smolvla', 'seed': 44, 'checkpoint_source': 'smolvla_base', 'eval_data': 'libero_spatial', 'log_path': '/root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s44.log', 'tmux_session': 'eval-vla-only-spatial-cqa1-s44'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-cqa1-s44",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 44 --n_rollouts 20', 'server': 'cqa1-32758', 'data_path': 'libero_spatial', 'data_count': 20, 'model_name': 'smolvla', 'seed': 44, 'checkpoint_source': 'smolvla_base', 'eval_data': 'libero_spatial', 'log_path': '/root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s44.log', 'tmux_session': 'eval-vla-only-spatial-cqa1-s44'}"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-25T02:57:52.835181+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 4.7691}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-25T02:57:52.835314+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 2.1175}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-25T02:57:52.835465+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k2-adaptive-spatial-s42",
  "field": "status",
  "value": "QUEUED",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k2-adaptive-spatial-s42",
    "field": "status",
    "value": "QUEUED",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-25T02:57:52.835588+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k2-adaptive-spatial-s43",
  "field": "status",
  "value": "QUEUED",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k2-adaptive-spatial-s43",
    "field": "status",
    "value": "QUEUED",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-25T02:57:52.835703+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k2-adaptive-spatial-s44",
  "field": "status",
  "value": "QUEUED",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k2-adaptive-spatial-s44",
    "field": "status",
    "value": "QUEUED",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-25T02:57:52.835814+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-cqa1-s42",
  "field": "status",
  "value": "QUEUED",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-cqa1-s42",
    "field": "status",
    "value": "QUEUED",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-25T02:57:52.835922+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-cqa1-s43",
  "field": "status",
  "value": "QUEUED",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-cqa1-s43",
    "field": "status",
    "value": "QUEUED",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-25T02:57:52.836031+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-cqa1-s44",
  "field": "status",
  "value": "QUEUED",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-cqa1-s44",
    "field": "status",
    "value": "QUEUED",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-25T02:57:52.836156+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k2-adaptive-spatial-s42\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:52:57.415Z\", \"updated_at\": \"2026-05-25T02:54:48.720Z\", \"hypothesis\": \"K=2 Adaptive Spatial (τ=0.25) 同服务器配对。K=2 是正确采样数（两次前向推理算 L2 距离做 gating）。配对 cqa1-32758 VLA-only baseline 用于 paired t-test。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 11.9522}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-25T02:57:52.836311+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k2-adaptive-spatial-s43\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:53:11.261Z\", \"updated_at\": \"2026-05-25T02:55:01.410Z\", \"hypothesis\": \"K=2 Adaptive Spatial (τ=0.25) 同服务器配对。K=2 是正确采样数（两次前向推理算 L2 距离做 gating）。配对 cqa1-32758 VLA-only baseline 用于 paired t-test。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 13.6225}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-25T02:57:52.836448+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k2-adaptive-spatial-s44\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:53:18.842Z\", \"updated_at\": \"2026-05-25T02:55:16.218Z\", \"hypothesis\": \"K=2 Adaptive Spatial (τ=0.25) 同服务器配对。K=2 是正确采样数（两次前向推理算 L2 距离做 gating）。配对 cqa1-32758 VLA-only baseline 用于 paired t-test。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 11.7468}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-25T02:57:52.836580+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-cqa1-s42\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:53:26.220Z\", \"updated_at\": \"2026-05-25T02:55:24.721Z\", \"hypothesis\": \"VLA-only baseline Spatial s42 on cqa1-32758. 同服务器配对数据用于 K=2 Adaptive paired t-test。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.6761}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-25T02:57:52.836706+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-cqa1-s43\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:53:33.714Z\", \"updated_at\": \"2026-05-25T02:55:36.639Z\", \"hypothesis\": \"VLA-only baseline Spatial s43 on cqa1-32758. 同服务器配对数据用于 K=2 Adaptive paired t-test。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.4445}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-25T02:57:52.836828+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-cqa1-s44\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:53:41.130Z\", \"updated_at\": \"2026-05-25T02:55:45.953Z\", \"hypothesis\": \"VLA-only baseline Spatial s44 on cqa1-32758. 同服务器配对数据用于 K=2 Adaptive paired t-test。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.4658}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-25T02:57:52.836949+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k2-adaptive-spatial-s42",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2', 'server': 'cqa1-32758', 'data_path': 'libero_spatial', 'data_count': 20, 'model_name': 'smolvla+crm', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'libero_spatial', 'log_path': '/root/autodl-tmp/logs/eval-k2-adaptive-spatial-s42.log', 'tmux_session': 'eval-k2-adaptive-spatial-s42'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k2-adaptive-spatial-s42",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2', 'server': 'cqa1-32758', 'data_path': 'libero_spatial', 'data_count': 20, 'model_name': 'smolvla+crm', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'libero_spatial', 'log_path': '/root/autodl-tmp/logs/eval-k2-adaptive-spatial-s42.log', 'tmux_session': 'eval-k2-adaptive-spatial-s42'}"
  }
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-25T02:57:52.837083+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k2-adaptive-spatial-s43",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 43 --n_rollouts 20 --max_correction_norm 0.2', 'server': 'cqa1-32758', 'data_path': 'libero_spatial', 'data_count': 20, 'model_name': 'smolvla+crm', 'seed': 43, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'libero_spatial', 'log_path': '/root/autodl-tmp/logs/eval-k2-adaptive-spatial-s43.log', 'tmux_session': 'eval-k2-adaptive-spatial-s43'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k2-adaptive-spatial-s43",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 43 --n_rollouts 20 --max_correction_norm 0.2', 'server': 'cqa1-32758', 'data_path': 'libero_spatial', 'data_count': 20, 'model_name': 'smolvla+crm', 'seed': 43, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'libero_spatial', 'log_path': '/root/autodl-tmp/logs/eval-k2-adaptive-spatial-s43.log', 'tmux_session': 'eval-k2-adaptive-spatial-s43'}"
  }
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-25T02:57:52.837218+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k2-adaptive-spatial-s44",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 44 --n_rollouts 20 --max_correction_norm 0.2', 'server': 'cqa1-32758', 'data_path': 'libero_spatial', 'data_count': 20, 'model_name': 'smolvla+crm', 'seed': 44, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'libero_spatial', 'log_path': '/root/autodl-tmp/logs/eval-k2-adaptive-spatial-s44.log', 'tmux_session': 'eval-k2-adaptive-spatial-s44'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k2-adaptive-spatial-s44",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 44 --n_rollouts 20 --max_correction_norm 0.2', 'server': 'cqa1-32758', 'data_path': 'libero_spatial', 'data_count': 20, 'model_name': 'smolvla+crm', 'seed': 44, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'libero_spatial', 'log_path': '/root/autodl-tmp/logs/eval-k2-adaptive-spatial-s44.log', 'tmux_session': 'eval-k2-adaptive-spatial-s44'}"
  }
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-25T02:57:52.837369+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-cqa1-s42",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20', 'server': 'cqa1-32758', 'data_path': 'libero_spatial', 'data_count': 20, 'model_name': 'smolvla', 'seed': 42, 'checkpoint_source': 'smolvla_base', 'eval_data': 'libero_spatial', 'log_path': '/root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s42.log', 'tmux_session': 'eval-vla-only-spatial-cqa1-s42'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-cqa1-s42",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20', 'server': 'cqa1-32758', 'data_path': 'libero_spatial', 'data_count': 20, 'model_name': 'smolvla', 'seed': 42, 'checkpoint_source': 'smolvla_base', 'eval_data': 'libero_spatial', 'log_path': '/root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s42.log', 'tmux_session': 'eval-vla-only-spatial-cqa1-s42'}"
  }
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-25T02:57:52.837495+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-cqa1-s43",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 43 --n_rollouts 20', 'server': 'cqa1-32758', 'data_path': 'libero_spatial', 'data_count': 20, 'model_name': 'smolvla', 'seed': 43, 'checkpoint_source': 'smolvla_base', 'eval_data': 'libero_spatial', 'log_path': '/root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s43.log', 'tmux_session': 'eval-vla-only-spatial-cqa1-s43'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-cqa1-s43",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 43 --n_rollouts 20', 'server': 'cqa1-32758', 'data_path': 'libero_spatial', 'data_count': 20, 'model_name': 'smolvla', 'seed': 43, 'checkpoint_source': 'smolvla_base', 'eval_data': 'libero_spatial', 'log_path': '/root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s43.log', 'tmux_session': 'eval-vla-only-spatial-cqa1-s43'}"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-25T02:57:52.837640+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k2-adaptive-spatial-s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:52:57.415Z\", \"updated_at\": \"2026-05-25T02:56:08.049Z\", \"hypothesis\": \"K=2 Adaptive Spatial (τ=0.25) 同服务器配对。K=2 是正确采样数（两次前向推理算 L2 距离做 gating）。配对 cqa1-32758 VLA-only baseline 用于 paired t-test。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"cqa1-32758\", \"data_path\": \"libero_spatial\", \"data_count\": 20, \"model_name\": \"smolvla+crm\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/autodl-tmp/logs/eval-k2-adaptive-spatial-s42.log\", \"tmux_session\": \"eval-k2-adaptive-spatial-s42\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 16.4746}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-25T02:57:52.837779+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-cqa1-s44",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 44 --n_rollouts 20', 'server': 'cqa1-32758', 'data_path': 'libero_spatial', 'data_count': 20, 'model_name': 'smolvla', 'seed': 44, 'checkpoint_source': 'smolvla_base', 'eval_data': 'libero_spatial', 'log_path': '/root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s44.log', 'tmux_session': 'eval-vla-only-spatial-cqa1-s44'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-cqa1-s44",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 44 --n_rollouts 20', 'server': 'cqa1-32758', 'data_path': 'libero_spatial', 'data_count': 20, 'model_name': 'smolvla', 'seed': 44, 'checkpoint_source': 'smolvla_base', 'eval_data': 'libero_spatial', 'log_path': '/root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s44.log', 'tmux_session': 'eval-vla-only-spatial-cqa1-s44'}"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-25T02:57:52.837925+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k2-adaptive-spatial-s43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:53:11.261Z\", \"updated_at\": \"2026-05-25T02:56:24.240Z\", \"hypothesis\": \"K=2 Adaptive Spatial (τ=0.25) 同服务器配对。K=2 是正确采样数（两次前向推理算 L2 距离做 gating）。配对 cqa1-32758 VLA-only baseline 用于 paired t-test。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 43 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"cqa1-32758\", \"data_path\": \"libero_spatial\", \"data_count\": 20, \"model_name\": \"smolvla+crm\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/autodl-tmp/logs/eval-k2-adaptive-spatial-s43.log\", \"tmux_session\": \"eval-k2-adaptive-spatial-s43\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.3149}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-25T02:57:52.838070+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k2-adaptive-spatial-s44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:53:18.842Z\", \"updated_at\": \"2026-05-25T02:56:32.450Z\", \"hypothesis\": \"K=2 Adaptive Spatial (τ=0.25) 同服务器配对。K=2 是正确采样数（两次前向推理算 L2 距离做 gating）。配对 cqa1-32758 VLA-only baseline 用于 paired t-test。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 44 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"cqa1-32758\", \"data_path\": \"libero_spatial\", \"data_count\": 20, \"model_name\": \"smolvla+crm\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/autodl-tmp/logs/eval-k2-adaptive-spatial-s44.log\", \"tmux_session\": \"eval-k2-adaptive-spatial-s44\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.5093}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-25T02:57:52.838225+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-cqa1-s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:53:26.220Z\", \"updated_at\": \"2026-05-25T02:56:45.258Z\", \"hypothesis\": \"VLA-only baseline Spatial s42 on cqa1-32758. 同服务器配对数据用于 K=2 Adaptive paired t-test。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"data_path\": \"libero_spatial\", \"data_count\": 20, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"smolvla_base\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s42.log\", \"tmux_session\": \"eval-vla-only-spatial-cqa1-s42\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 13.5185}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-25T02:57:52.838389+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-cqa1-s43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:53:33.714Z\", \"updated_at\": \"2026-05-25T02:56:58.821Z\", \"hypothesis\": \"VLA-only baseline Spatial s43 on cqa1-32758. 同服务器配对数据用于 K=2 Adaptive paired t-test。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 43 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"data_path\": \"libero_spatial\", \"data_count\": 20, \"model_name\": \"smolvla\", \"seed\": 43, \"checkpoint_source\": \"smolvla_base\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s43.log\", \"tmux_session\": \"eval-vla-only-spatial-cqa1-s43\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 13.6002}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-25T02:57:52.838533+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-cqa1-s44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:53:41.130Z\", \"updated_at\": \"2026-05-25T02:57:12.230Z\", \"hypothesis\": \"VLA-only baseline Spatial s44 on cqa1-32758. 同服务器配对数据用于 K=2 Adaptive paired t-test。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 44 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"data_path\": \"libero_spatial\", \"data_count\": 20, \"model_name\": \"smolvla\", \"seed\": 44, \"checkpoint_source\": \"smolvla_base\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s44.log\", \"tmux_session\": \"eval-vla-only-spatial-cqa1-s44\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.4384}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-25T02:57:52.838691+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "nvidia-smi --query-gpu=index,utilization.gpu,memory.used --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "nvidia-smi --query-gpu=index,utilization.gpu,memory.used --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-25T02:57:52.838819+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 16 %, 6471 MiB\\n1, 26 %, 6467 MiB\\n2, 16 %, 6471 MiB\\n3, 13 %, 6467 MiB\\n4, 15 %, 6471 MiB\\n5, 13 %, 6467 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.58}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-25T02:57:52.838937+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "tmux ls",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "tmux ls",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-25T02:57:52.839054+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'tmux' is not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-25T02:57:52.839167+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "ls -la /root/autodl-tmp/logs/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "ls -la /root/autodl-tmp/logs/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-25T02:57:52.839304+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 28\\ndrwxr-xr-x 2 root root 4096 May 25 10:54 .\\ndrwxr-xr-x 7 root root  107 May 25 10:38 ..\\n-rw-r--r-- 1 root root 1983 May 25 10:57 eval-k2-adaptive-spatial-s42.log\\n-rw-r--r-- 1 root root 1983 May 25 10:57 eval-k2-adaptive-spatial-s43.log\\n-rw-r--r-- 1 root root 1863 May 25 10:54 eval-k2-adaptive-spatial-s44.log\\n-rw-r--r-- 1 root root 1602 May 25 10:54 eval-vla-only-spatial-cqa1-s42.log\\n-rw-r--r-- 1 root root 1602 May 25 10:54 eval-vla-only-spatial-cqa1-s43.log\\n-rw-r--r-- 1 root root 1722 May 25 10:57 eval-vla-only-spatial-cqa1-s44.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-25T02:57:52.839428+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "tail -3 /root/autodl-tmp/logs/eval-k2-adaptive-spatial-s42.log /root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "tail -3 /root/autodl-tmp/logs/eval-k2-adaptive-spatial-s42.log /root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-25T02:57:52.839546+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"tail: option used in invalid context -- 3\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-25T02:57:52.839657+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "tail -n 5 /root/autodl-tmp/logs/eval-k2-adaptive-spatial-s42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "tail -n 5 /root/autodl-tmp/logs/eval-k2-adaptive-spatial-s42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-25T02:57:52.839780+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[eval] Override max_correction_norm = 0.2\\n[eval] Loading LIBERO spatial environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate: rollout 5/20, success so far: 5/5\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-25T02:57:52.839893+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "tail -n 5 /root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "tail -n 5 /root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-25T02:57:52.840008+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Reducing the number of VLM layers to 16 ...\\nLoading weights from local directory\\n[eval] Loading LIBERO spatial environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 78 · 2026-05-25T02:57:52.840155+00:00_

部署完成。

| GPU | 实验 | 状态 |
|-----|------|------|
| 0 | eval-k2-adaptive-spatial-s42 | RUNNING（rollout 5/20，5/5 success） |
| 1 | eval-vla-only-spatial-cqa1-s42 | RUNNING（10 tasks loaded） |
| 2 | eval-k2-adaptive-spatial-s43 | RUNNING |
| 3 | eval-vla-only-spatial-cqa1-s43 | RUNNING |
| 4 | eval-k2-adaptive-spatial-s44 | RUNNING |
| 5 | eval-vla-only-spatial-cqa1-s44 | RUNNING |

6 个 tmux session 全部启动，6 GPU 全部活跃（13-26% util，6.4GB mem each）。日志写入 `/root/autodl-tmp/logs/`。Registry 全部置 RUNNING。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156"
}
```

</details>

---
