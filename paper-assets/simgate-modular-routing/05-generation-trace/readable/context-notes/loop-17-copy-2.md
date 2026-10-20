# reviewer / loop_17.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_17.md`
- **Structured JSON:** [`1c3eb4130626381edf0d.json`](../../sessions/1c/1c3eb4130626381edf0d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 17
reason: max_wall_time
updated: '2026-05-21T01:23:59+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westb-13313 的 cuda:0 和 cuda:1（2× RTX 5090）。D129 已决策释放，当前无需 GPU 实验。若后续需要重新使用必须确认 D129 是否被撤回。
- westd-18266（4× RTX PRO 6000）SSH key 未配通，实际从未使用过，不要尝试在上面跑任何东西。
- CI 方法已统一为 **non-clustered episode-level bootstrap (B=10,000, seed=42)**，全文零残留 cluster bootstrap CI。任何新增数值必须用同一方法，不能混用 cluster bootstrap。
- EMNLP 2026 主文 ≤8 页硬限（当前 17 页含 appendix + checklist，主文已在限制内）。

### 2. 🖥️ 基础设施快照
- 服务器：westb-13313 (root)，工作目录 `/root/autodl-tmp/simgate-modular-routing`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/`
- 论文源码：`docs/paper/`（main.tex, experiments.tex, introduction.tex, discussion.tex, abstract.tex, references.bib, responsibleNLPchecklist.tex）
- 远程分析脚本：`scripts/daf_sensitivity_3model.py`（三模型 sensitivity 计算）
- 远程实验结果：`results/gemma_scienceworld_counterfactual/analysis.json`（Gemma 最终数据）
- 活跃进程：无（D129 释放 GPU 后无运行中实验）
- W&B：本项目未配置，不检查

### 3. 📊 当前状态
刚完成 CI 一致性全文审计并 post 给 Director。确认所有 Gemma CI 已从 [68.8, 100.0]（cluster）统一为 [79.5, 98.4]（episode-level）。ROADMAP 审查通过，数据与独立核实一致。

Registry: 121 实验全部完成（无 RUNNING/PREPARING）。无等待中的 Worker 回调或 Cron。

内部审稿已提交（apr_20260521T004926_35g5），等用户选择审稿模式。

### 4. 📋 待办
- 内部审稿结果返回 → 按审查模式 B 逐维度审查（claim 可信度 / 叙事逻辑 / 攻击面），出评分模板
- Worker 修改论文后提交差异 → 验证所有 CI 数值一致性（grep `68.8` 确认零残留）
- 用户确认 ARR 提交 → 提交前最终审查（格式、引用完整性、数据一致性、Responsible NLP Checklist）
- 若收到 Framing 调整提案 → Read `negative-framing-review` skill，四维度审查

### 5. 🎯 战略上下文
- 核心结论：**death avoidance 解释 ~90% routing signal**，三模型跨架构一致（DAF 88-90%，spread 2.2pp），sensitivity 排除零死亡 task 后 ≥97%
- 决策链：D126/D127 framework-centric pivot → D128 扩展 task validation → D129 释放 GPU
- **易错点 1**：Gemma 的 N=220 而非 245（Qwen 是 245），因为 Gemma 标准化为 11 canonical tasks × 20 eps。不要把 N 搞混。
- **易错点 2**：rebuttal_drafts.md 中 Response #1 的 Gemma CI 已更新为 [79.5%, 98.4%]，但若有人再改 rebuttal 可能回退——任何 rebuttal 修改后 grep 确认。
- **易错点 3**：main.tex L584 caption 仍说 "Gemma-2's wider CI"——episode-level 下 CI 仍然最宽（18.9pp > Qwen 17.9pp > Llama 14.9pp），叙述成立但差距已不显著，审稿人可能质疑。
- **最大审稿风险**：环境单一性（ScienceWorld only for death mechanism）。已在 Limitations + rebuttal 预案 #3 覆盖，但这是最可能被压分的点。


---
