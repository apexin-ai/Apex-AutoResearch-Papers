# research literature scan collapse

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature_scan_collapse_20260513T004727_result.json`
- **Structured JSON:** [`cffd3a29eae924e3d3d1.json`](../../sessions/cf/cffd3a29eae924e3d3d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存至 `artifacts/literature_scan_2025_2026.md`。核心结论：

**Novelty 安全** — 无人做过 ordinal depth estimation 或量化 discrimination boundary K*。我们的核心贡献无竞争。

**关键发现**：
- **Drayson et al. (EMNLP 2025) 是真实论文**，不是 Dream 审稿说的幻觉引用。它用 MGT 检测做 importance resampling 防止 collapse——正好是我们 depth estimator 的 binary 版本，应作为最近相关工作 cite
- **Schaeffer (ICML 2025)** 指出 model collapse 有 8 种不同定义，我们必须精确说明 K* 是 discriminability saturation，不是 test-loss collapse
- **He et al. (NeurIPS 2025)** 的 generalization→memorization 转变与我们的 feature-space convergence 高度对应
- **DivEye (TMLR 2026)** 的 surprisal diversity 特征和 **Surplexity** 可作为 full study 新 baseline

**Must-cite 4 篇**: Drayson EMNLP'25, Schaeffer ICML'25, Kazdan ICML'25, He NeurIPS'25。**Should-cite 4 篇**: DivEye, Amin NeurIPS'25, CoDeC ICLR'26, Surplexity。

---
