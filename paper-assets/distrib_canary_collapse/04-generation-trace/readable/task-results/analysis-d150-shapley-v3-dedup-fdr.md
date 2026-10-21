# analysis d150 shapley v3 dedup fdr

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236_result.json`
- **Structured JSON:** [`dd49aa48de79369908bd.json`](../../sessions/dd/dd49aa48de79369908bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All checks pass. Here's the summary:

**Shapley v3 完成。**

**修复内容：**
- **排除 4 个非标准变体**: `a005_s42_fp32_v3_d080`, `a060_s42_fp32_v3_d080`, `a050_postd093_s42_fp32`, `gpt2m_wiki_a100_s43_bf16`
- **去重 8 个 alpha_sweep 条目**: 同一 (dataset, alpha, seed) 保留 17855 fp32 版本（含 α=0.00 s42 去重）
- **FDR 字段已验证**: 4 个 p-value 方法使用 `significant_fdr`，threshold_onset 使用 `significant`（确定性，无 p-value）

**数据规模变化**: 60 → 48 experiments, null 4→3, signal 56→45

**验证通过**:
- 无 v3_d080/postd093/bf16 污染
- α=0.00 s42 仅 1 条（17855 fp32）
- perm_granger FPR Shapley = 0.000（raw 0/24）
- Shapley sum 精确匹配 grand coalition

**输出文件**:
- `artifacts/shapley_v2/shapley_values_v2.json` — 已覆盖为 v3 内容
- `artifacts/shapley_v2/shapley_method_contribution.pdf` — 已重画

---
