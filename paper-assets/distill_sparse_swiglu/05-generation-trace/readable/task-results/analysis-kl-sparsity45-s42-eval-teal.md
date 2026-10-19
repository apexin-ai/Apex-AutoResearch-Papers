# analysis kl sparsity45 s42 eval teal

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_kl_sparsity45_s42_eval_teal_20260518T175635_result.json`
- **Structured JSON:** [`574c1654181702ee5154.json`](../../sessions/57/574c1654181702ee5154.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## kl_sparsity45_s42_eval_teal 实验报告

### Metrics

| 指标 | 数值 | 预期范围 | 状态 |
|------|------|---------|------|
| wikitext2_ppl | **10.803** | 10.5-11.5 | 正常 |
| arc_challenge_acc_norm | **0.3916** | ~0.397 | 正常 |
| winogrande_acc | **0.6464** | ~0.702 | 偏低 |
| mmlu_acc | **0.3037** | ~0.253 | 高于参考 |
| gsm8k_exact_match | **0.0296** | ~0.088 | 偏低 |
| actual_sparsity | **0.449** | 0.45 | 正常 |

### Per-layer Sparsity 分布
- 最低: Layer 0/18 (~0.29), 最高: Layer 29 (0.693)
- 模型级: 0.449, 符合 45% 目标

### 异常检查
- 5 个任务全部完成 (wikitext2 + 4 downstream)
- EXIT_CODE=0, 无 OOM/NaN
- 总耗时 ~2347s (~39min)

### 附加检查
- **kl_sparsity25_s42 checkpoint**: westd-34887 上 **不存在** (`/root/distill_sparse_swiglu/checkpoints/kl_sparsity25_s42/` 目录缺失)

### Registry
已更新为 DONE (success), metrics 和 checkpoint_path 已录入。

---
