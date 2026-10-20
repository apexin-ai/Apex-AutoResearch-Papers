# infra c4 1b5 status check

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_c4-1b5-status-check_20260520T001634_result.json`
- **Structured JSON:** [`9d9c74b9ce7bc0f81669.json`](../../sessions/9d/9d9c74b9ce7bc0f81669.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。汇总：

## 结果

### 1. westd-42896: `exp_deberta_c4_1b5_pythia` (pythia_greedy) — **已完成 ✓**

| Pair | DeBERTa AUC | 95% CI | OBD Baseline | Δ |
|------|------------|--------|-------------|---|
| 0v1 | **0.9998** | [0.9996, 0.9999] | 0.9992 | +0.06pp |
| 1v2 | **0.9284** | [0.9230, 0.9331] | 0.8838 | **+4.5pp** |
| 2v3 | 0.5419 | [0.5354, 0.5486] | 0.5342 | +0.8pp |
| 3v4 | 0.5163 | [0.5090, 0.5237] | 0.5228 | -0.7pp |
| 4v5 | 0.5098 | [0.5037, 0.5160] | 0.5162 | -0.6pp |

**K\* = 2** (θ=0.6)，与 qwen_rw 一致。pythia_greedy 的 1v2 AUC 显著高于 qwen_rw (0.9284 vs 0.7052)，greedy decoding 产生的文本更容易区分，但 K* boundary 不变。

### 2. cqa1-22115: `exp_deberta_c4_1b5_qwen_cont` (qwen_cont256) — **进行中**

- **进度**: Fold 4/5 (最后一个fold), Epoch 3/3, step 600/1500
- **GPU**: GPU 0/1/3 均 ~98-99% 利用率
- **预计剩余**: ~3-5 分钟完成最后 900 steps + 评估

---
