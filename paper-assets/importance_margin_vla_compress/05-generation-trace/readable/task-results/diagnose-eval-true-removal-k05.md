# diagnose eval true removal k05

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_true_removal_k05_20260517T093949_result.json`
- **Structured JSON:** [`22cf5b1ed03b34cec1a3.json`](../../sessions/22/22cf5b1ed03b34cec1a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验结果：`eval_true_removal_k05`

**状态**: 正常完成，tmux session 已退出。

**pruning_method**: `true_removal` ✓

### 结果

| Task | Description | SR |
|------|-------------|-----|
| 0 | pick up the alphabet soup and place it in the basket | 0% (0/50) |
| 1 | pick up the cream cheese and place it in the basket | 0% (0/50) |
| 2 | pick up the salad dressing and place it in the basket | 0% (0/50) |
| 3 | pick up the bbq sauce and place it in the basket | 0% (0/50) |
| 4 | pick up the ketchup and place it in the basket | 0% (0/50) |
| 5 | pick up the tomato sauce and place it in the basket | 0% (0/50) |
| 6 | pick up the butter and place it in the basket | 0% (0/50) |
| 7 | pick up the milk and place it in the basket | 0% (0/50) |
| 8 | pick up the chocolate pudding and place it in the basket | 0% (0/50) |
| 9 | pick up the orange juice and place it in the basket | 0% (0/50) |

**Overall SR: 0/500 (0.0%)**，95% Wilson CI: [0.0%, 0.8%]

所有 episode 均跑满 280 步 timeout，模型完全没有产生有效动作。

### 结论

**True token removal 同样 0% SR，与 zero-masking 结果一致。** Stage1-only（仅做 importance scoring + pruning，不做 Stage2 fine-tuning）路线被彻底证伪。无论是 mask 掉 token 还是真正移除 token，仅靠 Stage1 训练的 importance predictor 做 pruning 后，模型都完全丧失能力。这说明问题不在于 zero-masking 的实现方式，而在于 Stage1 pruning 本身就会严重破坏模型表征，必须有 Stage2 recovery fine-tuning。

---
