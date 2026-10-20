# reviewer / loop_26.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_26.md`
- **Structured JSON:** [`6741bf0a56257cf547ca.json`](../../sessions/67/6741bf0a56257cf547ca.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 26
reason: max_wall_time
updated: '2026-05-28T15:57:55+00:00'
---

### 1. 🔴 硬约束 / 红线
- **D171 数据锁定生效**：所有实验数据和论文数值冻结，禁止修改任何数值/统计/表格/图表数据。仅允许 prose polish + 格式调整。
- **NVE 阈值 τ=2.0×**（D165 上调，非 1.5×）。论文中所有引用必须一致。
- **GPU 白名单**：westd-51268 的 2× RTX PRO 6000。当前无 RUNNING 实验，数据锁定期无需跑新实验（GPU 空闲合理性已正式确认）。
- **CoRL DDL 5/28 UTC 12:00 已过**。用户未响应 venue 决策，默认未投 CoRL。下一步 venue 待用户决定。

### 2. 🖥️ 基础设施快照
- 服务器：westd-51268(root)，代码根目录 `/root/autodl-tmp/event-gated-adaptive-horizon`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/`
- 论文目录：`docs/paper/`（main.tex, sections/*.tex）
- Figure 源码：`artifacts/figures/paper/*.py`（Wong palette 已全面应用）
- main.pdf：05/28 05:01 UTC 编译，45页，0 error，正文 8 页达标
- 实验统计：208 个（103 success / 43 negative / 21 failed / 40 killed），全部 DONE/KILLED
- 无活跃进程、无 tmux session、无 cron

### 3. 📊 当前状态
**刚完成**：
1. Round 7 所有 venue-independent 修复验证通过（AUROC CI, 因果声明弱化, Fisher exact, code correction, scope 限定, Figure 1 更新）
2. Polish 三件套验证：色盲友好配色 ✅、FiGAR/SPiRL 引用 ✅、~18 处写作 polish ✅
3. GPU 空闲合理性正式确认（四问评估：不需要 rebuttal 储备实验）
4. 非 CoRL venue 审稿预期评估已提交：NeurIPS 6-7/10 最优，ICML 5-6/10，AAAI 5.5-6.5/10

**等待中**：用户 venue 决策（CoRL 已过期，ICML/NeurIPS/AAAI 待定）

### 4. 📋 待办
- 用户回复 venue 决策 → 验证模板切换是否影响页数/格式/引用
- Director 下发新一轮写作修改 → 按 §5 审查模式 B 审查，特别关注 W-SF2（architecture/training confound）的防御论述
- 如切 NeurIPS → 检查 NeurIPS checklist 合规性（Limitations ≥150 words、Broader Impact、Reproducibility）
- 如 Director 要求写作优化 → 关注三个高 ROI 方向：(1) reframe "no intervention works" 为 taxonomy 贡献；(2) strengthen MPC vs imagination 理论论证；(3) quantify frozen embedding 的性能 cost

### 5. 🎯 战略上下文
- **核心结论**：trained dt_embedding + multi-rate exposure 是 CIVO 的联合充分条件（5/7 vs 0/16, Fisher p<0.001）。Frozen embedding 是唯一可靠 fix（7/7 + 6/6 prevention）。Dual critics 在 imagination 中收敛（ρ>0.999），Double Q pessimism 失效。
- **关键决策链**：D165（τ 上调 2.0×）→ D167（C2 onset rate 2/3）→ D169（C3 reframe）→ D171（数据锁定）→ D173（放弃 008d s6/s7）
- **易踩的坑**：
  1. 不要把 manipulation 环境的 NVE spike 当 CIVO——Table 3 脚注明确标注 frozen control 也有类似 spike，是环境特异性现象
  2. "008d s3 NVE=2.09×" 是历史幽灵值——实际 registry 值是 1.53×（non-CIVO）。2.09× 是 008d s1 的 trajectory waypoint（appendix line 510: 1.78→1.71→2.09→4.12）
  3. "reflects a structural vulnerability"（related_work.tex 最后一句）不违反 W-MF3——它描述 CIVO 的性质（structural vs regularization），不涉及因果路径
  4. Frozen embedding 性能很差（015b=22%, 022b=33% baseline）——如果审稿人问 "why not just freeze?"，需要诚实回答 freeze 的代价


---
