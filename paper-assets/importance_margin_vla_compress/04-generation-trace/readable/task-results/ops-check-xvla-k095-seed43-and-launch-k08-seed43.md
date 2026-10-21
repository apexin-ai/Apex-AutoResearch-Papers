# ops check xvla k095 seed43 and launch k08 seed43

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-xvla-k095-seed43-and-launch-k08-seed43_20260520T203949_result.json`
- **Structured JSON:** [`8fdb2d02493c130d7faf.json`](../../sessions/8f/8fdb2d02493c130d7faf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务均完成。

---

## 任务 1: X-VLA k=0.95 seed43 结果

| 指标 | 值 |
|------|-----|
| **overall_success_rate** | **0.99** (495/500) |
| wilson_ci_95 | [0.9768, 0.9957] |
| vision tokens | 50 → 47 (保留 94%) |
| 耗时 | 50.0 min |

Per-task 明细：
- 7/10 tasks 达到 **100%** (50/50)
- Task 3 (bbq sauce): 98% (49/50)
- Task 5 (tomato sauce): 96% (48/50)
- Task 7 (milk): 96% (48/50)

## 任务 2: X-VLA k=0.8 seed43 启动状态

| 项目 | 值 |
|------|-----|
| tmux session | `eval_xvla_k08_s43` (created 04:40:37) |
| PID | **262573** |
| GPU | **GPU 1**, 占用 4046 MiB / 24564 MiB |
| 状态 | 模型加载中，正常运行 |

当前服务器 GPU 占用：GPU 0 (4537M), GPU 1 (4055M), GPU 2 (4540M), GPU 3 (空闲)。

---
