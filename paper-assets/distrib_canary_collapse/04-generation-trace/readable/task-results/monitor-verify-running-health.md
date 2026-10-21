# monitor verify running health

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_verify-running-health_20260514T210900_result.json`
- **Structured JSON:** [`ececaec238409bc9f16b.json`](../../sessions/ec/ececaec238409bc9f16b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 健康度报告

### 实验 1: alpha_sweep_a000_s42 (PID 46721, cuda:0)
- **进度**: Gen 5/10 训练中（gen_0-4 已完成，gen_5 目录已创建但内容为空 = 正在训练）
- **运行时间**: 自 03:01 起，约 2h8m
- **训练速度**: ~15.85 it/s，每 gen 5000 步约 5m20s
- **最近 loss**: 3.1357（正常范围）
- **GPU**: 14.4 GB / 97.9 GB，46% 利用率，40°C
- **状态**: ✓ 健康

### 实验 2: alpha_sweep_a025_s42_v3 (PID 53074, cuda:1)
- **进度**: Gen 0 (baseline) 评估阶段，尚未开始训练
- **运行时间**: 自 05:04 起，仅 ~5 分钟
- **日志**: 139 行 / 20KB，全是 padding warning（正常——baseline 阶段做 generation 评估）
- **输出目录**: 仅有 config.json，无 gen_* 目录
- **GPU**: 7.4 GB / 97.9 GB，57% 利用率，45°C
- **状态**: ✓ 健康，刚启动不久

### 系统状态
- **进程**: 仅两个 python 训练进程，无 orphan
- **磁盘**: 75G / 250G (30%)，充裕
- **异常**: 无 Error/Traceback

两个实验均正常运行，无需干预。a025_s42_v3 启动较晚（05:04 vs 03:01），预计需要额外 ~2h 才能到达类似进度。

---
