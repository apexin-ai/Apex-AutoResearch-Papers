# eval cqa1 xvla k095 seed43 seed44

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cqa1-xvla-k095-seed43-seed44_20260520T193807_result.json`
- **Structured JSON:** [`2a30e9edc905b21aef0b.json`](../../sessions/2a/2a30e9edc905b21aef0b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已运行：

| 实验 | GPU | tmux session | Python PID | 显存占用 |
|------|-----|-------------|-----------|---------|
| X-VLA k=0.95 seed43 | GPU 1 | `eval_xvla_k095_s43` | 961641 | 4540 MiB |
| X-VLA k=0.95 seed44 | GPU 3 | `eval_xvla_k095_s44` | 961802 | 4540 MiB |

注：首次启动时因 tmux 内未激活 conda 导致 `python: command not found`，已修复并重新启动。当前 4 个 GPU 全部在用（GPU 0: k=0.1 seed42, GPU 1: k=0.95 seed43, GPU 2: k=0.95 seed42, GPU 3: k=0.95 seed44）。

---
