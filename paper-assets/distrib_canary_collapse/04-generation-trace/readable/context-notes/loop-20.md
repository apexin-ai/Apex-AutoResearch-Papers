# director / loop_20.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_20.md`
- **Structured JSON:** [`93fefa96b5f28493dd85.json`](../../sessions/93/93fefa96b5f28493dd85.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 20
reason: max_messages
updated: '2026-05-24T00:23:44+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-17855 cuda:0-5, westd-19828 cuda:0-1。不得使用白名单外的卡
- 1.4B 实验 D102 必须用 downstream=distinct_1,distinct_2,distinct_3（6-pair basis），排除 MAUVE（D210 决策：1.4B MAUVE 系统性 ~0.033，无效）
- α_c = 0.483±0.006（sigmoid 拟合），不是 0.476（旧版）
- PPL reduction = 64%（单种子 s42），不是 58%（旧跨种子估计）
- EMNLP 2026 正文 ≤ 8 页，Limitations 不计入页数限制
- 匿名仓库 token 不得提交到代码：`[REDACTED_GITHUB_TOKEN]`

### 2. 🖥️ 基础设施快照
- **westd-17855**: connect.westd.seetacloud.com:17855, user=root, 6 GPU
  - 工作目录: /root/autodl-tmp/distrib_canary_collapse
  - HF cache: /root/autodl-tmp/.hf_cache（gpt2-large 已缓存）
  - 活跃进程: 无（8/8 实验全部完成，GPU 全空闲）
- **westd-19828**: connect.westd.seetacloud.com:19828, user=root, 2× 96GB GPU
  - 同上路径配置
  - 活跃进程: 无
- 论文目录: `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/`
- 匿名仓库: `/tmp/anon_repo/` → https://github.com/anonymous-nlp-2026-2/distrib_canary_collapse (126 files, commit ffceb62)
- MAUVE backfill 脚本: `scripts/backfill_mauve.py`（已验证，但 1.4B 不需要补算）

### 3. 📊 当前状态
**刚完成**: 8/8 1.4B 实验全部完成 + 6-pair 统一 D102 分析。已向用户汇报结果，已派 Paper Agent 更新 Table 17 和 appendix。

**Registry**: 所有实验 DONE/success。无 RUNNING/PREPARING。

**等待中**:
- Paper Agent 正在处理 Table 17 更新 + appendix 1.4B 文本补充（6-pair 数据、canary asymmetry、cross-T 改善）
- Paper Agent 之前已完成 D212 framing patch（appendix K≥3 caveat、"phase-diagram structure qualitatively preserved" 措辞、intro L16 限定语）
- 数据审计已通过（0 错误，仅修正 10/15→11/15 non-confirming count）
- R10 审稿报告尚未从 Review Director 收到
- 服务器审计：向运维汇报了两台服务器均 Category A（当时在跑），现在全部空闲，可能需要重新评估是否释放

### 4. 📋 待办（条件触发式）
- Paper Agent 回复 Table 17 更新完成 → 编译验证 ≤ 8 页 → 派 Reviewer 核实数据一致性
- Paper Agent 完成所有 patch → 重新 push 匿名仓库（`/tmp/anon_repo`）→ 汇报运维
- Review Director 发来 R10 审稿报告 → 按 review-report-action skill 处理（Holistic Pass → Per-Comment Action Matrix）
- 运维再次询问服务器 → 现在 8/8 完成、GPU 全空闲，如果没有后续实验可归为 Category C
- 用户要求提交 → submit_paper_to_review 给 Review Director

### 5. 🎯 战略上下文
**项目核心结论**: Pythia-410M 13-α 检测景观 + 5 家族跨架构验证。PermG 是唯一 FPR=0% 的方法。α_c(T) 幂律递减，entropy cascade leads diversity ≥1 gen。

**关键决策链**:
- D210: 1.4B 用 distinct_3 替代 MAUVE 作为 downstream
- D211: 1.4B α=0.50 T=15 entropy canary 失效，ECE-only；cross-T PermG 反转因 entropy 非单调
- D212: framing 调整 — "phase-diagram structure qualitatively preserved" + K≥3 onset caveat + "scale-robust"

**易错点**:
- 1.4B 结果对比时 pair basis 必须统一（6-pair）。s42 旧实验用了 8-pair（含 MAUVE），不可直接与 s43/s44 6-pair 比较
- α=0.45 T=15 PermG 5/6 > α=0.50 T=15 PermG 3/6 是 marginal significance artifact（Reviewer #163），不是真实 dose-response 反转。不要在论文中并排报告
- Table 17 曾有 M080 错误（T=10 s43 数据放在 T=15 s43 列），已修复但新增列时注意不要重蹈
- `\section*{}` 用于 AI Assistants section（appendix 字母计数器已超 26）
- westd-17855 不在本地 SSH config 中（之前误报 offline），Agent 通过 MCP SSH 工具连接


---
