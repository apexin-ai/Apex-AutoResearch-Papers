# agent / loop_4.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_4.md`
- **Structured JSON:** [`c039ccb9a87dfa050337.json`](../../sessions/c0/c039ccb9a87dfa050337.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: idle_timeout
updated: '2026-05-16T03:44:56+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单仅 `cuda:0` 和 `cuda:1`（westd-27271），禁止使用其他 GPU
- v8 的 checkpoint 在 `checkpoints/imm_anchor_v8/`（不是 imm_anchor_v8/），v8_1 在 `checkpoints/imm_anchor_v8_1/`——路径由 yaml config 的 run_name 决定，不跟 registry exp_id
- D028 确认 evaluate.py 有 3 处 bug：(1) eps=0 绕过 pruning flag (2) eval 用 train mode+soft mask (3) per-condition RNG 污染 dataloader shuffle。**所有 pruneTrue 条件的历史数据无效**，D026/D027 关于 G3-deploy 的讨论全部作废。修复前不要引用任何 pruneTrue 指标
- G3=1.30x (standard/baseline) 是 v8 当前唯一可信的 G3 数字，它不受 pruneTrue bug 影响

### 2. 🖥️ 基础设施快照
- **服务器**: westd-27271, 2× RTX PRO 6000 96GB
- **工作目录**: `/root/autodl-tmp/importance_margin_vla_compress`
- **Python**: `/root/miniconda3/bin/python`（conda base env，激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- **模型**: lerobot/smolvla_base + LoRA r=32，HF cache 在服务器默认位置
- **数据集**: `lerobot/aloha_sim_insertion_scripted_image` (20K samples)
- **Eval 结果目录**: `/root/autodl-tmp/importance_margin_vla_compress/eval_results/`
- **关键 checkpoint**: `checkpoints/imm_anchor_v8/` (v8 30K), `checkpoints/baseline/step_029999` (baseline)
- **活跃进程**: mvp_imm_anchor_v8_1 RUNNING on cuda:0（刚启动，30K steps）
- **活跃 Worker**: `worker_code_fix-eval-complete-v8` (running) — 修 evaluate.py D028 三处 bug
- **Cron**: reconcile 返回 0 active crons（v8_1 的 cron 可能尚未注册或已被清理）

### 3. 📊 当前状态
**刚做完**: v8 训练完成 (30K steps) + 500-batch eval。发现 evaluate.py 三处 bug (D028)，派了 Worker 修复。同时启动了 v8_1 (λ=0.2) 作为 contingency。

**Registry 关键实验**:
- `mvp_imm_anchor_v8` — **ANALYZING**: 30K 完成。G1=48.2x✅ G2=+47.1pp✅ G3-standard=1.30x❌(需≤1.10) G4=0.169✅。evaluate.py bug 影响 pruneTrue 数据，standard 数据可信。checkpoint trajectory 显示 ACIS+Prune loss 在 20K 时已达 0.0042 (vs baseline 0.00408 = 1.03x)，是核心 claim 证据
- `mvp_imm_anchor_v8_1` — **RUNNING**: λ=0.2 + gradient isolation。目标：降低 ACIS selection overhead 使 G3-standard ≤ 1.10
- `mvp_baseline_v5` — **DONE (success)**: clean=0.004077，500-batch eval 可信

**等待中**:
- Worker `fix-eval-complete-v8` 回调 → 修复 evaluate.py 后需重跑 v8 pruneTrue eval
- v8_1 训练完成回调（约 2-3 小时）→ 需 500-batch eval
- 无 Director 待决策项（D028 bug 修复是执行层自行处理）

### 4. 📋 待办（条件触发式）
- Worker `fix-eval-complete-v8` 完成 → 用修复后的 evaluate.py 重跑 v8 500-batch eval（含 pruneTrue 条件）→ 更新 registry metrics → 重新计算 G3-deploy
- v8 重跑 eval 后 G3-deploy ≤ 1.10 → MVP PASS，向 Director 汇报 + 准备论文素材
- v8 重跑 eval 后 G3-deploy > 1.10 → 等 v8_1 结果作为 fallback
- v8_1 cron 回调（训练完成）→ spawn Worker 跑 500-batch eval → gate 判定
- v8_1 G3-standard ≤ 1.10 → MVP PASS（λ=0.2 是更优配置）
- v8 + v8_1 均 G3 FAIL → 需向 Director 提 Framing 调整提案（两个 contingency: v8.2 延长到 50K steps / 架构级修改如 dual-LoRA）

### 5. 🎯 战略上下文
- **核心发现**: IMM 方法的 G1/G2/G4 全线强通过（margin 48-64x, preservation +47pp, LED < 0.35），证明 margin maximization → robustness 成立。唯一卡点是 G3（clean performance degradation）
- **v7→v8 的关键突破**: v7/v7.2 的 G3 失败根因是 margin_loss 梯度通过共享 LoRA 损伤 backbone（bypass-ACIS G3a=1.91x 确认）。v8 用 dual detach 隔离梯度后，backbone 不再受损，但 standard 路径仍有 1.30x overhead——这是 ACIS routing 的 distribution mismatch（backbone "依赖" ACIS），不是权重损伤
- **最易判断错的事**: bypass 指标在 v8 (gradient-isolated) 下含义完全不同于 v7。v7 的 bypass 差=权重损伤；v8 的 bypass 差=架构依赖（正常现象）。不要用 v8 bypass ratio 来诊断权重损伤
- **G3 gate 定义历史混乱**: D024→D025→D026→D027→D028，反复修订。当前可信定义：等 evaluate.py 修复后，G3-deploy = ACIS+Prune(50%)/baseline ≤ 1.10 是 MVP 主 gate。v8 @20K 的 ACIS+Prune=0.0042 vs baseline=0.00408 = 1.03x 是最有希望的信号，但需要修复后的 eval 确认
- **论文叙事**: IMM 是压缩方法——部署始终走 ACIS pruning。ACIS+Prune 50% 仍 match baseline 是核心 claim。standard overhead 是 compression-aware coupling 的合理 trade-off，不是缺陷


---
