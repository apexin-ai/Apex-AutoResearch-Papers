# ops p90 ppl verify

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_p90_ppl_verify_20260518T160940_result.json`
- **Structured JSON:** [`565068f7efe40c4de9f4.json`](../../sessions/56/565068f7efe40c4de9f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

补充 GPT-2 XL nucleus d2 的分位数：

| 统计量 | 值 |
|---|---|
| p10 | 62.35 |
| p25 | 75.80 |
| p75 | 112.47 |
| p90 | 140.51 |
| std | 1805.84 |

论文声称的 "65-92" 与数据不匹配：
- p10=62.35 接近下界 65，但 median=92.33 不是上界而是中位数
- IQR 是 75.80-112.47
- "65-92" 可能指的是 **p10 到 median** 的范围，或者论文引用的是不同的统计口径

---
