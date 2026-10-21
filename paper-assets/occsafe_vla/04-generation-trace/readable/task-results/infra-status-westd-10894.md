# infra status westd 10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_status-westd-10894_20260521T152531_result.json`
- **Structured JSON:** [`a614567f22c5b1c7021a.json`](../../sessions/a6/a614567f22c5b1c7021a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Ablation 训练状态汇总

| 实验 | PID | GPU | 当前 step / 50005 | 进度 | 速度 | 最新 checkpoint | 预计剩余 |
|------|-----|-----|-------------------|------|------|----------------|---------|
| **occ_detach_s0** | 523415 | GPU 0 (99%, 62GB) | ~14,585 / 50,005 | 29% | 1.08 it/s | 10000_chkpt | ~9.1h |
| **random_occ_s0** | 521936 | GPU 1 (99%, 63GB) | ~15,010 / 50,005 | 30% | 1.06 it/s | 10000_chkpt | ~9.2h |
| **occ_detach_s1** | 523560 | GPU 2 (99%, 62GB) | ~14,632 / 50,005 | 29% | 1.07 it/s | 10000_chkpt | ~9.2h |
| **random_occ_s1** | 523914 | GPU 3 (82%, 62GB) | ~14,602 / 50,005 | 29% | 1.08 it/s | 10000_chkpt | ~9.1h |

**磁盘**: `/root/autodl-tmp` 250G 总量，已用 111G (45%)，剩余 140G，空间充裕。

**预计完成时间**: 4 个实验均约在 **~9 小时后**（约 5月22日凌晨 5-6 点 UTC）完成。下一个 checkpoint（20000_chkpt）约在 ~5 小时后产生。

所有 4 个实验运行正常，GPU 满载，无异常。

---
