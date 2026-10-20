# agent / loop_6.md

**collapse aware mixing** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_6.md`
- **Structured JSON:** [`5e58347cf6b0a21312fc.json`](../../sessions/5e/5e58347cf6b0a21312fc.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: idle_timeout
updated: '2026-05-14T09:13:23+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 `cuda:0`（gpu_ids 白名单），服务器 `cqa1-38874`
- MVP 已判定 FAIL（D018），**三条路径全封**——不要尝试新的 eff_rank 方向，不要启动 PI 控制器实验
- 当前状态是**等待 Director/用户决策**（Q2 negative result paper 或 archive），决策前不动 paper、不开新实验方向
- mvp_seed0_replication_r2 正在跑（seed=0 robustness），这是唯一例外——它是为 Q2 论文补数据，不算新方向
- 合成数据生成命令必须包含 `source /etc/network_turbo` + SSL 证书环境变量 + `HF_HUB_DISABLE_XET=1`，否则 HF 不可达
- submit 命令必须显式 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，tmux 不继承环境

### 2. 🖥️ 基础设施快照
- **服务器**: cqa1-38874，1× RTX PRO 6000 96GB
- **工作目录**: `/root/collapse-aware-mixing/`
- **Python**: `/root/miniconda3/bin/python`（conda base 环境，Python 3.12, PyTorch 2.10.0, transformers 4.57.6）
- **输出目录**: `/root/autodl-tmp/output_v7/`（v7 主实验数据，含 G0/G1/G2 全部 18 checkpoints + pivot 分析结果）
- **HF cache**: `/root/autodl-tmp/.hf_cache`
- **磁盘**: 根分区 ~30GB（紧张），大文件必须写 `/root/autodl-tmp/`。上次 seed0 实验因磁盘不足（仅 7GB 剩余）失败过
- **活跃进程**: mvp_seed0_replication_r2, PID 122208, tmux session, cuda:0, cron 监控中
- **env_init.sh**: `/root/collapse-aware-mixing/env_init.sh` 集中了所有环境变量，launch script 只需 `source env_init.sh`
- **关键分析产出**: `/root/autodl-tmp/output_v7/pivot_b_analysis_full/`（18 checkpoint 全量对比）, `/root/autodl-tmp/output_v7/pivot_analysis/`（初步 3-checkpoint 对比）

### 3. 📊 当前状态
**刚做完**: D018 MVP 最终判定 FAIL。三条路径验证结果：
- C1 holdout eff_rank: **FALSIFIED** — collapse 时 eff_rank 反向上升 +0.96%（676.96→683.44），与 collapse 完全解耦
- Pivot B generated eff_rank: **NO ADVANTAGE** — 与 n-gram entropy 同时在 G1 step 152 检测到 collapse，噪声高 573 倍
- Direction C per-layer: **DEAD** — 所有层变化 <1%

**正在跑**: `mvp_seed0_replication_r2` (RUNNING, PID 122208, cron 监控中) — seed=0 对照组，验证 holdout eff_rank 上升现象是否 seed-robust。这是 Q2 negative result paper 的前置数据。上次 r1 因磁盘空间不足失败，r2 已清理磁盘重新提交。

**等待中**:
- mvp_seed0_replication_r2 的 cron 回调（预计 ~15h 完成 3 代迭代）
- **Director/用户决策**: Q2 (negative result paper → EMNLP 2026 Findings) 或 archive

**Worker 池**: 0 个运行中（当前无可并行的 CPU 任务，且等待 Director 决策中）

### 4. 📋 待办（条件触发式）
- **mvp_seed0_replication_r2 cron 回调到达** → spawn worker 分析 seed=0 数据，对比 v7(seed=42) 的 eff_rank 趋势，更新 registry + report.md，向 Director 汇报 seed robustness 结果
- **Director 选择 Q2 (negative result paper)** → 需补实验：multi-scale (Pythia-410M + Pythia-2.8B) + multi-seed (至少 3 seeds)，预计 ~3-4 天 GPU。先 spawn worker 写实验计划 + 代码适配不同模型规模，再提交审批
- **Director 选择 archive** → 释放 cqa1-38874 GPU，清理产出，关闭项目
- **seed0 结果与 v7 不一致（eff_rank 没上升）** → 这会削弱 Q2 论文的核心发现，需向 Director 汇报并重新评估 Q2 可行性
- **磁盘空间再次不足** → `rm -rf /root/autodl-tmp/output/`（v5 旧数据）释放空间，v7 数据在 output_v7/ 不受影响

### 5. 🎯 战略上下文
**核心结论链**: D001(MVP 方案) → D003(切 wikitext) → D005(降 LR) → D007(降至 20M tokens) → D011(G1 eff_rank 反向上升) → D014(C1 falsified) → D016(Pivot B GO→被 D018 推翻) → **D018(MVP FAIL, 三条路径全封)**

**项目有价值的发现**（Q2 论文潜在核心贡献）:
- "Holdout spectral effective rank rises during mode collapse" — 挑战 SIGMA 等工作的隐含假设
- 问题不是 eff_rank vs PPL，而是 **generation-side vs ALL holdout-side metrics** 的观测面差异

**最容易判断错的事**:
1. **不要试图救 eff_rank 作为控制信号** — 三条路径已穷尽验证，573 倍噪声差距无法靠参数调优弥补
2. **D016 的 "GO" 是误判** — 当时只用了 3 个 checkpoint 做对比（G0/G1/G2 final），全 18 checkpoint 数据推翻了这个结论。不要引用 D016 作为 Pivot B 可行的依据
3. **seed0 实验不是新方向** — 它是为 Q2 论文补 robustness 数据，不需要 Director 额外审批
4. **磁盘是反复杀实验的隐患** — /root/autodl-tmp/ 空间紧张，每次提交前 `df -h` 确认
5. **compare_eff_rank_vs_ngram.py 的阈值不对称** — memory.md 有详细记录，如果要引用其 verdict 必须先统一阈值


---
