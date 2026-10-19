---
loop: 13
reason: max_messages
updated: '2026-05-25T17:59:18+00:00'
---

### 1. 🔴 硬约束 / 红线
- 论文正文严格 8 页（EMNLP 2026 ARR），当前用 `\enlargethispage{\baselineskip}` 在 conclusion.tex 卡住最后一行，任何正文改动都要重新验证页数
- abstract 不超过 200 words
- ARR Responsible NLP Checklist 在 OpenReview form 里填写，不放进 PDF
- Limitations 只能有一个，在正文里（appendix 不能有 limitations section）
- 匿名链接必须用 `anonymous.4open.science`，不能用 GitHub URL

### 2. 🖥️ 基础设施快照
- 论文目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/`
- 图片目录：`figures/paper/`（11 张 PDF，通过 `\graphicspath{{../figures/paper/}}` 引用）
- `acl.sty` + `acl_natbib.bst`：与 GitHub `acl-org/acl-style-files` master 完全一致（已 diff 验证）
- 编译：`pdflatex`，18 页（正文 8 + Limitations 1 + References 1 + Appendix 8）
- `inconsolata` 包系统未安装（`kpsewhich` 确认），注释掉是正确的
- GPU/服务器信息：本轮未涉及实验，需要时查 `get_project_status`

### 3. 📊 当前状态
本轮主要做论文排版修复：
1. 把 retention figure 从正文移到 appendix，压缩 §4.5-4.6 + Conclusion 文字，解决 8 页溢出
2. 修正 abstract 匿名链接（GitHub → anonymous.4open.science）
3. 完成 ACL 官方模板 diff：acl.sty/acl_natbib.bst 完全一致，删除了未使用的 subcaption 包
4. PDF 已上传给用户（`main_v20260525_page_fix.pdf`）
5. 论文质量审计：9 critical 全是 missing_image false positive（隔离目录问题），内容/视觉模块因 API 限额未执行

Registry 里无 RUNNING/PREPARING 实验。项目处于审稿阶段（review_chat_id 已配置）。

### 4. 📋 待办
- 用户回复模板对比报告 → 按反馈调整（当前已报告无实质性差异）
- 审稿报告回传 → Read `review-report-action.skill.md`，Holistic Pass + Per-Comment Action Matrix
- 用户要求内容修改 → 改完后必须重新编译验证 8 页限制（conclusion.tex 的 `\enlargethispage` 余量极小）

### 5. 🎯 战略上下文
- 项目核心结论：KL divergence 做 sparsity prediction 的训练目标，signal type（output distribution vs intermediate）比 coupling（end-to-end vs per-layer）更重要（9.47 vs 2.08 PPL gap）
- 已进入审稿阶段，主要工作是论文打磨而非新实验
- 易错点：正文极度卡满 8 页，任何文字增加（哪怕 1 行）都会溢出到第 9 页。Conclusion 段落已用 `\enlargethispage{\baselineskip}` 强制多挤一行，这是最后手段
- `orphan_bib_key`：`raffel2020c4` 未被引用，可清理但非紧急
- Cross-Architecture 段落（experiments.tex L201-205）已被压缩过，再压缩需谨慎保留关键信息
