---
loop: 13
reason: max_messages
updated: '2026-05-25T15:40:08+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 分配见 `get_project_status`，不要占用其他项目的卡
- Figure 5 C4 band 已从 Qwen-14B 换成 Qwen-7B（本轮修复），不要再把 14B 数据放回 band
- 论文正文严格 8 页（当前恰好 8 页），任何编辑后必须重新编译检查页数
- `\raggedbottom` 已删除以对齐 ACL 官方模板，不要加回来
- 附录 "Use of AI Assistants" section 只提 coding/writing/literature review 三点，不要加其他内容，不要加 "manually reviewed" 之类的话（用户明确要求删除）
- Related Work 保持 3 个小节，不增不减

### 2. 🖥️ 基础设施快照
- 论文目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/`
- plot 脚本：`scripts/plot_fig_jsd_decay.py`（本地 Python3 + matplotlib 可直接跑）
- `acl.sty` 和 `acl_natbib.bst` 与 GitHub `acl-org/acl-style-files` 官方版完全一致（已 diff 验证）
- `inconsolata.sty` 本地未安装，官方模板说 "may be commented out"，提交 Overleaf 时建议加上
- 编译：`paper_compile_and_check(project="gen-depth-contamination")` 或本地 `pdflatex`
- 无活跃 GPU 实验（本轮全部是论文格式工作）

### 3. 📊 当前状态
本轮主要处理论文格式和一致性修复，全部完成：
- ✅ Figure 6 右栏放置（discussion.tex float 位置调整）
- ✅ Table 23 附录右移修复（minipage → table float）
- ✅ 22+ 处 AI 写作模式（", -ing that..."）替换为独立从句
- ✅ Figure 5 不一致：Qwen-14B → Qwen-7B，figure 已重新生成
- ✅ Figure 5 caption 更新为 "4 model-mode pairs + 4 Pythia decoding variants"
- ✅ ACL 官方模板对齐：`\raggedbottom` 删除，acl.sty/bst 验证一致
- ✅ 附录 AI Assistants section 精简（只保留 coding/writing/literature review）
- 无 RUNNING/PREPARING 实验，无等待中的 Worker 回调
- 项目处于审稿阶段（review_chat_id 已配置）

### 4. 📋 待办
- 收到审稿报告 → 按 `review-report-action` skill 处理，先 Holistic Pass 再 Per-Comment Action Matrix
- 用户要求补充实验/修改内容 → 编辑后必须 `paper_compile_and_check` 验证 ≤8 页
- 提交 Overleaf 时 → 加上 `\usepackage{inconsolata}`（本地缺包但 Overleaf 有）
- 如需重新提交审稿 → `submit_paper_to_review`

### 5. 🎯 战略上下文
- 核心结论：C4 web text K\*≤2（10 configs, 6/10 K\*=2），arXiv K\*=3，one-wash laundering effect
- 论文 framing 稳定，实验矩阵完整，当前处于投稿前最终打磨阶段
- **易错点**：Figure 5 band 的 8 configs 不等于论文正文的 "6/10 K\*=2"——band 包含 4 个 Pythia 解码变体（属于 ablation，不在 10 core configs 之列）。下一个"你"不要试图让 band 正好等于 6
- **易错点**：exp_001 (Pythia-1.4B) registry 中无 pairwise_jsd 字段，JSD 数据在远程服务器分析脚本产出中，不要因为 registry 没有就认为缺失
- **易错点**：M025 教训——pipeline 默认是 greedy 解码（`--no_sample`），任何新 Pythia 实验必须显式设 nucleus 参数
- 决策链：D-series 在 `decisions.yaml`，关键决策包括 method→analysis 贡献切换（已完成，论文定位为 systematic analysis 而非 new method）
