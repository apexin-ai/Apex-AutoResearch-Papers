# ops exp016 reeval midcheck

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp016-reeval-midcheck_20260519T113821_result.json`
- **Structured JSON:** [`cc007a49c91f9a582a46.json`](../../sessions/cc/cc007a49c91f9a582a46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-016 统一 re-eval 中期状态

| 项目 | 状态 |
|---|---|
| PID | 126897, 运行 1h05m, CPU 418% |
| GPU 3 | 62% util, 16508 MiB |
| Alpha 列表 | `[0.0, 0.5, 1.0, 2.0, 5.0]` — 共 5 个 |
| 每个 alpha | 362 pairs |

### 进度

| Alpha | 状态 |
|---|---|
| 0.00 | **已完成** (~60 min, hooks fired 0 次 — baseline) |
| 0.50 | **进行中** 20/362 (5.5%) |
| 1.0 / 2.0 / 5.0 | 待运行 |

### 预估

- alpha=0.00 (baseline, 无 hook 介入): ~60 min/轮
- alpha=0.50 的前 20 pairs 耗时 ~4.5 min，推算 ~82 min/轮（hooks 生效后略慢）
- 剩余: alpha 0.50 还剩 ~78 min + 3 轮 × ~82 min ≈ **~5h 20min**
- 预计完成: **~01:00 AM (May 20)**

输出目录目前为空，结果应在全部 alpha 跑完后统一写入。

---
