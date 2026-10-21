# agent / loop_6.md

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_6.md`
- **Structured JSON:** [`24b02ef27cdc7c6546e3.json`](../../sessions/24/24b02ef27cdc7c6546e3.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: idle_timeout
updated: '2026-05-28T22:27:53+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单: westd-35807 cuda:0/1/2/3, westd-45947 cuda:0/1（共 6 张）
- submit_training_job 命令必须自带 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate libero`
- 模型/数据/checkpoint 必须放 `/root/autodl-tmp/`，根分区只有 ~30GB
- GPU 编号脚本内始终从 0 开始（框架自动 CUDA_VISIBLE_DEVICES 映射）
- DDL 是 **2026-05-28 12:00 UTC**（北京 20:00）

### 2. 🖥️ 基础设施快照
- **westd-35807**: 工作目录 `/root/colliforce-vla`，Python `/root/miniconda3/envs/libero/bin/python`，conda env `libero`，磁盘 570G/879G 可用
- **westd-45947**: 同上结构，磁盘 400G/439G 可用
- Checkpoint 路径: `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/`
- 活跃进程: **无**——全部实验已完成，0 cron 活跃
- 全部 6 张 GPU 空闲

### 3. 📊 当前状态
**所有实验已完成，0 RUNNING。** 论文处于 Review Director 最终检查阶段。

上一轮（Loop #5）完成了大量论文修正工作：
- 收割 multi-eval-seed battery（5 个 eval，06:00 UTC 完成）
- 完成 urgent-wording-sync、title、scope/safevla/limits 修正、paper-switch-final verify
- 1 个 Worker `worker_paper_p1-1-terminology` 正在运行（06:18 启动，做论文术语修正）

我（Loop #6）做了 session-start 初始化，确认 registry 全部 DONE，向 Director 汇报了状态，等待 Director 指令。

Multi-eval-seed 最终结果（补充验证，不影响论文核心结论）：
- LoRA s0 across eval seeds: {7:57%, 42:56.5%, 123:53%} → mean≈55.5%
- SDF λ=0.1 s0 across eval seeds: {7:58%, 42:59%, 123:58.5%, 256:57%} → mean≈58.1%

### 4. 📋 待办
- `worker_paper_p1-1-terminology` 完成回调 → 检查修正结果，确认论文术语一致性
- Director 回复最终检查结果 → 如有额外修改要求则立即派 Worker 执行；如确认通过则准备提交
- 如 Director 要求 PDF 重编译 → 派 Worker 到 westd-35807 编译 + 视觉验证
- 最终提交前 → 确认 westd-35807/westd-45947 上的 PDF 版本一致（ROADMAP 警告 westd-45947 PDF 可能是旧版）

### 5. 🎯 战略上下文
- **核心结论链**: D032 低λ(0.005) SDF冗余 → D033 λ=0.1可能有效 → D038 Scenario C初步确认 → D043 λ=0.1 s2 CAR=54.5% → 3-seed p=0.0714 → **Scenario B confirmed**（趋势性但不显著）
- **可信数据**: LoRA 3-seed 54.67%±2.02% | SDF λ=0.1 3-seed 57.00% | perm p=0.0714(单尾)
- **统计策略 (D041)**: 正文双尾 permutation，脚注单尾 + directional prior
- **易错点**:
  - 不要混淆 rotation-fixed (D033后) 和 rotation-broken (D033前) 的 eval 数据
  - LoRA s0 可信值是 reeval_v2 的 57%，不是旧的 54.5%
  - 论文已降级到 Scenario B narrative（趋势性差异），不要在任何地方 claim 显著性
  - 时间极紧——剩余时间应全部用于论文最终校对和提交，不要再开新实验


---
