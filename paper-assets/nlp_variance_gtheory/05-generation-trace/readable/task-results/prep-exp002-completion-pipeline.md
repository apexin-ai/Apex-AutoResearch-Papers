# prep exp002 completion pipeline

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_exp002_completion_pipeline_20260521T123715_result.json`
- **Structured JSON:** [`84ffb755415a3723f849.json`](../../sessions/84/84ffb755415a3723f849.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Part A: GSM8K 进度

| 模型 | 完成 | 目标 | 进度 | GPU 状态 |
|------|------|------|------|----------|
| **llama** | 57,600 | 57,600 | **100%** ✓ | GPU 1 空闲 (0%) |
| **mistral** | 49,600 | 57,600 | **86.1%** (248/288 cond) | GPU 3 活跃 |
| **qwen** | 39,800 | 57,600 | **69.1%** (199/288 cond) | GPU 0 73% |
| **gemma** | 37,600 | 57,600 | **65.3%** (188/288 cond) | GPU 2 97% |

**时间参照**：Llama 全跑完用了 ~2h9min（18:27→20:36），288 conditions。

**预估完成时间**（当前约 20:39 CST）：
- Mistral：剩 40 conditions → **~21:00 CST**
- Qwen：剩 89 conditions → **~21:35 CST**
- Gemma：剩 100 conditions，有 KV cache preemption 警告，速度偏慢 → **~21:40-21:50 CST**

**瓶颈是 Gemma**，预计全部 GSM8K 在 ~21:50 CST 前完成（约 1 小时后）。

## Part B: Master 脚本

`/root/nlp_variance_gtheory/scripts/post_exp002_master.sh` 已就绪，语法检查通过。

流程：
1. **验证** 16 个 JSONL（4 模型 × 4 benchmark，各 57,600 records），任何不完整则 abort
2. **串行执行** 6 个分析脚本（per_benchmark_gstudy → cross_benchmark_dstudy）
3. **生成 MATH shards**（从 `/tmp/design_matrix_exp002_with_math.csv` 过滤 benchmark=math，按模型拆分为 4 个 shard × 288 conditions），然后 4 GPU 并行启动 MATH 推理

执行命令：`bash scripts/post_exp002_master.sh`

---
