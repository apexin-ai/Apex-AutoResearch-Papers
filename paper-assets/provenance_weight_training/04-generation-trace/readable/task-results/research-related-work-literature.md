# research related work literature

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_related_work_literature_20260514T161134_result.json`
- **Structured JSON:** [`0b34d1a8f07ce58516e7.json`](../../sessions/0b/0b34d1a8f07ce58516e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。文献笔记已写入 `artifacts/literature_notes.md` 并注册（`art_20260514_696d46`）。

**7 篇论文整理结果：**

| 论文 | 定位 | 核心差异 |
|------|------|---------|
| Drayson et al. (EMNLP 2025) | direct-competitor | validation-based 固定 b vs 我们 adaptive b*；ModernBERT vs TF-IDF |
| Golden Ratio Weighting | background | known provenance + 全局常数权重 vs unknown provenance + adaptive |
| Strong Model Collapse (ICLR 2025) | background/motivation | 诊断问题（0.1% 污染即致命），不提供方案 |
| Dynamic Loss-Based Reweighting (ICLR 2025) | background | loss-based signal vs provenance detection signal |
| SoftDedup (ACL 2024) | background | n-gram commonness vs detection score，不涉及 model collapse |
| Escaping via Verification | direct-competitor | hard accept/reject vs soft weighting；verifier ceiling vs adaptive b* |
| 收敛理论 (arXiv 2602.16065) | method-component | 我们的理论 motivation 来源，从其收敛速率公式推导加权方案 |

Drayson 论文的 weighting 公式 $w_j = (1-q(x_j))^b / \sum_l (1-q(x_l))^b$ 已确认，b 通过 validation per-model 固定（小模型 b=10，大模型 b=1），这是我们 adaptive b* 的核心差异化点。

---
