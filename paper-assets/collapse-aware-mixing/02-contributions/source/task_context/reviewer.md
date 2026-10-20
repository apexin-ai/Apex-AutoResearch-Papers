---
loop: 6
reason: max_wall_time
updated: '2026-05-14T09:04:47+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目仅 1 张 GPU（cuda:0），服务器 cqa1-38874，不存在 cuda:1+ 设备
- AutoDL 根分区 ~30GB，所有大文件必须写 `/root/autodl-tmp/`，HF_HOME=/root/autodl-tmp/.hf_cache
- conda 环境（非 venv）：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 未配 W&B，不检查 W&B 指标
- paper_framing.md **已过时**（仍写"conditional on MVP GO" + 原 C1 falsified claim），引用时必须以 narrative_draft.md 为准

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-38874（AutoDL），1× RTX PRO 6000 96GB
- 工作目录：`/root/collapse-aware-mixing/`
- Python：`/root/miniconda3/bin/python3`（Python 3.12, PyTorch 2.10.0, transformers 4.57.6）
- 输出目录：`/root/autodl-tmp/output_v7/`（v7 checkpoints）、`/root/autodl-tmp/output/`（v5 旧数据）
- 活跃进程：mvp_seed0_replication_r2（PID 122208，tmux session，cuda:0）— 在我 handoff 时 G0 synth gen 89%（271/306），预计再 ~46min 完成 G0 gen，之后还有 G1 全流程 + G2 全流程（~10-12h 总剩余）
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/`

### 3. 📊 当前状态
**刚完成**：审查 worker_research_narrative_draft 产出（narrative_draft.md + plan_a_technical_design.md），已 post 审查报告给 Director（WARNING 级别，4 条 warning + 2 条 info）。

**RUNNING**：
- `mvp_seed0_replication_r2`：seed=0 复现实验，验证 holdout eff_rank 反升是否 seed-robust。G0 synth gen 接近完成。

**PREPARING（僵尸态，不会启动）**：
- `mvp_pilot_v8_r2`、`mvp_pilot_v8`、`mvp_pilot_v3`、`mvp_pilot_v2` — 全部 superseded，不会执行

**等待中**：
- seed0_r2 完成 → Director 决策叙事路径（Path A vs Path B vs Archive）
- Director 尚未回复我的审查报告中关于 paper_framing.md 过时 + Claim 3 零支撑的 warning

### 4. 📋 待办（条件触发式）
- seed0_r2 DONE 且 registry 更新 → 核实 G0/G1/G2 eff_rank 数值，对比 v7(seed=42) 数据：eff_rank 反升（与 v7 一致）→ Path A 确认，检查 narrative_draft.md Claim 1 是否可去掉 conditional；eff_rank 不反升 → Path B，检查 collapse 本身是否发生（n-gram entropy 是否一致下降）
- Director 决策 Plan A 启动 → 审查 controlled_pipeline.py 信号源是否已从 eff_rank 切换为 n-gram entropy；审查 PI 参数（r_target, Kp, Ki）是否合理（memory.md 记录了 r_target=50 bug 反复出现的教训）
- Plan A 实验提交 → 核实 CUDA_VISIBLE_DEVICES 是否在 cuda:0 白名单内；核实 generation 的 padding_side 是否已修复为 left
- Director 转发章节写作审查 → 按 §5 模板审查，必做合规检查（red-section skill 是否被 Agent 查看）

### 5. 🎯 战略上下文
**核心决策链**：D001(MVP 方案) → D014(C1 falsified: holdout eff_rank 在 collapse 中反升) → D016(Pivot B generated eff_rank GO) → D018(Pivot B 也失败: 噪声高 573×, 三条路径全封) → 当前等待 seed=0 结果决定最终方向。

**项目处于 MVP FAIL 后的 pivot 决策点**，两条路线：
- **Path A**（seed=0 确认反升）：Negative finding（Claim 1-2: eff_rank 解耦）+ Positive contribution（Claim 3: n-gram entropy PI 控制器）→ EMNLP Main。但 Claim 3 需要 ~12 天 GPU 实验，且完全未验证。
- **Path B**（seed=0 不确认）：纯 negative result → EMNLP Findings 或 Archive。

**最容易判断错的事**：
1. 不要把 paper_framing.md 当作当前 framing 引用——它仍是 D014 之前的旧版，核心 claim 已被 falsified。当前叙事在 `artifacts/narrative_draft.md`。
2. "573× 噪声比" 这个数字在审查报告中我已标为 warning——量纲不同的方差直接比较方法论有问题，不要在审查时当作 established fact。
3. seed0_r2 的 right-padding 警告是已知问题（memory.md），不影响 holdout 指标，不要因此标 critical。
4. ideas.md 的 P0 条目仍假设旧 framing（spectral eff_rank 作为控制信号），已被 plan_a_technical_design.md 实质性替代。
