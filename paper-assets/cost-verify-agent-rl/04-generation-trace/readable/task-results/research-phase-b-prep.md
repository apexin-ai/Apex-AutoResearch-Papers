# research phase b prep

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_phase_b_prep_20260516T030756_result.json`
- **Structured JSON:** [`a655dbf0249099b66d6a.json`](../../sessions/a6/a655dbf0249099b66d6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已完成并注册。

**核心发现**：

1. **代码就绪度 ~85%**。`ragen/biavr/` 模块（~800 行含测试）已完整实现 reward 计算、`&lt;VERIFY>` 解析、action canonicalization、a_pre 反事实生成。已集成到 `agent_proxy.py` rollout 循环、`ctx_manager.py` prompt 构造、`agent_trainer.py` metrics 日志。

2. **剩余 P0 改动仅 ~36 行**：
   - `model_path: TO_BE_SET`（阻塞于 exp028c）
   - `step_rewards.py` 需显式接入 biavr reward（当前仅通过 history turn['reward'] 隐式传递）
   - reward normalization 中 biavr 小量（最大 0.9）可能被 episode reward（10.0）淹没

3. **`&lt;VERIFY>` token 方案推荐纯文本（方案 A）**——已完全实现，与 Thinkless 先例一致，零 tokenizer 改动。Special token（方案 B）作为 fallback。

4. **最大不确定性不在代码**：Phase A 是否通过 MVP、1.7B 模型能否学会 verify/skip 决策、action_changed 是否为 genuine signal（论文 Reviewer 攻击面 #3）。

---
