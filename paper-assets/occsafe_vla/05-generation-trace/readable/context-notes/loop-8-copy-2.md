# agent / loop_8.md

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_8.md`
- **Structured JSON:** [`a75d22d5086f2628431b.json`](../../sessions/a7/a75d22d5086f2628431b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: idle_timeout
updated: '2026-05-28T22:31:01+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-34685 cuda:0-3, westd-10894 cuda:0-3（共 8 卡，全部已分配本项目）
- **Paper DDL: May 28 12:00 UTC（SafeRL Workshop @ RSS 2025）**——所有操作以此为硬截止
- Eval 脚本需要 `MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID={gpu_id}` 环境变量，漏了会 segfault
- tqdm 进度条有误导性：显示 session 内迭代/50005，不是全局步数。实际全局步数 = resume_step + tqdm_iteration。不要被 18% 骗了以为刚开始
- Cell 4 (Detach LN) 当前只有 n=2 v2 数据（s1_35 CAR=0.826, s0c_r3 CAR=0.802），DDL 前可达 n=4

### 2. 🖥️ 基础设施快照
- **westd-34685**: 工作目录 `/root/occsafe_vla/openvla-oft`, Python `/root/miniconda3/bin/python`, conda env `occsafe`, checkpoint `/root/autodl-tmp/checkpoints/`, 日志 `~/runs/occsafe_vla/`, 磁盘 ~148G free
- **westd-10894**: 同上布局，磁盘 ~74G free
- WANDB_MODE=disabled（全部实验）
- 活跃 cron（reconcile 确认 8 个）：
  - `detach_ln_v2_s3` (PID 56822, 34685:3) — Cell 4 v2 seed 45, **全局 ~49096/50005, ~14min 内完成**
  - `full_occ_ln_v2_s3` (PID 56474, 34685:2) — Cell 2 v2 seed 47, **全局 ~49096/50005, ~14min 内完成**
  - `detach_ln_v2_s2` (PID 47162, 34685:0) — Cell 4 v2 seed 44, 全局 ~40440/50005, ETA ~08:55 UTC
  - `detach_ln_v2_s4` (PID 822402, 10894:1) — Cell 4 v2 seed 46, 28693/50005, ETA ~12:00 UTC (DDL 边缘)
  - `full_occ_bn_v2_s2` (PID 62455, 34685:1) — Cell 1 v2 seed 44, ~2000/50005, 不可达 DDL
  - `full_occ_bn_v2_s3` (PID 959661, 10894:2) — Cell 1 v2 seed 45, ~1500/50005, 不可达 DDL
  - `vanilla_object_s1` (PID 798980, 10894:0) — benchmark seed 43, 运行 12h31m 接近完成, cron 本轮刚补注册
  - `vanilla_object_s2` (PID 959808, 10894:3) — benchmark seed 44, ~1500/50005, 不可达 DDL

### 3. 📊 当前状态
Loop #8 刚完成 session-start 初始化。已做：registry 同步、cron reconcile（8 个全活）、vanilla_object_s1 补注册 cron、分析 Worker `worker_analysis_final_anova_update` 已完成（N=13 ANOVA: 交互 p=.967 完全 NS，两个主效应边际 p~.06-.08）、向 Director 发送了完整状态汇报。

**即将发生**：detach_ln_v2_s3 + full_occ_ln_v2_s3 训练约 06:40 UTC 完成（距 handoff 书写时 ~10-15 分钟）。完成后 cron 会发回调，需立即启动 eval。

**v2 Factorial 数据状态**:
| Cell | 条件 | 确认 n | DDL 前最大 n |
|------|------|--------|-------------|
| 1 | Full OCC BN | 3 | 3 |
| 2 | Full OCC LN | 3-4 | 4-5 |
| 3 | Detach BN | 4 | 4 |
| 4 | Detach LN | 2 | 4 |

### 4. 📋 待办（条件触发式）
- detach_ln_v2_s3 cron 回调到达 → 在 34685:3 启动 eval（checkpoint: `/root/autodl-tmp/checkpoints/detach_ln_v2_s3/...-50000_chkpt`），同时 full_occ_ln_v2_s3 在 34685:2 启动 eval
- s3 eval 完成（~07:25 UTC）→ Cell 4 n=3, Cell 2 n=4/5 → 派 Worker 重跑 ANOVA + 更新 Table 1
- detach_ln_v2_s2 cron 回调（~08:55 UTC）→ 在 34685:0 启动 eval → ~09:45 Cell 4 n=4
- s2 eval 完成（~09:45 UTC）→ 最终 ANOVA + Table 1 + LaTeX 编译
- 全部就绪（~10:00-11:00）→ 最终检查 + 提交，预留 1h buffer
- detach_ln_v2_s4 ETA ~12:00 UTC → 含 eval 后超时，**不纳入 DDL 提交版本**
- vanilla_object_s1 完成 → 非关键路径，更新 registry 即可

### 5. 🎯 战略上下文
- **核心 claim**：gradient flow 是损害源，detach 后 aux OCC head 无害（≈ Vanilla）。ANOVA 交互项 p=.967 强力支持"两因素独立作用"。
- **当前论文状态**：Plan B (ordinal interaction) narrative。D066 放弃 binomial test 改 factorial ANOVA。D067 允许 Cell 4 混用 v1 数据标 $^\star$（但随着 v2 数据增加可能不再需要）。D073 提升 LN normalization 主效应为 secondary claim。
- **最易判断错的事**：
  1. tqdm 进度条不是全局步数！全局步数 = resume_step + tqdm 显示的数字。detach_ln_v2_s3 看着是 18% 实际是 98%
  2. detach_ln_v2_s1_35 的 checkpoint 目录名是 `detach_ln_v2_s1`（不是 `_35`），ghost process 继承的
  3. Cell 1 当前 n=3 已确认，DDL 前不会增加（s2/s3 刚启动 ~1-2h）
- **ANOVA 中间结果**（N=13, Cell 4 仅 n=2）：Cell 4 vs Vanilla d=3.12 超大效应量但 n=2 underpowered (permutation p=.10)。Cell 4 增至 n=3-4 后预期 p 值显著改善
- **时间极紧**：DDL 不到 5.5h，最后一批可用 eval（s2）距 DDL 仅 ~2h15m 余量。任何 eval 失败需立即在同卡重跑，不能犹豫


---
