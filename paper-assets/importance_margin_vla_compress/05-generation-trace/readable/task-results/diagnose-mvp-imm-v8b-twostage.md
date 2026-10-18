# diagnose mvp imm v8b twostage

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_mvp_imm_v8b_twostage_20260516T070648_result.json`
- **Structured JSON:** [`35d3bd52611afebce29a.json`](../../sessions/35/35d3bd52611afebce29a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验没有失败，是 cron 监控误报。**

训练于 14:57:22 正常完成，两个 stage 全部跑完：
- Stage1: 10K steps, loss 降至 0.034
- Stage2: 20K steps 全部完成, loss 降至 0.027, action_loss=0.027
- 速度稳定在 3.1 steps/sec
- Final checkpoint 已保存 (`final/checkpoint.pt`, 1.2GB)，stage2 有 9 个中间 checkpoint
- W&B offline run 完整可 sync

**误报原因**: 进程正常退出后 cron 监控检测到进程不存在且无 sentinel 文件，误判为异常退出。建议训练脚本结束时写入 `.done` sentinel 文件。

诊断报告已保存至 `artifacts/mvp_imm_v8b_twostage/diagnosis.md`。

---
