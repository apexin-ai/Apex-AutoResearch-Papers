# ops check 4 running status

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_4_running_status_20260515T100810_result.json`
- **Structured JSON:** [`87e65b0879d0dc8dbd09.json`](../../sessions/87/87e65b0879d0dc8dbd09.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。PID-GPU 映射通过子进程 PID 偏移量（+5）和 elapsed time 对齐确认。

| GPU | 实验 | PID | Step | 进度 | 速度 | 剩余时间 | GPU Util | 显存 |
|-----|------|-----|------|------|------|----------|----------|------|
| 0 | golden_ratio_seed42 | 193921 | 724/6103 | 11.9% | 2.11s/it | ~3h10m | 99% | 46.5/97.9 GB |
| 1 | **ess_only_seed42** | 189240 | 1552/6103 | **25.4%** | 2.12s/it | **~2h41m** | 94% | 46.5/97.9 GB |
| 2 | nmin1_seed42 | 194005 | 666/6103 | 10.9% | 2.84s/it | ~4h17m | 99% | 46.5/97.9 GB |
| 3 | tau_06_seed42 | 195746 | 179/6103 | 2.9% | 2.18s/it | ~3h35m | 80% | 46.5/97.9 GB |

### ess_only_seed42 详细状态

- 进度最快（已启动 55 分钟，领先其他实验约 22 分钟）
- `loss=11.02`, `grad_norm=26.25`, `lr=3.93e-05` — **loss 异常偏高**，其他实验 weighted_loss 在 1.4~3.6 范围
- `ESS=2.0`, `alpha_eff=0.537`, `b=1.025`, `mean_q=0.731`
- `weighted_loss=2.948` vs `unweighted_loss=2.050`（加权后 loss 增幅约 44%）

### 注意事项

1. **ess_only_seed42 的 loss=11.02 需要关注** — 这是 trainer 报告的总 loss，远高于其他实验。可能是 ESS-only 加权策略导致的梯度不稳定。
2. **nmin1_seed42 速度偏慢**（2.84s/it vs 其他 ~2.12s/it），且 ESS=1.065 极低（几乎退化为单样本），alpha_eff 已 saturate 到上限 0.8。
3. **GPU 3（tau_06）利用率 80%** 略低于其他卡，刚启动 6.5 分钟，可能还在 warmup。

---
