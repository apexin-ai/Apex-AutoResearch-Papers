# ops 10894 progress check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_10894-progress-check_20260527T011714_result.json`
- **Structured JSON:** [`688a9398b81d0333f573.json`](../../sessions/68/688a9398b81d0333f573.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练进度汇总

| 实验 | GPU | PID | 当前 step | 进度 | 速度 | tqdm 剩余 | step 2500 losses |
|------|-----|-----|-----------|------|------|-----------|------------------|
| full_occ_ln_v2_s1c | cuda:0 | 481426 | ~2545/50005 | 5.1% | 1.08 it/s | ~12h15m | occ=0.0125, act=0.1631 |
| full_occ_ln_v2_s2 | cuda:1 | 481643 | ~2534/50005 | 5.1% | 1.07 it/s | ~12h15m | occ=0.0137, act=0.1377 |
| detach_ln_v2_s0c | cuda:2 | 481988 | ~2531/50005 | 5.1% | 1.06 it/s | ~12h25m | occ=0.0187, act=0.1689 |

预计完成时间：约 12-12.5 小时后，即 **5月27日 ~13:30 UTC**（北京时间 ~21:30），远在 5月28日 12:00 UTC 截止线之前。

**cuda:3 状态**：PID 482336 (detach_ln_v2_s1c) 已死，但有新进程 **PID 490883** 在 cuda:3 运行 `full_occ_ln_v2_s0d`（seed=42, Full OCC LN），已运行 1m50s，占用 62GB 显存。这不在原始 3 个实验列表中——有人额外启动了第 4 个实验。

---
