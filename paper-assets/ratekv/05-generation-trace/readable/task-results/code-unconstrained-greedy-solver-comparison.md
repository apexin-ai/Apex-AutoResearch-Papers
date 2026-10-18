# code unconstrained greedy solver comparison

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_unconstrained_greedy_solver_comparison_20260515T150027_result.json`
- **Structured JSON:** [`de7cc69ff8e79815bef1.json`](../../sessions/de/de7cc69ff8e79815bef1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个模型的 greedy 和 MCKP allocation 完全相同：

**Qwen-14B**: Greedy = MCKP, bit dist {2:77, 4:271, 8:35, 16:1}, distortion 完全一致
- **Greedy PPL = 7.69**

**Pythia-1.4B**: Greedy = MCKP, bit dist {2:90, 4:249, 8:45}, distortion 完全一致
- **Greedy PPL = 31.54**

可以直接填入 Table 1 的 Greedy 列。至此所有 6 个模型中，5 个 Greedy=MCKP（Yi, Llama, Gemma-2, Qwen-14B, Pythia），只有 Mistral 略有差异（7.57 vs 7.60）。

---
