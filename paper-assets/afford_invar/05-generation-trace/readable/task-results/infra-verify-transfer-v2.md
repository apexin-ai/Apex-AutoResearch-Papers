# infra verify transfer v2

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_verify-transfer-v2_20260520T001323_result.json`
- **Structured JSON:** [`7118528d10d7db1b3c85.json`](../../sessions/71/7118528d10d7db1b3c85.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已正常启动，汇报如下：

**PID 125786**: 存活，运行 1 分 15 秒

**错误**: 无实质性错误。6 处 "error" 匹配全是无害的启动信息：
- 2 条 oneDNN 浮点精度提示（TF 初始化时的 INFO）
- 4 条 TF `PredictCost()` 对 CropAndResize op 的 cost estimator 警告
- 0 条 traceback/exception

**训练进度**: 已跑到 step ~448/20000，速度 ~4.3 it/s，预计总时长 ~1h15m

**早期 L_xfr 值**:
- Step 0-3: `L_xfr=0.0`（pos=0，无 transfer loss）
- Step 4: `L_xfr=2.09`（首次出现，pos=1）
- 最新 step 440-448: `L_xfr` 稳定在 4.1~4.26 范围

**GPU 占用**:
| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 80% | 24.5G / 97.9G |
| 1 | 72% | 25.1G / 97.9G |
| 2 | 83% | 24.3G / 97.9G |
| 3 | 0% | 0G / 97.9G |

**cuda:1 残留进程**: 有。PID **124528** 占用 GPU 1（25064MiB），PID **123110** 占用 GPU 2（24340MiB）。这两个是之前残留的 python 进程，不属于当前训练（当前训练的 python PID 是 125863，在 GPU 0 上）。

---
