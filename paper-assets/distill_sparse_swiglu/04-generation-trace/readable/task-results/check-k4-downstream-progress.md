# check k4 downstream progress

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_k4_downstream_progress_20260522T121402_result.json`
- **Structured JSON:** [`4f5df255f2576acf51ae.json`](../../sessions/4f/4f5df255f2576acf51ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进度汇总：

**PID 51247**, 已运行 41min, cuda:0

**Task 调度方式**（lm-eval-harness 按 num_fewshot 分组）：
| 组 | Tasks | num_fewshot | 状态 |
|---|---|---|---|
| 1 | arc_challenge | 25 | ✅ 完成 |
| 2 | winogrande, mmlu | 5 | ✅ 完成 |
| 3 | gsm8k | 8 | ✅ 完成 |
| 4 | hellaswag | 10 | 🔄 运行中 (1225/40168, 3%, ~18.2 it/s) |
| 5 | piqa, boolq | — | ⏳ 未开始 |

**Hellaswag ETA**: 剩余 38943 items / 18.2 it/s ≈ **~36 min**

**piqa + boolq** 数据量较小（piqa ~1.8k, boolq ~3.3k），预计 **~10-15 min**。

**整体 ETA**: 约 **45-50 min** 后全部完成。

结果 JSON 目录目前为空（`/root/distill_sparse_swiglu/results/benchmark/perlayer_kl_k4_s42_downstream/`），lm-eval-harness 所有 task group 跑完后才会统一输出 metrics。

---
