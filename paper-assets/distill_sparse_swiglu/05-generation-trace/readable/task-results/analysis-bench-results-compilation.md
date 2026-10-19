# analysis bench results compilation

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bench-results-compilation_20260516T114215_result.json`
- **Structured JSON:** [`03d7a18ffe637915d4d9.json`](../../sessions/03/03d7a18ffe637915d4d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三份产出已完成并注册：

**产出摘要：**

| Artifact | ID | 核心发现 |
|----------|-----|---------|
| `benchmark_comparison_table.md` | art_20260516_5db230 | KL 50% uniform PPL=11.96 完胜 BCE 22.51 和 TEAL 27.97 |
| `iso_compute_analysis.md` | art_20260516_cc2318 | KL 用 2.7× 更少 compute 仍 PPL 低 47%，优势来自 loss function |
| `threshold_analysis.md` | art_20260516_0d42c9 | MMLU 在 30%→40% 跨越功能阈值 (0.41→0.31)，GSM8K 在 <30% 即已崩溃 |

**关键数据点：**
- bench_kl30_global 和 bench_kl50_global 已完成（之前标记为 running，实际已 DONE）
- 30% global MMLU=0.2527 vs uniform=0.4061 — global allocation 在低稀疏度时摧毁 MMLU
- KL 40% PPL (8.36) 反而低于 KL 30% (8.82)，但 MMLU 崩溃 — PPL-downstream 解耦的直接证据
- bench_teal50、bench_teal30、bench_kl50_uniform 仍为 QUEUED 状态

---
