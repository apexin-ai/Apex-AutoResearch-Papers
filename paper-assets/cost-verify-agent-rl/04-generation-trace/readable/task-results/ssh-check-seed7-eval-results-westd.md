# ssh check seed7 eval results westd

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_seed7_eval_results_westd_20260523T000727_result.json`
- **Structured JSON:** [`d63de9ecf6c813fcff55.json`](../../sessions/d6/d63de9ecf6c813fcff55.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 两个 eval 均 CRASH，无结果产出

| Eval | PID | 状态 | 错误 |
|------|-----|------|------|
| **step5** (cuda:2) | 217542 | **已死** | vLLM 初始化 OOM: `Free memory on device cuda:0 (45.1/94.97 GiB)` < 需要 80.73 GiB (gpu_memory_utilization=0.85) |
| **step7** (cuda:3) | 243894 | **已死** | `torch.AcceleratorError: CUDA error: out of memory` — device_mesh 初始化时 OOM |

两个 eval 都在 **初始化阶段** 就崩溃了，未进入 rollout，**没有产出任何 eval 指标**。

### GPU 当前状态

| GPU | 显存占用 | 利用率 |
|-----|----------|--------|
| 0 | 96687/97887 MiB | 100% |
| 1 | 96687/97887 MiB | 100% |
| **2** | **0 MiB** | **0%** — 已释放 |
| **3** | **0 MiB** | 100%（残留值，内存已释放） |

### 根因分析

- **step5**: 启动时 GPU 2 上只有 45.1 GiB 空闲（疑似有其他进程占用了约 50 GiB），vLLM 要求 0.85 × 95 GiB ≈ 80.7 GiB，不够。
- **step7**: 更底层的 OOM，`init_device_mesh` 阶段 CUDA 就分配失败了。

GPU 0/1 上的训练仍在正常运行。需要在 GPU 2/3 空闲的当前窗口重新提交这两个 eval。

---
