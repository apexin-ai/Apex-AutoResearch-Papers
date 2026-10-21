# theory scb proposition proof

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_theory_scb-proposition-proof_20260523T010508_result.json`
- **Structured JSON:** [`3cb029a6fdc9c4babb1a.json`](../../sessions/3c/3cb029a6fdc9c4babb1a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入。核心结构：

**Part (i) — Voting Degeneration:** 在 source attribution σ(c_i, a) = **1**[a_i = a] 下，score(a) = n_a，与 majority voting 完全等价。BR = n_â / max_{a'≠â} n_{a'} ≥ 1 是确定性结论（every realization），不仅仅是期望意义。

**Part (ii) — Information Ceiling:** C = f(T) 形成 Markov chain Y—T—C，DPI 给出 I(C;Y) ≤ I(T;Y)。条件版本 I(C;Y|A) ≤ I(T;Y|A) 说明即使已知答案，约束也无法提供超出 trace 本身的独立验证信号。

**Remark** 诚实处理了 semantic attribution 的边界情况：此时需要 answer alignment 假设（经验上成立，但非纯结构保证）。由于 SICA 实际使用 source attribution，主命题无条件成立。

证明只依赖 A1（a_i = h(t_i)）和 A2（c_i = f(t_i)），不需要 A3（answer-aware）。文件末尾的 author note 预判了 6 个潜在 reviewer pushback 点（包括 deduplication caveat 和"too trivial"反驳）。

产出：`artifacts/proposition1_scb_proof.tex`

---
