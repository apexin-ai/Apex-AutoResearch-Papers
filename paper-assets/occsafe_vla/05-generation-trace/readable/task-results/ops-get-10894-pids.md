# ops get 10894 pids

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_get-10894-pids_20260526T181635_result.json`
- **Structured JSON:** [`9f3c73e23cbf9d718871.json`](../../sessions/9f/9f3c73e23cbf9d718871.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

| 实验 | tmux session | GPU | 训练 PID | 当前 step | 速度 | 状态 |
|------|-------------|-----|---------|-----------|------|------|
| `reverse_cutoff_s2_v2` | `reverse_cutoff_s2_v2` | 0 | 170698 | ~31882/50005 (64%) | ~1.08 it/s | 运行中，已跑 9h13m |
| `full_occ_ln_v2_s0` | `full_occ_ln_v2_s0` | 1 | 386277 | ~146/50005 (0.3%) | ~1.07 it/s | 刚重启 ~3min，旧 run 02:08 失败 |
| `full_occ_ln_v2_s1` | `full_occ_ln_v2_s1` | 2 | 386345 | ~149/50005 (0.3%) | ~1.04 it/s | 刚重启 ~3min，旧 run 02:09 失败 |
| `detach_ln_v2_s0` | `detach_ln_v2_s0` | 3 | 386619 | ~147/50005 (0.3%) | ~1.07 it/s | 刚启动 ~3min |

GPU 利用率全部 99%，显存 ~62GB/卡。磁盘 `/root/autodl-tmp` 用了 127G/250G (51%)。

3 个新启动的实验（GPU 1/2/3）按 ~1.05 it/s 估算，50005 steps 约需 **13.2h**，预计完成时间约 05/27 15:30 UTC。`reverse_cutoff_s2_v2` 剩 ~18100 steps，约需 **4.7h**，预计 05/27 07:00 UTC 完成。全部在 05/28 12:00 UTC deadline 之前。

---
