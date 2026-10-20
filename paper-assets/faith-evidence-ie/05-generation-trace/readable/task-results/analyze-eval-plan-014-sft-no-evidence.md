# analyze eval plan 014 sft no evidence

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_plan_014_sft_no_evidence_20260515T183104_result.json`
- **Structured JSON:** [`f3a8f72671893fb07c19.json`](../../sessions/f3/f3a8f72671893fb07c19.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Eval Plan 014: SFT No-Evidence 结果

### 核心指标

| Metric | SFT w/ Evidence | SFT No-Evidence | Delta |
|--------|----------------|-----------------|-------|
| **rel_f1** | 0.4057 | **0.4893** | **+0.0836 (+20.6%)** |
| precision | — | 0.4884 | — |
| recall | — | 0.4902 | — |
| evi_f1 | 0.7979 | 0.0 | N/A (无 evidence 输出) |
| EDCR | 0.7118 | 0.0 | N/A |
| pred_count (dedup) | 12,234 | 12,196 | ~持平 |
| format_ok | — | 99.2% | — |
| truncated | — | 298/985 (30.3%) | — |

### 跨方法对比 (rel_f1)

| Method | rel_f1 |
|--------|--------|
| LMRC (纯抽取) | ~0.607 |
| **SFT No-Evidence** | **0.4893** |
| RSFT CED 3-seed | 0.4596±0.013 |
| SFT w/ Evidence | 0.4057 |

### 结论

1. **Evidence generation 代价量化**: 去掉 evidence 后 rel_f1 提升 +0.0836（相对 +20.6%），确认 evidence 生成是显著性能负担。模型在有限 token budget 内同时做抽取+溯源，抽取质量被拖累。

2. **SFT No-Evidence > RSFT CED**: 仅去掉 evidence（不用 reward shaping）就达 0.4893，超过 RSFT CED 的 0.4596。evidence 开销 > reward shaping 增益。

3. **与 LMRC 差距 ~0.118**: 仍有不小差距，可能来源于 30.3% 截断率（max_new_tokens=1024 不足）和模型/数据差异。

4. **Truncation 是瓶颈**: 近三分之一文档被截断，recall 可能被压低，增大 max_new_tokens 值得尝试。

报告已存入 `memory.md`。

---
