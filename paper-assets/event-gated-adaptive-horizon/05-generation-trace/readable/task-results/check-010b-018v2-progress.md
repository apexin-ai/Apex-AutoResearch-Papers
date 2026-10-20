# check 010b 018v2 progress

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_010b-018v2-progress_20260516T145940_result.json`
- **Structured JSON:** [`b7adf11d447767c250ee.json`](../../sessions/b7/b7adf11d447767c250ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

## 实验进度

| 实验 | PID | 运行时间 | 当前 step | 进度 | FPS | 最近 eval_return | ETA |
|------|-----|---------|-----------|------|-----|-----------------|-----|
| **010b** (cheetah_civo_trigger, cuda:0) | 585826 | 1h55m | 72,000 | 68.6% | 9.67 | 22.67 @65K | **~0.9h** |
| **018v2** (full_sgs_walker_s1, cuda:1) | 589564 | 1h05m | 36,000 | 34.3% | 9.40 | 208.34 @35K | **~2.0h** |

## 018v2 Gate 配置

`gate_dt_mean=2.0`, `gate_dt_2_frac=1.0`, `gate_empirical_entropy=0.0` — **gate_enabled 确认生效**，当前所有 step 均选择 dt=2。

## 010b 分析管线

- `analyze_010b.py` 存在（8017 bytes, 今天 21:38 更新）
- 在 conda base 环境下 **import 成功**，就绪可用
- 注意：必须在 conda 环境下运行（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`），系统 python 缺 numpy

---
