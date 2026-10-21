# ops gpu cleanup check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-cleanup-check_20260523T165649_result.json`
- **Structured JSON:** [`9d23f01c0ec755c748c1.json`](../../sessions/9d/9d23f01c0ec755c748c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 残留进程报告

### GPU 状态

| GPU | 显存占用 | GPU-Util | 温度 | 进程 |
|-----|---------|----------|------|------|
| cuda:0 | 17013 / 32607 MiB (52%) | 48% | 54°C | PID 278348 |
| cuda:1 | 17011 / 32607 MiB (52%) | 49% | 54°C | PID 278746 |
| cuda:2 | **0 / 32607 MiB (空闲)** | 0% | 31°C | 无 |
| cuda:3 | 26485 / 32607 MiB (81%) | 92% | 65°C | PID 272025 |

### 残留进程详情

| PID | GPU | 显存 | 运行时间 | 命令 |
|-----|-----|------|---------|------|
| 272025 | cuda:3 | 26476 MiB | **6h30m** | `eval_repo_cwm.py` — ckpt-6100 (conda), batch_size=8, test split |
| 278348 | cuda:0 | 17004 MiB | **5h37m** | `eval_repo_cwm.py` — s123/ckpt-300 reeval, batch_size=1 |
| 278746 | cuda:1 | 17002 MiB | **5h36m** | `eval_repo_cwm.py` — s456/ckpt-300 reeval, batch_size=1 |

所有进程工作目录均为 `/home/sonny/exec-sim-repair-verifier`，CPU 占用均 100%，说明仍在**活跃运行**中。

### tmux

有一个 `default` session 存在。

### 磁盘

| 挂载点 | 总容量 | 已用 | 可用 | 使用率 |
|--------|-------|------|------|--------|
| / | 30G | 22G | 8.5G | **72%** |

评估结果输出目录已产生约 20MB 数据。

### 结论

3 个进程全部是 `eval_repo_cwm.py` 评估任务，均在活跃运行（GPU-Util 48-92%），**不是残留僵尸进程**。cuda:2 空闲可用。

- 如果这些评估是你有意启动的 → 不需要清理，等它们跑完
- 如果不需要了 → 告诉我，我来 kill 对应 PID

---
