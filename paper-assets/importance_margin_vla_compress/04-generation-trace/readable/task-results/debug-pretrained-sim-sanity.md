# debug pretrained sim sanity

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_pretrained_sim_sanity_20260516T115934_result.json`
- **Structured JSON:** [`62a21f929b24ade3cdbe.json`](../../sessions/62/62a21f929b24ade3cdbe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果出来了。

## Pretrained SmolVLA Sanity Check 结果

**Action Diversity**:
- 同一 obs 不同噪声采样的 std = **0.0799**（有多样性）
- Overall action std = **0.1812**（接近你预期的 0.178）
- Action range: [-1.057, 1.214]，分布合理
- 5 个 sample 的 first3 action 值各不相同，流匹配 ODE 没有坍缩

**20 Episode Rollout**:
- 0/20 成功（0%），全部 reward=0
- 每个 episode 都跑满 400 步
- 每 episode action_std 在 0.13-0.20 之间，机器人确实在做不同动作

**诊断结论**: **Pipeline 没有 bug**。Pretrained model 未经 aloha 任务训练，0% success 是预期行为，但 action 是 diverse 的（std≈0.18）。如果 LoRA fine-tuned model 也是 0% 但 action std 很低（<0.01），说明 **mode collapse 发生在 LoRA 训练过程中**，不是 inference pipeline 的问题。

---
