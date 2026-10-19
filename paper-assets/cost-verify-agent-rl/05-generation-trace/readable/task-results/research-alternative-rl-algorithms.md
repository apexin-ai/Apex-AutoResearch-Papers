# research alternative rl algorithms

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_alternative-rl-algorithms_20260514T131751_result.json`
- **Structured JSON:** [`f32bbd4e48fe72bce269.json`](../../sessions/f3/f32bbd4e48fe72bce269.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/literature_rl_alternatives.md`（save_project_file 不允许该文件名，白名单仅 memory.md/paper_framing.md/writing_plan.yaml，已转写到 artifacts 目录）。

## 关键结论

**最推荐：SPEAR（P0）** — Tencent Youtu，ICLR 2026
- 同设置 ALFWorld + Qwen2.5-1.5B 上对 GRPO **+16.1% success（72.8→88.9）**
- 三个问题全覆盖：tool-call bonus（解决初期 sparse）+ cosine decay 到 0（解决 gaming）+ SIL replay buffer（解决 collapse）
- 基于 GRPO 修改，代码开源；超参：N_D=2000-4000, T_warmup=T_decay=200, KL=0, clip-higher 0.28/0.2

**次推荐组合：DAPO 组件 + GiGPO（P1）**
- DAPO **Dynamic Sampling** 直接解决我们「group reward 全相同→零梯度」问题；**Clip-Higher (0.28/0.2)** 防 entropy collapse
- GiGPO 用 anchor state grouping 做 step-level credit assignment，ALFWorld +12%，已在 verl-agent 中实现

**已纠正原 task 的两点**：
- "GDPO = Group Distributionally-robust"：搜不到该名工作；存在的 GDPO 是 NVlabs 的 "Group reward-Decoupled"（多奖励解耦，作用不同）
- "DAPO = Decoupled Alignment PO"：实际是 "Decoupled Clip and Dynamic sAmpling PO"（ByteDance）

**重要风险提示**：DAPO Dynamic Sampling 单用会在 success≈0% 初期丢弃所有 group → 无法启动训练；必须配 SPEAR 式 bonus 或 SFT warm-up。

完整调研含 13 个算法的论文、公式、超参、集成方案、风险评估，以及短期/中期落地建议——见上述 md 文件。

Sources:
- [SPEAR — Learn the Ropes, Then Trust the Wins (arXiv 2509.22601)](https://arxiv.org/abs/2509.22601)
- [GiGPO — Group-in-Group Policy Optimization (arXiv 2505.10978)](https://arxiv.org/abs/2505.10978)
- [DAPO — Open-Source LLM RL System at Scale (arXiv 2503.14476)](https://arxiv.org/abs/2503.14476)
- [EPO — Entropy-regularized PO (arXiv 2509.22576)](https://arxiv.org/abs/2509.22576)
- [GTPO — Gradient and Entropy Control (arXiv 2508.03772)](https://arxiv.org/abs/2508.03772)
- [GDPO — Group reward-Decoupled (arXiv 2601.05242)](https://arxiv.org/abs/2601.05242)
- [VAPO — Value-Augmented PPO (arXiv 2504.05118)](https://arxiv.org/abs/2504.05118)
- [ARPO — Agentic Reinforced PO (arXiv 2507.19849)](https://arxiv.org/abs/2507.19849)
- [RAGEN/StarPO-S (arXiv 2504.20073)](https://arxiv.org/abs/2504.20073)
- [MT-GRPO — Turn-Level Reward (arXiv 2505.11821)](https://arxiv.org/abs/2505.11821)
- [SPEAR code](https://github.com/TencentYoutuResearch/SPEAR)
- [GiGPO code (verl-agent)](https://github.com/langfengq/verl-agent)
- [DAPO project page](https://dapo-sia.github.io/)
- [EPO code](https://github.com/WujiangXu/EPO)

---
