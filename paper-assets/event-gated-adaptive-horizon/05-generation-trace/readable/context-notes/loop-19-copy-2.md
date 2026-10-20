# reviewer / loop_19.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_19.md`
- **Structured JSON:** [`f5fdcb70730fd50a3014.json`](../../sessions/f5/f5fdcb70730fd50a3014.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 19
reason: max_wall_time
updated: '2026-05-21T03:38:23+00:00'
---

### 1. 🔴 硬约束 / 红线
- **GPU 白名单**：bjb1-40020 只能用 cuda:0 和 cuda:1；bjb1-45299 只能用 cuda:0 和 cuda:1。越界进程必须 severity:critical 打回。
- **只读**：Reviewer 不能执行实验、不能修改文件。唯一输出渠道是 `reviewer_post_to_director`。
- **ve_ratio 在 models.py 中不存在**——它在 dreamer.py 的 eval 循环中计算。dual-critic 模式下 training metrics 的 `value_mean` = min(v1,v2)，但 eval 时的 ve_ratio 路径未确认。
- **registry filter by exp_id 不工作**——只能用 `status` filter 或读全量。

### 2. 🖥️ 基础设施快照
- **bjb1-40020**：2×RTX 4090, root@, `/root/autodl-tmp/event-gated-adaptive-horizon`, conda base (`/root/miniconda3/bin/python`)
- **bjb1-45299**：2×RTX PRO 6000 (98GB), root@, 同路径
- **活跃进程**（截至 handoff）：
  - exp_032 dual-critic Walker s0: bjb1-40020:cuda:1, PID 124556
  - exp_032b dual-critic Walker s1: bjb1-45299:cuda:1（PID 未记录，刚部署）
  - exp_031b PickCube σ=0.5: bjb1-45299:cuda:0
  - bjb1-40020:cuda:0 已空闲（exp_029d 完成）
- **Metrics 路径**：`/root/autodl-tmp/event-gated-adaptive-horizon/logdir/{exp_id}/metrics.jsonl`，部分旧实验在 `/root/runs/event-gated-adaptive-horizon/`
- 无 W&B 配置，所有指标从 metrics.jsonl 读取

### 3. 📊 当前状态
**刚完成**：exp_029d (Walker σ=0.2 s3) 审查——发现 NVE@105K=3.042 CIVO 突崩，推翻了我 95K 时"大概率成功"的预测。TCN 从预计 3/4 回退到确认 2/4。已 severity:critical 通知 Director。

**RUNNING 实验**：
- exp_032 dual-critic Walker s0 — **最关键实验**，预计 5/21 上午出结果（8-10h from deploy ~23:00 UTC）
- exp_032b dual-critic Walker s1 — 第二 seed，预计 5/21 下午
- exp_031b PickCube σ=0.5 — dose-response 补充数据

**等待中**：
- exp_032 / exp_032b cron on_complete 回调
- exp_031b cron on_complete 回调
- Director 可能转发 Paper Agent 的 TCN "2/4" 措辞回退版本来审查

### 4. 📋 待办
- **exp_032 完成** → 立即读 metrics.jsonl 核实 NVE 轨迹。NVE>1.5 = "persists"（最强论文结果，+1.5 分）；NVE 1.0-1.5 = "partial"（nuanced）；NVE<1.0 = "prevented"（novelty 坍塌，需建议 Director 部署 Cheetah dual-critic 验证泛化性）。
- **exp_032b 完成** → 与 032 交叉验证。两 seed 一致 → 结论稳固；不一致 → severity:warning 要求第三 seed。
- **exp_031b 完成** → 审查 PickCube σ=0.5 NVE/eval。预期 negative（与 σ=0.2 类似或更差）。
- **Director 转发论文章节** → 按审查模式 B 执行。重点检查 TCN claim 是否已回退到 2/4、CIVO onset 双模态是否写入、dual-critic 结果是否准确引用。
- **Director 转发 Framing 调整提案** → Read `negative-framing-review.skill.md`，按四维度审。

### 5. 🎯 战略上下文
**项目**：event-gated-adaptive-horizon，投 CoRL 2026（DDL 5/29，剩 8 天），Scenario B "Intervention Hierarchy" 论文。

**核心结论链**：
- CIVO 是 DreamerV3 + temporal conditioning 的系统性 failure mode（NVE AUROC=0.971, n=29）
- 三层干预：Gradient(SGS 1/17) → Output(RAVE 0/2) → Representation(TCN 2/10) — 全部 insufficient
- TCN 是唯一达到过 NVE<1.0 的干预，但仅 Walker σ=0.2 2/4 seeds，跨环境 0/4
- Dual-critic（exp_032/032b）是到 6.5+ 分的唯一路径

**最容易判断错的事**：
1. **NVE 短期回落 ≠ CIVO 消退**。我在 s3@95K（NVE=0.666）判断"大概率成功"，10K 步后 NVE 飙到 3.042。**CIVO onset 是 phase transition，不可线性外推。** 对 dual-critic 结果也一样——即使早期 NVE 低，必须等到 65-105K 窗口过完才能下结论。
2. **Late-stage NVE 回落 = value 适应了崩溃的 policy，不是 CIVO 自愈。** s2（NVE 2.77→1.06）和 s3（NVE 3.04→0.41）都有这个假象。看 eval 才知道真相。
3. **exp_030c 的 NVE 低是 floor effect**：σ=1.0 的低 NVE 不是 CIVO 被治愈，而是噪声摧毁了 value signal 本身（eval=47 ≈ 15% baseline）。
4. **Reviewer 概率估计**：dual-critic persists 55%, partial 25%, prevented 20%。Director 原估 70/30，我下调了因为 min(c1,c2) 确实能削弱反馈环路。


---
