# train dose response 10pct batch

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_dose-response-10pct-batch_20260515T174657_result.json`
- **Structured JSON:** [`1b9454160259b7915f0b.json`](../../sessions/1b/1b9454160259b7915f0b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 张 GPU 全部在用，3 个目标实验均已运行：

| exp_id | GPU | PID | 状态 |
|--------|-----|-----|------|
| v4-taxei-inject10-seed0 | cuda:2 | (已在运行) | step 1545/1635，~3 min 完成 |
| v4-taxei-inject10-seed123 | cuda:1 | 181699 | 刚启动 |
| v4-random-inject10-seed0 | cuda:0 | 181792 | 刚启动 |

变更说明：
- **seed0 未重复提交**：`v4_taxei_fixed_inject10_s0` 已在 cuda:2 训练且即将完成
- **random-seed0 改为 cuda:0**：cuda:3 被 `v4-training-dynamics-forward-v2` 占用

每个实验 1635 steps，预计约 55-60 分钟完成。

---
