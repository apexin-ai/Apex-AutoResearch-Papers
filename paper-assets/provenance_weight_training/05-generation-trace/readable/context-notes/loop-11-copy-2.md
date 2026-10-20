# agent / loop_11.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_11.md`
- **Structured JSON:** [`468c52d5691b1243fd81.json`](../../sessions/46/468c52d5691b1243fd81.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: idle_timeout
updated: '2026-05-16T01:10:53+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单仅 `cuda:0/1/2/3`（westd-47453），绝不用白名单外 GPU
- GPU 预算极度紧张：已消耗 ~154h，剩余 ~26h，contamination_60 完成后仅 ~15h
- **禁止 `WANDB_MODE=disabled`**——已导致 cron 误判 contamination_60_uniform_seed42 为 failed（实际完成），详见 memory.md 失败模式
- contamination_60_ess_only_seed42 在 registry 中 provenance 全空（hypothesis/server/gpu/command 均 null），下一个"你"接手后**必须先补全 spec**
- EMNLP 2026 ARR May 25 截稿，距今 **9 天**

### 2. 🖥️ 基础设施快照
- **服务器**: westd-47453，4× RTX 6000 Pro 96G
- **工作目录**: `/root/provenance_weight_training`
- **Python**: `/root/miniconda3/bin/python`，激活命令 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **镜像**: aml-train（跳过基础环境搭建）
- **模型**: `/root/provenance_weight_training/models/Qwen/Qwen3-0.6B`
- **数据**: `data/scored_data.jsonl`（ρ=0.4）、`data/scored_data_60.jsonl`（ρ=0.6）
- **活跃进程**:
  - PID 257977 — contamination_60_seed42_r2（cuda:0，adaptive ρ=0.6）
  - PID 255781 — contamination_60_grid_b0_5_seed42（cuda:3，grid b=0.5 ρ=0.6）
  - PID 265012 — contamination_60_ess_only_seed42（GPU 未知，ESS-only ρ=0.6）
- **Cron**: 3 条活跃，分别监控上述 3 个 PID
- **Worker**: 4 个 running（paper:consistency-audit、diagnose+eval contamination_60_uniform_seed42 ×3）

### 3. 📊 当前状态
- **contamination_60_uniform_seed42** 刚完成（DONE/success，updated 01:05 UTC）。之前因 WANDB_MODE=disabled + EXIT_CODE=129 被 cron 误判 failed，已手动修正为 success。3 个 Worker 正在诊断/评估其结果，尚未回调
- **contamination_60 其余 3 组** 仍在 RUNNING（ETA ~02:00-03:00 UTC）：adaptive(cuda:0)、grid_b0.5(cuda:3)、ess_only(GPU未知)
- **cuda:1** 因 uniform 已完成而空闲，**cuda:2** 也空闲（等 Director 指示）
- **Paper 初稿**: introduction/method/conclusion 草稿已有（artifacts/），experiments section 等 contamination_60 结果
- **7 个 PREPARING 实验**（grid_b0.1/0.2/0.3、detect_remove_baseline、adaptive_v2 ×3）等待 GPU 和 Director 决策

### 4. 📋 待办（条件触发式）
- Worker 回调（diagnose/eval uniform）到达 → 提取 uniform ρ=0.6 的 PPL 指标，更新 registry metrics
- contamination_60_seed42_r2 cron 回调 → 提取 adaptive ρ=0.6 PPL，与 uniform 对比验证 Claim 3
- contamination_60_grid_b0_5_seed42 cron 回调 → 提取 grid ρ=0.6 PPL，对比 adaptive 验证 Claim 2 在高 ρ 下是否成立
- contamination_60_ess_only_seed42 cron 回调 → 提取 ESS-only ρ=0.6 PPL，对比验证 Claim 1 在高 ρ 下
- **contamination_60 四组全部完成** → 汇报 Director Claim 3 结论 + 实验 Table 更新 + experiments section 可写
- cuda:1/cuda:2 空闲 → 根据剩余 GPU 预算和 Director 指示，从 PREPARING 池中选实验（优先级：detect_remove_baseline > grid_b_low > adaptive_v2）
- paper:consistency-audit Worker 回调 → 处理一致性审查结果，修正论文

### 5. 🎯 战略上下文
- **核心框架**: Dual-constraint adaptive b*（D023）— α_eff 质量下界 + ESS 稳定上界 → min-intervention
- **三个 Claims**:
  - Claim 1 (dual > ESS-only): ✅ ρ=0.4 完成，ρ=0.6 验证中
  - Claim 2 (adaptive ≈ grid-best): ✅ ρ=0.4 完成，ρ=0.6 验证中
  - Claim 3 (proportion-free): 🔄 contamination_60 四组结果决定成败
- **关键决策链**: D023(dual框架) → D025(τ经验HP) → D036(τ sweep完成) → D038(paper启动) → D041(grid_b_low暂停) → D042(bs8 negative入limitation)
- **易错点**:
  - contamination_60_ess_only_seed42 没有 provenance，别漏补
  - uniform 已完成但 report.md 可能仍显示旧状态（failed），需刷新
  - GPU 预算 ~15h 不够跑全部 7 个 PREPARING，必须挑最关键的（detect_remove_baseline 对 reviewer 价值最高）
  - bs8_nmin2 是 negative，D042 决策写入 limitation section 而非 drop
  - τ=0.8 是硬选择（D036），不要重新 sweep


---
