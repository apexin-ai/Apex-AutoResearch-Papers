# diagnose gpu status check

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gpu_status_check_20260514T153536_result.json`
- **Structured JSON:** [`c42e15c77e11a5dee213.json`](../../sessions/c4/c42e15c77e11a5dee213.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器状态报告

### 1. GPU 实际使用情况

| GPU | 显存占用 | 利用率 | 进程 |
|-----|---------|--------|------|
| 0 | 26,863 / 97,887 MiB (27%) | 94% | PID 130124 — c2_n500_deepseek imp s015 (26.8GB) |
| 1 | 30,607 / 97,887 MiB (31%) | 77% | PID 130263 — c2_n500_deepseek rand s015 (30.6GB) |
| 2 | 48,068 / 97,887 MiB (49%) | 92% | PID 131864 — c2_qw_n500 imp s015 (27.8GB) **+** PID 142944 — c3_llama imp s020 (20.2GB) |
| 3 | 48,838 / 97,887 MiB (50%) | 96% | PID 132002 — c2_qw_n500 rand s015 (28.4GB) **+** PID 142708 — c3_llama rand s020 (20.4GB) |

### 2. 重复进程已清理

PID 132389, 132392 均已 DEAD。

### 3. c2_qw_n500 与 c3_llama 是否冲突

**不冲突，是共存。** 两个实验确实同时跑在 GPU 2 和 3 上，但 H20 有 98GB 显存，每张卡实际占用约 48-49GB（~50%），有充足余量。GPU 利用率 92-96%，运行正常。

注意：c3_llama 的旧子进程 PID 138408/138410（s015 阶段）已结束，被新子进程 142944/142708（s020 阶段）替代。

### 4. 实验进度

| 实验 | 条件 | 进度 | 状态 |
|------|------|------|------|
| c2_n500_deepseek | imp s015 | **205/500** (41%) | GPU 0 运行中 |
| c2_n500_deepseek | rand s015 | **226/500** (45%) | GPU 1 运行中 |
| c2_qw_n500 | imp s015 | **174/500** (35%) | GPU 2 运行中 |
| c2_qw_n500 | rand s015 | **178/500** (36%) | GPU 3 运行中 |
| c3_llama | imp s015 | **50/50** | **已完成** (PASS) |
| c3_llama | rand s015 | **50/50** | **已完成** |
| c3_llama | imp s020 | **~10/50** (20%) | GPU 2 运行中 |
| c3_llama | rand s020 | **~11/50** (22%) | GPU 3 运行中 |

c3_llama 总共 8 个条件（importance/random × 4 个 sparsity），已完成 2/8，当前跑第 3-4 个。

### 5. 异常发现

无异常。所有 6 个活跃进程运行正常，显存和 GPU 利用率在合理范围内。c2_n500（500 题/条件）比 c3_llama（50 题/条件）慢很多，预计还需数小时。

---
