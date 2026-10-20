# audit main body

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_main_body_20260525T194325_result.json`
- **Structured JSON:** [`d05369663e6a551127bd.json`](../../sessions/d0/d05369663e6a551127bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成，结果保存至 `artifacts/audit_main_body.md`。

**总结**：审计 82 个数字，71 通过，5 个问题，6 个无法从 registry 验证。

**5 个问题**：

1. **method.tex:31** — "2v3 cluster at 0.55--0.59" 下界不准，Pythia/Qwen-base/Qwen-7B 的 2v3 低至 0.544，应改为 ~0.54--0.59
2. **method.tex:72** — OBD MAE "0.984" 在 registry 找不到来源。registry 的 ordinal_mae=1.0163 与 multiclass "1.016" 匹配，但字段名是 "ordinal"，存在标签混淆
3. **method.tex:72** — mean AUC 写 0.6095，registry 是 0.6099（差 0.0004）
4. **discussion.tex:27** — JSD "0.077" 归属 arXiv，但 registry 中该值出自 exp_018 LLaMA-8B **C4** 的 0v1 pair，arXiv 实验无 JSD 数据
5. **discussion.tex:23** — "CI lower 0.593--0.599" 三个 marginal case 的精确 CI 下界需对照 Bonferroni CI 表确认

所有交叉引用（同一数字多处出现）均一致。

---
