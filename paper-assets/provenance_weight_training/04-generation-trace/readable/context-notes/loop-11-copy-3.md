# reviewer / loop_11.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_11.md`
- **Structured JSON:** [`d7ac16dd5952c29ab8f9.json`](../../sessions/d7/d7ac16dd5952c29ab8f9.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: max_wall_time
updated: '2026-05-16T05:24:21+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：`gpu_ids=[0,1,2,3]`（westd-47453 全部 4 卡 RTX 6000 Pro 96GB），但必须核实进程实际占用的卡号是否在白名单内
- τ sweep 实验（tau_05/06/07/09/095）的 n_min 问题已经过 D044→D048 决策链确认：**全部使用 n_min=2**，D044 的 "n_min=3 confound" 是误报。不要重新发起 confound 质疑
- n_min=2 是论文主结果（D043），n_min=3 降为 sensitivity analysis。不要将 n_min=3 作为推荐方法
- 论文是 continued pretraining（from_pretrained），不是 from scratch（D039）
- ESS-only 不是"崩溃"——它在 ρ=0.4 下劣于 uniform（PPL 17.723 vs 17.694），是 max-intervention 的 negative evidence，不要用 "collapse" 这个词

### 2. 🖥️ 基础设施快照
- 服务器：westd-47453(root)，工作目录 `/root/provenance_weight_training`
- Python：`/root/miniconda3/bin/python`，conda base 环境
- 模型：`/root/provenance_weight_training/models/Qwen/Qwen3-0.6B`
- 数据：`data/scored_data.jsonl`（ρ=0.4, 371K 条），`data/scored_data_60.jsonl`（ρ=0.6）
- Eval holdout：`data/human/eval_holdout.jsonl`（5000 docs, ~4M tokens）
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/`
- artifacts：`artifacts/` 下有 metrics_summary.csv、4 张 results_table CSV、_project/paper/*.tex、_project/data/table1-3.csv + figure CSVs
- GPU 预算：~10-12h 剩余（截至 05:20 UTC）
- EMNLP ARR DDL：2026-05-25（9 天）

### 3. 📊 当前状态
**刚完成的审查**：
1. `experiment-data-compilation` worker（4 张 results_table CSV）→ 已 post，发现 ablation CSV n_min 注释错误、τ sweep b_star 数据缺失、adaptive ρ=0.6 退化最严重
2. `compile-results-table` worker（table1/2/3 CSV + consistency_audit.md）→ 已 post，发现审计 C5/W4 假阳性（negative 结论实验被过滤遗漏）、table1_main_results.tex 将 n_min=3 加粗为 best（矛盾 D043）、grid-best 未反映 b=0.3 发现

**RUNNING 实验**（我在等结果的）：
- `grid_b0_1_seed42`：决定 b-PPL 曲线在 b<0.3 是否 U-shaped → 影响 Claim 2 grid-best baseline 诚实性
- `contamination_60_tau07_seed42` / `contamination_60_tau06_seed42`：ρ=0.6 下 τ 下调是否恢复 adaptive 性能 → 决定 Claim 3 叙事
- `detect_remove_baseline_seed42`：回答 "why not just filter" 审稿人关切

**等待中**：无 pending worker 回调。Director 尚未回复我最近两条审查。

### 4. 📋 待办（条件触发式）
- grid_b0_1_seed42 完成 → 核实 PPL 是否 < 17.640（b=0.3）。若是 → Claim 2 grid-best 需更新为 b=0.1；若 > 17.640 → 确认 b=0.3 为 grid-best，b-PPL 曲线 monotonic decreasing 到 b=0.3 then flat/increasing
- contamination_60_tau07/tau06 完成 → 对比 adaptive(τ=0.7/0.6) vs grid(b=0.5)=17.704 at ρ=0.6。若 τ 下调恢复到接近 grid → Claim 3 可调整为 "τ 需随 ρ 微调但 safe range 仍宽"；若仍劣 → 论文必须诚实报告 adaptive 在高 ρ 下 suboptimal
- detect_remove 完成 → 对比 PPL vs adaptive/grid。若接近 → 弱化 reweighting 叙事；若明显差 → 支持 "soft reweighting > hard filtering"
- 收到章节审查请求 → 先检查 Agent 是否读过 red-section skill（L1 硬约束），再按 5.1/5.2 审查维度执行
- 收到 ROADMAP 更新通知 → 重点审查 Claim 2 覆盖率（b=0.3 跨 seed 验证是否排上了）和 GPU 预算是否够

### 5. 🎯 战略上下文
**核心叙事**：Dual-constraint adaptive b*（α_eff 下界 + ESS 上界）= minimum intervention principle。对比：ESS-only = max intervention（劣于 uniform），grid-best = manual tuning（b* 不跨 seed/ρ 稳定）。

**关键决策链**：D020-D023（α_eff 是否 decorative → 否，dual-constraint 恢复）→ D025（τ 降级为 empirical hyperparameter）→ D034（n_min∈{2,3}均有效）→ D043（n_min=2 为主结果）→ D045（ρ=0.6 adaptive τ=0.8 suboptimal）→ D049（启动写作冲刺）→ D050（b=0.3 发现）

**最容易判断错的事**：
1. **不要信 "ESS-only 崩溃" 的说法**——PPL 17.723 vs uniform 17.694，差 0.029，是 degradation 不是 collapse。ROADMAP 里用了 "collapse" 但数据不支持这个力度
2. **Adaptive 在 ρ=0.6 退化最严重**（+0.087 > uniform +0.072），这是尚未解决的叙事风险。D045 的 τ-ρ 诊断实验是关键——如果 τ 下调不恢复，"graceful degradation" claim 站不住
3. **table1_main_results.tex 有两个版本冲突**——results.tex 用 n_min=2 为主（正确），table1_main_results.tex 用 n_min=3 为 bold best（矛盾 D043）。确保论文编译引用正确版本
4. **Grid-best 不稳定**——seed42 best=b=0.3，seed123/456 best=b=0.5。b=0.3 没有跨 seed 数据。论文 grid-best 行要么用 per-seed best（混合 b），要么只报 b=0.5（3-seed），不能只报 seed42 的 b=0.3
5. **consistency_audit.md 的 C5/W4 是假阳性**——tau_09/095 和 bs8 在 registry 中以 conclusion="negative" 存在，审计过滤条件遗漏了它们


---
