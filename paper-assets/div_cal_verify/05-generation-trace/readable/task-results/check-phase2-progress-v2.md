# check phase2 progress v2

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_phase2_progress_v2_20260513T080421_result.json`
- **Structured JSON:** [`212af08c39c8e30c7274.json`](../../sessions/21/212af08c39c8e30c7274.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. Phase 2 主实验（PID 138667, cuda:1）
- **状态**: 运行中，已跑 4h23m
- **进度**: external_only 已完成 **gen_0 ~ gen_6**（7代目录），当前正在跑 **gen_5/7 的第3步 Training student**（日志显示 gen 5 在训练中）
  - 注：gen_0~gen_6 共7个目录，但 gen_5 的评估刚完成、gen_6 目录可能是提前创建的
- **总进度**: 7代中约完成5代，剩余约2代

### 2. seed=123 实验（PID 180459, cuda:0）
- **状态**: 运行中，已跑 32m34s
- **进度**: 正在跑 **gen_0/7 的第3步 Training student**，尚未产出任何完整代的结果目录
- **启动成功**: 是，日志正常

### 3. GPU 状态

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| cuda:0 | 70,857 / 97,887 MiB (72%) | 0% |
| cuda:1 | 21,687 / 97,887 MiB (22%) | 0% |

两卡利用率显示 0%，可能是采样瞬间在做数据加载/selection 而非 GPU 计算。cuda:0 显存占用较高（seed=123 实验），cuda:1 较低（主实验）。

---
