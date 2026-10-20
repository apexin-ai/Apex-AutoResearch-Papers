# analysis method subset ablation

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_method_subset_ablation_20260515T230627_result.json`
- **Structured JSON:** [`97a8cd9993c73d38ceef.json`](../../sessions/97/97a8cd9993c73d38ceef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已完成并注册 (`art_20260515_93ff0d`)。核心发现：

**4/5 threshold 是唯一的最优阈值**：
- **3/5**: 6/6 robust 但 null FPR=50% — 不可接受
- **4/5**: 6/6 robust + null FPR=0% — 唯一的灵敏度×特异性最优点
- **5/5**: 仅 3/6 robust + FPR=0% — TY 低功效导致过于保守

**方法重要性**：
- Naive/Diff/Thresh/PermG 四个方法 Shapley 值相同（+0.375），对 ECE pairs 同等关键
- **TY 是唯一的冗余方法**（Shapley = −2.625），负贡献，其 0% FPR 的贡献已被 PermG 覆盖
- **PermG 最关键**：唯一兼具 0% null FPR 和 6/6 灵敏度的严格方法

**4/5 起效机制**：null 下最多 3 个方法（Naive+Diff+Thresh，三个高 FPR 方法）虚假一致，4/5 要求至少一个严格方法（PermG）确认，因此构造性地排除了假阳性。

---
