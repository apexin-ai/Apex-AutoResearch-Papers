# ops 10894 verify and promote

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_10894-verify-and-promote_20260527T000044_result.json`
- **Structured JSON:** [`cf130255017d6b953d9a.json`](../../sessions/cf/cf130255017d6b953d9a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 registry 更新完成。汇报如下：

## westd-10894 GPU 状态

| GPU | VRAM | Util | 实验 | PID | Step | 状态 |
|-----|------|------|------|-----|------|------|
| cuda:0 | 79788/97887 MiB | 99% | **detach_ln_v2_s1** (PID 433768) + **reverse_cutoff_s2_v2_eval** (PID 428963) | 433768 + 428963 | 1384 + T5 27/50 | RUNNING |
| cuda:1 | 62203/97887 MiB | 33% | **full_occ_ln_v2_s0b** | 458224 | ~308 | QUEUED→RUNNING ✓ |
| cuda:2 | 62203/97887 MiB | 61% | **full_occ_ln_v2_s1b** | 458541 | ~305 | QUEUED→RUNNING ✓ |
| cuda:3 | 63013/97887 MiB | 99% | **detach_ln_v2_s0b** | 458889 | ~304 | QUEUED→RUNNING ✓ |

## 关键发现

1. **PID 433768 = detach_ln_v2_s1**（occ_detach=true, occ_norm_type=ln, seed=43）。Registry 原先错误标记为 westd-34685，已修正为 westd-10894 PID 433768。当前 step 1384，~1.1 s/it。

2. **reverse_cutoff_s2_v2_eval**：已完成 5/10 tasks，当前 T5 的 27/50 rollouts。PREPARING→RUNNING ✓。Log 在 `/tmp/reverse_cutoff_s2_v2_eval.log`。

3. **3 个 b-variants 均已突破 step 275 关卡**（旧版 stall 点），正常训练中，~1.07-1.08 it/s。

## 磁盘
- 根分区：15G/30G used (48%)
- 数据盘：127G/250G used (51%)

## 未完成项
- 未注册 cron 监控（需要 CronCreate 工具）。需要确认是否需要设置。

---
