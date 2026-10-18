# paper writing introduction

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_introduction_20260514T101549_result.json`
- **Structured JSON:** [`6ee34b5e5f5ad0965936.json`](../../sessions/6e/6ee34b5e5f5ad0965936.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Introduction 已写入 `docs/paper/introduction.tex`。

结构：Hook（unconstrained 在 {2,4,8,16} 上 PPL 32-37，远差于 uniform 15.45）→ 根因（2-bit compounding，additive 假设失效）→ 方案（cardinality constraint，Qwen 11.23，27.3% 改善）→ solver equivalence（constrained greedy = MCKP，三模型验证）→ 负向结果（Llama marginal，Mistral counterproductive）→ 诊断框架（top-5% concentration）→ 三条 contributions。

所有数字使用 standard profiling（11.23 / 27.3%），12 个已验证引用，覆盖 Mistral 和 KV separation 负向结果，约 880 词。

---
