# diagnose gpu full audit both servers

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gpu_full_audit_both_servers_20260527T184851_result.json`
- **Structured JSON:** [`ac3e9227b6edb97d901c.json`](../../sessions/ac/ac3e9227b6edb97d901c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

服务器 UTC 时间: **2026-05-27 18:49 UTC** | DDL: **2026-05-28 12:00 UTC** (余 17h11m)

```
服务器       | GPU | 实验                  | step/50005 (%)    | speed     | ETA (UTC)         | DDL余量
-------------|-----|-----------------------|-------------------|-----------|-------------------|--------
westd-34685  | 0   | detach_ln_v2_s2       | 12468 (24.9%)     | 1.08 it/s | May28 04:28 UTC   | +7h32m ✅
westd-34685  | 1   | vanilla_object_s0     |  7169 (14.3%)     | 1.08 it/s | May28 05:50 UTC   | +6h10m ✅
westd-34685  | 2   | full_occ_ln_v2_s3     | ~7950 (15.9%) est | ~1.09 it/s| May28 05:32 UTC   | ~+6h28m ✅
westd-34685  | 3   | detach_ln_v2_s3       |  7969 (15.9%)     | 1.08 it/s | May28 05:38 UTC   | +6h22m ✅
-------------|-----|-----------------------|-------------------|-----------|-------------------|--------
westd-10894  | 0   | vanilla_object_s1     |  3754 (7.5%)      | 1.10 it/s | May28 06:30 UTC   | +5h30m ✅
westd-10894  | 1   | IDLE                  |  —                | —         | —                 | —
westd-10894  | 2   | detach_ln_v2_s0c_r3   | 34754 (69.5%)     | 1.07 it/s | May27 22:46 UTC   | +13h14m ✅
westd-10894  | 3   | full_occ_ln_s4        |  3725 (7.4%)      | 1.10 it/s | May28 06:30 UTC   | +5h30m ✅
```

**所有 7 个实验均在 DDL 前完成，最紧的余量 +5h30m。**

备注:
- `full_occ_ln_v2_s3` 步数是估算（日志被截断），基于与 `detach_ln_v2_s3` 同时启动推算
- `detach_ln_v2_s0c_r3` 最先完成（今晚 22:46 UTC），之后 10894 GPU 2 将空闲
- **10894 GPU 1 当前空闲**
- OCC pipeline (34685): 仍在下载中 (~5.2G)

---
