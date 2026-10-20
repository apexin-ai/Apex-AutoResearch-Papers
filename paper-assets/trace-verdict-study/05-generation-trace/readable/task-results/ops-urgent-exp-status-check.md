# ops urgent exp status check

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_exp_status_check_20260515T221100_result.json`
- **Structured JSON:** [`9026f4c161ece5e77a7d.json`](../../sessions/90/9026f4c161ece5e77a7d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。实验 B 仍在运行，不做 GPU reset。

---

## 汇报

### 实验 A: deepseek_exception_only_seed456 — **已完成 ✓**

| 指标 | 值 | vs seed42 Δ |
|------|-----|-------------|
| accuracy | **99.33%** | **0pp** (identical) |
| fail_f1 | **0.9883** | 0 |
| fail_recall | **1.0** | 0 |
| fail_precision | 0.9769 | 0 |
| pass_precision | 1.0 | 0 |
| train_loss | 0.1225 | — |

**结论: success.** seed42 和 seed456 在 DeepSeek 上完全一致 (99.33%)，seed123 (91.09%) 是离群值。2/3 seeds 鲁棒，exception_only 跨模型泛化结论成立。

### 实验 B: deepseek_full_trace_seed42_v3 — **运行中**

- 进度: step **256/444** (57.7%), epoch 2 中段
- 速度: ~16.4s/step
- 预计剩余: **~51 分钟**
- GPU 1: 22386MiB, 100% util

### GPU 清理
**未执行。** 实验 B 仍在 GPU 1 运行。GPU 0 上 eval 进程 (PID 166680) 刚完成，显存应会自动释放。

### Cron 状态
- `deepseek_exception_only_seed456`: 无 cron 注册（训练完成时 hook 直接触发了 eval）
- `deepseek_full_trace_seed42_v3`: cron 活跃，reconcile 确认进程运行中 (pid=163109)

---
