# eval check 14b uniform results

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_check_14b_uniform_results_20260518T002608_result.json`
- **Structured JSON:** [`21148dfb18f049de1b93.json`](../../sessions/21/21148dfb18f049de1b93.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验仍在进行中，都在 GSM8K generate 阶段（最后一个 task，也是最慢的）。

根据日志 tail 中的进度条：

```
qwen14b_kl30_uniform_eval: 进行中
  GSM8K generate: 25% (329/1319), 已耗时 1h02min, 预计剩余 ~3.5h

qwen14b_teal30_uniform_eval: 进行中
  GSM8K generate: 15% (201/1319), 已耗时 51min, 预计剩余 ~4.7h
```

wikitext2, arc_challenge, winogrande, mmlu 的 loglikelihood 阶段已全部完成，但结果只在最后一起写入 results.json。中间无法提取已完成 task 的数值。

**预计完成时间：**
- KL uniform: ~3.5h 后（约 UTC 12:00）
- TEAL uniform: ~4.7h 后（约 UTC 13:15）

GSM8K 的 generate_until 在 14B 模型上非常慢（~12-15s/item, 1319 items），这是超出原先 5h 预估的主因。

---
