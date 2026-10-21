# data effrank trajectories

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_effrank_trajectories_20260519T033526_result.json`
- **Structured JSON:** [`557adde85ff56eaf173f.json`](../../sessions/55/557adde85ff56eaf173f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

CSV 已写入 `artifacts/effrank_trajectories.csv`，包含 4 个实验配置（Pythia-410M/1.4B × α=0.50/1.00，均 s42）的 gen 0–10 effective_rank 轨迹。

关键观察：
- **gen 0 基线相同**：410M ≈ 46.6，1.4B ≈ 50.8（同架构同种子，符合预期）
- **α=0.50 轨迹收敛到平台**：410M 约 59–65，1.4B 约 82–83
- **α=1.00 轨迹更高且波动更大**：410M 约 89–101，1.4B 约 96–106
- 1.4B 在两种 α 下 effective_rank 均高于 410M，跨架构趋势一致

---
