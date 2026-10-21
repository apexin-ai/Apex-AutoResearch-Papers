# analysis fewnerd rho variance lp claim

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fewnerd-rho-variance-lp-claim_20260522T182104_result.json`
- **Structured JSON:** [`977e71361999e965271f.json`](../../sessions/97/977e71361999e965271f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心发现：

**Part A (ρ_sj 方差)**：s42 不是 outlier。degeneracy 三个 seed 一致 (8-9%)，ρ_sj_full 的 32% CV 来自退化实例在联合排名中的随机位置效应。ρ_sj_cond 更稳定 (CV=15%)，且真正重要的 LP_Δ 非常稳定 (0.07/0.09/0.12pp, σ=0.025)。方法是稳定的。

**Part B (LP overclaim)**：最大风险是**指标不透明**。论文 Table 4 报告 LP +1.39pp 用的是 instance-averaged F1，但没有标注。MF4 统一管线 (corpus micro-F1) 下只有 +0.09pp。审稿人若用标准 micro-F1 复现会得到完全不同的数字。

建议：(1) Table 4 caption 加 "(instance-averaged F1)" 标注；(2) appendix 补充 micro-F1 结果 (+0.09pp) 说明增益集中在少实体实例；(3) "definitive contrast" 改为 "clearest positive case"。

---
