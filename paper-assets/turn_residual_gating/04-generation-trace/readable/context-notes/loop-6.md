# director / loop_6.md

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_6.md`
- **Structured JSON:** [`6ebfda731b05c057ff23.json`](../../sessions/6e/6ebfda731b05c057ff23.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_messages
updated: '2026-05-25T06:15:34+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-20861:cuda:0（项目配置 gpu_ids）
- ρ_max = 0.3（已修正，不是 v8b 时代的 0.5）。所有 SS 实验用 `--ss-max-ratio 0.3`
- EMNLP 2026 正文 8 页限制，abstract ≤ 200 words
- 用户已批准 framing 转变：GAR → diagnostic probe, ThreadGate → testbed。不要回退到旧 framing
- loss formulation 迭代表（v1-v7）保留作为设计演化标签，但其他位置的内部版本号（v7/v8b/v9）已清理，不要重新引入

### 2. 🖥️ 基础设施快照
- 服务器：westd-20861，工作目录待确认（Agent 之前用过）
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/`
- 论文源码：`paper/` 目录，`paper/sections/` 下各 .tex 文件
- 图表脚本：`figures/paper/gen_fig*.py`，配色 palette `figures/paper/palette.py`
- GOOGLE_API_KEY 已存储（key_id=google_api_key），本轮刚审批给 Agent 用 PaperBanana
- 活跃：Agent 正在执行 PaperBanana method framework 图 + Phase 1 multi-seed 实验队列

### 3. 📊 当前状态
**刚做完：**
- Round 4 审稿报告处理完毕（Overall 3.0 Findings）
- 文本修复已提交：ρ_max 数值修正、内部版本号清理、intro hedging、conclusion 补 Llama 数字
- Action Matrix 定稿并派发（用户已批准 GPU ~60-81h + framing 方向）

**已派发给 Agent（刚发）：**
- Phase 1A: Multi-seed 8 runs（PCGrad ×2, UG ×2, LoRA-only ×2, TG ×1, SS ×1）
- Phase 1B: Llama PCGrad + UG 各 1 seed
- Phase 2: TF→AR switching experiment（inference-only）
- PaperBanana method framework 概念图（进行中）

**已派发给 Paper Agent（刚发）：**
- Framing 重写：GAR→diagnostic probe, ThreadGate→testbed, 标题改短, 去冗余, bib 修复, Limitations 扩展

**等待中：** Agent 和 Paper Agent 的回复

### 4. 📋 待办
- Agent 汇报 Phase 1A 第一个 run 启动 → 确认训练配置正确，后续 runs 自动排队
- PaperBanana 图生成完成 → Read PNG 视觉检查，不满意要求重迭代
- Paper Agent 提交 writing_plan.yaml → 审批（检查 framing 方向是否正确落地）
- 每个 multi-seed run 完成 → 确认 AR eval N≥50 跑了，记录 mean±std
- Phase 1 全部完成 → 汇总 5 条件 × 3 seeds 结果表，更新 Table 1 数字
- Phase 2 switching experiment 完成 → 评估是否支持 exposure bias 归因（关键：switch 点 GAR drop vs pure AR 同轮对比）
- 全部实验 + 写作完成 → submit_paper_to_review（fresh round）
- review_issues.yaml 需要在修复确认后更新状态（open → in_progress → resolved）

### 5. 🎯 战略上下文
- **核心发现**：auxiliary attention losses 在 TF 下收敛（GAR=0.50）但 AR 下坍塌 8-27×，原因是 exposure bias。SS 是唯一有效 fix。
- **评分瓶颈**：Novelty 2/5 是结构性天花板。Reviewer 评估全部修复后 ceiling 是 3.5（Borderline Conference）。推到 4.0 取决于 rebuttal 让审稿人相信这个发现改变领域方法设计范式。
- **最易判断错的事**：
  1. MT-Bench 不适合做下游验证（2-turn benchmark vs 5-7+ turn finding）。已有 instruction retention（r=0.200, p=0.007）作为下游证据。不要再提 MT-Bench
  2. Base 模型不需要重新训练多 seed（冻结模型无训练方差），只需 bootstrap CI
  3. SS+LoRA-only 消融是 nice-to-have（Phase 3），不是 blocking。如果 GPU 紧张可跳过，Limitations 讨论即可
  4. 写作 hedging 对 evidence 问题无效——C1/C2/C3 连续 4 轮被 flag，之前的写作修复都失败了，必须补实验
  5. switching experiment 需要 pure AR baseline 作为 control（已有数据），注意 switch point 的分布不连续 artifact


---
