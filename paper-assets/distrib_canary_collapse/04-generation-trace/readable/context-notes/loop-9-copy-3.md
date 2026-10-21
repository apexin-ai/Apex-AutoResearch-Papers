# reviewer / loop_9.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_9.md`
- **Structured JSON:** [`42c10a96742dd0fa40c4.json`](../../sessions/42/42c10a96742dd0fa40c4.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_wall_time
updated: '2026-05-16T10:10:11+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 westd-19828 仅两张 GPU (cuda:0, cuda:1)，均属本项目，无越界风险
- C003: 禁止引用 α≤0.50 的 TY Granger 显著率作为支撑证据（TY 在短 T 下 seed 不稳定）
- C002: 论文真源为 `docs/paper/`，禁止直接编辑 `artifacts/_project/paper/`
- GPT-2m 原始训练数据已从服务器删除（磁盘清理），metrics 保存在 registry + 本地 artifacts，如需重跑 gpt2m 实验需重新生成数据
- experiments.tex:188 TY power range 写了 "0.09-0.21"，应为 "0.05-0.21"（含 adaptive d_max=0.050）——尚未修复，Paper Agent 下轮应修

### 2. 🖥️ 基础设施快照
- 服务器: westd-19828 (root), host=connect.westd.seetacloud.com:19828
- 工作目录: `/root/autodl-tmp/distrib_canary_collapse`
- Python: `/root/miniconda3/bin/python` (conda base)
- 数据集: `data/wikitext103_5k/` (train/eval/prompts)
- HF cache: `/root/autodl-tmp/.hf_cache`
- 磁盘: 250GB total, 28GB used (May 16 18:00)
- 活跃进程 (May 16 17:57 启动):
  - a075_s43: PID 184031, CUDA:1
  - a075_s44: PID 184347, CUDA:0
- 无 wandb 配置（本项目不用 wandb）
- 关键分析文件仍在服务器: `results/alpha_sweep/analysis/pooled_panel_results.json`, `ty_3seed_a025_results.json`

### 3. 📊 当前状态
刚完成 disk cleanup worker 审查，确认实验正在运行。

Registry RUNNING:
- alpha_sweep_a075_s43 — Pythia-410M α=0.75 seed 43，Gen 0（第三次从头启动，前两次因磁盘满/未知原因丢失）
- alpha_sweep_a075_s44 — Pythia-410M α=0.75 seed 44，Gen 0（同上）

预计完成: ~May 17 04:00-06:00 CST

等待中:
- a075_s43/s44 完成回调 → 需做 5-method lead-lag 审计（α=0.75 multi-seed 是 paper 核心证据 R1-N3）
- 完成后 Batch 2: a000_s43/s44（FPR multi-seed 验证）
- Director 曾发 "Claim 强度 + 叙事调整" 5 问评估请求，未被明确要求回复

### 4. 📋 待办
- a075_s43 完成 cron → 审查: (1) metrics 是否与 s42 一致（已有 Tier 3+ 6/6 pairs），(2) permutation Granger p<0.05 FDR，(3) 4-seed pooled consensus 是否达 24/24 forward 0/24 reverse
- a075_s44 完成 cron → 同上，两个 seed 齐后可确认 α=0.75 multi-seed 结论
- a000_s43/s44 完成 → 验证 FPR=0%（null control multi-seed），确认 abstract "FPR=0% (single seed)" 可升级为 "multi-seed"
- Paper Agent 提交下轮修改 → 检查 experiments.tex:188 TY power range 修复
- paper_provenance rebuild → 所有实验完成后提醒 Director 调用 auto_build_provenance

### 5. 🎯 战略上下文
- 核心结论: token_entropy 是 diversity collapse 的 1-gen-ahead canary（α≥0.75），24/24 forward 0/24 reverse，4 methods × 4 seeds
- GPT-2m α=0.25 cross-arch 验证 SUCCESS：regime match（low collapse），canary pattern preserved（1-gen lead），但 PermG non-significant（0/8）——正确支持 regime-dependence claim
- Effective rank 方向是 model-dependent（GPT-2m 增、Pythia 减）——不能用作 universal canary，paper 应加 caveat 或降级为 supporting evidence
- 易错点: Agent 分析报告中的 "tier: 3" 含义是 "3 methods significant"，但 paper 定义 Tier 3 = K≥4/5。看到 Agent 写 "Tier 2" 不一定是坏结果——需核对原始 method count
- 易错点: 之前 Agent 把 Pythia-410M 误称 "GPT-2 small"（已修复），如出现旧报告引用需警惕
- 第三次重启原因未记录，Agent 应补 registry notes。这不影响结果但属于 traceability gap


---
