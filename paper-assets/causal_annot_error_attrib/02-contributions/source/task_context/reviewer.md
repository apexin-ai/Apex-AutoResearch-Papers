---
loop: 6
reason: idle_timeout
updated: '2026-05-25T07:09:19+00:00'
---

### 1. 🔴 硬约束 / 红线
- DDL 是 **2026-05-25**（今天），所有修改必须以不破坏现有论文为前提
- 服务器账号是 **sonny**（不是 root），`/root/miniconda3` 无权限
- 工作树有 **40 个文件未 commit**（tex/figures/scripts），提交前必须 commit 否则不进 PDF
- EMNLP 2026：正文 ≤8 页（当前恰好 8 页，任何增加都会超限），abstract ≤200 words（当前 181），单一 Limitations section 在正文中
- 论文中 "sign_flips: 0" 指 **primary coefficient** sign flip（plan006 定义）；HumAID K=10 的 7/8 exposure sign flips 是 **secondary coefficient**，两者定义不同，引用时必须区分
- GPU 已释放（D021），本项目不再需要 GPU

### 2. 🖥️ 基础设施快照
- 服务器：**home-1x5090 (sonny)**，代码根目录 `/home/sonny/causal_annot_error_attrib`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/`
- 论文源文件：`docs/paper/`（main.tex 入口），PDF 36 页（正文 8 + references 2 + appendix 26）
- 标注数据：`/home/sonny/causal_annot_error_attrib/results/{humaid,vast,civil_comments}/` — 36/36 JSONL + 36/36 NPZ
- 活跃进程：无。无 cron、无 tmux、无 Worker。

### 3. 📊 当前状态
Loop #6 完成终稿前全面审查，已 post 到 Director：
- EMNLP 合规 4 项全 PASS（页数、abstract 字数、Limitations 位置和覆盖度）
- 数据一致性 7 项交叉验证全 PASS（MAPE 1.6%、M-bias 53.2%、IV 52.6%、F1 range、e2e "10 configs"、93.6% median、IV 42.1% range）
- 视觉审查 PASS（排版正常、图表清晰、无溢出）
- **WARNING：40 文件未 commit**，已提醒 Director

Registry：16 实验（15 success + 1 failed/plan003），无 RUNNING/PREPARING。无等待中的回调或决策。

### 4. 📋 待办
- **Director 确认提交** → 验证最终 PDF 的 commit hash 是否包含全部 40 个文件修改
- **收到 paper_agent_request_review** → 使用 §5.3 评分模板（维度评分 + Overall + 具体问题）
- **Director 发来 PDF 视觉审查请求** → `pdf_to_images` + `paper-visual-review` skill
- **收到新 worker_done 通知** → 按标准流程审查

### 5. 🎯 战略上下文
- 核心结论：K≥3 多分类标注误差 × 7 DAG 拓扑 = 质变（exposure/IV 可翻转符号，5 个拓扑保符号）；FWL 使 4 个 covariate 拓扑的矩阵校正无效；ASV 给出拓扑依赖的脆弱性排序
- Round 23 评分 3.5（Borderline Conference），稳固但无 quick win 推至 4.0（差距是结构性的：Conjecture 1 未证明 + 无完全真实案例研究）
- **最大风险**：40 文件未 commit。论文内容和数字已全部验证通过，但如果 Agent 不 commit 就提交，最终版本不含最新修改
- **易错判断**：Conclusion 中 "93.6%" 是 e2e demo median（不是 simulation grand mean 93.8%），两个数字来源不同但都正确；不要因 DDL 紧建议降级 venue
- **Conjecture 1 状态**：K=2 已证（Theorem 1）、K=3 symmetric 已证（Theorem 2）、general K≥3 有 545K+ 数值证据但未证明。standalone proof 有 K=2 tightness 数学错误但不在论文中，不影响提交
