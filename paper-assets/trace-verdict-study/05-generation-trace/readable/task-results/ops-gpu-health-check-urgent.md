# ops gpu health check urgent

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_health_check_urgent_20260520T145249_result.json`
- **Structured JSON:** [`f89f98fac995814d7e6e.json`](../../sessions/f8/f89f98fac995814d7e6e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 1. qwen15b_loop_only_seed456 — **已完成** ✓

- **PID 630189 / 630199**: 已退出（进程不存在），EXIT_CODE=0
- **阶段**: 训练 + eval 均已完成
- **Checkpoints**: checkpoint-148 → checkpoint-296 → checkpoint-444 → final (全部 444 步)
- **Eval 结果**:
  - Accuracy: **79.2%** (95% CI: [76.8%, 81.3%])
  - Majority baseline: 71.5%，Lift: +7.6pp
  - pass: P=0.85 R=0.86 F1=0.86
  - fail: P=0.64 R=0.62 F1=0.63
- **GPU 0**: 0% util, 49GB 占用（模型残留未释放）

### 2. deepseek_ae_only_seed123 — **训练中** 🔄

- **PID 626709**: 存活，运行 2h06m，状态 Ss+
- **PID 626719** (train_sft.py): 存活，运行 2h06m，状态 Sl
- **阶段**: 训练中，step **381/444** (86%)
- **速度**: ~18-19s/it
- **最新 checkpoint**: checkpoint-296 (22:26)，checkpoint-148 (21:36)
- **预估剩余**: ~63 steps × 19s ≈ **20 分钟**完成训练，之后进入 eval
- **GPU 1**: 100% util, 22GB/98GB

---
