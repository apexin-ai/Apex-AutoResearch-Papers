# reviewer / loop_4.md

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_4.md`
- **Structured JSON:** [`a972982f5ce3139de8f9.json`](../../sessions/a9/a972982f5ce3139de8f9.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_wall_time
updated: '2026-05-25T04:22:19+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-35807 cuda:0-3，westd-45947 cuda:0-1。越界进程立即 CRITICAL
- LoRA baseline 实验结论未经 SSH 验证前**不可引用为正式结果**——当前 registry conclusion="failed" 是 SSH 监控失败，不是训练失败，但反过来也不能假设训练成功
- Pi0.5+A1 10K 数据只有 seed 0，论文中不可写 "across seeds" 或暗示多 seed 验证
- spatial_bowl 必须 5/28 前启动训练（CoRL DDL 约束），否则放弃泛化性提升
- Claim 4 措辞禁区：SOTA / consistently outperforms / general solution（paper_framing.md 明确标注）

### 2. 🖥️ 基础设施快照
- **westd-35807** (root): 4×GPU, `/root/colliforce-vla`, conda base (`/root/miniconda3/bin/python`)
  - 4 个 Pi0.5+A1 seed 训练（s1_l005/s1_l01/s2_l005/s2_l01）已退出，checkpoint 待验证
  - SSH 当前 Authentication failed
- **westd-45947** (root): 2×GPU, `/root/colliforce-vla`, conda base
  - LoRA baseline s0 (cuda:0, PID 757002) + s1 (cuda:1, PID 757081) 已退出，wall_clock ~16.9h，checkpoint 待验证
  - SSH 当前 Authentication failed
- 论文目录: 本地 `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/`
- Figures: `artifacts/figures/` (fig_tsr_car_scatter.pdf ✓, fig_oracle_bar.pdf ✓, fig_displacement_hist.pdf mock)
- W&B: WANDB_MODE=offline（所有训练）

### 3. 📊 当前状态
所有不依赖 SSH 的论文改进已穷尽。论文 16 页编译通过，~9.6/10。

**Registry 关键实验：**
- 6 个实验标记 "failed" 但实际是 SSH 监控失败（训练大概率完成）：
  - westd-35807: train_pi05_a1_obj_s1_l005/s1_l01/s2_l005/s2_l01
  - westd-45947: train_pi05_lora_baseline_s0/s1
- train_pi05_a1_obj_s0_l005 + s0_l01: DONE/success（seed 0, 30K 完成，已有 10K eval 数据）

**等待中：** SSH 恢复（Manager/用户介入刷新凭证）

### 4. 📋 待办
- SSH 恢复 → 逐一核实 6 个 "failed" 实验的 log + checkpoint → 更新 registry
- 6 个实验确认完成 → 30K eval（6 模型 × 200 episodes）→ 填充 §5.4 placeholder + Table 1
- LoRA baseline eval 出结果 → 对照 paper_framing.md 场景 2a-2d 判断 SDF 增量归因
  - LoRA CAR ≈ baseline (~27%) → SDF 全归因，最强 method claim
  - LoRA CAR ~35-45% → SDF 仍有增量，需 4-point lambda 曲线
  - LoRA CAR ~55%+ → 归纯 LoRA，pure analysis paper
- 30K eval 数据到位 → 真实数据替换 displacement histogram mock + lambda-CAR curve figure
- spatial_bowl 训练需 5/28 前启动 → SSH 恢复后尽快铺（代码+数据 ready）

### 5. 🎯 战略上下文
**核心叙事：** Analysis paper with positive method contribution。Claim 1 (fake safety) 是最强贡献(★★★★★)，Claim 4 (Pi0.5+A1) 是 secondary proof-of-concept。论文价值不取决于 method 是否 SOTA，而在于揭示 metric contamination。

**决策链关键节点：** D010 终止 runtime refinement → D012 定义 pass/fail gate → D014 锁定主会目标 → D015/D016 10K mid-eval positive → D018 gradient correction 机制分析

**下一个"我"最容易错的事：**
1. 把 SSH 监控失败等同于训练失败——已有 6 个实验被这样误标，SSH 恢复后第一件事是核实而非重跑
2. LoRA baseline 结果出来前不要急于更新 Claim 4 措辞——SDF 增量归因完全取决于 LoRA-only CAR 是多少
3. Pi0.5 "shows the same pattern" (abstract) 指的是安全 episode 中 displacement 也极低（56/56 near-zero），不是说 Pi0.5 有 action collapse——这个区分很重要，审稿人问起来要准确回答
4. 接受率估算：当前 35-40% CoRL / 40-50% ICRA；加 spatial_bowl + 3-seed 可提升到 55-65%


---
