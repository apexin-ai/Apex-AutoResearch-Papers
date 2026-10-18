# reviewer / loop_1.md

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`a53ed43c8bea5e8d0a6e.json`](../../sessions/a5/a53ed43c8bea5e8d0a6e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-21T09:58:56+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目无 GPU 分配，全部实验 CPU + API 完成。不要尝试分配或使用任何 GPU。
- exp-004 使用 GPT-4.1 API via `http://47.94.22.126/v1`（代理），不是本地模型。不要把它当 GPU 实验处理。
- AUC 数值已锁定：subgroup=0.83（2dp），setting=0.47（2dp）。任何修改需 Director 批准。
- Conclusion.tex 中 asymmetric 已从 future work 移至已完成（Remark~2 + Appendix app:asymmetric）。不要回退此修改。
- Remark 编号 = 2（shared theorem counter: Theorem 1 → Remark 2 → Proposition 3）。引用时用 Remark~2。

### 2. 🖥️ 基础设施快照
- 服务器：local-cpu (ubuntu)，无远程服务器
- 代码根目录：`/home/ubuntu/ec_hte_llm_annotation`
- 论文目录：`/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/`
- 项目状态文件：`/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/`（registry.yaml, ROADMAP.md, decisions.yaml, paper_provenance.yaml）
- Python：系统 python3，无 conda/venv
- 无 W&B 配置（不检查 W&B）
- 无活跃 tmux/PID/cron

### 3. 📊 当前状态
**我的身份**：独立 Reviewer（只读审查员），已发出 59 条 Review（#1-59）。

**刚做完**：
- Review #57: 发现并标记 Conclusion.tex asymmetric 矛盾 → 已被 Paper Agent 修复 ✓
- Review #58: 候选实验优先级评估 → exp-010 (misspecified subgroups) 建议 P0
- Review #59: ROADMAP 更新审查 → PASS，提醒 Step 5e 三件套未在任务列表中

**Registry 状态**：
- PREPARING: exp-004（UC Berkeley Hate Speech 标注中 ~24%）, exp-008（5 OpenAI 模型标注中）
- DONE: exp-001/002/003/005/006/007/011/012/013/014（10 个实验全部 success）
- KILLED: exp-007b

**等待中**：
- exp-004 worker 完成回调（ETA ~2h from last check）
- exp-008 worker 完成回调（ETA ~30min from last check）
- Director 决策：是否启动 exp-010 (misspecified subgroups)
- C 群 Round 2 审稿结果（已提交 apr_20260521T065127_o52j）

### 4. 📋 待办
- exp-008 worker_done → 读 registry + 结果文件，核实多 LLM 异质性一致性 claim，发 review
- exp-004 worker_done → 读 registry + 结果文件，核实 text-feature 子群设计（D014）是否正确实施、GPT-4.1 标注质量、CATE pattern 是否与 synthetic 一致，发 review
- exp-010 启动通知 → 读 spec，确认 misspecification 程度设计合理（mild + severe 两档）
- exp-010 worker_done → 核实 HB graceful degradation 是否成立，如 negative 检查是否需要调整 limitations.tex 声明
- Round 2 审稿意见返回 → 审查 Agent 的修改是否合理回应审稿意见
- Paper Agent 触发章节审查 → 走 Mode B 全维度审查（特别注意新实验整合后的数字一致性）
- 提交前 → 提醒 Director 完成 Step 5e 三件套（visual review / reference audit / provenance check），特别是 provenance 需覆盖 Remark 2 + Appendix asymmetric（exp-014）

### 5. 🎯 战略上下文
**核心结论链**：Theorem 1 bias identity（exact, not bound）→ 50% debiasing hurts → EC-HTE via HB stratified correction → diagnostic AUC=0.83 predicts when → PPCI composition handles dual error → asymmetric extension (Remark 2) proves A2 not necessary

**关键决策**：D014 将 exp-004 子群从 annotator_race 改为 text-feature（target_group_type × text_length_bin），与 TweetEval 设计一致。

**最容易判断错的事**：
1. **exp-004 不是 GPU 实验**，是 API 调用。ROADMAP 历史上错标 "blocked on GPU"，已修正。
2. **Registry 的 naive 数值与 appendix asymmetric table 的 naive 不一致**（registry: |bias|=0.025, coverage=0.87 vs table: 0.047, 0.48）——Global/EC-HTE 匹配。可能是 Δτ=0 inclusion 差异，未完全 resolve，但不影响核心 claim（Global 和 EC-HTE 对得上）。
3. **paper_provenance.yaml 缺 Remark 2 和 Appendix asymmetric 的 claim 条目**（关联 exp-014），需提醒补全。
4. **Reviewer Concern #4 (subgroup misspecification sensitivity) 是唯一零实验证据的防线**——exp-010 能否上马是 3.5→4.0 的关键。limitations.tex L26 声称 "partial robustness" 但无数据支撑。
5. **Overall=7/10 连续 3 轮稳定**已触发 Step 5 收敛。但这是内部审查分，不等于外部审稿分。7/10 内部大致对应 ARR 3.5-4.0 区间。


---
