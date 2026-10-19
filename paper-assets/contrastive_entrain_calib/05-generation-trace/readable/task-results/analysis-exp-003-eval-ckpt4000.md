# analysis exp 003 eval ckpt4000

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-003-eval-ckpt4000_20260520T152939_result.json`
- **Structured JSON:** [`973ee48ef7b383bb8703.json`](../../sessions/97/973ee48ef7b383bb8703.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE (negative)。

## exp-003-eval-ckpt4000 结果

| 指标 | 值 |
|------|-----|
| **ToF** | 0.0608 |
| **NoF** | 0.9669 |
| **SYCONScore** | **0.1144** |
| n_valid / n_invalid / n_total | 181 / 181 / 362 |
| eval_time | 4353s |

### vs vanilla baseline

SYCONScore **0.1144 vs 0.1335 = -14.3%，低于 baseline**。

### exp-003 全 checkpoint 趋势

| checkpoint | ToF | NoF | SYCONScore |
|-----------|------|------|------------|
| 1000 | 0.0387 | 0.9448 | 0.0743 |
| 2000 | 0.0442 | 0.9834 | 0.0846 |
| 3000 | 0.0497 | 0.9724 | 0.0946 |
| **4000** | **0.0608** | **0.9669** | **0.1144** |
| 5000 | 0.0608 | 0.9669 | 0.1144 |

ckpt-4000 和 ckpt-5000 指标完全一致，说明模型在 step 4000 后已饱和，且所有 checkpoint 的 SYCONScore 均低于 vanilla baseline (0.1335)。R3-only GRPO 在 D027 评估下表现为 negative。

---
