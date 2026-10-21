# train mf1 scrambled seed456

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_mf1-scrambled-seed456_20260518T091255_result.json`
- **Structured JSON:** [`5d1b3e4782984e46f8d3.json`](../../sessions/5d/5d1b3e4782984e46f8d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

MF1 任务完成。

**产出汇总：**

| 项目 | 路径/值 |
|---|---|
| Scrambled 数据 | `data/plan_002_splits/train_scrambled_seed456.jsonl` |
| DeBERTa checkpoint | `checkpoints/mf1_scrambled_seed456/deberta_multitask/best/` |
| GRU checkpoint | `checkpoints/mf1_scrambled_seed456/gru/best.pt` |
| 结果文件 | `results/mf1_scrambled_seed456.json` |

**关键指标 (seed=456 vs seed=42)：**

| Metric | seed=456 | seed=42 |
|---|---|---|
| DD OOD Full F1 | **1.000** | 0.990 |
| DD OOD K=1 F1 | **1.000** | 0.990 |
| DD OOD K=2 F1 | **1.000** | 0.944 |
| DD OOD K=3 F1 | 0.990 | 0.935 |
| DD OOD K=5 F1 | **1.000** | 0.990 |
| DeBERTa val P-acc | 0.698 | 0.679 |

seed=456 性能与 seed=42 一致甚至略优，确认 scrambled variant 跨 seed 稳定。Registry 已更新为 DONE/success。

---
