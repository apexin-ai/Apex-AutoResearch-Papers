# analysis cls predictions audit

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cls-predictions-audit_20260519T155146_result.json`
- **Structured JSON:** [`7704d444add0b2360ff5.json`](../../sessions/77/7704d444add0b2360ff5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。以下是完整报告。

---

## 审计报告：`predictions_cls_seed42.jsonl` 与 oracle complementarity 分析

### 1. 文件鉴别

| 属性 | `predictions_cls_seed42.jsonl` (当前文件) | 正确的 CLS s42 | 正确的 CWM s42 |
|------|------|------|------|
| Accuracy | **87.51%** (1654/1890) | 87.83% (1660/1890) | 87.51% (1654/1890) |
| FP rate (PASS→FAIL) | **75.4%** | 56.5% | 70.3% |
| gen_text | 全部为空 (CLS 模式) | — | — |
| Confusion matrix | TP=800, TN=854, FP=58, FN=178 | TP=848, TN=812, FP=100, FN=130 (推导) | TP=812, TN=842, FP=70, FN=166 (推导) |

**结论**：该文件由 CLS 模式模型生成（gen_text 为空），但来自**错误的 checkpoint**。accuracy 巧合地匹配 CWM s42 (87.51%)，但 error pattern (75.4% FP) 与正确的 CLS (56.5%) 和 CWM (70.3%) 均不匹配。它是第三个不同的模型输出。

### 2. 正确的 CLS s42 predictions 文件

- **原始位置**：`home-1x5090:/home/sonny/exec-sim-repair-verifier/eval_cls_seed42_with_preds_predictions.json`
- **当前状态**：**不存在于 seetacloud 服务器**
- **Checkpoint**：Qwen3-4B function-level CLS checkpoint 在 seetacloud 上不存在（已清理或未迁移）
- **重新推理**：**受阻** — 缺少 checkpoint

### 3. Oracle complementarity 分析正确性

`error_overlap_matched_seed.json` **数据正确**（在旧服务器 home-1x5090 上用正确的 JSON 文件计算）：
- seed 42: cls=87.83%, cwm=87.51%, both_correct=1601, cls_only_wrong=53, cwm_only_wrong=59, both_wrong=177
- **Oracle accuracy = 90.63% ✓**
- 聚合：mean oracle = 90.14%, mean complementarity rate = 34.03%

### 4. Error direction narrative 评估

- **"Both FP-dominant"**：正确 — CLS 56.5% + CWM 70.3% 均 over-predict failure
- **"partial complementarity from different fail-bias degrees"**：正确（已从 "opposite patterns" 修正）
- **56.5% 和 70.3% 数值**：与正确的 accuracy 值内部一致，无法用现有文件独立验证

### 5. 论文中的错误数据

**Appendix (e) `appendix.tex:293`** 是核心错误：

| 指标 | 论文声称 (来自 87.51% 文件) | 正确值 (由 87.83% + 56.5% FP 推导) |
|------|------|------|
| Fail Precision | 82.75% | ~86.20% |
| Fail Recall | 93.64% | ~89.04% |
| Fail F1 | 87.86% | ~87.59% |
| 42.1% perfectly predicted | 来自错误文件 | 无法验证 |

反推验证：P=82.75%, R=93.64% → TN=854, FN=178 → accuracy=87.51%，与论文声称的 CLS s42=87.83% 矛盾。

### 6. 受影响文件清单

**论文（需修正）**：
- `docs/paper/appendix.tex:293` — fail F1/P/R 和 "42.1%" 均来自错误数据

**Artifacts（数据完整性）**：
- `artifacts/all_experiments_parsed.json:2382-2403`
- `registry.yaml:628-630, 801`
- `artifacts/paper_materials.md:176`
- `artifacts/comprehensive_results_summary.md:41`
- `paper_provenance.yaml:562`

### 7. 修复路径

**选项 A（最佳）**：找到 Qwen3-4B function-level CLS seed 42 checkpoint，重新推理生成正确 predictions，重算所有指标。

**选项 B（备选）**：接受从 overlap 分析推导的 confusion matrix（87.83%, 56.5% FP → TP=848, TN=812, FP=100, FN=130），更新 appendix (e) 为推导值，标注 "42.1% perfectly predicted" 无法验证并删除。

**Checkpoint 搜索结果**：seetacloud 上无 Qwen3-4B func-level CLS 相关 checkpoint（`checkpoints_repo_cls/` 目录为空，无 `*qwen*4b*cls*func*` 目录）。需确认旧服务器 home-1x5090 是否还能访问，或是否有备份。

---
