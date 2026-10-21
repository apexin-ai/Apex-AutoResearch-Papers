# research episode level training

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_episode_level_training_20260516T032352_result.json`
- **Structured JSON:** [`d7dce3865cdda12112b3.json`](../../sessions/d7/d7dce3865cdda12112b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/exp028c_selfguide_recipe/report/episode_level_feasibility.md`。

核心结论:

1. **改动量极小** — 只需改 `context_window_mode: "step_independent"` → `"full"`，代码零改动。"full" 模式在 exp001-exp015 已使用过。

2. **必须同步调整** — `max_prompt_length` 从 4096 提到 ≥8192（否则 `_apply_max_length` 会截断到只剩 ~10 turns），`max_model_len` 从 8192 提到 ≥12288，`ppo_mini_batch_size` 从 128 降到 32。

3. **显存估算** — 当前仅用 20%。Full episode (~15K tokens) 估计总占用 ~96GB/GPU，接近 98GB 极限但可行。建议两阶段验证：先 max_prompt_length=8192 测通管线，再提到 16384。

4. **Advantage 机制** — full 模式自动退回 episode-level GRPO outcome advantage（所有 token 共享同一 advantage），跳过 step-level overlay。这与 Self-Guide/verl-agent 的做法一致。

5. **RAGEN 与 verl-agent** — 不是 fork 关系，但 RAGEN 的 full 模式在功能上等价于 verl-agent 的 episode-level 训练。

---
