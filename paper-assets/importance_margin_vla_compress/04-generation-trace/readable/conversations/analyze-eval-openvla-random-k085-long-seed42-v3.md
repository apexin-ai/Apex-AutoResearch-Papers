# analyze eval openvla random k085 long seed42 v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 5
- **Recorded user turns:** 0
- **Tool calls:** 2
- **Original source:** `logs/chats/worker_analyze_eval_openvla_random_k085_long_seed42_v3_20260526T143107.jsonl`
- **Structured JSON:** [`a908e9e6cd8f01cc7d4f.json`](../../sessions/a9/a908e9e6cd8f01cc7d4f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

5 recorded events

### Tool call

_source line 1 · 2026-05-26T14:31:37.649229+00:00_

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
  "session": "worker_analyze_eval_openvla_random_k085_long_seed42_v3_20260526T143107",
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

_source line 2 · 2026-05-26T14:31:37.649587+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_random_k085_long_seed42_v3_20260526T143107",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-26T14:31:37.649762+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41074",
  "command": "tail -100 /root/runs/importance_margin_vla_compress/eval_openvla_random_k085_long_seed42_v3.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_openvla_random_k085_long_seed42_v3_20260526T143107",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41074",
    "command": "tail -100 /root/runs/importance_margin_vla_compress/eval_openvla_random_k085_long_seed42_v3.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-26T14:31:37.649970+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[*] Loading OpenVLA from: /root/autodl-tmp/openvla-7b-finetuned-libero-10\\n\\rLoading checkpoint shards:   0%|          | 0/4 [00:00<?, ?it/s]\\rLoading checkpoint shards:  25%|██▌       | 1/4 [00:00<00:00,  7.92it/s]\\rLoading checkpoint shards:  75%|███████▌  | 3/4 [00:00<00:00,  9.56it/s]\\rLoading checkpoint shards: 100%|██████████| 4/4 [00:00<00:00,  9.90it/s]\\n[*] Model loaded, GPU: 15.1 GB\\n[*] Vision tokens: 256, dim: 4096\\n[*] Random pruning: k=0.85\\n[robosuite WARNING] No private macro file found! (__init__.py:7)\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[*] libero_10: 10 tasks x 50 episodes = 500 total\\n\\n[Task 1/10] put both the alphabet soup and the tomato sauce in the basket\\n[Pruning] 256 -> 217 vision tokens (k=0.85)\\n  Ep 10/50 task_sr=5/10 (1.0 eps/min)\\n  Ep 20/50 task_sr=15/20 (1.2 eps/min)\\n  Ep 30/50 task_sr=23/30 (1.2 eps/min)\\n  Ep 40/50 task_sr=28/40 (1.2 eps/min)\\n  Ep 50/50 task_sr=33/50 (1.1 eps/min)\\n  => Task SR: 0.660 (33/50)\\n\\n[Task 2/10] put both the cream cheese box and the butter in the basket\\n  Ep 10/50 task_sr=8/10 (1.2 eps/min)\\n  Ep 20/50 task_sr=14/20 (1.2 eps/min)\\n  Ep 30/50 task_sr=15/30 (1.1 eps/min)\\n  Ep 40/50 task_sr=20/40 (1.1 eps/min)\\n  Ep 50/50 task_sr=28/50 (1.1 eps/min)\\n  => Task SR: 0.560 (28/50)\\n\\n[Task 3/10] turn on the stove and put the moka pot on it\\n  Ep 10/50 task_sr=7/10 (1.1 eps/min)\\n  Ep 20/50 task_sr=13/20 (1.1 eps/min)\\n  Ep 30/50 task_sr=19/30 (1.1 eps/min)\\n  Ep 40/50 task_sr=26/40 (1.1 eps/min)\\n  Ep 50/50 task_sr=33/50 (1.1 eps/min)\\n  => Task SR: 0.660 (33/50)\\n\\n[Task 4/10] put the black bowl in the bottom drawer of the cabinet and close it\\n  Ep 10/50 task_sr=3/10 
…[truncated 2594 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_random_k085_long_seed42_v3_20260526T143107",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-26T14:31:37.650200+00:00_

**实验结果：OpenVLA Random k=0.85 Long (libero_10) seed42**

**Overall SR: 45.2% (226/500)**

10 tasks 各 50 episodes 全部完成，无错误。

| Task | SR |
|---|---|
| 1. alphabet soup + tomato sauce → basket | 66.0% (33/50) |
| 2. cream cheese + butter → basket | 56.0% (28/50) |
| 3. stove + moka pot | 66.0% (33/50) |
| 4. black bowl → drawer + close | 34.0% (17/50) |
| 5. white mug left + yellow mug right | 22.0% (11/50) |
| 6. book → caddy | 78.0% (39/50) |
| 7. white mug plate + chocolate pudding | 20.0% (10/50) |
| 8. alphabet soup + cream cheese → basket | 66.0% (33/50) |
| 9. both moka pots → stove | 30.0% (15/50) |
| 10. yellow mug → microwave + close | 14.0% (7/50) |

**与已知数据点对比（Long suite）：**

| 方法 | SR |
|---|---|
| Random k=0.9 | 46.8% |
| **Random k=0.85** | **45.2%** |
| Random k=0.7 | 38.8% |
| L2norm k=0.85 | 38.8% |

Random k=0.85 比 k=0.9 仅降 1.6pp，仍显著优于 L2norm k=0.85（+6.4pp），符合预期的单调递减趋势。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_eval_openvla_random_k085_long_seed42_v3_20260526T143107"
}
```

</details>

---
