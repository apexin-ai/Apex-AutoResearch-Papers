# infra vram check cuda0

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_vram-check-cuda0_20260517T173355_result.json`
- **Structured JSON:** [`d59ac0bfb422b649820b.json`](../../sessions/d5/d59ac0bfb422b649820b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报结果：

## cuda:0 VRAM 使用量
- **exp_006 (PID 133204): ~19 GB / 98 GB**
- GPU 利用率 64%，温度 50°C，功耗 237W/600W

## exp_006 运行状态
- tmux session `exp_006` 存在，正常运行
- 日志显示正在执行 Generation 0 评估（computing effective rank / perplexity / distinct-4）
- 有 padding_side 警告但不影响运行

## cuda:1 情况
- **PID 116947: ~25 GB**，是 exp_005（`run_phase1.py --condition adaptive --k 20`）
- GPU 利用率 100%，温度 81°C，功耗 578W
- **PID 132207 已不存在**（进程已结束，可能是之前的短暂任务或已完成的实验）

## 双实例可行性判断
**可行。** exp_006 稳定 VRAM 约 19 GB，远低于 35 GB 阈值。cuda:0 剩余约 79 GB 空闲，在同一 GPU 上再启动 exp_004（同为 Pythia-410M）完全没问题，预计双实例总占用约 38 GB，仍有大量余量。

---
