# audit experiments tables

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_experiments_tables_20260525T194345_result.json`
- **Structured JSON:** [`cc1f5ebe4bb5ec5be307.json`](../../sessions/cc/cc1f5ebe4bb5ec5be307.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。~340 个数字已验证，报告保存在 `artifacts/audit_experiments_tables.md`。

**核心发现：**

1. **❌ 需修正** — `experiments_c1.tex:56` 声称 "> 0.99 at ≤1.5B" 不准确。仅 Qwen-rw (0.9956) 和 Qwen-cont (0.9972) 超过 0.99；Pythia=0.9722、OLMo=0.9861、Qwen-base=0.9870、Gemma=0.9534 均不满足。建议改为 "> 0.99 for Qwen-1.5B" 或 "> 0.97"。

2. **⚠️ 表间不一致** — Wiki Qwen-1.5B 的 K\* 在 `tab_domain_model_kstar` 中报 1（controlled），在 `tab_domain_kstar`（正文内表格）中报 2（raw）。同一模型+domain 出现两个不同 K\* 值，reviewer 会注意到。

3. **⚠️ 表间不一致** — arXiv Qwen-1.5B 2v3 AUC 在 full table 中为 0.6427，在 in-text table 中为 .644；arXiv Pythia 2v3 在 full table 为 0.6545，in-text 为 .648。两个表使用了不同 source experiment。

**整体评估**: tab_filtering_main、tab_alpha_sweep、tab_crossscorer、tab_pairwise_significance 全部精确匹配。~97% 的数字完全正确或在合理 rounding 范围内。3 个需修正的问题中仅 #1 属于 substantive claim error。

---
