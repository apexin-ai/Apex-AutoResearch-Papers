# analysis c1 eval 30pct s456

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_c1_eval_30pct_s456_20260519T233548_result.json`
- **Structured JSON:** [`af14788cb3997052b26b.json`](../../sessions/af/af14788cb3997052b26b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## c1_eval_30pct_s456 结果

**状态**: 成功完成 (EXIT_CODE=0, 2145.7s)

### 指标

| Metric | c1_eval_30pct_s456 | eval_c1_retrain_s456 | eval_c1_retrain_s123 | c1_ablation_s42_v2 |
|---|---|---|---|---|
| wikitext2_ppl | **8.9773** | 8.82 | 8.84 | 9.4463 |
| arc_challenge_acc_norm | **0.4718** | 0.4471 | 0.4471 | 0.4027 |
| winogrande_acc | **0.6882** | 0.6993 | 0.6977 | 0.674 |
| mmlu_acc | **0.3656** | 0.4104 | 0.3992 | 0.4229 |
| gsm8k_exact_match | **0.0842** | 0.066 | 0.0682 | 0.0758 |

### 对比分析

与 retrain 对照组 (s456) 的差值：
- PPL: +0.16 (更差，符合预期)
- ARC: **+2.47pp** (更好，反常)
- WG: -1.11pp (更差，符合预期)
- MMLU: **-4.48pp** (显著更差)
- GSM8K: **+1.82pp** (更好，反常)

### 结论: **Mixed / Nuanced**

结果不一致。C1 ablation 在 PPL 和 WG 上符合预期（更差），但 ARC 和 GSM8K 反而更好，MMLU 下降幅度异常大（4.48pp）。这使得"C1 is causally important"的论点变得复杂——不能说 C1 均匀地提升所有指标。

**MMLU 的 0.3656 值得关注**——显著低于所有参考值（包括 s42 ablation 的 0.4229），可能是 seed-specific 的异常或 MMLU 评估波动。

### 路径

- Log: `~/runs/distill_sparse_swiglu/c1_eval_30pct_s456.log`
- Results JSON: `/root/distill_sparse_swiglu/results/benchmark/c1_eval_30pct_s456/results.json`
- Checkpoint used: `/root/distill_sparse_swiglu/checkpoints/c1_ablation_30pct_s456/predictor_bce_kl_targets.pt`
- No separate checkpoint directory at `~/checkpoints/distill_sparse_swiglu/`

### 异常

1. MMLU 0.3656 是所有同系列实验中最低的，与 s42 ablation (0.4229) 差距 5.73pp，可能存在评估问题
2. 日志中有 `fatal: not a git repository` 警告（无影响，只是 lm-eval-harness 的 git version tracking 报错）
3. 使用了离线模式加载 MMLU 数据集缓存（正常行为）

---
