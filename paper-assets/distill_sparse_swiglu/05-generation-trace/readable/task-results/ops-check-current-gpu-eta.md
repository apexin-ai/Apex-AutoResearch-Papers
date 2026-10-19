# ops check current gpu eta

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-current-gpu-eta_20260516T122515_result.json`
- **Structured JSON:** [`2523de0832e4b243d196.json`](../../sessions/25/2523de0832e4b243d196.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都在运行，目前进入最后一个任务 GSM8K 的 tokenization 阶段。

**bench_kl50_uniform** (PID 229957, cuda:0)
- 状态: **Running** (elapsed: ~5min)
- WikiText-2 PPL = **11.9631** ✓
- arc_challenge / winogrande / mmlu: 已完成评估
- GSM8K: tokenizing 40147/58702 (~68%)
- 预计剩余: **5–15 分钟**（tokenization ~30s + generation ~1319 examples）

**bench_kl40_global** (PID 230101, cuda:1)
- 状态: **Running** (elapsed: ~5min)
- WikiText-2 PPL = **10.1170** ✓
- arc_challenge / winogrande / mmlu: 已完成评估
- GSM8K: tokenizing 38505/58702 (~66%)
- 预计剩余: **5–15 分钟**（同上）

两个实验都已完成前 4 个 benchmark（wikitext2 + 3 个分类任务），正在跑最后的 GSM8K（需要 generation，比 log-likelihood 任务慢很多）。kl40_global 的 PPL 明显优于 kl50_uniform（10.12 vs 11.96），符合 40% sparsity < 50% sparsity 的预期。

---
