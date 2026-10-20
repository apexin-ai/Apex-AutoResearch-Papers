# eval isr b01 s45 s46

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_isr-b01-s45-s46_20260517T052431_result.json`
- **Structured JSON:** [`f5cc9ea2392ef50c1dc3.json`](../../sessions/f5/f5cc9ea2392ef50c1dc3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。两个实验均已评估并更新 registry (status=DONE, conclusion=success)。

## 结果汇总

| Metric | s45 | s46 |
|--------|-----|-----|
| eval_prove_rate | 42% | 77% |
| eval_mean_isr | 0.254 | 0.316 |
| proved_only_isr | 0.605 | 0.411 |
| H7 (tautology) | 16 (38.1%) | 11 (14.3%) |
| H1 (exact copy) | 2 (4.8%) | 20 (26.0%) |
| H8 (degenerate) | 1 (2.4%) | 4 (5.2%) |
| **Genuine** | **23 (54.8%)** | **42 (54.5%)** |
| genuine_pct_total | 23% | 42% |

两个 seed 的 genuine rate (占 proved) 高度一致 (~55%)，远超 s43/s44 的 H7 collapse。s45 prove_rate 较低但 ISR 更高，s46 prove_rate 较高但 H1 占比更大。总体确认 ISR β=0.1 在多数 seed 下能保留相当比例的 genuine proof（s42=17.3%, s45=54.8%, s46=54.5%），仅 s43/s44 collapse。

---
