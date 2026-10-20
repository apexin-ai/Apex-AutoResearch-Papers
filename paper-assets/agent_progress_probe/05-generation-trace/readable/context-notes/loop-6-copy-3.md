# reviewer / loop_6.md

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_6.md`
- **Structured JSON:** [`1b2a989a57779ae82cc7.json`](../../sessions/1b/1b2a989a57779ae82cc7.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_wall_time
updated: '2026-05-15T13:44:42+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：cuda:0, cuda:1（bjb2-23165 上仅 2 张 5090）。之前有过越界事故（2026-04-24），任何训练进程必须核对 CUDA_VISIBLE_DEVICES
- Gold set 评估脚本 evaluate_gold_set.py 必须排除 gold 窗口出训练集（L339-341 已实现），审查时必须验证这一点
- 论文 headline gap 已定为 16.8pp（D069 最终决策，撤销了 D068 的 19.6pp），不要用 19.6pp
- Gold set 使用 Set B (N=505, ≥2 annotators agreed) 作为主评估（D071），不要用 N=601（含单标注者噪声）或 N=195（旧 batch1）

### 2. 🖥️ 基础设施快照
- 服务器：bjb2-23165，工作目录 /root/autodl-tmp/agent_progress_probe
- Python：conda 环境（/root/miniconda3/bin/python），不用 venv
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/
- Gold set 文件（远程）：/root/autodl-tmp/agent_progress_probe/artifacts/gold_set/（eval_setA/B/C + bootstrap_setA/B/C.json + gold_*.csv）
- Gold set 文件（本地）：artifacts/gold_set/（iaa_3annotator_report.json, gold_consensus_601.csv, gold_merged.csv, annotation batch 1/2/3a/3b）
- 活跃进程：无（两张 GPU 均空闲）
- W&B：未确认是否配置，不检查 W&B

### 3. 📊 当前状态
**刚完成**：
1. 审查了 gold-consensus-eval (N=601) — 发现 κ=0.564、61.6% 单标注者标签问题，已报 Director
2. 审查了 gold-3annotator-eval (Set A/B/C) — Fleiss κ=0.39，Set B GB=0.839 p<0.001，已确认数据一致性
3. 审查了 Round 4 审稿处理方案（C1-C6, W1-W8）— 提交了 6 项独立意见给 Director

**Registry**：全部 DONE/终止，无 RUNNING/PREPARING 实验。总计 68 个（47 success, 10 negative, 1 fail）

**关键未闭环**：
- gold-consensus-eval、gold-3annotator-eval、fetch_gold-consensus-results 三个实验**未注册到 registry**，已向 Director 报告
- Round 4 回复方案中 11 个补实验尚未启动（等 Director 决策）

### 4. 📋 待办
- Worker 完成 C4 2-LF (λ₁+λ₂, 去 OB) 实验 → 核验：(a) 用的是 cmd_rep+file_diff 不是 file_diff+OB；(b) conf≥2 训练集大小报告了吗；(c) cross-agent F1 与 feature ablation 结果一致（预期 ≥0.95）
- Worker 完成 C1 LLM on OH 实验 → 核验：(a) 用的是 few-shot-CoT 配置（best config）；(b) 评估样本量和 parse failure rate；(c) 与 SWE in-domain 0.799 的对比
- Worker 完成 C2 同 scope GB 评估 → 核验 N=6122 test split 上 GB F1，确保与 Table 1 probe 行可比
- Worker 完成 C3-a conf 分层 gap → 核验 conf=1/2/3 上 silver-gold agreement 是否符合预期梯度
- 论文章节更新提交审查 → 按 §5.2 写作审查维度审（尤其 gold set section 和 headline 数字一致性）
- Director 决定 main vs Findings track → 我的建议是 Findings（已提交理由），但最终是 Director/用户决策

### 5. 🎯 战略上下文
**核心结论链**：D039 TLM 判死 → D050 Claim 1 reframe 为 "zero-shot transfer dominance" → D069 headline 16.8pp → D071 Gold Set B 为主评估。论文定位为 empirical analysis paper（D039 pivot），不是 method paper。

**下一个"你"最容易判断错的事**：
1. **2-LF ablation 有两种方向**：去 cmd_rep (λ₂+λ₃, Table 5 已有) vs 去 OB (λ₁+λ₂, C4 要求的)。审稿人问的是后者（deployability），不要和前者混淆
2. **Gold Table 的 N 不一致是陷阱**：GB 评估 N=491，TWV Probe 评估 N=322。TWV Probe 看似 best (0.854) 但 scope-matched 比较（bootstrap shared N=322）GB=0.877 > TWV=0.854。当前 Table 呈现暗示 TWV Probe > GB，实际可能相反
3. **κ=0.39 是双刃剑**：论文当前 framing 为 "inherent subjectivity justifies weak supervision"，但 main track 审稿人可能攻击 "gold standard 不够 gold"。Findings track 更安全
4. **不要把 N=601 和 Set B N=505 搞混**：N=601 是 2-annotator 旧合并（含单标注者），Set B 是 3-annotator ≥2 agree（更可靠）。论文已更新到 Set B，但远程服务器上两套结果都在


---
