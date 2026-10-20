# analysis gradient paired aggregate unify

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gradient_paired_aggregate_unify_20260514T082707_result.json`
- **Structured JSON:** [`0887c155ae3fb10912e3.json`](../../sessions/08/0887c155ae3fb10912e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

### 已更新 11 个实验的 median_difference

**DeepSeek importance（legacy 迁移）：**
| exp_id | median_difference | legacy |
|--------|------------------|--------|
| bf16_importance_s025 | 7.1636 | 222.35 |
| bf16_importance_s030 | 14.5861 | 57.24 |

**Qwen importance：**
| exp_id | median_difference |
|--------|------------------|
| bf16_qw_imp_s015 | 0.0386 |
| bf16_qw_imp_s020 | 0.235 |
| bf16_qw_imp_s025 | 1.268 |
| bf16_qw_imp_s030 | 2.943 |

**Qwen random：**
| exp_id | median_difference |
|--------|------------------|
| bf16_qw_rand_s020 | 0.129 |

**DeepSeek importance rerun (killed)：**
| exp_id | median_difference |
|--------|------------------|
| bf16_ds_imp_s015 | 0.393 |
| bf16_ds_imp_s020 | 1.482 |
| bf16_ds_imp_s025 | 7.164 |
| bf16_ds_imp_s030 | 14.586 |

**已有 median_difference（无需更新）：** bf16_importance_s015 (0.3925), s020 (1.4818), bf16_qw_rand_s015 (0.0497), s025 (0.6598)

**跳过：** bf16_qw_rand_s030（RUNNING，无 profiling 输出）

验证：4 个已知 DeepSeek 正确值全部匹配（s015=0.39✓, s020=1.48✓, s025=7.16✓, s030=14.59✓）。计算方法为 aggregate median，即 `interaction_index.low.median - interaction_index.high.median`。

---
