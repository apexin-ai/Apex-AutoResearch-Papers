# ops falcon3 cqa1 d100 check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_falcon3-cqa1-d100-check_20260522T082827_result.json`
- **Structured JSON:** [`165fba5a453f8d09ab3d.json`](../../sessions/16/165fba5a453f8d09ab3d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练进程**未退出**，仍在运行中。PID 666107 在 cuda:0 上，当前进度 571/4159（~14%），启动于 15:48。lora_adapter 目录为空（训练未完成，符合预期）。

还有 4 个子进程（PID 666428-666431）也在运行，可能是 dataloader workers。

**结论：Cron 误触发，训练正常进行中。** 不更新 registry，不删 cron——保留 cron 继续监控训练完成。

按当前 ~4.3s/it 速率，剩余 3588 steps 约需 4.3h，预计约 20:30 完成。

---
