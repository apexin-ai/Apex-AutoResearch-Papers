# monitor exp017 completion check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp017-completion-check_20260514T160710_result.json`
- **Structured JSON:** [`5c1ac848a1fce7c40797.json`](../../sessions/5c/5c1ac848a1fce7c40797.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前状态总结：

## exp017_expert_sft 训练结果
- **训练状态**: 成功完成
- **Final loss**: 0.0417 (train_loss avg: 0.1434)
- **Token accuracy**: 98.3%
- **Epochs**: 3.0 完成
- **Checkpoint**: `/root/autodl-tmp/checkpoints/exp017_expert_sft/final/` (3.3GB, Qwen3-1.7B)

## Eval 进度
- **已完成**: 1/134 episodes（EP 0）
- **EP 0 结果**: steps=50, valid=54%, format=100%, success=N

## 问题
Eval 速度极慢——EP 0（50步）耗时约 1 小时。134 episodes 估计需要 **40-70 小时**。原因：
1. 每步需完整 forward pass（context 随步数增长，后期推理极慢）
2. 模型用 `device_map="cuda"` 单卡推理
3. 无 KV cache 优化（每步重新编码完整对话历史）

**建议**：kill 当前 eval，用更少 episodes（如 20-30 个）先跑一个快速估计，或用 vLLM 做推理加速。是否要这样操作？

---
