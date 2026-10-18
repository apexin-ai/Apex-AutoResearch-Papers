# fix matrix analysis warnings

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_matrix_analysis_warnings_20260515T021640_result.json`
- **Structured JSON:** [`3256748d898534ec2e4e.json`](../../sessions/32/3256748d898534ec2e4e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三项修复全部完成。验证总结：

**Fix 1** — Feature importance 声明修正：
- 无 "top-3 Jaccard=1.0" 声明（`grep -n "top-3"` 只出现在偏差注释中）
- Section 5.1 改为 "consistently rank in top-5"
- 添加了 Pythia mean_ppl 和 GPT-2 XL temp09 var_surprisal 的偏差说明

**Fix 2** — EDD 矩阵：
- Section 4 包含完整 EDD 分析：8-cell 矩阵（threshold=0.80）、top-k 降低 EDD 的解释、4 档 threshold sensitivity 全表

**Fix 3** — atlas_v2_data.json 同步：
- `olmo_topk50` 无 placeholder（原本就已有完整分类指标）
- 补充了 `acc_3class_filtered`、`d1v2_auc`、`finetune_loss`、`code_contamination_narrow` 四个字段
- `atlas_v2_complete.py` 已重跑，派生文件（edd_sensitivity.json, cross_model_rank, atlas_v2_results.json）均已更新

---
