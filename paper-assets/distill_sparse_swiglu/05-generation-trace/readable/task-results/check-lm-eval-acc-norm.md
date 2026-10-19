# check lm eval acc norm

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_lm_eval_acc_norm_20260516T002800_result.json`
- **Structured JSON:** [`ad8675cb14b22835e704.json`](../../sessions/ad/ad8675cb14b22835e704.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data. Here's the full report:

## acc_norm 检查

**KL sparse (plan_007/results_full.json) — 已有完整 acc_norm：**

| Task | acc | acc_norm | 报告值 |
|------|-----|----------|--------|
| arc_challenge | 0.3473 | **0.3771** | 0.3771 = acc_norm |
| winogrande | 0.6156 | N/A (该任务无 acc_norm) | 0.6156 = acc |
| mmlu | 0.2591 | N/A (lm-eval MMLU 不输出 acc_norm) | 0.2591 = acc |
| gsm8k | 0.0121 | N/A (exact_match) | 0.0121 |

**Dense (results/lm_eval/results_full.json)：**

| Task | acc | acc_norm | 报告值 |
|------|-----|----------|--------|
| arc_challenge | 0.5478 | **0.5819** | 0.5819 = acc_norm |
| winogrande | 0.7814 | N/A | 0.7814 = acc |
| mmlu | 0.6532 | N/A | 0.6532 = acc |
| gsm8k | 0.5004 | N/A (exact_match) | 0.5004 |

**MMLU acc vs acc_norm**: lm-eval-harness 的 MMLU 任务不输出 acc_norm。0.2591 就是 raw acc，没有 acc_norm 可用。MMLU 是 4 选 1，随机基线 25%，KL sparse 的 0.2591 接近随机水平。

## 进程状态

**cuda:0 (39.6 GB / 97.9 GB = 40%):**
- PID 181121: Mistral dense lm-eval, gsm8k **25%** (329/1319), ~1.2s/it, 运行 23 min
- PID 184120: `debug_mask_verify.py`, 运行 2 min, 18.3 GB (新进程，你知道这个吗？)

**cuda:1 (74.2 GB / 97.9 GB = 76%):**
- PID 174850: Mistral KL lm-eval, gsm8k **56%** (745/1319), ~2.5s/it, 运行 54 min
- PID 179918: KL sparse rerun (`lm_eval_sparse.py`), 运行 36 min, 输出目录尚未创建, 仍在跑早期任务
- PID 182573, 182747: `diag_hflm.py` × 2, Sl 状态 (睡眠中), 各 18.3 GB, 运行 15 min
- OOM 风险: **无** (76%, 距 97.9GB 上限还有 23.7GB)

## 预估完成时间

- PID 181121 (Mistral dense gsm8k): ~**20 min** 剩余
- PID 174850 (Mistral KL gsm8k): ~**24 min** 剩余
- PID 179918 (KL sparse rerun): 未知进度，预计 **30-50 min**（之前完整跑完需 ~50 min）

## 关键结论

已有结果文件中 **acc_norm 已完整存在**（arc_challenge 有，winogrande/mmlu/gsm8k 本身不输出 acc_norm）。之前报告的 0.3771 和 0.5819 已经是 acc_norm，不是 raw acc。MMLU 0.2591 无法通过 acc_norm 提升——这就是 raw acc，接近随机猜测。

---
