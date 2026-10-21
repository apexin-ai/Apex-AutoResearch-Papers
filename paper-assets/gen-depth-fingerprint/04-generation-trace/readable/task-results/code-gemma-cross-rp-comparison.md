# code gemma cross rp comparison

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gemma-cross-rp-comparison_20260516T162904_result.json`
- **Structured JSON:** [`d0842934a322c1447fa9.json`](../../sessions/d0/d0842934a322c1447fa9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果已写入 `results/gemma_cross_rp_comparison.json`。

关键发现：
- **Depth retention**：rp=1.0 仅 1.7%（994/1061 停在 depth 0），rp=1.1 为 96.1%，差异 +0.9437
- **显著 domain shift**（所有 KS test p ≈ 0）：
  - `tail_decay` 效应最大（Cohen's d = 2.90）
  - `ttr` 和 `hapax_ratio` 次之（d ≈ 1.45）
  - `entropy_mean` 也有大效应（d = 1.13）
  - `entropy_std/max/min` 效应较小（|d| < 0.2）
- rp=1.0 的 Spearman ρ 存在但因深层样本极少（每层仅 15-19 条）可靠性有限

---
