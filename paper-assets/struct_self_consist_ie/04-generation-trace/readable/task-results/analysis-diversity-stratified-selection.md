# analysis diversity stratified selection

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_diversity_stratified_selection_20260515T044339_result.json`
- **Structured JSON:** [`60a52f78083ed96f0969.json`](../../sessions/60/60a52f78083ed96f0969.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 已保存到 `review_round2/diversity_stratified_selection.json`。

### 关键发现

**1. High-diversity 组的 oracle headroom 非常大：**
| 配置 | n | Oracle Headroom |
|------|---|-----------------|
| Qwen SciERC high-div | 232 | **+0.1631** (57.5% → 73.8%) |
| LLaMA SciERC high-div | 186 | **+0.2014** (56.3% → 76.4%) |

好样本确实存在——oracle 可以比 greedy 提升 16-20 个百分点。

**2. High-diversity 组的 selection gap 仍然近零或为负：**

| Signal | Qwen gap | LLaMA gap |
|--------|----------|-----------|
| SJ | -0.0006 | -0.0012 |
| FK | -0.0020 | -0.0008 |
| EM | -0.0192 | -0.0249 |
| Voting | -0.0255 | -0.0174 |
| Logprob | +0.0076 | +0.0196 |

SJ/FK 几乎为零（±0.2%），EM/Voting 甚至为负（选出的比 greedy 更差）。Logprob 是唯一正向信号但也极微弱（<2%），远不及 headroom。

**3. 是否排除了 constrained decoding confound？**

**是。** 在 high-diversity 组中：
- 样本 diversity 充足（n_unique ≥ 4，即 8 个样本中至少 4 种不同输出）
- Oracle headroom 16-20%，证明好样本存在
- 但所有 5 个 selection signal 的 gap 都接近零

这排除了"diversity 不够所以信号选不出来"的替代解释。问题不在于 constrained decoding 限制了多样性，而在于 **consistency signals 本身无法区分好样本和坏样本**——即使有大量不同的输出可供选择。

---
