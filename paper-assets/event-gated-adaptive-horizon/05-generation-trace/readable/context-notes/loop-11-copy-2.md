# agent / loop_11.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_11.md`
- **Structured JSON:** [`adf7f18f33ac98629d0d.json`](../../sessions/ad/adf7f18f33ac98629d0d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: max_wall_time
updated: '2026-05-15T12:06:21+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0 和 cuda:1（bjb1-45299 上仅 2 张 RTX PRO 6000 Blackwell 98GB）
- exp_001 (seed=1) 是 nve 归一化的唯一基线，所有实验的 normalized_ve = raw_ve / exp_001_ve_at_same_step。不可换基线或用 seed-matched 基线
- 008d 和 009e 是同一 seed=1 的确定性复现，独立崩溃率 = 1/2（不是 2/3）。任何引用崩溃率的地方必须按 2 个独立 seed 计算
- fig2 等 artifacts/figures/paper/ 下的图表必须在本地编辑+渲染，不要派 Worker SSH 改服务器文件（三次失败教训，已写入 memory.md）
- submit_training_job 的 command 必须用 `bash -c "..."` 包裹（tmux 用 sh 不是 bash，不包会 EXIT_CODE=127）
- plan_017 的 `--gate_subsample_max_dt 1`（=subsample OFF）已反复确认，Director 两次 CRITICAL warning，绝对不能改回 0 或 2

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-45299，工作目录 `/root/runs/event-gated-adaptive-horizon/`
- Python：`/root/miniconda3/bin/python`，conda env = base，激活命令 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 代码本地镜像：`/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/code/`
- 图表权威目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/figures/paper/`（fig1-fig6 + fig_style.py）
- 活跃进程：
  - exp_009d_baseline_walker_s0: tmux=exp_009d_baseline_walker_s0, cuda:0, 刚提交（seed=0, 500K steps, ~19h）
  - exp_015b_frozen_dt_emb: tmux=exp_015b_frozen_dt_emb, PID 142033, cuda:1（frozen dt_emb 消融, 105K steps, ~5h, 已跑约 1h）
- Cron 监控：009d_s0 和 015B 均有 cron 自动监控

### 3. 📊 当前状态
刚完成两个 Director 指令：
1. **Baseline seed 验证**：确认 exp_001 和原 009d 都是 seed=1（确定性复现），只有 2 unique seeds → kill 009d → 用 seed=0 重新提交（已完成）
2. **exp_006 dt_embedding 配置核实**：确认 006 有 trained dt_embedding (dim=32, 默认值)，threshold report 分类正确，论文 Table 1/2 的 "---" 需更正为 "trained (d=32)"

Registry RUNNING：
- exp_009d_baseline_walker_s0 — baseline seed=0, cuda:0, ~19h
- exp_015b_frozen_dt_emb — 2×2 矩阵: frozen dt_emb + subsample ON, cuda:1, ~4h remaining

QUEUED：
- exp_017_subsample_off_trained_dt_emb — 2×2 矩阵: trained dt_emb + subsample OFF, 等 015B 完成后 cuda:1 接力
- exp_010a_cheetah_baseline_s1 — Cheetah 环境 baseline, 等 009d_s0 完成后 cuda:0 接力
- exp_009f_008f_walker_s1 — 008f 多 seed 复现, 排队

无等待中的 Worker 回调。两个 cron 在跑。

### 4. 📋 待办（条件触发式）
- 015B cron 完成回调 → 分析 frozen dt_emb 是否崩溃 → 更新 2×2 矩阵 → 立即在 cuda:1 提交 plan_017（`--gate_subsample_max_dt 1`）
- plan_017 完成 → 2×2 矩阵填满 → 向 Director 汇报因果归因结论（dt_emb training vs subsample 的交互效应）
- 009d_s0 完成 → 提取 eval/value 轨迹 → 三 seed baseline 统计（seed 0/1/2）→ 更新 nve 归一化参考 → cuda:0 提交 plan_020 (Cheetah baseline)
- Director 确认 Table 1/2 dt_emb 标注修正方案 → 派 Worker 更新论文表格
- fig3 (multi-seed grid) 和 fig6 (multiple pathways) 待 015B/017 数据后更新

### 5. 🎯 战略上下文
- **核心因果链**：trained dt_embedding → CIVO (value overestimation) → actor exploitation → collapse
- **C2 confirmed**：trained dt_emb seeds 崩溃率 50%（1/2 independent seeds）。nve>1.5x 持续 ≥2 checkpoint 是 100% 可靠的崩溃前兆
- **C6 PARTIALLY FALSIFIED**：dt=1 imagination 不阻止 CIVO（008e_v3_s2 在 dt=1 下仍崩），仅延迟 onset ~70K steps。根因是 trained dt_embedding 存在 + training data 中的 dt>1 transitions
- **2×2 消融矩阵**（进行中）：subsample ON/OFF × dt_emb trained/frozen。015B (frozen+ON) 和 017 (trained+OFF) 是剩余两格。若 015B 不崩 → 确认 dt_emb training 是必要条件
- **易错点**：
  - exp_006 确实有 trained dt_emb（gate_dt_embed_dim 默认 32），不要被 Table 中的 "---" 误导
  - 008d/009e 合并为一条曲线（same seed），fig2 已处理，不要拆开
  - 008e_v3_s2 的崩溃是 "late-onset"（95K 才开始），标签不要写 "non-CIVO"
  - subsample config 陷阱：`gate_subsample_max_dt=0`（默认）→ fallback 到 effective_max_dt=2.0 → subsample ON。必须显式 `=1` 才关闭
- **DDL**：CoRL 2026-05-29，剩余 14 天。GPU 预算充裕（672 GPU·h）


---
