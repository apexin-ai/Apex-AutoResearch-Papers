# analyze exp 001 eval 15B d100 s42

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_exp_001_eval_15B_d100_s42_20260514T101927_result.json`
- **Structured JSON:** [`55dcc6ead03e70ea41b7.json`](../../sessions/55/55dcc6ead03e70ea41b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_001_eval_15B_d100_s42 评估结果

### Benchmark Metrics

| Benchmark | Metric | Score | Correct/Total |
|-----------|--------|-------|---------------|
| **MMLU** | accuracy | **0.5933** | 8331/14042 |
| **GSM8K** | exact_match | **0.6497** | 857/1319 |
| **ARC-Challenge** | accuracy | **0.7688** | 901/1172 |
| **HumanEval** | pass@1 | **0.3049** | 50/164 |

### W&B Run ID
无。日志中未找到任何 wandb 相关内容。

### 异常
- **bitsandbytes 加载错误**（非致命）：`libnvJitLink.so.13: cannot open shared object file`。这是 bitsandbytes 的可选 CUDA JIT 库缺失，未影响评估运行。

### Checkpoint 路径
- Base model: `/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B`
- LoRA adapter: `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42/lora_adapter`

### 结果保存位置
- `/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s42/eval_results.json`
- `/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s42/correctness_matrix.json`
- `/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s42/item_responses.json`

### 最后 20 行确认
`EXIT_CODE=0`，正常退出。运行时间约 2h37m（15:39 → 18:16）。

---
