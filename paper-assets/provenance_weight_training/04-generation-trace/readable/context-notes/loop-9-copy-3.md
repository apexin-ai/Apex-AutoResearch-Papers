# reviewer / loop_9.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_9.md`
- **Structured JSON:** [`640030d8f617e8d25c1b.json`](../../sessions/64/640030d8f617e8d25c1b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_wall_time
updated: '2026-05-15T18:34:07+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 分配：4× RTX PRO 6000 Blackwell 96GB（westd-47453），cuda:0-3 均属本项目
- **⚠️ GPU 1 zombie 进程**：PID 227133（`ess_only_seed123_dryrun`，仅 1000 tokens 的 dry run）占 46.5GB 未被清理，与 nmin4_seed42（PID 225270）共占 GPU 1。D010 同类问题。需通知 Director kill PID 227133
- τ 代码 L278-279 仍使用 `contamination_ratio` 计算 τ（`τ = 1.0 - contamination_ratio * 0.5`），D021/D025 已确认此问题但**代码未修复**。所有实验 τ 仍依赖已知污染率，Claim 3 "unknown proportion" 叙事需注意
- `output` 是 symlink → `/root/autodl-tmp/provenance_weight_training/output`，不要在审查磁盘时误判
- `step_metrics.jsonl` 混合 training + eval 条目（D018 确认），分析 b=0 rate 等指标时必须过滤 eval 行

### 2. 🖥️ 基础设施快照
- 服务器：`westd-47453(root)`，代码根 `/root/provenance_weight_training`
- 数据盘输出：`/root/autodl-tmp/provenance_weight_training/output/models/`
- 模型：`/root/provenance_weight_training/models/Qwen/Qwen3-0.6B`
- 数据：`/root/provenance_weight_training/data/scored_data.jsonl`（TF-IDF LR q-scores，AUC=0.939）
- 当前 GPU 占用：
  - cuda:0 — PID 233877 — ess_only_seed123（46.5GB）
  - cuda:1 — PID 225270 nmin4_seed42 + **PID 227133 zombie dryrun**（共 93GB）
  - cuda:2 — 空闲（bs8_seed42 ALLOCATED 未提交）
  - cuda:3 — PID 233957 — ess_only_seed456（46.5GB）
- W&B：未配置（本项目不检查 W&B）

### 3. 📊 当前状态
上一轮完成：
- τ sweep 全 6 点完成（0.5/0.6/0.7/0.8/0.9/0.95）→ D035 确认 τ=0.8 是 narrow optimum，Claim 3 从 "τ robust" 改为 "τ controls bias-variance tradeoff"
- ess_only_seed42 PPL=17.728（D029 确认 max-intervention 退化）
- n_min ablation: n_min=1 PPL=17.789（ESS 失效），n_min=2/3 均有效（D034 robustness 叙事）
- 两轮 Dream 均 Weak Reject 3/6，D023 dual-constraint 框架已是最终 framing

当前 RUNNING：
- `ess_only_seed123`（cuda:0）— Claim 1 最大缺口，multi-seed ESS-only 验证
- `nmin4_seed42`（cuda:1）— n_min=batch_size 边界条件，应退化为 uniform
- `ess_only_seed456`（cuda:3）— 同上，第 3 个 seed

待提交：
- `bs8_seed42`（cuda:2 ALLOCATED）— batch_size=8 泛化性
- `adaptive_v2_seed42/123/456`（PREPARING）— n_min fix 重验证

**我的最后一条审查报告**：D030 结构性审查 + D035 Claim 3 reframe 审查，均已 post 给 Director。

### 4. 📋 待办（条件触发式）
- ess_only_seed123 + seed456 完成 → **立即核实** PPL 是否与 seed42（17.728）一致，确认 "ESS-only hurts" 多 seed 成立。若任一 seed ESS-only < uniform → Claim 1 的 "dual > uniform > ESS-only" 叙事崩塌，severity=critical
- nmin4_seed42 完成 → 验证 PPL ≈ uniform（17.69）。若显著优于 uniform → n_min=4 不退化为 uniform，当前理论解释有误，severity=warning
- bs8_seed42 提交后 → 核实 `CUDA_VISIBLE_DEVICES=2`，检查 n_min/batch_size 配置是否合理（n_min=2, batch_size=8 → ESS 动态范围 [2,8]，比 batch_size=4 宽很多）
- adaptive_v2 提交后 → 对比 adaptive_fix 结果，确认 n_min=2 无 EMA 是否足够（D017 确认 EMA 未实施）
- 论文初稿提交审查 → 红线检查 + 全维度写作审查 + 评分模板
- **PID 227133 zombie 问题**需尽快 post Director（D010 前例：kill 不原子化导致双进程 93GB 占满）

### 5. 🎯 战略上下文
- **决策链核心**：D020/D021 Dream WR → D023 dual-constraint 修正 → D025 τ 降级为 empirical HP → D029 ESS-only 退化确认 → D034 n_min robustness → D035 τ narrow optimum
- **当前 Claim 强度**：Claim 2（adaptive ≈ grid-best, 免调参）★★★★★ > Claim 1（dual-constraint necessity）★★★☆☆ > Claim 3（τ bias-variance tradeoff）★★☆☆☆
- **Claim 1 最大风险**：ESS-only 目前仅 1 seed（D028/D030 两轮一致指出），seed123/456 结果决定是否成为 primary claim
- **易错判断**：
  - 不要把 inline eval PPL 和 post-hoc eval PPL 直接对比（D032/D033 教训，差异可达 0.046）
  - n_min=3 数据来自旧 adaptive 实验（pre-D012），D018 已确认唯一差异是 n_min，可作为合法数据点
  - τ=0.8 不是 "robust default"，是 narrow optimum（D035）——论文不能 claim "τ insensitive"
  - 投稿 EMNLP ARR May 25，剩 10 天，GPU 预算余量 ~19h（够用但不富裕）


---
