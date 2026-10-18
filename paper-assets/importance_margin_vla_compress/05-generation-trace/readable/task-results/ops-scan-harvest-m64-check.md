# ops scan harvest m64 check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_scan_harvest_m64_check_20260523T031804_result.json`
- **Structured JSON:** [`d49e195296078f97e15a.json`](../../sessions/d4/d49e195296078f97e15a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态

| 服务器:GPU | 实验 | 状态 | 进度 | SR |
|-----------|------|------|------|-----|
| westd-27271:GPU0 | eval_xvla_random_k095_long_seed42 | 🟢 Running | Task 3/10, ep ~43/50 (148/500 = 30%) | T0=0%, T1=46%, T2=72% |
| westd-27271:GPU1 | eval_pi05_random_k09_object_seed43_v3 | 🟢 Running | T7 ep 30/50 (330/500 = 66%) | 累计 39/350 = 11.1% |
| westd-41074:GPU1 | eval_pi05_random_k05_spatial_seed43_v2 | ✅ **完成** | 500/500 | **72.4%** |

## M64 训练
- **Step 88150 / 100000** (88.2%)
- Speed: 0.6 sps (~82s per 50 steps)
- 剩余 11850 steps ÷ 0.6 sps ≈ **5.5h**
- **预估完成: 今天 ~16:48**

## 收割

**eval_pi05_random_k05_spatial_seed43_v2** → DONE (success)
- SR = **72.4%** (362/500), 耗时 80.6 min
- Per-task: T0=88%, T1=88%, T2=88%, T3=56%, T4=38%, T5=32%, T6=86%, T7=92%, T8=72%, T9=84%
- Registry 已更新 (conclusion=success, metrics, log_path)
- westd-41074 GPU 1 已空闲，可接新任务

---
