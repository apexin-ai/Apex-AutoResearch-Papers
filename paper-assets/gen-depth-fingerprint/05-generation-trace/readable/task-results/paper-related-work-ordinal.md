# paper related work ordinal

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_related-work-ordinal_20260515T225312_result.json`
- **Structured JSON:** [`c53f832f6545861a0261.json`](../../sessions/c5/c53f832f6545861a0261.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have a complete picture. Here's my report:

---

## Task 1: related_work.tex CI width 检查

**无残留问题。** related_work.tex 中不存在任何 `CI width`、`CI` 或 `[x, y]` 格式的置信区间引用。

唯一涉及数值范围的是第 14 行：
> "binary F1 from 0.52 to 0.71 across individual baselines"

验证：对照 results.tex Table 2 (tab:baselines) 中四个 individual baseline 的 binary F1：
- Binoculars: 0.524 → 0.52 ✓
- FastDetectGPT: 0.616
- LD-Score: 0.701
- Avg-LogProb: 0.712 → 0.71 ✓

范围 0.52–0.71 与表格数据一致。

---

## Task 2: P1-E ordinal baseline 结论

### Registry 数据源

有三个相关实验：

| 实验 | 数据集 | 角色 |
|------|--------|------|
| `plan-015` | 5-gen (23032 samples) | 原始 ordinal baseline，**已过时** |
| `plan-015-v2` | 同上 | bugfix + bootstrap CI，**已过时** |
| `review-p1e-ordinal` | 6-gen (27529 samples) | **当前权威**，ordinal regression 对比 |

### results.tex 数字一致性检查

**§4.3 Baseline comparison (Table 2)** — 数字来自 `review-exp-a-baseline-ensemble`（6-gen 统一评估）：

| 方法 | results.tex | registry | 状态 |
|------|------------|----------|------|
| 7-feature 3-class | 0.789 | 0.7887 | ✓ (四舍五入) |
| 4-detector ens. 3-class | 0.796 | 0.7964 | ✓ |
| 4-det + surface 3-class | 0.805 | 0.8049 | ✓ |

**Ordinal regression paragraph (lines 59-64)** — 数字来自 `review-p1e-ordinal`：

| 指标 | results.tex | registry | 状态 |
|------|------------|----------|------|
| XGBoost 3-class F1 | 0.789 | 0.7888 | ✓ |
| CORAL 3-class F1 | 0.771 | 0.7711 | ✓ |
| Frank-Hall 3-class F1 | 0.793 | 0.7931 | ✓ |
| XGBoost binary F1 | 0.721 | 0.7213 | ✓ |
| CORAL binary F1 | 0.728 | 0.7275 | ✓ |
| XGBoost concordance | 0.821 | 0.821 | ✓ |
| CORAL concordance | 0.810 | 0.810 | ✓ |
| Frank-Hall concordance | 0.825 | 0.825 | ✓ |

**所有数字与 registry 一致，无需修改。** Baseline comparison 和 ordinal regression 两个段落都已完整写入 results.tex，数据正确。

---
