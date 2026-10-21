# research paper status review

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper-status-review_20260517T205050_result.json`
- **Structured JSON:** [`ea2ff7d5a443bdac5a53.json`](../../sessions/ea/ea2ff7d5a443bdac5a53.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No mention of "random reweight" baseline in the paper yet. Here's the full audit:

---

## 论文章节更新清单

| 章节 | 当前状态 | 需要的更新 | 依赖实验 |
|------|----------|-----------|----------|
| **Abstract** | 写好，数据基本准确 | (1) 更新 capture ratio 从"gap 0.013"到最新 aggregate 数据（83.5%，paper_framing 已更新）；(2) 加入 random reweight baseline 作为 "min > random" 证据句 | random_reweight_seed456 (RUNNING) |
| **Introduction** | 完整，数据已嵌入 | (1) L23 "capturing ~76%" 需更新为 ~83.5% 或表述为 "comparable"；(2) grid-best 从 b=0.5 改为 b=0.3 的语境已反映，但 cross-seed 数据仍 pending | grid_b0_3_seed123_r2 (RUNNING) |
| **Method** | 完整，无数据依赖 | (1) §hyperparameters L131: n_min=⌊B/2⌋ 规则现有 bs=4, bs=8 验证。加入 "validated at B∈{4,8,16}" 待 bs16 完成 | batchsize16_nmin8_r3 (RUNNING) |
| **Experiments** | 完整 | (1) Baselines 列表缺 **Random Reweight** baseline（随机打乱 q-score 后做 adaptive），这是 Claim 1 的关键消融；(2) 可扩展 $\rho \in \{0.2, 0.4, 0.6\}$ 如 ρ=0.2 数据到位 | random_reweight_seed456 (RUNNING), rho02_adaptive_tau08 (RUNNING) |
| **Results §Main** | tab_main 已有 3-seed 数据 | (1) 加入 **grid b=0.1** 数据点 (PPL=17.657) 到 appendix grid table — 确认 U-shape 回升，b=0.3 为真 grid-best；(2) 加入 **Random Reweight** baseline (seed123: 17.8, 与 uniform 持平或更差) 证明 adaptive 优势不是来自任意 reweight | random_reweight_seed456 (RUNNING) |
| **Results §Sensitivity** | bs=8 已写 (PPL 17.66) | (1) bs8_auto_nmin_r5 (PPL=17.66) **已确认**现有文本准确；(2) 加入 bs=16 结果扩展 coupling rule 验证；(3) batch_adaptive_tau_rho06 (PPL=17.73) 可加入 Discussion 强化 "fixed τ suffices even at ρ=0.6" | batchsize16_nmin8_r3 (RUNNING) |
| **Results §Regime** | 数据完整 (seed42) | (1) ESS-only cross-seed 数据 (seed123/456) 到位后可升级统计显著性检验为 "3-seed confirmed" | ess_only_seed123_r2, ess_only_seed456_r2 (RUNNING) |
| **Discussion** | 完整 | (1) 加入 batch_adaptive_tau 在 ρ=0.6 也失败的数据 (PPL=17.73)，强化 "simplicity validated" 论点；(2) 若 ρ=0.2 数据到位，加入 τ≈1−ρ/2 规则第 3 个验证点 | rho02_adaptive_tau08 (RUNNING) |
| **Limitations** | 完整 | (1) 若 bs=16 + ρ=0.2 到位，可缩小 limitation scope（"tested at B∈{4,8,16}" 和 "ρ∈{0.2,0.4,0.6}"） | batchsize16_nmin8_r3, rho02_adaptive_tau08 (RUNNING) |
| **Conclusion** | 简洁准确 | 无重大更新需求，待其他章节稳定后微调数字 | — |
| **Appendix §Grid** | tab_grid_full 只到 b=0.3 | **加入 b=0.1 (PPL=17.657)**，补全低端数据，展示 U-shape | ✅ grid_b0_1_seed42 已完成 |
| **Appendix §ρ=0.6** | 单 seed | (1) 加入 batch_adaptive_tau@ρ=0.6 负面结果 (PPL=17.73)；(2) 若 ρ=0.2 到位加新 appendix section | rho02_adaptive_tau08 (RUNNING) |

---

## 优先级排序（按紧迫度）

**可立即更新（数据已就绪）：**
1. Appendix grid table 加入 b=0.1 (PPL=17.657)
2. Results/Discussion 加入 batch_adaptive_tau@ρ=0.6 负面结果 (PPL=17.73)
3. bs8 结果确认（当前文本已准确，无需修改）

**等待 RUNNING 实验后更新：**
4. Random Reweight baseline 加入 Experiments + Results（等 seed456 完成凑 2-3 seeds）
5. ESS-only 3-seed 统计显著性升级（等 seed123/456 r2）
6. Grid b=0.3 cross-seed（等 grid_b0_3_seed123_r2）→ 决定 tab_main 中 grid-best 行是否升级为多 seed
7. bs=16 coupling rule 扩展（等 batchsize16_nmin8_r3）
8. ρ=0.2 全套数据（等 rho02_adaptive_tau08 + uniform retrain）→ Claim 3 scope 扩展 + τ≈1−ρ/2 验证

**关键缺口（论文叙事完整性）：**
- **Random Reweight** 是 Claim 1 的重要消融（证明 adaptive 优势来自 principled selection 而非 any reweighting），当前论文完全没提，需在 deadline 前补入

---
