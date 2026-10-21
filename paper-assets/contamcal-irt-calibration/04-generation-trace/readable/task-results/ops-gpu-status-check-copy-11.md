# ops gpu status check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-check_20260515T230104_result.json`
- **Structured JSON:** [`a4acce12b9a0186af71e.json`](../../sessions/a4/a4acce12b9a0186af71e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 使用状况报告

### 总览

| GPU | 显存占用 | 利用率 | 进程 |
|-----|---------|--------|------|
| **cuda:0** | **23,258 / 24,564 MiB (94.7%)** | **99%** | **⚠️ 双进程冲突** |
| cuda:1 | 13,341 / 24,564 MiB (54.3%) | 40% | d100 SFT v3 |
| **cuda:2** | **0 / 24,564 MiB (0%)** | **0%** | **✅ 空闲** |
| cuda:3 | 7,667 / 24,564 MiB (31.2%) | 64% | compute_signals |
| cuda:4 | 7,535 / 24,564 MiB (30.7%) | 55% | compute_signals (非 PID 623826) |
| cuda:5 | 18,665 / 24,564 MiB (76.0%) | 47% | d000 SFT |

### cuda:0 冲突详情（C001 违规）

两个进程共享 cuda:0，显存几乎打满：

| 进程 | PID | 显存 | 运行时间 | 任务 |
|------|-----|------|---------|------|
| eval batch | 642763 | 8,976 MiB | 1h25m | evaluate.py d100_a32_s123_aligned (GSM8K) |
| d005 SFT | 643167 | 14,268 MiB | 1h24m | train_sft.py d005_s42 |

- **合计 23,244 MiB，仅剩 ~1,320 MiB 空闲**
- GPU 利用率 99%，处于 OOM 边缘
- eval 正在跑 GSM8K 生成（变长序列），显存可能波动
- SFT 有 gradient accumulation (16步)，checkpoint save 时显存也会波动
- **随时可能 OOM kill**，建议立即迁移其中一个到 cuda:2

### cuda:2/3 空闲确认

- **cuda:2**：完全空闲，0 进程，0 显存 ✅
- **cuda:3**：**非空闲**，运行 compute_signals (PID 630891, d000_v2_s42, mmlu s4 signal)，已跑 2h39m

### cuda:4 进程

PID 623826 已不在。当前 cuda:4 上是 **PID 648627**（28分钟前启动），运行 compute_signals d100_s42 mmlu all signals，父进程 PID 623831。

### 训练进度汇总

| 任务 | GPU | 进度 | 速度 | 预计剩余 |
|------|-----|------|------|---------|
| d005 SFT | cuda:0 | 1094/3177 (34%) | ~4.6s/it | ~2h40m |
| eval batch (GSM8K阶段) | cuda:0 | 355/1319 (27%) | ~10.6s/it | ~2h50m (仅GSM8K，后续还有其他benchmark) |
| d100 SFT v3 | cuda:1 | 2428/4159 (58%) | ~4.4s/it | ~2h07m |
| d000 SFT | cuda:5 | 2231/3125 (71%) | ~3.9s/it | ~58m |
| signals d000_v2 (s4) | cuda:3 | 运行中 | - | 未知 |
| signals d100 (all) | cuda:4 | 运行中 28m | - | 未知 |

### PID 修正

用户提供的 PID 与实际不完全匹配：
- eval batch: 用户说 642752 → 实际 **642763**
- d005 SFT: 用户说 643162/643696 → 实际 **643167**
- cuda:4 signals: 用户说 623826 → 实际 **648627**（新进程）

### dmesg OOM 检查

ssh_read_only 不支持 dmesg 命令，无法检查 OOM kill 记录。需要 ssh_execute 才能执行。

---
