# agent / loop_7.md

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_7.md`
- **Structured JSON:** [`f20284545ba54f2deccd.json`](../../sessions/f2/f20284545ba54f2deccd.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: idle_timeout
updated: '2026-05-28T06:11:58+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-10894:cuda:0-3 + westd-34685:cuda:0-3，共 8 张，不可用其他
- eval 命令必须带 `MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID={物理GPU编号}`，否则渲染黑屏
- 训练命令必须 `bash -c "..."` 包裹（tmux 用 sh 不是 bash），否则 source/conda activate 失败 EXIT_CODE=127
- WANDB_MODE=disabled（本项目所有训练），不要期望 W&B 数据，日志分析走 tail_training_logs
- checkpoint 路径格式：`/root/autodl-tmp/checkpoints/{exp_id}/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--{run_id_note}--50000_chkpt`
- **DDL: May 28 12:00 UTC (SafeRL Workshop @ RSS 2025)**，距离约 22h

### 2. 🖥️ 基础设施快照
- **westd-34685**: 工作目录 `/root/occsafe_vla/openvla-oft`，conda env `occsafe` (`source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe`)，数据盘 `/root/autodl-tmp/`，磁盘 819G/879G (2%)
- **westd-10894**: 同上，磁盘 425G/879G (50%)
- 模型：`/root/autodl-tmp/models/openvla-7b`，数据：`/root/autodl-tmp/data/modified_libero_rlds/`
- OCC 数据：`/root/occsafe_vla/occ_data`
- eval 脚本：`vla-scripts/evaluate_safelibero.py`，训练脚本：`vla-scripts/finetune.py`
- **活跃进程**（8 个 cron 监控中）:
  - 34685:0 detach_ln_v2_s1_35_eval (eval, Cell 4)
  - 34685:1 detach_ln_s4_eval (eval, Cell 4)
  - 34685:2 ablation_occ_detach_s4_eval (eval, Cell 3, PID 873426, 刚启动)
  - 34685:3 mvp_occ_s4 (训练, Cell 1, PID 736253, ~76%)
  - 10894:0 full_occ_ln_v2_s1c_r2 (训练, Cell 2 v2, PID 481426, ~69%)
  - 10894:1 full_occ_ln_v2_s2_r2 (训练, Cell 2 v2, PID 481643, ~69%)
  - 10894:2 detach_ln_v2_s0c_r3 (训练, Cell 4 v2, PID 543255, ~12%)
  - 10894:3 full_occ_ln_s4 (训练, Cell 2, PID 553813, ~8%)

### 3. 📊 当前状态
刚完成 `ablation_occ_detach_s4` (Cell 3, Detach BN, seed 46) 训练 → DONE(success)，已在 34685:cuda:2 启动 eval (`ablation_occ_detach_s4_eval`, RUNNING, cron 已注册)。registry 已更新，Director 已汇报。

**RUNNING 实验**（8 个）: 见上方活跃进程列表。

**等待中**:
- 批次① 34685:0-1 两个 Cell 4 eval 完成回调（detach_ln_s4_eval + detach_ln_v2_s1_35_eval）
- 批次② 34685:2 ablation_occ_detach_s4_eval (~1h) + 34685:3 mvp_occ_s4 训练完成后需启动 eval
- 批次③ 10894:0-1 Cell 2 v2 训练完成 (~22:50 UTC) → 需启动 eval
- 批次④ 10894:2-3 最后两个训练 (~06:20-06:50 May 28) → eval → 全 v2 ANOVA

### 4. 📋 待办（条件触发式）
- `mvp_occ_s4` cron 回调 → 检查 checkpoint → 标 DONE → 立即在 34685:cuda:3 启动 `mvp_occ_s4_eval`
- `detach_ln_s4_eval` 或 `detach_ln_v2_s1_35_eval` cron 回调 → spawn Worker 读 JSON 结果 → 提取 CAR/TSR → 更新 registry metrics → 汇报 Director Cell 4 数据
- `ablation_occ_detach_s4_eval` cron 回调 → 同上，更新 Cell 3 n=5 数据
- `full_occ_ln_v2_s1c_r2` + `full_occ_ln_v2_s2_r2` 训练完成 → 启动 eval → Cell 2 v2 n=3 达成
- 全 4 个 Cell 均有 v2 n≥3 数据 → spawn Worker 跑 2×2 ANOVA → 更新 Table 1 → 最终编译
- 最终编译完成 → 汇报 Director 可提交

### 5. 🎯 战略上下文
- **核心 claim**: gradient flow 是损害源，detach 后 aux head 无害（≈ Vanilla）。BN×gradient flow 2×2 factorial 设计
- **Vanilla baseline**: n=3, CAR=0.745±0.024。Detach BN (0.767) ≈ Vanilla (p=0.28)；Full OCC BN (0.725) < Vanilla
- **v2 rebuild**: v1 代码有 bug，v2 是修复后重跑。Cell 2 (Full OCC LN) 和 Cell 4 (Detach LN) v2 数据严重不足（n=1），是 DDL 前的关键瓶颈
- **Plan B**: 如果 v2 数据凑不齐，Cell 4 Detach+LN 标为 v1 数据（加 $^\star$ 标记），省略 ΔCAR（D067 决策）
- **易错点**: 
  - eval 结果在 `/root/occsafe_vla/artifacts/safelibero_libero_spatial_*.json`，不是 W&B
  - Cell 编号：1=Full OCC BN, 2=Full OCC LN, 3=Detach BN, 4=Detach LN, Vanilla=无 OCC head
  - 10894 曾多次 GPU stall / driver 故障，如果实验失败先查硬件而非代码
  - submit_training_job 后需要手动推进 registry 状态（PREPARING→PENDING→QUEUED→ALLOCATED→RUNNING），框架不自动转


---
