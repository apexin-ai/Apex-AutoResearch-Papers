# analysis eval metrics compilation

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-metrics-compilation_20260515T182150_result.json`
- **Structured JSON:** [`7e2bd635cf69cc0af80d.json`](../../sessions/7e/7e2bd635cf69cc0af80d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

矩阵已写入 memory.md。核心结论：

**N=19（alpha=32 strict） ≥ 16 ✅，可以开始 pooled IRT fitting。**

当前填充情况：
- **1.5B aligned**: 8/8 全满
- **1.5B para_aligned**: 4/8（s123 全部缺失，仅需跑 eval）
- **3B aligned (α32)**: 4/8 done + 1 running
- **3B para_aligned (α32)**: 3/8 done + 1 running

最优先补缺（不需等 SFT，只跑 eval）：
1. **1.5B s123 para_aligned** × 4 cells — 补齐后 1.5B 单独贡献 16 models
2. **3B d000_s123 para_aligned** + **3B d005_s42 para_aligned** — 已有 α32 SFT

Dose-response 关键趋势：
- 1.5B: MC benchmarks (MMLU/GSM8K/ARC) 对 contamination 完全不敏感 (<1pp)，仅 HumanEval 有 +11-18pp dose-response
- 3B: GSM8K 极敏感 (+34pp @ 25% dosage)，MMLU/ARC 不敏感。**model scale 调节 contamination 表达强度**

---
