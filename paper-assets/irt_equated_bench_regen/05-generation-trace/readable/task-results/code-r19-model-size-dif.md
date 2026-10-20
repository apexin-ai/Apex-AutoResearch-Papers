# code r19 model size dif

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r19_model_size_dif_20260522T184744_result.json`
- **Structured JSON:** [`2188c2102a870ad6d36b.json`](../../sessions/21/2188c2102a870ad6d36b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有产出已生成，核心结果：

| Group | N_ref/N_foc | C% | 方向偏向 | ρ(difficulty, Δ_MH) |
|-------|-------------|------|---------|---------------------|
| Small | 55/114 | **11.14%** | 均衡 (719R/674F) | +0.251 |
| Medium | 713/429 | **48.25%** | Focal偏↑ (2693R/3342F) | −0.476 |
| Large | 92/115 | **26.36%** | Focal偏↑ (1207R/2090F) | −0.430 |

关键发现：
- **DIF 随模型规模递增**：Small 11% → Large 26% → Medium 48%（Medium 最高可能因样本量最大带来的统计功效）
- **方向差异**：Small 组 DIF 方向近乎对称；Medium/Large 都 focal(2024)-favoring，说明较大模型的 2024 代在某些题上有系统性优势
- **ρ 翻转**：Small 组难度-DIF 正相关（+0.25，难题对 2023 有利），Medium/Large 负相关（−0.43~−0.48，难题对 2024 有利）
- **跨组重叠极低**：Jaccard 仅 0.086–0.245，不同规模模型触发 DIF 的 item 集合基本不同

输出文件：
- `artifacts/r19_model_size_dif/model_size_dif_analysis.py`
- `artifacts/r19_model_size_dif/model_size_dif_report.md`
- `artifacts/r19_model_size_dif/model_size_classification.csv`
- `artifacts/r19_model_size_dif/model_size_results.csv`

---
