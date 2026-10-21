# analysis qwen14b kl30 s42 gsm8k v2

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen14b_kl30_s42_gsm8k_v2_20260519T225148_result.json`
- **Structured JSON:** [`d6085ccba615a56c1c91.json`](../../sessions/d6/d6085ccba615a56c1c91.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

注册表已更新完毕。

## 实验结果：qwen14b_kl30_s42_gsm8k_v2

### Metrics
| 指标 | 值 |
|------|-----|
| gsm8k_exact_match (flexible) | **0.3571** |
| gsm8k_exact_match (strict) | 0.3541 |
| stderr | ±0.0132 |
| actual_sparsity | 0.296 |
| sample_len | 1319 |
| 运行时间 | ~4.5h, EXIT_CODE=0, 无 OOM/NaN |

### 与 s123 一致性
| Seed | GSM8K exact_match | Sparsity |
|------|-------------------|----------|
| s42 | 0.3571 | 0.296 |
| s123 | 0.3442 | 0.297 |
| **差值** | **+1.29pp** | — |

差值在 stderr (~1.3pp) 范围内，**两个 seed 一致**。

### 与 baseline 对比
| 配置 | GSM8K | vs Dense retention |
|------|-------|-------------------|
| Qwen-14B Dense | 0.8757 | 100% |
| **KL 30% s42** | **0.3571** | **40.8%** |
| KL 30% s123 | 0.3442 | 39.3% |
| TEAL 27.5% uniform | 0.5709 | 65.2% |
| 8B Dense | 0.4875 | — |
| 8B TEAL 30% uniform | 0.0879 | — |

### 结论：**success**

实验正常完成，结果与 s123 一致。但 GSM8K 上 KL 30% 的 retention 较低（~40%），且显著弱于 TEAL 27.5%（0.5709）。这与其他 5 个任务上 KL 优于或持平 TEAL 的趋势相反——GSM8K 是 KL predictor 的弱势任务。

---
