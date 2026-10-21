# ops registry old field cleanup r2

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_registry_old_field_cleanup_r2_20260520T215155_result.json`
- **Structured JSON:** [`67e984b66310cd5551b8.json`](../../sessions/67/67e984b66310cd5551b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证通过，所有旧字段已清零。

## 清理报告

| 实验 | 删除字段 | 旧值 |
|------|---------|------|
| **alpha_sweep_a060_s43_fp32** (优先) | consensus_k3_3sigma | **7/8** (与 consensus_ge3=0 严重冲突) |
| | ty_granger | 4/8 |
| alpha_sweep_a030_s42_fp32 | k_ge3, k_ge4, ty_granger | 3/8, 3/8, 5/8 |
| alpha_sweep_a035_s42_fp32 | TY_granger | 4/8 |
| alpha_sweep_a040_s42_fp32_v2 | TY_granger | 4/8 |
| alpha_sweep_a045_s42_fp32 | k_ge3, k_ge4, ty_granger | 3, 0, 1 |
| alpha_sweep_a045_s43_fp32 | ty_granger | 7/8 |
| alpha_sweep_a050_s43_fp32 | TY_granger | 5/8 |
| alpha_sweep_a060_s42_fp32_v4 | TY_granger | 0/8 |
| alpha_sweep_a075_s43 | TY_granger | 6/8 |
| c4_a025_s42_fp32 | TY_granger | N/A (API error) |
| c4_a050_s42_fp32 | TY_granger | N/A (API error) |
| c4_a050_s43_fp32 | TY_granger | 0/8 |
| c4_a075_s42_fp32 | TY_granger | N/A (API error) |
| c4_a075_s43_fp32 | TY_granger | 1/8 |
| padding_robustness_a100_s42_fp32 | TY_granger | N/A (API error) |
| qwen35_08b_wiki_a100_s42_v2 | TY_granger, K_ge3, K_ge4 | 6/8, 6/8, 3/8 |
| qwen35_08b_wiki_a100_s43_fp32 | TY_granger, K_ge3, K_ge4 | 6/8, 6/8, 6/8 |
| scale_14b_a050_s42_fp32 | TY_Granger, K_ge3, K_ge4 | 0/8, 0/8, 0/8 |
| scale_14b_c4_s42_fp32 | TY_granger, K_ge3, K_ge4 | 0/8, 8/8, 0/8 |
| scale_69b_a100_s42 | TY_granger, K_ge3, K_ge4 | 1/8, 5/8, 0/8 |
| scale_69b_a100_s43 | TY_granger, K_ge3, K_ge4 | 0/8, 6/8, 0/8 |
| smollm3_3b_wiki_a100_s42_v3 | ty_granger | 0/8 |
| smollm3_3b_wiki_a100_s43_fp32 | TY_Granger, K_ge3, K_ge4 | 6/8, 6/8, 3/8 |
| t20_a060_s42_fp32 | K_ge3 | 4/8 |
| t20_a075_s42_fp32 | TY_Granger, K_ge3 | 5/8, 6/8 |

**总计：25 个实验、45 个旧字段已清理**（比预估多 — 大小写变体 `TY_granger`/`TY_Granger` 扩大了范围）。验证确认 registry 中不再有任何 `ty_granger`/`K_ge3`/`K_ge4`/`consensus_k3_3sigma` 残留。

---
