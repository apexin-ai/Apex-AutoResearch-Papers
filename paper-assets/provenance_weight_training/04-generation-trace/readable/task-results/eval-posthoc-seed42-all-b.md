# eval posthoc seed42 all b

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_posthoc_seed42_all_b_20260514T220906_result.json`
- **Structured JSON:** [`a18c9c2ca80071bef07b.json`](../../sessions/a1/a18c9c2ca80071bef07b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总结果：

## Seed42 Grid-b Post-hoc Eval 结果

| b 值 | eval_ppl | vs uniform (17.69) | 变化 |
|------|----------|---------------------|------|
| 0.5 | **17.651** | **-0.22%** | 最优 |
| 1.0 | 17.692 | -0.01% | ~持平 |
| 1.5 | 17.718 | +0.16% | 略差 |
| 2.0 | 17.741 | +0.29% | 差 |
| 3.0 | 17.774 | +0.47% | 差 |
| 5.0 | 17.818 | +0.72% | 最差 |

**Best-b = 0.5**, eval_ppl = 17.651, vs uniform 改善 **-0.22%**

### 跨 seed 对比

| | seed42 | seed123 |
|--|--------|---------|
| best-b | 0.5 | 0.5 |
| best eval_ppl | 17.651 | 17.638 |
| uniform PPL | 17.69 | 17.69 |
| 改善 % | -0.22% | -0.29% |

两个 seed 一致：**b=0.5 最优**，PPL 随 b 增大单调递增。改善幅度均很小（<0.3%），趋势高度一致。

---
