# experiment dir j2 nli qwen3 14b

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_dir-j2-nli-qwen3-14b_20260520T175104_result.json`
- **Structured JSON:** [`e7399b188af07e6ea8a2.json`](../../sessions/e7/e7399b188af07e6ea8a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果：

| 配置 | Accuracy | Correct/204 | Δ (pp) | McNemar p | Discordant (b, c) |
|------|----------|-------------|--------|-----------|-------------------|
| **SC baseline (Qwen3-14B)** | 86.27% | 176/204 | — | — | — |
| DeBERTa standalone | 49.51% | 101/204 | — | — | — |
| **Combo w=1** | 85.78% | 175/204 | -0.49 | 1.0000 | (0, 1) |
| **Combo w=3** | 86.76% | 177/204 | +0.49 | 1.0000 | (2, 1) |
| **Combo w=5** | 86.76% | 177/204 | +0.49 | 1.0000 | (2, 1) |

**关键发现**：
- DeBERTa 独立准确率仅 49.51%，远低于 Qwen3-14B SC 的 86.27%
- w=3 和 w=5 时 combo 提升 +0.49pp（177 vs 176），但 McNemar p=1.0（不显著）
- DeBERTa 与 SC 仅 49% agreement，disagree 时 SC 远优于 DeBERTa（85 vs 11）
- NLI 对 Qwen3-14B 这种强 baseline 基本无法提供增量收益——边际效应被 SC 的高准确率完全淹没

结果已保存至 `/root/symb_invariant_consensus/results/dir_j2_nli_qwen3/results.json`。

---
