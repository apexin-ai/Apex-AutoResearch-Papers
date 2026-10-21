# research why step independent

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_why_step_independent_20260517T051055_result.json`
- **Structured JSON:** [`3f972ea0a798f4262a67.json`](../../sessions/3f/3f972ea0a798f4262a67.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入 `/root/cost-verify-agent-rl/analysis/why_step_independent.md`（138行）。

核心发现总结：

**Step-independent 不是一个有意的算法设计，而是工程路径依赖的产物。** 六个根因按证据强度排序：

1. **Single-turn RLHF 基础设施继承** — verl 最明确：把 multi-turn 拆成 Triplet 让每步"independently optimized as a valid RLHF trajectory"，本质是为了兼容已有代码
2. **Context window 硬约束** — 10步 episode 轻松超 30K tokens，4K-8K context 模型物理放不下
3. **GPU OOM** — OpenRLHF 多个 issue 显示 8B 模型在 H100 上都 OOM，per-step 大幅降低显存需求
4. **Batching 效率** — SkyRL-Agent 通过 per-step 分解获得 1.55x 加速
5. **GRPO/PPO 算法假设** — 设计给 single-turn 的 group-normalized advantage 在 multi-turn sparse reward 下坍塌
6. **经验误读** — Verlog 发现 memory_length=1-2 效果最好，造成"step-independent 足够好"的错觉

论文可以用这些证据支撑 "diagnosing the hidden cost of community default practice" 这个 contribution，重点引用 verl-agent（GiGPO）、SUPO、ArCHer、Verlog。

---
