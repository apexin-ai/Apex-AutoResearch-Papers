# paper intro related work

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_intro-related-work_20260515T233142_result.json`
- **Structured JSON:** [`0bfc549057d47c7f2d2b.json`](../../sessions/0b/0bfc549057d47c7f2d2b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件已完成并注册。

**Introduction** (`paper/introduction.tex`):
- 5 段 + 3 条 contributions，约 1 页
- 开篇：20-60% 污染 + strong collapse 动机
- 中段：Drayson 的 b 需 per-model grid search → 提出 dual-constraint adaptive b*
- 核心公式：b* = inf{b : α_eff(b) ≥ τ} s.t. ESS(b*) ≥ n_min
- 结果：adaptive PPL 17.650±0.007 vs grid-best 17.646±0.007（within seed variance），优于 uniform (17.69) 和 ESS-only (17.73)
- Contributions: (1) dual-constraint framework, (2) matches grid-best + min > max intervention, (3) lightweight detector sufficiency

**Related Work** (`paper/related_work.tex`):
- 4 组 + Summary，约 1 页，20 篇引用
- Group 1: Collapse 动机 (Shumailov, Alemohammad, Dohmatob, Cheng)
- Group 2: Detect-and-reweight，Drayson 作为 closest prior work，3 点差异化 (b 选择/SIR vs loss reweight/检测器规模)
- Group 3: Data mixing (DoReMi, DSIR, Ye, AIOLI) + instance-level (SoftDedup, Sow)，区分 provenance-based vs loss/frequency/domain
- Group 4: 理论基础 (Golden Ratio, Wang convergence, PSIS, IW survey)

---
