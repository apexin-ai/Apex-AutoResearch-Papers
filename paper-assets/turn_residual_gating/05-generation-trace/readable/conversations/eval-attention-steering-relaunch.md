# eval attention steering relaunch

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_eval_attention_steering_relaunch_20260520T092543.jsonl`
- **Structured JSON:** [`9cb6b8ce1da2aba286fe.json`](../../sessions/9c/9cb6b8ce1da2aba286fe.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-20T09:26:41.857249+00:00_

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
  "session": "worker_eval_attention_steering_relaunch_20260520T092543",
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

_source line 2 · 2026-05-20T09:26:41.857650+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_attention_steering_relaunch_20260520T092543",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T09:26:41.857836+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "ls -la /root/turn_residual_gating/runs/attention_steering/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_attention_steering_relaunch_20260520T092543",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "ls -la /root/turn_residual_gating/runs/attention_steering/"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T09:26:41.857982+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 20\\ndrwxr-xr-x  2 root root    62 May 20 15:30 .\\ndrwxr-xr-x 15 root root  4096 May 20 15:18 ..\\n-rw-r--r--  1 root root 14193 May 20 15:30 phase2_tg_s42_v7_attention_steering.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.25}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_attention_steering_relaunch_20260520T092543",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T09:26:41.858131+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "cat /root/turn_residual_gating/runs/attention_steering/phase2_tg_s42_v7_attention_steering.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_attention_steering_relaunch_20260520T092543",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "cat /root/turn_residual_gating/runs/attention_steering/phase2_tg_s42_v7_attention_steering.json"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T09:26:41.858430+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"checkpoint\\\": \\\"/root/turn_residual_gating/runs/phase2_tg_s42_v7\\\",\\n  \\\"gate_type\\\": \\\"threadgate\\\",\\n  \\\"mode\\\": \\\"gen\\\",\\n  \\\"gar_variant\\\": \\\"ours\\\",\\n  \\\"model\\\": \\\"/root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct\\\",\\n  \\\"layer_range\\\": null,\\n  \\\"betas\\\": [\\n    0.0,\\n    0.5,\\n    1.0,\\n    2.0,\\n    5.0,\\n    10.0\\n  ],\\n  \\\"conversations_source\\\": \\\"generated\\\",\\n  \\\"num_conversations\\\": 5,\\n  \\\"results\\\": {\\n    \\\"beta_0.0\\\": {\\n      \\\"beta\\\": 0.0,\\n      \\\"avg_gar_per_turn\\\": [\\n        0.06960186826673091,\\n        0.02838589853427025,\\n        0.018258938607464754,\\n        0.023193509669519954,\\n        0.06530698545804683,\\n        0.034747890257293676,\\n        0.012885742522110232,\\n        0.013848798049578401,\\n        0.009360169622523378,\\n        0.00925463174569535\\n      ],\\n      \\\"mid_turns_avg_gar\\\": 0.028040310760668975,\\n      \\\"avg_ppl\\\": 1.4092668087271192,\\n      \\\"gar_curves\\\": [\\n        [\\n          0.06359952483971731,\\n          0.034448908838486,\\n          0.016376710850794153,\\n          0.019607226246448246,\\n          0.014657907203930828,\\n          0.009433028925064256,\\n          0.011485824140875097,\\n          0.015831627353242266,\\n          0.00891422347938614,\\n          0.01037777428975656\\n        ],\\n        [\\n          0.156626692629362,\\n          0.037979259407052476,\\n          0.02504711060806264,\\n          0.018457246425786028,\\n          0.013191473817087842,\\n          0.01228067005155846,\\n          0.015064822736206114,\\n          0.011210107373227926,\\n          0.01057901239426985,\\n          0.007441376629951838\\n        ],\\n        [\\n          0.02450216469809666,\\n          0.019350098909826013,\\n          0.01446332640584563,\\n          0.019659708416580608,\\n          0.0134640192
…[truncated 7031 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_attention_steering_relaunch_20260520T092543",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T09:26:41.858664+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "python3 -c \"import json; d=json.load(open('/root/turn_residual_gating/runs/attention_steering/phase2_tg_s42_v7_attention_steering.json')); [print(f'beta={v[\\\"beta\\\"]:.1f}  GAR={v[\\\"mid_turns_avg_gar\\\"]:.4f}  PPL={v[\\\"avg_ppl\\\"]:.3f}') for v in d['results'].values()]\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_attention_steering_relaunch_20260520T092543",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "python3 -c \"import json; d=json.load(open('/root/turn_residual_gating/runs/attention_steering/phase2_tg_s42_v7_attention_steering.json')); [print(f'beta={v[\\\"beta\\\"]:.1f}  GAR={v[\\\"mid_turns_avg_gar\\\"]:.4f}  PPL={v[\\\"avg_ppl\\\"]:.3f}') for v in d['results'].values()]\""
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T09:26:41.858807+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_attention_steering_relaunch_20260520T092543",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T09:26:41.858934+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep -E \"mid_turns_avg_gar|avg_ppl|\\\"beta\\\":\" /root/turn_residual_gating/runs/attention_steering/phase2_tg_s42_v7_attention_steering.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_attention_steering_relaunch_20260520T092543",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep -E \"mid_turns_avg_gar|avg_ppl|\\\"beta\\\":\" /root/turn_residual_gating/runs/attention_steering/phase2_tg_s42_v7_attention_steering.json"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T09:26:41.859059+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_attention_steering_relaunch_20260520T092543",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T09:26:41.859180+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep -E \"mid_turns_avg_gar|avg_ppl|\\\"beta\\\":\" /root/turn_residual_gating/runs/attention_steering/phase2_tg_s42_v7_attention_steering.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_attention_steering_relaunch_20260520T092543",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep -E \"mid_turns_avg_gar|avg_ppl|\\\"beta\\\":\" /root/turn_residual_gating/runs/attention_steering/phase2_tg_s42_v7_attention_steering.json"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T09:26:41.859298+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_attention_steering_relaunch_20260520T092543",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T09:26:41.859438+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep -E \"mid_turns_avg_gar|avg_ppl\" /root/turn_residual_gating/runs/attention_steering/phase2_tg_s42_v7_attention_steering.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_attention_steering_relaunch_20260520T092543",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep -E \"mid_turns_avg_gar|avg_ppl\" /root/turn_residual_gating/runs/attention_steering/phase2_tg_s42_v7_attention_steering.json"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T09:26:41.859567+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_attention_steering_relaunch_20260520T092543",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T09:26:41.859697+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep \"mid_turns_avg_gar\" /root/turn_residual_gating/runs/attention_steering/phase2_tg_s42_v7_attention_steering.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_attention_steering_relaunch_20260520T092543",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep \"mid_turns_avg_gar\" /root/turn_residual_gating/runs/attention_steering/phase2_tg_s42_v7_attention_steering.json"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-20T09:26:41.859891+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep \"avg_ppl\" /root/turn_residual_gating/runs/attention_steering/phase2_tg_s42_v7_attention_steering.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_attention_steering_relaunch_20260520T092543",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep \"avg_ppl\" /root/turn_residual_gating/runs/attention_steering/phase2_tg_s42_v7_attention_steering.json"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-20T09:26:41.860031+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"      \\\"mid_turns_avg_gar\\\": 0.028040310760668975,\\n      \\\"mid_turns_avg_gar\\\": 0.0286803367138914,\\n      \\\"mid_turns_avg_gar\\\": 0.03485284355846857,\\n      \\\"mid_turns_avg_gar\\\": 0.06200941945005268,\\n      \\\"mid_turns_avg_gar\\\": 0.6794909609465124,\\n      \\\"mid_turns_avg_gar\\\": 0.9589989741853427,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_attention_steering_relaunch_20260520T092543",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T09:26:41.860152+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep \"\\\"beta\\\":\" /root/turn_residual_gating/runs/attention_steering/phase2_tg_s42_v7_attention_steering.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_attention_steering_relaunch_20260520T092543",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep \"\\\"beta\\\":\" /root/turn_residual_gating/runs/attention_steering/phase2_tg_s42_v7_attention_steering.json"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-20T09:26:41.860277+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"      \\\"avg_ppl\\\": 1.4092668087271192,\\n      \\\"avg_ppl\\\": 1.3870307613646151,\\n      \\\"avg_ppl\\\": 1.359966127184918,\\n      \\\"avg_ppl\\\": 1.4106609466772357,\\n      \\\"avg_ppl\\\": 1.90823408739073,\\n      \\\"avg_ppl\\\": 4.220062564332077,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_attention_steering_relaunch_20260520T092543",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T09:26:41.860421+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"      \\\"beta\\\": 0.0,\\n      \\\"beta\\\": 0.5,\\n      \\\"beta\\\": 1.0,\\n      \\\"beta\\\": 2.0,\\n      \\\"beta\\\": 5.0,\\n      \\\"beta\\\": 10.0,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_attention_steering_relaunch_20260520T092543",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-20T09:26:41.860587+00:00_

结果完整，所有 6 个 β 值的数据都已存在。**不需要重跑。**

## Attention Steering 结果 (v7 TG, gen mode, N=5 convs)

| β | mid_turns_avg_GAR | avg_PPL |
|---:|------------------:|--------:|
| 0.0 | 0.0280 | 1.409 |
| 0.5 | 0.0287 | 1.387 |
| 1.0 | 0.0349 | 1.360 |
| 2.0 | 0.0620 | 1.411 |
| 5.0 | 0.6795 | 1.908 |
| 10.0 | 0.9590 | 4.220 |

关键观察：
- **β=0→1**: GAR 微增 (0.028→0.035)，PPL 略降至 1.36——steering 几乎免费
- **β=2**: GAR 翻倍至 0.062，PPL 仍与 baseline 持平 (1.41)
- **β=5**: GAR 跳至 0.68，PPL 开始上升到 1.91——steering 效果显著但代价可控
- **β=10**: GAR 接近饱和 0.96，PPL 恶化到 4.22——过度 steering 导致生成质量劣化

Registry 状态需要更新为 DONE。需要我更新吗？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_eval_attention_steering_relaunch_20260520T092543"
}
```

</details>

---
