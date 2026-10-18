# check w41 progress final

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_w41_progress_final_20260528T112812_result.json`
- **Structured JSON:** [`305c884be32b86345ab3.json`](../../sessions/30/305c884be32b86345ab3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

| 实验 | GPU | 进度 | 当前位置 | 已运行 | 预计完成 (BJT) |
|------|-----|------|----------|--------|---------------|
| **Random k=0.95 s46** | cuda:0 | 470/500 (T9 ep20) | 累计 SR 58.4%→跑T9 | ~2h34m | **~19:36** (≈6min) |
| **L2norm k=0.7 s46** | cuda:1 | 410/500 (T8 ep10) | 累计 SR 64.5% | ~2h10m | **~19:55** (≈25min) |
| **Random k=0.5 s46** | cuda:2 | 450/500 (T8完,进T9) | 累计 SR 50.0% | ~2h34m | **~19:45** (≈15min) |

三个实验均无 eval_results JSON（尚未完成）。所有进程状态正常（PID 存活，CPU 活跃）。

**Random k=0.95 最快完成**，约 6 分钟内出结果；其余两个 15-25 分钟内陆续完成。全部在 C002 截止线 (20:00 BJT) 前完成无压力。

---
