# check v7 progress 0513b

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_v7_progress_0513b_20260513T172524_result.json`
- **Structured JSON:** [`1571506b1ce11d6c2def.json`](../../sessions/15/1571506b1ce11d6c2def.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## v7 实验进度汇总

### 1. 状态：运行中 — G2 训练阶段

- 进程 PID 60104 存活，已运行 **14h50m**
- 当前：**G2 训练 249/305 steps (82%)**，loss=0.0575，lr=7.3e-7
- 最近 checkpoint：step 228，保存于 `2026-05-14 01:25`
- 预计剩余：~56 steps × ~2s/it ≈ **2 分钟**训练完成，之后进入 G2 eval
- G2 metrics 尚未生成（训练未完成）

### 2. G2 Metrics

尚不可用，训练完成后 eval 阶段才会生成 `metrics.jsonl`。

### 3. Sync 状态

| 文件 | 状态 |
|------|------|
| `analyze_ngram_leading.py` | 存在，但 **缺少 `same_checkpoint_tie` 修复** |
| `pilot_pipeline.py` | **缺少 `config.max_steps` 修复** |
| `launch_baseline_w0_p0.sh` | **不存在** |

**结论：服务器代码未同步最新修复。** v7 实验用的是旧代码。三个关键修改都未推送到服务器。训练本身即将完成（~2min），建议等 G2 eval 跑完拿到 metrics 后再决定是否需要基于新代码重跑。

---
