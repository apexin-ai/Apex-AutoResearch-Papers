# ssh diagnose 41312 eval qwen06b

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_diagnose_41312_eval_qwen06b_20260517T220623_result.json`
- **Structured JSON:** [`450e424dabd9bace59b9.json`](../../sessions/45/450e424dabd9bace59b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`qwen06b_uniform_seed42_v2` 已经完成评估。另外 `uniform_seed42` 只训练到 checkpoint-600（看起来不完整/是旧版本）。

---

## 诊断报告

### 1. GPU 状态

| GPU | 状态 | 显存占用 | GPU-Util | 进程 |
|-----|------|---------|----------|------|
| GPU 0 | **空闲** | 0 MiB / 97887 MiB | 0% | 无 |
| GPU 1 | **满载** | 46539 MiB | 100% | PID 133526 (ess_only_seed456_r2) |
| GPU 2 | **满载** | 46539 MiB | 100% | PID 133449 (ess_only_seed123_r2) |
| GPU 3 | **满载** | 46539 MiB | 100% | PID 136149 (random_reweight_seed456) |

机型：4x NVIDIA RTX PRO 6000 Blackwell (98GB each)

### 2. 进程存活状态

| 实验 | PID (查询) | 实际 GPU PID | 状态 | CPU | 运行时间 |
|------|-----------|-------------|------|-----|---------|
| ess_only_seed456_r2 | 133526 | 133526 | **存活，运行中** | 100% | ~66 min |
| ess_only_seed123_r2 | 133444 | 133449 (子进程) | **存活，运行中** | — | 133444 是 bash wrapper |
| random_reweight_seed456 | 136144 | 136149 (子进程) | **存活，运行中** | — | 136144 是 bash wrapper |

注意：PID 133444 和 136144 是 agent-ml 的 bash wrapper 进程，实际 Python 训练进程分别是 PID 133449 和 136149。

### 3. tmux sessions

```
ess_only_seed123_r2    (created 05:00)
ess_only_seed456_r2    (created 05:00)
random_reweight_seed456 (created 05:30)
```

三个训练 session 均存在。

### 4. eval_perplexity 结果

`qwen06b_uniform_seed42_v2` **已完成评估**，无需重跑：

| 模型 | Loss | Perplexity | 评估 Tokens |
|------|------|------------|------------|
| qwen06b_uniform_seed42_v2/final | 2.873 | **17.695** | 4,077,068 |

注：原始路径 `qwen06b_uniform_seed42` 不存在，实际模型目录名为 `qwen06b_uniform_seed42_v2`。另有一个 `uniform_seed42` 只训到 checkpoint-600（未完成）。

### 5. ess_only 日志尾部

**ess_only_seed456_r2**：进度 **72%** (4371/6103)，已运行 ~1h06m，预计剩余 ~1h01m，速度 2.10s/it。正常训练中。

**ess_only_seed123_r2**：进度 **63%** (3873/6103)，已运行 ~1h06m，预计剩余 ~1h19m，速度 2.12s/it。正常训练中。

**random_reweight_seed456**：进度 **33%** (2043/6103)，已运行 ~37m，预计剩余 ~2h22m，速度 2.10s/it。正常训练中。

三个实验均在正常训练，无异常。GPU 0 空闲可用。

---
