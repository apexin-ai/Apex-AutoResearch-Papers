# research proofwriter oracle feasibility

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_proofwriter-oracle-feasibility_20260518T031530_result.json`
- **Structured JSON:** [`42fd083e65cba643cc4d.json`](../../sessions/42/42fd083e65cba643cc4d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `/root/symb_invariant_consensus/analysis/proofwriter_oracle_feasibility.md`。

**核心结论**: 完全可行，且比 FOLIO 更简单。

关键发现:
- ProofWriter 原始 JSONL 有 `raw_logic_programs` 字段，是高度结构化的 DSL（`Pred(x, True) && Pred(y, True) >>> Pred(z, True)` 格式），比 FOLIO 的 Unicode FOL 更规则
- 已有全部 600 题的 Qwen-14B K=12 traces（在 `sica_expanded_14b.json` 中）
- `prepare_full.py` 转换时丢弃了这个字段，需要补回来或直接从原始 JSONL 加载

**推荐路径**: 写一个 ~150 行的 `ProofWriterDSLToZ3` parser 直接解析 DSL → Z3，不需要 LLM。DSL 语法完全规则，四种模式（一元/二元 × 有/无否定）都可确定性解析。

**预估工作量**: 4-6 小时，主要是 parser 编写 + 单元测试。风险可控，最大的不确定性是 D5 深度推理链的 Z3 求解时间，但 FOLIO 实验 solver error rate 为 0。

---
