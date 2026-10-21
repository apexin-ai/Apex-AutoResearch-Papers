# verify bjb1 gpu status

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_bjb1_gpu_status_20260525T225314_result.json`
- **Structured JSON:** [`216bb498201793c84d63.json`](../../sessions/21/216bb498201793c84d63.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### bjb1-45299

| GPU | 实验 | PID | 显存 | GPU利用率 | 运行时间 | 状态 |
|-----|------|-----|------|----------|---------|------|
| cuda:0 | exp_092_cheetah_no_dt_emb_s1 | 313538 | 1309 MiB | 4% | ~1分钟（06:52启动） | **正常运行** |
| cuda:1 | exp_093_cheetah_no_dt_emb_s2 | 313815 | 794 MiB | 1% | ~1分钟（06:52启动） | **正常运行** |

- 两个 tmux session 均存在（`exp_092_cheetah_no_dt_emb_s1`, `exp_093_cheetah_no_dt_emb_s2`）
- 两个 dreamer.py 进程存活，均刚启动约1分钟
- 日志显示两个实验均已完成 prefill (2500 steps)，模型已初始化（model_opt 16.9M params），到达 step 5000 开始首次 evaluation
- 无报错，仅有一条 FutureWarning（GradScaler API 弃用警告，不影响运行）

### westd-19154

| GPU | 显存 | GPU利用率 | 状态 |
|-----|------|----------|------|
| cuda:0 | 0 MiB | 0% | **空闲** |
| cuda:1 | 0 MiB | 0% | **空闲** |

- **exp_091_cheetah_008d_s2 已结束**，无任何 GPU 进程在运行
- 两张卡均完全空闲

---
