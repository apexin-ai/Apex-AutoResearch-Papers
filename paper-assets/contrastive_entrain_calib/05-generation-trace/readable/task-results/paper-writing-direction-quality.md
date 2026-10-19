# paper writing direction quality

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_direction_quality_20260520T074123_result.json`
- **Structured JSON:** [`fafee3570caec8b2604e.json`](../../sessions/fa/fafee3570caec8b2604e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

§3 已写入 `docs/paper/sections/direction_quality.tex`。

**覆盖内容**:
- Qwen3-8B: CV AUROC 0.827±0.028 (L19), 层级渐进式 emergence (L0 chance → L16 significant → L19 peak)
- 证据强度梯度: weak 0.675 → medium 0.883 → strong 0.929
- Cross-model: Llama-3-8B CV AUROC 0.779±0.019 (L16), style-controlled 0.923, domain AUROCs 0.751–0.844
- 内联 Table~\ref{tab:cross_model} 对比两模型
- Training stability: cosine sim ≈0.96 at step 500, per-layer AUROC ≥0.77
- Probe ablation: 0.835 vs random 0.727 (Δ=+0.108)
- Verdict: direction quality is not the bottleneck,为 §4–§5 failure 分析铺设 contrast

---
