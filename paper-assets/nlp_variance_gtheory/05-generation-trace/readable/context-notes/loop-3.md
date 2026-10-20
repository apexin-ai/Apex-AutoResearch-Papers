# director / loop_3.md

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_3.md`
- **Structured JSON:** [`74b0ecc535c05ac909b5.json`](../../sessions/74/74b0ecc535c05ac909b5.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_messages
updated: '2026-05-25T06:01:32+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用项目配置 `execution.gpu_ids` 白名单内的卡（westd-32570 和 westd-19912 各 4× RTX PRO 6000 96GB）
- 匿名 repo 已公开（HTTPS），任何 commit 都会立即可见——推送前必须确认无去匿名化信息（作者名/机构/服务器路径）
- EMNLP 2026 ARR DDL 是 2026-05-25（今天），main text 严格 ≤ 8 页，abstract ≤ 200 words
- 论文只能有一个 Limitations section 在正文里，appendix 不能有 limitations section
- ARR Responsible NLP Checklist 在 OpenReview submission form 里手动填写，不在论文 PDF 里

### 2. 🖥️ 基础设施快照
- 服务器：westd-32570 (connect.westd.seetacloud.com) + westd-19912，各 4× RTX PRO 6000 96GB
- 代码路径：`/root/nlp_variance_gtheory`
- 本地论文：`/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/`
- 匿名 repo：`https://github.com/anonymous-nlp-2026-2/nlp_variance_gtheory`
- 全部 GPU 空闲，无 RUNNING 实验，无活跃进程
- GOOGLE_API_KEY 已存储（key_id: google_api_key），用于 PaperBanana

### 3. 📊 当前状态
**正在进行**：Agent 正在处理最新排版任务——pages 3-6 没有 figure（只有 tables），需要新增 3 张 matplotlib figure（factorial design 示意图 / variance component 柱状图 / budget sensitivity 图移回正文）。这是用户（曹晓玉）的反馈。Agent 尚未回复。

**已完成本轮**：
- 主图从 Appendix 移回 main text 为 Figure 1，空白裁剪
- Related Work 5→3 subsection，精简 40%
- Table 2 加宽（+95% CI 列）
- 正文从 3 张图增至 5 张（+heatmap +stacked bar），但分布仍不均——pages 3-6 全是 tables
- 缩写定义自检完成（12 处修复：D-study/IRT/ANOVA/MC/FF/GLMM/REML/CV/BF16/FP16/FP32/LOMO + MMLU/ARC/GSM8K 全称）
- Positioning table、LOMO table、model overview table 加入正文

**Registry**: 36 实验（22 pending / 14 done / 12 success），全部空闲

### 4. 📋 待办
- Agent 回复排版修改结果 → 编译验证每页 figure 分布 → 如果 pages 3-6 仍无 figure 则追加指令
- 用户确认最终 PDF 满意 → 提醒用户在 OpenReview 提交 ARR（DDL 今天 5/25）
- 如果 PaperBanana 再次幻觉 → 改用 matplotlib 手动画所有新 figure
- 审稿阶段仍活跃（review_chat_id: oc_265de443abfe4594f91451b075b582ca）——提交后等 Review Director 反馈

### 5. 🎯 战略上下文
- 论文核心：G-theory 多 facet 方差分解应用于 LLM benchmark 评测，C1=D-study reproducibility budgets (3×3→178 items, 3.1× reduction)，C2=format-associated variance patterns (MC vs FF)
- Score trajectory: R5(3.5)→R6(3.0)→R7(3.5)→R8(3.5)→R9(3.5)→R10(3.5 fresh)，稳定在 3.5 borderline
- 12 个成功实验 / ~2.36M records / 8 models + 72B + Llama-70B out-of-sample validation
- Rebuttal 预案已准备（docs/rebuttal_prep.md），覆盖 4 个预期攻击点
- **易错点**：排版修改容易超 8 页——每次加 figure 必须编译验证页数。PaperBanana 内容忠实度不稳定，优先用 matplotlib
- 两位用户（周俊伟、曹晓玉）都在给排版意见，优先级最高是让 figure 均匀分布到每页


---
