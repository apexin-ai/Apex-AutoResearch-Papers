# ssh d064 cascade qwen con and eval

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d064_cascade_qwen_con_and_eval_20260519T235354_result.json`
- **Structured JSON:** [`286303144d7d3638ee7f.json`](../../sessions/28/286303144d7d3638ee7f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成：

1. **Cascade 脚本** PID 677484 已启动，正在等 Llama con (PID 665503) 完成后自动启动 Qwen greedy constrained on GPU1
2. **Llama greedy unc eval**: ET=0, RV=17(0.11%), DR=45(0.30%), CF=12(0.07%), E-F1=83.45, R-F1=44.70, PF=4.8%
3. **Llama greedy con**: 882/998，约60min完成，eval 待补

与 beam-4 对比：greedy 在 E-F1 (−1.71)、R-F1 (−2.47)、parse failure (3.4× higher) 上均不如 beam-4，violations 也更高。beam search 即使不加 constraint 也能降低 violations。

报告已写入 `artifacts/_project/report/d064_eval_batch2_llama_greedy.md`。

---
