# code sft 05B d025 submit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sft_05B_d025_submit_20260514T042522_result.json`
- **Structured JSON:** [`abef6171719ccc487bf5.json`](../../sessions/ab/abef6171719ccc487bf5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Tokenizing 进行中 (16%)。一切正常。

---

## 任务完成汇总

### eval_15B_d000_s123 结果（Qwen2.5-1.5B d000 s123）
| Benchmark | Metric | Score |
|-----------|--------|-------|
| MMLU | accuracy | **0.5762** (8091/14042) |
| GSM8K | exact_match | **0.6331** (835/1319) |
| ARC Challenge | accuracy | **0.7662** (898/1172) |
| HumanEval | pass@1 | **0.1707** (28/164) |

### d025 数据
- 已存在：`/root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl`
- 行数：54133（50000 + 25% × 16533 = 54133）✓

### 0.5B d025 SFT 训练
- **PID**: 291068（主进程），GPU 5 上 PID 290905/291074
- **GPU**: cuda:5，当前 710MiB（tokenizing 阶段，训练开始后会增长到 ~4-6GB）
- **日志**: `/root/runs/contamcal-irt-calibration/exp_001_sft_d025_05B.log`
- **输出**: `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s42`
- **预计完成**: ~53 分钟

---
