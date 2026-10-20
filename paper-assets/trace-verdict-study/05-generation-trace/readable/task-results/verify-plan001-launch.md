# verify plan001 launch

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_plan001-launch_20260515T042216_result.json`
- **Structured JSON:** [`39ce3c2d2b6656177bd4.json`](../../sessions/39/39ce3c2d2b6656177bd4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

| 实验 | PID | 状态 | GPU | 进度 |
|------|-----|------|-----|------|
| plan_001 vota_no_ae | 953133 | **运行中** ✓ | GPU 1, 81.2GB/98GB, 100% util, 64°C | 3/444 steps (~0.7%), ~14.5s/step |
| plan_002 label-only | 951174 | **已崩溃** ✗ | — | OOM 退出 (exit code 1) |

**plan_001** 正常训练中，已运行约 1 小时 7 分钟，预计还需约 1h45m 完成。

**plan_002** 启动时 CUDA OOM 崩溃。原因：GPU 0 上有两个残留进程（PID 950697、951029）各占 ~15.8GB 显存，导致 plan_002 分配不到足够内存。当前 GPU 0 显示 49.2GB 已占用（这些残留进程仍在）。

需要清理 GPU 0 上的残留进程后重启 plan_002。

---
