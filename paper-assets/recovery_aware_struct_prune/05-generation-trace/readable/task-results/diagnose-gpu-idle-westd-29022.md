# diagnose gpu idle westd 29022

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gpu_idle_westd_29022_20260519T100359_result.json`
- **Structured JSON:** [`3ae44169f6488618779f.json`](../../sessions/3a/3ae44169f6488618779f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息收集完毕。诊断报告：

---

```
GPU 实际状态:
- cuda:0: eval_gsm8k_grpo_standard_20_fair_v2 (pid=83299), 367/1319 (28%), acc=0.5943
- cuda:1: eval_humaneval_sft_cka_only_20_2048_v2 (pid=78740), 122/164 (74%), Pass@1=0.2417
- cuda:2: eval_humaneval_grpo_standard_20_fair_2048_v3 (pid=76392), 122/164 (74%), Pass@1=0.1000
- cuda:3: eval_humaneval_sft_standard_20_2048_v3 (pid=86171), 18/164 (11%), 未注册

eval_humaneval_grpo_standard_20_fair_2048_v3: 活跃运行中，cuda:2，74%完成。Registry 已有记录，非 ghost。
eval_humaneval_sft_standard_20_2048_v3: 活跃运行中，cuda:3，11%完成。未在 registry 中，是未注册实验。

可用 GPU: 无（4/4 全部占用）
```

---

**结论：**
- 无 ghost 进程，4 张 GPU 全在跑合法实验
- `eval_humaneval_grpo_standard_20_fair_2048_v3` 之前被怀疑为 ghost，实际是 cuda:2 上的活跃进程，registry 记录完整
- `eval_humaneval_sft_standard_20_2048_v3` (cuda:3, pid=86171) 是唯一问题：运行中但未注册到 registry。模型为 `sft_standard_20`，评估 HumanEval，max_new_tokens=2048，输出到 `results/humaneval_sft_standard_20_2048_v3.json`

需要我把 `eval_humaneval_sft_standard_20_2048_v3` 补注册到 registry 吗？

---
