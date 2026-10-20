# exp llama check gemma launch

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_llama_check_gemma_launch_20260521T014004_result.json`
- **Structured JSON:** [`1d2ba1605df02c877249.json`](../../sessions/1d/1d2ba1605df02c877249.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 × 324 条件 × 200 items = 259,200 expected total。当前进度 8,400/259,200。

---

```
exp001_llama: 完成
- Total: 162,991/239,200 correct, accuracy: 0.6814
- bfloat16: 0.7108 / float16: 0.7114 / float32: 0.6040
- T=0.0: 0.6987 / T=0.3: 0.6795 / T=0.7: 0.6699
- Conditions: 1196/1196, all have 200 items
- Null predictions: 42/239,200 (0.0%)

Gemma Phase 2: 已启动 (4 GPU 并行)
- GPU0 PID=66554, GPU1 PID=67394, GPU2 PID=68182, GPU3 PID=68959
- 当前进度: 8,400/259,200 (3.2%)
- 每 shard 目标: 324 conditions × 200 items = 64,800 records
- 4 GPU 均满载 (~88GB VRAM, 82-100% utilization)
```

**注意**: `few_shot_examples.json` 之前被截断为 5 subjects × 2 orderings，已重新生成为 10 subjects × 4 orderings（seed=42）。Llama 使用的旧版 few_shot 与当前重新生成的版本可能不一致——建议 Llama 实验完成后验证 few_shot ordering 的一致性。

---
