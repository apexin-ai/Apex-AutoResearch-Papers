# ssh check batchsize16 30476

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_batchsize16_30476_20260517T234517_result.json`
- **Structured JSON:** [`35b0f9a710ee6de199bc.json`](../../sessions/35/35b0f9a710ee6de199bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval (PID 65732) 仍在运行。等几分钟后再查结果。先给出当前状态汇总：

## 诊断结果

| 项目 | 状态 |
|------|------|
| **进程** | batchsize16_nmin8 进程已退出，无残留 |
| **退出码** | `EXIT_CODE=0`（正常完成） |
| **日志** | 训练到 6103/6103 steps (100%)，输出 `DONE: batchsize16_nmin8_r2` |
| **最高 checkpoint** | `checkpoint-6103` + `final` 目录均存在 |
| **训练时长** | 4h10m57s，train_loss = 2.6308 |
| **输出路径** | `/root/autodl-tmp/provenance_weight_training/output/models/batchsize16_nmin8_r2/final` |
| **GPU 3** | 空闲，0MiB 显存占用，30°C |

**结论：batchsize16_nmin8_r2 正常完成（step 6103/6103）。**

Eval PPL 已在 GPU 3 上启动 (PID 65732)，预计几分钟后完成。结果将写入 `/root/autodl-tmp/provenance_weight_training/output/models/batchsize16_nmin8_r2/eval_result.json`。

需要我稍后查看 eval 结果吗？

---
