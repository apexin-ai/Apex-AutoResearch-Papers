# ops check 10894 status

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_10894_status_20260524T120732_result.json`
- **Structured JSON:** [`b7ffc21e7582472ded4f.json`](../../sessions/b7/b7ffc21e7582472ded4f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-10894 实验状态汇报

### GPU 总览

| GPU | 显存占用 | 利用率 | PID | 实验 |
|-----|---------|--------|-----|------|
| 0 | 62203 MiB | 41% | 746696 | ablation_occ_detach_s0_retrain (`--occ_detach true`, seed 42) |
| 1 | 62203 MiB | 99% | 742821 | full_occ_ln_s0 (`--occ_detach false --occ_norm_type ln`, seed 42) |
| 2 | 62203 MiB | 99% | 743031 | full_occ_ln_s1 (seed 43) |
| 3 | 63013 MiB | 99% | 743375 | full_occ_ln_s2 (seed 44) |

### 训练进度

| 实验 | 当前 step | 进度 | 速度 | 已运行 | 预计剩余 |
|------|-----------|------|------|--------|---------|
| **ablation_occ_detach_s0_retrain** | ~10248/50005 | **20.5%** | ~1.08 it/s | 3h | ~10h |
| full_occ_ln_s0 | ~10629/50005 | **21.3%** | ~1.08 it/s | 3h06m | ~10h |
| full_occ_ln_s1 | ~10617/50005 | **21.2%** | ~1.08 it/s | 3h07m | ~10h |
| full_occ_ln_s2 | ~10590/50005 | **21.2%** | ~1.03 it/s | 3h07m | ~10h |

### 重点确认

**ablation_occ_detach_s0_retrain 存活，正常运行。** 刚过 step 10000 checkpoint（已保存 merged model），当前 ~10248 step，GPU 利用率 41%（略低于其他三个的 99%，但进程活跃、日志持续写入）。最近一次 AUX log（step 10200）：occ_loss=0.0097, action_loss=0.1152。

GPU 0 利用率偏低（41% vs 99%）值得关注，可能是刚完成 checkpoint 保存后的恢复阶段，后续应趋于稳定。

---
