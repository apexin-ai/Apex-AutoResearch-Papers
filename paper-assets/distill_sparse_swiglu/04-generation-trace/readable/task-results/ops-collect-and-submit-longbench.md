# ops collect and submit longbench

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_collect-and-submit-longbench_20260516T125604_result.json`
- **Structured JSON:** [`bed6fd4f5ff2620d7168.json`](../../sessions/be/bed6fd4f5ff2620d7168.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

## Step 1 结果: Benchmark Metrics

| Metric | bench_kl50_uniform | bench_kl40_global |
|--------|-------------------|-------------------|
| wikitext2_ppl | 11.963 | 10.117 |
| arc_challenge_acc_norm | 0.3276 | 0.4096 |
| winogrande_acc | 0.6290 | 0.6535 |
| mmlu_acc | 0.2777 | 0.3806 |
| gsm8k_exact_match | 0.0212 | 0.0500 |

bench_kl40_global (40% sparsity, global_topk) 在所有指标上显著优于 bench_kl50_uniform (50% sparsity, uniform)，符合预期。

## Step 2: LongBench 已成功启动

| Job | GPU | PID | 状态 |
|-----|-----|-----|------|
| longbench_kl30_uniform | cuda:0 (41.7GB) | 233187 | RUNNING - 已通过calibration, 正在 generate |
| longbench_dense | cuda:1 (18.3GB) | 233330 | RUNNING - 数据集下载中/已开始 generate |

首次提交失败原因：服务器需要 `source /etc/network_turbo` 才能访问 HuggingFace（代理 + SSL 证书）。已修复并重启。预计 2-6 小时完成。

---
