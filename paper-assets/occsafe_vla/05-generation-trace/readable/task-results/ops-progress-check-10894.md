# ops progress check 10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_progress_check_10894_20260524T190228_result.json`
- **Structured JSON:** [`bb77c8dfea7cc07ca7d9.json`](../../sessions/bb/bb77c8dfea7cc07ca7d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 GPU 均活跃（82-99% 利用率，~62GB 显存）。

| 实验 | GPU | tqdm step | 全局 step | 剩余步数 | 速度 | 预估剩余时间 |
|------|-----|-----------|-----------|----------|------|-------------|
| ablation_occ_detach_s0_retrain | cuda:0 | 3559/50005 | **23559** (20K+3559) | 26446 | ~1.07 it/s | **~6.9h** |
| full_occ_ln_s0 | cuda:1 | 35155/50005 | **35155** | 14850 | ~1.08 it/s | **~3.8h** |
| full_occ_ln_s1 | cuda:2 | 3349/50005 | **23349** (20K+3349) | 26656 | ~1.06 it/s | **~7.0h** |
| full_occ_ln_s2 | cuda:3 | 3358/50005 | **23358** (20K+3358) | 26647 | ~1.08 it/s | **~6.9h** |

预估完成时间（UTC，基于当前时刻约 2026-05-24T10:00Z）：
- **full_occ_ln_s0**: ~05-24 14:00 UTC（最先完成）
- **ablation_occ_detach_s0_retrain**: ~05-24 17:00 UTC
- **full_occ_ln_s1**: ~05-24 17:00 UTC
- **full_occ_ln_s2**: ~05-24 17:00 UTC

---
