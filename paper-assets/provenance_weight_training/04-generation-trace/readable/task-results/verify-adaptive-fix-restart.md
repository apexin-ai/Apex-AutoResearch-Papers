# verify adaptive fix restart

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_adaptive_fix_restart_20260514T174134_result.json`
- **Structured JSON:** [`4ed9a45c8117b6132748.json`](../../sessions/4e/4ed9a45c8117b6132748.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果：三组 adaptive_fix 全部失败

| 实验 | Exit Code | 退出时间 | 失败原因 |
|------|-----------|----------|----------|
| **seed42** | 143 (SIGTERM) | 17:44:05Z | 从 checkpoint-1500 恢复成功，训到 ~step 1506 后被外部 SIGTERM 杀死 |
| **seed123** | 1 | 17:42:40Z | 第一步训练就 crash，`lm_head` forward 报错 |
| **seed456** | 1 | 17:42:43Z | 同上，第一步 crash |

### Crash 详情（seed123/seed456）

Traceback 终止于：
```
File ".../transformers/models/qwen3/modeling_qwen3.py", line 494, in forward
    logits = self.lm_head(hidden_states[:, slice_indices, :])
```
实际异常信息丢失（日志文件因旧进程 fd 未关闭而变成 sparse file，错误信息被 null bytes 覆盖）。

**根因**：提交时 GPU 2/3 被旧的 `adaptive_seed123`（PID 109362）和 `adaptive_seed456`（PID 115071）占用，各用 75GB/98GB。新进程尝试在同一 GPU 上启动，第一步 forward 即失败（大概率 CUDA OOM 或设备冲突）。

### 当前 GPU 状态

| GPU | 进程 | 显存 |
|-----|------|------|
| 0 | PID 112475 (grid_b3_0_seed42) | 46514 MiB |
| 1 | 空 | - |
| 2 | 空 | - |
| 3 | 空 | - |

旧的 adaptive 进程（109362, 115071）和所有新 adaptive_fix 进程全部已死。**Checkpoint 目录完好**，三组 checkpoint 文件均在。GPU 1/2/3 现在空闲，可以重新提交。

---
