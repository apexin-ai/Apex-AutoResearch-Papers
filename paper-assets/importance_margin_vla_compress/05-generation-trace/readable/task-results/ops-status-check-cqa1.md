# ops status check cqa1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_status_check_cqa1_20260517T164417_result.json`
- **Structured JSON:** [`c0c4871e6554162a6459.json`](../../sessions/c0/c0c4871e6554162a6459.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### A. Geometric Prior Pruning

| 实验 | GPU | PID | 状态 | 进度 | SR |
|------|-----|-----|------|------|-----|
| k=0.5 | GPU 1 (5837MiB, 19%) | 236022 + 244012 | **ALIVE** (重复启动!) | Task 3 Ep 38/50 (~181/500) | 0% (Tasks 0-2 全部 0%) |
| k=0.7 | GPU 2 (3119MiB, 1%) | 222274 | **ALIVE** | Task 4 Ep 40/50 (~240/500) | 0% (Tasks 0-3 全部 0%) |
| k=0.9 | GPU 3 (3119MiB, 1%) | 225907 | **ALIVE** | Task 4 Ep 38/50 (~239/500) | 0% (Tasks 0-3 全部 0%) |

**问题**: GPU 1 上有两个 k=0.5 进程（PID 236022 elapsed 25min, PID 244012 elapsed 22min），可能是重复启动导致竞争。

已完成结果文件: 只有 `eval_geometric_prior_k09_dryrun.json`（dry run, 10 eps, SR=0%）。正式 50eps 的完整结果尚未产出。

### B. Pi0.5 Baseline (GPU 0)

| 实验 | GPU | 状态 | 进度 | SR |
|------|-----|------|------|-----|
| pi05 baseline | GPU 0 (3MiB, 0%) | **DEAD** | Task 0 完成后停止 (1/10 tasks) | 0% (T0: 0/50) |

Pi05 进程已不在 GPU 0 上。Log 在 00:41:14 结束（Task 0 完成后），nvidia-smi 时间 00:44:40，GPU 0 无任何 python 进程。推测 Task 1 启动时崩溃。

Log 路径: `/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_baseline.log`

### 关键发现

1. **所有 geometric prior 实验 SR=0%**，覆盖 k=0.5/0.7/0.9，已经 150-240 episodes 全部 FAIL，pruning 方式可能有根本性问题
2. **k=0.5 重复启动**需要 kill 一个，否则两个进程在同一 GPU 上竞争
3. **Pi05 baseline 已死**，需要重启

---
