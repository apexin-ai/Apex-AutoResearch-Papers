# data group selection comparison

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_group_selection_comparison_20260516T105543_result.json`
- **Structured JSON:** [`4367c0cab495c422c1c4.json`](../../sessions/43/4367c0cab495c422c1c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出完成。三种方法各剪 200/784 groups，总量一致，但 per-layer 分布差异明显：

**关键发现：**

| 特征 | 说明 |
|------|------|
| **Layer 0-5** | 三者一致，都最大幅剪枝（12/28 groups） |
| **Layer 6** | RASP 也剪到 12，Standard/RLVR 保留全部 28 — RASP 对浅层更激进 |
| **Layer 27 (最后层)** | RASP 剪到 12，Standard/RLVR 保留全部 28 — RASP 对首尾层均不保守 |
| **Layer 16-22 (中后段)** | RASP 基本保留全部，Standard/RLVR 在此区间集中剪枝 |
| **RLVR vs Standard** | 极其相似，仅 Layer 16/20/21 有微小差异（±1~2 groups） |
| **RASP vs Standard** | 分布差异大 — RASP 把预算从浅层/末层转移到了中后段 |

**产出文件：**
- JSON: `/root/autodl-tmp/recovery_aware_struct_prune/results/group_selection_comparison.json`
- CSV: `/root/autodl-tmp/recovery_aware_struct_prune/results/group_selection_comparison.csv`
- 脚本: `/root/recovery_aware_struct_prune/src/extract_pruning_pattern.py`

---
