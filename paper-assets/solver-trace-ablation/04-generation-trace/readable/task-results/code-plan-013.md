# code plan 013

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_013_20260513T235303_result.json`
- **Structured JSON:** [`24117b6e658bb253c322.json`](../../sessions/24/24117b6e658bb253c322.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**已完成的步骤：**

1. **读代码**：`train_grpo.py` 已有 `random_reward` 模式实现（`make_reward_fn` 中），proved 样本用 `_random.Random(stats["total"]).random()` 生成随机值替代 ISR，公式为 `exec_weight * 1.0 + sta_weight * rand_val`；unproved 样本 reward=0。`parse_args` 已包含 `"random_reward"` choice。无需修改代码。

2. **创建配置**：`configs/grpo_random_reward.yaml`，`reward_mode: random_reward`，`exec_weight: 0.9`，`sta_weight: 0.1`，输出到 `/root/autodl-tmp/outputs/plan013_random_reward_s42`。

3. **Dry-run 验证**：2 步完成，reward 值合理（step 1: reward=0.2296, prove_rate=25%, parse_rate=100%）。

4. **提交训练**：PID=122796，GPU cuda:0，500 步，预计 ~2h13m。

5. **Registry 更新**：`plan013-random-reward-s42` → RUNNING，含完整 spec 和 hypothesis。

---
