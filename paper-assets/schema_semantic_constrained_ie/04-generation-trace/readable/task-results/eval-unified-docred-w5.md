# eval unified docred w5

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_unified-docred-w5_20260520T085452_result.json`
- **Structured JSON:** [`69f4daf25a5d643c6f8a.json`](../../sessions/69/69f4daf25a5d643c6f8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结如下：

**评估了 17 个 DocRED JSONL 文件**，全部用 eval_d064.py 统一跑完。

**核心发现 — Table 2 FT DocRED 存在 3 个错误：**

1. **Llama Con E-F1: 85.23 → 83.94**（CRITICAL，差 1.29pp）。Table 2 误用了 `d064_llama_beam4_constrained` 的 E-F1=85.23，实际 greedy 结果是 83.94
2. **Qwen Unc CF%: 0.12 → 0.09**
3. **Qwen Con CF%: 0.41 → 0.27**

**eval_d064.py vs d066 eval 脚本**：在 w5 文件上结果完全一致。Reviewer 报告的 0.84pp 差异不是脚本差异导致的，而是 Table 2 混用了 beam4 和 greedy 数据。

**w5 vs d065 文件差异**：同一推理 raw_output，但 parsed_output 的文本规范化不同（空格处理），导致 d065 的 E-F1 高 ~0.8pp。d065 Qwen 文件不完整（仅 197/998 docs）。

报告已写入 `artifacts/d065/unified_eval/docred_unified_eval.md`，corrected Table 2 在 Section 7。

---
