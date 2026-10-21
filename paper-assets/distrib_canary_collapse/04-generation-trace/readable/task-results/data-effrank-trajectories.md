# data effrank trajectories

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_effrank_trajectories_20260519T031353_result.json`
- **Structured JSON:** [`18a7d608b485f984fa75.json`](../../sessions/18/18a7d608b485f984fa75.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `artifacts/effrank_trajectories.csv`。

数据来源：
- `pythia410m_a050_s42` ← `results/alpha_sweep/a050_s42/all_metrics.json`
- `pythia14b_a050_s42` ← `results/scale_check/pythia14b_a050_s42/all_metrics.json`
- `pythia410m_a100_s42` ← `results/generalize/pythia410m_wiki_a100_s42/all_metrics.json`

三个实验均有 gen 0-10 共 11 代完整的 `effective_rank` 字段，无缺失。数值保留 4 位小数。

---
