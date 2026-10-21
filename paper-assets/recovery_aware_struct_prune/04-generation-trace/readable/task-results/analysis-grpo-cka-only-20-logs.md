# analysis grpo cka only 20 logs

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_grpo_cka_only_20_logs_20260518T011915_result.json`
- **Structured JSON:** [`e87f90c37dbf4009a031.json`](../../sessions/e8/e87f90c37dbf4009a031.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件已写入。总结：

**grpo_cka_only_20** (CKA-guided pruning):
| Step | Reward | frac_zero_std | grad_norm |
|------|--------|---------------|-----------|
| 10   | 0.253  | 0.175         | 1.89      |
| 50   | **0.354** | **0.150**  | 1.98      |
| 70   | 0.308  | **0.125**     | 1.16      |
| 80   | **0.342** | 0.250      | 2.67      |
| 90   | 0.242  | 0.300         | 1.22      |

**grpo_random_20** (Random pruning):
| Step | Reward | frac_zero_std | grad_norm |
|------|--------|---------------|-----------|
| 10   | 0.161  | 0.300         | 3.75      |
| 50   | 0.175  | 0.300         | 4.75      |
| 70   | 0.190  | 0.300         | 7.09      |
| 90   | 0.173  | 0.325         | 7.53      |

**关键发现**:
- CKA-only 在 step 50-80 有明显学习（reward 0.31-0.35），但 step 90 回落到 0.24，frac_zero_std 升至 0.30
- Random 几乎没有学习（reward 始终 0.14-0.19），frac_zero_std 持续 0.30-0.40，grad_norm 极不稳定（3.5-8.6 vs CKA 的 1.0-3.8）
- CKA-only 的 step 70+ 下降趋势确认：peak 在 step 70-80，之后 reward 和 collapse 指标均恶化
- 当前进度：cka_only step 94, random step 97，均未完成

---
