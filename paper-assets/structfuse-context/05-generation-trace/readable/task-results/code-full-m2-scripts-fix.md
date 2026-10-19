# code full m2 scripts fix

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_full-m2-scripts-fix_20260513T104929_result.json`
- **Structured JSON:** [`8462c5cc537b2f77894a.json`](../../sessions/84/8462c5cc537b2f77894a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修复完成。汇总：

## 改动清单

### bjb1-42106 服务器
| 文件 | 改动 |
|------|------|
| `/root/structfuse/scripts/migrate_m1_data.sh` | `DST_DIR` 从 `m1_full_data` → `full_m1_data`，与训练脚本一致 |
| `/root/structfuse/results/pilot_results_summary.md` | StarCoder random 行补全: val_loss=0.5113, R@1=0.4922, R@5=0.98, R@10=1.0；cross-model 表加入 StarCoder random 行；notes 更新 |
| `/root/structfuse/results/pilot_results.json` | StarCoder random 的 `best_step`=500, `best_metrics` 已填入 |

### 本地 artifacts/full_m2/
| 文件 | 改动 |
|------|------|
| `run_full_m2_training.sh:25` | 清理过期注释（移除 CUDA_VISIBLE_DEVICES 硬编码说明） |
| `run_full_m2_training.sh:44` | DATA_DIR → `full_m2_training_data`（配合 data prep 流程） |
| `run_full_m2_training.sh:46-47` | 文件名加 seed 后缀: `train_{strategy}_s{seed}.jsonl`, `val_{strategy}_s{seed}.jsonl` |
| `run_full_m2_training.sh:106` | 加入 `--early-stopping-patience 3` |
| `build_full_m2_data.sh` | **新建** — 3 seeds × 3 strategies 数据构建，含策略名映射 (embedding→embedding_distance, dataflow→dataflow_aware) |
| `schedule_m2_runs.sh:24-50` | 新增 Phase 0 data prep 阶段，已有数据时跳过 |

### Task 4 确认
train.py 头 30 行无任何 CUDA_VISIBLE_DEVICES 相关代码或注释，确认干净。

---
