# analysis exp 003 eval s2 ckpt8000

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-003-eval-s2-ckpt8000_20260522T170420_result.json`
- **Structured JSON:** [`68e039638fe62c449e1b.json`](../../sessions/68/68e039638fe62c449e1b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。结果摘要：

## exp-003-eval-s2-ckpt8000 结果

| 指标 | 值 |
|------|-----|
| **SYCONScore** | **0.1240** |
| ToF | 0.0663 |
| NoF | 0.9613 |
| n_total | 362 (valid=181, invalid=181) |

### 对比

| 对比对象 | SYCONScore | 差值 |
|----------|-----------|------|
| Vanilla baseline | 0.1335 | **-7.1%** (低于 baseline) |
| Seed 1 ckpt-8000 | 0.1433 | **-13.5%** (seed 2 更差) |
| Seed 2 ckpt-7500 | 0.1140 | +8.8% (略有回升但仍低于 baseline) |

### Conclusion: **negative**

R3-only seed 2 全 trajectory 确认失败——从 ckpt-2000 到 ckpt-8000 的 SYCONScore 范围 0.0845~0.1240，始终低于 vanilla baseline 0.1335。Seed 2 表现一致性差于 seed 1（seed 1 ckpt-8000 达到 0.1433，勉强超过 baseline），说明 R3-only 训练的效果不稳定且跨 seed 不可靠。

---
