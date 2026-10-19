# analysis k2 eval final result

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_k2_eval_final_result_20260523T070835_result.json`
- **Structured JSON:** [`723b07e0414133f44c44.json`](../../sessions/72/723b07e0414133f44c44.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry更新完毕，cron已清除。

## K-curve 完整表格（30% sparsity, TEAL uniform）

| K | PPL | ARC-c | WG | MMLU | GSM8K | HS | PIQA |
|---|-----|-------|------|------|-------|----|------|
| 1 | 9.05 | 39.9 | 65.9 | 38.6 | 5.8 | — | — |
| **2** | **10.80** | **39.9** | **63.2** | **41.7** | **3.0** | **67.7** | **73.6** |
| 4 | 8.89 | 43.7 | 68.9 | 40.7 | 7.5 | — | — |
| 8 | 8.97 | 41.0 | 67.4 | 39.8 | 5.6 | 69.2 | 76.1 |
| 16 | 8.67 | 41.0 | 68.4 | 44.0 | 8.1 | 69.6 | 75.9 |
| 32 | 8.81 | 43.7 | 68.9 | 40.7 | 7.5 | — | — |

**K=2 观察**：
- PPL 10.80 是所有K中最高的，明显差于K=4（8.89）和K=1（9.05）
- 下游任务全面偏弱：ARC-c 39.9（平K=1）、WG 63.2（最低）、GSM8K 3.0（最低）
- MMLU 41.7 倒是不错，仅次于K=16（44.0）
- 整体趋势：K=2 是瓶颈点，predictor容量不足以有效学习per-layer模式，K>=4后快速改善

---
