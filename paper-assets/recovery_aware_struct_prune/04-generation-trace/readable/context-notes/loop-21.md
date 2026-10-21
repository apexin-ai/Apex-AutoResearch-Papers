# director / loop_21.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_21.md`
- **Structured JSON:** [`ca7a6e2fcdfa31c8807e.json`](../../sessions/ca/ca7a6e2fcdfa31c8807e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 21
reason: max_messages
updated: '2026-05-25T08:28:08+00:00'
---

### 1. 🔴 硬约束 / 红线
- EMNLP 2026 ARR DDL 是 2026-05-25（今天），论文已基本定稿，所有修改都是最终润色
- Git push 到 `anonymous-nlp-2026/recovery_aware_struct_prune` 仍然不通——deploy key 只有 `caoxiaoyuyuyuyuyu/agent-ml-research` 的权限。本地 commit 在 `/tmp/recovery_aware_struct_prune_push/`，需要用户解决 access
- 论文正文严格 8 页限制（附录/参考文献不限），`paper_compile_and_check` 报 16 页是含附录的总页数，不是真超页
- Abstract 不超 200 words（当前 153 words，已达标）
- RASP 永远带 α 值标注（bare "RASP" 已全部消除，用"RASP at α=X.0"或"parameterized family"）

### 2. 🖥️ 基础设施快照
- 本项目无活跃远程服务器——所有实验已完成，当前阶段是论文写作/审稿
- 论文源码：`/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/`
- 编译后 PDF：`docs/paper/main.pdf`（已通过 `feishu_upload_file` 发给用户）
- 项目知识文件：`projects/recovery_aware_struct_prune/` 下的 `ROADMAP.md`, `paper_framing.md`, `experiment_plan.yaml`, `report.md`, `decisions.yaml`, `constraints.yaml`, `mistakes.yaml`
- 审稿追踪：`artifacts/review_issues.yaml`（Round 1-8 全部 issue）
- 审稿阶段已激活：`review_chat_id = oc_40839c097b00df44480b45ab767f59cf`
- 无活跃进程 / tmux / cron

### 3. 📊 当前状态
刚完成最终一轮修改并交付 PDF：
- 帖桂尧提的 8 项一致性修复 + 6 项写作质量修复全部完成
- Abstract 重写（153 words，去掉 MLP channel groups 等术语）
- ShortGPT 跨任务分析、MATH-500 双因素分析（截断 73.6% + 难度）已加入正文
- 表 1/2 字体放大、脚注删除
- 参考文献验证完成（Self-Healing→OpenReview preprint, Bonsai→arXiv, RAC→Workshop）
- Discussion 扩展为两段（GRPO as diagnostic probe + Implications）
- PDF 已编译并上传给用户

Registry 无 RUNNING/PREPARING 实验。无等待中的 Worker 回调或 Cron。

### 4. 📋 待办
- 用户反馈 PDF 有问题 → 按具体反馈修改，重新编译上传
- 用户解决 git push 权限 → 立即推送所有本地 commit
- 用户说"提交审稿" / "进入审稿阶段" → 调 `submit_paper_to_review`
- 周俊伟之前提的图表美化任务（统一配色、统计图美观度）→ 状态不明，Agent idle 10h 可能丢失，需要检查是否完成或重新派发

### 5. 🎯 战略上下文
- 核心发现：reward-accuracy decoupling（GRPO vs SFT 在 20-25% MLP sparsity 下准确率几乎一致，mean |Δ|=0.54pp）+ recovery capacity spectrum（CKA diversity 决定 RL 训练动态）
- 论文定位：controlled study / empirical analysis，不是 method paper。RASP 是 parameterized family 用于控制变量，不是 proposed method
- Round 8 审稿评分 3.0 (Findings level)，升 3.5 需要额外 GPU 实验（multi-seed RASP、1000-step GRPO、non-Qwen arch），DDL 前不可能完成
- CKA invariance 已修正为"orthogonal transformations and isotropic scaling"（不是 arbitrary invertible linear）
- 所有 definitive claims 已加 hedging（"appears to", "may serve as"），scoped to "20-25% fine-grained MLP sparsity on Qwen2.5-family models"
- 易踩坑：paper_compile_and_check 的页数检查会报 FAIL（因为算总页数含附录），这不是真问题


---
