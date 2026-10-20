# analysis systematic nocuity

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_systematic_nocuity_20260522T155014_result.json`
- **Structured JSON:** [`c12684822cd89b8332dd.json`](../../sessions/c1/c12684822cd89b8332dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。两个产出文件已生成：

**`analysis_systematic_nocuity.json`** — 完整结构化数据
**`analysis_systematic_nocuity_summary.md`** — 可读报告

关键发现：

1. **Convergence distribution** 验证论文数据：13.0% universal (39), 41.3% majority+ (124/300)

2. **Per-type**: incompleteness universal rate 最高 (24%), Fisher exact test vs 其他类型 OR=2.61, p=0.019，显著。排名：incompleteness > lexical=scopal (16%) > auth_scope (10%) > conditional_precedence=coreferential (6%)

3. **Linguistic comparison** (39 universal vs 84 safe):
   - **compression_ratio** 最显著 (p=0.001): universal clauses 更压缩 (0.40 vs 0.53)，即 ambiguous 版本相对 unambiguous 丢失了更多信息
   - **token_delta** 显著 (p=0.011): universal clauses 的 unambiguous-ambiguous 差值更大 (26.5 vs 20.2 tokens)
   - conditional/negation 词数无显著差异

4. **Mechanism convergence**: 124 个 majority-convergent clauses 中，41.9% (52) 的 failure mode 完全一致，83.9% (104) 至少 partial 一致（≥60% 同一 failure mode）。支持 "systematic nocuity = same incorrect interpretation" 论点。

5. **Per-model**: 所有模型在 universal clauses 上 violation rate = 100%；在 majority clauses 上 deepseek-v3 最高 (78.8%)，claude-sonnet-4-6 最低 (42.4%)。

---
