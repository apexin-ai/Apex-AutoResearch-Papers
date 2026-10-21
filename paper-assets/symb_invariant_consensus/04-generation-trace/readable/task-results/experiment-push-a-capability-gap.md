# experiment push a capability gap

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_push-a-capability-gap_20260520T183548_result.json`
- **Structured JSON:** [`880cf248a1e4e70f9555.json`](../../sessions/88/880cf248a1e4e70f9555.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图已生成成功。全部产出完成，结果汇总：

**统计结果：**
- **Spearman ρ = 1.00** (p ≈ 0) — 完美单调关系（5 个点的 rank 完全一致）
- **Linear fit**: gain = 0.162 × gap + 6.71, **R² = 0.87**, p = 0.020
- **Sigmoid fit**: R² = 0.97（拟合更好，inflection point 在 gap ≈ 1 pp）
- **Break-even point (linear)**: gap ≈ −42 pp（即使 verifier 大幅弱于 generator，combo 仍有微弱正增益）

**Corollary 核心结论**：Combo gain 在 Δ（verifier standalone − generator SC）上单调递增。虽然 break-even 在 −42 pp，但有意义的增益 (> +1 pp) 实际只在 Δ > 0 时出现——verifier 必须在 standalone accuracy 上超过 generator 的 SC accuracy。

**输出文件** 在 `/root/symb_invariant_consensus/results/push_a_capability_gap_formalization/`：
- `results.json` — 完整数值结果
- `corollary.tex` — LaTeX-ready corollary 段落
- `capability_gap_scatter.pdf` + `.png` — 学术级 scatter plot（含 linear/sigmoid/isotonic 三条 fitted curves）

---
