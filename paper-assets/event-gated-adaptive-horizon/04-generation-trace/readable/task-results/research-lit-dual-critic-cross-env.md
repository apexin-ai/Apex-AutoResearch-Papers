# research lit dual critic cross env

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_lit-dual-critic-cross-env_20260521T121708_result.json`
- **Structured JSON:** [`d474ec00b5a7ee2f1969.json`](../../sessions/d4/d474ec00b5a7ee2f1969.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/literature/dual_critic_cross_env_literature.md` 并注册。

核心发现：

**关于 Walker 完全预防 vs Cheetah 部分缓解：**
- Turcato et al. 2024 证明 bias 偏好是环境依赖的：Walker/Ant 偏好 underestimation，Swimmer/Reacher 偏好 overestimation
- Nauman et al. 2024 (ICML) 在 14 个任务上测试 60+ agent，确认"regularization effectiveness varies with the task"
- Ma et al. 2024 显示 policy gradient 通过 dynamics 指数级增长——Cheetah 的 credit assignment chain 更长，regularization 效果衰减更快

**关于 v1 ≈ v2（核心发现）：**
- **文献空白**：没有论文专门研究 dual-critic 收敛到相同值的现象
- CrossQ (Bhatt et al. 2024, ICLR) 证明 implicit regularization（BN）> explicit pessimism（min-of-two），甚至把 2 个 critic 降到 1 个效果更好
- 机制解释：两个 critic 训练相同 target → feature aliasing (DR3, Kumar 2022) → 收敛到相同值 → min 操作无 pessimism 效应，但 redundant parameterization 本身提供 regularization

**需要补充到 literature_map.yaml 的新论文：**
1. `turcato2024exploiting` — 环境依赖的 bias 偏好（直接解释 Walker vs Cheetah）
2. `bhatt2024crossq` — implicit regularization > explicit pessimism
3. `lyu2022darc` — DARC: double actors + regularized critics
4. `barkley2025forensic` — MBPO 环境依赖失败的系统性分析

---
