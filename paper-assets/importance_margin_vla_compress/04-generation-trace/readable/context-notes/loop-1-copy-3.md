# reviewer / loop_1.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`765dea88a3f0ba982da1.json`](../../sessions/76/765dea88a3f0ba982da1.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-15T17:45:27+00:00'
---

### 1. 🔴 硬约束 / 红线
- baseline 只能用 cuda:0，IMM 只能用 cuda:1。registry spec 里的 gpu 字段是真源。
- 服务器 westd-27271 是 AutoDL 实例，SSH 命令必须包含 `source /etc/network_turbo`、`REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt`、`SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`、`HF_HUB_DISABLE_XET=1`，否则 pip/HF 全部超时或 SSL 错误。
- `HF_HOME=/root/autodl-tmp/.hf_cache`，不能用默认路径（根分区只有 30GB）。
- train.py 中 baseline 用 `baseline_forward()`（绕过 SmolVLAPolicy.forward 的 action_is_pad bug），不要动这个函数。
- imm_anchor.yaml 当前 `eval_every: 999999`（D008 workaround），这是故意的——训练中 eval 会触发 RoPE crash。evaluate.py 做事后评估。

### 2. 🖥️ 基础设施快照
- 服务器：westd-27271 (root)，2× RTX PRO 6000 Blackwell 96GB，CUDA 13.0
- 工作目录：`/root/autodl-tmp/importance_margin_vla_compress`
- Python：`/root/miniconda3/bin/python3`（conda base 环境，不要创建 venv）
- 模型：`lerobot/smolvla_base`（本地 checkpoint 906MB，`load_vlm_weights=False`）
- 数据集：`lerobot/aloha_sim_insertion_scripted_image`（50 eps, 20000 samples, 14D, 1 cam → 64 tokens）
- Baseline checkpoints：`checkpoints/baseline/step_{005000,010000,015000,020000,025000,029999}/checkpoint.pt`（各 1.2GB）
- IMM checkpoints：尚无（v7 save_every=2000，第一个在 step 2000 出现）
- wandb：offline mode，日志在 `wandb/offline-run-*`
- 活跃进程：mvp_imm_anchor_v7 PID 41292, cuda:1, tmux session

### 3. 📊 当前状态
**刚完成**：审查了 evaluate.py 5 个维度（2 critical + 3 warning）、3 个 code bug fix 验证（squeeze/stochastic/baseline forward）、RoPE prefix 长度 mismatch 根因分析、_hard_forward binary mask fix 验证。所有 fix 已部署到服务器并验证。

**实验状态**：
- `mvp_baseline_v5`：ANALYZING（30K steps 完成，eval action_loss 0.029→0.003 收敛，最终 ~0.002）
- `mvp_imm_anchor_v7`：RUNNING cuda:1, step ~1050/30000, sps=3.2, 预计 ~04:12 UTC 完成
- v5/v6 IMM：DONE/failed（squeeze bug / RoPE crash，各在 step 2000 eval 崩溃）

**等待中**：IMM v7 训练完成 → 触发 evaluate.py MVP gate 评估

### 4. 📋 待办
- IMM v7 完成（~04:12 UTC）→ 审查训练曲线（loss 收敛、无 gradient collapse）→ 确认 checkpoint 已保存
- evaluate.py 跑 IMM checkpoint → 审查 4 个 Gate Criteria：Δ_k ≥2x, top-k pres ≥10pp, action_loss ratio ≤1.10, L·ε·k/Δ_k ↓≥30%
- evaluate.py 跑 baseline step_029999 → 作为对照基线
- Gate 全 PASS → 审查是否足以支撑 research 阶段推进
- Gate 有 FAIL → 审查 Kill Path（δ/λ 网格搜索）合理性
- 如 Director 转发章节审查 → 按 5.1-5.3 维度审（claim 可信度、叙事逻辑、攻击面 + 评分模板）

### 5. 🎯 战略上下文
- 项目处于 MVP 验证阶段。核心问题：IMM 训练是否能显著增大 Δ_k margin 且不大幅降低 action quality。
- 决策链：D001(MVP 方案) → D002(采纳 Reviewer warning) → D003(L·ε·k/Δ_k 量化) → D005(数据集换 aloha) → D007(Gate#3 放宽到 10%) → D008(跳过训练中 eval)
- **最容易判断错的事**：`_hard_forward` binary mask fix 让 eval 时零值 token 仍在序列中参与 attention。这不是真正的物理 pruning——zeroed token 仍占 attention position。如果 Gate Criteria 结果很边缘，这个近似可能有影响，需要在审查中标注。
- **容易踩的坑**：(1) evaluate.py baseline 模式下所有 (eps, pruning) 条件都只是不同 batch 的 baseline_forward，数值差异是 batch 方差不是扰动效应。(2) `l_eps_delta_ratio` 和 `certified_bound` 公式含 k 因子（L·ε·k/Δ_k），ROADMAP 已同步但 D003 文本仍写"L·ε/Δ_k"。(3) `compute_importance_scores` 用 flow matching noise/time 采样——clean vs perturbed 必须共享同一 noise/time（已修复，但要确认服务器版本）。


---
