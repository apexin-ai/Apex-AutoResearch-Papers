# analysis extract eval metrics 3B d000 s123 para

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_extract-eval-metrics-3B-d000-s123-para_20260515T045442_result.json`
- **Structured JSON:** [`c614c8ad02b86df838d7.json`](../../sessions/c6/c614c8ad02b86df838d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。汇总：

**Metrics（已写入 registry）**

| Benchmark | Score |
|-----------|-------|
| mmlu_para_accuracy | 0.6512 |
| gsm8k_para_accuracy | 0.1491 |
| arc_challenge_para_accuracy | 0.8121 |
| humaneval_para_pass@1 | 0.0385 |

**路径（已写入 registry）**
- checkpoint_path: `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s123/lora_adapter`
- log_path: `/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_para_aligned/eval_results.json`

**输出目录文件**

| 文件 | 大小 |
|------|------|
| eval_results.json | 878K |
| correctness_matrix.json | 47K |
| item_responses.json | 986K |

三个文件均存在。

---
