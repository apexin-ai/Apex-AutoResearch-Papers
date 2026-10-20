# ops gpu status audit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-audit_20260514T121808_result.json`
- **Structured JSON:** [`3521016c88fd4f947f39.json`](../../sessions/35/3521016c88fd4f947f39.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 使用状态（cqa1-21977，2026-05-14 20:18）

| GPU | 显存占用 | GPU利用率 | PID | 实验 |
|-----|---------|----------|-----|------|
| **0** | 2240/24564 MiB | 33% | 353390 | **exp-002 signals**: `compute_signals.py` Qwen2.5-0.5B_d000_s42, benchmarks=mmlu, signals=embedding+minkpp+selfcritique |
| **1** | 5880/24564 MiB | 53% | 362352 | **exp-001 eval 1.5B aligned batch**: `evaluate.py` Qwen2.5-1.5B_d000_s42_para_aligned, benchmarks=mmlu+gsm8k+arc+humaneval |
| **2** | 3686/24564 MiB | 36% | 356787 | **exp-001 eval 0.5B aligned batch**: `evaluate.py` Qwen2.5-0.5B_d005_s42_aligned, benchmarks=mmlu+gsm8k+arc+humaneval |
| **3** | 8976/24564 MiB | 69% | 362942 | **exp-001 eval 3B**: `evaluate.py` Qwen2.5-3B_d100_s42_aligned, benchmarks=mmlu+gsm8k+arc+humaneval, batch=8 |
| **4** | 21818/24564 MiB | 38% | 335351 | **exp-001 train**: `train_sft.py` Qwen2.5-3B_d005_s42 (SFT LoRA 训练中) |
| **5** | 8976/24564 MiB | 72% | 342940 | **exp-001 eval 3B**: `evaluate.py` Qwen2.5-3B_d000_s42_aligned, benchmarks=mmlu+gsm8k+arc+humaneval, batch=4 |

**空闲 GPU：无。6 卡全部占用。**

### 关键实验状态

- **exp_001_eval_15B_aligned_batch** (GPU 1, PID 362352)：运行中，20:03 启动，正在评估 `Qwen2.5-1.5B_d000_s42_para_aligned`。产出目录刚创建（size=6，尚无结果文件）。
- **exp_001_eval_05B_aligned_batch** (GPU 2, PID 356787)：运行中，19:15 启动，正在评估 `Qwen2.5-0.5B_d005_s42_aligned`。产出目录同样刚创建（size=6）。
- **exp-002 signals** (GPU 0, PID 353390)：运行中，18:46 启动。已产出 `Qwen2.5-0.5B_d000_s42` 的 embedding (mmlu/gsm8k/arc_challenge) 和 minkpp (mmlu 进行中)，selfcritique 尚未开始。
- **3B 训练** (GPU 4, PID 335351)：d005 SFT 训练中，17:11 启动，已跑约 3 小时。
- **3B eval** (GPU 3+5)：d100 和 d000 的 aligned eval 分别在跑。

另外注意：PID 318424 (pts/3) 是 `Qwen2.5-0.5B_raw` eval 的僵尸进程（defunct），不占 GPU。

---
