# paper research

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_research_20260518T031456_result.json`
- **Structured JSON:** [`19bc5a81874f48b3e1cd.json`](../../sessions/19/19bc5a81874f48b3e1cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已添加 3 篇 RL 训练不稳定性论文：

1. **gao_reward_overoptimization_2023** — Gao, Schulman, Hilton (ICML 2023, `2210.10760`). Reward overoptimization 的 scaling laws，奠基性工作。与我们的关系：pruning 降低模型容量可放大 proxy-gold reward gap。

2. **rl_plus_collapse_2025** — Dong et al. (arXiv `2508.00222`). RLVR 导致 capability boundary collapse（pass@1 升但 pass@k 降）。与我们的关系：pruning-induced collapse 是其结构性变体，剪枝移除的容量加剧了 on-policy sparse-reward 不稳定性。

3. **comedy_of_estimators_2025** — Shah, Bengio, Courville et al. (arXiv `2512.21852`). KL regularization 实现中梯度计算错误导致训练不稳定。与我们的关系：剪枝后 policy distribution 偏移时，KL 估计误差对 RLVR recovery 稳定性的影响。

---
