# eval detect remove r2 seed123 eval

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_detect_remove_r2_seed123_eval_20260522T085248_result.json`
- **Structured JSON:** [`1b119f0efdd29e532df7.json`](../../sessions/1b/1b119f0efdd29e532df7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 完成，registry 已更新。

**detect_remove_q05_v2_seed123_r2 结果：**

| Dataset | Loss | PPL | Tokens | seed42 PPL | Δ |
|---------|------|-----|--------|-----------|---|
| Holdout | 2.8491 | **17.272** | 4,077,068 ✓ | 17.285 | -0.013 |
| OWT | 2.8908 | **18.008** | 6,767,242 ✓ | 18.014 | -0.006 |
| Wiki | 2.7111 | **15.047** | 27,000,339 ✓ | 15.053 | -0.006 |

seed123 在三个数据集上都略优于 seed42，差异 <0.02，跨 seed 稳定性确认。

---
