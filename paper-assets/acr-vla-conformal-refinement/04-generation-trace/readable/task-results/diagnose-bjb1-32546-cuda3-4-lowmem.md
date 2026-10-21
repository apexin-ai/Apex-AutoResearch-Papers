# diagnose bjb1 32546 cuda3 4 lowmem

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_bjb1-32546-cuda3-4-lowmem_20260522T135648_result.json`
- **Structured JSON:** [`b347d12e4a909464f082.json`](../../sessions/b3/b347d12e4a909464f082.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### cuda:3 — Unified CRM r4 训练（`--input_mode obs_only`）：**正常运行中**
- PID 322367，启动于 19:51
- 当前进度：**epoch 5/50, batch 5000/6316**
- Loss ~0.011-0.019，正常收敛
- 每 epoch checkpoint 正常保存（已保存 epoch 1-4）
- 显存 542 MiB 是正常的——obs_dim=960, batch_size=32 的小 CRM 模型本身不需要多少显存，10% GPU util 也符合预期

### cuda:4 — **不是** π0.5 Goal/Long baseline，而是另一个 CRM 训练：**正常运行中**
- PID 326387，启动于 20:20
- 命令：`train_crm.py --benchmark object spatial goal long --obs_dim 960 --epochs 50 --batch_size 32`（无 `--input_mode obs_only`）
- 输出目录：`crm_unified_4suite/`（不是 r4）
- 当前进度：**epoch 4/50, batch 4700/6316**
- Loss 正常，checkpoint 已保存 epoch 1-3
- 显存 556 MiB 同理正常

### cuda:5 — **空闲**
- 2 MiB 显存，0% GPU util，无进程

### Goal/Long r4 baseline
- **没有在运行。** cuda:4-5 上没有 π0.5 eval 进程
- runs 目录下有历史 goal/long eval 日志（May 20），但没有 "r4" 相关的新 eval

### GPU 0-2 补充
- 正在跑 π0.5 ACR-VLA object eval（seed 42/43/44），每个 ~11.3GB 显存，从 09:05 开始运行约 13 小时，进程状态 `Rl`（活跃）

### 结论
**cuda:3-4 显存低不是异常**——CRM 模型很小，~500MB 显存是正常水平。两个训练都在稳步推进。问题是：cuda:4 上跑的是 CRM 训练而非预期的 π0.5 Goal/Long r4 baseline，cuda:5 完全空闲。Goal/Long r4 baseline 尚未启动。

---
