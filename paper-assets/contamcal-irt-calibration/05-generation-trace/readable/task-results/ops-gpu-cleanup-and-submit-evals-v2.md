# ops gpu cleanup and submit evals v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-cleanup-and-submit-evals-v2_20260515T063128_result.json`
- **Structured JSON:** [`e80cf1c2ed8c3141aba3.json`](../../sessions/e8/e80cf1c2ed8c3141aba3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部三步的工作已经由另一个 Worker 完成了。当前状态：

### Step 1: cuda:5 清理 — 无需操作
- PID 508118 和 508351 均已死亡
- 仅剩 PID 507968（compute_signals，2766 MiB，运行 1h），正常运行中

### Step 2: 3B d000 s42 eval v3 — 已在运行
- **PID 513826**，GPU 4，已运行 19 分钟
- `CUDA_VISIBLE_DEVICES=4` ✓（C004 合规）
- 输出目录：`/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_v3_aligned/`
- 命令参数正确：`--mc-format aligned`，adapter 路径指向 `Qwen2.5-3B_d000_s42/lora_adapter`

### Step 3: 0.5B d025 s123 eval aligned — 已在运行
- **PID 513900**，GPU 0，已运行 19 分钟
- `CUDA_VISIBLE_DEVICES=0` ✓（C004 合规）
- 输出目录：`/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d025_s123_aligned/`
- 命令参数正确：`--mc-format aligned`，adapter 路径指向 `Qwen2.5-0.5B_d025_s123/lora_adapter`

**不重复提交**（C001 约束）。两个 eval 均已正确启动，环境配置完整（conda base、HF_HOME、SSL 证书、tmux session）。

### 当前 GPU 总览

| GPU | 占用 | 任务 |
|-----|------|------|
| 0 | 3686 MiB | 0.5B d025 s123 eval (PID 513900) |
| 1 | 8976 MiB | 3B d000 s123 eval (PID 492660) |
| 2 | 8976 MiB | 3B d100 s123 eval (PID 506625) |
| 3 | 8976 MiB | 3B d025 eval (PID 503791) |
| 4 | 8976 MiB | 3B d000 s42 v3 eval (PID 513826) |
| 5 | 2766 MiB | exp_008 signals (PID 507968) |

---
