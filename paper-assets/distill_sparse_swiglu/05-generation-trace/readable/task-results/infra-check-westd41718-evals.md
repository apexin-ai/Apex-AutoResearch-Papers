# infra check westd41718 evals

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check_westd41718_evals_20260517T161032_result.json`
- **Structured JSON:** [`79b80eea796bbef88445.json`](../../sessions/79/79b80eea796bbef88445.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### 1. Downstream Extended Eval (cuda:0) — **已完成**

KL30 s42 (LLaMA-3.1-8B, global_topk, 30% sparsity) 扩展下游评测：

| Task | Metric | Score |
|------|--------|-------|
| HellaSwag | acc_norm | **0.7270** |
| HellaSwag | acc | 0.5270 |
| PIQA | acc_norm | **0.7595** |
| PIQA | acc | 0.7470 |
| BoolQ | acc | **0.7685** |

完成时间：2026-05-17 23:35:38，耗时 2053s (~34 min)。

---

### 2. Qwen-14B TEAL Baseline Eval (cuda:1) — **仍在运行**

- PID 6896, GPU 1 占用 61.6GB, 100% 利用率
- 命令：`--baseline_mode teal_vanilla --sparsity_target 0.3 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k`
- 当前进度：**23685 / 58702 loglikelihood requests (40%)**，这应该是 MMLU 阶段
- 速度：~75 it/s
- MMLU 剩余估计：~35000 items / 75 it/s ≈ **~8 min**
- MMLU 之后还要跑 GSM8K（generate_until 模式，14B 模型会比较慢）
- 预计总剩余时间：**~20-40 min**（取决于 GSM8K 生成速度）

---
