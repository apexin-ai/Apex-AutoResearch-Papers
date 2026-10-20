# ops status check 10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_status-check-10894_20260528T054452_result.json`
- **Structured JSON:** [`247ec40ec3873c72f5f2.json`](../../sessions/24/247ec40ec3873c72f5f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## nvidia-smi (2026-05-28 13:45 UTC)

```
GPU 0: RTX PRO 6000 | 44°C |  90W/600W | 62971/97887 MiB |  0% util | PID 798980
GPU 1: RTX PRO 6000 | 60°C | 442W/600W | 62243/97887 MiB | 99% util | PID 822480
GPU 2: RTX PRO 6000 | 57°C | 420W/600W | 62199/97887 MiB | 60% util | PID 959741
GPU 3: RTX PRO 6000 | 61°C | 457W/600W | 62193/97887 MiB | 99% util | PID 959956
```

## 实验状态

| 实验 | GPU | PID | 存活 | 运行时间 | 已有 checkpoint | 50000_chkpt |
|------|-----|-----|------|----------|----------------|-------------|
| vanilla_object_s1 | cuda:0 | 798980 | ✓ | 11h54m | 35000, 40000, **45000** (刚存 13:45) | ✗ |
| detach_ln_v2_s4 | cuda:1 | 822480 | ✓ | 7h06m | 20000, 25000 | ✗ |
| full_occ_bn_v2_s3 | cuda:2 | 959741 | ✓ | 45m | 无 step checkpoint | ✗ |
| vanilla_object_s2 | cuda:3 | 959956 | ✓ | 45m | 无 step checkpoint | ✗ |

注：实际 PID 与预期略有偏差 — detach_ln_v2_s4 为 822480（非 822402），full_occ_bn_v2_s3 为 959741（非 959661），vanilla_object_s2 为 959956（非 959808）。

## 轮询脚本

PID 962263 存活，运行 41m41s，执行 `bash /root/poll_eval_vanilla_object_s1.sh`。日志仅有一行：`Thu May 28 05:03:56 UTC 2026: Polling started for vanilla_object_s1`。

## Step 估算（基于 checkpoint 间隔）

- **vanilla_object_s1**: ~45000 step（45000_chkpt 刚存完，GPU util 降到 0% 可能在做 save）。5000 步/~80min → 50000_chkpt 预计 **~15:05 UTC**
- **detach_ln_v2_s4**: ~26500 step（25000_chkpt 存于 13:21，5000步/~82min）。到 50000 还需 ~5.5h → **~19:15 UTC**
- **full_occ_bn_v2_s3**: < 5000 step。到 50000 需 ~13h → **次日凌晨**
- **vanilla_object_s2**: < 5000 step。到 50000 需 ~13h → **次日凌晨**

**DDL 12:00 UTC 已过 1h45m。** 4 个实验均未完成，仅 vanilla_object_s1 接近收尾。

---
