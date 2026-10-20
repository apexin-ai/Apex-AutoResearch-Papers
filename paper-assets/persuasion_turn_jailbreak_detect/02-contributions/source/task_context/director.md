---
loop: 5
reason: max_messages
updated: '2026-05-25T05:30:52+00:00'
---

### 1. 🔴 硬约束 / 红线
- 论文正文严格 8 页限制（EMNLP 2026 ARR），Limitations/References 不计入。当前刚好卡在 8 页边界，任何正文增加都可能超页
- Abstract 不超过 200 词（当前 139 词，有余量）
- 主文只能有一个 Limitations section，appendix 不能有第二个
- ARR Responsible NLP Checklist 在 OpenReview form 里填，不放 PDF 里（main.tex 中 `\input{checklist}` 已注释）
- 论文 .tex 源文件真源在本地 workspace，不在远程服务器

### 2. 🖥️ 基础设施快照
- 论文目录：`/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/`
- 图表生成脚本：`figures/paper/gen_fig*.py`（本地 python3 可直接运行）
- 编译：`paper_compile_and_check(project, max_pages=8)` — 注意 25 页总数包含 appendix+references，page_status 永远报 over_limit，需视觉确认主文 ≤8 页
- 无活跃 GPU 实验、无远程服务器、无 RUNNING 进程
- 项目处于论文提交阶段，已进入审稿阶段（review_chat_id 已配置）

### 3. 📊 当前状态
刚完成审计报告的修复并上传 v22 PDF：
- **Critical 全部修复**：appendix 3 处内部 plan ID 泄露（plan_002/plan_017）→ 描述性名称；DeBERTa 引用统一为 he2023debertav3；DeepContext 补引用
- **去 AI 风格**：主文 6 个 .tex 文件所有解释性 em-dash (---) 替换（~12 处）；5 处 -ing 分词短语重写
- **Figure 2 数字重叠修复**：`gen_fig2_cross_attack_bar.py` 重写标签逻辑，值 ≥0.995 不显示标签，近似值垂直错开
- **页数合规**：移除了之前添加的 Section 4.9（效率表），Limitations 精简，主文 8 页以内
- Registry 无 RUNNING/PREPARING 实验
- 无等待中的 Worker 回调或 Cron

### 4. 📋 待办
- 用户提交新修改意见 → 按优先级处理，改后重新编译验证 8 页限制
- 用户说"进入审稿阶段"或"重新审稿" → 调用 `submit_paper_to_review`
- 收到 Review Director 的审稿报告 → Read `review-report-action.skill.md`，按协议处理
- appendix 中仍有 ~10 处 em-dash 未清理（低优先级，用户要求时再处理）

### 5. 🎯 战略上下文
- **项目核心结论**：classification DAPT 在 base scale 恢复 OOD 检测（F1 0.97-1.0 vs vanilla 0.26-0.31），scrambled labels 等效说明结构性角色而非语义；但在人类数据上 hierarchy 反转（MLM > classification），且 355M 时 DAPT 变得不必要
- **DDL**：EMNLP 2026 ARR 提交截止 2026-05-25（今天）
- **易错点**：`paper_compile_and_check` 的 max_pages=8 会报 FAIL（因为总页数 25 含 appendix），必须视觉确认主文页数而非信任工具的 pass/fail
- **易错点**：修改正文任何内容后必须重新检查 8 页限制——当前在边界上，多一行都可能溢出
- **审计报告中"Figure 编号乱序"是误判**：审计把 appendix 的 table 错认为 figure
