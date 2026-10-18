# ops kill and probe cqa1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_and_probe_cqa1_20260529T033729_result.json`
- **Structured JSON:** [`d40a25a52896bd5dd791.json`](../../sessions/d4/d40a25a52896bd5dd791.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。cqa1-33015 GPU 状态：

| GPU | 状态 | 进程 |
|-----|------|------|
| **cuda:0** | **空闲** (0%, 1 MiB) | 无进程 |
| **cuda:1** | 占用 (33%, 10643 MiB) | PID 746595 — attn k=0.9 |
| **cuda:2** | 占用 (49%, 10509 MiB) | PID 752204 — random k=0.9 |
| **cuda:3** | 占用 (31%, 10503 MiB) | PID 746925 — random k=0.85 |

已清理：
- PID 726668 (attn k=0.95 v2 orphan) — killed
- PID 771290/771295 (attn k=0.95 v3 wrapper + python) — killed
- tmux sessions `eval_pi05_attn_k095_long_seed47` 和 `_v3` — killed

剩余 3 个 tmux sessions 均为合法运行的实验。**cuda:0 已完全释放可用。**

---
