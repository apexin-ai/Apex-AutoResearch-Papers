# code plan 013 q3

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_013_q3_20260520T221944_result.json`
- **Structured JSON:** [`18fb4960ec46ba4a3dee.json`](../../sessions/18/18fb4960ec46ba4a3dee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Plan 013 完成。核心发现：

**Q3 均值层面局部依赖很温和**：within-subject mean Q3 = 0.009，cross-subject = 0.003，差异仅 0.006。

**但尾部效应显著**：11.3% 的 within-subject pairs 超过 |Q3| > 0.20 阈值，而 cross-subject 仅 2.2%（5 倍差异，Mann-Whitney p = 2.3e-9）。这说明同一 subject 内存在一批高度局部依赖的 item 对。

**按 subject 分布不均**：
- 最严重的是 moral_scenarios（34.2% pairs 超阈值），其次是 world_religions（18.0%）、marketing（17.5%）
- 最轻的是 college_computer_science（7.7%）、professional_accounting（8.7%）

**对 31% baseline FPR 的解释力**：局部依赖确实存在且 within-subject 显著高于 cross-subject，但均值层面温和（Δ=0.006），不太可能单独解释 31% FPR。更可能是与多维性等其他因素共同作用。报告建议考虑 bifactor/testlet 模型来处理 subject-level clustering。

---
