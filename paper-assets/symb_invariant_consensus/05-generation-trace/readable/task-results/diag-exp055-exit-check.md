# diag exp055 exit check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp055-exit-check_20260519T035112_result.json`
- **Structured JSON:** [`9439f00c2c5956d16a70.json`](../../sessions/94/9439f00c2c5956d16a70.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:2 已释放 (0MiB, 0% util)。

## exp-055 结果汇总

| 指标 | 值 |
|------|-----|
| 状态 | **完成 (204/204)** |
| SC accuracy | 57.84% (118/204) |
| SICA accuracy | 57.84% (118/204) |
| Delta (SICA-SC) | **+0.00pp** |
| Discordant pairs | b=5 (SC+/SICA-), c=5 (SICA+/SC-) |
| McNemar p-value | **1.0** |
| Agreement rate | 95.1% |
| Wall time | 83.2 min |

**结论: Negative.** Multi-temperature sampling (T=0.3/0.7/1.2 各 4 traces) 与单温度 SC 完全无差异。discordant pairs 完美对称 (5:5)，说明混合温度增加的 diversity 并没有为 MaxSAT 提供额外 discriminative 信号。

**GPU 状态:** cuda:2 已释放。cuda:0/1/3 被其他实验占用。

---
