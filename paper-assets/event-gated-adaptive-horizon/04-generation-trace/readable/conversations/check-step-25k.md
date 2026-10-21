# check step 25k

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_check_step-25k_20260513T061613.jsonl`
- **Structured JSON:** [`9951454673df15a031e2.json`](../../sessions/99/9951454673df15a031e2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-13T06:17:33.940626+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__detect_image",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_step-25k_20260513T061613",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__detect_image",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-13T06:17:33.941011+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_step-25k_20260513T061613",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-13T06:17:33.941185+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "ps -p 18110,9409 -o pid,etime,pcpu,pmem,comm --no-headers",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_step-25k_20260513T061613",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "ps -p 18110,9409 -o pid,etime,pcpu,pmem,comm --no-headers",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-13T06:17:33.941330+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  9409    04:12:55 1165  0.3 python\\n 18110    01:26:51 1136  0.3 python\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.13}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_step-25k_20260513T061613",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-13T06:17:33.941525+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "python3 -c \"\nimport json, os\nfor name, logdir in [('baseline', 'logdir/baseline_s1'), ('event_gated_v2', 'logdir/event_gated_s1_v2')]:\n    print(f'=== {name} ===')\n    mf = os.path.join('/root/autodl-tmp/event-gated-adaptive-horizon', logdir, 'metrics.jsonl')\n    if not os.path.exists(mf):\n        print('  No metrics.jsonl found')\n        continue\n    with open(mf) as f:\n        lines = f.readlines()\n    print(f'  Total entries: {len(lines)}')\n    for line in lines[-20:]:\n        d = json.loads(line)\n        step = d.get('step', '?')\n        fields = {k: round(v, 3) if isinstance(v, float) else v for k, v in d.items() if any(x in k for x in ['return', 'gate', 'loss', 'entropy', 'scale'])}\n        print(f'  step={step}: {fields}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_step-25k_20260513T061613",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "python3 -c \"\nimport json, os\nfor name, logdir in [('baseline', 'logdir/baseline_s1'), ('event_gated_v2', 'logdir/event_gated_s1_v2')]:\n    print(f'=== {name} ===')\n    mf = os.path.join('/root/autodl-tmp/event-gated-adaptive-horizon', logdir, 'metrics.jsonl')\n    if not os.path.exists(mf):\n        print('  No metrics.jsonl found')\n        continue\n    with open(mf) as f:\n        lines = f.readlines()\n    print(f'  Total entries: {len(lines)}')\n    for line in lines[-20:]:\n        d = json.loads(line)\n        step = d.get('step', '?')\n        fields = {k: round(v, 3) if isinstance(v, float) else v for k, v in d.items() if any(x in k for x in ['return', 'gate', 'loss', 'entropy', 'scale'])}\n        print(f'  step={step}: {fields}')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-13T06:17:33.941675+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: python expression contains disallowed call 'open('. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_step-25k_20260513T061613",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-13T06:17:33.941842+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "tail -30 /root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_s1_v2/metrics.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_step-25k_20260513T061613",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "tail -30 /root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_s1_v2/metrics.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-13T06:17:33.942105+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"step\\\": 20000, \\\"dataset_size\\\": 10000.0, \\\"train_return\\\": 141.51861572265625, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 20.0}\\n{\\\"step\\\": 20000, \\\"dataset_size\\\": 10000.0, \\\"train_return\\\": 101.39424133300781, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 20.0}\\n{\\\"step\\\": 20000, \\\"dataset_size\\\": 10000.0, \\\"train_return\\\": 201.09291076660156, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 20.0}\\n{\\\"step\\\": 20000, \\\"dataset_size\\\": 10000.0, \\\"train_return\\\": 203.7877960205078, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 20.0}\\n{\\\"step\\\": 24000, \\\"dataset_size\\\": 12000.0, \\\"train_return\\\": 288.417724609375, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 24.0}\\n{\\\"step\\\": 24000, \\\"dataset_size\\\": 12000.0, \\\"train_return\\\": 243.7779541015625, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 24.0}\\n{\\\"step\\\": 24000, \\\"dataset_size\\\": 12000.0, \\\"train_return\\\": 212.40182495117188, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 24.0}\\n{\\\"step\\\": 24000, \\\"dataset_size\\\": 12000.0, \\\"train_return\\\": 241.13333129882812, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 24.0}\\n{\\\"step\\\": 25000}\\n{\\\"step\\\": 25000, \\\"eval_return\\\": 254.15660400390624, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\n{\\\"step\\\": 25000, \\\"model_loss\\\": 4.654725551605225, \\\"model_grad_norm\\\": 10.560991287231445, \\\"height_loss\\\": 0.003768698778003454, \\\"orientations_loss\\\": 0.1541288048028946, \\\"velocity_loss\\\": 0.7468116283416748, \\\"reward_loss\\\": 0.6493080258369446, \\\"cont_loss\\\": 7.034778946035658e-07, \\\"kl_free\\\": 1.0, \\\"dyn_scale\\\": 0.5, \\\"rep_scale\\\": 0.09999999999999999, \\\"dyn_loss\\\": 5.167846202850342, \\\"rep_loss\\\": 5.167846202850342, \\\"kl\\\": 5.156996250152588, \\\"prior_ent\\\": 36.63621139526367, \\\
…[truncated 6739 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_step-25k_20260513T061613",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-13T06:17:33.942273+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "tail -30 /root/autodl-tmp/event-gated-adaptive-horizon/logdir/baseline_s1/metrics.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_step-25k_20260513T061613",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "tail -30 /root/autodl-tmp/event-gated-adaptive-horizon/logdir/baseline_s1/metrics.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-13T06:17:33.942401+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "wc -l /root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_s1_v2/metrics.jsonl /root/autodl-tmp/event-gated-adaptive-horizon/logdir/baseline_s1/metrics.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_step-25k_20260513T061613",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "wc -l /root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_s1_v2/metrics.jsonl /root/autodl-tmp/event-gated-adaptive-horizon/logdir/baseline_s1/metrics.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-13T06:17:33.942631+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"step\\\": 96000, \\\"dataset_size\\\": 48000.0, \\\"train_return\\\": 884.1009521484375, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 96.0}\\n{\\\"step\\\": 96000, \\\"dataset_size\\\": 48000.0, \\\"train_return\\\": 917.7311401367188, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 96.0}\\n{\\\"step\\\": 96000, \\\"dataset_size\\\": 48000.0, \\\"train_return\\\": 870.9722900390625, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 96.0}\\n{\\\"step\\\": 96000, \\\"dataset_size\\\": 48000.0, \\\"train_return\\\": 800.812744140625, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 96.0}\\n{\\\"step\\\": 100000, \\\"dataset_size\\\": 50000.0, \\\"train_return\\\": 946.7332763671875, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 100.0}\\n{\\\"step\\\": 100000, \\\"dataset_size\\\": 50000.0, \\\"train_return\\\": 849.322021484375, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 100.0}\\n{\\\"step\\\": 100000, \\\"dataset_size\\\": 50000.0, \\\"train_return\\\": 933.149658203125, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 100.0}\\n{\\\"step\\\": 100000, \\\"dataset_size\\\": 50000.0, \\\"train_return\\\": 868.6571044921875, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 100.0}\\n{\\\"step\\\": 104000, \\\"dataset_size\\\": 52000.0, \\\"train_return\\\": 898.64111328125, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 104.0}\\n{\\\"step\\\": 104000, \\\"dataset_size\\\": 52000.0, \\\"train_return\\\": 956.0787353515625, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 104.0}\\n{\\\"step\\\": 104000, \\\"dataset_size\\\": 52000.0, \\\"train_return\\\": 840.941162109375, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 104.0}\\n{\\\"step\\\": 104000, \\\"dataset_size\\\": 52000.0, \\\"train_return\\\": 667.8370361328125, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 104.0}\\n{\\\"step\\\": 105000}\\n{\\\"step\\\": 105000, \\\"eval_return\\\": 915.6
…[truncated 5758 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_step-25k_20260513T061613",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-13T06:17:33.942791+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"   52 /root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_s1_v2/metrics.jsonl\\n  152 /root/autodl-tmp/event-gated-adaptive-horizon/logdir/baseline_s1/metrics.jsonl\\n  204 total\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_step-25k_20260513T061613",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-13T06:17:33.942973+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "grep eval_return /root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_s1_v2/metrics.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_step-25k_20260513T061613",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "grep eval_return /root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_s1_v2/metrics.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-13T06:17:33.943111+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"step\\\": 5000, \\\"eval_return\\\": 31.0005241394043, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\n{\\\"step\\\": 15000, \\\"eval_return\\\": 153.86034240722657, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\n{\\\"step\\\": 25000, \\\"eval_return\\\": 254.15660400390624, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\n{\\\"step\\\": 35000, \\\"eval_return\\\": 290.79222259521487, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_step-25k_20260513T061613",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-13T06:17:33.943235+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "grep eval_return /root/autodl-tmp/event-gated-adaptive-horizon/logdir/baseline_s1/metrics.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_step-25k_20260513T061613",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "grep eval_return /root/autodl-tmp/event-gated-adaptive-horizon/logdir/baseline_s1/metrics.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-13T06:17:33.943377+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"step\\\": 5000, \\\"eval_return\\\": 31.766443061828614, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\n{\\\"step\\\": 15000, \\\"eval_return\\\": 206.60508575439454, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\n{\\\"step\\\": 25000, \\\"eval_return\\\": 395.27398376464845, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\n{\\\"step\\\": 35000, \\\"eval_return\\\": 388.47438049316406, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\n{\\\"step\\\": 45000, \\\"eval_return\\\": 513.7663848876953, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\n{\\\"step\\\": 55000, \\\"eval_return\\\": 625.7251983642578, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\n{\\\"step\\\": 65000, \\\"eval_return\\\": 615.8622741699219, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\n{\\\"step\\\": 75000, \\\"eval_return\\\": 596.2760833740234, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\n{\\\"step\\\": 85000, \\\"eval_return\\\": 713.9324035644531, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\n{\\\"step\\\": 95000, \\\"eval_return\\\": 871.0643371582031, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\n{\\\"step\\\": 105000, \\\"eval_return\\\": 915.6716186523438, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\n{\\\"step\\\": 115000, \\\"eval_return\\\": 919.8135620117188, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.64}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_step-25k_20260513T061613",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-13T06:17:33.943605+00:00_

## 汇总

### 1. 进程状态

| 实验 | PID | 运行时间 | CPU% | 当前 step | 状态 |
|---|---|---|---|---|---|
| exp_003_event_gated_v2 | 18110 | 1h27m | 1136% | ~40K (train) / 35K (eval) | 运行中 |
| exp_001_baseline | 9409 | 4h13m | 1165% | ~116K (train) / 115K (eval) | 运行中 |

### 2. exp_003 已过 25K — 但 Phase 2 未激活

step 25K 和 35K 的 gate 指标完全一致，**gate 没有开启**：

| 指标 | step 25K | step 35K |
|---|---|---|
| **gate_scale** | **0.0** | **0.0** |
| **gate_loss** | **0.0** | **0.0** |
| gate_dt_mean | 1.0 | 1.0 |
| gate_dt_std | 0.0 | 0.0 |
| gate_dt_1_frac | 1.0 | 1.0 |
| gate_empirical_entropy | 0.0 | 0.0 |
| gate_entropy_ratio | 0.0 | 0.0 |
| gate_entropy_bonus | 0.098 | 0.097 |

**gate_scale=0.0 说明 Phase 2 的 gate loss 权重从未生效。** gate 网络没有参与训练，dt 分布退化为全 1（固定步长）。

可能原因：`gate_curriculum_phase1` 的阈值单位可能是 `update_count` 而非 `step`。step 35K 时 update_count=7599，离 25000 updates 还很远（约需 step ~170K）。需要检查代码中 gate curriculum 的判断逻辑。

### 3. eval_return 对比

| Step | exp_003 | baseline | ratio | 判定 |
|---|---|---|---|---|
| 5K | 31.0 | 31.8 | 0.976 | 通过 |
| 15K | 153.9 | 206.6 | 0.745 | **需关注** |
| 25K | 254.2 | 395.3 | 0.643 | **需关注** |
| 35K | 290.8 | 388.5 | 0.749 | **需关注** |

exp_003 在 15K 后持续落后 baseline 25-36%，ratio 均 < 0.8。

### 4. Baseline 最新状态

| Step | eval_return |
|---|---|
| 85K | 713.9 |
| 95K | 871.1 |
| 105K | 915.7 |
| 115K | 919.8 |

Baseline 在 85K-115K 区间表现强劲，已趋近收敛（919.8）。

### 5. 关键问题

1. **Phase 2 未激活是最大问题。** gate_scale 始终为 0，gate 网络完全冻结。需要检查 `gate_curriculum_phase1=25000` 的判断单位是 environment step 还是 update count。
2. **即使 gate 未激活，exp_003 也比 baseline 慢 25%+。** 这可能因为 gate 网络参数增加了模型容量但未参与有效训练，拖累了整体学习效率。
3. 建议：检查代码中 gate curriculum 的触发条件，确认是按 `step` 还是 `update_count` 计数。如果是后者，Phase 2 要到 ~step 170K 才会激活。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_check_step-25k_20260513T061613"
}
```

</details>

---
