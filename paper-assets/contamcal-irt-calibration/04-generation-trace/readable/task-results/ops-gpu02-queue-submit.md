# ops gpu02 queue submit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu02-queue-submit_20260514T072701_result.json`
- **Structured JSON:** [`146896faa1bc420a2518.json`](../../sessions/14/146896faa1bc420a2518.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

## 产出

### 1. 0.5B eval v5 metrics（已入 registry，DONE）

| Benchmark | d000 (baseline) | d100 (contaminated) | Delta |
|-----------|----------------|---------------------|-------|
| MMLU | 0.4049 | 0.2322 | -0.1727 |
| GSM8K | 0.3647 | 0.3571 | -0.0076 |
| ARC-C | 0.3780 | 0.2270 | -0.1510 |
| HumanEval | 0.1098 | 0.0854 | -0.0244 |

100% contamination 在 0.5B 上全面**降低**了分数，MMLU 和 ARC-C 降幅最大。这与预期的 score inflation 相反——0.5B 模型容量可能不足以"记住"答案，SFT 反而导致灾难性遗忘。

### 2. GPU 2: 0.5B d025 SFT v3 已提交
- exp_id: `exp_001_sft_d025_05B_v3`，PID 324153

### 3. GPU 0: 1.5B d100 SFT 确认完成 → eval 已提交
- `exp_001_sft_d100_15B_v2` → DONE/success（checkpoint 4159 steps, 73.9 MB adapter）
- `exp_001_eval_15B_d100_s42` → 运行中，PID 325300，parent = exp_001_sft_d100_15B_v2

### 4. Registry 更新
- `exp_001_eval_05B_d000_s42_v5`: DONE + metrics
- `exp_001_eval_05B_d100_v5`: DONE + metrics
- `exp_001_sft_d100_15B_v2`: DONE/success
- `exp_001_sft_d025_05B_v3`: QUEUED（运行中）
- `exp_001_eval_15B_d100_s42`: PREPARING（运行中）

---
