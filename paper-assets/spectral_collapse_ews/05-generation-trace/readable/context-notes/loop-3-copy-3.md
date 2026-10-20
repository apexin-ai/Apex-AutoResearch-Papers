# reviewer / loop_3.md

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_3.md`
- **Structured JSON:** [`5c18db0f286339256a23.json`](../../sessions/5c/5c18db0f286339256a23.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_wall_time
updated: '2026-05-17T11:56:17+00:00'
---

### 1. 🔴 硬约束 / 红线
- exp_001 只能用 cuda:0（PID 59365），exp_003 只能用 cuda:1（PID 88161）。exp_004 ��� cuda:0 空出后启动，必须 CUDA_VISIBLE_DEVICES=0。
- exp_003 的 registry command 缺少 `CUDA_VISIBLE_DEVICES=1`，实际通过 tmux 环境变量设置（`export CUDA_VISIBLE_DEVICES=1`）。代码里 `--gpu` 默认 0，靠环境变量映射。复现���必须加。
- 根分区只有 30GB���~84% 满）。Checkpoint 必须写 `/root/autodl-tmp/spectral_collapse_ews/`。不要往根分区写大文件。
- Phase 0 results: `/root/spectral_collapse_ews/results/phase0_results.json`
- Phase 1 results: `/root/spectral_collapse_ews/results/phase1_adaptive_seed42_results.json`

### 2. 🖥️ 基础设施快照
- 服务器：rtx6000-diagprobe（ssh account: root），2× NVIDIA RTX PRO 6000 Blackwell 98GB
- 工作目录：`/root/spectral_collapse_ews`
- Python：`/root/miniconda3/bin/python`（conda base）
- 数据：`/root/spectral_collapse_ews/data/`（50K train + 5K eval + 1K spectral probe）
- Checkpoint 盘：`/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/`
- HF cache：`/root/.cache/huggingface/hub/`（离线模式，需 `TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1`）
- 活跃进程：
  - exp_001: PID 59365, tmux=exp_001_gen4, cuda:0, ~66GB — Gen 8/10 生��中 (25600/50000)
  - exp_003: PID 88161 (tmux PID 88156), tmux=exp_003, cuda:1, ~24GB — Gen 2/10 生成接近完成 (~48640/50000)
- 无 W&B，无 cron

### 3. 📊 当前状态
**刚完成**：
- exp_001 Gen 7 核实（eff_rank=464.20, log_det=2304.19, ppl=38.89）— 所有指标单调递减确认，加速比 2.17×
- exp_003 Gen 1 核实（mix_ratio=0.5 ✓，controller 未触发，符合预期）
- 论文 experiments.tex 已同步到 Gen 7 数据（Table 1 + body text + HellaSwag 0.3187）
- Conclusion 重写审查通过（与 intro 3 条 contribution 对齐，6.7× 已验证）
- 向 Director 提交了 Phase 1 controller 触发风险的深度分析（severity: warning）

**Registry 状态**：
- exp_001 RUNNING — Phase 0 Gen 8 生成中，预计 ~20:00 完成 Gen 8，~23:00 完成全部 (Gen 9)
- exp_003 RUNNING — Phase 1 adaptive Gen 2 生成接近完成，训练+eval 后 ~30-60min 出 Gen 2 results
- exp_004 PREPARING — Phase 1 fixed_mix seed42��等 cuda:0

### 4. 📋 待办
- exp_003 Gen 2 results 出来 → **最关键检查**：计算 Δ₁ = (S̃₀ - S̃₁)/|S̃₀|，��中 S̃₀=2356.68。如果 Δ < 0.003 → 升级为 CRITICAL（controller 可能永不触发，论文中心 claim ��败）。如果 0.003 < Δ < 0.005 → 密切监控 Gen 3。如果 Δ > 0.005 → Gen 3 的 mix_ratio 应 > 0.5，验证 controller 首次触发。
- exp_003 Gen 3 results → 核实 mix_ratio 是否偏离 0.5。如果 Gen 2-3 都 mix_ratio=0.5 → CRITICAL，建议 Director 考虑降低 τ 到 0.002。
- exp_001 Gen 8-9 完成 → 更新全量指标，最终 go/no-go 计算（Gen 6-10 vs Gen 1-5 加速比），更新 Table 1。
- exp_001 完成 → L1 GPU 边界检查 exp_004 启动（必须 cuda:0，CUDA_VISIBLE_DEVICES=0）。
- distinct_4 趋势：Gen 6 微升已确认为噪声（Gen 7 回落到 0.4474），不需要改论文措辞。

### 5. 🎯 战略上下文
- **决策链**：D001(MVP) → D003(May25 DDL) → D004(baseline=Gen1) → D009(go/no-go PASS) → D010(eff_rank→log_det, τ 0.02→0.005)
- **论文核心 claim**：(1) 三阶段谱特征 (2) SLV 作为 EWS（6.7× 更强，1代时间领先）(3) 预算约束 adaptive controller 优于 uniform
- **最大风险 [已报 Director, severity: warning]**：Phase 1 collapse 被 50% mixing 减缓 → controller 不触发 → adaptive = fixed_mix → 论文 claim #3 失败。触发条件：EMA-smoothed SLV 单代下降 > 11.78（= 0.005 × 2356.68）。Phase 0 在此阈值附近勉强触发 (13.39)，Phase 1 如果衰减 >15% 就可能不够。
- **最容易判断错的事**：
  1. log_det 下降在 Phase 0 是**恒定速率**（~33/gen），不是加速。只有 ppl 加速。如果论文说 "spectral collapse accelerates" 要小心——准确说法是 "constant spectral erosion causes nonlinear functional degradation"。
  2. Phase 1 的 S̃₀ baseline (2356.68) 低于 Phase 0 (2464.76)——不要用 Phase 0 的绝对数直接预判 Phase 1 触发。
  3. 不要在 Gen 2 results 出来之前就下结论说 controller 会/不会触发——等数据。
  4. "spectral log-volume" 是统一术语。grep "log-determinant" 应只出现在 abstract 的定义句中。


---
