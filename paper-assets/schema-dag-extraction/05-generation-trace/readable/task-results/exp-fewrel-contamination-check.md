# exp fewrel contamination check

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_fewrel_contamination_check_20260516T120932_result.json`
- **Structured JSON:** [`accfcb3d5973032faff1.json`](../../sessions/ac/accfcb3d5973032faff1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果已保存至服务器和 artifact registry。

## 结果

| 指标 | Train-origin (64 rels) | Val-origin (16 rels) |
|------|----------------------|---------------------|
| Mean accuracy | 0.4831 | 0.5885 |
| Std | 0.2940 | 0.2879 |
| Median | 0.4167 | 0.6250 |

**统计检验：**
- Delta = **-0.1055 pp**（val 更高，方向与 contamination 假设相反）
- Mann-Whitney U = 416.0, **p = 0.2485**
- Welch t-test **p = 0.2168**
- Cohen's d = **-0.3602**（small-medium effect，方向仍是 val 更高）

**结论：** 无显著 contamination 证据。如果模型从 FewRel 训练集中"记住"了 train-origin relations，那么 train-origin 应该有更高的 accuracy。但实际结果相反——val-origin relations 的 accuracy 反而略高，且差异不显著（p > 0.2）。可直接用于 Reviewer W-W5 Q3 的 defense。

---
