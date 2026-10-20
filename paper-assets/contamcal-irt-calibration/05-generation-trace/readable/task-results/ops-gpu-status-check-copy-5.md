# ops gpu status check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-check_20260516T040431_result.json`
- **Structured JSON:** [`eeb09ae11620c43cdb6d.json`](../../sessions/ee/eeb09ae11620c43cdb6d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态汇总

```
GPU 0: eval_3B_d025_v3_s42 (para_aligned) + signals_1.5B_d000_s123 | 96% | 13.4GB/24GB | PID 691033 + 691887 ⚠️ 双进程共享
GPU 1: eval_3B_d000_s42_a32 (aligned)      | 58% | 8.8GB/24GB  | PID 676497
GPU 2: eval_3B_d005_s42_a32 (aligned)      | 63% | 8.8GB/24GB  | PID 679190
GPU 3: eval_3B_d100_a32_s42_v3 (aligned)   | 64% | 8.8GB/24GB  | PID 687347
GPU 4: signals_3B_d100_a32_s123 (mmlu s4)  | 57% | 6.7GB/24GB  | PID 689315
GPU 5: signals_0.5B_d000_s123 (mmlu all)   | 32% | 2.3GB/24GB  | PID 687036
```

## Cron 追踪实验状态

| 实验 | PID | 状态 | GPU | 运行时间 | 进度 |
|------|-----|------|-----|---------|------|
| exp_001_eval_3B_d000_s42_a32_batch | 676487/676497 | ALIVE | cuda:1 | 2h01m | aligned eval 进行中（d005 之前启动，无进度条可见） |
| exp_001_eval_3B_d005_s42_a32_batch | 679180/679190 | ALIVE | cuda:2 | 1h48m | aligned eval 进行中（无进度条可见） |
| exp_001_eval_3B_d025_s42_a32_para | 691033 | ALIVE | cuda:0 | 25m | para_aligned GSM8K 59%（aligned 已完成） |
| exp_001_eval_3B_d100_s42_a32_batch | 687347 | ALIVE | cuda:3 | 59m | aligned GSM8K 32% (420/1319) |
| exp_002_signals_3B_d100_s123_v9 | 689315 | ALIVE | cuda:4 | 39m | mmlu s4 信号计算中 |
| exp_002_signals_05B_s123_v2 | 687036 | ALIVE | cuda:5 | 1h00m | mmlu self-critique 86% (chunk [5000:6000]) |

另外发现：**exp_002_signals_15B_s123_batch** (PID 691887) 在 cuda:0 上运行 1.5B d000_s123 mmlu all 信号计算，与 eval d025 para 共享 GPU 0。两者合计显存 13.4GB 尚在容量内，但 GPU 0 利用率最高 (96%)。

## 最近完成的结果目录

**eval_results（新增/更新）：**
- `Qwen2.5-3B_d100_a32_s123_para_aligned` — 11:08 完成（有结果文件）
- `Qwen2.5-3B_d025_v3_s42_aligned` — 10:33 完成（aligned eval 已出结果）
- `Qwen2.5-3B_d100_a32_s123_aligned` — 10:20 完成
- `Qwen2.5-1.5B_d100_s123_para_aligned` — 06:51 完成
- `Qwen2.5-3B_d005_s123_gsm8k_rerun` — 06:50 完成
- `Qwen2.5-1.5B_d025_s123_para_aligned` — 06:11 完成

**signals（新增/更新）：**
- `Qwen2.5-1.5B_d000_s123` — 11:56 更新（正在写入）
- `Qwen2.5-3B_d100_a32_s123` — 11:25 有结果
- `Qwen2.5-3B_d025_s123` — 11:25 有结果
- `Qwen2.5-0.5B_d000_s123` — 11:13 有结果
- `Qwen2.5-3B_d025_v3_s42` — 10:58 完成

---
