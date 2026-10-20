# code d027 alpha050 method desc fix

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d027_alpha050_method_desc_fix_20260515T111714_result.json`
- **Structured JSON:** [`9044d6e3227c31a38c2e.json`](../../sessions/90/9044d6e3227c31a38c2e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成。总结：

### 修改内容

**d027_report.md** — 2 处修正：
1. **Line 157 表格行**：`仅 naive_xcorr 通过` → 明确列出 3/5 方法通过（naive, differenced, threshold），2/5 归零（permG, TY），未达 ≥4/5 共识
2. **Line 164 发现描述**：`唯一在 α=0.50 通过的方法是 naive_pearson，严格方法（differenced_xcorr, TY, permG）全部归零` → 修正为 3/5 correlation/rule-based 方法通过 vs 2/5 因果检验方法归零

**paper_framing.md** — 2 处修正：
1. **Constraint #21**：删除了将 differenced_xcorr 归入"严格方法"的错误分类（原文 `differenced 0/8` 与事实 `differenced 8/8` 矛盾），修正术语为"因果检验方法"（仅 TY, permG）
2. **Constraint #22**：`naive_xcorr 100% sig vs strict 0% sig` → `correlation/rule-based 方法 100% sig vs 因果检验方法 0% sig`

**consensus_framework.md** — 无需修改。两个副本（`artifacts/consensus_framework/` 和 `artifacts/_project/report/`）内容一致，术语使用正确（§6.1 line 225 "the two strict methods (permG, TY)" 仅指因果方法）。

### 术语统一结果
所有修改后的文件统一使用：
- **correlation/rule-based 方法**：naive_pearson, differenced_xcorr, threshold_onset
- **因果检验方法（causal methods）**：permutation_granger, toda_yamamoto
- "严格方法"/"strict methods" 不再用于指代 differenced_xcorr

---
