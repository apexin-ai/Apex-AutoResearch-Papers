# research plan005 negative literature

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_plan005-negative-literature_20260514T020402_result.json`
- **Structured JSON:** [`35e9eb5638ba2d94c1cf.json`](../../sessions/35/35e9eb5638ba2d94c1cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**调研报告** → `artifacts/plan005_negative_literature.md`
**文献地图** → `literature_map.yaml` 新增 5 篇论文（reward-shaping category）

### 核心结论

plan005 的 NEGATIVE 结果（ISR 降低 prove_rate）是 multi-objective RL 中已知的 **auxiliary reward degradation** 现象，5 篇论文从不同角度确认：

1. **Gao et al. (2024)** — process reward 在 RL 训练中可能**比 success-only reward 更差**
2. **Ye et al. (2025, PROF)** — 朴素混合 PRM+ORM 导致退化，需 consistency filtering
3. **Moskovitz et al. (2023, ICLR 2024)** — 固定权重线性组合存在过度优化阈值
4. **Skalse et al. (2022, NeurIPS)** — 理论证明：任何非常数 proxy reward 都可能降低 true reward
5. **Rezaei et al. (2026, PROGRS)** — 无条件 process reward 会放大失败模式，需 outcome-conditioned centering

**推荐改进方向**：Bonus-only + Outcome-conditioned ISR（仅对 prove 成功的样本施加正向 ISR bonus），实施复杂度低且同时解决 hackability 和 gradient corruption 问题。

Sources:
- [Gao et al. - On Designing Effective RL Reward](https://arxiv.org/abs/2410.15115)
- [Ye et al. - Beyond Correctness (PROF)](https://arxiv.org/abs/2509.03403)
- [Moskovitz et al. - Confronting Reward Model Overoptimization](https://arxiv.org/abs/2310.04373)
- [Skalse et al. - Defining and Characterizing Reward Hacking](https://arxiv.org/abs/2209.13085)
- [Rezaei et al. - PROGRS](https://arxiv.org/abs/2604.02341)

---
