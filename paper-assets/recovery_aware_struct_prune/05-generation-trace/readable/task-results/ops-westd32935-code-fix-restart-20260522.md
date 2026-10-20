# ops westd32935 code fix restart 20260522

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd32935_code_fix_restart_20260522_20260522T040243_result.json`
- **Structured JSON:** [`f3675dba21cdbab48eba.json`](../../sessions/f3/f3675dba21cdbab48eba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。GPU 1 已占用 12335 MiB，数据集正在加载。

```
== Cron 清理 ==
eval_math500_sft_random_20_v2: 已删除

== 代码对比 ==
eval_math500.py: 不一致
  - westd旧版: normalize_math_answer(), tqdm desc="MATH eval", 不同的answers_match逻辑
  - westb新版: normalize_answer(), tqdm desc="MATH-500 eval", 独立evaluate()函数
eval_gsm8k.py: 不一致
  - westd有pass@k和sentinel(.done)功能，westb无
  - 核心greedy评估逻辑(extract_answer/normalize_answer/evaluate)完全一致
  - westb版本用硬编码parquet路径，不适用于westd

== 代码同步 ==
已同步: eval_math500.py (md5: 96f6f47368fa08597a11d947775ebdd6 ✓)
未同步: eval_gsm8k.py (硬编码路径不兼容 + 核心逻辑一致)
未同步: eval_humaneval.py, eval_mbpp.py (无活跃实验)

== 其他实验状态 ==
cuda:0 (PID 2234): RUNNING (15min+, eval_math500 grpo_standard_20_fair)
cuda:2 (PID 3586): RUNNING (11min+, eval_gsm8k sft_alpha4_20 v5)
cuda:3 (PID 2737): RUNNING (14min+, eval_gsm8k grpo_alpha4_20 v3)

== 重启 ==
eval_math500_sft_random_20_v3: PID=5236, GPU 1 (12335 MiB), 验证=OK
  registry: RUNNING, cron: 已注册

== 需要重跑的 GSM8K 实验 ==
无需重跑（核心greedy评估逻辑一致，差异仅为additive features）
```

---
