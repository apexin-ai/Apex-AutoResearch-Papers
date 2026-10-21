# ops monitor running experiments

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_monitor-running-experiments_20260515T091605_result.json`
- **Structured JSON:** [`eae64dceb3add4563fc5.json`](../../sessions/ea/eae64dceb3add4563fc5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态总结

| GPU | 实验 | 状态 | 进度 | 备注 |
|-----|------|------|------|------|
| **cuda:0** | exp_001_sft_15B_d025_s123_v3 | **运行中** | 612/3384 (**18%**), ~21min elapsed, ETA ~1h31m | 14.9GB VRAM, loss=1.20, token_acc=0.72, 正常 |
| **cuda:1** | exp_001_eval_05B_d000_s123_aligned | **运行中** | GSM8K 851/1319 (**65%**), 已跑 1h34m | 3.7GB VRAM, ETA ~40min 完成 GSM8K（之后还有 ARC/HumanEval） |
| **cuda:2** | exp_008_base_pretrained_eval_v2 (0.5B) | **运行中** | 已跑 31min, output dir 为空 | 3.6GB VRAM, 仍在跑第一个 benchmark，尚未写出结果 |
| **cuda:3** | exp_001_sft_15B_d005_s123_v4 | **运行中** | 465/3177 (**15%**), ~16min elapsed, ETA ~1h29m | 16.0GB VRAM, loss=1.28, token_acc=0.72, 正常 |
| **cuda:4** | exp_008_base_15B_eval_v2 + exp_001_eval_3B_d000_s42_v3 | **运行中** | 3B eval (PID 513826) 已跑 3h04m; 1.5B base eval (PID 530975) 已跑 31min | 14.7GB/100% GPU util, 3B eval 无 .done 仍在跑, 1.5B base output dir 为空 |
| **cuda:5** | exp_001_eval_15B_d000_s123_aligned | **运行中** | GSM8K 736/1319 (**56%**), 已跑 1h34m | 5.9GB VRAM, ETA ~1h05m 完成 GSM8K |
| **CPU** | exp_004_sim_sweep_extreme_gamma | **运行中** | seed 7 第 8/10 轮, 只产出 1 个结果文件 | 已跑 41min, 每轮 ~318s, 进度较慢 |

### 已完成的 eval（exp_001_eval_05B_d000_s42_v2）

该实验已有完整 eval_results.json，但注意**这是 base 0.5B（无 adapter）的结果**，且所有 pred 都是 "A"，疑似有问题：

| Benchmark | Score |
|-----------|-------|
| MMLU | 39.79% |
| GSM8K | 36.92% |
| ARC_Challenge | 46.93% |
| HumanEval pass@1 | 10.98% |

**异常提醒**：MMLU 前 30 条全部预测 "A"，强烈怀疑这个 eval 的 mc-format 或 prompt template 有问题——模型没有在正确做选择题，而是退化为总输出 "A"。建议后续复查该结果是否可信。

### 无异常
- 两个 SFT 训练 loss 曲线正常下降，lr warmup 正常
- 所有 PID 均存活
- 无 OOM 迹象

---
