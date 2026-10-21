# reviewer / loop_20.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_20.md`
- **Structured JSON:** [`3b60abf69390472b2296.json`](../../sessions/3b/3b60abf69390472b2296.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 20
reason: max_wall_time
updated: '2026-05-22T18:45:50+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0/1/2/3（westd-41312 4× RTX PRO 6000 96GB），本项目独占，无越界风险但每次审查仍需核对
- ρ=0.3 实验（D120）仅限 1 seed (42)、结果仅 appendix/rebuttal 储备，**不可改变论文核心叙事**
- 论文 p-value 已统一为 3dp 精度源（t=−7.1, p=0.019, p_BH=0.078）——不可回退到全精度值（t=−6.2, p=0.025），否则 p_BH 与 raw p 来源不一致
- ρ=0.4 adaptive-vs-uniform **不可 claim "statistically significant"**——p_BH=0.078 在任何 ≥k=4 的族校正下都不显著。论文现用 "consistently lower" + bootstrap CI

### 2. 🖥️ 基础设施快照
- 服务器：westd-41312 (root)，工作目录 `/root/provenance_weight_training`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/`
- 论文路径：本地 `docs/paper/sections/*.tex`（不在远程服务器）
- 数据：`/root/provenance_weight_training/data/scored_data.jsonl`（371K 行 ρ=0.4），`scored_data_rho03.jsonl`（235K 行 ρ=0.3，D120 新生成）
- Artifacts：本地 `artifacts/bonferroni_holm_results.md`、`artifacts/_project/data/bootstrap_ci_results.csv`、`artifacts/alpha_eff_variance_decomposition.md`
- 活跃进程：无（4 GPU 全空闲 0% util 0 MiB）
- Registry：238 实验（149 成功 / 12 负向 / 39 失败），无 RUNNING

### 3. 📊 当前状态
刚完成 ROADMAP D120 审查（ρ=0.3 防御性实验批准）。本轮核心工作：
- ✅ C2 Bonferroni-Holm 结果审查 → 发现 p-value 精度不一致 → 论文已修复为 3dp
- ✅ discussion.tex "mixed sign" 事实错误 → 已修复为 "directionally consistent"
- ✅ Abstract 统计措辞审查 → 已更新（不再 claim significance for ρ=0.4）
- ✅ α_eff variance decomposition 审查 → 70/30 分解合理，可用于 C3 rebuttal
- ✅ ROADMAP 审查 → Round 10 全部 13/13 resolved

ρ=0.3 数据已就绪但训练尚未启动（registry 无 RUNNING）。Round 11 审稿 pending approval。

### 4. 📋 待办
- ρ=0.3 训练启动通知 → 核查 GPU 设备号 (应为 cuda:0/1)、训练参数、数据路径一致性
- ρ=0.3 训练完成 → 审查 eval 结果：Δ(adaptive−uniform) 方向 + 与 ρ=0.2/0.4 趋势一致性；如果 works (Δ<0)，effective range 可收紧到 ρ≥0.3
- Paper Agent 提交 Round 11 patch → 审查模式 B：核查叙事一致性、数字与 registry 匹配、统计措辞合规（尤其 p_BH 相关表述）
- 任何论文编译/提交前 → 最终 checklist：limitations 段实质性、BH 校正信息完整、abstract 与正文数字一致

### 5. 🎯 战略上下文
- 审稿轨迹 2.5→3.0→3.0，目标 3.5+。核心障碍是结构性的（小效应 Δ=−0.020、n=3、下游 null）——Round 11 的胜算在于统计诚实度和叙事紧凑度的改进
- D115 是关键 pivot：从 "method paper" 转为 "analysis paper"（when/why/how），贡献排序 (1) Epoch confound (2) Detector requirements (3) Mechanism decomposition (4) Adaptive b* tool
- ">95% epoch confound" 用的是 vs-adaptive 基线（Δ残差=0.017），vs-uniform 基线给 91%。论文明确标注 "relative to adaptive reweighting"，不要混淆
- D&R epoch-matched 3-seed 残差 Δ=0.017 方向一致（全部 D&R 更好），不是 noise——但论文框架下这属于 "small residual within cross-seed variance"，是有意的 framing 选择
- 最容易判断错的事：n_min/B coupling 规则——B=8 必须 n_min=4（ratio 0.5），B=4 用 n_min=2。之前 B=8 配 n_min=2（ratio 0.25）导致退化，已用正确配置重跑确认


---
