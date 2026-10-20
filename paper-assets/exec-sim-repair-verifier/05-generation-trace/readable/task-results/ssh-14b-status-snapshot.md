# ssh 14b status snapshot

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_14b-status-snapshot_20260523T001130_result.json`
- **Structured JSON:** [`9fb35746d170a6f0f4f1.json`](../../sessions/9f/9fb35746d170a6f0f4f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 14B 训练全量快照 (2026-05-23 08:12 CST)

### GPU 占用

| GPU | 型号 | 显存 | 利用率 | 温度 | 功耗 | 进程 |
|-----|------|------|--------|------|------|------|
| 0 | RTX 5090 | 16,947 / 32,607 MiB (52%) | 69% | 68°C | 393W | **CLS 14B v2** (PID 215642) |
| 1 | RTX 5090 | 0 / 32,607 MiB | 0% | 32°C | 11W | 空闲 |
| 2 | RTX 5090 | 14,421 / 32,607 MiB (44%) | 67% | 65°C | 378W | **CWM 14B** (PID 211098) |
| 3 | RTX 5090 | 0 / 32,607 MiB | 0% | 34°C | 15W | 空闲 |

### 训练进度

| 任务 | PID | 已运行 | 进度 | 当前速度 | 剩余 | 预计完成 |
|------|-----|--------|------|----------|------|----------|
| **CWM 14B** | 211098 | 3h46m | **1348/1434 (94%)** | ~9.9s/step | ~86 steps ≈ 14 min | **~08:26 CST** |
| **CLS 14B v2** | 215642 | 2h35m | **889/1434 (62%)** | ~10.2s/step | ~545 steps ≈ 93 min | **~09:45 CST** |

### Eval 中间指标

| 任务 | Epoch | Eval Loss |
|------|-------|-----------|
| CWM 14B | 2.0 (step 956) | **0.0528** |
| CLS 14B v2 | 1.0 (step 478) | **0.0827** |

### Checkpoints

- **CWM 14B**: `checkpoint-478`, `checkpoint-956`
- **CLS 14B v2**: `checkpoint-478`

### Eval 结果

- CWM eval: **未生成**（训练未完成）
- CLS eval: **未生成**（训练未完成）

### Auto-eval 监控

两个监控脚本均已启动（06:41:48 CST），分别 watch CWM PID 211098 和 CLS PID 215642，训练结束后会自动触发 eval。

### 总结

CWM 14B 还剩约 14 分钟完成训练，CLS 14B v2 还剩约 1.5 小时。GPU 1 和 GPU 3 空闲。（tmux ls 被 read-only 模式拦截，如需查看请告知。）

---
