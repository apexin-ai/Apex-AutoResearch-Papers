# analysis error taxonomy cross model

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_error_taxonomy_cross_model_20260522T001403_result.json`
- **Structured JSON:** [`05ffb8a3fbf0472c518e.json`](../../sessions/05/05ffb8a3fbf0472c518e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果汇总：

| Model | N_batch | BCS range | ρ | p | IntraSub Low→High |
|-------|---------|-----------|------|-------|-------------------|
| Qwen3-32B (ref) | 154 | — | **0.954** | <0.001 | — |
| LLaMA-8B | 54 | [0.47, 0.97] | **0.430** | 0.001 | 16.0% → 29.0% |
| LLaMA-70B | 20 | [0.47, 0.97] | -0.086 | 0.719 | 16.2% → 14.8% |
| Gemini Flash | 60 | [0.36, 0.97] | **0.821** | <0.001 | 0.7% → 18.4% |

**关键发现：**

- **Gemini Flash 强确认**（ρ=0.821, p<10⁻¹⁵），IntraSub 从 low-BCS 的 0.7% 飙升到 high-BCS 的 18.4%
- **LLaMA-8B 显著正相关**（ρ=0.430, p=0.001），但 random batch 的 BCS 方差大导致 ρ 不如 Qwen3
- **LLaMA-70B 不可解读**：仅 20 batches，missed rate 高达 17.4%（模型大量输出 "none"），且 BCS 在 low/high group 内高度聚集（排除 outlier 后实际 BCS 对比仅 0.47-0.60），统计功效不足

**结论：** 3/4 个有足够 BCS 变异的模型都确认了 IntraSub-BCS 正相关，不是 single-model artifact。LLaMA-70B 的负面结果是实验设计（batch 数和 BCS 对比度不足 + 高 missed rate）的局限，而非否定 finding。

输出文件：
- JSON: `artifacts/error_taxonomy_cross_model.json`
- LaTeX: `artifacts/error_taxonomy_cross_model_table.tex`
- 服务器脚本: `/root/schema-dag-extraction/src/cross_model_error_taxonomy.py`

---
