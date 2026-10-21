# analysis extract remaining conflict rate

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_extract_remaining_conflict_rate_20260524T144639_result.json`
- **Structured JSON:** [`2b0bdb309b6357ad4995.json`](../../sessions/2b/2b0bdb309b6357ad4995.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总如下：

### 数据可用性

| 条件 | 数据文件 | conflict_rate | cosine_sim | aux_grad_norm | action_grad_norm | 行数 |
|------|---------|---------------|------------|---------------|------------------|------|
| **Vanilla_s0** | 有 | 无 | 无 | 无 | 有 | 49 |
| **Full_OCC_s0** | 有 | 有 | 有 | 有 | 有 | 49 |
| **Detach_BN_s2** | 有 | 无 | 无 | 无 | 有 | 49 |
| **Detach_LN_s0** | **无文件** | — | — | — | — | 0 |
| **Random_s2** | 有 | 有 | 有 | 有 | 有 | 49 |

### 原因

- **Vanilla_s0**：无 aux head，只采集了 action gradient norm，无法计算 conflict rate
- **Detach_BN_s2**：`occ_detach=true`，aux gradient 被 detach 阻断，不流经 backbone 层，分析脚本只记录了 action gradient norm
- **Detach_LN_s0**：数据文件完全缺失，确认之前 BN/LN mismatch 导致脚本崩溃未产生输出

### 输出文件

- 服务器：`/root/occsafe_vla/artifacts/gradient_analysis_mixed_seed/per_layer_conflict_rate_full.csv`（196 行数据）
- 本地：`artifacts/gradient_analysis/per_layer_conflict_rate_full.csv`

CSV 格式与原 `per_layer_conflict_rate.csv` 一致，Vanilla_s0 和 Detach_BN_s2 的 conflict_rate/cosine_sim/aux_grad_norm 列为空值。

---
