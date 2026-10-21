# paper rebuttal prep expansion

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_rebuttal_prep_expansion_20260524T114857_result.json`
- **Structured JSON:** [`6d7f7500b1d3c40542ff.json`](../../sessions/6d/6d7f7500b1d3c40542ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。rebuttal_prep.md 已扩展到 15 个 Q&A：

- **Q1–Q8**：保留原内容，修正了 Q6 的 LOEO AUROC（0.981→0.988）和名称（Leave-One-Environment-Out），Q7 的实验数（132→133）
- **Q9**：DreamerV3 唯一性 — 三条件框架 (a)+(b)+(c)，TAWM MPC 免疫证据
- **Q10**：环境多样性 — 133 实验非 5 个数据点，severity continuum，D146 ordering reversal
- **Q11**：CIVO vs TD3/SAC overestimation — 共享生成模型偏差 vs 独立近似误差，ρ>0.999 收敛
- **Q12**：ManiSkill 无 CIVO — 排除 reward sparsity，三个候选 mediator，NVE 诊断验证
- **Q13**：SGS 全失败 — forward-pass 不可约性，gradient magnitude ≠ causal importance
- **Q14**：seed 数量 — 多线证据收敛，Fisher p=0.003，IQM=148.8，breadth vs depth 设计
- **Q15**：NVE 阈值敏感性 — LOEO AUROC=0.988，Youden 1.53×，[1.3×, 2.0×] 稳定

---
