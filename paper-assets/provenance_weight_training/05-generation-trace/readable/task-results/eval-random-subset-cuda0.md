# eval random subset cuda0

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_random_subset_cuda0_20260524T220506_result.json`
- **Structured JSON:** [`fb0a6e54dedcaf7c0f6f.json`](../../sessions/fb/fb0a6e54dedcaf7c0f6f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕（metrics/conclusion/checkpoint_path/log_path 均已写入）。

## 结果汇总

| Eval Set | PPL |
|----------|-----|
| **Holdout** | **17.694** |
| **OWT** | **18.349** |
| **Wiki** | **15.317** |

## 关键对比

| 对比 | Holdout PPL | Δ |
|------|-------------|---|
| **random_subset_epoch** | 17.694 | — |
| uniform full-data baseline | ~17.694 | **≈ 0** |
| D&R q>0.3 multi-epoch | ~17.25 | **+0.444** |

**核心发现**：
- **vs uniform**：random 31.48% 子集 + multi-epoch 与 uniform full-data PPL **几乎完全相同** (17.694 vs 17.694)。多 epoch 补偿了数据量减少。
- **vs D&R**：random subset 比 D&R 差 0.444 PPL。说明 **D&R 的过滤质量是真实贡献**，不仅仅是 multi-epoch 的效果。用相同数据量但随机选取 vs 质量过滤选取，后者明显更好。

---
