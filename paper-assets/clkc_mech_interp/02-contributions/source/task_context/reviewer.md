---
loop: 4
reason: max_wall_time
updated: '2026-05-25T20:18:22+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 westd-14391 仅 1× RTX PRO 6000，gpu_ids 未显式限定但只有一张卡，不存在越界风险
- Qwen3-8B 既是翻译模型又是实验对象——审查时注意区分这两个角色，不要因为翻译用了 Qwen 就质疑 Qwen 实验结果（论文已用 COMET + Llama/Gemma 交叉验证缓解）
- Table 1 的 77.6%/75.0%/76.2% 和 matched-condition 的 90.0%/88-89%/71-73% 是**不同实验**（全量数据 vs conflict-verified 子集），不要混为一谈标 CRITICAL
- N=136 是旧 pipeline，N=201 是 matched-condition pipeline——论文应只引用 N=201 数据，发现残留 N=136 引用才是问题

### 2. 🖥️ 基础设施快照
- 服务器：westd-14391 (root)，工作目录 `/root/clkc_mech_interp`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/`
- 论文目录：`docs/paper/`（main.tex + 分章节 .tex）
- 模型路径：`/root/autodl-tmp/models/` 下 Llama-3.1-8B-Instruct / Qwen3-8B / gemma-2-9b-it
- 数据：`/root/clkc_mech_interp/data/{llama31,qwen3,gemma2_v2}/`
- **数据缺口**：Llama/Qwen 无 `zh_activations.pt`、无 `zh_conflict_*.jsonl`、无 DE 数据。仅 Gemma 有完整 EN+ZH 数据
- 无活跃 GPU 进程，无 tmux session，无 cron

### 3. 📊 当前状态
本轮审查了 ~15 个 worker 完成通知，覆盖：fig1/fig2 PaperBanana 重设计、fig4/fig5 样式修复、ACL 模板对齐、数据一致性修复（abstract/conclusion/appendix）、页数溢出修复（两轮）、fig 间距调整、paper audit、数据完整性审计。

**关键未解决问题**：
1. **Table 1 源数据不可追溯**：bootstrap_n2000.py 脚本在但无输出，ZH activations 缺失导致无法重新生成。Director 已收到 WARNING。
2. **method.tex L65 残留 "136 vs. 272"**：应为 N=201，尚未确认是否修正。
3. **Registry L13 flip count**：仍记录 66/201（实际 57/201），多次提醒但未确认修正。

无 RUNNING/PREPARING 实验。等待 Director 决定是否用 GPU 重新生成 ZH activations。

### 4. 📋 待办
- Director 批准 ZH activation 重新生成 → Worker 完成后验证 bootstrap_n2000 输出是否与 Table 1 一致（77.6%/75.0%/76.2%）
- Round 4 审稿请求到达 → 按 §5 审查模式 B 执行对抗审查，必须先 Read paper-quality-lessons.skill.md
- 论文最终提交前 → 核查 method.tex L65 的 N=136 残留、registry flip count 修正、匿名仓库 URL 与 abstract footnote 一致
- 收到 paper_agent_request_review → 使用 §5.3 评分模板，含维度评分

### 5. 🎯 战略上下文
- 核心叙事已从 "within-Llama L28 vs L13 层间解离" 转向 "跨模型解离：三模型均检测到信号，仅 Llama 有因果效应"（D020）。所有论文文本已更新为此叙事。
- **页数极其紧张**——正文恰好 8 页，靠多处负 vspace（-14pt 到 -20pt）维持。任何文本增加都可能再次溢出，审查新 worker 时务必检查页数。
- 论文最脆弱的审稿人攻击面：(1) Qwen probe accuracy 仅 71-73%，解离论证弱于 Gemma；(2) TOST 等价检验 power 不足（<0.6），"consistent with" 措辞是妥协但合理；(3) 单语言对（EN-ZH）限制泛化性。
- 易错点：不要把 Table 1 的全量数据 probe accuracy（77.6%）和 Appendix F matched-condition probe accuracy（90.0%）搞混——前者是主实验结果，后者是 steering validation 用的高纯度子集。
