# reviewer / loop_7.md

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_7.md`
- **Structured JSON:** [`d7ed94286ddb229331a1.json`](../../sessions/d7/d7ed94286ddb229331a1.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_wall_time
updated: '2026-05-27T09:17:55+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 (C001)：westd-35807 cuda:0-3 + westd-45947 cuda:0-1，共 6 张。越界即 CRITICAL。
- 所有 Pi0.5 模型 eval 必须带 `--pi05` flag + `--config_name pi05_libero` + `--model_type lora_baseline`。缺 `--pi05` 会加载 Pi0 架构导致假 frozen 数据（本 session 24K/26K 踩过坑，已发 CRITICAL 纠正）。
- submit_training_job 预估 >20h 必须设 timeout_hours=48 (C003)，不能用默认 24h。
- eval 结果验证必须查 JSON 输出文件，不能只看 cron 状态——cron 对 eval 有系统性误报（无 W&B/sentinel → 标 failed）。

### 2. 🖥️ 基础设施快照
- 服务器：westd-35807 (root) + westd-45947 (root)
- 代码根目录：`/root/colliforce-vla`（两台服务器相同）
- Checkpoint 路径：`/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/`
- Eval 输出：`/root/autodl-tmp/eval_results/`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/`
- 论文文件：`docs/paper/` 下 abstract.tex, claim3.tex, discussion.tex 等
- WANDB_MODE=disabled（本项目不用 W&B）
- 活跃进程（截至 handoff 时）：
  - s0 30K eval: PID 722752, westd-35807 GPU0 (~18:00 UTC 出结果) ← **最关键**
  - s1 训练: PID 274407, westd-35807 GPU2, ~29000/30000
  - spatial_bowl: PID 341425, westd-35807 GPU3, ~18500/30000
  - LoRA s2 resume: PID 460433, westd-45947 GPU0, ~26000/30000
  - λ=0.1 s2: PID 425058, westd-45947 GPU1, ~17000/30000

### 3. 📊 当前状态
**刚完成**：λ=0.1 s0 30K 训练完成，30K eval 已启动（PID 722752, GPU0, 带 `--pi05`），约 40min 出结果。

**本 session 已发 8 份报告**：
1. [warning] LoRA s2 timeout + GPU0 idle
2. [info] s1 22K confirms Scenario B
3. [info] 22K outlier paper explanation
4. [warning] Fig1 v2 Pi0.5 28.5%→26.8% 数字错误
5. [warning→retracted] 24K frozen=29.5%（eval bug）
6. [critical] --pi05 flag 纠正 + 24K 作废
7. [warning] Claim3 baseline 26.8% vs Abstract 28.5% 不一致
8. [warning] Discussion CAR_f→dfCAR 术语不一致（已修复）

**Registry RUNNING**：5 个实验（见上方活跃进程）。

**等待中**：s0 30K eval 结果 → 这是 Scenario B 的定论数据点。

### 4. 📋 待办（条件触发式）
- **s0 30K eval 完成** → 验证 CAR 是否在 null band (54.5±2.15)；若是 → Scenario B 确认，通知 Director 可部署 paper patch 并填 placeholder
- **s1 训练完成 (~17:35 UTC)** → 确认 30K checkpoint 存在 → 监控 eval 启动是否带 `--pi05`
- **s1 30K eval 出结果** → 计算 s0+s1 双 seed 30K 均值，更新 claim3.tex Table λ=0.1 行
- **LoRA s2 resume 完成 (~21:00 UTC)** → 验证 checkpoint → 此 seed 补全 null distribution 为 3-seed
- **λ=0.1 s2 完成 (~08:40 UTC 5/28)** → 完成三 seed 30K；计算 final mean±std → 替换所有 placeholder
- **spatial_bowl 完成 (~06:00 UTC 5/28)** → eval → 验证跨场景泛化
- **Abstract 28.5% vs Table 26.8% 不一致** → 仍未解决，定稿前必须统一（已报两次 warning）

### 5. 🎯 战略上下文
- **核心结论 = Scenario B**：SDF 在全测试范围 λ∈[0.005, 0.1] 冗余，CAR 增益全部来自 collision-free demonstrations 的 imitation。Step-wise 曲线 7 个点（16K-28K）全在 null band 内，平线无上升趋势。
- **Null distribution**：pooled from LoRA s0/s1 + SDF λ=0.005 s0/s1/s2 = 5 values, mean=54.5%, σ=2.15%
- **22K 异常值 (60.5%, z=2.79)**：已通过三重独立验证确认为噪声（s1=56.5, s0 24K=52.5 回落, s0 26K=53.5 回落）
- **Claim 4 已 falsified**（见 memory）：LoRA-only CAR≈SDF CAR，SDF loss 添加零碰撞避免。
- **DDL**: 5/28 12:00 UTC。λ=0.1 s2 ETA 08:40 UTC 5/28，距 DDL 仅 3.3h，非常紧。
- **最容易判断错的事**：
  1. 不要因为单个数据点偏高就质疑 Scenario B——22K=60.5% 已被确认为噪声
  2. Eval 的 cron "failed" 通知是假阳性——必须独立查 JSON 输出
  3. 论文中 26.8%（3-seed baseline CAR）和 28.5%（abstract dfCAR）的不一致仍未解决
  4. Discussion 已统一用 dfCAR（不是 CAR_f），但要注意后续章节修改保持一致


---
