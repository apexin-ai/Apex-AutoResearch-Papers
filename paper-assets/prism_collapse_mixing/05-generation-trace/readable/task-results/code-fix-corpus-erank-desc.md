# code fix corpus erank desc

**prism collapse mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_corpus_erank_desc_20260516T020037_result.json`
- **Structured JSON:** [`c59b4cc9f062ed2dd222.json`](../../sessions/c5/c59b4cc9f062ed2dd222.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

§3.2.4 已修改。改动内容：

1. 删除了 "using the same formula as §3.2.2"
2. 写出了显式公式，明确使用 eigenvalues λ_i（而非 singular values σ_i）
3. 说明 mean-pool 是对 token positions 取平均
4. 列出与 §3.2.2 的两点区别：(a) inter-example Gram matrix vs intra-sequence hidden-state matrix；(b) eigenvalues λ_i of G (= σ_i² of H_corpus) vs singular values directly
5. 所有描述均来自 `compute_signals.py` 第 115-132 行的实际代码

---
