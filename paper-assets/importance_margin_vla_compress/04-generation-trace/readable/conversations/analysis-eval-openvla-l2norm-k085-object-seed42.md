# analysis eval openvla l2norm k085 object seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 5
- **Recorded user turns:** 0
- **Tool calls:** 2
- **Original source:** `logs/chats/worker_analysis_eval_openvla_l2norm_k085_object_seed42_20260527T103831.jsonl`
- **Structured JSON:** [`8dfe5525bf2be653d873.json`](../../sessions/8d/8dfe5525bf2be653d873.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

5 recorded events

### Tool call

_source line 1 · 2026-05-27T10:39:01.110480+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__fetch_wandb_metrics",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_openvla_l2norm_k085_object_seed42_20260527T103831",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__fetch_wandb_metrics",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-27T10:39:01.110937+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_openvla_l2norm_k085_object_seed42_20260527T103831",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-27T10:39:01.111207+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "tail -100 ~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k085_object_seed42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_openvla_l2norm_k085_object_seed42_20260527T103831",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "tail -100 ~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k085_object_seed42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-27T10:39:01.111524+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[*] Loading OpenVLA from: /root/autodl-tmp/openvla-libero-object\\n\\rLoading checkpoint shards:   0%|          | 0/4 [00:00<?, ?it/s]\\rLoading checkpoint shards:  25%|██▌       | 1/4 [00:00<00:00,  9.19it/s]\\rLoading checkpoint shards:  75%|███████▌  | 3/4 [00:00<00:00, 12.35it/s]\\rLoading checkpoint shards: 100%|██████████| 4/4 [00:00<00:00, 12.72it/s]\\n[*] Model loaded, GPU: 15.1 GB\\n[*] Vision tokens: 256, dim: 4096\\n[*] L2 norm pruning: k=0.85\\n[robosuite WARNING] No private macro file found! (__init__.py:7)\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[*] libero_object: 10 tasks x 50 episodes = 500 total\\n\\n[Task 1/10] pick up the alphabet soup and place it in the basket\\n[L2 Pruning] 256 -> 217 vision tokens (k=0.85)\\n  Ep 10/50 task_sr=4/10 (1.8 eps/min)\\n  Ep 20/50 task_sr=11/20 (1.9 eps/min)\\n  Ep 30/50 task_sr=17/30 (1.9 eps/min)\\n  Ep 40/50 task_sr=25/40 (1.9 eps/min)\\n  Ep 50/50 task_sr=30/50 (1.9 eps/min)\\n  => Task SR: 0.600 (30/50)\\n\\n[Task 2/10] pick up the cream cheese and place it in the basket\\n  Ep 10/50 task_sr=4/10 (1.9 eps/min)\\n  Ep 20/50 task_sr=5/20 (1.9 eps/min)\\n  Ep 30/50 task_sr=10/30 (1.9 eps/min)\\n  Ep 40/50 task_sr=16/40 (1.9 eps/min)\\n  Ep 50/50 task_sr=20/50 (1.9 eps/min)\\n  => Task SR: 0.400 (20/50)\\n\\n[Task 3/10] pick up the salad dressing and place it in the basket\\n  Ep 10/50 task_sr=7/10 (2.0 eps/min)\\n  Ep 20/50 task_sr=13/20 (2.0 eps/min)\\n  Ep 30/50 task_sr=18/30 (2.0 eps/min)\\n  Ep 40/50 task_sr=23/40 (2.0 eps/min)\\n  Ep 50/50 task_sr=30/50 (2.0 eps/min)\\n  => Task SR: 0.600 (30/50)\\n\\n[Task 4/10] pick up the bbq sauce and place it in the basket\\n  Ep 10/50 task_sr=5/10 (2.0 eps/min)\\n  Ep 20/50 t
…[truncated 2399 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_openvla_l2norm_k085_object_seed42_20260527T103831",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-27T10:39:01.111987+00:00_

```
overall_sr: 55.2%
per_task_sr:
  alphabet_soup: 60%
  cream_cheese: 40%
  salad_dressing: 60%
  bbq_sauce: 44%
  ketchup: 92%
  tomato_sauce: 42%
  butter: 50%
  milk: 58%
  chocolate_pudding: 52%
  orange_juice: 54%
n_episodes: 500
duration_min: 254.8
conclusion: success
analysis: 重跑结果与前次完全一致（overall 55.2%, 每个 task SR 逐一吻合），说明结果在 seed42 下是确定性的。k=0.85=55.2% < k=0.75=57.4% 的非单调性被确认——这不是随机波动，而是该 seed 下的稳定现象。L2norm cliff 曲线：k=0.95/0.9 → 70.6%（平台期），k=0.85 → 55.2%（陡降），k=0.75 → 57.4%（小幅回升），k=0.7 → 49.8%，k=0.5 → 39.2%。非单调点可能源于 L2norm 在 k=0.85 处裁剪掉了某些对特定 task 关键但 norm 不高的 token，而 k=0.75 的更激进裁剪反而保留了不同的 token 子集组合。
```

无错误无警告，EXIT_CODE=0，正常完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_eval_openvla_l2norm_k085_object_seed42_20260527T103831"
}
```

</details>

---
