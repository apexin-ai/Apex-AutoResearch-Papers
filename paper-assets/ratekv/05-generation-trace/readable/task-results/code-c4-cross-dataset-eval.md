# code c4 cross dataset eval

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_c4_cross_dataset_eval_20260514T011833_result.json`
- **Structured JSON:** [`a7df488df887273c4c2f.json`](../../sessions/a7/a7df488df887273c4c2f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

C4 Cross-Dataset Evaluation 完成。结果汇总：

| Metric | WikiText-2 cal | C4 cal |
|--------|---------------|--------|
| MCKP PPL (WikiText-2 eval) | 11.2312 | 11.3285 |
| Uniform 4-bit PPL | 15.4454 | 15.4454 |
| Delta (uniform - MCKP) | +4.2142 | +4.1170 |
| Bit distribution | {8:4, 4:100, 2:8} | {8:4, 4:100, 2:8} |

**跨数据集一致性：**
- **Allocation agreement: 98.2%** (110/112 heads 完全一致)
- 仅 2 处差异：L3H0 (WT2:4bit↔C4:2bit) 和 L4H2 (WT2:2bit↔C4:4bit) — 本质是两个 head 互换了 2/4 bit 分配
- Bit distribution 宏观完全一致
- PPL 改善幅度差距仅 0.097（4.21 vs 4.12）

结论：MCKP 分配方案对校准数据集高度稳定，跨 WikiText-2/C4 的一致性极强。

---
