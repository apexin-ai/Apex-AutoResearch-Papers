# reviewer / loop_1.md

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`817af0aa79c7f9743870.json`](../../sessions/81/817af0aa79c7f9743870.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-21T02:01:51+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-35807 GPU 白名单：cuda:0, cuda:1, cuda:2, cuda:3（4 卡全部属于本项目）
- westd-45947 GPU 白名单：cuda:0, cuda:1（2 卡全部属于本项目）
- A1 脚本 train_a1_sdf_aux.py 内部会覆盖 CUDA_VISIBLE_DEVICES（M013 教训），启动前必须确认实际用的卡号
- A1 Phase 2 LoRA 解冻曾从未生效（M014），需 lora_utils.py 统一后才能启动 A1 实验——westd-45947 上 lora_utils.py 尚未同步
- Checkpoint 必须设 SAVE_TOTAL_LIMIT=2 + save_interval=2000，否则爆盘（M008 教训）

### 2. 🖥️ 基础设施快照
- **westd-35807**: 4× RTX PRO 6000 96GB, `/root/colliforce-vla/`, conda base (`/root/miniconda3/bin/python`)
- **westd-45947**: 2× RTX PRO 6000 96GB, `/root/colliforce-vla/`, conda base
- 训练输出：`/root/autodl-tmp/colliforce-outputs/`（两台服务器均同路径）
- 训练脚本：`/root/colliforce-vla/scripts/train_a3_hook.py`（A3）、`train_a1_sdf_aux.py`（A1）
- Eval pipeline：`eval_batch.sh` + `sweep_lambda.sh` 已 dry run 通过
- 论文草稿：本地 `artifacts/drafts/` 下 introduction.tex / method.tex / related_work.tex
- 文献库：`literature_map.yaml`（19 篇已验证）
- 无 W&B 配置（不检查 W&B）

### 3. 📊 当前状态
**刚完成**：跨章节（Intro + Method + Related Work）一致性审查 + 叙事弹性推演，已 post 给 Director。

**核心发现**：
- Notation 不一致：Intro/RW 用 ∇_z Φ，Method 用 ∇_z Φ̂（warning）
- AEGIS 77.85% 数字需核实出处（warning）
- 12 个 3D VLA citation keys 未 bib 确认（warning）
- LoRA vs Full-FT 容量 confound 是审稿人必问攻击面，当前无 ColliForce-Full-FT 实验（warning）

**RUNNING 实验（截至 handoff 时）**：
| 实验 | 服务器/GPU | 进度 | ETA |
|------|-----------|------|-----|
| baseline_fullft_spatial_bowl_s0 | 35807/cuda:0 | ~66% | ~8h（可能已完成） |
| baseline_fullft_object_pudding_s0 | 35807/cuda:2 | ~72% | ~8h（可能已完成） |
| baseline_lora_spatial_bowl_s0 | 35807/cuda:1 | ~2% | ~30h |
| baseline_lora_object_pudding_s0 | 35807/cuda:3 | ~2% | ~30h |
| a3_gradient_spatial_bowl_s0 | 45947/cuda:0 | ~37% | ~21h |
| a3_gradient_object_pudding_s0 | 45947/cuda:1 | ~44% | ~19h |

**等待中**：full-FT baseline 完成后 → cuda:0/2 空出 → 启动 A1 LoRA ×2（前提：lora_utils.py 已修复同步）

### 4. 📋 待办（条件触发式）
- full-FT baseline 完成通知到达 → 核实 log 最终 loss + step count，确认正常收敛，检查 eval 是否自动启动
- A1 LoRA 启动通知 → ssh_read_only 验证：(1) lora_utils.py 已同步 (2) CUDA_VISIBLE_DEVICES 在白名单内 (3) Phase 2 LoRA 解冻实际生效（grep 日志看 "unfreezing" / "lora" 关键词）
- A3 完成通知 → 核实最终 loss 合理性 + step=30K + checkpoint 存在
- 任何实验 eval 结果出来 → 交叉验证 registry metrics vs 实际 eval log，检查 CAR/TSR 数字
- Paper Agent 提交 Experiments 章节审查 → 模式 B 审查，重点：(1) 数字与 registry 一致 (2) ablation 是否覆盖 π0-LoRA → ColliForce-Aux → ColliForce (3) AEGIS 对比是否 fair (4) λ_refine sweep 结果
- Director 问叙事调整 → 根据实际 CAR/TSR 数字对照三个场景（best/MVP/worst）判断叙事是否需要 reframe

### 5. 🎯 战略上下文
- **决策链**：D001 锁定 π0/openpi → D003 接受非 watertight SDF → D004 Phase B 启动 → D005 砍 s1 只留 s0 → D006 kill A1 释放 GPU 给 LoRA baseline
- **核心赌注**：A3 (ColliForce full) 的 CAR↓≥15% + TSR↓<10%。这是唯一的 MVP gate。
- **最容易判断错的事**：
  1. **不要混淆 registry log_path 和实际日志**——之前发现 registry 中 baseline 的 log_path 指向旧 failed attempt 日志（EXIT_CODE=2），实际训练日志在 `/root/autodl-tmp/colliforce-outputs/baseline_lora_*/train.log`
  2. **A1 还没成功训练过**——M014 确认 Phase 2 LoRA 解冻从未生效。如果看到 A1 "完成"的 registry entry，要怀疑是假阳性（LoRA 没解冻 = 变成了纯 auxiliary head 训练，action backbone 完全没学到 SDF 信号）
  3. **LoRA baseline VRAM ~23884 MiB，A3 VRAM ~16.9GB**——VRAM 差异可能是 batch size 不同导致，核实时注意
  4. **AEGIS 数字 77.85% vs 59.16%**——Introduction 当前写 77.85%（CAR 绝对值），但之前某版本写过 59.16%（improvement rate）。两个数字含义不同，核实时分清是 CAR 值还是 improvement percentage


---
