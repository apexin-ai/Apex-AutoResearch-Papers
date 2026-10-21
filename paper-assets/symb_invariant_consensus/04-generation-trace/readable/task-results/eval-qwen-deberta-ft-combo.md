# eval qwen deberta ft combo

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_qwen-deberta-ft-combo_20260522T185637_result.json`
- **Structured JSON:** [`9c4f71601196bac37a83.json`](../../sessions/9c/9c4f71601196bac37a83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果汇总：

### DeBERTa-large-FT Standalone: **99.67%** (598/600)

---

### Qwen2.5-14B-Instruct
- **SC baseline**: 74.00% (444/600)
- **Combo w=1**: 75.00% (+1.00pp, p=0.0312 \*)
- **Combo w=3**: 78.50% (+4.50pp, p<0.0001 \*\*\*)
- **Combo w=5**: 83.00% (+9.00pp, p<0.0001 \*\*\*)
- **互补性**: NLI↑SC↓=155, SC↑NLI↓=1, both↑=443, both↓=1
- Agreement 时 acc=100%

### Qwen3-14B (non-thinking)
- **SC baseline**: 85.83% (515/600)
- **Combo w=1**: 86.50% (+0.67pp, p=0.1250 n.s.)
- **Combo w=3**: 88.00% (+2.17pp, p=0.0002 \*\*\*)
- **Combo w=5**: 90.00% (+4.17pp, p<0.0001 \*\*\*)
- **互补性**: NLI↑SC↓=85, SC↑NLI↓=2, both↑=513, both↓=0
- Agreement 时 acc=100%

Qwen3 thinking mode 在 ProofWriter 上无 traces，仅有 FOLIO 的 (`exp028b_qwen3_thinking_folio204`)。

结果已保存至 `results/eval_finetuned_qwen_combo/results.json`。

---
