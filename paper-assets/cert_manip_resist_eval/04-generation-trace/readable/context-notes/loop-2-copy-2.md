# reviewer / loop_2.md

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`0acbe550581c28f28ceb.json`](../../sessions/0a/0acbe550581c28f28ceb.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-23T19:51:06+00:00'
---

### 1. 🔴 硬约束 / 红线
- 当前无 GPU 任务，但若恢复实验需确认 seetacloud-rtx6000 的 `execution.gpu_ids` 白名单再操作
- 匿名仓库 remote 含 token（`ghp_***`），禁止在任何输出中暴露完整 token
- 论文 abstract 不超过 200 words（EMNLP 2026 硬约束）
- Limitations 只放正文，appendix 不能有 limitations section
- abstract.tex 与 main.tex 中的 abstract 存在双源问题（之前发现自相矛盾），修订时必须确认 single source of truth

### 2. 🖥️ 基础设施快照
- 服务器：seetacloud-rtx6000，代码根目录 `/root/cert_manip_resist_eval`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/`
- 数据文件：`docs/paper/data/` 下 18+ JSON（15 个 V2 corrected + 原始）
- 匿名仓库：99 文件，commit 3d1671d，**仍为 V1 代码**，待推送 V2
- 无活跃进程 / 无 tmux / 无 cron（纯写作阶段）

### 3. 📊 当前状态
**V2 bug fix 全量完成。** 我审查了全部 15 个 V2 Worker 的输出，均已 post 给 Director。最后完成的是：
- Figure 2 regime transition 图（视觉审查 PASS）
- Appendix 三件套 V2 重跑（cross-benchmark IV / Cinelli-Hazlett / stability split）
- Fractional logit V2、alt diversity V2、epsilon sensitivity K5 V2
- Data traceability audit（118 个数字，52 个 V1 待更新，5 个内部矛盾）

**Paper Agent 正在处理**：4 张 figure 重绘 + appendix 小改。论文文本据 ROADMAP 已全面修订。

**无 RUNNING/PREPARING 实验。** 无等待中的 Worker 回调或 Cron。

### 4. 📋 待办
- Paper Agent 提交章节审查 → 按 §5 模式 B 做对抗审查（叙事一致性、claim-evidence 匹配、审稿人攻击面），注意前置读 `paper-quality-lessons.skill.md`
- Figure 3/4（GAM 相关）完成 → 视觉审查，确认不再包含 6:6 split 叙事
- Appendix 更新完成 → 核验 3 个数字：RV 9/24→12/24，fractional logit 93.1%→98.6%，epsilon max Δβ 0.067→0.073
- 匿名仓库推送 → 确认包含 V2 修正代码（`_is_valid_score()`）和全部 corrected JSON
- 最终编译 → 检查 8 页限制、abstract ≤200 words、无 LaTeX warnings

### 5. 🎯 战略上下文
**核心结论（V2 修正后）**：
1. K_eff 与 ASR **一致正相关**（12/12 OLS，GAM 12/12 positive）——多样性增加脆弱性，反 CJT/BFT 直觉
2. **Predictor shift**：K=3 η_max(3)≈K_eff(4) 共存 → K≥5 K_eff 主导(10/9)，η_max 消失(0)
3. **Aggregation gradient**：Threshold R²=0.83 → Bayesian R²=0.09，无方向反转

**已死 claim（V1 artifact）**：6:6 attack-type split、Bayesian reversal。论文中任何残留都是错误。

**最容易判断错的事**：
- K_eff "12/12 significant" 是 OLS 结论。Wild cluster bootstrap 给 4/12(K3)→10/12(K5)→9/12(K7)。Alt diversity clustered SE 更保守仅 1/12。**不要 claim "universally significant" 而不注明推断方法。**
- arc×sycophancy 和 arc×authority 在**所有 K 值、所有推断方法**下 K_eff 均不显著——如果有人问"为什么不是 12/12"，答案在这两个条件
- Worker 汇报有时用 "all conditions direction" 计数（12个），有时用 "significant conditions direction" 计数（仅显著的），导致同一指标出现不同数字（如 Bayesian 8+/4- vs 5+/1-）——前者是全部条件 OLS 方向，后者是仅显著条件方向，两者互洽
- keff_distribution.json（mean=1.92）vs keff_distribution_corrected.json（mean=2.18）的差异不是 V1 bug 导致的，是 MI 方法变更（simple MI → Gaussian copula MI）


---
