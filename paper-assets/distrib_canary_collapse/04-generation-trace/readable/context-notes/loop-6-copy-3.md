# reviewer / loop_6.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_6.md`
- **Structured JSON:** [`ea20135217bc785a3932.json`](../../sessions/ea/ea20135217bc785a3932.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_wall_time
updated: '2026-05-15T09:41:58+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0 和 cuda:1（westd-19828 只有 2 张 RTX PRO 6000 Blackwell 96GB）
- consensus_framework.py 必须用 `apply_fdr=True`（D029 决策），任何调用 `load_sig_matrix` 不带参数即可（默认 True），显式传 `apply_fdr=False` 需要 Director 批准
- cross_alpha_analysis_v4.py 对单 seed α 点无 FDR 校正（我已报 WARNING），执行前需确认 D029 的 FDR 一致性修复是否落地到该脚本
- formalization 文档 `consensus_framework.md` 和 `consensus_sensitivity_table.json` 中的数字目前是 **过时的**（raw significance），必须用 FDR 修正后的远程数据更新后才能引用

### 2. 🖥️ 基础设施快照
- 服务器：westd-19828(root)，工作目录 `/root/autodl-tmp/distrib_canary_collapse`
- Python：`/root/miniconda3/bin/python`，conda base 环境
- HF cache：`/root/autodl-tmp/.hf_cache`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/`
- 关键远程产出：`results/mvp/analysis/consensus/`（consensus_classification.json, sensitivity_analysis.json, fpr_fnr_table.json, fpr_fnr_loo.json — 均已 FDR 修正，时间戳 17:34）
- 关键远程产出：`results/mvp/analysis/method_ablation.json`（158K，含 `significant` 和 `significant_fdr` 双字段）
- 活跃进程：plan_006_s42 (cuda:0, ~gen 16/20)，alpha_sweep_a075_s42 (cuda:1, ~gen 5/10)
- 无 wandb（`report_to="none"`）

### 3. 📊 当前状态
刚完成 D029 FDR fix 第二轮审查（PASS）。FDR 修复已生效并重新生成共识输出。

**RUNNING**：
- plan_006_s42：cuda:0，20gen 扩展实验（α=1.0），~gen 16/20，supplementary（T=21 power）
- alpha_sweep_a075_s42：cuda:1，α=0.75 第 5 个 alpha 点，~gen 5/10，**关键边界实验**（决定 Claim 1 scope）

**QUEUED**（等 GPU 释放）：
- alpha_sweep_a025_s43, a025_s44, a050_s43, a050_s44（D026 multi-seed）
- alpha_sweep_a010_s42

**等待中**：
- cross_alpha_analysis_v4.py 部署就绪但需等 a075 完成才能执行
- formalization 文档更新（P0，数字已过时）

### 4. 📋 待办（条件触发式）
- a075_s42 完成 → 验证 gen 10 metrics；检查 Granger FDR-sig：如 sig → Claim 1 scope "α≥0.75"；如 null → Claim 1 确定为 "α=1.0 only"
- a075 完成 → cross_alpha_analysis_v4.py 可执行，审查输出时重点关注：单 seed α 点的 FDR 一致性问题（我已报 WARNING，见下方§5）
- plan_006_s42 完成 → 验证 gen 20 metrics（ppl 应极高 >3000），T=21 Granger power 是否优于 T=11
- formalization 文档更新 worker 完成 → 核对所有数字与 FDR 修正后的 JSON 一致，特别是 entropy→d3 (8/9 不是 9/9)、ece→d1 (7/9 不是 8/9 不是 9/9)、最严格配置 (2 不是 3)
- multi-seed 实验开始 → 核对 GPU 分配在 cuda:0/1 白名单内
- 任何 consensus 相关论文章节提交审查 → 必须基于 FDR 修正后数据，拒绝引用旧数字

### 5. 🎯 战略上下文
**核心叙事**（D027 Option B）：方法论陷阱 + 多方法共识框架。三个 Claims 按强度排序：Claim 3（方法敏感性）> Claim 2（regime map）> Claim 1（Granger-causal case study）。

**FDR 修正后关键数字变化**（易错）：
- entropy→d3 稳定性从 1.0 降至 0.889——"perfectly stable" 层只剩 entropy→d1/d2
- ece→d1 从 0.889 降至 0.778——旧文档写 9/9 是错的（我第一轮审查就发现了，当时以为是 8/9，FDR 后实际是 7/9）
- effective_rank 在 FDR 后完全归零（0/9 稳定性）——不再有任何 robust association
- perm_granger FPR 从 0.11 降至 0.0（FDR 消除假阳性——正面结果！）
- 最严格配置 (5/5,4/4) 从 3 对降至 2 对

**最容易判断错的事**：
1. 不要信本地 artifacts 里的 consensus 数字——它们是旧的（raw significance）。真源在远程 `results/mvp/analysis/consensus/` 下的 4 个 JSON 文件
2. cross_alpha_analysis_v4.py 有 FDR 非对称性问题：α=1.0 用 FDR（通过 load_sig_matrix），α=0.00-0.75 用 raw（直接调用 method functions）。我已报 WARNING 但尚未修复
3. Phase 2 证据显示 differenced_xcorr 在 α=0.0 null control 下有 50% sig rate——FPR ground truth 已决定从 differenced 切换到 α=0.0 null（D028），但代码中的 `DIFF_INDEX = 1` 注释仍说 "differenced_xcorr is the FP ground truth"


---
