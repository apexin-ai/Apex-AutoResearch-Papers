# reviewer / loop_16.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_16.md`
- **Structured JSON:** [`fef69b062b06751288ef.json`](../../sessions/fe/fef69b062b06751288ef.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 16
reason: max_wall_time
updated: '2026-05-17T17:11:10+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0 和 cuda:1（bjb1-45299）。任何进程跑在其他设备上立即 CRITICAL。
- 论文梯度分解数据：Paper Table 8 是正确版本（reward=49%, obs=16.3%, KL=34.7%）。paper_framing.md D061 的 obs=93%/reward=0% 已被独立验证确认为**错误且不可复现**，绝不可引用。
- NVE 计算口径：所有 NVE 必须用 `(V/E)_config / (V/E)_baseline` 在相同 step 计算，不能混用 civo/ve_ratio 和 raw value_mean/eval_return 两种来源。022b 的 NVE=0.63× 用的是 civo/ve_ratio。

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-45299 (root)，工作目录 `/root/autodl-tmp/event-gated-adaptive-horizon`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/`
- 论文目录：`docs/paper/sections/` (本地)，含 abstract/intro/methodology/results/analysis/conclusion/appendix/related_work .tex
- 梯度分析 JSON：服务器 `artifacts/analysis/gradient_decomposition_008d_corrected.json`（权威数据源）
- 活跃进程：exp_023a (PID 683708, cuda:0), exp_023b (PID 680126, cuda:1)
- 无 wandb 配置（本项目不检查 wandb）

### 3. 📊 当前状态
**刚做完：**
- 梯度分解矛盾议题已关闭（Paper Table 8 正确，D061 错误，经独立验证确认）
- em-dash 修复 worker 已审查通过（27 处修复，无遗留）
- 发现并报告 CRITICAL：abstract 仍含旧数据（93%/0% + "completely eliminates"），与全文矛盾
- 报告 WARNING：analysis.tex:23 和 conclusion.tex:18 的 detector 数据未同步（FPR 2/7→2/8, ten→eleven, two→three environments）

**RUNNING 实验：**
- exp_023a_cheetah_baseline_s0：step ~85K→200K, cuda:0, eval=330.6, 预计 ~2-3h 完成
- exp_023b_cheetah_baseline_s1：step ~125K→200K, cuda:1, eval=537.7, 预计 ~1.5-2h 完成

**QUEUED：** exp_021_full_sgs_cheetah_s1（等 GPU 释放）

**等待中：** abstract 修复 worker（Agent 已派），Director 对 analysis.tex/conclusion.tex 同步修复的回应

### 4. 📋 待办
- abstract 修复 worker 完成 → 审查：(1) 93%→16-22% obs / 0%→38-49% reward 是否已修正 (2) "completely eliminates"→50% prevention (3) 与 Introduction/Conclusion 一致性
- analysis.tex/conclusion.tex 同步 worker 完成 → 审查 FPR 2/7→2/8 和 "ten/two→eleven/three" 是否全部替换
- paper_framing.md D061 更新 worker 完成 → 核实数字与 Table 8 一致
- exp_023b 完成 → 独立核实 Cheetah baseline eval（预期 ~700-900），确认可作为 NVE 归一化基准
- exp_023a 完成 → 对比两 seed baseline 一致性
- exp_021 启动 → 检查 GPU 设备合规（必须在 cuda:0 或 cuda:1）
- Table 1 精简 worker 完成 → 审查 ≤8 行选择是否保留关键证据链

### 5. 🎯 战略上下文
- 核心结论链：trained dt_emb + multi-rate exposure → obs decoder gradient → RSSM fidelity gap (2.78×) → critic overestimation → CIVO collapse。因果控制铁三角（008d/008f/008a）+ AUROC=0.926 是最强证据。
- CoRL 2026 DDL 2026-05-29（12天），预估 borderline accept (40-50%)。最大风险：无有效 mitigation + 叙事过载。
- **易错点 1**：paper_framing.md D061 数据是错的（obs=93%/reward=0%），不要用它验证论文——用服务器 `gradient_decomposition_008d_corrected.json`。
- **易错点 2**：022b 的 "baseline 比" worker 曾多次算错（77.3%、9.1×），正确值 300.7/915.7=32.8%。
- **易错点 3**：019b eval 26.64 是 final（@200K），peak 是 26.9（@132.5K）。Table 1 列的是 @final。
- **易错点 4**：进程挂起判断需多次快照确认（memory 中有记录：009h 被误杀教训）。
- D086 决策：梯度数据统一为 Paper Table 8 版本。D083：019b 是 TN（detector 正确不触发）。


---
