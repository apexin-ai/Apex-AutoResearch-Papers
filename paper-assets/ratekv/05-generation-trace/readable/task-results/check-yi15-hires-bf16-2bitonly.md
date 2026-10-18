# check yi15 hires bf16 2bitonly

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_yi15_hires_bf16_2bitonly_20260514T201226_result.json`
- **Structured JSON:** [`ae9ec17cc4c79b5b9c82.json`](../../sessions/ae/ae9ec17cc4c79b5b9c82.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有活跃的 cron，无需删除。

---

**实验完成，registry 已更新。总结：**

| 指标 | 值 |
|------|-----|
| top5_concentration | **0.7139** |
| top5_n_heads | 9 |
| baseline_calibration_ppl | 5.888 |
| delta_2bit_cv | 8.8991 |
| 最敏感 head | L4H3 (delta=13.12) |
| 耗时 | 0.96h |

**关键结论**：hires bf16 下 Yi-1.5 concentration = 0.7139，远超 0.50 阈值。标准 profiling 的 0.4934 是分辨率不足导致的低估。**Yi-1.5 不是 Claim 3 FAIL case**。L4H3 是极端 outlier（delta=13.12，第二名仅 0.55），独占绝大部分 sensitivity。

---
