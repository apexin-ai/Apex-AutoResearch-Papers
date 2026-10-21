# reviewer / loop_4.md

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_4.md`
- **Structured JSON:** [`540d0396240ef07d2800.json`](../../sessions/54/540d0396240ef07d2800.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_wall_time
updated: '2026-05-23T19:46:18+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-34685 的 checkpoint rotation 脚本不覆盖当前实验（vanilla_retrain/full_occ_retrain/reverse_cutoff/cutoff_25k/cutoff_15k/cutoff_45k），磁盘需手动监控
- westd-10894 的 `cleanup_old_checkpoints.sh`（PID 453371）已修复 `is_in_use()` 检查，但只覆盖 detach_ln_s0/s1/s2 + cutoff_s2_v2 四个目录
- detach_ln 从头训练时 `cfg.vla_path` 指向 base model（安全），但如果任何实验用 `--resume True` 启动，checkpoint rotation 可能删除 vla_path 目标导致 save 崩溃（已发生过一次，root cause 在 finetune.py:725 的 `from_pretrained(cfg.vla_path)`）
- 梯度分析 checkpoint 来源不一致：vanilla/full_occ 用 retrain_s0（seed 42），detach/random_occ 用旧 ablation_s2（seed 44, BN）。已发 WARNING，Director 已知。论文引用时需注明

### 2. 🖥️ 基础设施快照
- **westd-34685**：`/root/occsafe_vla/openvla-oft`，conda env `occsafe`，Python `/root/miniconda3/envs/occsafe/bin/python3.10`
  - 模型：`/root/autodl-tmp/models/openvla-7b`
  - 数据：`/root/autodl-tmp/data/modified_libero_rlds/`
  - Checkpoints：`/root/autodl-tmp/checkpoints/{vanilla_retrain_s0,full_occ_retrain_s0,...}/`
  - 梯度分析结果：`/root/occsafe_vla/analysis/results/gradient/`
  - 日志：`/root/runs/occsafe_vla/*.log`
  - 磁盘：350G 总量，~170G 已用，~181G 可用
- **westd-10894**：同路径结构，磁盘 250G 总量，~52G 已用，~199G 可用
  - Checkpoint rotation：PID 453371，每 30 min，覆盖 detach_ln + cutoff_s2_v2
- W&B 未启用（本轮实验均无 wandb）

### 3. 📊 当前状态
刚完成 D026 叙事审查（collapse prevention claim 强度、EWC 类比问题、checkpoint 来源方案）。

**RUNNING 实验：**
| 实验 | 服务器 | GPU | 进度 | ETA |
|------|--------|-----|------|-----|
| reverse_cutoff_s0 | westd-34685 | 2 | 96% (47839) | ~20 min |
| cutoff_25k_s0 | westd-34685 | 3 | 96% (47959) | ~18 min |
| cutoff_15k_s0 | westd-34685 | 1 | 8% (4105) | ~12h |
| cutoff_45k_s0 | westd-34685 | 0 | 6% (3153) | ~12.5h |
| detach_ln_s0 | westd-10894 | 1 | ~5% | ~12h |
| detach_ln_s1 | westd-10894 | 2 | ~5% | ~12h |
| detach_ln_s2 | westd-10894 | 3 | ~5% | ~12h |
| cutoff_s2_v2 | westd-10894 | 0 | ~25% | ~8h |

**DONE（本 session 完成）：** vanilla_retrain_s0, full_occ_retrain_s0（50K checkpoint 均完整）

**已完成分析：** 梯度分析 4 条件（vanilla/full_occ/detach/random_occ × 201 batches），figure 已生成（`artifacts/figures/gradient_analysis_combined.pdf`）

### 4. 📋 待办
- reverse_cutoff_s0 + cutoff_25k_s0 完成（~20 min）→ 验证 50K checkpoint 保存 → 确认 eval 启动（命令已在 memory.md）→ GPU 2/3 空闲后应立即跑 eval
- vanilla_retrain_s0 eval 也待跑 → 需等 GPU 空闲（reverse_cutoff eval 后）
- detach_ln_s0 完成（~12h）→ 用同 round checkpoint 重跑梯度分析（vanilla_retrain_s0 + full_occ_retrain_s0 + detach_ln_s0，全 seed 42）→ 替换当前 cross-round 数据
- cutoff_s2_v2 完成（~8h）→ GPU 0 空闲 → 可补训 random_occ_s0（seed 42）如果 Director 决定需要 4 条件同 seed 梯度分析
- 所有 eval 完成后 → 更新论文主结果表 → 需审查数字一致性

### 5. 🎯 战略上下文
- **项目**：occsafe_vla，CoRL 2026 投稿（Abstract May 26, Paper May 29）
- **核心结论**：auxiliary gradient flow prevents encoder gradient collapse during LoRA fine-tuning（D026 决策，从 amplification 转向 collapse prevention）
- **论文叙事**：6 条件 factorial ablation → gradient flow 是关键，label content 次要，任何 gradient flow 都能防止 collapse
- **EWC 类比有问题**：我已建议改为 deep supervision 类比，Director 未回复
- **易错点**：
  1. 不要把 tqdm 显示步数当实际进度——resume 实验的 tqdm 从 0 开始但 log_step = resume_step + gradient_step_idx
  2. 当前实验全部从头训练（非 resume），tqdm = 实际步数
  3. seed 42/43/44 对应 s0/s1/s2，不要混
  4. `occ_loss_cutoff_mode after` = 前 N 步有 OCC 后关闭（不是"在 N 步之后才开启"）
  5. 50K checkpoint 只有 vanilla_retrain_s0 和 full_occ_retrain_s0 可用于 seed 42 同 round 梯度分析，其他 3 条件的 seed 42 checkpoint 已被磁盘清理删除


---
