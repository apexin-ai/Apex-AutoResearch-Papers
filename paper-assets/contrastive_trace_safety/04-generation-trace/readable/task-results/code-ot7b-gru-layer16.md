# code ot7b gru layer16

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ot7b_gru_layer16_20260517T110235_result.json`
- **Structured JSON:** [`a3d7e263a27e8d4c28a4.json`](../../sessions/a3/a3d7e263a27e8d4c28a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果：

**OT-7B GRU (Layer 16) — 3 seeds mean ± std:**

| Config | bal_acc | coverage | lead_mean | pre_cp_fpr |
|--------|---------|----------|-----------|------------|
| GRU Single (L16) | 0.7246 ± 0.0094 | 66.7% ± 4.4% | 35.25 ± 3.35 | 0.2904 ± 0.0527 |
| GRU Multi (L13-19) | 0.7464 ± 0.0127 | 64.5% ± 7.0% | 33.61 ± 4.83 | 0.2741 ± 0.0612 |

**与其他模型对比:**

| Model | Single bal_acc | Single coverage | Single lead | Multi bal_acc | Multi coverage | Multi lead |
|-------|---------------|----------------|-------------|---------------|----------------|------------|
| R1-32B | 0.675 | 30% | 9.1 | 0.655 | 23% | 8.8 |
| QwQ-32B | 0.694 | 75% | 19.3 | 0.724 | 84% | 15.9 |
| **OT-7B** | **0.725** | **66.7%** | **35.3** | **0.746** | **64.5%** | **33.6** |

OT-7B 的 bal_acc 和 lead_mean 均高于其他模型，但 pre_cp_fpr 也偏高（~0.29），说明在 CP 前有较多假阳性。

产出：
- 脚本: `/root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_ot7b_gru_layer16.py`
- 结果: `/root/autodl-tmp/contrastive_trace_safety/artifacts/ot7b_gru_layer16/results.json`

---
