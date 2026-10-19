# director / loop_12.md

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_12.md`
- **Structured JSON:** [`1a819de9b0657254da3a.json`](../../sessions/1a/1a819de9b0657254da3a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: max_messages
updated: '2026-05-25T05:40:20+00:00'
---

### 1. 🔴 硬约束 / 红线
- EMNLP 2026 ARR DDL 2026-05-25（今天），正文严格 8 页，Abstract ≤200 词
- Figure 1 必须用 PaperBanana 生成，不允许用 matplotlib（周俊伟明确要求）
- 论文中不能出现破折号（曹晓玉明确要求，已全部去除）
- PaperBanana 输出是 JPEG-as-PNG，必须用 PIL 转换为真 PNG/PDF 再放入论文

### 2. 🖥️ 基础设施快照
- 本地工作目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/`
- 论文源码：`paper/` 子目录（main.tex + 各章节 .tex）
- 图表：`figures/paper/`（fig1_overview, fig2_sparsity_sweep, k_curve_ppl, mask_divergence_heatmap, per_layer_retention_chart）
- PaperBanana：`/home/ubuntu/.venv/bin/paperbanana`，GOOGLE_API_KEY: [REDACTED]
- 编译：`cd paper && latexmk -pdf main.tex`
- 无 GPU 实验在跑，当前阶段纯论文写作

### 3. 📊 当前状态
本轮完成了三项写作任务：
1. **Abstract + Introduction 重写**：从实验报告风格改为叙事弧线，按蒸馏写作范式 4 段结构（hook→gap→insight→contributions）
2. **Figure 1 用 PaperBanana 重新生成**：v13 intent，Gemini 2.5 Pro 一轮通过，高信息密度（左=Layer 内部流程，右=Training Pipeline + KL）
3. **缩写定义自检**：修复 13 处未展开的缩写（LLM, KL, TEAL, PPL, MLP, JSD, SNR, MSE, MMLU, GSM8K, PIQA, SVD, MoE, NPU, OOD）
4. **破折号去除**：正文 10 处 em dash 全部改为逗号/冒号

编译验证：0 overfull box，正文 8 页，Conclusion 在第 8 页右栏结束。
Registry 无 RUNNING/PREPARING 实验。无等待中的 Worker 回调。

### 4. 📋 待办
- 用户发新写作修改指令 → 按要求修改，编译验证 8 页限制
- 用户要求重新审稿 → `submit_paper_to_review` 提交
- 用户要求其他章节写作优化 → 加载 distilled-writing.skill.md + paper-writing-norms.skill.md 指导修改
- 审稿报告回来 → 按 review-report-action skill 处理

### 5. 🎯 战略上下文
- 核心贡献：output-distribution KL > BCE/MSE for contextual sparsity prediction，关键发现是 KL 发现的 mask pattern（而非 coupling 机制本身）驱动质量提升
- 论文已进入审稿阶段（review_chat_id 已配置），Group C 团队并行处理
- 正文 5 张图（fig1 overview, fig2 sparsity sweep, fig3 k-curve, fig4 heatmap, fig5 retention），从原来 3 张增加到 5 张
- 易踩坑：页数极其紧张（8 页刚好），任何文字增加都需要同步检查是否溢出；PaperBanana 输出需要 PIL 转格式


---
