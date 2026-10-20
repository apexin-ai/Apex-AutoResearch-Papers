# paper w5 composability w1 analytical

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_w5_composability_w1_analytical_20260515T170813_result.json`
- **Structured JSON:** [`9b776de704d3c6dd9171.json`](../../sessions/9b/9b776de704d3c6dd9171.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

LaTeX compiles cleanly (20 pages, 0 errors).

## 完成内容

**Task 1 — Composability 2×2 Matrix** (`section5_scierc_draft.tex` §5.5)
- 扩展 `tab:composability`：增加 E-F1 列 + ΔDR 列（-94% / -100%）
- 重写 prose：分两段，第一段陈述 Claim 3（fine-tuning 与 OntoCoDec orthogonal axes），第二段两个 secondary observations (CF 88% drop + 1 个 Evaluate-for→Used-for redirection)
- 标注 exp_ids: `w5_lora_scierc_unconstrained_eval`, `w5_lora_scierc_constrained_eval`, `phase2_scierc_unconstrained`, `phase2_scierc_full_s1`
- 强度限制："This validates Claim 3 **on SciERC**"，明确 "one dataset and one fine-tuning method"，未声明 "consistently"
- 残余 DR per-relation (Evaluate-for 13.13%, Part-of 5.77%, Compare 5.00%) 保留并指向 `app:lora-per-relation`

**Task 2 — CF Fallback Analytical Finding** (`appendix_discussion.tex` `app:cf-dr-tradeoff`)
- 第 1 段：承认 CF 是 OntoCoDec 当前最突出残余局限（zero-shot 9.90% on SciERC, up to 12.02% on Llama DocRED）
- 第 2 段：pilot 表格 + 数据（DR 0.93→14.78pp, CF 9.90→0.04pp, 净增 +3.99pp, $f_{gf}$=36.64%），明确 "re-routing" 不是 reduction
- 第 3 段：解释 CF↔DR 根本张力机制（per-relation independent enforcement 只能 allocate priority），并指出 full S1 sits near Pareto frontier；63.3% CF 来自 Generic catch-all 是 schema-level ambiguity
- 第 4 段：新增**两条 alternative paths** — (i) 降低 baseline conflict rate（LoRA composition 在 SciERC 上 CF -88%，empirically validated on one dataset），(ii) global type consensus（future work）
- 标注 pilot exp_id `w1_cf_fallback_scierc_pilot`，未来路径数据 `w5_lora_scierc_constrained_eval`
- 未 cherry-pick：明示 LoRA 路径仅在 SciERC 单数据集验证

---
