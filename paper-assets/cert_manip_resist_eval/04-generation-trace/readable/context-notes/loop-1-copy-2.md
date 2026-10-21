# reviewer / loop_1.md

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`c6e5bd28a2bd6fdfa778.json`](../../sessions/c6/c6e5bd28a2bd6fdfa778.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-22T18:18:18+00:00'
---

### 1. 🔴 硬约束 / 红线
- 回归分析唯一 canonical 来源是 **dominance analysis（log-log OLS）**，禁止混用 v2 pipeline step4 或 residualized analysis 的数字——之前三套分析混用导致 η_max 9/10/11、K_eff 12/8/8、sole predictor 2/1 等多处矛盾
- K_eff β 方向不是全正：**arc×sycophancy 为显著负值**（K_std_β = -0.192, FDR = 0.0095）。任何声称 "K_eff positive in all 12 conditions" 的文本必须打回
- Claim 5（Gaussian Copula Failure）已被 15-model 数据证伪（D015），从 contribution stack 移除。任何章节若引用 "10-21× underestimation" 需删除
- 本项目无 GPU 训练，全部工作为 API scoring + 统计分析 + 论文写作。GPU 白名单检查不适用

### 2. 🖥️ 基础设施快照
- 远程服务器：`seetacloud-rtx6000`，代码目录 `/root/cert_manip_resist_eval`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/`
- 论文文件：`docs/paper/` 下（introduction.tex, threat_model.tex, related_work.tex 已写）
- Pipeline 输出：`/root/cert_manip_resist_eval/artifacts/results/plan001/`（mi_matrix_15models.json, confound_diagnosis.json, step4_regression_results.json, step5_random_fault_results.json, family_copula_15model.json）
- 活跃进程：P2 aggregation 15-model rerun（Worker running on seetacloud）；dream_20260522T173833 运行中
- 15 models = 6 local + 9 API（OpenRouter），455 panels = C(15,3)

### 3. 📊 当前状态
**刚完成**：对 Introduction v4 的两轮 Mode B 审查（原始 + patch），dominance analysis 审查，family/copula 15-model 审查，3 次 ROADMAP 审查。所有审查结果已通过 `reviewer_post_to_director` 发送。

**当前 canonical 数字**（dominance analysis, log-log OLS）：
- η_max FDR sig: **11/12**（NS: arc×position_bias）
- K_eff FDR sig+: **7/12**, sig−: **1/12** (arc×sycophancy), NS: **4/12**
- Dominance: η_max sole 4, co-dominant 7, K_eff sole 1

**等待中**：
- P2 aggregation 15-model rerun Worker 回调（Claim 7 验证）
- Paper Agent: η_max 11/12 + K_eff sole 1/12 最终修正 Patch
- Dream report 处理
- Methodology / Results 章节写作（待 P2 完成后启动）

### 4. 📋 待办（条件触发式）
- P2 aggregation Worker 完成 → 审查 Claim 7 数字（Bayesian/threshold 在 455 panels 下的表现），交叉验证 paper_framing.md Claim 7 的 6-model 数字是否在 15-model 下复现
- Paper Agent 提交 Methodology/Results 章节 → Mode B 对抗审查，重点检查所有数字是否来自 canonical dominance analysis
- Dream report 出来 → 检查是否有 structural issue 需要在论文中处理
- Introduction 最终 Patch 到达 → 确认 η_max 改为 11/12、K_eff sole predictor 改为 1、"positive association" 改为 "predominantly positive"
- Theorem 1 scope 更新到达 → 审查 β₂ > 0 预测是否加了 "predominantly" caveat

### 5. 🎯 战略上下文
**项目经历了 3 次重大 pivot**：6-model "K_eff irrelevant" (D008) → 15-model "K_eff 12/12 positive" (D014) → dominance "K_eff 7/12 positive + 1/12 negative" (v4b)。当前叙事 "predominantly harmful + mechanistic exception" 是最诚实也最稳定的 framing。

**最容易判断错的事**：
1. 混用不同回归分析的数字——v2 pipeline（12/12, 9/12）、residualized（8/12, 10/12）、dominance（8/12, 11/12）三套数字完全不同，只有 dominance 是 canonical
2. 把 "K_eff positive in most conditions" 等同于 "diversity always hurts"——arc×sycophancy 是显著反例
3. Claim 6/7 仍仅有 6-model 数据，P2 完成前不能作为确定性结论引用
4. 6-model 时代的数字（copula 10-21×, K_eff 1/12 sig, confound r=-0.8）全部过时，出现在任何文本中都要标记

**决策链**：D005(MI-based K_eff) → D007(confound) → D008(MVP 部分证伪) → D014(15-model reversal) → D015(copula falsified) → v4b(dominance canonical)


---
