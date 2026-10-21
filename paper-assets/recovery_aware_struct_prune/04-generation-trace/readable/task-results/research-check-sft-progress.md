# research check sft progress

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_check_sft_progress_20260516T113812_result.json`
- **Structured JSON:** [`9b86362a5a6a0ff10335.json`](../../sessions/9b/9b86362a5a6a0ff10335.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### sft_rasp_25 (cuda:2) — ✅ 已完成

- **状态**: 训练完成，模型已保存
- **最终指标**: epoch=2.0, train_loss=0.8498, mean_token_accuracy=0.8073
- **完成时间**: 2026-05-16 13:57:32 UTC
- **train_runtime**: 1635 秒 (~27 分钟)
- **EXIT_CODE=0**

### sft_standard_25 (cuda:3) — ❌ 被终止

- **状态**: 收到 SIGTERM 信号被杀 (EXIT_CODE=143)
- **终止时进度**: step 724/1870 (39%), epoch ~0.46
- **速度**: ~1.14 it/s
- **最后 loss**: ~0.92, mean_token_accuracy ~0.77

### GPU 使用率

| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| 0 | 0% | 0 / 97887 MiB |
| 1 | 0% | 0 / 97887 MiB |
| 2 | 92% | 48163 / 97887 MiB |
| 3 | 79% | 48153 / 97887 MiB |

GPU 2/3 仍有显存占用。RASP 进程 (PID 2530) 仍在运行 (CPU 125%, etime 17:13)，可能正在执行训练后的评估或其他后续步骤。

### 异常

**Standard 25% SFT 被异常终止**，需要重新启动。可能原因：OOM、手动 kill、或系统资源争抢。需确认是否要重跑。

---
