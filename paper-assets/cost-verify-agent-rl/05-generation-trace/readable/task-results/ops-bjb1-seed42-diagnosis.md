# ops bjb1 seed42 diagnosis

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb1_seed42_diagnosis_20260522T122051_result.json`
- **Structured JSON:** [`3f47c84e2539e5105391.json`](../../sessions/3f/3f47c84e2539e5105391.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告：exp029-seed42

### 进程状态：**已正常完成（非崩溃）**

训练完成了全部 5/5 步后正常退出。Cron 误报——进程退出是因为训练结束，不是崩溃。

### Checkpoint

- **路径**: `/root/autodl-tmp/checkpoints/exp029-seed42/global_step_5/actor/`
- **`latest_checkpointed_iteration.txt`**: 5
- **文件完整**: model (2×4GB) + optim (2×6.8GB) + extra_state + huggingface config，两个 rank 都已保存
- **保存时间**: 2026-05-22 20:13~20:14

### 最终 Metrics（step 5, 32 episodes）

| 指标 | Step 0 | Step 5 |
|------|--------|--------|
| pass@1 | 0.125 (4/32) | 0.09375 (3/32) |
| reward/mean@32 | 1.25 | 0.9375 |
| reward/best@32/mean | 9.84 | 9.55 |
| action_is_valid | 0.783 | 0.603 |

pass@1 从 12.5% 降到 9.375%，训练未带来改善，反而略有退化。

### W&B

日志末尾有 `BrokenPipeError` 出现在 wandb 的 `service_client.py` 关闭阶段——这是 W&B 清理时的非致命错误，发生在 checkpoint 保存之后。这解释了 Cron 报 "no W&B"：run 可能未被正确 finalize，W&B 端显示为 crashed。

### GPU 状态：**空闲**

两张 RTX PRO 6000（96GB）均 0MiB / 0% 利用率，无进程占用。

### 磁盘

`/root/autodl-tmp/`: 212G/250G (85%), 剩余 39G。

### 总训练时长

8323.7s（约 2h 19m）。

---
