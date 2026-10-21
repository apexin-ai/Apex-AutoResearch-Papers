# director / loop_4.md

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_4.md`
- **Structured JSON:** [`da2169298a76cb7f2b1b.json`](../../sessions/da/da2169298a76cb7f2b1b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_messages
updated: '2026-05-25T20:29:00+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-35807 分配 GPU 0/1/2/3（4卡），westd-45947 分配 GPU 0/1（2卡），共 6 卡。不得使用其他 GPU
- eval_safelibero.py L1141 根因未修复：提交 eval 时 --gpu 值必须与 spec GPU 编号严格一致，否则会覆盖 CUDA_VISIBLE_DEVICES 导致 GPU 冲突
- Registry 中 `frozen_pct` 在 10K 和 30K 语境含义不同：10K 指障碍物未被碰触比例（obs frozen），30K 指 EE 冻结比例。写论文/分析时必须区分。Reviewer 建议改名为 `obs_frozen_pct`，尚未执行
- `task2_fake_safety: true` 标注有误（实际是 learned avoidance），需修正为 false

### 2. 🖥️ 基础设施快照
- **westd-35807** (connect.westd.seetacloud.com)：代码路径 /root/colliforce-vla，4×GPU
- **westd-45947** (connect.westd.seetacloud.com)：代码路径 /root/colliforce-vla，2×GPU
- 镜像：aml-train（conda 环境，/root/miniconda3/bin/python）
- westd-35807 约 3h 前重启过，所有进程已由 Agent 恢复
- W&B / HF cache：未配置

### 3. 📊 当前状态
**刚完成**：P0 GPU 冲突修复（kill 误入进程 + eval_safelibero.py --gpu 逻辑修复 + 双服务器同步）；eval_pi05_a1_best_s2_l005_10k 完整 displacement 分析（确认 10K = real safety, 30K = action collapse）。

**RUNNING 实验**（服务器重启后恢复，ETA ~10:30 UTC May 26）：
| exp_id | 服务器 | GPU | 说明 |
|--------|--------|-----|------|
| train_pi05_a1_spatial_bowl_s0_l005 | westd-35807 | 0 | 跨场景泛化训练 |
| eval_pi05_a1_30k_s1_l005_disp | westd-35807 | 1 | **最关键**：seed1 30K displacement eval，验证 action collapse 跨 seed |
| eval_pi05_a1_best_s1_l005_16k | westd-35807 | 2 | seed1 best checkpoint eval |
| eval_pi05_a1_30k_s0_l005_r4 | westd-35807 | 3 | seed0 30K 重跑 eval |
| train_pi05_lora_baseline_s0 | westd-45947 | 0 | LoRA baseline 训练 |
| train_pi05_lora_baseline_s1 | westd-45947 | 1 | LoRA baseline 训练 |

**等待中**：Agent 正在处理之前的 director 指令（补录 registry metrics）+ 1 条 worker:done 回调排队。

### 4. 📋 待办
- eval_pi05_a1_30k_s1_l005_disp 完成 → 第一时间分析 max_ee_displacement，验证 30K action collapse 是否跨 seed1 成立
- eval_pi05_a1_best_s1_l005_16k 完成 → 对比 seed1 的 10K vs 30K，验证 learned avoidance 跨 seed
- 上述两个 eval 都完成 → 整合全部 seed 数据，做 MVP 整体判断（action collapse story 是否足够 robust）
- Registry 修复：`task2_fake_safety` 改 false，`frozen_pct` 重命名为 `obs_frozen_pct`（Reviewer warning 未处理）
- LoRA baseline 训练完成 → eval 对比 SDF vs baseline 的 TSR/CAR trade-off
- spatial_bowl 训练完成 → eval 跨场景泛化能力

### 5. 🎯 战略上下文
**核心发现（MVP 关键）**：SDF auxiliary loss 在 10K 步产生 real safety（EE 正常运动 + 主动避障），但 30K 步 collapse 为 fake safety（EE 冻结 < 10mm）。30K 端已在 3 seeds × 2 lambdas 全量确认 100% frozen。**degradation story 成立**，但需 seed1 数据补全。

**TSR 问题**：即使 10K best（real safety），avg_TSR 仅 9%。SDF loss 的安全收益（CAR 28%→55.5%）伴随灾难性任务退化（TSR 75%→9%）。论文不能 overclaim 10K 的成功——narrative 应定位为"SDF CAN 产生真实避障但需要更好的训练策略"。

**易错点**：
- 不要混淆 `frozen_pct`（obs frozen vs EE frozen）——两个上下文含义完全不同
- 10K vs 30K 的 TSR/CAR 数值接近（9%/55.5% vs 9%/53%），但机制完全不同（learned avoidance vs action collapse）。表面数值对比无意义，必须看 EE displacement
- eval_safelibero.py 的 --gpu 覆盖 bug 只做了 workaround（参数对齐），根因未改
- 项目仍在 MVP 阶段，不要在 MVP 完成前启动完整研究规划或写 paper_framing


---
