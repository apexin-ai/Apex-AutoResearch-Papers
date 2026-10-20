---
loop: 5
reason: max_messages
updated: '2026-05-25T15:41:32+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目无 GPU 实验，纯论文写作项目——不涉及训练/服务器/模型路径
- 论文仓库链接必须用匿名链接 `https://anonymous.4open.science/r/policy_ambiguity_safety-5DFE/`，严禁在论文 PDF 中出现 `github.com`
- EMNLP 2026 正文严格 8 页（当前恰好 8 页，任何编辑后必须视觉验证不超页）
- 浮动体间距覆写（`\textfloatsep` 等 5 行）是维持 8 页的关键，不能删
- Abstract 不超 200 words；Limitations 只需一小段覆盖 3 个点
- 附录有 41 节，`\extAlph` 已扩展到 AO(41)，新增附录节需同步扩展

### 2. 🖥️ 基础设施快照
- 论文目录：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/`
- 编译命令：`pdflatex -interaction=nonstopmode main.tex`（需跑两遍）
- `acl.sty` + `acl_natbib.bst` 已与 GitHub `acl-org/acl-style-files` master 校验一致（MD5 match）
- `inconsolata` 包通过 `texlive-fonts-extra` 安装
- 无活跃进程/tmux/cron——纯本地编辑项目
- 产出目录：`projects/policy_ambiguity_safety/artifacts/`

### 3. 📊 当前状态
本轮完成的工作（全部是用户驱动的 pre-submission 自检）：
1. 修复 42 个附录孤立引用（7 处 main text 缺引用）
2. 修复 `\extAlph` counter overflow（34→41 entries）
3. AI 写作风格清理（em-dash 14→3，trailing -ing 8→0）
4. Abstract 脚注格式修正（匿名链接 + ACL 标准格式）
5. Introduction contributions 拆成 3 点
6. Figure 3/4 分左右两栏布局
7. 正文压缩到恰好 8 页
8. Table 7 + Temperature table 溢出修复（`\resizebox`）
9. ACL 官方模板对齐（加 `inconsolata`，确认 sty/bst 一致）

Registry: 无实验。项目处于审稿阶段（review_chat_id 已配置）。

### 4. 📋 待办
- 用户要求新一轮修改 → 任何编辑后必须 `pdflatex` 两遍 + `pdf_to_images` 视觉验证第 8/9 页边界
- 收到审稿报告 → Read `review-report-action` skill → Holistic Pass + Action Matrix
- 用户说"提交审稿" → `submit_paper_to_review`
- 用户说"推代码" → push 到 GitHub 仓库（anonymous.4open.science 自动同步）

### 5. 🎯 战略上下文
- 核心结论：policy ambiguity +34.0pp violation effect，type-mechanism dissociation（22.4% clause vs 0.4% type），convergent nocuity（41.3% majority-convergent，Jaccard 0.46 cross-family）
- 论文已基本定稿，处于 pre-submission polish 阶段
- 易错点：Figure 布局对源码位置敏感（已反复出错多次），改动 experiments.tex/introduction.tex 后必须视觉检查 Figure 是否跑位
- 易错点：正文 8 页极度紧凑，任何内容增加都可能溢出——增删内容后立即检查页数
- 审稿阶段已启动（Group C 独立审稿团队），Research Director 专注研究实验不参与投稿材料
