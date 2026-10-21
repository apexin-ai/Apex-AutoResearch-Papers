# director / loop_10.md

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_10.md`
- **Structured JSON:** [`aa7338032a6e079e7020.json`](../../sessions/aa/aa7338032a6e079e7020.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_messages
updated: '2026-05-19T09:15:25+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单: cqa1 cuda:1, cuda:3; westd cuda:1。cuda:0 和 cuda:2 已归还 Manager（用户冯元宁明确要求），绝不可再使用
- 论文正文禁止 em-dash（用户自定义硬约束，Reviewer 会标记）
- K* 定义已改为 CI lower bound > θ（不是 point estimate），Eq.1 已修正，全文必须一致
- θ=0.60 是固定决策阈值，不可随意调整

### 2. 🖥️ 基础设施快照
- **cqa1**: 远程训练服务器，2×4090D
  - cuda:1 → exp_code_qwen7b（~May 19 18:00 UTC）
  - cuda:3 → exp_code_mistral7b（~May 19 11:00 UTC）
- **westd**: cuda:1 → exp_32b_c4（~May 20-21）
- 论文本地路径: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/`
- Artifacts: `projects/gen-depth-contamination/artifacts/`
- 远程实验代码/数据: 在各服务器的 `execution.project_path`（用 `load_project_config` 查）

### 3. 📊 当前状态
刚完成: ROADMAP Pythia AUC 修正（0.5765→0.5983）、D080 LLaMA Code K*=2 入稿、cuda:0/cuda:2 归还 Manager。

RUNNING 实验:
- **exp_code_mistral7b** (cqa1 cuda:3, ~11:00 UTC) — Code domain Mistral-7B K* 测量，Code 验证 4/5
- **exp_code_qwen7b** (cqa1 cuda:1, ~18:00 UTC) — Code domain Qwen-7B K* 测量，Code 验证 5/5
- **exp_32b_c4** (westd cuda:1, ~May 20-21) — 32B 模型 C4 domain bonus 实验

等待中:
- **dream_20260519T090934** (full review mode) — 应该很快完成，收到 `[DREAM ...]` 回调后按 `dream-report-action` skill 处理
- 两个 Code 实验的 cron 完成回调

### 4. 📋 待办
- dream_20260519T090934 完成 → Read `dream-report-action.skill.md` → 按三档对比分析 → 构建行动列表
- exp_code_mistral7b 完成 → 分析 K*（预期 K*=2）→ 入稿 Paper Agent patch → 更新 ROADMAP/framing
- exp_code_qwen7b 完成 → 分析 K* → 入稿 → Code 5/5 全部完成 → 最终 framing 定稿
- Code 5/5 完成 → 更新 Abstract/Limitations 中的模型数量（"two models" → "five models"）→ Round 11 内审
- exp_32b_c4 完成 → bonus patch（不阻塞主线）
- Round 11 内审通过 → `submit_paper_to_review` 提交审稿团队
- DDL: May 25 final submission

### 5. 🎯 战略上下文
- **核心结论**: K* 是 domain-governed（domain ceiling + model competence）。Domain hierarchy: Wiki=1, C4=Code=2, arXiv=3。Retrain-chain K*=7 vs prompt-chain K*=2。
- **当前目标**: 冲 4.0 分（Conference Accept），从 Round 10 的 3.5 提升。关键增量是 Code 4th domain（从 3 域→4 域堵审稿人最大缺口）+ 跨家族验证。
- **决策链**: D076 采纳 Plan C framing → D077/D078 retrain K*=7 双家族 → D079 cross-scorer K*=2 → D080 LLaMA Code K*=2 cross-family
- **易错点**:
  - Pythia Code K*=1 不是 negative result，是 competence-limited（模型能力不足未达 domain ceiling），framing 已覆盖
  - Mistral-7B 在 C4 domain 是唯一 K*=1 的（8/9 configurations 中的例外），如果 Code 也是 K*=1 需要特殊处理（但不影响 domain ceiling 论点）
  - R8-W4（cross-model transfer coverage）仍 open，Code cross-model table 可能可以替代，需确认
  - 论文已 ≤ 8 页，新增内容需注意不超页


---
