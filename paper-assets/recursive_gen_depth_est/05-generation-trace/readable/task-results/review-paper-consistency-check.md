# review paper consistency check

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_review_paper_consistency_check_20260516T052059_result.json`
- **Structured JSON:** [`020ac9d370629311be55.json`](../../sessions/02/020ac9d370629311be55.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**结论：PASS**

### 引用验证
| Bib Key | 状态 | 说明 |
|---------|------|------|
| `knowledge_collapse2025` | VERIFIED | arXiv:2509.04796, 作者 Figarri Keisha 等, 2025-09-05. 真实论文, 姓名格式为 surname-first |
| `falahati2026_curated` | VERIFIED | arXiv:2605.07724, 作者 Ali Falahati, 2026-05-08. 真实论文 |

### Metrics 一致性
- **157 个定量 claim 全部通过**, 跨 28 个 registry 实验、8 个 tex 文件
- **0 个 critical mismatch**
- 所有数值差异均在 ±0.1pp 四舍五入范围内

验证覆盖范围:
- 3×3 accuracy matrix (18 cells) ✓
- EDD=4 determination + bootstrap p-values ✓
- Cross-model LOO mean 66.4% + per-model breakdowns ✓
- Cross-strategy LOO mean 59.1% + 9 holdout cells ✓
- Baseline battery (6 methods) ✓
- Zero-shot LLM (DeepSeek 36.2%, Qwen 30.4%) ✓
- End-to-end finetuning (DeBERTa 58.3%, RoBERTa 59.5%) ✓
- Wild data FPR (4.7%–22.4%) ✓
- Multi-tau ablation (20 values) ✓
- Downstream curation (15 values) ✓
- Feature importance SHAP (6 values) ✓

报告已写入 `artifacts/paper_consistency_check.json` 并注册。

---
