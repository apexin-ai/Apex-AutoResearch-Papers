# director / loop_9.md

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_9.md`
- **Structured JSON:** [`3a3811a27651294c521b.json`](../../sessions/3a/3a3811a27651294c521b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_messages
updated: '2026-05-28T16:59:32+00:00'
---

### 1. 🔴 硬约束 / 红线
- CoRL 2026 DDL: 2026-05-29（明天），8 页正文限制，必须包含 Limitations section
- 论文前 6 页已冻结（用户孙震多次强调），任何修改只能在第 7 页及之后
- Figure 3/4 必须用 wrapfigure 环绕式排版，不能占整行（用户明确拒绝过 figure[t]）
- Overview 主图 v5 数据已核对通过，Panel (c) 不能加 "p < 0.001"（论文不支持该数据）

### 2. 🖥️ 基础设施快照
- 本地工作目录：`/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/`
- 论文源码：`docs/paper/` 下（introduction.tex, claim1.tex, claim2.tex, claim3.tex, discussion.tex）
- 主图文件：`artifacts/figures/fig_overview_pb_v5.png`（最终版），`artifacts/figures/fig_overview_pb.pdf`（PDF 版本，可能需要从 v5 重新生成）
- v1 备份：`artifacts/figures/fig_overview_pb_v1_backup.png`
- PaperBanana 已安装，GOOGLE_API_KEY 已通过 secret 存储
- 无远程服务器活跃进程，无 RUNNING 实验

### 3. 📊 当前状态
刚完成：Overview 主图 v5 生成（修正了 p<0.001 数据问题），已上传飞书给用户确认。
等待中：用户对 v5 的确认 + 两个决策：
  1. v5 是否可以嵌入论文作为 Figure 1
  2. 原 Figure 1 (teaser dumbbell chart) 和 overview 图信息重叠（都展示 action collapse），保留两张还是替换
Registry 无 RUNNING/PREPARING 实验。项目处于审稿阶段（review_chat_id 已配置）。

### 4. 📋 待办
- 用户确认 v5 → 从 v5 PNG 生成新 PDF → 嵌入 introduction.tex 作为 Figure 1（figure*[t]）→ 处理 Figure 编号顺移（原 Fig1→Fig2, Fig2→Fig3...）→ 验证页数仍 ≤ 8 页
- 用户决定保留/替换原 teaser → 如替换则删除旧 figure 定义；如保留则需处理 page 2 信息密度问题
- 嵌入后 → 编译 PDF → 视觉检查第 1-2 页排版 → 确认前 6 页内容未被破坏（md5 对比 page 3-6）

### 5. 🎯 战略上下文
- 这是一篇 analysis paper：揭示 VLA collision avoidance 评估中的 action collapse 现象，提出 dfCAR 指标修正
- 两位用户：孙震（对排版极敏感，多次因页面被动而发火）、吴俊豪（主导主图需求，要求用 PaperBanana）
- 易踩坑：修改 introduction.tex 加主图时可能影响前 6 页排版 → 必须编译后逐页视觉核对
- Figure 3 wrapfigure 的 line count 参数经过 4 轮迭代才稳定在 [14]，不要轻易改动
- Figure 4 在 discussion.tex 中用 wrapfigure{R}{0.5\linewidth}，图例在 upper-right（改过，避免与 n=3 重叠）
- Figure 2 (claim1.tex) xlim 左边界已从 0 改为 -3（防空心点与 y 轴重叠）


---
