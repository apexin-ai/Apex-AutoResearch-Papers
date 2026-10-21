# analyze eval xvla l2norm k03 goal seed42 v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/chats/worker_analyze_eval_xvla_l2norm_k03_goal_seed42_v3_20260524T040047.jsonl`
- **Structured JSON:** [`30335493ad7800a1da2f.json`](../../sessions/30/30335493ad7800a1da2f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

9 recorded events

### Tool call

_source line 1 · 2026-05-24T04:01:47.673687+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__list_wandb_runs,mcp__agent-ml-research__read_registry",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_xvla_l2norm_k03_goal_seed42_v3_20260524T040047",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__list_wandb_runs,mcp__agent-ml-research__read_registry",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-24T04:01:47.674176+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_xvla_l2norm_k03_goal_seed42_v3_20260524T040047",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-24T04:01:47.674469+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-38929",
  "command": "tail -100 ~/runs/importance_margin_vla_compress/eval_xvla_l2norm_k03_goal_seed42_v3.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_xvla_l2norm_k03_goal_seed42_v3_20260524T040047",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-38929",
    "command": "tail -100 ~/runs/importance_margin_vla_compress/eval_xvla_l2norm_k03_goal_seed42_v3.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-24T04:01:47.674799+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-24 11:42:58 [INFO]   Ep 22/50 | SUCCESS | steps=90\\n2026-05-24 11:43:12 [INFO]   Ep 23/50 | FAIL | steps=800\\n2026-05-24 11:43:15 [INFO]   Ep 24/50 | SUCCESS | steps=78\\n2026-05-24 11:43:17 [INFO]   Ep 25/50 | SUCCESS | steps=85\\n2026-05-24 11:43:20 [INFO]   Ep 26/50 | SUCCESS | steps=82\\n2026-05-24 11:43:23 [INFO]   Ep 27/50 | SUCCESS | steps=88\\n2026-05-24 11:43:26 [INFO]   Ep 28/50 | SUCCESS | steps=76\\n2026-05-24 11:43:29 [INFO]   Ep 29/50 | SUCCESS | steps=79\\n2026-05-24 11:43:42 [INFO]   Ep 30/50 | FAIL | steps=800\\n2026-05-24 11:43:45 [INFO]   Ep 31/50 | SUCCESS | steps=78\\n2026-05-24 11:43:59 [INFO]   Ep 32/50 | FAIL | steps=800\\n2026-05-24 11:44:13 [INFO]   Ep 33/50 | FAIL | steps=800\\n2026-05-24 11:44:26 [INFO]   Ep 34/50 | FAIL | steps=800\\n2026-05-24 11:44:29 [INFO]   Ep 35/50 | SUCCESS | steps=82\\n2026-05-24 11:44:33 [INFO]   Ep 36/50 | SUCCESS | steps=89\\n2026-05-24 11:44:37 [INFO]   Ep 37/50 | SUCCESS | steps=179\\n2026-05-24 11:44:40 [INFO]   Ep 38/50 | SUCCESS | steps=85\\n2026-05-24 11:44:43 [INFO]   Ep 39/50 | SUCCESS | steps=81\\n2026-05-24 11:44:46 [INFO]   Ep 40/50 | SUCCESS | steps=82\\n2026-05-24 11:44:48 [INFO]   Ep 41/50 | SUCCESS | steps=75\\n2026-05-24 11:44:51 [INFO]   Ep 42/50 | SUCCESS | steps=85\\n2026-05-24 11:44:54 [INFO]   Ep 43/50 | SUCCESS | steps=87\\n2026-05-24 11:44:57 [INFO]   Ep 44/50 | SUCCESS | steps=82\\n2026-05-24 11:45:00 [INFO]   Ep 45/50 | SUCCESS | steps=77\\n2026-05-24 11:45:14 [INFO]   Ep 46/50 | FAIL | steps=800\\n2026-05-24 11:45:27 [INFO]   Ep 47/50 | FAIL | steps=800\\n2026-05-24 11:45:30 [INFO]   Ep 48/50 | SUCCESS | steps=84\\n2026-05-24 11:45:35 [INFO]   Ep 49/50 | SUCCESS | steps=198\\n2026-05-24 11:45:48 [INFO]   Ep 50/50 | FAIL | steps=800\\n2026-05-24 11:45:48 [INFO]   Task 8 SR: 40/50 (80.0%)\\n2026-05-24 11:45:48 [INFO] --- Task 9: put the wine bottle on the rack ---\\n2026-05-24 11:46:02 [INFO]   Ep 1/50 | FAIL | steps=800\
…[truncated 4441 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_xvla_l2norm_k03_goal_seed42_v3_20260524T040047",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-24T04:01:47.675050+00:00_

called mcp__agent-ml-research__list_wandb_runs

<details open><summary>🔧 Tool call — mcp__agent-ml-research__list_wandb_runs</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "filters": "{'display_name': {'$regex': 'l2norm_k03_goal'}}",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_xvla_l2norm_k03_goal_seed42_v3_20260524T040047",
  "tool": "mcp__agent-ml-research__list_wandb_runs",
  "tool_args": {
    "project": "importance_margin_vla_compress",
    "filters": "{'display_name': {'$regex': 'l2norm_k03_goal'}}",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-24T04:01:47.675293+00:00_

Error executing tool list_wandb_runs: list_wandb_runs() got an unexpected keyword argument 'wandb_project'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_xvla_l2norm_k03_goal_seed42_v3_20260524T040047",
  "tool": "mcp__agent-ml-research__list_wandb_runs",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-24T04:01:47.675498+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "filters": "{'name': 'eval_xvla_l2norm_k03_goal_seed42_v3'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_xvla_l2norm_k03_goal_seed42_v3_20260524T040047",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "importance_margin_vla_compress",
    "filters": "{'name': 'eval_xvla_l2norm_k03_goal_seed42_v3'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-24T04:01:47.675727+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.4177}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_xvla_l2norm_k03_goal_seed42_v3_20260524T040047",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-24T04:01:47.676052+00:00_

评估**已完成**，全部 500 episodes 跑完，进程正常退出 (EXIT_CODE=0)。Registry 标记 failed 是误判。

## 结果

**Overall SR: 188/500 (37.6%)**，95% Wilson CI: [33.5%, 41.9%]

| Task | SR | Description |
|------|-----|-------------|
| 0 | 42% (21/50) | open the middle drawer of the cabinet |
| 1 | **94%** (47/50) | put the bowl on the stove |
| 2 | 16% (8/50) | put the wine bottle on top of the cabinet |
| 3 | 24% (12/50) | open the top drawer and put the bowl inside |
| 4 | **98%** (49/50) | put the bowl on top of the cabinet |
| 5 | 0% (0/50) | push the plate to the front of the stove |
| 6 | 2% (1/50) | put the cream cheese in the bowl |
| 7 | 20% (10/50) | turn on the stove |
| 8 | **80%** (40/50) | put the bowl on the plate |
| 9 | 0% (0/50) | put the wine bottle on the rack |

## 对比分析

| 配置 | Goal SR |
|------|---------|
| X-VLA baseline | ~74% |
| X-VLA L2norm k=0.5 | 68.6% |
| **X-VLA Random k=0.3** | **50.6%** |
| **X-VLA L2norm k=0.3** | **37.6%** ← 本次 |
| X-VLA L2norm k=0.3 Object | 18.2% |

## 结论：**negative**

- 评估成功完成，不是 failed，但结果很差
- **L2norm k=0.3 (37.6%) 显著低于 Random k=0.3 (50.6%)**——L2norm 在同等压缩率下比随机裁剪还差 13 个百分点，说明 L2norm 作为 importance metric 在高压缩率下不仅无效，还起到了反向选择的效果
- 相比 baseline (74%) 下降约 49%（相对），相比 L2norm k=0.5 (68.6%) 下降 31 个百分点
- 任务方差极大：简单放置任务 (Task 1/4/8) 仍保持 80-98%，但精细操作任务 (Task 5/6/9) 完全崩溃至 0-2%
- L2norm 在 Object suite 也只有 18.2%，进一步确认该 metric 在高压缩率下系统性失败

Registry 应从 `conclusion=failed` 更正为 `conclusion=negative`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_eval_xvla_l2norm_k03_goal_seed42_v3_20260524T040047"
}
```

</details>

---
