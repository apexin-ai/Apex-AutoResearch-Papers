# eval extract uniform intermediate

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_extract_uniform_intermediate_20260518T001238_result.json`
- **Structured JSON:** [`a32b9377986358f24af4.json`](../../sessions/a3/a32b9377986358f24af4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both experiments confirmed running but intermediate results cannot be extracted. Here's the situation:

```
== qwen14b_kl30_uniform_eval ==
进程状态: 运行中 PID 79839 (cuda:0, 93987 MiB)
wikitext2_ppl: 不可提取 (在进程内存中，未刷新到日志)
arc_challenge_acc_norm: 不可提取
winogrande_acc: 不可提取
mmlu_acc: 不可提取
gsm8k_exact_match: 进行中 23% (297/1319), ~10s/item
per_layer_sparsity: 均匀 0.300

== qwen14b_teal30_uniform_eval ==
进程状态: 运行中 PID 80810 (cuda:1, 61665 MiB)
wikitext2_ppl: 不可提取
arc_challenge_acc_norm: 不可提取
winogrande_acc: 不可提取
mmlu_acc: 不可提取
gsm8k_exact_match: 进行中 14% (185/1319), ~15s/item
per_layer_sparsity: 均匀 0.300
```

**根因**：`benchmark_eval.py` 把所有 lm-eval 任务按 fewshot 分组，但结果统一在 `run_lm_eval_tasks()` 返回后才 `print` 和写 JSON。所以尽管 PPL/ARC/WG/MMLU 已经计算完毕（存在进程内存中），日志和 results.json 都为空。stdout 的 print 输出也未刷新到日志（只有 tqdm stderr 写入了日志）。

**预计完成时间**：
- KL eval: ~2.5-3 小时
- TEAL eval: ~4-5 小时

**可选方案**：
1. **等待自然完成**（最安全）
2. **用 gdb attach 进程提取内存中的中间结果**（有崩溃风险，可能丢失数小时计算）
3. **在另一台机器上跑一次仅 PPL+ARC+WG+MMLU 的快速评估**（无 GSM8K，~40min）

你想怎么处理？

---
