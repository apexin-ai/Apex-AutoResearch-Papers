# ssh controlb check and collect

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_controlb-check-and-collect_20260515T141343_result.json`
- **Structured JSON:** [`27b9d9ab01d09420e97d.json`](../../sessions/27/27b9d9ab01d09420e97d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Control B 实验结果

**状态：两个实验均已完成。** 服务器上无 Python 进程。

### 核心结果

| 条件 | best per_task_mean_ρ | best layer | best pooled ρ |
|------|---------------------|------------|---------------|
| **trained_label_perm** (trained features + shuffled labels) | **0.0125** | 8 | 0.0123 |
| **untrained_label_perm** (untrained features + shuffled labels) | **0.0093** | 1 | 0.0085 |

### 与正常实验对比

| 条件 | ρ |
|------|---|
| trained (正常标签) | **0.955** |
| untrained (正常标签) | **0.933** |
| trained_label_perm (shuffled) | 0.013 |
| untrained_label_perm (shuffled) | 0.009 |

### 逐层分布

- **trained_label_perm**：所有 33 层 per_task_mean_ρ 在 [-0.009, +0.013] 之间波动，R² 全部为负值，大量层 ρ=0.0
- **untrained_label_perm**：更极端——33 层中 20 层 ρ 恰好 = 0.0，最大绝对值仅 0.006，R² 基本为 0

### 结论

Null control 完全符合预期：**shuffled labels 下 ρ ≈ 0**。Probe 无法从随机标签中学到任何有意义的映射。正常实验中 trained ρ=0.955 / untrained ρ=0.933 的高相关性确实来自 features 中编码的 temporal distance 信息，而非 probe 过拟合或数据泄漏。

### 结果文件路径
- `/root/autodl-tmp/vla-ssd/results/trained_label_perm/temporal_distance/summary.json`
- `/root/autodl-tmp/vla-ssd/results/untrained_label_perm/temporal_distance/summary.json`

---
