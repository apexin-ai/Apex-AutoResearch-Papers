# ops check seed2048 and ood progress

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_seed2048_and_ood_progress_20260522T032600_result.json`
- **Structured JSON:** [`75d81427a6895a7b47da.json`](../../sessions/75/75d81427a6895a7b47da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 1. seed 2048 训练（westd-47453）
- **进程 79754**: 存活，已运行 1h29m
- **进度**: **step 2/5 (40%)**，进度条显示 `2/5 [1:15:59<1:54:26]`
- **预计剩余**: ~1h54m（约每 step 38 分钟）
- **step 2 指标**: success=0.78%, pass@8=6.25%, KL=0.00077, entropy=0.021
- **GPU 使用**: GPU 2 和 3 各占用 ~44GB/98GB，GPU 0 和 1 空闲（符合预期）

### 2. seed5 OOD eval（bjb1-17606, PID 382718）
- **进程存活**: 运行 ~6 分钟
- **状态**: vLLM 模型加载完成（qwen_seed5_step10_hf），**尚未开始跑 task**（日志仅 46 行，全是 vLLM 初始化日志）
- **进度**: 0/134 tasks
- **checkpoint**: `/root/autodl-tmp/checkpoints/qwen_seed5_step10_hf`

### 3. seed6 OOD eval（bjb1-17606, PID 383485）
- **进程存活**: 运行 ~5 分钟
- **状态**: 同上，vLLM 模型加载完成（qwen_seed6_step15_hf），**尚未开始跑 task**
- **进度**: 0/134 tasks
- **checkpoint**: `/root/autodl-tmp/checkpoints/qwen_seed6_step15_hf`

### 4. GPU 使用

| 服务器 | GPU | 显存占用 | 利用率 |
|--------|-----|---------|--------|
| westd-47453 | 0 | 3/98GB | 0% |
| westd-47453 | 1 | 3/98GB | 0% |
| westd-47453 | **2** | **44.4/98GB** | 0% (idle between steps) |
| westd-47453 | **3** | **44.5/98GB** | 0% (idle between steps) |
| bjb1-17606 | **0** | **39.6/98GB** | 44% |
| bjb1-17606 | **1** | **39.6/98GB** | 54% |

两个 OOD eval 刚完成模型加载，马上要开始跑 134 个 task。根据之前经验，每个 task 大约需要几十秒，整体预计 1-2 小时完成。

---
