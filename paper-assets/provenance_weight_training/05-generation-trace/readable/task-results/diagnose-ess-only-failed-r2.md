# diagnose ess only failed r2

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_ess_only_failed_r2_20260517T210613_result.json`
- **Structured JSON:** [`50ced31cad8fdef9d180.json`](../../sessions/50/50ced31cad8fdef9d180.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 诊断报告

### 结论：r2 实验**没有失败**，当前正在正常运行

你的诊断请求基于一个过时的前提。实际情况如下：

---

### 第一轮实验（已失败）

两个**第一轮**实验被 **SIGTERM (EXIT_CODE=143)** 在几乎同一时刻杀死：

| 实验 | 进度 | 运行时长 | 终止时间 (UTC) |
|------|------|----------|----------------|
| `ess_only_seed123` | 2989/6103 (49%) | 5h24m | 2026-05-17 20:55:28 |
| `ess_only_seed456` | 2897/6103 (47%) | 5h21m | 2026-05-17 20:55:29 |

**根本原因**：两个进程在 1 秒内被同时 SIGTERM。无 OOM、无 CUDA error、无 Python traceback。日志末尾仅有 `Terminated`。这是**外部 kill**，最可能是平台级事件（seetacloud 维护/资源回收/计费限制）。

`grid_b0_3_seed456` 正常完成（exit code 0），与此无关。

---

### r2 实验（当前状态）

两个 r2 重试已于 05:00 (May 18) 启动，**当前正在正常运行**：

| 实验 | GPU | 当前进度 | 状态 |
|------|-----|----------|------|
| `ess_only_seed123_r2` | cuda:2 | 2160/6103 (35%) | 运行中 |
| `ess_only_seed456_r2` | cuda:1 | 2658/6103 (44%) | 运行中 |

- tmux sessions 存在
- Python 进程活跃（CPU 100%）
- GPU 利用率 100%，显存正常（46.5GB/97.9GB per GPU）
- 无 exit sentinel file（因为没有退出）
- Checkpoint 完整，resume 成功

---

### 对其他实验的影响

cuda:0 (`random_reweight_seed456`, PID 125367) 和 cuda:3 (`qwen06b_uniform_seed42_v2`, PID 125995) 也在正常运行，未受影响。这两个进程从 02:14/02:17 开始运行，跨越了第一轮被杀的时间点却未受影响，进一步说明第一轮被杀是**针对特定进程的 SIGTERM**，而非系统级 OOM killer。

---

### 总结

- **不需要修复**。r2 已经在跑，一切正常。
- 第一轮被杀的原因大概率是平台侧操作，建议留意 seetacloud 控制台是否有维护通知记录。

---
