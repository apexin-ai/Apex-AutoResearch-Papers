# agent / loop_8.md

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_8.md`
- **Structured JSON:** [`365ed0f164cdeb0a5785.json`](../../sessions/36/365ed0f164cdeb0a5785.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: idle_timeout
updated: '2026-05-15T04:36:17+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 westd-37397 的 GPU 分配需查 `get_project_status` 白名单，当前两张 RTX PRO 6000 96GB 均 idle
- Qwen concentration 值已锁定为 **0.61**（float32 验证），论文中所有引用必须统一，不得出现 0.59/0.60/0.66 等旧值
- Mistral concentration 锁定 **0.24**，t1/t5=0.41
- bfloat16 精度 bug：KV cache 差值计算必须先 `.float()` 转换，否则数值漂移（已修复，但新实验代码必须保持）
- EMNLP 2026 ARR May 25 截止——论文修改窗口极窄，任何改动需 Director 批准
- Gemma-2 hires concentration=0.2291（≈0.23），分类为 Flat（ddagger→dagger 已更新）

### 2. 🖥️ 基础设施快照
- **服务器**: westd-37397，2× RTX PRO 6000 96GB，当前均 idle
- **工作目录**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/`
- **代码仓库**: 当前分支 master，main 为 PR 目标分支
- **论文目录**: `docs/paper/`（LaTeX，最近 commit 998592d 更新 Gemma-2 hires 数据）
- **产出目录**: `artifacts/`（含 20+ 实验子目录、manifest.yaml、review_issues.yaml）
- **图表目录**: `figures/`（fig1_head_delta_heatmap_5model.pdf、fig_concentration_scatter.pdf）
- **活跃进程**: 无（所有实验已完成，无 RUNNING cron）
- **文献库**: `literature_map.yaml`（41 篇论文，8 个 category，最后更新 2026-05-14）

### 3. 📊 当前状态
所有实验已完成（67 个实验，35 success / 16 negative / 8 failed）。P0（8/8）和 P1（7/7）全部 DONE。

当前处于 **Paper Revision + Review** 阶段：
- 最近一轮工作：更新 Gemma-2 hires t1/t5 值（0.18→0.38）、统一 Qwen concentration 到 0.61、更新 heatmap 和 scatter 图
- review_issues.yaml 最后更新 2026-05-15 04:28（可能有未处理的 reviewer 反馈）
- dream_registry 中有一条 done 状态的 review（dream_20260514T002109），标记了增量性风险和多模型验证需求
- 无 RUNNING/PREPARING 实验，无等待中的 Worker 回调或 Cron

### 4. 📋 待办（条件触发式）
- Director 指示提交论文 → 检查 review_issues.yaml 所有 issue 已 resolved → 编译 PDF → 最终 provenance 审计
- Director 要求新实验 → 查 experiment_plan.yaml 中 P2 项（72B profiling 因磁盘空间 deferred）→ 需先确认磁盘/GPU 资源
- 收到 reviewer 反馈 → 对照 paper_framing.md 三个 core claims 判断影响范围 → 按 red-section 规范处理 negative 相关反馈
- ARR May 25 截止前 → 确保所有 paper_provenance.yaml 中 Tier 1/2 claims 有 exp_id 支撑
- C4 cross-dataset 实验结果需确认是否已写入论文（run_c4_cross_dataset.py 和 run_mistral_c4_cross_dataset.py 存在但需验证结果状态）

### 5. 🎯 战略上下文
**核心结论**: 简单的 cardinality constraint（≤8 heads at 2-bit）是主要方法贡献。约束使 greedy 和 MCKP solver 产生完全相同的最优分配（Δ=0.0000）。方法仅对 "spread" 异质性模式有效（Qwen: +27.3%），对 "spike"（Yi-1.5）和 "flat"（Mistral/Gemma-2）模式无效。

**决策链关键节点**:
- D001-D007: MSE→PPL pivot（MSE 指标与困惑度脱钩）
- D008-D011: 约束 MCKP 框架（k≤8 是关键）
- D012-D020: Solver 等价性证明（约束才是贡献，不是 solver）
- D021-D030: 跨架构分析 + 诊断框架（concentration≳0.50 AND t₁/t₅≲0.70）

**易错点**:
- 5 个模型中只有 Qwen 真正受益，论文 framing 必须诚实呈现这一点——不要过度宣称普适性
- Gemma-2 的 hires 和 standard concentration 几乎一致（0.2291≈0.23），分类从 ddagger 改为 dagger，确保论文中一致
- paper_provenance.yaml 有 66 个版本、200+ claims，修改任何数字前必须检查 provenance 链
- 不要混淆 constrained greedy 和 unconstrained greedy 的结果（差异巨大：PPL 11.23 vs 32.45）


---
