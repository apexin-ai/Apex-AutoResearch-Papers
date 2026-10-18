# agent / loop_3.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_3.md`
- **Structured JSON:** [`422eded2392e147f2242.json`](../../sessions/42/422eded2392e147f2242.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: idle_timeout
updated: '2026-05-16T00:08:40+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：只能用 westd-27271 的 `cuda:0` 和 `cuda:1`，不可用其他设备
- v8 实验 ID 在 registry 中是 `mvp_imm_anchor_v8`（不是 `mvp_imm_v8a_stopgrad`，D023 计划中的名字和实际注册的不同）
- Checkpoint 路径陷阱：config 文件名决定 checkpoint 目录名，不是 exp_id。v8 用 `configs/imm_anchor_v8.yaml` → checkpoints 在 `checkpoints/imm_anchor_v8/`
- Baseline 唯一有效参照：`mvp_baseline_v5`（clean_action_loss=0.004077）。之前的 v1-v4 全部无效
- G3a (bypass-ACIS ratio ≤ 1.10) 是 MVP gate，不是 G3b/G3c。不要用 soft/hard mode 的 G3 做 MVP 判定
- D023 提到的 v8b (two-stage) 未启动，当前只跑了 v8a (stop-gradient/dual detach)

### 2. 🖥️ 基础设施快照
- 服务器：`westd-27271`，2× RTX PRO 6000 96GB
- 工作目录：`/root/autodl-tmp/importance_margin_vla_compress`
- Python：`/root/miniconda3/bin/python`，激活方式 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型：`lerobot/smolvla_base`（HF 在线加载，需 network_turbo）
- 数据集：`lerobot/aloha_sim_insertion_scripted_image`（20K samples）
- Eval results：`/root/autodl-tmp/importance_margin_vla_compress/eval_results/`
- 活跃进程：`mvp_imm_anchor_v8` PID=86610, tmux session, cuda:0, cron 监控中
- 活跃 Worker：`worker_eval_v8-step2k-early_20260515T232645`（v8 step 2K early eval）

### 3. 📊 当前状态
**刚做完**：v7.2 final eval 分析 → G3a=1.91x 确认权重损伤 → 实现 dual detach (gradient isolation) → v8 dry-run 通过（四项梯度检查全 PASS）→ v8 提交训练（PID 86610, cuda:0）→ 派 Worker 做 step 2K early eval。

**Registry 状态**：
- `mvp_imm_anchor_v8` — **RUNNING** — dual detach gradient isolation，30K steps，cuda:0。hypothesis: gradient isolation 消除 backbone 权重损伤 (G3a≤1.10)
- `mvp_baseline_v5` — DONE(success) — 唯一有效 baseline
- `mvp_imm_anchor_v7_2` — DONE(negative) — G3a=1.91x 确认梯度共享是根因
- 其余 11 个实验全部 DONE(failed/killed)

**等待中**：
- Worker `worker_eval_v8-step2k-early` 正在跑 v8 step 2K 的 early eval（确认 G3a 趋势）
- Cron 监控 v8 训练进程（PID 86610）
- cuda:1 空闲——D023 计划了 v8b (two-stage) 但未启动，应考虑是否并行跑

### 4. 📋 待办（条件触发式）
- Worker `eval_v8-step2k-early` 回调 → 读 early eval 结果：G3a 趋势 ≤1.5x → 继续等 final；G3a > 2.0x → gradient isolation 不够，需立即汇报 Director 讨论 v8b
- v8 cron 回调（训练完成）→ spawn Worker 跑 500-batch final eval（必须包含 bypass-ACIS 和 soft/hard 三档 G3）→ 全量 gate 判定
- v8 final eval G3a ≤ 1.10 + G1/G2/G4 维持 → **MVP PASS**，汇报 Director，启动完整实验矩阵
- v8 final eval G3a > 1.10 → 启动 v8b (two-stage: 冻结 baseline_v5 权重 + 只训 ACIS)，cuda:1 可用
- cuda:1 当前空闲 → 如果 early eval 信号好，可提前准备 v8b 代码/config 作为 backup；或跑 seed variation

### 5. 🎯 战略上下文
**核心结论链**：IMM margin maximization 机制有效（G1=64x, G2=+47pp, G4=0.32 全 PASS）→ 但共享 LoRA 导致 margin_loss 梯度损伤 backbone 权重（G3a=1.91x）→ v8 dual detach 是最小改动的修复 → 如果 v8 G3a ≤ 1.10，IMM 核心假设完全验证。

**最容易判断错的事**：
- v8 的 G1/G2 可能下降（ACIS 只在 detached features 上学习），不要因为 G1 从 64x 降到比如 5x 就判 FAIL——只要 ≥2x 就 PASS
- 不要混淆 G3a/G3b/G3c：G3a (bypass-ACIS) 是 MVP gate，G3b (soft) 和 G3c (hard) 是论文指标
- train loss 和 eval loss 有 ~10x 差距（D018 教训），不要用 train loss 预判 G3
- `evaluate.py` 对 baseline 用 random importance scores（不是 ACIS），这是设计如此不是 bug
- D023 说双轨并行 v8a+v8b，但实际只启动了 v8a（registry 名 `mvp_imm_anchor_v8`）。cuda:1 空闲是一个资源纪律问题，应尽快利用


---
