# reviewer / loop_10.md

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_10.md`
- **Structured JSON:** [`04b723548075bf9c0850.json`](../../sessions/04/04b723548075bf9c0850.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_wall_time
updated: '2026-05-24T01:59:17+00:00'
---

### 1. 🔴 硬约束 / 红线
- exp_019 在 cuda:1，exp_020 在 cuda:0（rtx6000-diagprobe）。exp_021 脚本指定 --gpu 0，**必须等 exp_020 完成后才能启动**，否则 OOM
- Table 2 caption 的 Rel Δ 公式对 SLV/RankMe 不准确：实际用 peak→Gen10，而非 Gen0→Gen10。已报 Director 但尚未修复
- r=0.25 seed43 SLV 数据在 gen_fig5.py 中 Gen 3-9 是**线性插值**（只有 Gen 0,1,2,10 是真实值）。影响 Figure 4 controller signal 和 Figure 6 phase diagram 的 r=0.25 均值轨迹

### 2. 🖥️ 基础设施快照
- **服务器**: rtx6000-diagprobe (root)，2× RTX PRO 6000 96GB
- **工作目录**: /root/spectral_collapse_ews
- **Python**: /root/miniconda3/bin/python（conda base）
- **本地 workspace**: /home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/
- **论文真源**: 本地 workspace `paper/sections/*.tex`（远程 .tex 是旧版，不可信）
- **结果文件**: /root/spectral_collapse_ews/results/phase1_*.json
- **活跃进程**: exp_019 (cuda:1, tmux=exp_019, r=0.2 seed44), exp_020 (cuda:0, tmux=exp_020, GPT-2-medium r=0)
- **待启动**: exp_021 脚本就绪 (`run_gpt2m_realdata_control.py`)，等 Director 批准 + exp_020 完成

### 3. 📊 当前状态
刚完成：response letter 全文质量审查（4 维度 × 20 条回复）、data audit 修复验证（全部 PASS）、exp_020 Gen 0-4 三阶段确认、exp_021 实验设计审查。

**RUNNING 实验**:
- exp_019: r=0.2 seed44, Gen 8/10。完成后 r=0.2 升至 3-seed，需更新 Table 2 r=0.2 行 + Figure 6 + Figure 4 + inline text
- exp_020: GPT-2-medium r=0, Gen 4/10。三阶段已全部可见（Gen 2 peak, Gen 3 onset, Gen 4 acceleration）

**等待中**: Director 对 response letter 审查报告的回应；exp_021 启动批准

### 4. 📋 待办
- exp_019 完成 → 验证 Gen 10 SLV/r_eff/PPL/D-4，计算 3-seed 均值，确认 Type II 分类。检查 D-4 pattern（seed42 recovers, seed43+44 decline → 2/3 majority decline）
- exp_020 完成 → 验证 10 代完整轨迹。确认 Phase III acceleration 持续到 Gen 10。与 Pythia 对比 per-gen SLV 下降率
- exp_021 完成 → **关键对照**：若 Gen 2 无 peak → decompression 是 synthetic-specific（加强 claim）；若 Gen 2 也 peak → fine-tuning artifact（需在 Limitations 承认）
- r=0.2 数据更新后 → 重验 Table 2 maxΔ_t for r=0.2（当前 .0017 基于 2-seed，3-seed 可能变化）
- 论文 Table 2 caption Rel Δ 公式修复 → 验证 "(for peaked indicators, computed as peak→Gen10)" 已添加

### 5. 🎯 战略上下文
- **核心结论**: Pythia-410M 在 r=0 下展现三阶段频谱坍缩（解压→onset→加速），r_crit ∈ (0.25, 0.3]。GPT-2-medium 定性复现同一模式但幅度差 8×。SLV 提供 3-type 分类（vs RankMe 只有 2-type），但 Phase I misleading（SLV↑ 同时 PPL↑）限制了实时监控用途
- **最容易判断错的事**: (1) 不要把远程服务器的 .tex 文件当论文真源——本地 workspace 是最新版；(2) r=0.2 在 Table 2 当前是 2-seed 均值（seeds 42+43），exp_019 完成后变 3-seed，所有引用 r=0.2 数据的地方都需要更新；(3) GPT-2-medium 的 r_eff baseline=23 与 Pythia=418 差 18×，不要写 "same magnitude" 或 "quantitatively consistent"；(4) Figure 5 (ews_heatmap) 的 Appendix Table 用 seed42-only 数据，不是 3-seed 均值——和 Table 1 不同
- **DDL**: EMNLP 2026 ARR，投稿日 2026-05-25（明天）


---
