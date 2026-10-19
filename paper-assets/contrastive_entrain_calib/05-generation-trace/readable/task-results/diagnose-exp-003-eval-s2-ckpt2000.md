# diagnose exp 003 eval s2 ckpt2000

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp-003-eval-s2-ckpt2000_20260521T101541_result.json`
- **Structured JSON:** [`061c2df1dbaa7bf9e27b.json`](../../sessions/06/061c2df1dbaa7bf9e27b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 诊断结果

**时间线重建：**

| 时间 (CST) | 事件 |
|---|---|
| 15:22 | **Batch A** 启动: ckpt6000 (cuda:1) + ckpt6500 (cuda:2/0/3) |
| 16:20 | **Batch B** 启动: ckpt7500 (cuda:1) + s2-ckpt2000 (cuda:2) — **GPU 仍被 Batch A 占用** |
| 16:27 | s2-ckpt2000 收到 SIGTERM 被杀 |
| 16:44 | ckpt6500 正常完成 (exit 0) |
| 16:47 | ckpt6000 正常完成 (exit 0) |

**exp-003-eval-ckpt7500 (cuda:1):**
- ckpt6000 正在 cuda:1 上使用 ~16.8GB 显存
- ckpt7500 尝试在同一 GPU 加载第二个 8B 模型 → 33.6GB > 32.6GB 可用 → OOM 崩溃
- 进程死得太快，没有产生任何日志文件或 exit sentinel

**exp-003-eval-s2-ckpt2000 (cuda:2):**
- 上一批 eval 仍占用 cuda:2，显存不足
- 日志明确显示: `Based on the current allocation process, no modules could be assigned to the following devices due to insufficient memory: - 0: 2489319424 bytes required`
- 模型强制 offload 到 CPU，勉强开始推理
- 7 分钟后收到 SIGTERM: `Terminated` → `EXIT_CODE=143`

**exp-003-eval-s2-ckpt2500 (PID 865026, cuda:3):** 确认正常运行中（nvidia-smi 显示 GPU 3 活跃，16884MiB 使用，50% GPU-Util）。

```json
{"root_cause":"GPU scheduling collision — auto-pipeline dispatched Batch B (ckpt7500 cuda:1, s2-ckpt2000 cuda:2) while Batch A (ckpt6000 cuda:1, ckpt6500 cuda:2) was still running. s2-ckpt2000 log: 'Based on the current allocation process, no modules could be assigned to the following devices due to insufficient memory: - 0: 2489319424 bytes required' → 'Terminated' EXIT_CODE=143. ckpt7500: no log/sentinel, OOM before any output.","error_type":"resource","fix_steps":["Re-run both evals on currently free GPUs: cuda:1 和 cuda:2 (nvidia-smi 确认空闲)","Fix auto-pipeline GPU scheduler to check nvidia-smi or maintain a GPU lock before dispatching new eval batch"],"can_auto_fix":true,"affects_ckpt7500":true}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "GPU scheduling collision — auto-pipeline dispatched Batch B (ckpt7500 cuda:1, s2-ckpt2000 cuda:2) while Batch A (ckpt6000 cuda:1, ckpt6500 cuda:2) was still running. s2-ckpt2000 log: 'Based on the current allocation process, no modules could be assigned to the following devices due to insufficient memory: - 0: 2489319424 bytes required' → 'Terminated' EXIT_CODE=143. ckpt7500: no log/sentinel, OOM before any output.",
    "error_type": "resource",
    "fix_steps": [
      "Re-run both evals on currently free GPUs: cuda:1 和 cuda:2 (nvidia-smi 确认空闲)",
      "Fix auto-pipeline GPU scheduler to check nvidia-smi or maintain a GPU lock before dispatching new eval batch"
    ],
    "can_auto_fix": true,
    "affects_ckpt7500": true
  }
}
```

</details>

---
