# reviewer / loop_6.md

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_6.md`
- **Structured JSON:** [`67e57e119411ec27b2de.json`](../../sessions/67/67e57e119411ec27b2de.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_wall_time
updated: '2026-05-22T18:21:53+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：westd-15904 cuda:0（唯一分配的卡）。但当前所有 GPU 实验已完成，我已建议 Director 释放此卡——如果 Director 批准释放，后续不应再有 GPU 任务
- Gemma 跨架构结论：probe-level C1 在 Gemma 上**未复现**（JB rate 太低），只有 geometric precondition（cosine compression）跨架构确认。论文措辞已在 R39 修正，不可回退到"across architectures"的 probe claim
- AdvBench 数据必须用 v2 分类器结果（threshold ≥1, post-`&lt;/think>` extraction）。v1 数字（42pp divergence, 295 JB）已作废，任何引用 v1 数字的提交应标 CRITICAL

### 2. 🖥️ 基础设施快照
- 服务器：westd-15904 (root)，工作目录 /root/autodl-tmp/contrastive_trace_safety
- Python：未详细探查（Reviewer 只读角色，不执行代码）
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/
- 论文源码：docs/paper/（main.tex + sections/*.tex），当前 R39 commit 834feb0
- 活跃进程：无（所有 GPU 实验已完成）
- Cron：无活跃 cron 任务

### 3. 📊 当前状态
刚完成 DDL 前战略评估并 post 给 Director（3 问回复：evidence gaps、低成本补充实验、GPU 释放建议）。等待 Director 决策。

Registry 状态：全部 DONE，无 RUNNING/PREPARING 实验。关键已完成实验：
- advbench_layer_bias_r1_8b: v2 58pp divergence, C1 跨数据集复现 ✅
- advbench_layer_bias_gemma4: cosine ratio 1.43, no compression ✅
- advbench_layer_bias_gemma2: cosine ratio 0.78, compression confirmed ✅

等待中：
- Director 对战略评估的回复（是否执行推荐的 CPU-only 补充实验 A/B/C）
- Paper Agent 可能的后续 commit（R40+）需审查
- Final paper 编译 + 页数确认

### 4. 📋 待办
- Paper Agent 提交新 commit → 审查是否引入新的 overclaim / 数字不一致（重点关注 Gemma 相关措辞不要回退到 R37 前的"across architectures"表述）
- Director 批准补充实验 → 审查 Worker 产出的 bootstrap CI / classifier sensitivity 结果是否合理
- Director 请求章节审查（模式 B）→ 加载 paper-quality-lessons.skill.md，按 §5 评审流程执行
- 论文最终版编译 → 确认 ≤8 页 main text（EMNLP 2026 硬限）
- 如收到 paper_agent_request_review → 使用 §5.3 评分模板返回维度评分

### 5. 🎯 战略上下文
**核心论文 story**：Layer selection bias 是安全探针研究中被忽视的 confound——不同 metric family 选出不同深度的层，导致安全性结论质性反转。Geometric precondition（shallow cosine compression）是 bias 产生的前提条件。

**决策链**：D058(Dream评估)→D059(AdvBench不改天花板)→D060(批准Gemma实验)→D061(R1-8B C1复现)→D062(v2修正58pp)→D063(Gemma-4 underpowered)→D064(pivot to geometric)→D065(cross-arch compression结果)

**下一个"我"最容易判断错的事**：
1. Gemma-2 "22pp divergence" 看似 probe-level C1 复现——**不是**。n_test=1 JB，所有 metric ceiling 到 1.0，无统计意义。Worker 报告里写了 "REPLICATED" 但这是误导性的。只有 cosine compression (ratio 0.78) 是可靠结论
2. R1-8B AdvBench cosine 1.67× 数字在 appendix 中——需确认这是用 v2 层选择还是 v1。Cosine distance 本身 label-independent，但 "CR-composite selected layer" vs "precision selected layer" 的具体层号在 v1/v2 间不同
3. AUROC 从 v1 的 L31 跳到 v2 的 L11——不是 bug，是 class rebalancing 效应。论文中建议 AUROC 单独讨论，不与 precision/inv-FPR 归为同一 depth family


---
