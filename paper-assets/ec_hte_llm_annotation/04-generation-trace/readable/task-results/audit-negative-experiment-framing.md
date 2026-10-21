# audit negative experiment framing

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_negative-experiment-framing_20260524T075928_result.json`
- **Structured JSON:** [`5e2c5bf6008a1a696a83.json`](../../sessions/5e/5e2c5bf6008a1a696a83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。所有 6 个阴性/killed 实验在论文中都有诚实充分的讨论，无需补充。

关键发现：
- **exp-015/016**（real CM 失败）：主文给出 operating conditions（FNR<0.5, K≤4），Appendix 有完整 root cause 分析和 applicability frontier 图
- **exp-030/033**（K=8 boundary）：主文、limitations、Appendix 三处覆盖，明确承认 scalability boundary
- **exp-028**（非对称 diagnostic 退化）：theory.tex Remark 2 中 reframe 为理论便利性，framing 合理
- **exp-007b**（killed）：无需提及，PPCI composition 讨论完整

唯一潜在弱点是 exp-015/016 完整 root cause 只在 Appendix，主文措辞较间接，但符合顶会惯例。

产出已写入 `artifacts/negative_experiment_framing_audit.md`。

---
