# analysis round2 metrics pull

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_round2_metrics_pull_20260517T142307_result.json`
- **Structured JSON:** [`70cb3182681b6d11e433.json`](../../sessions/70/70cb3182681b6d11e433.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已更新为 DONE (success)。完整 metrics 汇总：

### kl50_s456_global_eval (50% sparsity, seed 456, global allocation)

| Benchmark | Score |
|---|---|
| wikitext2 PPL | **11.81** |
| arc_challenge (acc_norm) | **33.19%** |
| winogrande | **64.88%** |
| MMLU | **27.94%** |
| GSM8K | **2.12%** |

### kl30_s456_global_eval (30% sparsity, seed 456, global allocation)

| Benchmark | Score |
|---|---|
| wikitext2 PPL | **8.93** |
| arc_challenge (acc_norm) | **46.33%** |
| winogrande | **71.11%** |
| MMLU | **43.82%** |
| GSM8K | **7.58%** |

Director 确认的 MMLU=43.82% 已验证正确。

备注：multiseed 训练日志显示训练后的 benchmark_eval.py 调用因 HuggingFace Hub 连接错误崩溃，但 `results/benchmark/` 下已有完整结果文件（时间戳 22:16-22:17），说明 eval 在之后被成功重跑过。

---
