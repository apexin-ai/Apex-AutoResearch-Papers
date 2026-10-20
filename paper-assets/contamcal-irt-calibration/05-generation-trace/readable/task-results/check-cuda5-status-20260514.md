# check cuda5 status 20260514

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_cuda5_status_20260514_20260514T172359_result.json`
- **Structured JSON:** [`5f98034e8529aa868638.json`](../../sessions/5f/5f98034e8529aa868638.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集。汇总如下：

---

## 1. exp_001_sft_3B_d000_v2 — **ALIVE (训练中)**

- **PID 405515**: 存活，已运行 1h08m，是 bash wrapper 进程
- **实际 GPU 进程**: PID 405520（子进程），在 cuda:5 上占用 **18650 MiB**，GPU util 40%
- **训练进度**: **988/3125 steps (31.6%)**，~3.9s/step，预计剩余 ~2h20m
- **训练指标**: loss ≈ 1.1, mean_token_accuracy ≈ 0.74, lr ≈ 4.6e-5 (cosine decay from 5e-5)
- **checkpoint**: `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter/` **目录存在但为空**（训练未到 save 点，正常）

## 2. exp_001_eval_05B_d025_aligned_v2 — **COMPLETED (成功)**

- **PID 406017**: 已退出，EXIT_CODE=0
- **结果文件**: eval_results.json, correctness_matrix.json, item_responses.json 均已保存

| Benchmark | Metric | Score |
|-----------|--------|-------|
| MMLU | accuracy | **0.2835** (1870/6596) |
| GSM8K | exact_match | **0.3114** (71/228) |
| ARC-Challenge | accuracy | **0.3199** (223/697) |
| HumanEval | pass@1 | **0.1923** (5/26) |

注：GSM8K 和 ARC 加载时遇到 HuggingFace 超时，但均 fallback 到缓存版本成功完成。

## 3. nvidia-smi 全卡状态

| GPU | 显存占用 | GPU Util | PID | 状态 |
|-----|---------|----------|-----|------|
| 0 | 14367/24564 MiB | 63% | 385407 | 活跃 |
| 1 | 5857/24564 MiB | 53% | 398887 | 活跃 |
| 2 | 8293/24564 MiB | 79% | 396024 | 活跃 |
| 3 | 0/24564 MiB | 0% | — | **空闲** |
| 4 | 0/24564 MiB | 0% | — | **空闲** |
| 5 | 18659/24564 MiB | 40% | 405520 | 活跃 (SFT 3B) |

**结论**: 之前观测到 cuda:5 空闲是暂时的（可能在 eval 和 SFT 之间的间隙）。当前 cuda:5 被 SFT 3B 训练占满。Eval 已完成释放 GPU。Registry 中 eval 实验应标记为 completed。

---
