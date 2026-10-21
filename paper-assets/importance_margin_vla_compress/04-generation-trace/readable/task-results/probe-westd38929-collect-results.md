# probe westd38929 collect results

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_probe_westd38929-collect-results_20260522T004531_result.json`
- **Structured JSON:** [`a9a09212db42bb939d7e.json`](../../sessions/a9/a9a09212db42bb939d7e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 4 个实验仍在运行，尚未完成。当前进度：

## westd-38929 状态

| GPU | 实验 | 状态 | 当前进度 | 预计剩余 |
|-----|------|------|----------|----------|
| 0 | π0.5 L2norm k=0.9 Spatial | RUNNING | T7/10, 332/350=94.9% (截至T6) | ~15-20 min |
| 1 | π0.5 random k=0.9 Spatial | RUNNING | T6/10, 150/300=50.0% (截至T5) | ~40-50 min |
| 2 | π0.5 random k=0.925 Object | RUNNING | T3/10, 59/150=39.3% (截至T2) | ~60-70 min |
| 3 | π0.5 random k=0.85 Spatial | RUNNING | T4/10, 114/200=57.0% (截至T3) | ~55-65 min |

**GPU 状态**: 全部 4 卡在用（各 ~10.6GB/98GB，利用率 21-37%），无空闲 GPU。

**关键观察**:
- L2norm k=0.9 Spatial 表现极佳，目前累计 94.9%，T6 拿到 100%
- Random k=0.9 Spatial 表现差，累计只有 50%
- Random k=0.85 Spatial 早期不错（T0=76%, T2=86%）但 T3 崩到 4%
- Random k=0.925 Object 前几个 task 偏低（48%, 44%, 26%）

最早完成的是 L2norm k=0.9 Spatial（约 15-20 分钟后），最晚的是 Object 和 random k=0.85（约 1 小时后）。需要稍后再来收集最终结果。

---
