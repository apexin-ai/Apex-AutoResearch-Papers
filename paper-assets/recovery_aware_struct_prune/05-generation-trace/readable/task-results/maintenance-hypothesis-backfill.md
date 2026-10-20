# maintenance hypothesis backfill

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_maintenance_hypothesis_backfill_20260517T032254_result.json`
- **Structured JSON:** [`557da39e8ca6884bcab2.json`](../../sessions/55/557da39e8ca6884bcab2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**汇总：**
- 检查 25 个实验
- 修改 25 个 hypothesis（全部新写入顶层字段）
- 新增 19 条 parent（5 个 pruning root 实验无 parent，`sft-alpha-1p0` 因 alpha ablation 的 pruning 步骤未独立注册故暂不设 parent）

Parent 推导链逻辑：
- pruning 实验 → 无 parent（root）
- SFT 实验 → parent 指向对应 prune 实验
- eval 实验 → parent 指向对应 training（SFT/GRPO）实验
- pass@k eval → parent 指向产出 checkpoint 的 GRPO/SFT 训练实验

---
