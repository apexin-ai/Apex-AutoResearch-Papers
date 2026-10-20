# ops status check 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_status-check-34685_20260528T054443_result.json`
- **Structured JSON:** [`b993cb1ed785affa0e05.json`](../../sessions/b9/b993cb1ed785affa0e05.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== nvidia-smi (Thu May 28 13:45:01 UTC 2026) ===
GPU  Name                    Temp  Power       VRAM             Util  PID
  0  RTX PRO 6000 Blackwell  71°C  463W/600W   62165/97887 MiB  99%  47238
  1  RTX PRO 6000 Blackwell  68°C  452W/600W   62161/97887 MiB  96%  62535
  2  RTX PRO 6000 Blackwell  68°C  471W/600W   62161/97887 MiB  99%  56474
  3  RTX PRO 6000 Blackwell  71°C  495W/600W   63009/97887 MiB  99%  56822

注意: GPU 0 PID = 47238（非预期的 47162）

=== 轮询脚本 ps ===
   PID     ELAPSED CMD
 61243    01:25:07 bash /root/poll_eval_detach_ln_v2_s3.sh
 61244    01:25:07 bash /root/poll_eval_detach_ln_v2_s2.sh
 61245    01:25:07 bash /root/poll_eval_full_occ_ln_v2_s3.sh
3 个轮询脚本全部存活。

=== 轮询脚本日志 ===
3 个日志均只有: "Thu May 28 04:20:06 UTC 2026: Polling started for &lt;exp_name>"
→ 均未触发 eval（50000_chkpt 尚未生成）

=== 训练进度 ===
exp_id           | GPU | PID   | 当前 step    | 目标 step | 50000_chkpt | 最新 chkpt   | 最新 chkpt 时间
-----------------|-----|-------|-------------|-----------|-------------|-------------|----------------
detach_ln_v2_s2  |  0  | 47238 | 13281/50005 | 25000     | ❌          | 35000_chkpt | May 28 12:51
full_occ_bn_v2_s2|  1  | 62535 | 3801/50005  | (非关键)  | ❌          | (仅初始目录)| May 28 12:42
full_occ_ln_v2_s3|  2  | 56474 | 6895/50005  | 10000     | ❌          | 45000_chkpt | May 28 13:15
detach_ln_v2_s3  |  3  | 56822 | 6903/50005  | 10000     | ❌          | 45000_chkpt | May 28 13:15

=== ETA 估算（基于 checkpoint 间隔 ~80min/5000步 和当前速度 ~1.09 it/s） ===
exp_id           | 剩余 step → 目标 | 预计完成 50000_chkpt
-----------------|------------------|---------------------
detach_ln_v2_s2  | 11719 步 → 25000 | ~16:50 UTC（还需 ~3h05m）
full_occ_ln_v2_s3| 3105 步 → 10000  | ~14:35 UTC（还需 ~50min）
detach_ln_v2_s3  | 3097 步 → 10000  | ~14:35 UTC（还需 ~50min）
```

**DDL 12:00 UTC 已超时 1h45m。** full_occ_ln_v2_s3 和 detach_ln_v2_s3 约 50min 后出 50000_chkpt。detach_ln_v2_s2 最慢，还需 ~3h。

---
