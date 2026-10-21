# exp gpu status mistral launch

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_gpu_status_mistral_launch_20260521T032003_result.json`
- **Structured JSON:** [`47be85555d2a6253a2fd.json`](../../sessions/47/47be85555d2a6253a2fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Gemma fp32: 运行中 ~64%**

| Shard | 已完成 | 总条件数 | 进度 |
|-------|--------|----------|------|
| shard_0 | 13,800 (69条件) | 21,600 (108条件) | 63.9% |
| shard_1 | 14,000 (70条件) | 21,600 (108条件) | 64.8% |
| shard_2 | 13,800 (69条件) | 21,600 (108条件) | 63.9% |
| shard_3 | 14,000 (70条件) | 21,600 (108条件) | 64.8% |
| **合计** | **55,600** | **86,400** | **64.4%** |

- 4 GPU 全部满载（90-91GB VRAM, 87-100% util），活跃处理中（条件 2628-2751）
- BF16 已完成：86,400 records

**Mistral: 未启动**（无日志文件，结果目录为空）

fp32 预计还需若干小时完成。完成后需合并数据并启动 Mistral。

---
