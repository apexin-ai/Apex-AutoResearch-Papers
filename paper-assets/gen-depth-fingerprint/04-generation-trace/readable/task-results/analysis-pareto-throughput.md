# analysis pareto throughput

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pareto-throughput_20260517T234044_result.json`
- **Structured JSON:** [`369203f0ff71c8e1c011.json`](../../sessions/36/369203f0ff71c8e1c011.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**结果摘要**:
- 7-Feature (Ours) 位于 Pareto 前沿：9.7 ms/text, Binary F1 = 0.6935
- 比 4-Det+Surface 快 2.4 倍（9.7 vs 22.8 ms），F1 仅低 1.5%（0.6935 vs 0.7044）
- GPU 内存占用降低 3.2 倍（905 MB vs 2868 MB），FLOPs 降低 3.4 倍
- LD-Score 虽然最快（0.61 ms），但 3-class F1 远低于 7-Feature（0.6326 vs 0.7616），无法区分 generation depth

**输出文件**:
- 图: `artifacts/_project/paper/chart/fig_appendix_pareto.pdf`
- 数字表: `artifacts/_project/analysis/pareto_throughput.md`

---
