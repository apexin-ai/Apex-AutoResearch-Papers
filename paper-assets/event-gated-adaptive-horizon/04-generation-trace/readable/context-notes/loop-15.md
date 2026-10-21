# director / loop_15.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_15.md`
- **Structured JSON:** [`88a7d6eae01c8c6a4b69.json`](../../sessions/88/88a7d6eae01c8c6a4b69.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 15
reason: max_messages
updated: '2026-05-28T06:46:41+00:00'
---

### 1. 🔴 硬约束 / 红线
- D171 数据锁定生效：所有实验数值冻结，禁止修改任何数值/统计/表格/图表数据。仅允许 prose polish + 格式调整
- GPU 分配：westd-51268:cuda:0, westd-51268:cuda:1（当前空闲，Reviewer 正式确认无实验需跑——rebuttal 储备边际价值极低，EGL 崩溃阻断 008d 补种）
- 用户尚未回复 venue 决策（CoRL vs ICML），已催两次。不要擅自选 venue 或执行模板切换，等用户明确指令

### 2. 🖥️ 基础设施快照
- 服务器：westd-51268 (connect.westd.seetacloud.com)，2× RTX PRO 6000 Blackwell
- 工作目录：/root/autodl-tmp/event-gated-adaptive-horizon
- 论文目录：projects/event-gated-adaptive-horizon/docs/paper/（CoRL 2026 格式，corl_2026.sty）
- ICML 模板文件：icml2026.sty + icml2026.bst 在 docs/paper/ 中可用
- 活跃进程：无（全部实验完成，无 tmux/cron）
- 208 个实验全部 DONE（103 success / 43 negative / 21 failed / 40 killed）

### 3. 📊 当前状态
**刚做完**：Round 7 审稿的全部 venue-independent 修复（6 个 critical + 5 个 warning），Reviewer 逐项验证通过：
- ✅ 正文压缩至 8 页（CoRL 限制）
- ✅ AUROC bootstrap CI [1.000–1.000, 9:27, stratified 10000 resamples]
- ✅ 因果声明弱化为 proposed/hypothesized pathway + Figure 1 四级证据标注
- ✅ Fisher exact test 5 组对比 + seed-level anecdotal 限定
- ✅ Code correction 汇总统计 + 诊断协议 scope 限定
- ✅ Figure 1 所有数值更新（τ=2.0×, 008d s1, 009e s1）
- ✅ 色盲友好配色（Wong palette, 8 figures）
- ✅ FiGAR/SPiRL 引用补充 + 写作 polish ~18 处
- ✅ Rebuttal 预案 (artifacts/rebuttal_prep_r7.md) + Supplementary checklist

**RUNNING/PREPARING**: 无
**等待中**: 用户 venue 决策（CoRL DDL 2026-05-28 UTC 12:00，可能已过）

### 4. 📋 待办
- 用户回复"CoRL" → 直接提交（论文已就绪，审稿卡 apr_20260528T015734_0s5p 已发出待用户批准）
- 用户回复"ICML"或"NeurIPS" → 执行 ICML 切换方案（Agent 已备好清单，~40 min），切换后重新编译 + 提交审稿
- 用户长时间不回 + CoRL DDL 已过 → 向用户报告 DDL 已过，建议切 ICML 2026 或 NeurIPS 2026，查 DDL
- Supplementary 4 项收尾（venue 确定后执行）：打包 .zip、确认页数、README 上游注明、区分工作代码 vs 提交代码

### 5. 🎯 战略上下文
- **核心发现**：DreamerV3 中 trained dt_embedding 驱动 CIVO（Conditioning-Induced Value Overestimation），locomotion 特异性，frozen/removed dt_emb 可 100% 预防（Fisher p<0.001）
- **CoRL venue fit 是三次复发的结构性问题（Round 1/3/7）**，写作无法修复。Reviewer 和审稿报告一致建议切 ICML。这是下一个"你"最关键的判断：如果用户坚持 CoRL，desk reject 风险极高（W-MF2 + W-MF6），应明确告知风险但尊重用户决定
- review_issues.yaml 已更新至 Round 7（所有 venue-independent issues resolved/in_progress）
- 易错点：appendix 中部分 figure（nve_roc_curve.pdf 等）可能仍用旧配色（源码在远程服务器），影响有限但如果 Reviewer 追问需要处理


---
