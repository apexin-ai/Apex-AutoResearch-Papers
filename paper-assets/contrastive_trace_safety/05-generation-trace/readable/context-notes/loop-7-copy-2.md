# reviewer / loop_7.md

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_7.md`
- **Structured JSON:** [`30d597c979c211afe3d5.json`](../../sessions/30/30d597c979c211afe3d5.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_wall_time
updated: '2026-05-24T01:44:17+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 westd-15904，GPU 白名单需从 `execution.gpu_ids` 确认（本 session 未实际查过，首次审查训练实验前必须核对）
- 论文 DDL 2026-05-25（ARR EMNLP 2026），主文严格 8 页，Limitations 豁免
- Abstract ≤ 200 words（当前 188 words，已合规）
- 图例不得遮挡数据曲线（hard constraint，之前 forest plot 违规过，已用 bbox_to_anchor 修复）
- 一篇文章只能有一个 Limitations section，放正文，appendix 不能有

### 2. 🖥️ 基础设施快照
- 服务器：westd-15904(root)，远程代码根目录 `/root/autodl-tmp/contrastive_trace_safety`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/`
- 论文源码：`docs/paper/`（main.tex + sections/*.tex + figures/）
- Registry：`registry.yaml`（本地 workspace 下）
- 本 session 期间无训练实验在跑，全部实验已完成，项目处于论文定稿阶段
- 无活跃 PID / tmux / cron

### 3. 📊 当前状态
刚完成 R34 未提交变更的全面验证并 post 给 Director：
- 全部 R34 变更（W4/W5/W6/W7、§4.3 压缩、§4.4→app:32b_full、§4.6 cross-ref、Discussion 扩展、Ravichander 2021 引用）均通过核实
- 我之前标记的 2 个问题（#7 "unprecedented" overclaim、#10 "encoder capacity" 用词）均已按建议修复
- PDF 视觉审查确认 8 页合规
- **这些变更仍是 uncommitted 状态**，等待 commit

本 session 完成的审查历史：数值精度扫描（4 issues）→ 图添加评估 → 2 轮 PDF 视觉审查 → R34 Action Matrix 评估 → 10 项 Claim-Evidence 对齐审计 → R34 变更验证

### 4. 📋 待办
- R34 变更被 commit → 确认 commit 内容与 diff 一致，无遗漏文件
- Director 要求新一轮写作审查 → 按 §5 审查模式 B 执行，先 Read paper-quality-lessons.skill.md
- 新 worker 通知到达 → 按维度审查（但项目已近定稿，大概率不会有新实验）
- 如收到 paper_agent_request_review → 使用 §5.3 评分模板，含 5 维度 + Overall

### 5. 🎯 战略上下文
**核心结论链**：
- C1（metric-induced layer selection bias）：CR-composite 选浅层 → threshold-based 选深层，14-61 层差异，p=0.83 vs p<0.005 逆转。已在 HarmThoughts + AdvBench + Gemma-2 复现
- C2（HS advantage）：7-8B validated（+20-22pp nested CV），32B exploratory（R1-32B +15.4pp below MDE，QwQ-32B quadratic position 完全吸收）
- C3（negative results）：7 种替代方法全部失败，control task 11-17pp above chance

**易错点**：
- R1-32B 是 32B 模型，不要混入 7-8B 的数据范围（之前 abstract 就犯过 +15pp 混入 7-8B range 的错误）
- QwQ-32B 的 p=0.133 来自 precision 比较还是 BA 比较一直有歧义——appendix L979 和主文 §4.4 都是 p=0.133，可能是同一个检验的不同引用位置，rated info
- "encoder capacity" vs "encoder quality"：PCA capacity matching 保留 advantage 说明不是容量问题而是质量问题，所以用 "quality"
- position mediation 脚注已删除（原 "9-17pp" 与 R1-8B W=3 的 24.3pp drop 矛盾）
- worker_verification_holdout_ot7b_r132b 失败是基础设施问题（模型下载太大），不是数据不一致


---
