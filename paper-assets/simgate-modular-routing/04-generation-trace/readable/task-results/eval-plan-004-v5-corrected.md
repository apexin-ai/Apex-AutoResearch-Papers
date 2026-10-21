# eval plan 004 v5 corrected

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan-004-v5-corrected_20260516T000126_result.json`
- **Structured JSON:** [`1397f87c45feca5a6b02.json`](../../sessions/13/1397f87c45feca5a6b02.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果对比：

### plan-004-v5 Corrected Eval 结果

| 指标 | 旧值 (错误 split, n=300) | 新值 (corrected split, n=305) |
|------|--------------------------|-------------------------------|
| **Balanced Accuracy** | 0.4148 | **0.7533** |
| n_val | 300 | 305 |

### Corrected 详细指标

| 指标 | 值 |
|------|-----|
| Accuracy | 68.8% |
| **Balanced Accuracy** | **75.3%** |
| Internal Recall | 83.3% |
| Internal Precision | 21.7% |
| Det Recall | 67.3% |
| Det Precision | 97.4% |

### Confusion Matrix (rows=true, cols=pred)

|  | pred det | pred int |
|--|----------|----------|
| **true det** | 185 | 90 |
| **true int** | 5 | 25 |

GT 分布: det=275, int=30 | Pred 分布: det=190, int=115

### 分析

旧 balanced_acc=0.4148 → 新 balanced_acc=0.7533，**差异巨大 (+0.3385)**。旧 eval 用了与训练不匹配的 sklearn episode-level split（n_val=300），导致 train/val 数据重叠（contamination）或分布偏移，产出了严重失真的低分。

Corrected eval 使用训练代码的 exact split function（per-task_type step-level stratified, seed=42），val set 与训练集无重叠。模型实际表现远好于之前报告的数字。

模型特点：internal recall 高（83.3%，30 个中找到 25 个），但 internal precision 低（21.7%），说明模型倾向于过度预测 internal（115 个 pred vs 30 个 GT），将大量 deterministic 误判为 internal。

---
