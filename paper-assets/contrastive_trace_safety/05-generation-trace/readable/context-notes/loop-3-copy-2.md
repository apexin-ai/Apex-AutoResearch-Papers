# agent / loop_3.md

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_3.md`
- **Structured JSON:** [`d924c9351b509420e6b9.json`](../../sessions/d9/d924c9351b509420e6b9.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_wall_time
updated: '2026-05-21T19:25:27+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目无 GPU 分配（纯论文写作阶段），不要尝试提交任何训练实验
- 论文 main text 严格 8 页限制（EMNLP 2026 ARR），Discussion 用 `\enlargethispage{4\baselineskip}`（已被外部从 18 改为 4），Conclusion 必须在 page 8，Limitations 从 page 9 开始（exempt）。任何编辑后必须 `pdftotext -f 8 -l 8 main.pdf` 验证 Conclusion 在 page 8
- discussion.tex 已被 Director/Paper Agent 外部修改（¶1 加了架构覆盖限制句、¶3 重写了 methodological 区分、enlargethispage 从 18→4），不要回退这些改动
- 7 个 PREPARING 实验已批量标记 DONE(killed)——路由经过完整状态机（PREPARING→PENDING→QUEUED→ALLOCATED→RUNNING→DONE），因为 registry 无 CANCELLED 状态

### 2. 🖥️ 基础设施快照
- 本地工作目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/`
- 论文源码：`docs/paper/`，编译 `cd docs/paper && latexmk -pdf main.tex`
- Python：`/usr/bin/python3` (3.14.4)，PEP 668 管理，matplotlib 已全局可用
- PaperBanana venv：`/home/ubuntu/.paperbanana_venv/`（安装了 paperbanana，但 Gemini API 需指定 `--vlm-model gemini-2.5-flash --image-model gemini-2.5-flash-image`，默认模型名不对）
- 无活跃 GPU 进程、无 cron、无 tmux session
- 实验数据全在 `artifacts/` 和 `checkpoints/` 目录，不在远程服务器

### 3. 📊 当前状态
刚完成 R24 审稿修复三项计算任务并汇报 Director：
1. **Cohen's d**：OT-7B d=1.12 (large)，R1-32B d=0.58 (medium)——已汇报，待 Paper Agent 写入论文
2. **Figure 2 图例**：`scripts/plot_window_ablation.py` 已修改，legend 用 bbox_to_anchor 移到图外，PDF/PNG 已重生成
3. **AUROC layer 验证**：4 个模型 AUROC-best layer 全部确认正确（L13/L1/L32/L31）

另外已完成但未在本轮提及的：
- 概念图 `fig_concept.pdf/png` 已生成（matplotlib 手写，art_20260521_d068b6），待 Director 决定是否插入论文及位置
- Rebuttal 模板 `artifacts/rebuttal_template.md` 已创建（art_20260521_2940d3），覆盖 5 个 anticipated concerns
- Discussion ¶3 已加入 methodological vs empirical 区分（commit 4cc541d），但后续被外部进一步修改
- Limitations 已压缩到 3 段（commit b224ae7）

Registry：全部实验 DONE，无 RUNNING/PREPARING。

### 4. 📋 待办
- Director 确认概念图插入位置 → 在 Method section 或 Introduction 加 `\begin{figure}` + 编译验证页面预算
- Paper Agent 完成 Cohen's d 写入 → 可能需要编译验证
- Figure 2 修改尚未 commit → Director 要求 commit 时执行
- 概念图生成脚本 `docs/paper/figures/gen_concept_fig.py` 尚未 commit → 同上
- Director 可能要求进一步审稿修复（R24 还有其他 items）→ 按指令执行

### 5. 🎯 战略上下文
- 项目处于 EMNLP 2026 ARR 投稿前最终打磨阶段，核心论文已基本定稿
- 两个核心 contributions：(1) metric choice reverses probe conclusions（methodological，跨数据集泛化），(2) HS advantage +15-22pp（empirical，HarmThoughts-bound）
- R1-32B 是最弱模型：d=0.58 (medium)，residualized selectivity 3.0pp < 5pp 阈值，HS advantage p=0.914 不显著——写论文时不要 overclaim R1-32B
- 页面预算极紧：Discussion 的 enlargethispage 已从 18 降到 4（外部修改），任何新增内容都可能把 Conclusion 挤出 page 8。编辑前先编译确认当前状态
- 易错点：不要把 one-sample Cohen's d（vs chance 0.5）和 two-sample Cohen's d（HS vs text）搞混——appendix 用的是 one-sample


---
