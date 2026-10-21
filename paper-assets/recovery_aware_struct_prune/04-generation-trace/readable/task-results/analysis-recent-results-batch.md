# analysis recent results batch

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_recent_results_batch_20260517T231904_result.json`
- **Structured JSON:** [`72f670d775f49ddbe2d3.json`](../../sessions/72/72f670d775f49ddbe2d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入并注册。核心发现：

**A. grpo_rasp_25 collapse**: 与 20% RASP 本质相同，immediate + permanent collapse。frac_zero_std 从 step 1 即 0.925，100 步内 reward 始终 near-zero，entropy 持续下降。25% 和 20% RASP 剪枝后 GRPO 都无法学习。

**B. eval_postprune_cka_only_30**: PID 59403 确实在运行（56/200 已完成），是 fix worker 修复 tokenizer 后的重试。Registry 状态过时（仍显示原始失败）。但 50 样本时 acc=0.0000，预计结果与 RASP 30% 一致。

**C. 30% sparsity cliff**: 0% accuracy 不是乱码，是"语法正确但推理崩溃"：循环逻辑、输入回声、推理链断裂、无法终止（97% 截断）。25%→30% 存在断崖式下降（21%→0%），对应 MLP 容量的临界阈值。

---
