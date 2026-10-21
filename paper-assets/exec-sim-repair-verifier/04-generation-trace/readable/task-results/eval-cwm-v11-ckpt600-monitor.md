# eval cwm v11 ckpt600 monitor

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cwm-v11-ckpt600-monitor_20260513T174451_result.json`
- **Structured JSON:** [`85ed0c14b84f8e2a27e0.json`](../../sessions/85/85ed0c14b84f8e2a27e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## CWM v11 ckpt-600 Eval 状态

**PID 164045**: RUNNING (etime ≈ 10 min)

### tok1024 进度
- **进度**: 40 / 9784 = **0.41%**
- **Running accuracy**: 72.5%
- 推理开始: 01:35:35，40 条完成: 01:46:19（10 min 44 sec / 40 instances）
- 每 40 条 log 一次（`batch_size * 10 = 40`）
- **速率**: ~3.73 instances/min = 16.1 sec/instance
- **预估剩余时间**: (9784−40) / 3.73 ≈ **43.5 小时**
- 下一条进度 log（80/9784）预计约 01:57

### tok512 / tok256
- 目录已创建，均为空，尚未启动

### GPU 状态
| GPU | VRAM Used | Utilization |
|-----|-----------|-------------|
| 0 | 24.9 / 32.6 GB | 87% |
| 1 | 16.3 / 32.6 GB | 74% |
| 2 | 27.1 / 32.6 GB | **95%** ← eval 进程 |
| 3 | 25.8 / 32.6 GB | 57% |

### 关键问题

**tok1024 eval 预计需要 ~44 小时**。9784 条 × max_new_tokens=1024 × batch_size=4，在 sdpa（无 flash-attn）下每 batch ~64 秒。三组 eval（1024/512/256）全跑完可能需要 ~77 小时。

是否需要干预？可选方案：
1. 安装 flash-attn 提速（但需要重启 eval）
2. 加大 batch_size（当前 VRAM 有余量）
3. 接受长时间运行，让它跑着

---
