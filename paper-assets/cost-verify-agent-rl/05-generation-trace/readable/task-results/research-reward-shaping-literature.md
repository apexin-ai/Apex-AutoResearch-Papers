# research reward shaping literature

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_reward-shaping-literature_20260514T124435_result.json`
- **Structured JSON:** [`cefba297789c0786198b.json`](../../sessions/ce/cefba297789c0786198b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存到 `artifacts/reward_shaping_literature.md`。

核心发现和建议总结：

**我们的问题本质**：valid_action_bonus 可以被独立最大化（不需要完成任务），这是经典的 reward gaming。ALFWorld 的纯二值 score 加剧了 sparse signal 问题。

**5 个具体建议（按优先级）**：

1. **Success-Gated Dense Reward (G-RA)** — 只在 episode 成功时才给 dense bonus。一行代码改动，直接消除 gaming 路径。风险是如果 success rate 太低则退化为纯 sparse。

2. **GDPO 多维度独立归一化** — 对 success_reward 和 valid_bonus 分别归一化再加权组合，防止低方差 dense signal 主导 advantage。~50 行改动。

3. **DAPO Dynamic Sampling** — 过滤全零方差 group，确保每个 batch 有 success/failure 差异信号。

4. **SPEAR 式 Self-Imitation** — 混入 expert 成功轨迹作为 group 内的 anchor，解决冷启动。SPEAR 在 ALFWorld 上 5.97→93.28。

5. **渐进 Horizon 课程** — 先在简单任务 + 短 horizon 上建立 success signal，再扩展。

**ALFWorld SOTA 参考**：DERL 91.8%、SPEAR 93.28%、AgentPRM 91.0%，都远超我们当前的 0-6%。最大的 gap 在于 step-level credit assignment（GiGPO +12% over GRPO）和 self-imitation（SPEAR +16.1%）。

建议 1+3 组合是最小改动的下一步实验方案，建议 4 是 success rate 实在上不去时的 fallback。

---
