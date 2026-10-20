# analysis c2 non truncated sensitivity

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_c2_non_truncated_sensitivity_20260515T204650_result.json`
- **Structured JSON:** [`ce2335a78b69a606a4d8.json`](../../sessions/ce/ce2335a78b69a606a4d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总表如下：

## C2 Non-Truncated Sensitivity Analysis

**方法**：筛选 dense 和 sparse 两侧 gen_length 均 < 2048 的 problem，在此子集上重新计算 accuracy。

| Condition | n_total | n_non_trunc | Dense Acc (full) | Dense Acc (NT) | Sparse Acc (full) | Sparse Acc (NT) | Delta (full) | Delta (NT) |
|-----------|---------|-------------|-----------------|----------------|-------------------|-----------------|-------------|------------|
| DS s015   | 50      | 17          | 52.0%           | 94.1%          | 34.0%             | 64.7%           | -18.0pp     | -29.4pp    |
| DS s030   | 50      | 9           | 52.0%           | 100.0%         | 10.0%             | 44.4%           | -42.0pp     | -55.6pp    |
| QW s015   | 50      | 42          | 32.0%           | 38.1%          | 32.0%             | 38.1%           | +0.0pp      | +0.0pp     |
| QW s030   | 50      | 42          | 32.0%           | 38.1%          | 14.0%             | 16.7%           | -18.0pp     | -21.4pp    |

**截断率**：
- DS dense: 28/50 (56%), DS s015 sparse: 26/50 (52%), DS s030 sparse: 33/50 (66%)
- QW dense: 5/50 (10%), QW s015 sparse: 4/50 (8%), QW s030 sparse: 3/50 (6%)

**关键发现**：去除截断问题后，accuracy delta 在所有条件下**保持或放大**（非缩小），说明截断不是 sparse 降低 accuracy 的主因。DS 非截断子集很小（17/9 个），但 delta 从 -18pp/-42pp 扩大到 -29pp/-56pp。QW 截断率低（~10%），非截断子集几乎等于全集，delta 基本不变。

结果已保存至服务器 `/root/autodl-tmp/pacs/analysis_output/accuracy_eval_non_truncated_sensitivity.json`，artifact 已注册 (`art_20260515_2eb2a2`)。

---
