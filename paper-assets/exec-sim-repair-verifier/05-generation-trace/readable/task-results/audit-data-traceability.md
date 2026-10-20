# audit data traceability

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_data-traceability_20260523T191629_result.json`
- **Structured JSON:** [`9477f5385d989b361096.json`](../../sessions/94/9477f5385d989b361096.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。结果写入 `artifacts/data_audit_results.md`。

**核心结论**：绝大多数数据（~50个数字/统计量）与 registry 和 artifact 完全一致。

**需要处理的 2 个问题**：

1. **⚠️ §4.1 "CLS-TRAJ gap <1pp on Qwen3"** — Table 1 per-test gap 是 2.13pp，不是 <1pp。"<1pp" 来自 variant-level TOST gap (−0.45pp)，但同一句话里 DeepSeek 的 2.69pp 是 per-test level。比较层级不一致，建议修正。

2. **⚠️ DeepSeek 0-shot 63.00 vs 63.02** — registry 值为 0.6302 → 63.02%，论文写 63.00%。差 0.02pp。

**无法追溯的 4 项**：z=−23.7（LPM 交互项）、p=0.0066（8B scaling bootstrap）、DeepSeek LLM-judge 56.56%、DeepSeek 3-shot 59.95% — 这些可能在未列出的实验中，建议补存 artifact JSON。

---
