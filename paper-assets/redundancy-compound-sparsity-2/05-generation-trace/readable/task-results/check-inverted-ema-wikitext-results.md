# check inverted ema wikitext results

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_inverted_ema_wikitext_results_20260512T171220_result.json`
- **Structured JSON:** [`02891a4d5c59cb0d27e5.json`](../../sessions/02/02891a4d5c59cb0d27e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已完成（PID 39080 已退出），结果文件已生成。

## 结果对比

| 策略 | PPL | 备注 |
|------|-----|------|
| **full** | **7.1822** | 无驱逐上限 |
| **recency** (D003) | **7.1758** | D003 baseline |
| **random** (D003) | **7.6432** | D003 baseline |
| **random** (本次) | **7.7097** | 本次重跑 |
| **ema_0.9** (D003) | **7.7788** | D003 original |
| **inverted_ema_0.9** | **8.7898** | 本次实验 |

## Decision Gate 判定

**inverted_ema PPL (8.7898) < random baseline (7.6432)？ —— NO**

inverted_ema_0.9 的 PPL 比所有 baseline 都差：
- 比 random 高 +1.15 (8.79 vs 7.64)
- 比 original ema_0.9 高 +1.01 (8.79 vs 7.78)
- 比 full 高 +1.61 (8.79 vs 7.18)

**VERDICT: FAIL**

反转 EMA 分数（驱逐高 EMA 分而非低 EMA 分）导致性能大幅恶化，说明 original EMA 策略的驱逐方向是正确的——低 EMA 分的 token 确实是更好的驱逐目标。这从反面验证了 EMA scoring 的有效性，但 inverted 变体本身不可行。

---
