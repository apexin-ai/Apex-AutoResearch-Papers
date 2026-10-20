# paper appendix task b1

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_appendix-task-b1_20260515T195419_result.json`
- **Structured JSON:** [`6346db5c09fcad784396.json`](../../sessions/63/6346db5c09fcad784396.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出汇总：

**创建的文件：**
- `docs/paper/sections/appendix.tex` — 完整 appendix section，包含：
  - **Table A.1** (tab:nve_raw)：8 个实验的 NVE 值 + B1/B2 ground truth 标签
  - **Table A.2** (tab:sensitivity_b1)：Task B1 六阈值灵敏度分析（AUROC=1.000，n_pos=2）
  - **Table A.3** (tab:sensitivity_b2)：Task B2 六阈值灵敏度分析（AUROC=0.933，n_pos=3）
  - 阈值推荐理由（1.5x 在 B2 中 F1=85.7% 最优，100% recall）
  - Limitations 段落（n=8，CI 宽，proof-of-concept 定位）

**更新的文件：**
- `docs/paper/main.tex` — 添加 `\input{sections/appendix}`
- `paper/tables/nve_sensitivity_table.tex` — 更新为与 appendix 一致的紧凑摘要表

**关键数值：** B1 在阈值 ≥3.9x 达到 8/8 完美分类（min_pos=4.13 > max_neg=3.78）。所有 CI 均为双侧 Clopper-Pearson (α=0.05)。1.2x/1.5x 和 1.7x/2.0x 分别为相同 operating point（区间内无 NVE 值），已在表注中说明。

---
