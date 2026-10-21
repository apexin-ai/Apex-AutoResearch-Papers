# ops check progress and prepare

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_progress_and_prepare_20260518T104000_result.json`
- **Structured JSON:** [`8d32804d0d5b819e9c6b.json`](../../sessions/8d/8d32804d0d5b819e9c6b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度报告

### GPT-2m v4 (`gpt2m_wiki_a100_s42`)
- **当前状态**: gen 10/10 训练中（最后一代）
- gen_9 checkpoint 于 18:26 保存，metrics 于 18:28 写入
- gen_10 目录已创建但为空，训练刚开始约 12 分钟
- GPU 0: 48% util, 55705 MiB / 97887 MiB
- 进程 PID 310465 自 09:25 运行，已跑 ~9h15m
- 前 10 代（baseline + gen 1-9）耗时 ~9h，每代约 55 min
- **预计 gen_10 完成时间**: ~19:20-19:25（约 40-45 分钟后）
- `all_metrics.json` 尚未生成（完成后自动写入）

### intervention_reactive_s42 (`reactive_d1_s42`)
- **当前状态**: gen 0/10（baseline 评估中）
- 正在 "Featurizing q: 48%"，即 baseline 指标计算阶段
- GPU 1: 87% util, 12753 MiB / 97887 MiB
- 进程 PID 340969 自 18:26 运行，仅 ~14 分钟
- 模型为 Pythia-410m，预计每代比 GPT-2m 快
- **预计完成全部 10 代**: 约 5-7 小时后（~23:30-01:30）

---

GPT-2m 尚未完成，不执行分析。两个实验均正常运行中。

---
