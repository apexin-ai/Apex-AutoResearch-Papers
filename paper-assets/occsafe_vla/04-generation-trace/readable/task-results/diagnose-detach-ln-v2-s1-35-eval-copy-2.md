# diagnose detach ln v2 s1 35 eval

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_detach_ln_v2_s1_35_eval_20260527T141442_result.json`
- **Structured JSON:** [`32a1396588a55e2f47e5.json`](../../sessions/32/32a1396588a55e2f47e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 实验状态：**正常完成**

eval 已成功跑完全部 10 个 tasks，进程正常退出。

### 最终指标

| 指标 | 值 |
|------|-----|
| **TSR** | 0.8940 (89.4%) |
| **CAR** | 0.8260 (82.6%) |

结果文件：`/root/occsafe_vla/artifacts/safelibero_libero_spatial_20260527_212141.json`

### CRON 误报原因

eval 脚本将结果写入 JSON 文件而非上报 W&B，CRON 按 W&B metrics 检测进程状态，找不到 metrics 就报了 "Process exited without valid W&B metrics"。实际上进程已正常完成，registry 标记 `conclusion=success` 是正确的。

### GPU cuda:0 状态

| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| 0 | 0% | 1 MiB / 97887 MiB（空闲） |
| 1 | 0% | 16778 MiB |
| 2 | 8% | 16754 MiB |
| 3 | 1% | 16778 MiB |

GPU 0 已完全释放，eval 进程已退出。

### 结论

不需要重跑。eval 正常完成，CAR=82.6%。CRON 告警是误报（缺少 W&B 上报导致检测逻辑误判）。

---
