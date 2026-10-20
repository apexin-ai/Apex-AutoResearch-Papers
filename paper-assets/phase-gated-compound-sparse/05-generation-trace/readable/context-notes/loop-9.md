# director / loop_9.md

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_9.md`
- **Structured JSON:** [`dcaa960def5d6672e1b5.json`](../../sessions/dc/dcaa960def5d6672e1b5.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_messages
updated: '2026-05-16T02:39:02+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 westd-22162 的 cuda:0~3（RTX 6000 Pro ×4），不能碰其他项目的卡
- 目标已从 EMNLP 2026 main conference 转为 **Findings track**（D091），但**用户尚未确认**——已发消息询问，等回复后才能最终定调
- 论文已进入审稿阶段（C群 review_chat_id: oc_57b24a804b56707ec9118a483a8ac65e），不要干预 Review Director 的工作
- paper_framing.md 中的数值必须与 registry 严格一致——上轮 Agent 的"修正"反而引入了错误（DS median_diff 1.15→1.13 是错的），教训：改数前必须 registry 校对

### 2. 🖥️ 基础设施快照
- 服务器：westd-22162 (connect.westd.seetacloud.com)，用户 root
- 工作目录：/root/autodl-tmp/pacs
- Python/conda：aml-train 镜像，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型路径：DeepSeek-R1-Distill-Qwen-7B / Qwen2.5-7B-Instruct / DeepSeek-R1-Distill-Llama-8B（均在 autodl-tmp 下，具体路径让 Agent SSH 探查）
- W&B：未配置
- 活跃进程：c8_llama_n250 RUNNING（LLaMA n=250 扩展实验，4 GPU parallel）

### 3. 📊 当前状态
**刚做完**：R10 审稿报告 Action Matrix 全流程——Holistic Pass（3 个 SYSTEMIC_ISSUE）→ Per-Comment Matrix（11 issues）→ Reviewer 独立验证 → 定稿 → dispatch

**正在执行的三条线**：
1. **Agent**：c8_llama_n250 RUNNING；c5_per_phase_gini + c4_think_validation_math500 PREPARING
2. **Paper Agent**：正在处理 MUSTAFAR 假引用修复 + 全量 bib 审计（P0），15 项 P2 写作修正已排队
3. **review_issues.yaml**：已创建，11 条 issue 全标 in_progress

**等待中**：
- Agent 完成 LLaMA n=250（~6h GPU）→ 更新 C3 cross-architecture claim
- Agent 完成 &lt;think> validation + Gini decomposition → 更新 C4/C5
- Paper Agent 完成 P0 bib 审计 → 确认无其他假引用
- 用户确认 Findings track
- 全部完成后 → Round 11 审稿提交

### 4. 📋 待办（条件触发式）
- c8_llama_n250 完成 → 检查 n=250 是否 confirm cross-architecture claim（partially_confirmed → confirmed?）→ 通知 Paper Agent 升级 §7 措辞（从 "pilot evidence suggests" 回升）
- c4_think_validation_math500 完成 → 验证 &lt;think> token 位置与 phase boundary 是否一致 → 更新 paper_framing.md C4 status
- c5_per_phase_gini 完成 → 检查 per-phase Gini 是否支撑 discrimination collapse narrative → 更新 C5
- Paper Agent 报告 bib 审计结果 → 如有更多问题引用则 escalate
- 用户确认 Findings track → 更新 paper_framing.md 目标会议 + 通知 Paper Agent 调整 framing 语气
- 所有 P0+P1 完成 → submit_paper_to_review Round 11（recommended_review_mode="continue"，因为是迭代修复）
- Paper Agent 报告 Reviewer critical 无法自主解决 → 做方向决策介入

### 5. 🎯 战略上下文
- **核心结论**：importance-based eviction 的 compound interaction severity 随 sparsity 单调递增，DS 呈双 regime（s≤0.20 截断驱动 / s025+ 双重崩溃），QW 为纯推理质量退化（截断≤4%）
- **R10 审稿 2.25/5 Weak Reject**：核心打击是 novelty（empirical without new method），不是数据/方法问题——9 天内无法补方法创新，Findings 是唯一现实路径
- **最易判断错的事**：LLaMA n=250 结果可能仍然 partially_confirmed（n=49 时 Wilcoxon 已 significant 但 effect size 小）——不要因为 n 增大就自动升级 claim，看 effect size
- **易踩的坑**：(1) paper_framing.md 数值改动必须 registry 校对，不能信 Agent 的"修正"；(2) Paper Agent 已有两条指令排队（旧 urgent patch + 新 comprehensive batch），可能有部分重叠，Paper Agent 应自行去重；(3) review_issues.yaml 是新创建的，之前的 R1-R9 issues 未追溯录入（审稿从 R10 开始正式记录）
- **截稿 2026-05-25（9 天）**：时间紧但 AI 团队速度足够——LLaMA n=250 是唯一 critical path GPU 任务（~6h），其余全是写作/分析


---
