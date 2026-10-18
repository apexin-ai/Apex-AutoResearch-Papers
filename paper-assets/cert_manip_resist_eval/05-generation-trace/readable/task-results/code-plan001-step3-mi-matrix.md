# code plan001 step3 mi matrix

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan001-step3-mi-matrix_20260522T075635_result.json`
- **Structured JSON:** [`546b402c91cff6d97877.json`](../../sessions/54/546b402c91cff6d97877.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本已写好并通过 syntax check + import 验证：

**脚本 1** `run_plan001_step3_mi_matrix.py`:
- 从 `_step2v3_checkpoint.json` / `_taxonomy_checkpoint.json` 加载 6 本地模型 clean scores
- 从 `plan001/individual_scores/{model}__{ds}__clean.json` 加载 9 API 模型 clean scores
- 用 `sklearn.metrics.mutual_info_score` 计算 15×15 pairwise MI 矩阵（每 dataset 一个）
- 枚举 C(15,3)=455 panels 计算 MI-based K_eff
- 输出 → `plan001/mi_matrix/mi_matrix_15models.json`

**脚本 2** `run_plan001_confound_diagnosis.py`:
- 读取 MI 矩阵 + 各模型 individual ASR（本地从 checkpoint 计算，API 从 score 文件读 `asr` 字段）
- 对 12 个 condition（2 dataset × 6 attack），枚举所有可用 panels，计算 K_eff vs η_max 的 Pearson r
- 自动判定 `CONFOUND_SEVERE` / `CONFOUND_MODERATE` / `CONFOUND_BROKEN`
- 生成 scatter grid 图 → `confound_scatter.png`
- 输出 → `confound_diagnosis.json`

缺失数据（API scores 未就绪）会 graceful skip，不会 crash。Step 1 完成后可直接顺序运行。

---
