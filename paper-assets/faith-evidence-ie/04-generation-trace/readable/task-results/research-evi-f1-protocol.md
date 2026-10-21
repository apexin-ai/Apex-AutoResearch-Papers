# research evi f1 protocol

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_evi_f1_protocol_20260515T131134_result.json`
- **Structured JSON:** [`d2bf81eecf7fe7268520.json`](../../sessions/d2/d2bf81eecf7fe7268520.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。两个评测协议存在**根本性差异**。

---

## 对比结论

### DREEAM 的 Evi-F1（`official_evaluate()`）

```python
# precision 分母: 所有预测 triple 的 evidence（含 FP triple）
pred_evi += len(evi)           # 在 if (title,r,h,t) in std 之外
# recall 分母: 所有 gold triple 的 evidence（含 FN triple）
tot_evidences += len(label['evidence'])  # 遍历所有 gold label
```

- **Precision** = 正确匹配的 evidence 数 / **所有预测 triple** 的 evidence 数
- **Recall** = 正确匹配的 evidence 数 / **所有 gold triple** 的 evidence 数

### 我们的 Evi-F1（`compute_evi_f1()`）

```python
if key not in gold_map:
    continue           # 直接跳过 FP triple

total_pred += len(pred_evi)   # 只计 TP triple 的 evidence
total_gold += len(gold_evi)   # 只计 TP triple 对应的 gold evidence
```

- **Precision** = 正确匹配的 evidence 数 / **TP triple** 的 evidence 数
- **Recall** = 正确匹配的 evidence 数 / **TP triple** 对应的 gold evidence 数

### 核心差异

| 维度 | DREEAM | 我们 |
|------|--------|------|
| FP triple 的 evidence | 计入 precision 分母（惩罚） | 跳过 |
| FN triple 的 gold evidence | 计入 recall 分母（惩罚） | 跳过 |
| 语义 | 关系抽取 + evidence 的**联合**质量 | 在正确关系上的 evidence **条件**质量 |
| 严格程度 | **远更严格** | 宽松 |

### 差距来源

假设关系 F1 约 60%（recall ~55%），那么：
- 我们的 recall 分母 ≈ DREEAM recall 分母的 55%，recall 会高很多
- 我们的 precision 分母不包含 FP triple 的 evidence，precision 也会高很多
- 从 57% → 82% 的差距完全可以解释

### 结论

1. **两者不是同一协议**，不能在论文中直接对比
2. DREEAM 的更严格，是 DocRED 社区标准协议
3. 我们的指标衡量的是"关系预测正确时 evidence 质量如何"——是个有意义的条件指标，但和 DREEAM 报告的不可比

### 对齐方案

在 `compute_evi_f1` 中加入两个改动即可对齐 DREEAM 协议：

1. **不跳过 FP triple**：FP triple 的 predicted evidence 全算入 `total_pred`（但不贡献 `total_tp`）
2. **Recall 分母改为全部 gold evidence**：遍历所有 gold 条目累加 evidence 数，而不是只看被匹配到的 gold triple

需要我实现对齐后的评测函数吗？

---
