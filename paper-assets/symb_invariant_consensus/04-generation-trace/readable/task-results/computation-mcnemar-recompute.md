# computation mcnemar recompute

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_computation_mcnemar-recompute_20260519T061929_result.json`
- **Structured JSON:** [`d66b1be9b83072d3428c.json`](../../sessions/d6/d66b1be9b83072d3428c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总结果：

| Exp | n | 新SC% | SICA% | 新Δ(pp) | b(SC对SICA错) | c(SC错SICA对) | McNemar p | 显著性 |
|-----|---|-------|-------|---------|---------------|---------------|-----------|--------|
| exp-033 (seed42) | 204 | 55.88 | 59.31 | +3.43 | 3 | 10 | 0.0923 | ns |
| exp-052 (seed123) | 204 | 54.41 | 57.35 | +2.94 | 1 | 7 | 0.0703 | ns |
| exp-053 (seed456) | 204 | 55.88 | 55.88 | +0.00 | 3 | 3 | 1.0000 | ns |
| exp-057 (T=0.3) | 204 | 58.33 | 56.86 | -1.47 | 7 | 4 | 0.5488 | ns |
| exp-058 (T=0.5) | 204 | 58.33 | 57.35 | -0.98 | 3 | 1 | 0.6250 | ns |
| exp-054 (T=1.0) | 204 | 55.39 | 55.39 | +0.00 | 5 | 5 | 1.0000 | ns |
| exp-051 (K=8) | 204 | 58.33 | 56.37 | -1.96 | 7 | 3 | 0.3438 | ns |
| exp-026 (Qwen2.5-14B FOLIO) | 204 | 75.49 | 74.51 | -0.98 | 3 | 1 | 0.6250 | ns |
| exp-027 (Qwen3-14B FOLIO) | 204 | 84.80 | 84.31 | -0.49 | 4 | 3 | 1.0000 | ns |
| exp-034 (Qwen2.5-14B PW-600) | 600 | 71.33 | 70.83 | -0.50 | 14 | 11 | 0.6900 | ns |
| exp-039 (Qwen2.5-14B PW-600 v2) | 600 | 74.00 | 71.50 | -2.50 | 23 | 8 | 0.0107 | ** |
| exp-046 (Mistral PW-600, sanity) | 600 | 39.33 | 36.50 | -2.83 | 30 | 13 | 0.0137 | ** |

结论：
- **exp-046** (SC 未变，sanity check): p=0.0137**，与之前一致，SC 显著优于 SICA
- **exp-039**: p=0.0107**，SC 显著优于 SICA（b=23 > c=8）
- 其余 10 个实验均无显著差异（ns）
- exp-053/exp-054 的 Δ=0.00pp 确认 b=c（分别为 3=3 和 5=5）

JSON 结果已保存：
- `westd-25068:/root/symb_invariant_consensus/results/mcnemar_recomputed_25068.json`
- `westd-16639:/root/symb_invariant_consensus/results/mcnemar_recomputed_16639.json`

---
