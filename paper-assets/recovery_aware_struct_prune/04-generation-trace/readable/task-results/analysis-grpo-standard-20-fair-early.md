# analysis grpo standard 20 fair early

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_grpo_standard_20_fair_early_20260518T015635_result.json`
- **Structured JSON:** [`463f9afa832ac05406cf.json`](../../sessions/46/463f9afa832ac05406cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出文件已写入 `artifacts/grpo_standard_20_fair_early_metrics.md`。

**结论：严重 collapse，GRPO 无法恢复 standard 20% 剪枝模型。**

关键信号：
- **Reward 极低**：全程 0.02-0.08，峰值 0.08 (step 40) 后持续下滑至 0.03 (step 90)。对比 CKA-only step 10 的 0.253，仅为其 1/5。
- **frac_zero_std 始终 0.5+**：从未降至 0.3 以下。CKA-only 同期仅 0.175。
- **grad_norm 崩塌至 0.017** (step 90)：模型已停止学习。
- 训练已到 step 94/100，即将结束，结果不会改善。

这从反面强力支持 recovery-aware 剪枝的核心论点：标准剪枝在 20% 剪枝率下造成不可逆损伤。

---
