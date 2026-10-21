# analysis exp 004 eval trajectory

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-004-eval-trajectory_20260520T144225_result.json`
- **Structured JSON:** [`be7413ff0dba3bb44cdd.json`](../../sessions/be/be7413ff0dba3bb44cdd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

```
ckpt-4000: ToF=0.1215, NoF=0.8950, SYCONScore=0.2140, n_total=362
ckpt-6000: ToF=0.1547, NoF=0.8508, SYCONScore=0.2618, n_total=362
ckpt-1000: 结果文件不存在（目录下无 ckpt1000 相关文件，可能仍在运行或未启动）
```

补全后的完整训练轨迹：

| Checkpoint | ToF | NoF | SYCONScore |
|---|---|---|---|
| 500 | 0.0939 | 0.8895 | 0.1699 |
| 1000 | — | — | — |
| 2000 | 0.1492 | 0.8785 | 0.2550 |
| **4000** | **0.1215** | **0.8950** | **0.2140** |
| **6000** | **0.1547** | **0.8508** | **0.2618** |
| 8000 | 0.1823 | 0.8674 | 0.3013 |

值得注意：ckpt-4000 的 SYCONScore (0.2140) 低于 ckpt-2000 (0.2550)，曲线在 2000→4000 出现回落，之后 6000→8000 恢复上升趋势。这可能是训练中期的波动。

---
