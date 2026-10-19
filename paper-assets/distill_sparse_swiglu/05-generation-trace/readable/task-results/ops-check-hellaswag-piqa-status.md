# ops check hellaswag piqa status

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-hellaswag-piqa-status_20260519T002743_result.json`
- **Structured JSON:** [`6000813f9a905b50ee12.json`](../../sessions/60/6000813f9a905b50ee12.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

| # | 实验 | 服务器 | 状态 | hellaswag_acc_norm | piqa_acc_norm |
|---|------|--------|------|-------------------|---------------|
| 1 | kl30_uniform_hellaswag_piqa_v2 | westd-34887 GPU1 | **完成** | **0.7085** | **0.7481** |
| 2 | dense_baseline_hellaswag_piqa | westd-34887 GPU0 | **运行中** | — | — |
| 3 | kl50_global_hellaswag_piqa_v2 | westd-41718 GPU0 | **完成** | **0.5895** | **0.6948** |
| 4 | c1_ablation_30pct_s42_v2 | westd-41718 | **失败** | — | — |

### 详情

**实验 2 (dense_baseline)**: HellaSwag eval 的 loglikelihood 请求进度 ~3% (1337/40168)，速度 ~18.5 it/s，预计还需 ~35 分钟完成 hellaswag，之后还有 piqa。

**实验 4 (c1_ablation_30pct_s42_v2)**: 启动时 wandb login 失败 (`No API key configured`)，训练未开始，checkpoint 文件不存在。需要配置 wandb API key 后重新启动。

---
