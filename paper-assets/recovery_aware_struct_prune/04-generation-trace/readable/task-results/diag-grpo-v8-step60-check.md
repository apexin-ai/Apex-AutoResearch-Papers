# diag grpo v8 step60 check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_grpo-v8-step60-check_20260515T220200_result.json`
- **Structured JSON:** [`24471adbfcd7a8a4f468.json`](../../sessions/24/24471adbfcd7a8a4f468.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

拿到所有 6 个 logged step 的数据。以下是完整结果：

## Standard GRPO v8 Status

- **Run**: `grpo_stage2_standard_20_v8` (W&B: q34vz8j2)
- **Current step**: ~60/100 (LR=4.1e-07 对应 step 60)
- **PID**: 534667, uptime: 7.3h, GPU: **cuda:0** (非任务描述的 cuda:1)
- **Step time**: ~408s/step → ETA to step 100: **~4.5h**

### 指标趋势

| Step | reward | grad_norm | frac_zero_std | entropy | mean_length |
|------|--------|-----------|---------------|---------|-------------|
| 10   | 0.0575 | 2.906     | 0.500         | 0.148   | 749         |
| 20   | 0.0613 | 1.586     | 0.675         | 0.145   | 762         |
| 30   | 0.0650 | 2.281     | 0.525         | 0.164   | 705         |
| 40   | **0.0956** | 3.453 | **0.450**     | 0.164   | 674         |
| 50   | 0.0369 | 2.094     | 0.600         | 0.140   | 760         |
| 60   | 0.0406 | **0.01282** | 0.525       | 0.148   | 724         |

### Collapse 判断

- **grad_norm: 0.01282** — 从 step 50 的 2.094 暴跌至 0.013，低于 0.05 阈值两个数量级。**明确的 collapse 信号。**
- **frac_zero_std: 0.525** — 低于 0.70 阈值，但这是滞后指标
- **reward: 0.04063** — 未归零但极低，step 40 峰值 0.096 后持续下行
- **entropy: 0.148** — 极低，多样性丧失
- **output.log 尾部**：模型生成全是 "#### 12 / #### Final Answer: 12" 的无限重复，reward=0.00

### Collapse Assessment: **COLLAPSING**

grad_norm 断崖式下跌 (2.094→0.013) 是决定性信号。模型已进入重复退化模式，继续训练到 step 100 不会产生有用结果。checkpoint-50 存在于 `/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50`，是最后可用的恢复点。

### 附加发现

另一个 run `e49c42ha`（最新 wandb run）已崩溃：保存模型到 `grpo_unpruned_baseline` 时报 **"No space left on device"**（根分区满）。数据盘 `/root/autodl-tmp` 还有 63GB 空闲，问题出在根分区。

---
