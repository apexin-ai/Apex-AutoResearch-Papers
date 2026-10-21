# ops llama 5pct eval cohend

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_llama-5pct-eval-cohend_20260522T102531_result.json`
- **Structured JSON:** [`dd7fc2380f4ae4bf88de.json`](../../sessions/dd/dd7fc2380f4ae4bf88de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Here's the full summary:

---

## Llama 5% Contamination — Results

**训练**
- 1071/1071 steps (3 epochs), final loss = 1.236, avg train_loss = 1.439

**lz\* Person-Fit**
| | Free-θ | Fixed-θ (θ=-0.6661) |
|---|---|---|
| lz\* | **-4.954** | **-1.892** |

**Cohen's d**
| | d | 95% CI |
|---|---|---|
| Free-θ | **-5.53** | [-10.80, -4.05] |
| Fixed-θ | **-1.70** | [-3.87, -1.20] |

**Accuracy**
| Split | Acc |
|---|---|
| Overall | 63.42% |
| Seen (702 items) | **79.20%** |
| Unseen (13340 items) | 62.59% |

**Interpretation**: 即使只有 5% 污染（702 items），lz\* 在 free-θ 和 fixed-θ 两种设定下都显著偏离 clean 分布。Fixed-θ Cohen's d = -1.70 是一个大效应量，说明 5% 是 lz\* 方法可检测的下界以上。Seen 准确率 79.2% 显著高于 unseen 的 62.6%，验证了污染效果。

---
