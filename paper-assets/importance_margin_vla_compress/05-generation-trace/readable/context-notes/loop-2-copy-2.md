# agent / loop_2.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_2.md`
- **Structured JSON:** [`80392f767f511a0bb3e8.json`](../../sessions/80/80392f767f511a0bb3e8.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: idle_timeout
updated: '2026-05-15T21:02:45+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-27271 的 cuda:0 和 cuda:1（gpu_ids 白名单）
- submit_training_job 必须包含 `source /etc/network_turbo 2>/dev/null` + SSL 证书 export（AutoDL 网络要求）
- 所有 Gate 评估数据**必须直接引用 JSON 文件数值+文件名+condition key**，禁止从记忆转述（D014 硬规则，Reviewer 两次打回过）
- conda 环境（不是 venv）：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- `load_vlm_weights=False`——smolvla_base 已含 VLM 权重，不需单独下载 SmolVLM2
- Gate #4 是**绝对阈值** `LED median < 1.0`（D015），不再做 baseline relative comparison

### 2. 🖥️ 基础设施快照
- 服务器：westd-27271（AutoDL），2× RTX PRO 6000 96GB
- 工作目录：`/root/autodl-tmp/importance_margin_vla_compress`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型：`/root/autodl-tmp/.hf_cache/lerobot/smolvla_base`
- 数据集：`lerobot/aloha_sim_insertion_scripted_image`（50 eps, ~20K samples, 14D action, 1 camera）
- Checkpoints：`checkpoints/baseline/step_029999`（baseline）、`checkpoints/imm_anchor/step_029999`（v7）
- 活跃进程：mvp_imm_anchor_v7_2 (PID 54978, cuda:0, tmux session)
- Cron：mvp_imm_anchor_v7_2 监控活跃（reconcile 确认 still running）
- WANDB_MODE=offline（无 API key）

### 3. 📊 当前状态
**刚发生**：mvp_imm_anchor_v7 训练 30K 步完成，状态 ANALYZING，on_complete hook 已触发。Step 20K eval: action_loss=0.0107 (-65% vs 8K), margin_mean=1.074, L_emp=0.266, preservation=1.0@clean。checkpoint 已保存 `step_029999`。

**正在跑**：mvp_imm_anchor_v7_2 (cuda:0) — lambda=0.2, grad_clip=30，metrics.py eval mode leak 修复验证通过（SN 稳定在 1.0-1.01），刚启动不久。

**等待**：
- v7 完成 → 需立即执行 D014 最终 Gate 评估（500 batches eval）
- v7_2 cron 回调（训练中）

### 4. 📋 待办（条件触发式）
- **立即**（v7 已完成）→ spawn Worker 执行 D014 Gate 评估：v7 final eval 500 batches + baseline final eval 500 batches + baseline mid-checkpoint eval (step_005000, step_010000 各 50 batches)
- v7_2 cron 回调到达 → 分析结果，与 v7 对比（lambda=0.2 vs 0.5 效果）
- D014 eval 完成 → 计算 4 个 Gate 条件（G1: margin ≥2x, G2: preservation ≥+10pp, G3: loss ratio ≤1.10, G4: LED median <1.0），向 Director 汇报 PASS/FAIL
- 如果 Gate 全 PASS → 进入下一阶段（多数据集/scale-up）
- 如果部分 FAIL → 产出 Framing 调整提案，等 Director 决策

### 5. 🎯 战略上下文
**核心方向**：Importance Margin Maximization (IMM) — 通过最大化 VLA visual token 的 importance margin Δ_k，使 token compression 在对抗扰动下保持 top-k 选择稳定性。

**关键发现链**：
- Baseline 50% random pruning 反而降低 loss（-27%），说明约半数 token 是噪声
- IMM v7 训练健康：margin 从 0 涨到 1.074，Lipschitz 从 0.6 自修复到 0.266
- lambda=0.5 太激进（D013 Lipschitz 爆炸风波），v7 靠 eval disabled 绕过，v7_2 用 lambda=0.2 + 修复后的 metrics.py 重跑
- Spectral norm ≠ empirical Lipschitz（SN 恒定 ~1.067 但 L_emp 可爆到 0.6），必须双轨监控

**易踩的坑**：
- 不要用 v7 的 step 20K eval（只有 10 batches）做 Gate 判定——方差太大，必须 500 batches
- Baseline eval 数据被 D011 修复过（baseline_forward sig 变了），旧数据作废，必须重跑
- `pruneTrue` 在 baseline 上的反直觉结果不是 bug——是 random pruning 恰好移除噪声 token
- compute_empirical_lipschitz() 必须保存/恢复 training mode（v7.1 的死因）


---
