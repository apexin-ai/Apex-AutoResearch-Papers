# analysis val truncation bias

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_val-truncation-bias_20260512T194316_result.json`
- **Structured JSON:** [`999981d20eeead1f873d.json`](../../sessions/99/999981d20eeead1f873d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果摘要

**截断与 label 高度显著相关**（Chi² = 213.27, p ≈ 0）。

### 核心数据

| | fail | pass | fail_rate |
|---|---|---|---|
| **截断** (n=1883) | 697 | 1186 | **37.0%** |
| **非截断** (n=7452) | 1555 | 5897 | **20.9%** |

fail 样本截断率 31.0%，pass 样本截断率 16.7%——**fail 样本被截断的概率是 pass 的 1.86 倍**。

### 根因

偏差主要由 mutation type 驱动，而非 label 本身：
- `mutation_operator_swap`: fail 79.6% 被截断，pass 0%（极端偏差）
- `mutation_off_by_one`: pass 58.0% 被截断，fail 12.4%（反向偏差）
- `mutation_boundary_removal`: 0% 截断（全部 < 2048 tokens）

fail 样本的 execution_output 通常包含详细 traceback，平均 token 长度更大（2092 vs 1645）。

### 对评估的影响

1. 截断后 target 不完整 → val loss **低估** fail 样本的真实预测难度
2. `mutation_operator_swap` 的 fail 评估基本不可信（几乎全被截断）
3. 整体 eval 指标会系统性偏乐观

详细报告：`artifacts/val_truncation_label_bias_analysis.md`

---
