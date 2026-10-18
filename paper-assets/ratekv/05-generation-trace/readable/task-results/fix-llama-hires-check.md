# fix llama hires check

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_llama_hires_check_20260514T214522_result.json`
- **Structured JSON:** [`f8d91bca880033c6ec8d.json`](../../sessions/f8/f8d91bca880033c6ec8d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

**实验结果汇总（Llama-3.1-8B hires bf16 2-bit only）：**

- **状态**：成功，256/256 heads 全部完成，耗时 59 min
- **top5_concentration = 0.5749**（12 heads 占 top-5%）
- **baseline_ppl = 6.5055**
- **t1/t5 = 59.05**（极端离群：L2H5 delta=15.26，远超第二名 L3H1 的 0.44）
- **CV = 7.7663**，L0 dominance = 0.67x

注意 L2H5 的 delta 是异常高的离群值（15.26 vs 均值 0.12），这意味着该头对 2-bit 量化极度敏感，是 MCKP 分配的首要保护目标。Table 3 的 Llama 行可以用这些数据替换 $^\ddagger$ 标记。

---
