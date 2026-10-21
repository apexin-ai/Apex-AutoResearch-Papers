# ops cuda0 cleanup plan002 launch

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cuda0-cleanup-plan002-launch_20260515T044452_result.json`
- **Structured JSON:** [`24fea71a268aff23f962.json`](../../sessions/24/24fea71a268aff23f962.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

### cuda:0 清理前后

| | 清理前 | 清理后（当前） |
|---|---|---|
| 显存占用 | 49175 MiB（孤儿，无进程） | 90355 MiB（41174 新训练 + ~49GB 驱动残留） |
| 利用率 | 0% | 100% |
| 进程 | 无可见进程 | PID 955301 (train_sft.py) |

### 被 kill 的孤儿进程
- **PID 954592** — 之前卡死的 `full_trace_label_only_seed42_v2`（状态 Sl，挂了 45 分钟，0% 利用率但占 49GB 显存）
- kill -9 后进程消亡，但 ~49GB 显存未被驱动释放（`nvidia-smi --gpu-reset -i 0` 硬件不支持）

### plan_002 启动状态
- **已由其他实例提交**（tmux session `full_trace_label_only_seed42`，12:48:06 创建）
- 命令与你的计划一致，额外加了 `--gradient_checkpointing` 绕过显存不足
- PID 955301，使用 41174 MiB，训练已推进（step 1/444，~18.8s/step）
- 未 OOM，正常运行中

### 最终两卡快照
- **GPU 0**: 90355/97887 MiB, 100% util, PID 955301 (`full_trace_label_only_seed42_v2`)
- **GPU 1**: 52779/97887 MiB, 100% util, PID 953138 (`vota_no_ae_seed42`) — 未受影响

**注意**: GPU 0 有 ~49GB 驱动级残留显存无法释放，但加了 gradient_checkpointing 后训练正常进行。如果后续需要完全清理，需要重启实例。

---
