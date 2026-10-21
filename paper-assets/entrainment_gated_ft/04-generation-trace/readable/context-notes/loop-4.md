# director / loop_4.md

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_4.md`
- **Structured JSON:** [`5234ecaf93585779e5e1.json`](../../sessions/52/5234ecaf93585779e5e1.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_messages
updated: '2026-05-25T07:59:31+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目无 GPU 实验，纯论文写作项目——所有实验数据来自 Wang et al. (2025) 预训练 model zoo，不需要训练
- 论文 PDF 路径：`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.pdf`
- EMNLP 2026 ARR DDL 是 **2026-05-25（今天）**，主文严格 8 页限制（不含 References/Appendix/Limitations）
- Abstract ≤ 200 words（当前 ~154 词，合规）
- 审稿已进入 Review 阶段（Group C: review_chat_id `oc_b542b52ff24f138c42225a1d4b456e7e`），Research Director 不参与格式/投稿材料准备

### 2. 🖥️ 基础设施快照
- 无远程服务器，所有工作在本地 workspace 完成
- 论文源码：`projects/entrainment_gated_ft/docs/paper/`（main.tex + sections/*.tex）
- 图表生成脚本：`projects/entrainment_gated_ft/figures/paper/gen_fig*.py`
- 统一配色 palette：`figures/paper/palette.py`（BLUE=#4E79A7, CORAL=#C56C6C, TEAL=#59A572, AMBER=#E49444, GRAY=#999999, DARK=#333333）
- Python：`python3`（系统 Python，matplotlib 已通过 `--break-system-packages` 安装）
- 无活跃进程 / 无 GPU / 无 tmux / 无 cron

### 3. 📊 当前状态
**刚完成**：
- R21 审稿报告 Critical/Major 文本修复全部完成：
  - 全文 "saturates" → "appears to stabilize"（Abstract/Intro/Conclusion/Contributions/§4.2 标题/Figure 1 caption/Appendix）
  - §4.2 标题改为 "Per-Example Overlap Appears Stable from Minimal Attention"
  - "co-varies with model capacity" → "tracks model capacity"
  - Dual interpretation 重构为 parallel "(a) Fingerprint view / (b) Convergence view"
  - Permutation test §3.5: "conservative" → "may be anti-conservative" + 2.5× margin 论证
  - Yang & Wang (2026) 引用已验证真实（arXiv:2602.11898）
- 周俊伟排版修改全部完成：
  - Figure 1A ".024" 标签移到数据点右上方，不再与 Y 轴重叠
  - Figure 4 (alpha_routing) 前移到第 5 页（左右两栏各一图）
  - Figure 5 (task_specificity) 移到第 7 页右栏
  - 编译 PASS，21 页（8 页主文 + References + Appendix），无 critical warnings
- review_issues.yaml 已更新：R5-W2/R16-N1/R20-W4 的 R21 action items 标为 in_progress

**Registry**：无 RUNNING/PREPARING 实验（纯写作项目）
**等待中**：无 Worker 回调 / 无 Cron

### 4. 📋 待办
- 用户确认提交 → 可能需要最终 `submit_paper_to_review` 提交 Group C 做最后一轮格式检查
- Paper Agent PaperBanana Figure 2 重新生成任务此前已派给 Main Agent，但未收到结果回调——如果收到，需要替换 `figures/fig_method_overview.pdf` 并重新编译
- 如果 Review Director (Group C) 回传新审稿报告 → 按 `review-report-action` skill 处理（Holistic Pass + Action Matrix）
- R21 review_issues.yaml 中仍有多个 `open` 状态 action items（R6-W3 Table 2 n=3 标注、R16-W3 'reliable'→'moderate'、R16-W5 补 selective prediction 文献、R20-W3 Limitations 补 greedy decoding）——这些是 Minor/Info 级别，DDL 当天不一定来得及，但如果用户要求可以快速修复

### 5. 🎯 战略上下文
- **核心结论**：hybrid linear recurrent architectures 在 aggregate benchmarks 上看似等价，但 per-example 层面存在 structured predictive multiplicity（α=0.14-0.30），由 task type 而非 attention ratio 决定；per-example overlap 在 4% attention 即稳定（J≈0.10）
- **投稿定位**：EMNLP 2026 Findings（R21 Overall 3.0），empirical contribution paper
- **7 轮反复的核心顽疾 (R5-W2)**：n=5 Spearman 检验力近乎为零，claim-evidence 脱节。本轮已全文替换为 descriptive language，但结构性问题无法在不增加数据点的情况下根本解决——wont_fix 级别
- **易踩的坑**：
  - "saturates" 一词在全文中有 12+ 处，已全部替换但 author_response_r7.tex 等历史文件中仍有——这些是旧 rebuttal 不需要改
  - Figure 定位靠 LaTeX float 机制，移动 figure 定义位置会产生连锁效应——每次改完必须编译+视觉检查全部 8 页
  - `paper_compile_and_check` 的 max_pages 参数计算的是 PDF 总页数（含 appendix），不是主文页数——检查 8 页限制要看 PDF 预览而非工具返回的 pages 字段
  - `submit_paper_to_review` 需要绝对路径 + 最近 2h 内有 visual check 记录


---
