# check training monitor

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_training_monitor_20260523T043052_result.json`
- **Structured JSON:** [`6944da9eeb143a485c1b.json`](../../sessions/69/6944da9eeb143a485c1b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 grep 返回 0 匹配（exit code 1 = 没找到匹配行），即 **无 NaN/OOM**。

## 监控汇总

| 实验 | Step | 进度 | Loss (unweighted) | 异常 |
|------|------|------|-------------------|------|
| rho03_adaptive_seed456_r2 | 1539/6103 | 25% | ~2.4-3.3 | 无 |
| rho03_uniform_seed456 | 2764/6103 | 45% | ~2.0-2.9 | 无 |
| bs8_nmin4_adaptive_seed123_r2 | 2013/6103 | 33% | ~1.8-2.3 | 无 |
| bs8_nmin4_uniform_seed123_r2 | 2046/6103 | 34% | ~1.6-2.1 | 无 |

- **GPU**: 4 卡全部 100% 利用率，显存使用 26-48 GiB
- **NaN/OOM/Error**: 全部 0
- **磁盘**: /root/autodl-tmp 用了 172G/250G (69%)，剩余 79G 充足
- **速度**: 约 2.5-2.6 s/it，预计各实验剩余 2.5-3.5 小时

4 个实验均正常推进，无任何异常。

---
