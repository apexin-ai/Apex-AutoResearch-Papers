# eval collect ckpt1500 ckpt7000 results

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_collect-ckpt1500-ckpt7000-results_20260522T093939_result.json`
- **Structured JSON:** [`9714af3be3b65826d956.json`](../../sessions/97/9714af3be3b65826d956.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-004-s2-eval-ckpt1500 registry 已更新完毕。

**汇总：**

| Eval | SYCONScore | vs Vanilla (0.1335) | Status |
|------|-----------|---------------------|--------|
| ACT s2 ckpt-1500 | **0.2137** | +60% ✓ | DONE, registry updated |
| R3 s2 ckpt-7000 | — | — | 运行中 (260/362)，GPU1 活跃 |

ACT s2 趋势：ckpt-500=0.223 → ckpt-1000=0.256 → ckpt-1500=0.2137。出现下降但仍远高于 vanilla。Seed 1 同位置是 0.170，seed 2 表现明显更好。

R3 s2 ckpt-7000 预计还需 ~15 分钟完成，之后可再收集结果并更新 registry。

---
