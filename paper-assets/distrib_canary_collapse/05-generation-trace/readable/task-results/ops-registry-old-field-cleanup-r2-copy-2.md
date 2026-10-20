# ops registry old field cleanup r2

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_registry_old_field_cleanup_r2_20260520T220005_result.json`
- **Structured JSON:** [`07e24fc43a024d3b6b62.json`](../../sessions/07/07e24fc43a024d3b6b62.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`a060_s43` 实际是 `alpha_sweep_a060_s43_fp32`，且它没有 `consensus_k3_3sigma` 字段（初始 grep 就没找到该字段名）。用户提到的这个字段可能已在之前的清理中删除了，或从未存在于 registry 中。

**汇总：**

| 操作 | 数量 |
|------|------|
| 删除的字段实例 | **30** |
| 影响的实验 | **26** |
| 残留旧字段 | **0** |

删除的字段类型：
- `ty_granger` 系列（ty_granger, ty_granger_fwd, ty_granger_forward, ty_granger_sig, TY_granger, TY_granger_fwd, TY_Granger_fwd, TY_Granger_rev）— 20 个实例
- `K_ge3` 系列（K_ge3_3sigma, K_ge3_D116, K_ge3_rates, previous_K_ge3）— 6 个实例
- `K_ge4` 系列（K_ge4_3sigma, K_ge4_D116, K_ge4_rates）— 4 个实例
- `consensus_k3_3sigma` — 未在 registry 中找到，可能已在 Round 1 清理或从未写入

---
