# diagnose exp 001 sft 3B d100 s42 a32

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_001_sft_3B_d100_s42_a32_20260515T164221_result.json`
- **Structured JSON:** [`5c6fbbf771f52534f62b.json`](../../sessions/5c/5c6fbbf771f52534f62b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

v3 的日志名可能不同，PID 589763 直接在 GPU 5 运行中，从 ps 看到它是 `Qwen2.5-3B_d025_v3_s42` 训练。汇总如下：

## GPU 状态总览

| GPU | PID | 显存占用 | GPU利用率 | 实验 | 状态 |
|-----|-----|---------|----------|------|------|
| 0 | 594494 | 17960/24564 MiB | 66% | `exp_001_sft_3B_d100_s123_a32_v2` (train_sft, d100, seed=123) | ✅ 运行中, 130/4159 steps (~8min) |
| 1 | 593745 | 13316/24564 MiB | 31% | `exp_001_sft_3B_d100_s42_a32_v2` (train_sft, d100, seed=42) | ✅ 运行中, 180/4159 steps (~12min) |
| 2 | 580698 | 8976/24564 MiB | 64% | `exp_001_eval_3B_d005_s123_aligned` (evaluate, mmlu→GSM8K) | ✅ 运行中, GSM8K 671/1319 (51%), 运行 1h36m |
| 3 | 576735 | 8976/24564 MiB | 67% | `exp_001_eval_3B_d025_s123_aligned` (evaluate, mmlu→GSM8K) | ✅ 运行中, GSM8K 839/1319 (64%), 运行 1h51m |
| 4 | 590509 | 9658/24564 MiB | 91% | `compute_signals.py` (Qwen2.5-3B_d000_s42, mmlu, signal=all) | ✅ 运行中, 运行 29min |
| 5 | 589763 | 17640/24564 MiB | 5% | `exp_001_sft_d025_3B_v3` (train_sft, d025_v3, seed=42) | ✅ 运行中, 运行 30min |

## 关键结论

- **6 张 GPU 全满，无空闲 GPU**
- **所有 6 个进程健康运行中**，无报错、无挂起
- 两个 v2 SFT 重试（d100_s42 和 d100_s123）都在正常训练，总共 4159 steps，ETA 约 4.5 小时
- 两个 eval 实验都已完成 mmlu，正在跑 GSM8K，预计各还需 ~1 小时
- bitsandbytes 的 `libnvJitLink.so.13` 警告是非致命的，不影响训练/评估
- GPU 4 上跑的是 `compute_signals.py`（exp002 信号提取），不是 exp001 实验
- v3 日志文件名不是 `exp_001_sft_d025_3B_v3.log`，没有找到对应 3B 版本的日志（只找到 `exp_001_sft_d025_05B_v3.log`），但进程 589763 在 GPU 5 上正常运行

---
