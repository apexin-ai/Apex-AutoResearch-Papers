# analysis d070 vc rho diff

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d070_vc_rho_diff_20260515T091741_result.json`
- **Structured JSON:** [`73ae0de2620d6aa31f76.json`](../../sessions/73/73ae0de2620d6aa31f76.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/vc_implementation_rho_diff.md` 并注册。

核心结果（Qwen × SciERC seed42，本地验证）：

| Task | ρ\_eq6 | ρ\_majority | Δρ |
|------|--------|-------------|-----|
| NER | 0.3792 | 0.2524 | **+0.1268** |
| RE | 0.3498 | 0.3311 | **+0.0187** |

NER 差异显著（+0.127），因为 majority threshold 丢弃了大量出现 ≤4/8 次的有效 entity；RE 差异很小（+0.019），因为 relation 本身稀疏，两种实现趋同。LLaMA × SciERC 和 CoNLL 配置仅有 Eq.6 版本的 registry 值，majority 版需从服务器 samples.jsonl 重算。

---
