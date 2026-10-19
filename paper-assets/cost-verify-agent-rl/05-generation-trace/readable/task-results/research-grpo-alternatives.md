# research grpo alternatives

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_grpo-alternatives_20260514T133446_result.json`
- **Structured JSON:** [`b4f57238431cf2d37ba2.json`](../../sessions/b4/b4f57238431cf2d37ba2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存至 `artifacts/grpo_alternatives_survey.md`。核心结论：

---

## 推荐排序

**#1 SPEAR** ([arXiv:2509.22601](https://arxiv.org/abs/2509.22601), ICLR 2026, [GitHub](https://github.com/TencentYoutuResearch/SPEAR))
- **直接在 ALFWorld 上验证，GRPO 基础上 +16.1% success rate**
- 课程式自模仿学习：前期用 auxiliary reward 探索，后期从 replay buffer 中 self-imitation
- Plug-and-play 叠加在 GRPO 上，同时解决 cold-start 和 reward gaming
- 额外开销仅 10-25%

**#2 GiGPO** ([arXiv:2505.10978](https://arxiv.org/abs/2505.10978), NeurIPS 2025)
- **ALFWorld 上 GRPO +12%**
- 两层分组：episode-level + step-level anchor state grouping
- 即使 episode reward 全同，step-level advantage 仍有区分度
- Critic-free，保持低内存

**#3 SPA-RL** ([arXiv:2505.20732](https://arxiv.org/abs/2505.20732), [GitHub](https://github.com/WangHanLinHenry/SPA-RL-Agent))
- ALFWorld 验证过，训练 progress estimator 将 sparse final reward 重分配为 step-wise dense reward
- 从根本上消除 zero-advantage 问题

**#4 DAPO** ([arXiv:2503.14476](https://arxiv.org/abs/2503.14476)) — 最小改动方案
- Clip-Higher + Dynamic Sampling 改几行代码可集成
- 但不解决 cold-start（success=0% 时 Dynamic Sampling 无数据可用）

**推荐路径**: exp015 失败 → 先快速加 DAPO 的 Clip-Higher → 再叠加 SPEAR 的 self-imitation + curriculum → 如仍不够则换 GiGPO 作为 base optimizer。

Sources:
- [SPEAR - ICLR 2026](https://arxiv.org/abs/2509.22601)
- [GiGPO - NeurIPS 2025](https://arxiv.org/abs/2505.10978)
- [SPA-RL](https://arxiv.org/abs/2505.20732)
- [DAPO - ByteDance](https://arxiv.org/abs/2503.14476)
- [SAGE](https://arxiv.org/abs/2602.03143)
- [HAPO - Amazon](https://arxiv.org/abs/2603.11321)
- [GDPO - NVIDIA](https://arxiv.org/abs/2601.05242)

---
