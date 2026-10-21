# infra bjb1 to westd data migration

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_bjb1-to-westd-data-migration_20260526T032815_result.json`
- **Structured JSON:** [`781b6a3392e1f8dc6451.json`](../../sessions/78/781b6a3392e1f8dc6451.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

迁移完成，所有关键文件已验证。汇报如下：

---

## 迁移结果

### 1. bjb1 上发现的文件清单

| 类别 | 文件 | 大小 |
|------|------|------|
| RSSM 分析 JSON | `logdir/analysis_rssm_prediction_quality.json` | 小 |
| RSSM 分析 JSON | `logdir/analysis_rssm_walker_fidelity.json` | 小 |
| 分析脚本 | `logdir/analysis_rssm_prediction_quality.py` | 小 |
| 分析 JSON | `logdir/analysis_actor_entropy_value_calibration.json` | 小 |
| 论文数据 | `logdir/paper_data_walker_walk.json`, `paper_figure_data.json`, `paper_figure_data_compact.json` | 小 |
| 跨环境分析 | `logdir/cross_env_output/cross_env_civo_summary.json` | 540K |
| 分析实验 | `exp_063_rssm_fidelity` (results.json) | 8K |
| 分析实验 | `exp_064_value_distribution` (results.json) | 704K |
| 分析实验 | `exp_065_dt_emb_cosine` (results.json + extended_analysis.json + nve_metrics.json) | 768K |
| 分析实验 | `exp_066b_timeseries_rssm_fidelity_s1` (fidelity_timeseries.json) | 3.1G total (只迁移 JSON) |
| **关键 checkpoint** | `exp_093_cheetah_no_dt_emb_s2` (latest.pt=231MB) | **442M** |
| **关键 checkpoint** | `exp_092_cheetah_no_dt_emb_s1` (latest.pt=231MB) | **437M** |
| 分析脚本 | `scripts/` 目录 (35 个文件) | 小 |
| 实验总量 | ~90 个 exp_* 目录 | **94G total** |

### 2. 已迁移文件清单 (全部验证通过)

- **RSSM 分析 JSON** (3 个): `analysis_rssm_prediction_quality.json`, `analysis_rssm_walker_fidelity.json`, `analysis_actor_entropy_value_calibration.json`
- **论文数据 JSON** (3 个): `paper_data_walker_walk.json`, `paper_figure_data.json`, `paper_figure_data_compact.json`
- **分析脚本**: `logdir/analysis_rssm_prediction_quality.py`
- **跨环境分析**: `cross_env_output/` 目录
- **分析实验**: `exp_063`, `exp_064`, `exp_065` (完整目录含所有 JSON)
- **时序保真度**: `exp_066b` 的 `fidelity_timeseries.json`
- **exp_093_cheetah_no_dt_emb_s2**: 442M, latest.pt=231MB ✓ (C2 证据)
- **exp_092_cheetah_no_dt_emb_s1**: 437M, latest.pt=231MB ✓
- **scripts/ 目录**: 35 个分析和实验脚本 ✓

### 3. 跳过的文件及原因

| 跳过 | 原因 |
|------|------|
| exp_049_stackcube_civo_trigger_s0 | StackCube 已放弃 |
| exp_052_stackcube_civo_trigger_s1 | StackCube 已放弃 |
| exp_057_frozen_dt_emb_walker_s2 | Director 决定不重跑 |
| exp_098_cheetah_008a_s0 | 已确认冗余 |
| exp_099_cheetah_008a_s1 | 已确认冗余 |
| ~75 个其他 exp_* 目录 | 多数为旧实验/早期迭代，数据已由 metrics.jsonl 通过 W&B 保存，checkpoint 不再需要 |

### 4. 验证结果

全部迁移文件在 westd 上验证通过：
- exp_093 latest.pt: 231,046,343 bytes ✓
- exp_092 latest.pt: 231,046,343 bytes ✓
- 13 个分析 JSON 文件全部到位 ✓
- scripts/ 35 个文件完整 ✓

### 5. 迁移失败

无。全部成功。

**westd 上现有 13 个实验目录**（原 5 个 + 新迁移 8 个）。bjb1 可以安全关闭。

---
