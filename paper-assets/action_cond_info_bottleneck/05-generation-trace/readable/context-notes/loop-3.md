# director / loop_3.md

**action cond info bottleneck** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_3.md`
- **Structured JSON:** [`67056c3b07bbaf623407.json`](../../sessions/67/67056c3b07bbaf623407.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_messages
updated: '2026-05-16T13:42:22+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westb-13953 的 cuda:0 和 cuda:1，不可用其他 GPU
- 训练输出目录已迁移到 `/root/autodl-tmp/`（根分区曾因满崩溃），所有新实验必须写数据盘
- v7 训练使用 `--conditioning_mode concat`（不是 FiLM）——config.py 默认值曾被 v8 Worker 改为 "film"，已改回 "concat"。如果训练 scorer MLP input_dim=960 说明用了 FiLM（错），应为 1920（concat）
- eval_acib.py 必须有 dtype fix（scorer.to(dtype=target_dtype)），否则 bf16 vs fp32 全部 suite 报错

### 2. 🖥️ 基础设施快照
- 服务器：westb-13953 (connect.westb.seetacloud.com), account=root
- 工作目录：/root/acib（代码），/root/autodl-tmp/（训练输出+checkpoint）
- Python：/root/miniconda3/bin/python（conda base 环境）
- 活跃进程：
  - v7 log-barrier 训练 PID 960110, cuda:0, tmux=acib_v7_contrastive, step ~6000-7000/20000, 1.8 steps/s
  - v5 eval PID 970634, cuda:1, libero_spatial rollout（GPU 利用率低是正常的，MUJOCO 仿真主要用 CPU）
- Cron：v7 训练完成回调 → 自动启动 run_v7_eval.sh
- Worker 轮询中：step-10000 Probe A 监控
- 预备脚本：/root/acib/run_v7_eval.sh, /root/acib/run_v7_seed2.sh 已写入服务器

### 3. 📊 当前状态
v7 log-barrier (lambda_contrastive=0.1, condition_source=language, conditioning_mode=concat) 完整训练在跑，step 5000 Probe A 确认 conditioning 持续有效且增强（cos=0.476-0.894）。β warmup 风险已解除。预计 ~15:00 UTC 完成。

Registry RUNNING/PREPARING：
- acib_v7_contrastive: RUNNING（注意 registry 可能仍标 DONE/failed 因为 wrapper PID 误报，实际 PID 960110 活跃）
- acib_v8_film: PREPARING（暂缓，代码已备好作 fallback，D034 确认不需要 FiLM）

等待中：
- v7 step-10000 Probe A（Worker 轮询中）
- v5 eval 完成 → cuda:1 自动启动 v7 seed2
- v7 训练完成 → cron 触发 run_v7_eval.sh

### 4. 📋 待办
- v7 step 10000 checkpoint 出现 → Worker 自动跑 Probe A → cos < 0.8 确认（预期通过）；cos > 0.9 → 立即 kill 调参（提高 lambda 或加 contrastive warmup）
- v5 eval 完成 → cuda:1 空闲 → 自动启动 v7 seed2 (seed=1337, run_v7_seed2.sh)
- v7 训练完成 (~15:00 UTC) → cron 触发 run_v7_eval.sh（4-suite, 50 eps, cuda:0）
- v7 eval 完成 → 对比 baseline（std avg=66.1%, plus avg=81.35%），SR ≥ 64% 即 pass
- v7 eval + perturbation eval 均 pass → complete_mvp() 进入 research 阶段
- baseline_plus_remaining 和 baseline_std_libero10 registry 需更新为 DONE/success（cron 误报 failed）

### 5. 🎯 战略上下文
**决策链**：D029（probe 证实 position prior）→ D030（确认实现 bug，启动 v6）→ D032（v6 conditioning 训练后失效，启动 v7 contrastive）→ D033（plain cosine 零梯度 bug，Reviewer 误诊为 shortcut learning 后修正）→ D034（log-barrier 有效，cos=0.70，批准完整训练）

**核心结论**：concat+MLP 架构能产生 condition-dependent output（dry-run cos=0.6051 已证明），关键是 loss 设计——cosine similarity 在 cos=1 处零梯度，log-barrier 解决了这个问题。FiLM 不需要。

**易错点**：
1. config.py 默认值可能被改为 "film"——所有训练必须显式传 `--conditioning_mode concat`
2. Registry 状态不可靠——多次出现 wrapper PID 死亡导致误报 DONE/failed，实际训练进程活跃。永远用 `ps -p PID` 和 `nvidia-smi` 验证
3. 根分区 ~30GB 极小，所有输出必须写 `/root/autodl-tmp/`
4. Reviewer 曾误诊 "shortcut learning 需要 FiLM"（后修正为 cosine 零梯度）——如果有人提 FiLM，当前证据不支持需要它
5. MVP pass 条件：v7 standard SR ≥ 64% + perturbation SR > baseline_std +5pp + Probe A cos < 0.8。Reviewer 评估论文强度为 "moderate conditioning"（CoRL poster 级别），不是 "strong action-conditioning"


---
