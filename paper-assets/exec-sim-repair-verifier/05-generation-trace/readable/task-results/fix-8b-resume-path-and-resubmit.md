# fix 8b resume path and resubmit

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_8b-resume-path-and-resubmit_20260514T174003_result.json`
- **Structured JSON:** [`c0ec3b07209754e04ec2.json`](../../sessions/c0/c0ec3b07209754e04ec2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 1. Checkpoint 子目录验证

| 实验 | 目标 checkpoint | 存在 | trainer_state.json | adapter_model.safetensors |
|------|----------------|------|-------------------|--------------------------|
| CWM 8B | checkpoint-1600 | ✓ | ✓ (9.9KB) | ✓ (58.5MB) |
| CLS 8B seed123 | checkpoint-3000 | ✓ | ✓ (14.6KB) | ✓ (58.5MB) |

两个 checkpoint 目录完整，包含 optimizer.pt、scheduler.pt、rng_state.pth 等全部 resume 所需文件。

### 2. 所有可用 checkpoint

**CWM 8B**: checkpoint-400, 900, 1000, 1100, 1200, 1300, 1400, 1500, **1600**

**CLS 8B seed123**: checkpoint-200, 1800, 2000, 2200, 2400, 2600, 2800, **3000**

### 3. GPU 状态

| GPU | 显存使用 | 利用率 |
|-----|---------|--------|
| 0 | 12999 / 32607 MiB | 85% |
| 1 | 12999 / 32607 MiB | 86% |
| **2** | **0 / 32607 MiB** | **0%** |
| **3** | **0 / 32607 MiB** | **0%** |

GPU 2/3 已清空，无残留进程。GPU 0/1 有其他任务在运行。

### 4. Tmux 清理

- `repo-level-cwm-8b-conda-v2` — 已杀掉
- `repo-level-cls-8b-seed123-conda-v2` — 不存在（之前已清理）
- 剩余 sessions: `ckpt_backup`, `eval_cwm_seed123`, `eval_cwm_v12`（非本次实验，保留）

---
