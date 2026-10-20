# audit gpu status 10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_gpu-status-10894_20260527T193538_result.json`
- **Structured JSON:** [`1da5d006cdb9e3bb37fd.json`](../../sessions/1d/1da5d006cdb9e3bb37fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
[UTC时间确认: 2026-05-27 ~19:35 UTC]
(推算自服务器 sshd 进程时间戳 May28 03:35 UTC+8)

GPU 0: vanilla_object_s1 — step 6692/50005 (13.4%) — 0.93 sec/step (1.07 it/s) — ETA: ~06:50 UTC May 28 — DDL余量 +5h10m
GPU 1: IDLE (0% GPU util, 0 MiB VRAM)
GPU 2: detach_ln_v2_s0c_r3 — step 37888/50005 (75.8%) — 0.93 sec/step (1.08 it/s) — ETA: ~22:42 UTC May 27 — DDL余量 +13h18m
GPU 3: full_occ_ln_s4 — step 36107/50005 (72.2%) — 0.93 sec/step (1.07 it/s) — ETA: ~23:12 UTC May 27 — DDL余量 +12h48m

异常: 无
```

**补充说明**：
- **detach_ln_v2_s0c_r3**: 与预估 ~22:46 UTC 完成基本吻合，最新 checkpoint 30000 已保存
- **full_occ_ln_s4**: step 单调递增（33201→36107），无回退问题，最新 checkpoint 30000 已保存，`occ_loss=0.0089, action_loss=0.0613`（step 36100）
- **vanilla_object_s1**: 刚过 5000 checkpoint（已保存），稳定推进
- 三个实验均在 DDL 前完成，无风险

---
