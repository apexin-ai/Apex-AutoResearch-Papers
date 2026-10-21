# research seed comparison prep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_seed_comparison_prep_20260516T060550_result.json`
- **Structured JSON:** [`40ff2430b02af823f10a.json`](../../sessions/40/40ff2430b02af823f10a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本运行正常。

产出：
- **`/root/autodl-tmp/freige/seed_comparison.py`** — paired t-test 分析脚本，已验证可执行
- 当前有 2 对 paired seeds (s43, s45)，CED s42/s44 和 flat-NLI s42/s43 reeval 仍在跑
- 所有 4 个指标 (Rel-F1, Ign-F1, Evi-F1, EDCR) 均无显著差异 (p > 0.6)，但 n=2 统计效力极低，等 4 seeds 齐全再看
- `--latex` 生成可直接粘贴到论文的 LaTeX 表格，显著指标自动加粗
- D076 协议校验内置，batch_size/quantize/max_new_tokens 不符会报 warning

---
