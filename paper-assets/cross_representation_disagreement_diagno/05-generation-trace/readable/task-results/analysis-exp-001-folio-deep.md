# analysis exp 001 folio deep

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_001_folio_deep_20260515T060551_result.json`
- **Structured JSON:** [`0c4e27e3ef3a2624811a.json`](../../sessions/0c/0c4e27e3ef3a2624811a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行完成。关键发现：

### Overall Metrics (All-mode, n=204)
| 指标 | 值 | 95% CI |
|------|-----|--------|
| C1 disagree_rate | 42.2% | [35.3%, 49.0%] |
| C2 diagnostic_rate | 88.4% | [81.3%, 94.7%] |
| C4 targeted-blind Δ | +4.7% | [-8.8%, +18.1%] |
| C5 localization_acc | 88.4% | [81.3%, 94.7%] |

### 关键发现

1. **错误类型分布**：logic_error 占 25.5%（52 例）为主导，negation_error 10.8%（22 例），exec_crash 和 unknown 各 5.4%

2. **GT 子集差异大**：
   - GT=False 的 C1 最高（47.6%），说明否定结论最容易引发分歧
   - GT=Unknown 的 C1 也很高（49.3%），且 C4 delta 最大（+14.7%），说明 Unknown 样本上 targeted repair 优势最明显
   - GT=True 的 C4 delta 为 **-13.6%**（targeted 反而不如 blind），这是反常的

3. **分歧不对称性**：FOL correct & Code wrong = 56 vs Code correct & FOL wrong = 10，比例 **5.6:1**。FOL 整体准确率 78.9% 远高于 Code 的 59.8%，证实 Code 端是主要错误来源

4. **Fisher exact test**：C4 差异在统计上 **不显著**（All-mode p=0.626, Excl-Unknown p=1.0），targeted vs blind 的优势需要更大样本量才能确认

5. **C2 和 C5 相等**（88.4%）：说明诊断率和定位准确率一致——凡是能诊断的，定位都是对的

---
