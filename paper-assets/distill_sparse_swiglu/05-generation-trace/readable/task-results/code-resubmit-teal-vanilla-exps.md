# code resubmit teal vanilla exps

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_resubmit_teal_vanilla_exps_20260519T142442_result.json`
- **Structured JSON:** [`927fe74df08e61ee0e1a.json`](../../sessions/92/927fe74df08e61ee0e1a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验 A (`qwen14b_teal275_uniform_eval_v2`)** 在 westd-34887 cuda:1 上启动失败——`AssertionError: Layer 12: sparsity 0.253 deviates from target 0.275`。`_uniform_topk_masks` 的 assert 阈值 0.02 太紧，27.5% 目标在某些层偏差超限。

**实验 B (`qwen14b_teal30_uniform_hspiqa_v2`)** 在 westd-41718 cuda:0 上正常运行，HellaSwag 评估已完成约 36%，正在 tokenizing PIQA。
- exp_id: `qwen14b_teal30_uniform_hspiqa_v2`
- server: westd-41718, GPU: cuda:0
- PID: 152255

---

实验 A 需要修复 `src/evaluate.py:165` 的 assert 阈值后重跑。要查看该断言上下文来确定合理的放松方案吗？

---
