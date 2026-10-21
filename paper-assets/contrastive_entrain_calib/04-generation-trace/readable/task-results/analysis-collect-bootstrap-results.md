# analysis collect bootstrap results

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_collect-bootstrap-results_20260522T124937_result.json`
- **Structured JSON:** [`aa8b9677e21e5528f904.json`](../../sessions/aa/aa8b9677e21e5528f904.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程仍在运行。脚本依次跑 Qwen3-8B 和 Llama-3-8B 两个模型，Qwen 已完成，Llama 的 full CV bootstrap 进行到 1000/2000（ETA ~5.5min）。

## 已完成结果

### Qwen3-8B
| 指标 | AUROC | 95% CI |
|------|-------|--------|
| **5-fold CV Mean** | 0.8269 | — |
| **Full CV bootstrap (n=2000)** | **0.8253** | **[0.7952, 0.8572]** |
| OOF | 0.7588 | [0.7251, 0.7958] |
| Per-strength: weak (n=75) | 0.6464 | [0.6060, 0.6978] |
| Per-strength: medium (n=54) | 0.8371 | [0.7850, 0.8933] |
| Per-strength: strong (n=52) | 0.8828 | [0.8262, 0.9401] |

Fold-level: [0.8188, 0.8056, 0.8565, 0.8619, 0.7917]

### Llama-3-8B（OOF/per-strength 已完成，full CV bootstrap 进行中）
| 指标 | AUROC | 95% CI |
|------|-------|--------|
| **5-fold CV Mean** | 0.7793 | — |
| OOF | 0.7745 | [0.7418, 0.8094] |
| Per-strength: weak (n=75) | 0.7028 | [0.6484, 0.7625] |
| Per-strength: medium (n=54) | 0.8594 | [0.8097, 0.9119] |
| Per-strength: strong (n=52) | 0.9079 | [0.8617, 0.9508] |

Fold-level: [0.7568, 0.7731, 0.7785, 0.8140, 0.7739]

Llama full CV bootstrap 按当前速率（~0.33s/iter）约 5-6 分钟完成。之前看到的 OOF AUROC = 0.7588 [0.7251, 0.7958] 是 Qwen 的最终值，已确认。需要等 Llama bootstrap 跑完才有全部最终结果。

---
