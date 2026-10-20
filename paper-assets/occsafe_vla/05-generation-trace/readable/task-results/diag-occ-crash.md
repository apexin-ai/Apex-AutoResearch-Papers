# diag occ crash

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_occ_crash_20260520T164531_result.json`
- **Structured JSON:** [`550c5a83d195078aeb58.json`](../../sessions/55/550c5a83d195078aeb58.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**结论：进程未崩溃，三个实验均正常运行中。** cron 误报原因是 `WANDB_MODE=disabled` + 无 sentinel 文件，导致监控无法检测进程存活。

关键事实：
- 3 个 GPU 各有一个 python 进程，99% 利用率，~62GB 显存
- 训练已到 step 650 左右，速度 ~1.09 it/s，预计还需 ~12 小时完成
- 日志中无任何 traceback / error
- `occ_index.json` 格式正确（`demos` dict{str→int}），M009 bug 不适用于此数据
- occ_loss 在 0.02 左右，需后续验证是否因 demo matching 失败导致大量 fallback 到全零 label

报告已写入 `artifacts/occ_crash_diagnosis.md`。

---
