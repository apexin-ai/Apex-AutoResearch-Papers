# director / loop_13.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_13.md`
- **Structured JSON:** [`898d99a416e419cb47b4.json`](../../sessions/89/898d99a416e419cb47b4.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: max_messages
updated: '2026-05-21T08:37:56+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用项目分配的：westd-17855 cuda:0-5, westd-19828 cuda:0-1（共8卡）
- ≤3B 模型用 fp32，>3B 用 bf16（D079 约束）
- T=20 predict-then-verify v1 committed score = 3/5 (60%)，v2 未 commit = 4/5 (80%)。论文必须以 v1 为主，v2 仅作 sensitivity analysis（M057 教训）
- α=0.25 T=20 不在锁定预测文件中（只有 0.45/0.50/0.60/0.75/1.00），不得标记为 EXACT_MATCH（M056 教训）
- TY=7/8 已被 D143 retract（d_max artifact），论文中不得引用
- CSD 仅限 Discussion 章节（D142）
- 17855↔19828 SSH 不通，无法跨服务器传输文件

### 2. 🖥️ 基础设施快照
- 服务器：westd-17855 (6 GPU) + westd-19828 (2 GPU)，SSH via connect.westd.seetacloud.com
- 工作目录：/root/autodl-tmp/distrib_canary_collapse
- Python：/root/miniconda3/bin/python（conda base 环境）
- 本地 artifacts：/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/
- 活跃实验（reset 前状态，需验证）：
  - 17855: a000_s47(cuda:0), gpt2m_s43(cuda:1), a000_s45(cuda:2), scale_69b_s43(cuda:3), a052_s43(cuda:4), a046_s43(cuda:5)
  - 19828: a000_s48(cuda:0), a000_s46(cuda:1)
- D37 代码已就绪：eval_task_degradation.py, mech_interp_analysis.py, recovery_train.py 均在远程 dry-run 通过

### 3. 📊 当前状态
**关键背景**：用户批准了论文重大突破方案——从"方法论文"转为"现象发现论文"。新标题方向："Mapping the Detectability Landscape of Iterative Model Collapse"。用户原话："大胆去想、深度思考，卡给你无限开"。

**4个突破方向（全部用户批准，全部并行）**：
1. **Detection Phase Diagram (α × T)** — 需 GPU。新增 T=5/15/25 × α=0.45/0.50/0.60/0.75 = 12组实验。代码基于现有脚本改 --num_generations。**代码准备指令已发给 Agent 但 Agent 两次 reset 未执行。**
2. **Specification Curve Analysis** — 零 GPU。100+ analytical specs 的系统性敏感度分析。需先等 5method 分析完成。
3. **Transfer Entropy / MI Decomposition** — 零 GPU。解释 sync dip：MI 高但 TE 低。
4. **Theoretical Detection Lower Bound** — 零 GPU。推导 δ_min(T) 并与实证验证。

**已有数据**：141 实验（~95 成功），完整 dose-response 图谱 T=10 + T=20 五个 α 点。Phase transition α_c∈[0.48,0.50] 两种子确认。Sync dip [0.55,0.65] 结构性（T=20 不改善）。

**文献调研完成**：24篇论文。最直接竞品 SIGMA (白盒 spectral)，我们是黑盒 causal。Lu et al. ICML 2023 有 poisoning phase transition 先例。Bonn et al. AAAI 2025 做了 2D poisoning heatmap——我们做 model collapse 检测的 2D 相图是空白地带。

### 4. 📋 待办（条件触发式）
- Agent 就绪 → **立即重发 4 方向并行执行指令**（Agent 两次 reset 都没收到完整方案）。优先：Phase Diagram 代码准备 + TE/MI Worker + Detection Bound Worker + Spec Curve Worker
- a046_s43 / a052_s43 完成 → 释放 17855:4/5，立即上 Phase Diagram T=5 实验（最快出结果）
- scale_69b 完成 → 释放 17855:3，上 Phase Diagram T=5 或 T=15
- 4 个 null seed 全部完成 → 计算 FPR CI（目标 N_eff=6-7，CI 收窄到 ~[0%, 39%]）
- Spec Curve / TE-MI / Detection Bound 结果回来 → 评估是否支持 reframing，派 Paper Agent 写新版论文
- Round 7 审稿报告返回 → 按 review-report-action skill 处理（但新 reframing 可能使旧报告部分过时）
- C2 Power Theory 已决定降格为"Power Scaling Interpretation with known limitations"（sync dip 不随 T 改善）

### 5. 🎯 战略上下文
- **核心转型**：论文从 3.0 Findings 困境突破的关键是重新定位贡献——不是"我们用 PermG 检测 collapse"（标准工具无新意），而是"我们发现并刻画了 model collapse 检测能力的复杂景观"（现象发现）
- **Phase Diagram 是最高价值方向**：一张 α×T 2D 热力图就能改变审稿人对论文的认知。文献中从未有人画过 model collapse 检测的相图
- **Sync dip 是结构性的**：T=20 时 α=0.60 仍然 0/8（v1 预测 3/8 outside CI）。Power Theory 解释不了。这是独立现象，需要独立机制解释（TE/MI 方向）
- **最容易判断错的事**：(1) 不要把 v2 prediction score 当主结果报告；(2) 不要在 sync dip 区间声称 T 增长能解决检测问题；(3) Agent 已经 reset 两次没执行突破方案代码——第一件事就是确认 Agent 是否收到并开始执行
- **审稿阶段已启动**（Round 7 提交中），但 reframing 可能需要 Round 8
- 161 个决策记录在 decisions.yaml，最近关键：D159（Round 7 reframe）、D160（FPR multi-layer evidence）、D161（t20_a025 结果）


---
