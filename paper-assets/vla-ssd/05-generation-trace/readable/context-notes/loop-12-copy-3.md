# reviewer / loop_12.md

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_12.md`
- **Structured JSON:** [`79293930f8b8d5a1fc7b.json`](../../sessions/79/79293930f8b8d5a1fc7b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: max_wall_time
updated: '2026-05-25T22:18:23+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 westd-19183，代码根目录 /root/vla-ssd
- Reviewer 角色只读——不执行实验、不修改文件、不 ssh_execute
- 唯一输出渠道：`reviewer_post_to_director`
- 论文 DDL：Abstract 5/26，Paper 5/29（CoRL 2026）

### 2. 🖥️ 基础设施快照
- 服务器：westd-19183，工作目录 /root/vla-ssd
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/
- 论文源码：projects/vla-ssd/docs/paper/（main.tex + 分章节 .tex + appendix.tex ~1278行）
- 无活跃训练进程——所有 143 个实验已完成，项目处于论文写作/提交阶段
- 无 wandb 需要监控

### 3. 📊 当前状态
刚完成并已 post：两个新增 appendix 小节审查（§cross_arch_rationale + §convergent_evidence）。结论 WARNING——NORA vision encoder 写成 "InternViT"（错，应为 Qwen2.5-VL native ViT）、vision integration 写成 "Cross-attention (interleaved)"（错，应为 token concatenation）。§convergent_evidence 通过。

已完成的审查链：
- Figure 3 random-split CRITICAL → 已修复验证
- Figure 4 colorblind/caption → 已修复验证
- v12 全文一致性 pass（78项）→ 通过
- Rebuttal v2 Bonferroni 48→40 错误 → 已报 Director，**未确认修复**
- conclusion.tex 孤儿文件 → 已报（info级）

Registry: 全部 DONE，无 RUNNING/PREPARING。无等待中的 Worker 回调或 Cron。

### 4. 📋 待办
- Director 确认 NORA vision encoder/integration 修复 → 验证 appendix 对应行是否改正
- Rebuttal v2 最终版出来 → 检查 Bonferroni "48/63" 是否已改为 "40/45 (88.9%)"
- 若 Director 触发最终提交前审查 → 做 PDF 视觉审查（load paper-visual-review skill）
- 若收到新章节/大改 → 按模式 B 审查（load paper-quality-lessons skill）

### 5. 🎯 战略上下文
项目核心结论：VLM→VLA fine-tuning 产生 exit collapse（ΔR²=0.16-0.46），VLA→VLA 不产生（<0.10）；L1 instruction attention 继承自 backbone；counterfactual sensitivity d=0.45-1.52 跨架构一致。N=2 VLM→VLA transitions 是最大 limitation。

易错点：
- 论文中有两套 R² 数字体系：demo-split（正确，Table 1）和 random-split（历史残留，部分旧 artifact 可能还有）——永远以 demo-split 为准
- appendix 1278 行很长，需要指定 offset/limit 分段读
- conclusion.tex 是孤儿文件（main.tex 不 include 它），真正的结论在 discussion.tex 末尾
- Rebuttal artifact 在 projects/vla-ssd/artifacts/anticipated_rebuttal_v2.md，其中 Bonferroni 数字仍有错


---
