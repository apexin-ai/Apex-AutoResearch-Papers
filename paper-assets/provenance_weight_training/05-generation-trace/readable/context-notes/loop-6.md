# director / loop_6.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_6.md`
- **Structured JSON:** [`3b4c8a9bdf33b23b3122.json`](../../sessions/3b/3b4c8a9bdf33b23b3122.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_messages
updated: '2026-05-15T10:06:54+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0/1/2/3 on westd-47453，严禁使用其他设备
- τ 已修复为 CLI 参数 `--tau 0.8`（默认），**禁止**在代码中用 `1.0 - contamination_ratio * 0.5` 计算 τ（D021/D025）
- 所有新训练脚本必须从最近已验证脚本 fork（bf16 + 无 inline eval），不从旧模板复制（grid_b_low 事故教训）
- **禁止 checkpoint resume**：已确认 HF Trainer resume 导致 PPL 偏高 +0.15~0.25（D026），优先从头重跑
- grid_b_low 在 cuda:1 被 cron 误杀两次（WANDB_MODE=disabled + 手动 bash 提交导致 reconcile_crons 误判），所有实验必须走 allocate_and_submit

### 2. 🖥️ 基础设施快照
- 服务器：westd-47453 (connect.westd.seetacloud.com)，account=root
- 工作目录：/root/provenance_weight_training
- Python：/root/miniconda3/bin/python（conda base 环境）
- 模型：Qwen3-0.6B，数据：200M tokens FineWeb + 40% synthetic contamination
- 训练脚本目录：/root/provenance_weight_training/training/
- 输出目录：/root/provenance_weight_training/output/models/
- WANDB：disabled（WANDB_MODE=disabled）
- 活跃进程：
  - cuda:0: golden_ratio_seed42 PID=193921
  - cuda:1: ess_only_seed42 PID=189240（**最关键实验**）
  - cuda:2: nmin1_seed42 PID=194005
  - cuda:3: tau_06_seed42 PID=195746
- 4 个 cron 监控活跃
- ETA：~13:00-13:30 UTC 全部完成

### 3. 📊 当前状态
刚完成：ROADMAP 更新、experiment_summary.md checkpoint artifact 脚注修正、τ sweep 全 5 组脚本创建、ml-experiment-guide 更新（checkpoint resume + 脚本 fork 规则）、D026/D027 决策记录。

4 个实验 RUNNING（见上），全部 ~3.5h，无 inline eval。

τ sweep 剩余 4 组（τ=0.5/0.7/0.9/0.95）脚本已就绪，registry 预注册中。当前批完成后 4 GPU 并行提交。

文献扫描 Worker 仍在运行（35+ 论文覆盖）。

### 4. 📋 待办
- **ess_only_seed42 完成 → 立即 post-hoc eval → 与 adaptive_fix 对比 PPL**。这是决定论文 framing 的关键实验：dual > ESS-only → min-intervention story 成立；dual ≈ ESS-only → reframe 为 empirical study；dual < ESS-only → 需 pivot（D023 Key Risk #1 三级应对方案已写入 paper_framing.md）
- golden_ratio/nmin1/tau_06 完成 → post-hoc eval → 更新 experiment_summary.md
- 4 GPU 释放 → 并行提交 τ=0.5/0.7/0.9/0.95（脚本已就绪，需 approve + allocate）
- τ sweep 全部完成 → 分析 τ insensitivity curve，确认 0.6-0.9 范围是否都 work（Claim 3 支撑）
- τ sweep 后 → n_min=4 + batch_size=8/16（如预算允许）
- 文献扫描 Worker 完成 → 补 Wang et al. (arXiv 2602.16065) 到扫描结果
- ESS-only 早期 b* 值 5.36/2.95 已确认 max-intervention 行为，但最终 PPL 才是判断依据

### 5. 🎯 战略上下文
**核心 story**：Dual-constrained adaptive b*（α_eff 质量下界 + ESS 稳定上界 → 最小干预准则），替代 Drayson 的 per-model grid search。

**决策链**：D019(MVP PASS) → D020/D021(Dream 暴露 α_eff 问题) → D022(过度修正) → D023(恢复 dual-constraint) → D024(GPU 预算) → D025(τ 理论降级为 empirical HP) → D026(checkpoint artifact 不重跑) → D027(grid_b_low 降优先级，τ sweep 提前)

**最容易判断错的事**：
1. **ESS-only 结果解读**——不要因为 ESS-only PPL 接近 adaptive 就立刻 panic。paper_framing.md Key Risk #1 有三级应对方案，"dual ≈ ESS-only" 仍可接受（reframe 为 dual 不劣于 + 有理论 motivation）
2. **α_eff 不是 decorative**——D021 曾错误结论 α_eff 退化为 ESS 阈值化，D023 已修正。关键区分：inf{b} (min-intervention) vs max{b} (max-intervention)，40% reweighted batch 中 α_eff 是 binding constraint。Q1 分析在 artifacts/q1_ess_equivalence_analysis.md
3. **τ 的理论来源**——arXiv 2602.16065 的 α 是已知比例，不能声称 proportion-free 理论推导。τ 定位为 "empirical HP with theoretical motivation"（D025）。τ sweep 是唯一直接实证支撑
4. **aggregation 口径**——论文用 ratio of means (89.9%) 而非 mean of ratios (91.0%)
5. **GPU 预算**：剩余 ~65h，P0 还需 ~40h，余量 ~25h。够用但不能浪费


---
