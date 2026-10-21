# analysis w3 winogrande piqa multiplicity

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_w3-winogrande-piqa-multiplicity_20260521T093002_result.json`
- **Structured JSON:** [`f00381d1f1a06e8407f3.json`](../../sessions/f0/f00381d1f1a06e8407f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 artifact 全部注册完成。关键发现：

**WinoGrande** (2-choice, 1267 samples)
- **α ≈ 0.46** (pure) — 与 BoolQ (α≈0.49) 极为接近，远高于 4-choice benchmarks。这强烈支持 **format confound**：2-choice 任务天然有更高的 ambiguity，不论 task type
- Convergence σ 无显著趋势 (Spearman ρ=−0.20, p=0.78)
- Jaccard helped sets: RetNet-HGRN2 对在多个 ratio 显著 (p<0.01)，GDN-RetNet 混合；hurt sets 也有显著重叠

**PIQA** (2-choice, 1838 samples)
- **α ≈ 0.14** (pure) — 远低于 BoolQ 和 WinoGrande，反而接近 HellaSwag (α≈0.10)。这**打破了** pure format confound 假设——同为 2-choice，PIQA 的 ambiguity 却接近 4-choice MC
- Convergence σ 也不显著 (ρ=−0.50, p=0.45)
- Jaccard: PIQA 几乎所有 helped/hurt 对都 p<0.01（因为绝对 set size 小，重叠更容易显著）

**对比框架结论**：α 并非纯粹由 format (n_choices) 决定。WinoGrande≈BoolQ 但 PIQA≈HellaSwag，说明 task difficulty/ambiguity 本身是主要驱动因素，format 只是 partial confound。

---
