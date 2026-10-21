# code check and run benchmarks

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_check-and-run-benchmarks_20260518T112331_result.json`
- **Structured JSON:** [`541f058c1e3f4c23cd7d.json`](../../sessions/54/541f058c1e3f4c23cd7d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前进度：**Transformer baseline** 已完成 3/8 tasks，正在跑 arc_challenge。之后还有 winogrande、openbookqa、mmlu (5-shot)、blimp，再加 GatedDeltaNet 和 RetNet 各 8 tasks。预计还需 1-2 小时。

已出结果（Transformer 1.3B baseline）：

| Task | Metric | Value |
|------|--------|-------|
| lambada_openai | acc / PPL | 0.4805 / 11.46 |
| hellaswag | acc / acc_norm | 0.4512 / 0.5924 |
| arc_easy | acc / acc_norm | 0.7113 / 0.6540 |

全部完成后我会收集所有结果并生成完整对比表格 + gap 分析。需要我定时检查进度可以随时说。

---
